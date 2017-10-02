import discord
from discord.ext import commands
import time
import queue
import asyncio
import random
import re


class DataController:
    client = None
    users = {}

    def __init__(self, client):
        self.client = client

    async def handle_message(self,message):
        print("new message")

    class User:
        def __init__(self):
            last_message = ""