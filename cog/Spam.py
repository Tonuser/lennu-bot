import discord
from discord.ext import commands
import time
import queue
import asyncio
import random
import re


class SpamDetector:
    bot = None
    data = None

    def __init__(self, bot, data_controller):
        self.bot = bot
        bot.add_cog(self)
        self.data = data_controller

    async def on_message(self, message):
        if str(message.author) in self.data.users:
            if str(self.data.users[str(message.author)].last_message) == str(message.content) and \
                            len(str(message.content)) > 0:
                await self.bot.delete_message(message)
        else:
            raise Exception("Unknown user " + str(message.author))