#!/opt/homebrew/bin/python3
# -*- coding:utf-8 -*-
# Metadata allows your plugin to show up in the app, and website.
#
#  <xbar.title>Garage Door</xbar.title>
#  <xbar.version>v1.0</xbar.version>
#  <xbar.author>Ryan Chiechi</xbar.author>
#  <xbar.author.github>rchiechi</xbar.author.github>
#  <xbar.dependencies>python</xbar.dependencies>
# <swiftbar.hideAbout>true</swiftbar.hideAbout>
# <swiftbar.hideRunInTerminal>true</swiftbar.hideRunInTerminal>
# <swiftbar.hideDisablePlugin>true</swiftbar.hideDisablePlugin>

import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')
sys.path.append('/usr/local/lib/python3.9/site-packages')

import os
import base64
import requests


PWD = os.path.dirname(os.path.realpath(__file__))
URL1 = "http://10.10.10.67"
URL2 = "http://10.10.10.180:5000"

def check_status(url):
    try:
        response = requests.get("%s/status" % url)
    except requests.exceptions.ConnectionError:
        return -1
    data = response.json()
    if 'inputs' in data:
        return data['inputs'][0]['input']
    else:
        return -1


for _url in [URL1, URL2]:
    if check_status(_url) == 1:
        print(":door.garage.closed:", end='')
    elif check_status(_url) == 0:
        print(":door.garage.open:", end='')
    elif check_status(_url) == -1:
        print(":door.garage.open.trianglebadge.exclamationmark:", end='')
    else:
        print("??? | color=blue", end='')
print("")
