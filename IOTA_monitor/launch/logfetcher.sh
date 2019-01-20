#!/bin/sh
# logfetcher.sh

scp -i ~/.ssh/id_rsa IOTA_sensor:/home/pi/IOTA_sensor/logs/main.log  /home/pi/IOTA_project/logs/sensor.log
