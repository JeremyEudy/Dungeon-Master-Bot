# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    Dungeon-Master.py                                  ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2018/05/29 10:00:02 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2018/06/19 18:44:37 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #

import random
import asyncio
import aiohttp
from py_expression_eval import Parser
import discord
from discord.ext.commands import Bot
import strawpoll
import requests

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
async def info(ctx):
    embed = discord.Embed(title="Dungeon-Master", description="Use this bot for making dice rolls, doing math, creating straw polls, or to bug Jeremy to add more features.", color=0xeee657)
    embed.add_field(name="Author", value="Fascist Stampede")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=458438661378277379&permissions=36849728&scope=bot")
    await ctx.send(embed=embed)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Dungeon-Master", description="This bot does some stuff, here's a list:", color=0xeee657)
    embed.add_field(name="!greet", value="Greets the user", inline=False)
    embed.add_field(name="!m X + Y + Z", value="Solves a math problem of any length (addition, subtraction, multiplication, division).\nAlso able to solve more advanced math. A comprehensive list is available at https://github.com/AxiaCore/py-expression-eval", inline=False)
    embed.add_field(name="!r # D M", value="Rolls a dice of size 'D' '#' times and adds a modifier of 'M', 'M' is optional.", inline=False)
    embed.add_field(name="!strawpoll", value="Generates a strawpoll based on the given options. Allows more than one choice, and only one vote per user.", inline=False)
    embed.add_field(name="!info", value="Gives information about the bot.", inline=False)
    embed.add_field(name="!help", value="You're lookin' at it.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def greet(ctx):
	await ctx.send(":smiley: :wave: Hello, there "+ctx.message.author.mention)

@bot.command()
async def m(ctx, a: str):
    if a=="pi":
        a=a.upper()

    elif a=="e":
        a=a.upper()

    else:
        a=a.lower()

    parser = Parser()
    exp = parser.parse(a).evaluate({})
    exp=str(exp)
    await ctx.send(ctx.message.author.mention+": "+a+" = "+exp)

@bot.command()
async def r(ctx, a: int, b: int, c: int = 0):
    roll=0
    rolls = []
    final=0
    if b>0:
        if a>0:
            for x in range(0, a):
                roll = random.randint(0, b)
                rolls.append(str(roll))
                final+=roll
        else:
            await ctx.send(ctx.message.author.mention+", you're not funny. Don't give Jeremy a headache.")
            return
    else:
         await ctx.send(ctx.message.author.mention+", you're not funny. Don't give Jeremy a headache.")
         return

    rolls = ' + '.join(rolls)
    if c!=0:
        final=str(final+a*c)
        c=str(c)
        await ctx.send(ctx.message.author.mention+": ("+rolls+") + "+c+" = "+final)
    else:
        final=str(final)
        await ctx.send(ctx.message.author.mention+": ("+rolls+") = "+final)

@bot.event
async def on_message(message):
    command_name = bot.command_prefix + 'strawpoll'
    messageContent = message.content
    if message.content.startswith(command_name):
        pollURL = await createStrawpoll(messageContent)
        await message.channel.send(pollURL)
    else:
        await bot.process_commands(message)

async def createStrawpoll(message):
    #gets the title of the poll
    first = message.find("{") + 1
    second = message.find("}")
    title = message[first:second]

    #gets the # of options and assigns them to an array
    newMessage = message[second:]
    loopTime = 0

    option = []
    for options in message:
        #get from } [option 1]
        #if newThis == -1:
        stillOptions = newMessage.find("[")
        if stillOptions != -1:
            if loopTime == 0:
                first = newMessage.find("[") + 1

                second = newMessage.find("]")
                second1 = second + 1
                option.append(newMessage[first:second])

                loopTime+=1
            else:
                newMessage = newMessage[second1:]
                first = newMessage.find("[") + 1
                second = newMessage.find("]")
                second1 = second + 1
                option.append(newMessage[first:second])
                loopTime+=1
    strawpollAPI = strawpoll.API()
    try:
        r = requests.post('https://www.strawpoll.me/api/v2/polls', json = {"title": title, "options": option[:(len(option)-1)], "multi": "true"}, headers={"Content Type": "application/json"})
        json = r.json()
        return "https://strawpoll.me/" + str(json["id"])


    except strawpoll.errors.HTTPException:
        return "Please make sure you are using the format '+strawpoll {title} [Option1] [Option2] [Option 3]'"

    except KeyError:
        return "Please make sure you are using the format '+strawpoll {title} [Option1] [Option2] [Option 3]'"


bot.run(TOKEN)
