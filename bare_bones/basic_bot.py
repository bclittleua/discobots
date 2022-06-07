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
client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
###########################################################################
#Command Format #1, using context(ctx)
@client.event
async def on_ready():
    print(f"logged in as {client.user}\n\n")
    chanID = "Your channel_ID here"
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.") #NOTE: this sends to a specified channel, chanID

#Conversely, the context (ctx) data captures which user sent what and from where
#without having to track all those ids:
@client.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! {ctx.author.mention}") 
    #ctx.author is the user that sent the command and replies with @username (.mention)

@client.command()
async def ping(ctx): #built-in funtion to get your ping, neat
    await ctx.channel.send(f"Pong {round(client.latency*1000)} ms")
    
@client.command()
async def quote(ctx): #this one just reads and returns a file
      await ctx.channel.send(open('/path/to/desired/file.txt').read())
      
      #WARNING: the file path above is a linux format! for WINDOWS use the following:
      await ctx.channel.send(open('C:\Users\YOUR!-USERNAME\Desktop\another_folder\file.txt').read())
###########################################################################
#Commmand Format #2, commands as a response to @client.event
#aka, when the bot detects a match in chat it fires commands as a response
#think: IF this THEN that AND that_other
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
