from discord.ext import commands
import discord
import asyncio

from cog.DataController import DataController
from cog.Mandunu import Mandunu
from cog.LevelSystem import LevelSystem
from cog.Spam import SpamDetector

class Lennu:
    bot = None

    def __init__(self, bot):
        self.bot = bot
        bot.add_cog(self)

        data_controller = DataController(bot)
        spam_detector = SpamDetector(bot, data_controller)
        level_system = LevelSystem(bot, data_controller)
        level_system.add_level("esimene_tase", 70)
        level_system.add_level("teine_tase", 140)
        level_system.add_level("kolmas_tase", 200)
        level_system.add_level("neljas_tase", 280)
        mandunu = Mandunu(bot, data_controller)


    async def on_message(self, message):

        await self.bot.process_commands(message)
