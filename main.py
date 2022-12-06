import discord
from discord.ext import commands

TOKEN = '<token>'
bot = commands.Bot(command_prefix='!')

@bot.command()
async def code(ctx,code):
    await ctx.message.delete()
    user = await bot.fetch_user(ctx.author.id)
    if code == "naisuさんnaisu":
        await user.send("^^")


bot.run(TOKEN)
