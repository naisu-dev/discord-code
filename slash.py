import discord
from discord import app_commands
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
  print("ログインしました")
  await tree.sync()

@tree.command(name="code")
async def code(interaction: discord.Interaction, code: str):
  if code == "naisuさんnaisu":
    await interaction.user.send("^^")

bot.run(TOKEN)