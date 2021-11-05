Dependencies for Linux users (I use a RPi):
- requires python3.4 or better
- install ffmpeg with apt: apt-get install ffmpeg
- install ffmpeg support for python with: pip install ffmpeg
- install discord for python with: pip install ffmpeg
- install voice_client support for python with: python -m pip install -U discord.py[voice]

-I'm not sure what is different in Windows other than the installation of ffmpeg...

Set up your bot at https://discord.com/developers/applications/  
- no intents required, disable them in bot settings
- admin permission to make things easy, permissions=8
- add bot to server with https://discord.com/api/oauth2/authorize?client_id=00000000000000000000&permissions=8&scope=bot
  be sure to replace the 00000000000000 with your own client_id

