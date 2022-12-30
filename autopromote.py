import discord
import os

import global_objects as GO

AB_SERVER_ID = 933083666912014416
AB_ATEVERYONE = 933083666912014416
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
    'fileckeck': ":mag: | Checking for data files.",
    'doublerolecheck': ":mag: | Checking for double roles. (eg: AAHQ and Battlefront, or Battlefront and Guild, etc.)",
    'nodoublecheckerrors': ":white_check_mark: | Everyone in the server only has 1 role (AAHQ or Battlefront or Guild or Recruit).",
    'doublecheckerrors': ":no_entry: | Members with more than 1 promotable role have been detected. These must be fixed before Autopromotions can continue.",
    'aaa': ":warning: | {each_member} (<@{each_member.id}>) has more than 1 promotable role: {', '.join(ListOfDoubleRoles)}."
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

    await log_channel.send(f"{MSGS['doublerolecheck']}".format(**locals(), **globals()))
    await CheckUsersForDoubleRoles(log_channel)

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

def GetNewRoleUserIds() -> None:
    for each_role in ROLES:
        if each_role == "Recruit":
            continue
        else:
            with open(f"{FILE_PATH}{ROLES[each_role]['short_name']}.txt") as contents:
                ROLES[each_role]['new_users'] = {
                    int(each_line) for each_line in contents.read().split('\n') if each_line
                }

async def LogUserContents(log_channel) -> None:
    for each_role in ROLES:
        if each_role == "Recruit":
            continue
        else:
            if len(ROLES[each_role]['new_users']) == 0:
                await log_channel.send(f":warning: | {ROLES[each_role]['short_name']}.txt is empty. This might not be intentional.")
                # to do, add print statment
            else:
                await log_channel.send(f":printer: | {ROLES[each_role]['short_name']}.txt has content. Printing this to the console.")

async def CheckUsersForDoubleRoles(log_channel):
    guild = GO.BOT_CLIENT.get_guild(AB_SERVER_ID)
    autopromote_roles = set()

    for each_role in ROLES:
        autopromote_roles.add(ROLES[each_role]['role_id'])

    # Get all of a members roles
    for each_member in guild.members:
        members_roles_ids = set()
        for each_role in each_member.roles:
            members_roles_ids.add(each_role.id)
            
        # Remove @everyone from the list
        members_roles_ids.remove(AB_ATEVERYONE)

        check_output_ids = members_roles_ids.intersection(autopromote_roles)
        if len(check_output_ids) > 1:
            DoubleRoleCheckErrors = 1
            ListOfDoubleRoles = [ ]

            for each_role in check_output_ids:
                role_ids = guild.get_role(each_role)
                role_names = role_ids.name
                ListOfDoubleRoles.append(role_names)
            await log_channel.send(f":warning: | {each_member} (<@{each_member.id}>) has more than 1 promotable role: {', '.join(ListOfDoubleRoles)}.")
     
    if DoubleRoleCheckErrors > 0:
        await log_channel.send(f"{MSGS['doublecheckerrors']}".format(**locals(), **globals()))
        raise ValueError("foo")
    else:
        await log_channel.send(f"{MSGS['nodoublecheckerrors']}".format(**locals(), **globals()))



        # if DoubleRoleCheckErrors > 0:
        #     
        # else:
        #     await log_channel.send(f"{MSGS['nodoublecheckerrors']}".format(**locals(), **globals()))















    

    #for each_role in ROLES

    # for each_member in guild.members:
    #     for each_role in each_member.roles:
    #         if each_role.id == 933085846549200897:
    #             print(f"{each_member}")


# guild = GO.BOT_CLIENT.get_guild(AB_SERVER_ID)







#[<Role id=933083666912014416 name='@everyone'>, <Role id=933187568944685076 name='Battlefront Member'>, <Role id=933120465592016928 name='Server Booster'>, <Role id=935594354918187099 name='Translator-kun'>, <Role id=933149343752544306 name='Kanade'>, <Role id=933085846549200897 name='Student Council'>, <Role id=935297556223762493 name='Faculty committee (a)'>, <Role id=935299833370144828 name='Acting President'>]