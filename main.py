import discord
from discord.ext import commands
import asyncio
import time
import Theme
import Mandunu
import DataController
import Spam


#client = discord.Client()
client = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description='aylmao xd')
client.add_cog(Theme.ThemeController(client))
theme_controller = None
data_controller = None
mandunu = None



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

    # theme_controller = Theme.ThemeController(client)
    global mandunu, data_controller
    data_controller = DataController.DataController(client)

    spam_detector = Spam.SpamDetector(client, data_controller)
    mandunu = Mandunu.Mandunu(client, data_controller)


@client.event
async def on_message(message):
    """docstring"""

    await data_controller.handle_message(message)


    limit = 0
    if str(message.channel) == 'kolmas_tase':
        limit = 140
    elif str(message.channel) == 'teine_tase':
        limit = 70

    if len(message.content) < limit and len(message.attachments) == 0:
        await client.send_message(
            message.author,
            "Su sõnum oli alla " + str( limit ) + " tähemärgi: \n```" + message.content + "```")
        await client.delete_message(message)


    await mandunu.handle(message)

    await client.process_commands(message)

client.run('MzU4NzcyOTA0NDYyMzg1MTU0.DJ9U4w.YHCqBU0XaAJZnOalIrZzg1zaqng')