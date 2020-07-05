import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='++')
CmdPrefix = bot.command_prefix

@bot.command()
async def ping(ctx):
    await ctx.send(':stopwatch: Pong!')

@bot.command(aliases=['commands', 'command'])
async def help2(ctx):
    embed=discord.Embed(title="Command list", description="**Here is a list of all the commands:**", color=0x2ECC71)
    embed.add_field(name="Image commands:", value=f"{CmdPrefix}blush\n{CmdPrefix}bored\n{CmdPrefix}compliment\n{CmdPrefix}cry" \
        f"\n{CmdPrefix}cuddle\n{CmdPrefix}cute\n{CmdPrefix}dab\n{CmdPrefix}dance\n{CmdPrefix}excited\n{CmdPrefix}goodmorning" \
        f"\n{CmdPrefix}handshake\n{CmdPrefix}hide\n{CmdPrefix}highfive\n{CmdPrefix}holdhands\n{CmdPrefix}hug\n{CmdPrefix}kiss" \
        f"\n{CmdPrefix}laugh\n{CmdPrefix}lolihug\n{CmdPrefix}meme\n{CmdPrefix}nani\n{CmdPrefix}nini\n{CmdPrefix}nod\n{CmdPrefix}nom" \
        f"\n{CmdPrefix}pat\n{CmdPrefix}pirate\n{CmdPrefix}poke\n{CmdPrefix}pout\n{CmdPrefix}respect\n{CmdPrefix}scared\n{CmdPrefix}share" \
        f"\n{CmdPrefix}ship\n{CmdPrefix}shrug\n{CmdPrefix}sip\n{CmdPrefix}smack\n{CmdPrefix}smile\n{CmdPrefix}smugspank\n" \
        f"{CmdPrefix}wasted\n{CmdPrefix}wave", inline=True)
    embed.add_field(name="Misc. commands", value=f"{CmdPrefix}help\n{CmdPrefix}sourcecode", inline=True)
    await ctx.send(embed=embed)

@bot.command(aliases=['source', 'code'])
async def sourcecode(ctx):
    embed=discord.Embed(title="The bot's source code", color=0x2ECC71,
                        description="The source code for this bot is open source and is available on Github.")
    await ctx.send(embed=embed)

@bot.command(aliases=['bug', 'bugs', 'suggest'])
async def suggestions(ctx):
    pass

bot.run('xxx')


