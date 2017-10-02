import discord
from discord.ext import commands
import time
import queue
import asyncio
import random
import re


class SpamDetector:
    client = None
    data_controller = None

    def __init__(self, client, data_controller):
        self.client = client
        self.data_controller = data_controller