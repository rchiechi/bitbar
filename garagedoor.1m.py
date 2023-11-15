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
BASEURL = "https://api.krustylu.org/garage"

def check_status(url):
    try:
        r = requests.get(url)
        return r.json().get('state', 'fail')
    except requests.exceptions.ConnectionError:
        return 'fail'


for _door in ['pinky', 'mustang']:
    _sfcolor = 'orange'
    try:
        _state = requests.get(f'{BASEURL}?door={_door}').json().get('state', 'fail')
    except requests.exceptions.ConnectionError:
        _state = 'fail'
    if _state == 'closed':
        _sfcolor = 'green'
        print(":door.garage.closed:", end='')
    elif _state == 'open':
        _sfcolor = 'red'
        print(":door.garage.open:", end='')
    else:
        print(":door.garage.open.trianglebadge.exclamationmark: | sfcolor=organge", end='')
print(f"| sfcolor={_sfcolor}")
