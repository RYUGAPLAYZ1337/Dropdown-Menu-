import discord as sanemijija   #made by sanemicodeZ
from discord.ext import commands , tasks#made by sanemicodeZ
#made by sanemicodeZ
import asyncio as SanemiXGhosty#made by sanemicodeZ
import random #made by sanemicodeZ
import os as samjija#made by sanemicodeZ
intents = sanemijija.Intents.all()#made by sanemicodeZ

sanemi = commands.Bot(command_prefix ='$',intents= intents)#made by sanemicodeZ
sanemi.remove_command('help') #used to remove default cmd provided by discord.py
@sanemi.event#made by sanemicodeZ
async def on_ready():
    print(f'Logged in as {sanemi.user}')#made by sanemicodeZ
async def load_extensions(bot):#made by sanemicodeZ
    for filename in samjija.listdir('./cogs'):#made by sanemicodeZ
        if filename.endswith('.py'):#made by sanemicodeZ
            try:#made by sanemicodeZ
                await   sanemi.load_extension(f'cogs.{filename[:-3]}')#made by sanemicodeZ
                print(f'Loaded extension: {filename}')#made by sanemicodeZ
            except Exception as e:#made by sanemicodeZ
                print(f'Failed to load extension {filename}: {e}')#made by sanemicodeZ
@sanemi.event
async def on_ready():#made by sanemicodeZ#made by sanemicodeZ
    await load_extensions(sanemi)#made by sanemicodeZ
async def start_bot():#made by sanemicodeZ
    await sanemi.start("#Yourtoken")

SanemiXGhosty.run(start_bot())#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ








#made by sanemicodeZ
#made by sanemicodeZ

#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ
#made by sanemicodeZ