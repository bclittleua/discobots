#
# to add record to reactrole.json via discord:
# .reactrole [emoji] @rolename message-to-be-displayed [another emoji , optional]
# use that command to find out the ids for emojis, messages, channels, etc

import discord
import json
import sys, os, subprocess, time
from discord.ext import commands

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x ['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])
                    await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x ['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])
                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

@client.command()
async def reactrole(ctx,emoji, role: discord.Role,*,message):
    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)
    with open('reactrole.json') as json_file:
        data = json.load(json_file)
        new_react_role = {
            'role_name':role.name,
            'role_id':role.id,
            'emoji':emoji,
            'message_id':msg.id
        }
        data.append(new_react_role)
    with open('reactrole.json','w') as j:
        json.dump(data,j,indent=4)



##SCRIPT KIDDIES##########################################################
#This little bit runs a script that dumps output of wttr.in to weather.txt
##########################################################################
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
            "#react-for-roles to choose projects\n" +
            ".weather for current conditions\n" +
    if message.content.startswith(".weather"):
        result = subprocess.check_output(['getwttr.sh']);
        time.sleep(2)
        channel = message.channel
        await channel.send(open('weather.txt').read())
                           
###Run the Bot:                           
token = ""
with open("toke.n") as file:
    token= file.read()
Bot.run(token)
