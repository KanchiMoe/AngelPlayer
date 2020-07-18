'''
This file contains all of the commands the bot has.
'''

import random
import discord
import mybot
import botvars

@mybot.bot.command()
async def ping(ctx):
    await ctx.send(':stopwatch: Pong!')

@mybot.bot.command(aliases=['commands', 'command'])
async def help2(ctx):
    embed=discord.Embed(title="Command list", description="**Here is a list of all the commands:**", color=0x2ECC71)
    embed.add_field(name="Image commands:", value=f"{mybot.CmdPrefix}blush\n{mybot.CmdPrefix}bored\n{mybot.CmdPrefix}compliment\n{mybot.CmdPrefix}cry" \
        f"\n{mybot.CmdPrefix}cuddle\n{mybot.CmdPrefix}cute\n{mybot.CmdPrefix}dab\n{mybot.CmdPrefix}dance\n{mybot.CmdPrefix}excited\n{mybot.CmdPrefix}goodmorning" \
        f"\n{mybot.CmdPrefix}handshake\n{mybot.CmdPrefix}hide\n{mybot.CmdPrefix}highfive\n{mybot.CmdPrefix}holdhands\n{mybot.CmdPrefix}hug\n{mybot.CmdPrefix}kiss" \
        f"\n{mybot.CmdPrefix}laugh\n{mybot.CmdPrefix}lolihug\n~~{mybot.CmdPrefix}meme~~\n{mybot.CmdPrefix}nani\n{mybot.CmdPrefix}nini\n{mybot.CmdPrefix}nod\n{mybot.CmdPrefix}nom" \
        f"\n{mybot.CmdPrefix}pat\n{mybot.CmdPrefix}pirate\n{mybot.CmdPrefix}poke\n{mybot.CmdPrefix}pout\n{mybot.CmdPrefix}respect\n{mybot.CmdPrefix}scared\n{mybot.CmdPrefix}share" \
        f"\n~~{mybot.CmdPrefix}ship~~\n{mybot.CmdPrefix}shrug\n{mybot.CmdPrefix}sip\n{mybot.CmdPrefix}smack\n{mybot.CmdPrefix}smile\n{mybot.CmdPrefix}smug\n" \
        f"{mybot.CmdPrefix}wasted\n{mybot.CmdPrefix}wave", inline=True)
    embed.add_field(name="Misc. commands", value=f"{mybot.CmdPrefix}help\n{mybot.CmdPrefix}sourcecode", inline=True)
    await ctx.send(embed=embed)

@mybot.bot.command(aliases=['source', 'code'])
async def sourcecode(ctx):
    embed = discord.Embed(title="The bot's source code", color=0x2ECC71,
                          description="The source code for this bot is open source and is available on Github.\nhttps://github.com/ChiyoOsaka/AngelPlayer")
    await ctx.send(embed=embed)

#@mybot.bot.command(aliases=['bug', 'bugs', 'suggest'])
#async def suggestions(ctx):
#    pass

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

@mybot.bot.command(aliases=['stare'])
async def glare(ctx):
    ReqImg = "Glare"
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

@mybot.bot.command()
async def insult(ctx):
    template = random.choice(botvars.InsultTemplates)
    await ctx.send(template)

@mybot.bot.command()
async def compliment(ctx):
    template = random.choice(botvars.ComplimentTemplates)
    await ctx.send(template)
