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
    embed.add_field(name="Image commands:", value='\n'.join((f'{mybot.CmdPrefix}{command}' for command in COMMANDS)), inline=True)
    embed.add_field(name="Misc. commands", value=f"{mybot.CmdPrefix}help\n{mybot.CmdPrefix}sourcecode", inline=True)
    await ctx.send(embed=embed)

@mybot.bot.command(aliases=['source', 'code'])
async def sourcecode(ctx):
    embed = discord.Embed(title="The bot's source code", color=0x2ECC71,
                          description="The source code for this bot is open source and is available on Github.\nhttps://github.com/KanchiMoe/AngelPlayer")
    await ctx.send(embed=embed)

async def command_doer(ctx):
    '''Does the commands'''
    # Check if channel restricted
    cmd_name = ctx.command.name
    if 'allowed_channels' in COMMANDS[cmd_name]:
        if ctx.channel.id not in COMMANDS[cmd_name]['allowed_channels']:
            await ctx.send('Not allowed in this channel')
            return

    img = random.choice(COMMANDS[cmd_name]['links'])
    embed_colour = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=embed_colour)
    embed.set_image(url=img['link'])
    await ctx.send(embed=embed)

with open('imagevars.json', 'r') as handle:
    COMMANDS = json.load(handle)
for command in COMMANDS:
    if 'aliases' in COMMANDS[command]:
        mybot.bot.command(name=command, aliases=COMMANDS[command]['aliases'])(command_doer)
    else:
        mybot.bot.command(name=command)(command_doer)
