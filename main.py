import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio
import logging
import random
import discord.emoji
import discord.user
import discord.activity
import discord.member
import socketserver
import discord.channel
from discord import Member
from discord import Emoji
from discord.ext.commands import has_permissions, MissingPermissions, MissingAnyRole, MissingRole, has_any_role, has_role
import re
import io
import os
import json
import datetime
from json import load
import re
import time

with open("./Json/config.json", encoding="utf8")as f:
    d = load(f)
    TOKEN = d["token"]
    prefix = d["prefix"]
    mainmess = d["Main.py"]

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print(mainmess)

for filename in os.listdir('./komendy'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.{filename[:-3]}')

for filename in os.listdir('./eventy'):
    if filename.endswith('.py'):
        client.load_extension(f'eventy.{filename[:-3]}')

for filename in os.listdir('./komendy./custom'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.custom.{filename[:-3]}')

for filename in os.listdir('./komendy./clear'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.clear.{filename[:-3]}')

for filename in os.listdir('./komendy./kick'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.kick.{filename[:-3]}')

for filename in os.listdir('./komendy./mute'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.mute.{filename[:-3]}')

for filename in os.listdir('./komendy./warn'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.warn.{filename[:-3]}')

for filename in os.listdir('./komendy./nickname'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.nickname.{filename[:-3]}')

for filename in os.listdir('./eventy./gamestatus'):
    if filename.endswith('.py'):
        client.load_extension(f'eventy.gamestatus.{filename[:-3]}')

for filename in os.listdir('./eventy./notification'):
    if filename.endswith('.py'):
        client.load_extension(f'eventy.notification.{filename[:-3]}')

for filename in os.listdir('./komendy./role'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.role.{filename[:-3]}')

for filename in os.listdir('./komendy./ban'):
    if filename.endswith('.py'):
        client.load_extension(f'komendy.ban.{filename[:-3]}')

client.run(TOKEN)
