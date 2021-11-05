- You can run a lot of Linux commands and other scripts from discord as well as return file output. 
  This folder doesn't have a fully working/tested bot, just a bunch of snippets of examples.



- This block shows three defined user commands, .help, .weather., and .botstat.
  .weather and .botstat both run a script that writes to a file, then returns that file
to the discord channel the request was sent from (context):

```python
import discord, subprocess
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
            "#react-for-roles to choose projects\n" +
            ".weather for current conditions near main campus\n" +
            ".botstat to ask how I am feeling\n")
    if message.content.startswith(".weather"):
        result = subprocess.check_output(['getwttr.sh']);
        time.sleep(2)
        channel = message.channel
        await channel.send(open('weather.txt').read())
    if message.content.startswith(".botstat"):
        result = subprocess.check_output(['cputemp.sh']);
        time.sleep(2)
        channel = message.channel
        await channel.send(open('cpu.tmp').read())
```
- Here are some examples of commands that use context (ctx) to simplify referencing the channel you're talking to:

```python
import discord
from discord.ext import commands
client = commands.Bot(command_prefix=".")
@client.event
async def on_ready():
    print(f"logged in as {client.user}")
@client.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! {ctx.author.mention}")
@client.command()
async def ping(ctx):
    await ctx.channel.send(f"Pong {round(client.latency*1000)} ms")
```
