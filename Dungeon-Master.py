# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    Dungeon-Master.py                                  ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2018/05/29 10:00:02 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2018/08/29 11:49:05 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #

import re
import operator as op
import random
import asyncio
import aiohttp
from py_expression_eval import Parser
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import strawpoll
import requests
import youtube_dl
from roller import *

BOT_PREFIX = ("/")
f = open('Token.txt', 'r')
TOKEN = f.read().rstrip()
f.close()

bot = commands.Bot(command_prefix = BOT_PREFIX, description='A bot that does a whole host of things that Jeremy works on in his free time.')
client = discord.Client()

british_insults = ['Tosser',
 'Wanker',
 'Slag',
 'No better than those Cheese Eating Surrender Monkeys',
 'Someone has Lost the plot.',
 'Daft Cow',
 'Arsehole',
 'Barmy',
 'Chav',
 'Dodgy',
 'Manky',
 'Minger',
 'Muppet',
 'Naff',
 'Nutter',
 'Pikey',
 'Pillock',
 'Plonker',
 'Prat',
 'Scrubber',
 'Trollop',
 'Uphill Gardener',
 'Twit',
 'Knob Head',
 'Piss Off',
 'Bell End',
 'Lazy Sod',
 'Skiver',
 'Knob Gobbler',
 'Wazzock',
 'Ninny',
 'Berk',
 'Airy-fairy',
 'Ankle-biter',
 'Arse-licker',
 'Arsemonger',
 'Chuffer',
 'You are Daft as a bush',
 "This one's Dead from the neck up",
 'Clearly your brain has gone to the dogs',
 'Ligger',
 'You are Like a dog with two dicks',
 'Mad as a bag of ferrets',
 'Maggot',
 'What a Mingebag',
 "This one's not Not batting on a full wicket",
 'You are Plug-Ugly',
 ]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Dungeon-Master", description="Use this bot for making dice rolls, doing math, creating straw polls, answering questions, or to bug Jeremy to add more features.\nLook at the full write up with !help or on Github at https://github.com/JeremyEudy/Dungeon-Master-Bot", color=0xeee657)
    embed.add_field(name="Author", value="Fascist Stampede")
    embed.add_field(name="Server count", value=len(bot.guilds))
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=458438661378277379&permissions=36849728&scope=bot")
    await ctx.send(embed=embed)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Dungeon-Master", description="This bot does some stuff, here's a list:", color=0xeee657)
    embed.add_field(name="/greet", value="Greets the user", inline=False)
    embed.add_field(name="/sponge", value="SpOnGe", inline=False)
    embed.add_field(name="/m X + Y + Z", value="Solves a math problem of any length (addition, subtraction, multiplication, division).\nAlso able to solve more advanced math. A comprehensive list is available at https://github.com/AxiaCore/py-expression-eval", inline=False)
    embed.add_field(name="/r iDj+math", value="Roll i dice with j sides, then perform arithmetic with the results.\nCredit for this function goes to Will Irwin (Upgwades) https://github.com/Upgwades", inline=False)
    embed.add_field(name="/8ball *question*", value="Ask the bot a yes/no question that it will answer with advanced machine learning (or random choices).", inline=False)
    embed.add_field(name="/strawpoll {title} [Option 1] [Option 2] [Option 3] [Option n]", value="Generates a strawpoll based on the given options. Allows more than one choice, and only one vote per user.", inline=False)
    embed.add_field(name="/suggest *suggestion*", value="Submit a suggestion to a suggestion box. Jeremy checks the box once a week.", inline=False)
    embed.add_field(name="/info", value="Gives information about the bot.", inline=False)
    embed.add_field(name="/help", value="You're lookin' at it.", inline=False)
    await ctx.send(embed=embed)

def check_if_it_is_me(ctx):
    f = open("YourID.txt", "r")
    ID = int(f.read().rstrip())
    f.close()
    return ctx.author.id == ID

