import discord

import global_objects as GO

AB_SERVER = 933781308289712178 

ROLE_IDS = {
    'aahq': 933187649143980064,
    'bf': 933187568944685076,
    'guild': 1008455039884468244,
    'recruit': 933187488053334022,
}

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
    await log_channel.send(f":robot: | Autopromotions started by <@{interaction.user.id}>. Conducting start-up validation checks.")
    await log_channel.send(f":mag: | Checking for AAHQ, Battlefront, Guild and Recruit roles.")

    guild = GO.BOT_CLIENT.get_guild(AB_SERVER)

    for k, v in ROLE_IDS.items():
        r = guild.get_role(v)
        if r is not None:
            await log_channel.send(f":white_check_mark | Role {r} exists.")
        else:
            await log_channel.send(f":x: | Role {r} does not exist.")

