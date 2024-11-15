"""
Simple Bot to reply to Telegram voice messages with the text transcription.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Send the bot an audio, it will reply with the transcription.
run it with python3 main.py
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from dotenv import load_dotenv
import logging
import os
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import whisper
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Load the Whisper model
# Choose "tiny", "base", "small", "medium", or "large"
model = whisper.load_model("medium")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
# if you want to see everything, put logging.INFO
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()} I'm an audio transcribing bot! Send me an audio and I'll reply with the transcription.",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Send me and audio and I'll reply with the transcription.")

async def echo_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Save the voice message to the current folder, transcribes it and sends it back."""
    voice_file = await update.message.voice.get_file()
    audio_path = f"{voice_file.file_id}.ogg"
    await voice_file.download_to_drive(audio_path)
    # Transcribe the audio
    result = model.transcribe(audio_path)
    await update.message.reply_text(result["text"])


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on receiving a voice message, send it back
    application.add_handler(MessageHandler(filters.VOICE, echo_voice))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
