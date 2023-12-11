#!/opt/python/swiftbar/bin/python

# -*- coding:utf-8 -*-

# <bitbar.title>Default Browser</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Provides a menu to swap default browsers quickly.</bitbar.desc>
# <bitbar.dependencies>bash</bitbar.dependencies>
# <swiftbar.hideAbout>true</swiftbar.hideAbout>
# <swiftbar.hideRunInTerminal>true</swiftbar.hideRunInTerminal>
# <swiftbar.hideDisablePlugin>true</swiftbar.hideDisablePlugin>
# <swiftbar.hideSwiftBar>true</swiftbar.hideSwiftBar>

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
        _base64 = base64.b64encode(fh.read())
    return str(_base64, encoding='utf8')

def getcurrentbrowser():
    _p = subprocess.run(['defaults',
                         'read',
                          os.path.join(os.environ['HOME'],
                                       "Library/Preferences/com.apple.LaunchServices/com.apple.launchservices.secure")],
                         capture_output=True)
    _last_line = ''
    for _l in str(_p.stdout, encoding='utf8').split('\n'):
        if _l.strip() == 'LSHandlerURLScheme = http;':
            break
        _last_line = _l.strip()
    return _last_line.split('.')[-1].strip('";')

def listbrowsers():
    _p = subprocess.run([DBBIN], capture_output=True)
    browsers = []
    for _browser in str(_p.stdout, encoding="utf8").split("\n"):
        browsers.append(_browser.strip())
    return browsers

def switchbrowsers(browser):
    _p = subprocess.run([DBBIN, browser])
    if _p.returncode != 0:
        return False
    return True

def main():
    current_browser = getcurrentbrowser()
    browsers = listbrowsers()
    if current_browser in BROWSERS:
        print(f" | size=6 image='{BROWSERS[current_browser][1]}'")
    else:
        print("??? | color=blue")
    # Everything else goes in menus
    print('---')
    for browser in enumerate(BROWSERS):
        _key = browser[1]
        if _key in browsers:
            print("%s | size=10 image='%s' shell='%s' param1='%s' refresh=true terminal=false" %
                  (BROWSERS[_key][0], BROWSERS[_key][1], DBBIN, _key))


BROWSERS = {"linkobrowser":("Linko", geticonasbase64('linko.png')),
            "safari":("Safari", geticonasbase64('safari.png')),
            "firefox":("Firefox", geticonasbase64('firefox.png')),
            "chrome":("Chrome", geticonasbase64('chrome.png')),
            "edgemac":("Edge", geticonasbase64('edge.png')),
            "browser":("Brave", geticonasbase64('brave.png')),
            "chromium":("Chrommium", geticonasbase64('chromium.png'))
            }

main()
