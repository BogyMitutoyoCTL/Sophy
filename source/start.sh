#!/bin/bash
cd /home/pi/Sophy/source/

mv /home/pi/Sophy/values/HighScoreSave.json home/pi/Sophy/values/HighScoreSave-$(date "+%Y%m%d-%H%M%S").json
/home/pi/Sophy/venv/bin/python /home/pi/Sophy/source/programm.py
