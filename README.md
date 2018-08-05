# Dungeon-Master-Bot
A discord bot used for making dicerolls, strawpolls, doing math, and other easily automated tasks.

## Getting Started
Easy clone:
```
mkdir -p ~/Dungeon-Master-Bot/ && cd
git clone https://github.com/JeremyEudy/Dungeon-Master-Bot
```
Or replace ~/Dungeon-Master-Bot with a different valid location.

## Install Dependencies
To setup this bot, run the setup.sh script:
```
chmod +x setup.sh
sudo ./setup.sh
```
This will install all dependencies for the bot. The dependencies are as listed below:\
-asyncio\
-aiohttp (3.3.0-3.4.3)\
-discord.py (1.0.0a0)\
-py_expression_eval\
-strawpoll.py\
-youtube-dl\
-opuslib

## Setup
You must generate a token for this bot in order to implement it in your server. The token must be kept secret, so it will not be included in this repo. Add the token as the only line in a .txt file name ```Token.txt``` and place it in the same directory as ```Dungeon-Master-Bot.py```

## Functions
This bot performs an everchanging host of functions, such as:\
```!greet```\
The bot responds to the user with a friendly greeting.\
```!m X + Y + Z```\
The bot will perform simple to advanced math using standard operators as long as the format matches the above syntax. A comprehensive list of functions can be found here: https://github.com/AxiaCore/py-expression-eval  
```!r iDj+math```\
Rolls i dice with j sides, and allows the user to perform arithmetic with the result.\
```!8ball *question*```\
Ask the bot a yes/no question that it will answer with advanced machine learning (or random choices).\
```!strawpoll {title} [Option 1] [Option 2] [Option 3] [Option n]```\
Generates a strawpoll based on the title given and options listed. The poll will allow users to pick multiple options, and limits the poll to one vote per user by default.\
```!suggest *suggestion*```\
Submit a suggestion to a suggestion box. The box is checked once a week.\
```!info```\
Provides general information about the bot.\
```!help```\
Prints this menu.

### Author
Jeremy Eudy

### License
This project is licensed under the GPLv2
