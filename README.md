# Dungeon-Master-Bot
A discord bot used for server administration, making dicerolls, strawpolls, doing math, and other easily automated tasks.

## Getting Started
Easy clone:
```
git clone https://github.com/JeremyEudy/Dungeon-Master-Bot
```

## Install Dependencies
To setup this bot, run the setup.sh script:
```
sudo ./setup.sh
```
This will install all dependencies for the bot. The dependencies are as listed below:
- asyncio
- aiohttp (3.3.0-3.4.3)
- discord.py (1.0.0a0)
- py_expression_eval
- strawpoll.py
- youtube-dl
- opuslib
- Dice-Roller

## Setup
You must generate a token for this bot in order to implement it in your server. The token must be kept secret, so it will not be included in this repo. During install, ```setup.sh``` will ask you for your token and generate a file where it's kept for reference by the bot.

Some commands are restricted to admin only based on the user's role. In order to access these commands, create a `.txt` file in `CustomData/` called `ServerName_AdminRole.txt` (you must type your server name exactly the way it appears in discord), containing the name of the admin role for your server.

## Functions
This bot performs an everchanging host of functions, such as:
- ```!greet```
  - The bot responds to the user with a friendly greeting.
- ```!announce [channel] 'announcement'```<sup>†</sup>
  - The bot makes an annoncement in the referenced channel.
- ```!defaultRole 'role'```<sup>†</sup>
  - Sets a role to be given to users upon joining the server.
- ```!defaultChannel 'channel'```<sup>†</sup>
  - Sets the default channel for the server for generic bot messaging.
- ```!sponge *string*```
  - sTrInG
  - (If you would like this to also insert a picture of mocking spongebob, then put that picture in `CustomData/Images/` and save it as `Sponge.png`)
- ```!emojify *string*```
  - Take any text and make it `d a n k` 😎
- ```!shrug```
  - ¯\\_(ツ)_/¯
- ```!m X + Y + Z```
  - The bot will perform simple to advanced math using standard arithmetic operators as well as trigonometry (in radians). A comprehensive list of functions can be found here: https://github.com/AxiaCore/py-expression-eval 
- ```!r iDj+math```
  - Rolls i dice with j sides, and allows the user to perform arithmetic with the result. Credit goes to [Will Irwin (Upgwades)](https://github.com/Upgwades "Will's Github")
- ```!8ball *question*```
  - Ask the bot a yes/no question that it will answer with advanced machine learning (or random choices).
- ```!bootycall```
  - Connects you randomly with another person looking for a good time 😘 (DISCLAIMER: I cannot verify that the other party knows you'll be calling)
- ```!strawpoll {title} [Option 1] [Option 2] [Option 3] [Option n]```
  - Generates a strawpoll based on the title given and options listed. The poll will allow users to pick multiple options, and limits the poll to one vote per user by default.
- ```!suggest *suggestion*```
  - Submit a suggestion to a suggestion box. The box is checked once a week.
- ```!ping```
  - Returns the latency of the bot.
- ```!info```
  - Provides general information about the bot.
- ```!help```
  - Prints this menu.

<sup>†</sup>Can only be used by administrator.
### Author
Jeremy Eudy

### Special Thanks
[Will Irwin (Upgwades)](https://github.com/Upgwades "Will's Github")

### License
This project is licensed under the GPLv2
