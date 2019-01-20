#!/bin/sh
# launchsendiota.sh

cd /home/pi/IOTA_sensor
sudo -H -u pi /usr/bin/python3 main.py
cd /
