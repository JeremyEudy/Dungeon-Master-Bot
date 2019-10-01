#!/usr/bin/env bash

if ! screen -list | grep -q "DungeonMaster"; then
    screen -dmS DungeonMaster python3.6 /home/jeremy/Dungeon-Master-Bot/Dungeon-Master.py
fi
