import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

BOT_DESC = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
BOT_INTENTS = discord.Intents.all()
BOT_CLIENT = commands.Bot(command_prefix='$$', description=BOT_DESC, intents=BOT_INTENTS, help_command=None)
