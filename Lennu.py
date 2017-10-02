from discord.ext import commands
import discord
import asyncio

from cog.DataController import DataController
from cog.Mandunu import Mandunu

class Lennu:
    bot = None

    def __init__(self, bot):
        self.bot = bot
        bot.add_cog(self)

        data_controller = DataController(bot)
        mandunu = Mandunu(bot, data_controller)

    async def on_message(self, message):

        await self.bot.process_commands(message)
