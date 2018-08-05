#**************************************************************************** #
#                                                                              #
#                                                             |\               #
#    Dungeon-Master.py                                  ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2018/05/29 10:00:02 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2018/07/04 20:17:28 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #

import re
import random
import asyncio
import aiohttp
from py_expression_eval import Parser
import discord
from discord.ext.commands import Bot
import strawpoll
import requests
import youtube_dl

BOT_PREFIX = ("!")
f = open('Token.txt', 'r')
TOKEN = f.read().rstrip()
f.close()

bot = Bot(command_prefix = BOT_PREFIX, description='A bot that does a whole host of things that Jeremy works on in his free time.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

def rollFunction(a, i):
    frontMath = ''
    parser = Parser()
    a.replace(" ", "")
    a=a.split('D', 1)
    amt = a[0]
    try:
        frontMath = amt[amt.index('+')+1:]
        amt = amt[amt.rindex('+')+1:]
    except ValueError:
        pass
    if amt=='':
        amt=1
    a[0] = frontMath+str(amt)
    amt = int(amt)
    if amt<=0:
        return "amtError"
    cut = str(a[1])
    dice = int(re.split('(\D+)', cut)[0])
    if dice<=1:
        return "diceError"
    math = re.split('(\D+)', cut)[1:]
    math=''.join(math)
    if frontMath!='':
        math=frontMath+math
    roll=0
    rolls = []
    final=''
    for x in range(0, amt):
        roll = random.randint(1, dice)
        rolls.append(str(roll))
    rolls = '+'.join(rolls)
    final = "("+rolls+")"+math
    return final

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Dungeon-Master", description="Use this bot for making dice rolls, doing math, creating straw polls, answering questions, or to bug Jeremy to add more features.\nLook at the full write up with !help or on Github at https://github.com/JeremyEudy/Dungeon-Master-Bot", color=0xeee657)
    embed.add_field(name="Author", value="Fascist Stampede")
    embed.add_field(name="Server count", value="{len(bot.guilds)}")
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=458438661378277379&permissions=36849728&scope=bot")
    await ctx.send(embed=embed)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Dungeon-Master", description="This bot does some stuff, here's a list:", color=0xeee657)
    embed.add_field(name="!greet", value="Greets the user", inline=False)
    embed.add_field(name="!m X + Y + Z", value="Solves a math problem of any length (addition, subtraction, multiplication, division).\nAlso able to solve more advanced math. A comprehensive list is available at https://github.com/AxiaCore/py-expression-eval", inline=False)
    embed.add_field(name="!r iDj+math", value="Roll i dice with j sides, then perform arithmetic with the results.", inline=False)
    embed.add_field(name="!eightball *question*", value="Ask the bot a yes/no question that it will answer with advanced machine learning (or random choices).", inline=False)
    embed.add_field(name="!strawpoll {title} [Option 1] [Option 2] [Option 3] [Option n]", value="Generates a strawpoll based on the given options. Allows more than one choice, and only one vote per user.", inline=False)
    embed.add_field(name="!suggest *suggestion*", value="Submit a suggestion to a suggestion box. Jeremy checks the box once a week.", inline=False)
    embed.add_field(name="!info", value="Gives information about the bot.", inline=False)
    embed.add_field(name="!help", value="You're lookin' at it.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def greet(ctx):
	await ctx.send(":smiley: :wave: Hello, there "+ctx.message.author.mention)

@bot.command()
async def suggest(ctx, *args):
    counter = 0
    suggestion = '{}'.format(' '.join(args))
    server = str(ctx.guild.name)
    suggestionFile = server+"_SuggestionBox.txt"
    file = open(suggestionFile, "a+")
    for line in file:
        if ctx.message.author.mention in line: counter+=1
    if counter >= 10:
        await ctx.send("I think you've submitted enough suggestions for right now... Try again later.")
    else:
        await ctx.send("Thank you for your suggestion!")
        file.write(ctx.message.author.mention+": "+suggestion)
    file.close()
'''
@bot.command()
async def play(ctx, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await yield from self.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()
'''
@bot.command()
async def m(ctx, *args):
    a = '{}'.format(''.join(args))
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
async def r(ctx, *args):
    a = '{}'.format(''.join(args))
    func=""
    parser = Parser()
    a=a.upper()
    count = a.count('D')
    for i in range(0, count):
        func+=str(rollFunction(a, i))
    if "amtError" in func:
        await ctx.send(ctx.message.author.mention+", you messed up your dice amounts my dude.")
        return
    if "diceError" in func:
        await ctx.send(ctx.message.author.mention+", you messed up your dice sizes my dude.")
        return
    func=str(func)
    final = str(int(parser.parse(func).evaluate({})))
    await ctx.send(ctx.message.author.mention+": `"+func+"` = "+final)

@bot.command()
async def eightball(ctx, *args):
    a = '{}'.format(' '.join(args))
    responses = ["It is certain.", "As I see it, yes.", "It is decidedly so.", "Without a doubt.", 
                 "Outlook good.", "Most likely", "Yes.", "Yes - definitely.", "You may rely on it.", 
                 "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", 
                 "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", 
                 "My sources say no.", "Outlook not so good.", "Very doubtful."]
    choice = random.randint(1, len(responses))
    await ctx.send(ctx.message.author.mention+": "+responses[choice])

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
        return "Please make sure you are using the format '!strawpoll {title} [Option1] [Option2] [Option 3]'"

    except KeyError:
        return "Please make sure you are using the format '!strawpoll {title} [Option1] [Option2] [Option 3]'"


bot.run(TOKEN)
