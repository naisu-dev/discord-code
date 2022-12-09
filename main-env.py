import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command()
async def code(ctx, code):
  await ctx.message.delete()
  user = await bot.fetch_user(ctx.author.id)
  if code == "naisuさんnaisu":
    await user.send("^^")


bot.run(TOKEN)
