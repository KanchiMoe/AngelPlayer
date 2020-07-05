import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='++')

@bot.command()
async def ping(ctx):
    await ctx.send(':stopwatch: Pong!')

@bot.command(aliases=['commands'])
async def help2(ctx):
    embed=discord.Embed(title="Command list", description="**Here is a list of all the commands:**", color=0x2ECC71)
    embed.add_field(name="Image commands:", value="foobar", inline=True)
    embed.add_field(name="Misc. commands", value="+help\n+sourcecode", inline=True)
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