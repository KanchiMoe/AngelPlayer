import discord
from discord import app_commands
import logging
import global_objects as GO

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Error handling for slash commands
@GO.BOT_CLIENT.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    InvokedBy, InvokedByID = interaction.user, interaction.user.id
    InvokedIn, InvokedInID = interaction.guild, interaction.guild_id
    cmd = interaction.command.name 

    logging.error(f"{InvokedBy} ({InvokedByID}) tried to use the command \"{cmd}\" in \"{InvokedIn}\" ({InvokedInID})")
    await interaction.response.send_message(error, ephemeral=True)
    
    
    logging.error(error)

    #if isinstance(error, app_commands.BotMissingPermissions):
    #to do
  

# Error handling for prefix commands
@GO.BOT_CLIENT.event
async def on_command_error(ctx, error):
    await ctx.reply(error, ephemeral=True)
    logging.error(error)










@GO.BOT_CLIENT.event
async def on_command_completion(ctx):
    InvokedBy, InvokedByID = ctx.author, ctx.author.id
    InvokedIn, InvokedInID = ctx.guild, ctx.guild.id
    cmd = ctx.command.name
    logging.info(f"{InvokedBy} ({InvokedByID}) ran the prefix command \"{cmd}\" in \"{InvokedIn}\" ({InvokedInID}).")

def Can_I_Run_Commands_Here(guild_id: int) -> bool:
    if guild_id == 933781308289712178:
        return True
    else:
        return False









# replaced by async def on_command_completion(ctx):
# def PrefixCommandRanSucess(ctx, cmd) -> None:
#     InvokedBy, InvokedByID = ctx.author, ctx.author.id
#     InvokedIn, InvokedInID = ctx.guild, ctx.guild.id
#     logging.info(f"{InvokedBy} ({InvokedByID}) ran the prefix command \"{cmd}\" in \"{InvokedIn}\" ({InvokedInID}).")

