import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

@bot.command(name="median", help="gives you median")
async def median(A, ctx):
    m = len(A)
    A.sort()
    if m % 2 == 0:
        med1 = A[m//2]
        med2 = A[m//2 - 1]
        med = (med1 + med2)/2
    else:
        med = A[m//2]
    await ctx.send(med)

bot.run(TOKEN)
