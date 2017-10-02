import discord
from discord.ext import commands


class LevelSystem:
    """Ayy lmao dude"""
    bot = None
    data = None
    levels = {}

    def __init__(self, bot, data_controller):
        self.bot = bot
        bot.add_cog(self)
        self.data = data_controller

    def add_level(self, name, min_chars):
        self.levels[name] = self.Level(min_chars)

    async def on_message(self, message):
        if str(message.channel) in self.levels:
            if self.levels[str(message.channel)].is_valid(message.content) is False:
                await self.bot.send_message(
                    message.author,
                    "Su sõnum ei vastanud kanali " + str(message.channel) + " reeglitele: \n```" +
                    message.content + "```")
                await self.bot.delete_message(message)

    class Level:
        def __init__(self, min_chars):
            self.min_chars = min_chars

        def is_valid(self, content):
            if len(content) < self.min_chars:
                return False

            return True
