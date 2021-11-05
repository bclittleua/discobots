# How to use
1. Copy mbot.py and music_cog.py to same folder
2. Copy your bot token to toke.n in same folder
3. Run mbot.py to start bot

# Dependencies for Linux users (I use a RPi):
1. requires python 3.4 or better
2. install ffmpeg with apt: ```apt-get install ffmpeg```
3. install ffmpeg support for python with: ```pip install ffmpeg```
4. install discord for python with: ```pip install discord```
5. install voice_client support for python with: ```python -m pip install -U discord.py[voice]```

# Windows users:
I'm not sure what is different in Windows other than installing and referencing FFmpeg...
- ¯\\_(ツ)_/¯
- ¯\\_(ツ)_/¯
- do steps 3, 4, and 5 for linux users.
#
# Set up your bot at https://discord.com/developers/applications/  
- no intents required, disable them in bot settings
- the only scope required for OAuth2 is 'bot'
- admin permission to make things easy, permissions=8
- add bot to server with https://discord.com/api/oauth2/authorize?client_id=00000000000000000000&permissions=8&scope=bot
  
  be sure to replace the 00000000000000 with your own client_id

