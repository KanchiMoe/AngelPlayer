import logging
import discord
import global_objects as GO
import maincommands

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

@GO.BOT_CLIENT.event
async def on_ready():
    # Login
    logging.info(f"Logged in as \"{GO.BOT_CLIENT.user}\" (ID: {GO.BOT_CLIENT.user.id})")  

    # Slash command sync
    SlashCommandSynched = await GO.BOT_CLIENT.tree.sync()
    logging.info(f"Synched {len(SlashCommandSynched)} slash command(s).")

    # Bot ready
    logging.info(f"Bot ready.")

@GO.BOT_CLIENT.tree.command(name="demoa",description="Slash command demo A")
async def slash_demo_a(interaction: discord.Interaction):
    await interaction.response.send_message("I'm slash command demo A ", ephemeral=True)


@GO.BOT_CLIENT.command()
async def a(ctx):
    await ctx.send("I'm A")

def main():
    #maincommands.init(BOT_Client)
    GO.BOT_CLIENT.run(GO.DISCORD_BOT_TOKEN)

if __name__ == '__main__':
    main()
