import discord
from discord.ext import commands
import random
# randint is needed to generate random numbers.
from random import randint
import asyncio
import json
from pprint import pprint

# set description
description = '''Discord vor-bot based on https://github.com/Rapptz/discord.py'''

#Keep token secret by reading it from a token file.
txt = open("token","r")
#Python adds new line when reading from a file. Strip it with strip().
bot_token = txt.read().strip()
#read the json file

def read_db(file):
    with open(file, 'r') as json_file:
        db = json.load(json_file)
        json_file.close()
        return db

database = read_db('database.json')
pprint(database)
# create bot
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

commands_help = {
    "commands": "Display available commands",
    "add": "Adds two numbers together",
    "choose": "Chooses random item from given list of choices",
    "repeat": "Repeats a message given numbers of times",
    "joined": "Displays information when a member joined",
    "flip": "Flips a coin",
    "rps": "Rock, paper, scissors",
    "rng": "Random number generator",
    "isboton": "Checks if bot is online",
    "reverse": "Reverse a string"
    }
#display all the commands available
@bot.command()
@asyncio.coroutine
def commands():

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

# Flips a coin.
@bot.command()
@asyncio.coroutine
def flip():

    result = randint(0,1)
    if result == 0:
        yield from bot.say('Heads')
    else:
        yield from bot.say('Tails')

# Rock, paper, scissor.
@bot.command()
@asyncio.coroutine
def rps():

    result = randint(0,2)
    if result == 0:
        yield from bot.say('Rock')
    elif result == 1:
        yield from bot.say('Paper')
    else:
        yield from bot.say('Scissor')

# Generates random number between 0 and given number.
@bot.command()
@asyncio.coroutine
def rng(number : int):

    result = randint(0, number)
    yield from bot.say(result)


# Checks if bot is online
@bot.command()
@asyncio.coroutine
def isboton():

    yield from bot.say("Beep, beep, boop, I'm online. Ready for your commands!")

# Reverse input
@bot.command()
@asyncio.coroutine
def reverse(string : str):

    reversed_str = ''.join(reversed(string))
    yield from bot.say(reversed_str)

'''
Database based commands
'''

# Assigns artificial points to a user
@bot.command()
@asyncio.coroutine
def gpoints(user, points):

    with open("database.json", "w+") as jsonFile:
        database['users'][user]["points"] += int(points)
        jsonFile.write(json.dumps(database))
        jsonFile.close()
    yield from bot.say('Added {0} points to {1}'.format(points, user))
# Removes points
@bot.command()
@asyncio.coroutine
def rpoints(user, points):

    with open("database.json", "w+") as jsonFile:
        database['users'][user]["points"] -= int(points)
        jsonFile.write(json.dumps(database))
        jsonFile.close()
    yield from bot.say('Removed {0} points from {1}'.format(points, user))
# Check leaderboards
@bot.command()
@asyncio.coroutine
def leaderboard():
    database = read_db('database.json')
    for key,val in database['users'].items():
        #print(key, "=>", val['points'])
        yield from bot.say('{0} => {1}'.format(key, val['points']))
#Start the bot
bot.run(bot_token)
