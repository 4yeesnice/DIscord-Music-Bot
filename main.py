import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
from yt_dlp import YoutubeDL
#import all of the cogs


FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'}


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


async def connect(ctx):
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()

async def sending(ctx):
    await ctx.send('1')

#remove the default help command so that we can write out own
@bot.command(name='leave', pass_context = True)
async def disconnect(ctx):
    await ctx.voice_client.disconnect(force=True)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

#register the class with the bot


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('hello')

@bot.command(name='play')
async def play(ctx):
#    await connect(ctx)
#    source = discord.FFmpegPCMAudio(
#                                  executable="Discord Bot\\ffmpeg\\bin\\ffmpeg.exe",
#                                  source='BAKER_YA_MAKER_-_Cry_Of_Fear_66952382.mp3',
#                                 **FFMPEG_OPTIONS)
    
#    play = discord.VoiceClient.play(source = source)
#    await ctx.voice_client.play(source=discord.FFmpegPCMAudio(source='test.mp3', executable='ffmpeg\\bin\ffmpeg.exe'))
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\user\\Desktop\\Python Projects\\Discord Bot\\ffmpeg\\bin\\ffmpeg.exe", source="test.mp3"))
                        

bot.run('MTAzNTI1MTU2NTk2OTI5MzM5Mw.GR4DIx.HXM7F50GknlJomNWICFhPJYmmFm5jhZ9esj3IE')