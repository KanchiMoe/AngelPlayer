import discord

import global_objects as GO

START_MSG = "Starting Autopromotions. Outputting logs to channel ID `{log_channel_id}` (<#{log_channel_id}>)."
START_ERR = ":x: The ID you provided (`{log_channel_id}`) contains letters, symbols or spaces. Only numbers are allowed."

@GO.BOT_CLIENT.tree.command(name="apwip",description="Promote users in Angel Beats! based on the most recent promotion data.")
async def apwip(interaction: discord.Interaction, log_channel_id: str):

    # Doing this cause https://github.com/Rapptz/discord.py/issues/9147
    if not log_channel_id.isnumeric():
        await interaction.response.send_message(START_ERR.format(**locals(), **globals()))
    else:
        await interaction.response.send_message(START_MSG.format(**locals(), **globals()))

    log_channel = GO.BOT_CLIENT.get_channel(int(log_channel_id))
    await log_channel.send(f"Autopromotions started by {interaction.user.id}. Conducting start-up validation checks.")


