# **************************************************************************** #
#                                                                              #
#                                                   ---------------------      #
#    Dungeon-Master.py                              |     ______  _____ | J    #
#                                                   |    / ____/ / ___/ | E    #
#    By: jeremy <jeremyeudy@gmail.com>              |   / / __  / /_    | R    #
#                                                   |  / /_/ / / __/    | E    #
#    Created: 2018/05/29 10:00:02 by jeremy         | /_____/ /_/       | M    #
#    Updated: 2021/09/06 01:17:48 by jeremy         |                   | Y    #
#                                                   ---------------------      #
#                                                                              #
# **************************************************************************** #

from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
from py_expression_eval import Parser
from emojifier import Emojifier
from roller import *
import operator as op
import re, random, asyncio, aiohttp, discord, strawpoll, requests, youtube_dl

debugMode = True

PATH = "/usr/bin/Dungeon-Master-Bot/"
BOT_PREFIX = ("!")
f = open(PATH+'Token.txt', 'r') #Find token
TOKEN = f.read().rstrip()
f.close()

f = open(PATH+"YourID.txt", "r")
OwnerID = int(f.read().rstrip())
f.close()

#Function to get server admin role
def Check_Admin(ctx):
        try:
                server = str(ctx.guild.name)
        except AttributeError:
                # If this is a DM, then there isn't a guild.name
                return True

        try:
                fileInfo = PATH+"CustomData/"+server+"_AdminRole.txt"   #This file must be created by you
                f = open(fileInfo, "r")
                roleName = str(f.read().rstrip())
                if roleName in [i.name for i in ctx.author.roles]:
                        return True
                else:
                        return False
        except:
                return False

bot = commands.Bot(command_prefix = BOT_PREFIX, description='A bot that does a whole host of things that Jeremy works on in his free time.')

#Will's beautiful insult table
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

bot.remove_command('help')      #Required to insert my own
@bot.command()
async def help(ctx):
        #Prints an embedded message describing all the features of the bot
        embed = discord.Embed(title="Dungeon-Master", description="This bot does some stuff, here's a list:", color=0xeee657)
        embed.add_field(name="!greet", value="Greets the user", inline=False)
        embed.add_field(name="!sponge", value="SpOnGe", inline=False)
        embed.add_field(name="!emojify", value="Take any text and make it `d a n k` 😎", inline=False)
        embed.add_field(name="!shrug", value=" ¯\_(ツ)_/¯", inline=False)
        embed.add_field(name="!m X + Y + Z", value="Solves a math problem of any length (addition, subtraction, multiplication, division).\nAlso able to solve more advanced math. A comprehensive list is available at https://github.com/AxiaCore/py-expression-eval", inline=False)
        embed.add_field(name="!r iDj+math", value="Roll i dice with j sides, then perform arithmetic with the results.\nCredit for this function goes to Will Irwin (Upgwades) https://github.com/Upgwades", inline=False)
        embed.add_field(name="!8ball *question*", value="Ask the bot a yes/no question that it will answer with advanced machine learning (or random choices).", inline=False)
        embed.add_field(name="!bootycall", value="Connects you randomly with another person looking for a good time 😘 (DISCLAIMER: I cannot verify that the other party knows you'll be calling)", inline=False)
        embed.add_field(name="!strawpoll {title} [Option 1] [Option 2] [Option 3] [Option n]", value="Generates a strawpoll based on the given options. Allows more than one choice, and only one vote per user.", inline=False)
        embed.add_field(name="!suggest *suggestion*", value="Submit a suggestion to a suggestion box. Jeremy checks the box once a week.", inline=False)
        embed.add_field(name="!ping", value="Returns the latency of the bot.", inline=False)
        embed.add_field(name="!info", value="Gives information about the bot.", inline=False)
        embed.add_field(name="!help", value="You're lookin' at it.", inline=False)
        await ctx.send(embed=embed)
        if(Check_Admin(ctx)):
                #If the user that called /help is an admin, then the bot sends them a PM with admin commands
                channel = ctx.author.dm_channel
                if(channel is None):
                        await ctx.author.create_dm()
                channel = ctx.author.dm_channel
                embed = discord.Embed(title="Dungeon-Master (Admin Commands)", description="Here's a secret list of commands your role can perform:", color=0xeee657)
                embed.add_field(name="!announce {channel name} *announcement*", value="A command to send an announcement to a specified channel (it doesn't abuse @everyone)", inline=False)
                embed.add_field(name="!DefaultChannel *channel name*", value="Sets the default posting channel for the bot.", inline=False)
                embed.add_field(name="!DefaultRole *role name*", value="Sets the role new members get on join.", inline=False)
                await channel.send(embed=embed)

