import discord
import numpy as np
import random
from discord.ext import commands
from discord.utils import get
import os
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = ',', intents = intents)
