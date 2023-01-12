#!/bin/bash

# <bitbar.title>Roon Controls</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Use roon control script to control roon remote.</bitbar.desc>
# <bitbar.image>https://i.imgur.com/woYDSdX.png</bitbar.image>
# <bitbar.dependencies>bash, roon</bitbar.dependencies>


getbasedir(){
    if readlink "$0" > /dev/null
    then
        script=$(readlink "$0")
    else
        script=$0
    fi
    basedir=$(dirname "$script")
}

getroonstate() {
    roonstate=$(roon -N -z Familyroom)
    playing=$(printf "${roonstate}"| grep State | tr -d '\t' | cut -d ' ' -f 2)
    if [[ "$playing" == "playing" ]]
    then
        ISPLAYING=1
    else
        ISPLAYING=0
    fi
    track=$(printf "${roonstate}"| grep Track | tr -d '\t' | cut -d ':' -f 2- | tr -d '"')
    artist=$(printf "${roonstate}"| grep Artist | tr -d '\t' | cut -d ':' -f 2- | tr -d '"')
    album=$(printf "${roonstate}"| grep Album | tr -d '\t' | cut -d ':' -f 2- | tr -d '"')

}

ISPLAYING=0
ROONICON="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N8tUOwsAAAATdEVYdGV4aWY6SW1hZ2VXaWR0aAAzNDNQBHlYAAAAGnRFWHRleGlmOlNvZnR3YXJlAEdJTVAgMi4xMC4zMB8Lt4MAAAAkdEVYdGV4aWY6dGh1bWJuYWlsOkJpdHNQZXJTYW1wbGUAOCwgOCwgOCAb9FMAAAAcdEVYdGV4aWY6dGh1bWJuYWlsOkNvbXByZXNzaW9uADb5ZXBXAAAAHnRFWHRleGlmOnRodW1ibmFpbDpJbWFnZUxlbmd0aAAyNTHOFKWgAAAAHXRFWHRleGlmOnRodW1ibmFpbDpJbWFnZVdpZHRoADI1NogG+hQAAAAodEVYdGV4aWY6dGh1bWJuYWlsOkpQRUdJbnRlcmNoYW5nZUZvcm1hdAAzMjiXx+HBAAAAL3RFWHRleGlmOnRodW1ibmFpbDpKUEVHSW50ZXJjaGFuZ2VGb3JtYXRMZW5ndGgAMzc3MkZubH4AAAAqdEVYdGV4aWY6dGh1bWJuYWlsOlBob3RvbWV0cmljSW50ZXJwcmV0YXRpb24ANhIVihoAAAAgdEVYdGV4aWY6dGh1bWJuYWlsOlNhbXBsZXNQZXJQaXhlbAAz4dfNWgAAABt0RVh0aWNjOmNvcHlyaWdodABQdWJsaWMgRG9tYWlutpExWwAAACJ0RVh0aWNjOmRlc2NyaXB0aW9uAEdJTVAgYnVpbHQtaW4gc1JHQkxnQRMAAAAVdEVYdGljYzptYW51ZmFjdHVyZXIAR0lNUEyekMoAAAAOdEVYdGljYzptb2RlbABzUkdCW2BJQwAAAAl0RVh0dW5rbm93bgAx2iFVfAAAAABJRU5ErkJggg=="

# echo "$(dirname $0)"

if [[ -z "$1" ]]
then
    getbasedir
    getroonstate
    # printf " | image=%s\n" $(base64 -w0 "${basedir}/icons/roon.png")
    echo " | image=${ROONICON}"
    echo "---"
    # echo "${emoji}  ${_item}| bash='$0' param1=${remote} refresh=true terminal=false ${color}"
    
    if [[ ISPLAYING == 1 ]]
    then
        echo "Stop | bash='$0' param1=control param2=stop refresh=true terminal=false"
        echo "Next | bash='$0' param1=control param2=stop refresh=true terminal=false"
        echo "-----"
        echo "Playing:${artist}"
        echo "${track}"
        echo "From:${album}"
    else
        echo "Play | bash='$0' param1=control param2=play refresh=true terminal=false"
    fi
fi

if [[ $1 == "control" ]]
then
    roon -c $(echo "${2}"| tr '[:upper:]' '[:lower:]') -z "Familyroom"
fi