@bot.command(name='announce', description="A command to send an announcement to a specified channel (it doesn't abuse @everyone)")
async def announce(ctx, *args):
        if(Check_Admin(ctx)):
                text = ' '.join(args)
                front = text.find("{")+1                #Find channel name indices
                back = text.find("}")
                if text.find("{") == back:                      #Verify user input channel name
                        await ctx.send("Oof bad formatting there bud. Use {channel} *announcement*")
                else:
                        textList = list(text)
                        text = ''.join(textList[back+2:])               #Get announcement
                        channel = str(''.join(textList[front:back]))    #Get channel
                        channelList = ctx.guild.text_channels           #Get list of channels
                        for i in channelList:
                                if i.name == channel:                   #Find channel in channel list and save its ID
                                        channelID = i.id
                                        channel = i
                        if channelID != None:                           #Verify the channel was found using ID
                                embed = discord.Embed(title="Announcement:", description=text, color=0xeee657)
                                await channel.send(embed=embed)
                        else:
                                await ctx.send("You have to use a real channel duder.")


@bot.command(name='say', description="A command to speak through the bot.")
async def say(ctx, *args):
        if(Check_Admin(ctx)):
                text = ' '.join(args)
                frontS = text.find("[")+1               #Find server name indices
                backS = text.find("]")
                frontC = text.find("{")+1               #Find channel name indices
                backC = text.find("}")
                server = None
                if text.find("{") == backC:                     #Verify user input channel name
                        await ctx.send("Oof bad formatting there bud. Use [server] {channel} *text*")
                elif text.find("[") == backS:
                        await ctx.send("Oof bad formatting there bud. Use [server] {channel} *text*")
                else:
                        textList = list(text)
                        text = ''.join(textList[backC+2:])              #Get message contents
                        serverName = str(''.join(textList[frontS:backS]))   #Get server
                        serverList = bot.guilds                         #Get list of servers
                        for i in serverList:
                                if i.name == serverName:                #find the right server
                                        server = i

                channel = str(''.join(textList[frontC:backC]))  #Get channel
                channelList = server.text_channels              #Get list of channels
                for i in channelList:
                        if i.name == channel:                   #Find channel in channel list and save its ID
                                channelID = i.id
                                channel = i
                if channelID != None:                           #Verify the channel was found using ID
                        await server.channel.send(text)
                else:
                        await ctx.send("You have to use a real channel duder.")

@bot.command(description="Greets users")
async def greet(ctx):
        await ctx.send(":smiley: :wave: Hello, there "+ctx.message.author.mention)

@bot.command(description="Returns a shrug emoticon")
async def shrug(ctx):
        await ctx.send("¯\_(ツ)_/¯")

@bot.command(description="Returns the bots ping")
async def ping(ctx):
        await ctx.send(':ping_pong: Pong! {}'.format(round(bot.latency, 1)))

@bot.event
async def on_member_join(member):
        #Greets new users in the default channel, and gives them the default role (if both are set)
        server = str(member.guild.name)
        try:
                fileInfo = PATH+"CustomData/"+server+"_DefaultChannel.txt"
                channel = None
                with open(fileInfo, "r") as f:
                    channel = str(f.read().rstrip())        #Get channel name
                channelList = member.guild.text_channels        #Get list of text channels
                for i in channelList:                   #Iterate through channelList and find the default channel
                        if i.name == channel:
                                channelID = i.id
                                channel = i
                if channelID != None:                   #Use the channel ID to ensure we found the channel
                        await channel.send(":smiley: :wave: Hello, there "+member.mention+", welcome to the server.")
        except:
                pass
        try:
                fileInfo = PATH+"CustomData/"+server+"_DefaultRole.txt"
                roleName = None
                with open(fileInfo, "r") as f:
                    roleName = str(f.read().rstrip())       #Get role name
                try:
                    role = discord.utils.get(member.guild.roles, name=roleName)     #Find the role object that has that name
                except:
                    pass
                await member.add_roles(role, atomic=True)               #Give the role to the member
        except:
                pass

