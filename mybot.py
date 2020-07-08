'''
This file contains the global "bot" variable
'''

from discord.ext import commands

bot = commands.Bot(command_prefix='++')
CmdPrefix = bot.command_prefix
