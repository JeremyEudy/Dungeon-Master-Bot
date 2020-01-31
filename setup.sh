#!/usr/bin/env bash
# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    setup.sh                                           ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2018/06/19 18:40:41 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2018/06/19 18:40:41 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "-------------------------------------------------------------------------------"
echo "${BLUE}Make sure you have Python 3.6 installed.${NC}"
echo "-------------------------------------------------------------------------------"
sudo python3.6 -m pip install aiohttp
sudo python3.6 -m pip install py_expression_eval
sudo python3.6 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
sudo python3.6 -m pip install strawpoll.py
sudo python3.6 -m pip install asyncio
sudo python3.6 -m pip install --upgrade youtube-dl
sudo python3.6 -m pip install opuslib
git clone https://github.com/Upgwades/Dice-Roller || mv Dice-Roller roller
mv roller/roller.py .

echo "-------------------------------------------------------------------------------"
echo "${BLUE}Do you want to register the bot as a system service?${NC}"
echo "-------------------------------------------------------------------------------"
echo "1 - Yes"
echo "2 - No"
read answer
if [ $answer -eq 1 ]
then
    cp DungeonMaster.service /lib/systemd/system/
    cd ..
    mv Dungeon-Master-Bot/ /usr/bin/Dungeon-Master-Bot/
    cd /usr/bin/Dungeon-Master-Bot/
fi

echo "-------------------------------------------------------------------------------"
echo "${BLUE}Creating directories and fixing paths${NC}"
echo "-------------------------------------------------------------------------------"
mkdir -p CustomData/
mkdir -p CustomData/Images/

sed -i -e 's@PATH = "/usr/bin/Dungeon-Master-Bot/"@PATH = "'$PWD'/"@g' Dungeon-Master.py

echo "-------------------------------------------------------------------------------"
echo "${BLUE}Paste your token here:${NC}"
echo "-------------------------------------------------------------------------------"
read token
echo $token > Token.txt

echo "-------------------------------------------------------------------------------"
echo "${BLUE}Paste your Discord UID here:${NC}"
echo "-------------------------------------------------------------------------------"
read UID
echo $UID > YourID.txt

echo "-------------------------------------------------------------------------------"
echo "${GREEN}Install complete.${NC}"
echo "-------------------------------------------------------------------------------"
