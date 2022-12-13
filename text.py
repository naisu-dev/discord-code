import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def code(ctx,code):
    await ctx.message.delete()
    if code == "naisuさんnaisu":
        await ctx.author.send("^^")

bot.run(TOKEN)