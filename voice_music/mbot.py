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
    await channel.send("Sup Dummy! Beep beep!")
###########################################################################
@Bot.command()
async def h(ctx):
    await ctx.send("Music Bot Commands (/h for this menu): \n /play songname-goes-here to add to queue \n /skip to play next song \n /q to see the queue\n /pause and /res to toggle pause and \n /clear stops player and clears queue \n /dc to kick me out of voice channels \n\n queue stuck? try /skip")
###########################################################################
token = ""
with open("toke.n") as file:
    token= file.read()
Bot.run(token)
###########################################################################