@bot.command()
@commands.check(check_if_it_is_me)
async def announce(ctx, *args):
    text = '{}'.format(' '.join(args))
    front = text.find("{")+1
    back = text.find("}")
    if front == back:
        await ctx.send("Oof bad formatting there bud. Use {channel} *announcement*")
    else:
        textList = list(text)
        text = ''.join(textList[back+2:-1])
        channel = str(''.join(textList[front:back]))
        print("Parse channel name: {}".format(channel))
        print("List of text channels: {}".format(discord.utils.get(client.get_all_channels())))
        if channel in ctx.guild.text_channels:
            channelID = discord.utils.get(guild.text_channels, name=channel).id
            embed = discord.Embed(title="Announcement:", description=text, color=0xeee657)
            await client.send_message(discord.Object(id=channel, embed=embed))
        else:
            await ctx.send("You have to use a real channel duder.")

@bot.command()
async def greet(ctx):
	await ctx.send(":smiley: :wave: Hello, there "+ctx.message.author.mention)

@bot.command()
@commands.check(check_if_it_is_me)
async def on_member_join(ctx, member):
    await ctx.send(":smiley: :wave: Hello, there "+ctx.message.author.mention+", welcome to the server.")
    server = str(ctx.guild.name)
    fileInfo = server+"_CustomData.txt"
    f = open(fileInfo, "a+")
    data = f.readlines()
    roleID = data[1]
    role = discord.utils.get(member.server.roles ,id=roleID)
    await bot.add_roles(member, role)
    f.close()

@bot.command()
@commands.has_role(check_if_it_is_me)
async def defaultRole(ctx, *args):
    text = '{}'.format(' '.join(args))
    server = str(ctx.guild.name)
    fileInfo = server+"_CustomData.txt"
    f = open(fileInfo, "a+")
    data = f.readlines()
    role = data[0]
    roleString = "Default role = "
    if text in data:
        await ctx.send("This role is already set as the default role.")
    elif roleString in data:
        await ctx.send("There is already a default role set. Overwriting...")
        role = "Default role = "+text+"\\n"

        await ctx.send("Default role set to '"+text+"'.")
    else:
        role = "Default role = "+text+"\\n"
        await ctx.send("Default role set to '"+text+"'.")
    f.close()

@bot.command()
async def sponge(ctx, *args):
    text = '{}'.format(' '.join(args))
    text = list(text)
    for i in range(0, len(text)):
        if i%2:
            text[i]=text[i].upper()
        else:
            text[i]=text[i].lower()
    await ctx.send(ctx.message.author.mention+": "+''.join(text))

@bot.command()
async def suggest(ctx, *args):
    counter = 0
    suggestion = '{}'.format(' '.join(args))
    server = str(ctx.guild.name)
    suggestionFile = server+"_SuggestionBox.txt"
    f = open(suggestionFile, "a+")
    for line in f:
        if ctx.message.author.mention in line: counter+=1
    if counter >= 10:
        await ctx.send("I think you've submitted enough suggestions for right now... Try again later.")
    else:
        await ctx.send("Thank you for your suggestion!")
        f.write(ctx.message.author.mention+": "+suggestion)
    f.close()

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
    if a.find("/0") == -1:
        exp = parser.parse(a).evaluate({})
        exp=str(exp)
        await ctx.send(ctx.message.author.mention+": "+a+" = "+exp)
    else:
        await ctx.send(ctx.message.author.mention+" don't divide by 0!")

@bot.command()
async def r(ctx, *args):
    a = '{}'.format(''.join(args))
    ops = ['+','-','*','/']
    a = a.replace(' ','')
    for op in ops:
        a = a.replace(op, ' {} '.format(op))
    a = a.split(' ')
    a = ' '.join([str(item) for item in transmogrifier(a)])
    b = str(a)
    try:
        await ctx.send(ctx.message.author.mention+": `"+b+"` = "+str(eval(a)))
    except Exception as e:
        await ctx.send(ctx.message.author.mention+": "+random.choice(british_insults))

@bot.command(name='8ball', description="Answers a yes/no question.", aliases=['eightball', '8-ball', 'eight_ball'], pass_context=True)
async def eightball(ctx, *args):
    a = '{}'.format(' '.join(args))
    responses = ["It is certain.", "As I see it, yes.", "It is decidedly so.", "Without a doubt.", 
                 "Outlook good.", "Most likely", "Yes.", "Yes - definitely.", "You may rely on it.", 
                 "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", 
                 "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", 
                 "My sources say no.", "Outlook not so good.", "Very doubtful."]
    choice = random.randint(0, len(responses)-1)
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
