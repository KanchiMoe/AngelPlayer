import discord
import os

import global_objects as GO

AB_SERVER_ID = 933083666912014416
FILE_PATH = "./modules/autopromote/"

ROLES = {
    'AAHQ': {
        "role_id": 933187649143980064,
        "short_name": "aahq",
        "current_users": { },
        "new_users": { }
    },
    "Battlefront": {
        "role_id": 933187568944685076,
        "short_name": "bf",
        "current_users": { },
        "new_users": { }
    },
    "Guild": {
        "role_id": 1008455039884468244,
        "short_name": "guild",
        "current_users": { },
        "new_users": { }
    },
    "Recruit": {
        "role_id": 933187488053334022,
        "short_name": "recruit",
        "current_users": { },
        "new_users": { }
    }
}

MSGS = {
    'init': "Starting Autopromotions. Outputting logs to channel ID `{log_channel_id}` (<#{log_channel_id}>).",
    'idnotint': ":x: The ID you provided (`{log_channel_id}`) contains letters, symbols or spaces. Only numbers are allowed.",
    'start': ":robot: | Autopromotions started by <@{interaction.user.id}>. Conducting start-up validation checks.",
    'rolecheck': ":mag: | Checking for AAHQ, Battlefront, Guild and Recruit roles.",
    'rolenotexist': ':x: | Role "{role_name}" does not exist.',
    'roleexists': ':white_check_mark: | Role "{role_name}" exists.',
    'createrole': ' Please double check the role ID used in the code. ID: `{role_id}`',
    'fileexists': ':white_check_mark: | {each}.txt exists.',
    'filedoesntexist': ":x: | {each}.txt doesn't exist. Autopromotion can't continue without this file.",
    'fileckeck': ":mag: | Checking for data files."
}

@GO.BOT_CLIENT.tree.command(name="apwip",description="Promote users in Angel Beats! based on the most recent promotion data.")
async def apwip(interaction: discord.Interaction, log_channel_id: str):

    log_channel = await GetLogChannelObj(interaction, log_channel_id)
    await interaction.response.send_message(MSGS['init'].format(**locals(), **globals()))

    await log_channel.send(f"{MSGS['start']}".format(**locals(), **globals()))
    await log_channel.send(f"{MSGS['rolecheck']}".format(**locals(), **globals()))
    await CheckRolesExist(log_channel)

    await log_channel.send(f"{MSGS['fileckeck']}".format(**locals(), **globals()))
    await CheckFilesExist(log_channel)
    GetNewRoleUserIds()
    await LogUserContents(log_channel)



#
#   Spacing just for clarity while working
#

# Doing this cause https://github.com/Rapptz/discord.py/issues/9147
async def GetLogChannelObj(interaction: discord.Interaction, log_channel_id: str):
    if not log_channel_id.isnumeric():
        await interaction.response.send_message(MSGS['idnotint'].format(**locals(), **globals()))
        raise ValueError("foobar")
    else:
        return GO.BOT_CLIENT.get_channel(int(log_channel_id)) 

async def CheckRolesExist(log_channel) -> None:
    guild = GO.BOT_CLIENT.get_guild(AB_SERVER_ID)
    role_ids = { }

    for each in ROLES:
        role_ids[ROLES[each]['short_name']] = ROLES[each]['role_id']

    for role_name, role_id in role_ids.items():
        role = guild.get_role(role_id)
        if role is None:
            await log_channel.send(f"{MSGS['rolenotexist'] + MSGS['createrole']}".format(**locals(), **globals()))
            raise ValueError("role doesn't exist")
        else:
            await log_channel.send(f"{MSGS['roleexists']}".format(**locals(), **globals()))

async def CheckFilesExist(log_channel) -> None:
    FileList = ["aahq", "bf", "guild"] 

    for each in FileList:
        if os.path.exists(f"{FILE_PATH}{each}.txt"):
            await log_channel.send(f"{MSGS['fileexists']}".format(**locals(), **globals()))
        else:
            await log_channel.send(f"{MSGS['filedoesntexist']}".format(**locals(), **globals()))
            raise ValueError("file doesn't exist")
            # to do, autocreate file

def GetNewRoleUserIds():
    for each_role in ROLES:
        if each_role == "Recruit":
            continue
        else:
            with open(f"{FILE_PATH}{ROLES[each_role]['short_name']}.txt") as contents:
                ROLES[each_role]['new_users'] = {
                    int(each_line) for each_line in contents.read().split('\n') if each_line
                }

async def LogUserContents(log_channel):
    for each_role in ROLES:
        if each_role == "Recruit":
            continue
        else:
            if len(ROLES[each_role]['new_users']) == 0:
                await log_channel.send(f":warning: | {ROLES[each_role]['short_name']}.txt is empty. This might not be intentional.")
                # to do, add print statment
            else:
                await log_channel.send(f":printer: | {ROLES[each_role]['short_name']}.txt has content. Printing this to the console.")
