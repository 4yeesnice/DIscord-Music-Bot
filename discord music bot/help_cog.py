import discord
from discord.ext import commands

class Help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """

```

Комманды:
/help - показывает все доступные комманды
/p <ключевое слово или же ссылка> - находит песню с ютуба и проигрывает в голосовом канале в котором вы находитесь
/q - показывает все песни находящиеся в очереди
/skip - пропускает песню играющую в голосовом канале
/clear - останавливает песню и очищает очередь
/leave - отключает бота с голосового канала
/pause - останавливает играющую песню или продолжает проигрывание если песня уже была в паузе
/resume - продолжает проигрывание песни находящуюся в паузе
негры пидорасы

```

"""
        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bit.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)

    

    @commands.command(name='help', help="Показывает все доступные комманды")
    async def help(self, ctx):
        await ctx.send(self.help_message)
    
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)