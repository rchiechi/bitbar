#!/opt/python/swiftbar/bin/python

# -*- coding:utf-8 -*-

# <bitbar.title>Default Browser</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Provides a menu to swap default browsers quickly.</bitbar.desc>
# <bitbar.dependencies>bash</bitbar.dependencies>

import os
# import sys
import subprocess
import base64
# import json

DBBIN = os.path.join(os.environ['HOME'],'bin','defaultbrowser')
PWD = os.path.dirname(os.path.realpath(__file__))
ICONDIR = os.path.join(PWD,'icons')

def geticonasbase64(icon):
    with open(os.path.join(ICONDIR,icon), 'rb') as fh:
        __base64 = base64.b64encode(fh.read())
    return str(__base64, encoding='utf8')

def getcurrentbrowser():
    __p = subprocess.run(['defaults',
                         'read',
                          os.path.join(os.environ['HOME'],
                                       "Library/Preferences/com.apple.LaunchServices/com.apple.launchservices.secure")],
                         capture_output=True)
    __last_line = ''
    for __l in str(__p.stdout, encoding='utf8').split('\n'):
        if __l.strip() == 'LSHandlerURLScheme = http;':
            break
        __last_line = __l.strip()
    return __last_line.split('.')[-1].strip('";')

def listbrowsers():
    __p = subprocess.run([DBBIN], capture_output=True)
    browsers = []
    for __browser in str(__p.stdout, encoding="utf8").split("\n"):
        browsers.append(__browser.strip())
    return browsers

def switchbrowsers(browser):
    __p = subprocess.run([DBBIN, browser])
    if __p.returncode != 0:
        return False
    return True

def main():
    current_browser = getcurrentbrowser()
    browsers = listbrowsers()
    if current_browser in BROWSERS:
        print(" | image='%s'" % BROWSERS[current_browser][1])
    else:
        print("??? | color=blue")
    # Everything else goes in menus
    print('---')
    for browser in enumerate(BROWSERS):
        __key = browser[1]
        if __key in browsers:
            print(" | image='%s' shell='%s' param1='%s' refresh=true terminal=false" %
                  (BROWSERS[__key][1], DBBIN, __key))


BROWSERS = {"linkobrowser":("Linko", geticonasbase64('linko.png')),
            "safari":("Safari", geticonasbase64('safari.png')),
            "firefox":("Firefox", geticonasbase64('firefox.png')),
            "chrome":("Chrome", geticonasbase64('chrome.png')),
            "edgemac":("Edge", geticonasbase64('edge.png')),
            "browser":("Brave", geticonasbase64('brave.png'))
            }

main()
