#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# Metadata allows your plugin to show up in the app, and website.
#
#  <xbar.title>Garage Door</xbar.title>
#  <xbar.version>v1.0</xbar.version>
#  <xbar.author>Your Name, Another author name</xbar.author>
#  <xbar.author.github>your-github-username,another-github-username</xbar.author.github>
#  <xbar.desc>Short description of what your plugin does.</xbar.desc>
#  <xbar.image>http://www.hosted-somewhere/pluginimage</xbar.image>
#  <xbar.dependencies>python,ruby,node</xbar.dependencies>
#  <xbar.abouturl>http://url-to-about.com/</xbar.abouturl>

# Variables become preferences in the app:
#
#  <xbar.var>string(VAR_NAME="Mat Ryer"): Your name.</xbar.var>
#  <xbar.var>number(VAR_COUNTER=1): A counter.</xbar.var>
#  <xbar.var>boolean(VAR_VERBOSE=true): Whether to be verbose or not.</xbar.var>
#  <xbar.var>select(VAR_STYLE="normal"): Which style to use. [small, normal, big]</xbar.var>

import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')
sys.path.append('/usr/local/lib/python3.9/site-packages')

import os
import base64
import requests


PWD = os.path.dirname(os.path.realpath(__file__))
# URL = "http://garagedoor.krustylu.org"
URL = "http://10.10.10.180:5000"

def check_status():
    response = requests.get("%s/status" % URL)
    data = response.json()
    if 'inputs' in data:
        return data['inputs'][0]['input']
    else:
        return -1

if check_status() == 1:
    png = base64.b64encode(open(os.path.join(PWD, 'door_closed.png'), 'rb').read())
    print(" | image=%s" % str(png, encoding='utf8'))
    #print("Closed | color=green")
elif check_status() == 0:
    png = base64.b64encode(open(os.path.join(PWD, 'door_open.png'), 'rb').read())
    print(" | image=%s" % str(png, encoding='utf8'))
    #print("Open | color=red")
else:
    print("??? | color=blue")