@bot.command(name='DefaultRole', description="A command to set the default role given to new members upon joining a server.")
async def DefaultRole(ctx, *args):
        if(Check_Admin(ctx)):
                text = ' '.join(args)
                server = str(ctx.guild.name)
                fileInfo = PATH+"CustomData/"+server+"_DefaultRole.txt"
                with open(fileInfo, "w+") as f:
                    f.write(text)                           #Generates a file containing the default role for your server
                await ctx.send("The default role is now "+text)

@bot.command(name='DefaultChannel', description="A command to set the default channel for the server.")
async def DefaultChannel(ctx, *args):
        if(Check_Admin(ctx)):
                text = ' '.join(args)
                server = str(ctx.guild.name)
                fileInfo = PATH+"CustomData/"+server+"_DefaultChannel.txt"
                with open(fileInfo, "w") as f:
                    f.write(text)                   #Generates a file containing the default channel for your server
                await ctx.send("The default channel is now "+text)

@bot.command(description="Returns a string with alternating case.")
async def sponge(ctx, *args):
        text = ' '.join(args)
        text = list(text)
        for i in range(0, len(text)):           #Iterates through text and changes every other characters case
                if i%2:
                        text[i]=text[i].upper()
                else:
                        text[i]=text[i].lower()
        text = ctx.message.author.mention+": "+''.join(text)
        try:
                picture = discord.File("CustomData/Images/Sponge.png")  #Directory for mocking spongebob image
                await ctx.send(content=text, file=picture)
        except:
                await ctx.send(text)

@bot.command(name='emojify', description="Takes any string and makes it `d a n k` 😎")
async def emojify(ctx, *args):
        message = ' '.join(args)
        emoji = Emojifier.of_default_mappings()
        emojify = emoji.generate_emojipasta(text=message)
        await ctx.send(ctx.message.author.mention+': '+emojify)

@bot.command()
async def suggest(ctx, *args):
        counter = 0
        suggestion = ' '.join(args)                #Get input in suggestion
        server = str(ctx.guild.name)                    #Get server name
        suggestionFile = PATH+"CustomData/"+server+"_SuggestionBox.txt" #Construct file name based on server name
        with open(suggestionFile, "a+") as f:
            for line in f:
                    if ctx.message.author.mention in line: counter+=1       #Count the number of suggestions a user has in the file
            if counter >= 10:                                               #Make sure no one is spamming
                    await ctx.send("I think you've submitted enough suggestions for right now... Try again later.")
            else:
                    await ctx.send("Thank you for your suggestion!")
                    f.write(ctx.message.author.mention+": "+suggestion)     #Write suggestion to file and close

@bot.command()
async def m(ctx, *args):
        #Gets and cleans input from user and passes it to py-expression-eval parser
        _input = ''.join(args)
        #Check for constants
        if _input=="pi":
                _input=_input.upper()
        elif _input=="e":
                _input=_input.upper()
        else:
                _input=_input.lower()
        parser = Parser()
        if _input.find("/0") == -1:             #Make sure no one divides by 0
                exp = parser.parse(_input).evaluate({})
                exp=str(exp)
                await ctx.send(ctx.message.author.mention+": "+_input+" = "+exp)
        else:
                await ctx.send(ctx.message.author.mention+" don't divide by 0!")

