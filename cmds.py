'''
This file contains all of the commands the bot has.
'''

import random
import json
import discord
import mybot

@mybot.bot.command()
async def ping(ctx):
    await ctx.send(':stopwatch: Pong!')

@mybot.bot.command(aliases=['commands', 'command'])
async def help2(ctx):
    embed=discord.Embed(title="Command list", description="**Here is a list of all the commands:**", color=0x2ECC71)
    embed.add_field(name="Image commands:", value='\n'.join((f'{mybot.CmdPrefix}{command}' for comand in COMMANDS)), inline=True)
    embed.add_field(name="Misc. commands", value=f"{mybot.CmdPrefix}help\n{mybot.CmdPrefix}sourcecode", inline=True)
    await ctx.send(embed=embed)

@mybot.bot.command(aliases=['source', 'code'])
async def sourcecode(ctx):
    embed = discord.Embed(title="The bot's source code", color=0x2ECC71,
                          description="The source code for this bot is open source and is available on Github.\nhttps://github.com/ChiyoOsaka/AngelPlayer")
    await ctx.send(embed=embed)

async def command_doer(ctx):
    '''Does the commands'''
    img = random.choice(COMMANDS[ctx.command.name]['links'])
    embed_colour = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=embed_colour)
    embed.set_image(url=img['link'])
    await ctx.send(embed=embed)

with open('imagevars.json', 'r') as handle:
    COMMANDS = json.load(handle)
for command in COMMANDS:
    mybot.bot.command(name=command)(command_doer)
