import discord
from discord.ext import commands
import random
# randint is needed to generate random numbers.
from random import randint
import asyncio

# set description
description = '''Discord vor-bot based on https://github.com/Rapptz/discord.py'''
# create bot

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

commands_help = {"add": "Adds two numbers together", "joined": "Displays information about user"}

@bot.command()
@asyncio.coroutine
def commands():
    #display all the commands available
    for key, value in commands_help.items():
        yield from bot.say('{0}{1} = {2}{3}'.format('```', key, value, '```'))

# Adds two numbers together.
@bot.command()
@asyncio.coroutine
def add(left : int, right : int):
    yield from bot.say(left + right)

# Rolls a basic 1-6 dice.
@bot.command()
@asyncio.coroutine
def roll():
    result = randint(1,6)
    yield from bot.say(result)

# Chooses random item from given list of choices
@bot.command()
@asyncio.coroutine
def choose(*choices : str):
    yield from bot.say(random.choice(choices))

# Repeats a message given numbers of times
@bot.command()
@asyncio.coroutine
def repeat(times : int, content='repeating...'):
    for i in range(times):
        yield from bot.say(content)

# Displays information when a member joined
@bot.command()
@asyncio.coroutine
def joined(member : discord.Member):
    yield from bot.say('{0.name} joined in {0.joined_at}'.format(member))

# Says if user is cool
@bot.group(pass_context=True)
@asyncio.coroutine
def cool(ctx):
    if ctx.invoked_subcommand is None:
        yield from bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

'''@cool.command(name='bot')
@asyncio.coroutine
def _bot():
    """Is the bot cool?"""
    yield from bot.say('Yes, the bot is cool.')'''

bot.run('token')
