import discord
from discord import app_commands
from discord.ext import commands
import typing

import global_objects as GO
import master_logic as ML

@GO.BOT_CLIENT.command()
async def ping(ctx):
    try:
        await ctx.send(':stopwatch: Pong!')
        ML.PrefixCommandRanSucess(ctx, cmd="ping")
    except Exception as e:
        print(e)

@GO.BOT_CLIENT.command(aliases=['source', 'code'])
async def sourcecode(ctx):
    await ctx.send("The source code for this bot is open source is can be found on Github: <https://github.com/KanchiMoe/AngelPlayer>")
    ML.PrefixCommandRanSucess(ctx, cmd="sourcecode")



# @commands.command()
# async def test(ctx, arg):
#     await ctx.send(arg)
#     master_logic.PrefixCommandRanSucess(ctx, cmd="test")


# @commands.command()
# async def getguild(ctx) -> None:
#     if master_logic.Can_I_Run_Commands_Here(ctx.message.guild.id):
#         await ctx.send(f"I'm allowed to talk in {ctx.message.guild.id}")
#     else:
#         await ctx.send(f"I'm not allowed to talk in {ctx.message.guild.id}")





@GO.BOT_CLIENT.tree.command(name="demob",description="No arguments.")
async def slash_demo_b(interaction: discord.Interaction):
    await interaction.response.send_message(f"I'm slash command demo B. {interaction.user.id}", ephemeral=True)

@GO.BOT_CLIENT.tree.command(name="democ",description="1 argument, \"arg\".")
async def slash_demo_c(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(f"I'm slash command demo C with args: {arg}", ephemeral=True)

@GO.BOT_CLIENT.tree.command(name="demod", description="Options, required")
@app_commands.describe(option="This is a description of what the option means")
@app_commands.choices(option=[
        app_commands.Choice(name="Option 1", value="1"),
        app_commands.Choice(name="Option 2", value="2")
    ])
async def slash_demo_d(interaction: discord.Interaction, option: app_commands.Choice[str]):
    await interaction.response.send_message(f"I'm slash command demo D, option: {option.value}", ephemeral=True)

@GO.BOT_CLIENT.tree.command(name="demoe", description="Option, optional.")
@app_commands.describe(option="This is a description of what the option means")
@app_commands.choices(option=[
        app_commands.Choice(name="Option 1", value="1"),
        app_commands.Choice(name="Option 2", value="2")
    ])
async def slash_demo_e(interaction: discord.Interaction, option: typing.Optional[app_commands.Choice[str]]):
    await interaction.response.send_message(f"I'm slash command demo E, option: {option.value}", ephemeral=True)

@GO.BOT_CLIENT.tree.command(name="demof", description="2 Options, both required")
@app_commands.describe(optiona="This is a description of optionA")
@app_commands.choices(optiona=[
        app_commands.Choice(name="Option 1", value="1"),
        app_commands.Choice(name="Option 2", value="2")
    ])
@app_commands.describe(optionb="This is a description of optionB")
@app_commands.choices(optionb=[
        app_commands.Choice(name="Option 3", value="3"),
        app_commands.Choice(name="Option 4", value="4")
    ])
async def slash_demo_f(interaction: discord.Interaction, optiona: app_commands.Choice[str], optionb: app_commands.Choice[str]):
    await interaction.response.send_message(f"I'm slash command demo E, optionA: {optiona.value}, optionB: {optionb.value}", ephemeral=True)

@GO.BOT_CLIENT.hybrid_command(name="demog", with_app_command= True, description="Slash and prefix command")
async def slash_demo_g(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply("I'm slash command demo G.")

@GO.BOT_CLIENT.hybrid_command(name="demoh", with_app_command= True, description="Slash and prefix command, but you need administrator")
@commands.has_permissions(administrator=True)
async def slash_demo_h(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply("I'm slash command demo H, and you have administrator permissions!")

@GO.BOT_CLIENT.hybrid_command(name="demoi", with_app_command= True, description="Slash and prefix command, but bot needs administrator")
@commands.bot_has_permissions(administrator=True)
async def slash_demo_i(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply("I'm slash command demo I, and I have administrator permissions!")

@GO.BOT_CLIENT.hybrid_command(name="demoj", with_app_command= True, description="Slash and prefix command, but you need a role")
@commands.has_any_role("aaa")
async def slash_demo_j(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply("I'm slash command demo J, and you have the right role!")


##########################

@GO.BOT_CLIENT.tree.command(name="demok",description="Bot needs admin")
@app_commands.checks.bot_has_permissions(administrator=True)
async def slash_demo_k(interaction: discord.Interaction):
    await interaction.response.send_message("I'm slash command demo K, and you have the right role! ", ephemeral=True)


















# @GO.BOT_CLIENT.tree.command(name="demog",description="Only in 1 server.")
# @app_commands.guilds(933781308289712178)
# async def slash_demo_g(interaction: discord.Interaction):
#     await interaction.response.send_message("I'm slash command demo G ", ephemeral=True)

@GO.BOT_CLIENT.command()
async def b(ctx):
    await ctx.send("I'm B")
    # $$b

@GO.BOT_CLIENT.group(name="cparent", invoke_without_command=True)
async def cparent(ctx):
    await ctx.send("I'm C parent!")
    # $$cparent

@cparent.command()
async def cchilda(ctx):
    await ctx.send("I'm C-A, a child of C!")
    # $$cparent cchilda

@cparent.command()
async def cchildb(ctx):
    await ctx.send("I'm C-B, a child of C!")
    # $$cparent cchildb

@cparent.command()
async def cchildc(ctx):
    await ctx.send("I'm C-C, a child of C!")
    # $$cparent cchildc

@GO.BOT_CLIENT.command()
@commands.has_any_role("aaa")
async def d(ctx):
    await ctx.send("I'm D, you need a role to run me. Role as a text string.")

@GO.BOT_CLIENT.command()
@commands.has_any_role(1027747728735866910)
async def e(ctx):
    await ctx.send("I'm D, you need a role to run me. Role as an ID.")

@GO.BOT_CLIENT.command()
@commands.has_any_role(1027747728735866910, "aaa")
async def f(ctx):
    await ctx.send("I'm D, you need a role to run me. Role as ID and text string.")

@GO.BOT_CLIENT.command()
@commands.guild_only()
async def g(ctx):
    await ctx.send("I'm G. I can only be ran in a server and not DMs!")
