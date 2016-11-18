import discord
from discord.ext import commands
import random
import asyncio
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
@asyncio.coroutine
def add(left : int, right : int):
    """Adds two numbers together."""
    yield from bot.say(left + right)

@bot.command()
@asyncio.coroutine
def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        yield from bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    yield from bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
@asyncio.coroutine
def choose(*choices : str):
    """Chooses between multiple choices."""
    yield from bot.say(random.choice(choices))

@bot.command()
@asyncio.coroutine
def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        yield from bot.say(content)

@bot.command()
@asyncio.coroutine
def joined(member : discord.Member):
    """Says when a member joined."""
    yield from bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
@asyncio.coroutine
def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        yield from bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
@asyncio.coroutine
def _bot():
    """Is the bot cool?"""
    yield from bot.say('Yes, the bot is cool.')

bot.run('token')
