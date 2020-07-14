'''
This file contains all of the commands the bot has.
'''

import mybot, botvars
import random
import discord
from discord.ext import commands

@mybot.bot.command()
async def ping(ctx):
    await ctx.send(':stopwatch: Pong!')

@mybot.bot.command(aliases=['commands', 'command'])
async def help2(ctx):
    embed=discord.Embed(title="Command list", description="**Here is a list of all the commands:**", color=0x2ECC71)
    embed.add_field(name="Image commands:", value=f"{CmdPrefix}blush\n{CmdPrefix}bored\n{CmdPrefix}compliment\n{CmdPrefix}cry" \
        f"\n{CmdPrefix}cuddle\n{CmdPrefix}cute\n{CmdPrefix}dab\n{CmdPrefix}dance\n{CmdPrefix}excited\n{CmdPrefix}goodmorning" \
        f"\n{CmdPrefix}handshake\n{CmdPrefix}hide\n{CmdPrefix}highfive\n{CmdPrefix}holdhands\n{CmdPrefix}hug\n{CmdPrefix}kiss" \
        f"\n{CmdPrefix}laugh\n{CmdPrefix}lolihug\n~~{CmdPrefix}meme~~\n{CmdPrefix}nani\n{CmdPrefix}nini\n{CmdPrefix}nod\n{CmdPrefix}nom" \
        f"\n{CmdPrefix}pat\n{CmdPrefix}pirate\n{CmdPrefix}poke\n{CmdPrefix}pout\n{CmdPrefix}respect\n{CmdPrefix}scared\n{CmdPrefix}share" \
        f"\n~~{CmdPrefix}ship~~\n{CmdPrefix}shrug\n{CmdPrefix}sip\n{CmdPrefix}smack\n{CmdPrefix}smile\n{CmdPrefix}smug\n" \
        f"{CmdPrefix}wasted\n{CmdPrefix}wave", inline=True)
    embed.add_field(name="Misc. commands", value=f"{CmdPrefix}help\n{CmdPrefix}sourcecode", inline=True)
    await ctx.send(embed=embed)
 
@mybot.bot.command(aliases=['source', 'code'])
async def sourcecode(ctx):
    embed=discord.Embed(title="The bot's source code", color=0x2ECC71,
                        description="The source code for this bot is open source and is available on Github.")
    await ctx.send(embed=embed)
 
@mybot.bot.command(aliases=['bug', 'bugs', 'suggest'])
async def suggestions(ctx):
    pass

def EmbedMaker(ReqImg):
    ImgListName = "%sImgs" % ReqImg
    ImgList = getattr(botvars, ImgListName)
    Img = random.choice(ImgList)
    EmbedColour = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=EmbedColour)
    embed.set_image(url=Img)
    return embed

@mybot.bot.command()
async def blush(ctx):
    ReqImg = "Blush"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def bored(ctx):
    ReqImg = "Bored"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

#@mybot.bot.command()
#async def compliment(ctx):

@mybot.bot.command()
async def cry(ctx):
    ReqImg = "Cry"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def cuddle(ctx):
    ReqImg = "Cuddle"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def cute(ctx):
    ReqImg = "Cute"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def dab(ctx):
    ReqImg = "Dab"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def dance(ctx):
    ReqImg = "Dance"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def excited(ctx):
    ReqImg = "excited"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command(aliases=['gm'])
async def goodmorning(ctx):
    ReqImg = "Goodmorning"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def handshake(ctx):
    ReqImg = "Handshake"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def hide(ctx):
    ReqImg = "Hide"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def highfive(ctx):
    ReqImg = "Highfive"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def holdhands(ctx):
    ReqImg = "Holdhands"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def hug(ctx):
    ReqImg = "Hug"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def kiss(ctx):
    ReqImg = "Kiss"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def laugh(ctx):
    ReqImg = "Laugh"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def lolihug(ctx):
    ReqImg = "Lolihug"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def meme(ctx):
    ReqImg = "Meme"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def nani(ctx):
    ReqImg = "Nani"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command(aliases=['gn', 'night', 'goodnight'])
async def nini(ctx):
    ReqImg = "Nini"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def nod(ctx):
    ReqImg = "Nod"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def nom(ctx):
    ReqImg = "Nom"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command(aliases=['pet'])
async def pat(ctx):
    ReqImg = "Pat"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def pirate(ctx):
    ReqImg = "Pirate"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def poke(ctx):
    ReqImg = "Poke"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def pout(ctx):
    ReqImg = "Pout"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def respect(ctx):
    ReqImg = "Respect"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def scared(ctx):
    ReqImg = "Scared"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def share(ctx):
    ReqImg = "Share"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def ship(ctx):
    ReqImg = "Blush"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def shrug(ctx):
    ReqImg = "Shrug"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def sip(ctx):
    ReqImg = "Sip"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def smack(ctx):
    ReqImg = "Smack"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def smile(ctx):
    ReqImg = "Smile"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def smug(ctx):
    ReqImg = "Smug"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def spank(ctx):
    ReqImg = "Spank"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def wasted(ctx):
    ReqImg = "Wasted"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)

@mybot.bot.command()
async def wave(ctx):
    ReqImg = "Wave"
    embed=EmbedMaker(ReqImg)
    await ctx.send(embed=embed)
