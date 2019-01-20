#!/bin/sh
# updatedatabase.sh
cd /home/pi/IOTA_project
sudo -H -u pi /usr/bin/python3 update_database.py
cd /
