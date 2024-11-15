# Telewhisp: Receives audio, transcribes it and sends them back through telegram

In progress!

![Demo](assets/demo.gif)

Create a .env file with:  
* TOKEN=your_telegram_bot_token in the root folder (the folder where main.py is)

Run it with python3 main.py

You must install whisper:

```
pip install git+https://github.com/openai/whisper.git
pip install ffmpeg-python
```

And ffmpeg:
```
sudo apt update && sudo apt install ffmpeg
```

If you need additional help, please refer to this: [Whisper Github](https://github.com/openai/whisper).
