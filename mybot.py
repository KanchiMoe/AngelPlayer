'''
This file contains the global "bot" variable
'''

import logging
from discord.ext import commands

bot = commands.Bot(command_prefix='++')
CmdPrefix = bot.command_prefix
LOGGER = logging.getLogger('AngelPlayer')
LOGGER.setLevel(logging.INFO)
