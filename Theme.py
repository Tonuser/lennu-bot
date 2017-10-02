import discord
from discord.ext import commands
import time
import queue
import asyncio


class ThemeController:
    """Ayy lmao dude"""
    channels = {}
    channel_links = {}
    client = None
    help = "theme has the following subcommands\n" \
           "add {channel} {theme} {link} - add a theme to a channel\n" \
           "list - lists all the themes"

    def __init__(self, client):
        self.client = client

        channels = client.get_all_channels()

        for channel in channels:
            self.channels[str(channel)] = []
            self.channel_links[str(channel)] = channel

        self.client.loop.create_task(self.handle_themes())

    async def handle_themes(self):
        for key in self.channels:

            pq = queue.PriorityQueue()

            for theme in self.channels[key]:
                pq.put((theme.date_s, theme))

            if pq.empty() == False:
                print("Channel: " + str(key))

            while pq.empty() == False:
                el = pq.get()[1]
                if time.time() - el.date_s > 10: #43200
                    embed = discord.Embed(
                        title="Lennu™",
                        description="Lennu ülesanne on esitada talle ette antud teemasid, mis tuleks läbi arutada.",
                        color=0x00ff00,
                        url=""
                    )
                    embed.set_author(
                        name=el.author,
                        url="",
                        icon_url=el.author.avatar_url
                    )
                    embed.set_image(
                        url="https://i.imgur.com/Xn0bnNK.png"
                    )
                    await self.client.send_message(
                        self.channel_links[key],
                        embed=embed)
                    await self.client.send_message(
                        self.channel_links[key],
                        "Teema: _**" + el.theme + "**_\n" + el.link)

                    el.date_s = time.time()

                print(str(el.author) +
                      " - " + str(el.theme) +
                      " - " + str(round(time.time() - theme.date_s)) + " - " + str(el.link))

        await asyncio.sleep(2)  # task runs every 10 seconds
        self.client.loop.create_task(self.handle_themes())

    async def add_theme(self, channel, author, theme, link):
        # To add - verify user permissions

        self.channels[channel].append(Theme(author, theme, link))

    @commands.group(pass_context=True, no_pm=True)
    async def theme(self, ctx):
        """Themes are topics to discuss in different channels"""
        if ctx.invoked_subcommand is None:

            await self.client.send_message(
                ctx.message.author,
                "Invalid subcommand. ?help theme for more information"
            )
            await self.client.delete_message(ctx.message)

    @theme.command(pass_context=True, no_pm=True)
    async def add(self, ctx, channel: str, theme: str, link: str):
        """
        {channel} {theme} {link} Add a theme to a specific channel to be displayed
        :param channel: Name of the channel
        :type channel: str
        :param theme: A short description of the theme
        :type theme: str
        :param link: Link to an overview of the theme
        :type link: str
        """

        if channel in self.channels:
            if theme != "" and link != "":
                await self.add_theme(channel, ctx.message.author, theme, link)
                await self.client.send_message(
                    ctx.message.author,
                    "Sinu lisatud teema:"
                )
                embed = discord.Embed(
                    title="Lennu™",
                    description="Lennu ülesanne on esitada talle ette antud teemasid, mis tuleks läbi arutada.",
                    color=0x00ff00,
                    url=""
                )
                embed.set_author(
                    name=ctx.message.author.name,
                    url="",
                    icon_url=ctx.message.author.avatar_url
                )
                embed.set_image(
                    url="https://i.imgur.com/Xn0bnNK.png"
                )
                await self.client.send_message(ctx.message.author, embed=embed)
                await self.client.send_message(
                    ctx.message.author,
                    "Teema: _**" + theme +"**_\n" + link)
                await self.client.delete_message(ctx.message)
            else:
                await self.client.send_message(
                    ctx.message.author,
                    "Invalid theme / link"
                )
        else:
            await self.client.send_message(
                ctx.message.author,
                "Invalid channel name"
            )

    @theme.command(pass_context=True, no_pm=True)
    async def list(self, ctx):
        """Lists all themes"""
        s = "List\n```Markdown\n"
        c = 1
        for key in self.channels:
            pq = queue.PriorityQueue()

            for theme in self.channels[key]:
                pq.put((theme.date_s, theme))

            if pq.empty() == False:
                s += "  " + str(c) + ". " + str(key) + "\n"
                c += 1

            while pq.empty() == False:
                el = pq.get()[1]
                s += "    # " + str(el.theme) + " - " + str(el.author) + " [](" + str(el.link) + ")\n"
        s += "```"
        await self.client.send_message(ctx.message.author, s)
        await self.client.delete_message(ctx.message)


class Theme:
    author = None
    theme  = None
    link   = None
    date_c = None # Date Created
    date_s = None # Date shown

    def __init__(self, author, theme, link):
        self.author = author
        self.theme  = theme
        self.link   = link
        self.date_c = time.time()
        self.date_s = time.time()

    def __gt__(self, theme2):
        return self.date_s > theme2.date_s
