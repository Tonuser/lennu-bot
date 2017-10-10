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

        for y in bot.get_all_members():
            self.users[str(y)] = self.User(y)

    async def on_message(self, message):
        if str(message.author) in self.users:
            member = self.users[str(message.author)]
            self.users[str(message.author)].last_message = member.message
            self.users[str(message.author)].message = str(message.content)
        else:
            raise Exception("Unknown user " + str(message.author))

    async def on_member_join(self, member):
        self.users[str(member)] = self.User(member)
        print("User joined")

    class User:
        def __init__(self, user):
            self.message = ""
            self.last_message = ""
            self.user = user
