#!/bin/usr/python3

# Task: Sets radio stream to play on boot; simple version for User (Pi) Desktop

import subprocess

URL1 = www.google.com
URL2 = www.adobe.com

# remove "#" below to launch URL1 on reboot
subprocess.Popen(['epiphany-browser',URL1 &])  # open URL1

# remove "#" below to launch URL2 on reboot
#subprocess.Popen(['epiphany-browser',URL2 &])  # open URL2
