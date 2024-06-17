import discord
from discord.ext import commands
import os
from config import *
intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents) 


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event 
async def on_ready():
    await load()
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="leo"))
    try:
        synced = await bot.tree.sync()
        print(f'Entegre edilen slash Komut sayısı: {len(synced)}')
    except Exception as e:
        print(e)

bot.run(token)