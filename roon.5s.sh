#!/bin/bash

# <bitbar.title>Roon Controls</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Use roon control script to control roon remote.</bitbar.desc>
# <bitbar.image>https://i.imgur.com/woYDSdX.png</bitbar.image>
# <bitbar.dependencies>bash, roon</bitbar.dependencies>


if [[ -z "$1" ]]
then
    echo "Roon"
    echo "---"
    # echo "${emoji}  ${_item}| bash='$0' param1=${remote} refresh=true terminal=false ${color}"
    echo "Play | bash='$0' param1=control param2=play refresh=true terminal=false"
    echo "Stop | bash='$0' param1=control param2=stop refresh=true terminal=false"
    echo "Next | bash='$0' param1=control param2=stop refresh=true terminal=false"
fi

if [[ $1 == "control" ]]
then
    roon -c $(echo "${2}"| tr '[:upper:]' '[:lower:]') -z "Familyroom"
fi