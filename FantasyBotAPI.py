#PuzzleBot API

import discord
from discord.ext import commands
from discord import DMChannel
import logging
from pathlib import Path
import json
import typing

en = '{"playing": "RAID!"}'
fr = '{"playing": "RAID!"}'
lang = json.loads(en)

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

bot = commands.Bot(command_prefix='?', case_insensitive=True)
bot.remove_command('help')
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print("RAID!!!")
    await bot.change_presence(activity=discord.Game(name=lang["playing"]))

bot.run("Nzg0NDc4NzI0OTY3NjI4ODQx.X8p4vg.rxQcX5ByvNmcaxgFIDOVNbOEcnw")