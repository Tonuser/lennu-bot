import discord
from discord.ext import commands
import time
import queue
import asyncio
import random
import re


class SpamDetector:
    bot = None
    data_controller = None

    def __init__(self, bot, data_controller):
        self.bot = bot
        self.data_controller = data_controller