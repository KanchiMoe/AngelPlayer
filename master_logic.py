import discord
from discord import app_commands
import logging
import global_objects as GO

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

INVOKED_INFO = "{InvokedBy} ({InvokedByID}) tried to use the command \"{cmd}\" in \"{InvokedIn}\" ({InvokedInID})"
BUT_ERROR = " but encountered an error: {error}"

# Error handling for slash commands
@GO.BOT_CLIENT.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    InvokedBy, InvokedByID = interaction.user, interaction.user.id
    InvokedIn, InvokedInID = interaction.guild, interaction.guild_id
    cmd = interaction.command.name 

    logging.error((INVOKED_INFO + BUT_ERROR).format(**locals(), **globals()))

    if isinstance(error, app_commands.BotMissingPermissions):
        #import pdb; pdb.set_trace()
        BotMissingPermissions = []
        for EachMissingPermission in error.missing_permissions:
            BotMissingPermissions.append(EachMissingPermission.capitalize().replace("_", " "))

        await interaction.response.send_message(f":exclamation: Bot requires the following permission(s) to run this command: {', '.join(BotMissingPermissions)}", ephemeral=True) 

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
    logging.info((INVOKED_INFO).format(**locals(), **globals()))

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

