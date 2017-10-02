import discord
from discord.ext import commands
import time
import queue
import asyncio
import random
import re


class Mandunu:
    """Ayy lmao dude"""
    bot = None
    data = None

    # 0 = is, -1 = starts with, 1 = ends with, 2 = contains
    pos = [
        ["meeldi", -1], ["armas", -1], ["nunnu", -1], ["beaut", -1],
        ["sexy", -1], ["hea", 0], ["häs", -1], ["good", 0], ["nice", 0],
        ["like", 0], ["äraproov", -1], ["mittegei", -1],
        ["imeli", -1], ["kepi", -1], ["kepp", -1], ["ma", 0], ["olen", -1],
        ["am", 0], ["mull", -1], ["pan", -1], ["taht", -1], ["tahan", -1],
        ["ilus", -1], ["okei", -1], ["hea", -1], ["tahab", -1], ["jää", -1],
        ["edu", -1], ["kivistu", -1], ["käitu", 2], ["kõva", 2], ["olen", 2],
        ["nice", 0], ["suude", -1], ["suudl", -1],
        ["lakk", -1], ["vött", -1], ["võtt", -1],
        ["neel", -1], ["im", 0], ["love", -1], ["sobi", -1],
        ["huvita", -1], ["võrguta", -1], ["on", 0], ["olen", -1],
        ["suckin", -1]
    ]
    neg = [
        ["tapp", -1], ["tapa", -1], ["poo", -1], ["puua", -1], ["köi", -1],
        ["nöör", -1], ["ahi", 0], ["ahj", -1], ["gaas", -1], ["gas", 0],
        ["war", 0], ["race", -1], ["kike", -1], ["juu", -1], ["rõve", -1],
        ["vastik", -1], ["ilge", -1], ["surm", -1], ["sure", -1],
        ["oled", 0], ["are", 0], ["dislike", 0], ["hate", -1], ["ew", -1],
        ["ei", 0], ["paha", -1], ["päh", -1], ["nais", -1],
        ["kole", -1], ["vihk", -1], ["nais", -1], ["ravi", 2]
    ]
    gay = [
        ["mees", 0], ["mehe", 2], ["gei", -1], ["pede", -1], ["homo", -1],
        ["seksuaal", 1], ["munn", -1], ["peenis", -1], ["munad", -1],
        ["trap", -1], ["suhu", -1], ["neel", -1], ["sperm", -1],
        ["lähene", -1], ["kõva", 2], ["seks", -1], ["man", -1],
        ["gay", -1], ["sexual", 1], ["penis", -1], ["benis", -1],
        ["dick", -1], ["cock", -1], ["wom", -1], ["blowjob", 0],
        ["erect", -1], ["sex", -1], ["mehi", -1], ["mehed", -1],
        ["trukk", -1], ["nuss", -1], ["pers", -1], ["imeda", -1],
        ["imema", -1], ["suck", -1], ["mittegei", -1], ["äraproov", -1],
        ["9gag", -1], ["reddit", -1], ["kiim", -1], ["pepp", -1],
        ["pepu", -1], ["fetis", -1], ["fetiš", -1], ["fetish", -1], ["kooselu", -1],
        ["cum", 2], ["türa", -1], ["toitaine", 2], ["iphone", 0],
        ["kikki", 0], ["silit", 2], ["anaal", 2],
        ["anal", 2], ["noku", 2], ["till", -1], ["bumhole", -1],
        ["ass", -1], ["dildo", -1], ["anus", -1], ["kristl", -1]
    ]

    def __init__(self, bot, data_controller):
        self.bot = bot
        bot.add_cog(self)
        self.data = data_controller

    async def on_message(self, message):
        """docstring"""
        if message.server is not None:
            author = message.server.get_member(message.author.id)

            gay_level = self.get_gay(message.content)
            if "mandunu" in [y.name.lower() for y in message.author.roles] or gay_level != 0:
                await self.bot.add_reaction(
                    message, self.data.emoji["pede2ratus"])
                await self.bot.add_reaction(
                    message, "\N{REGIONAL INDICATOR SYMBOL LETTER G}")
                await self.bot.add_reaction(
                    message, "\N{REGIONAL INDICATOR SYMBOL LETTER E}")
                await self.bot.add_reaction(
                    message, "\N{REGIONAL INDICATOR SYMBOL LETTER I}")
                await self.bot.add_reaction(
                    message, "\N{RAINBOW}")
                await self.bot.add_reaction(
                    message, self.data.emoji[str(min(round(gay_level * 6), 9))])
                await self.bot.add_reaction(
                    message, self.data.emoji[str(0)])


    def get_gay(self, content):
        content = content.lower()

        def kw_inword(word, keyword):
            return keyword in word

        def kw_swword(word, keyword):
            return word.startswith(keyword)

        def kw_ewword(word, keyword):
            return word.endswith(keyword)

        def kw_isword(word, keyword):
            return word is keyword

        func = {
            -1: kw_swword,
            0: kw_isword,
            1: kw_ewword,
            2: kw_inword
        }

        total = 0
        count = len(re.findall(r'\w+', content))
        words = re.findall(r'\w+', content)

        emo = 0.05

        for word in words:
            for y in self.gay:
                if func[y[1]](word, y[0]):
                    total += 1

            for y in self.pos:
                if func[y[1]](word, y[0]):
                    emo += 1

            for y in self.neg:
                if func[y[1]](word, y[0]):
                    emo -= 1

        if count:
            gay = total / (count / 5) * (emo * 0.5)
            print("gay: " + str(gay) + " c:" + str(total / count) + " emo " + str(emo))

            if gay > 0.15:  # total / count >= 0.1 and emo >= 0:
                return gay  # True
            else:
                return 0  # False
        else:
            return 0  # False
