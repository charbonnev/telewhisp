# Telewhisp: Receives audio, transcribes it and sends them back through telegram

In progress!

Create a .env file with:  
* TOKEN=your_telegram_bot_token in the root folder (the folder where main.py is)
* LANGUAGE=language you want to transcribe

Run it with python3 main.py

Next steps:
Transcribe using whisper. Whisper must be installed and added to path before you can use this, please refer to this: [Whisper Github](https://github.com/openai/whisper).
