#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3

# <bitbar.title>Default Browser</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Provides a menu to swap default browsers quickly.</bitbar.desc>
# <bitbar.dependencies>bash</bitbar.dependencies>

import os
import sys
import subprocess
import base64
# import json

DBBIN=os.path.join(os.environ['HOME'],'bin','defaultbrowser')
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
    return __p.stdout

def switchbrowsers(browser):
    __p = subprocess.run([DBBIN, browser])
    if __p.returncode != 0:
        return False
    return True

def main():
    current_browser = getcurrentbrowser()
    if current_browser in BROWSERS:
        print(" | image='%s'" % BROWSERS[current_browser][1])
    # Everything else goes in menus
    print('---')
    for browser in enumerate(BROWSERS):
        __key = browser[1]
        print(" | image='%s' shell='%s' param1='%s' refresh=true terminal=false" % 
             (BROWSERS[__key][1], os.path.join(PWD, sys.argv[0]), __key))
        # print(" %s | bash='$0' param1=%s refresh=true terminal=false" % (BROWSERS[__key][0], __key))
        
BROWSERS = {"safari":("Safari",
    geticonasbase64('safari.png')),
"firefox":("Firefox",
    geticonasbase64('firefox.png')),
"chrome":("Chrome",
    geticonasbase64('chrome.png')),
"edgemac":("Edge",
    geticonasbase64('edge.png'))
}    

if len(sys.argv) > 1:
    cmd = sys.argv[1]
    if cmd in BROWSERS:
        print(cmd)
        switchbrowsers(cmd)
else:
    main()
