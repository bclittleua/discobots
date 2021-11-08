#/usr/bin/env python3
###########################################################################
###########################################################################
##########                         _      _____  ##########################
##########   ___  __ _ _ __ ___   /_\     \_   \ ##########################
##########  / __|/ _` | '_ ` _ \ //_\\     / /\/ ##########################
##########  \__ \ (_| | | | | | /  _  \_/\/ /__  ##########################
##########  |___/\__,_|_| |_| |_\_/ \_(_)____(_) ##########################
#########################################################2021##############
###########################################################################
import discord
from discord.ext import commands
from music_cog import music_cog
###########################################################################
Bot = commands.Bot(command_prefix='/')
Bot.add_cog(music_cog(Bot))
###########################################################################
@Bot.event
async def on_ready():
    chanID = "YOUR CHANNEL_ID HERE"
    channel = Bot.get_channel(chanID) #send online status to private chan
    await channel.send("Online! Beep beep!")
###########################################################################
@Bot.command()
async def h(ctx):
    await ctx.send("Music Bot Commands (/h for this menu): \n "+
                   "/add songname-goes-here  to add a song to queue \n "+
                   "/pause and /resume       to toggle pause and \n "+
                   "/skip   to play next song \n "+
                   "/q or /np      to see the queue or now_playing\n\n "+
                   #/np requires music_cog1.py and npformater.sh
                   "/clear  stops playback and clears queue \n"+
                   "/dc     to kick bot out of voice channel \n\n"+
                   "/limits I'm not perfect and can't do some things \n\n"+
                   "queue stuck? try /skip")
###########################################################################
token = ""
with open("toke.n") as file:
    token= file.read()
Bot.run(token)
###########################################################################
