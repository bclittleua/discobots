###########################################################################
###########################################################################
##########                         _      _____  ##########################
##########   ___  __ _ _ __ ___   /_\     \_   \ ##########################
##########  / __|/ _` | '_ ` _ \ //_\\     / /\/ ##########################
##########  \__ \ (_| | | | | | /  _  \_/\/ /__  ##########################
##########  |___/\__,_|_| |_| |_\_/ \_(_)____(_) ##########################
##############################################################2021#########
###########################################################################
import discord, sys, os, subprocess, time
from discord.ext import commands
###########################################################################
client = commands.Bot(command_prefix="/",intents=discord.Intents.all())
###########################################################################
@client.event
async def on_ready():
    print(f"logged in as {client.user}\n\n")
    chanID = Your-channel_ID-here-no-quotes
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.") #NOTE: this sends to a specified channel, chanID
###########################################################################
# Commands as a response to @client.event
# aka, when the bot detects a match in chat it fires commands as a response
# can chain these, think: IF this THEN that AND that_other
@client.event
async def on_message(message):
    if message.content.startswith("/custom_query"):
        channel = message.channel
        await channel.send("custom_response")
        
    if message.content.startswith("/run_a_script"):
        result = subprocess.check_output(['/path/to/your/custom_script.sh']);
        time.sleep(2)
        channel = message.channel
        await channel.send(open('/path/to/your/script_output.txt').read())
###########################################################################
token = ""
with open("tok.en") as file:
    token= file.read()
client.run(token)
###########################################################################
###########################################################################
