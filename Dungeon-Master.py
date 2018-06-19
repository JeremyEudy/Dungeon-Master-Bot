# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    Dungeon-Master.py                                  ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2018/05/29 10:00:02 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2018/05/29 10:21:04 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #

import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
f = open('Token.txt', 'r')
TOKEN = f.read().rstrip()

bot = Bot(command_prefix = BOT_PREFIX, description='A bot that does a whole host of things that Jeremy works on in his free time.')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def greet(ctx):
	await ctx.send(":smiley: :wave: Hello, there!")

#@bot.command(name='Strawpoll',
#		description="Creates a poll for users to vote on",
#		brief="Exercise democracy.",
#		aliases=['strawpoll', 'StrawPoll', 'straw-poll', 'Straw-poll', 'Straw-Poll'],
#		pass_context=True)

bot.run(TOKEN)