@bot.command(name='r', description="A basic port of Will's roller program that essentially recreates his __main__ class and sends the output", aliases=['roll'])
async def r(ctx, *args):
        roll = ''.join(args)
        ops = ['+','-','*','/']
        #clean the roll input because it gets messy
        roll = roll.replace(' ','')
        for op in ops:
                roll = roll.replace(op, ' {} '.format(op))
        roll = roll.split(' ')
        roll = ' '.join([str(item) for item in transmogrifier(roll)])           #Pass clean input into Will's code
        rollString = str(roll)
        try:
                await ctx.send(ctx.message.author.mention+": `"+rollString+"` = "+str(eval(roll)))
        except Exception as e:
                await ctx.send(ctx.message.author.mention+": "+random.choice(british_insults))

@bot.command(name='stats', description="Generates a list of DnD character stats (/r 6(6d4kh3)).", aliases=['rollstats', 'rstats'])
async def stats(ctx):
        rolls = []
        for i in range(0, 6):
                stat = []
                for j in range(0, 6):
                        stat.append(random.randint(1, 6))
                lowest = min(stat)
                stat.pop(stat.index(lowest))
                lowest = min(stat)
                stat.pop(stat.index(lowest))
                lowest = min(stat)
                stat.pop(stat.index(lowest))
                statFinal = str(sum(stat))
                rolls.append(statFinal)

        rollString = rolls[0]+" "+rolls[1]+" "+rolls[2]+" "+rolls[3]+" "+rolls[4]+" "+rolls[5]
        await ctx.send("Here's your stats "+ctx.message.author.mention+":\n"+rollString)

@bot.command(name='8ball', description="Answers a yes/no question.", aliases=['eightball', '8-ball', 'eight_ball'])
async def eightball(ctx, *args):
        a = ' '.join(args)
        responses = ["It is certain.", "As I see it, yes.", "It is decidedly so.", "Without a doubt.", 
                                 "Outlook good.", "Most likely", "Yes.", "Yes - definitely.", "You may rely on it.", 
                                 "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", 
                                 "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", 
                                 "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(ctx.message.author.mention+": "+random.choice(responses))

@bot.command(name='bootycall', description="Connects you randomly with another person looking for a good time 😘 (DISCLAIMER: I cannot verify that the other party knows you'll be calling)")
async def bootycall(ctx):
        responses = [
                "They're into feet 😘", "Try talking about herbs",
                "Give 'em a call, who knows what'll happen", "Remember, don't talk about the news",
                "Make sure they're not allergic to something you love"]
        number = "{}-{}-{}".format(random.randint(100, 1000), random.randint(100, 1000), random.randint(1000, 10000))
        await ctx.send(ctx.message.author.mention+": **"+number+"** - "+random.choice(responses))

@bot.command(name='newStrawpoll', description="A simple interface for the strawpoll.me API.", aliases=['strawpoll'])
async def newStrawpoll(ctx, *args):
        message = ''.join(args)
        #Gets the title of the poll
        first = message.find("{") + 1
        second = message.find("}")
        title = message[first:second]

        #Gets the # of options and assigns them to an array
        newMessage = message[second:]
        loopTime = 0

        option = []
        for options in message:
                stillOptions = newMessage.find("[")     #Checks to see if there's more options
                if stillOptions != -1:
                        if loopTime == 0:               #First run has to be different so there's a separate case
                                first = newMessage.find("[") + 1
                                second = newMessage.find("]")
                                second1 = second + 1
                                option.append(newMessage[first:second])
                                loopTime+=1
                        else:
                                newMessage = newMessage[second1:]       #Update the contents of newMessage to get rid of old options
                                first = newMessage.find("[") + 1
                                second = newMessage.find("]")
                                second1 = second + 1
                                option.append(newMessage[first:second])
        try:
                r = requests.post('https://www.strawpoll.me/api/v2/polls', json = {"title": title, "options": option[:(len(option)-1)], "multi": "true"}, headers={"Content Type": "application/json"})         #Send poll to strawpoll.me
                json = r.json()
                await ctx.send("https://strawpoll.me/" + str(json["id"]))

        except:
                await ctx.send( "Please make sure you are using the format '/strawpoll {title} [Option1] [Option2] [Option 3]'")

bot.run(TOKEN)
