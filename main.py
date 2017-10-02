from discord.ext import commands
from Lennu import Lennu

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description='aylmao xd')
lennu = None

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

    global lennu
    lennu = Lennu(bot)

bot.run('token')