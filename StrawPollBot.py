# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    StrawPollBot.py                                    ------| \----          #
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

TOKEN = 'MzIxMTQ3OTQ3NDE5MDQxODA1.De7t1w.wJteQA3xi5WhAh-G7yq2W33VIH8'

client = Bot(command_prefix = BOT_PREFIX)

@client.event
async def on_message(message):
# we do not want the bot to reply to itself
    if message.author == client.user:
        return
        
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(name='Strawpoll',
                description="Creates a poll for users to vote on",
                brief="Exercise democracy.",
                aliases=['strawpoll', 'StrawPoll', 'straw-poll', 'Straw-poll', 'Straw-Poll'],
                pass_context=True)
async def strawpoll(context):
#This shit costs money. I'm out.


client.run(TOKEN)   
