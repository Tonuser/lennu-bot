import discord
from discord.ext import commands
import time
import queue
import asyncio
import random
import re


class DataController:
    bot = None
    users = {}
    emoji = {
        "0": "0⃣",
        "1": "1⃣",
        "2": "2⃣",
        "3": "3⃣",
        "4": "4⃣",
        "5": "5⃣",
        "6": "6⃣",
        "7": "7⃣",
        "8": "8⃣",
        "9": "9⃣"
    }

    def __init__(self, bot):
        self.bot = bot
        bot.add_cog(self)

        for y in bot.get_all_emojis():
            self.emoji[y.name] = y

    # async def on_message(self, message):

    class User:
        def __init__(self):
            last_message = ""