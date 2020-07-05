from discord.ext import commands
bot = commands.Bot(command_prefix='++')

@bot.command()
async def ping(ctx):
    await ctx.send(':stopwatch: Pong!')

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Command list", description="**Here is a list of all the commands:**", color=#2ECC71)
    embed.add_field(name="Image commands:", value="foobar", inline=True)
    embed.add_field(name="Misc. commands", value="+help\n+sourcecode", inline=True)
    await ctx.send(embed=embed)

@bot.command(aliases=['source', 'code'])
async def sourcecode(ctx):