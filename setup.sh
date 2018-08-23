#!/bin/sh
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

echo "Make sure you have Python 3.6 installed."
sudo python3.6 -m pip install aiohttp
sudo python3.6 -m pip install py_expression_eval
sudo python3.6 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
sudo python3.6 -m pip install strawpoll.py
sudo python3.6 -m pip install asyncio
sudo python3.6 -m pip install --upgrade youtube-dl
sudo python3.6 -m pip install opuslib
git clone https://github.com/Upgwades/Dice-Roller && mv roller.py ..
