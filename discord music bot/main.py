import discord
from discord.ext import commands
import os

from help_cog import Help_cog
from music_cog import music_cog

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(Help_cog(bot))


bot.run("MTA1NzMxMzIxNjI0MzQzNzcwOA.GUh0td.TPPy4MnaalUIzxykzM_-ToyoybUJQx51KA3Mho")
