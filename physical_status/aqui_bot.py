###########################################################################
###########################################################################
##########                         _      _____  ##########################
##########   ___  __ _ _ __ ___   /_\     \_   \ ##########################
##########  / __|/ _` | '_ ` _ \ //_\\     / /\/ ##########################
##########  \__ \ (_| | | | | | /  _  \_/\/ /__  ##########################
##########  |___/\__,_|_| |_| |_\_/ \_(_)____(_) ##########################
###########################################################2021############
###########################################################################
import discord
import sys, os, subprocess, time
from discord.ext import tasks
###########################################################################
client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
###########################################################################
@client.event
async def on_ready():
    print(f"logged in as {client.user}\n\n")
    looper.start()
    chanID = "Your channel_id goes here"
    channel = client.get_channel(chanID)
    await channel.send("Bot online.")
###########################################################################
#Read the presence flag stats, 1 or 0, and change bot status accordingly
@tasks.loop(seconds=30)
async def looper():    
    with open("/path/to/your/flag/status/file", "r") as file:
        flag = file.read().replace("\n", "")
    if flag == '0': #0 = afk = do not disturb
        await client.change_presence(status=discord.Status.dnd)
    if flag == '1': #1 = here = online
        await client.change_presence(status=discord.Status.online)
###########################################################################
token = ""
with open("toke.n") as file:
    token= file.read()
Bot.run(token)
###########################################################################
