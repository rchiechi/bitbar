#!/bin/bash

# <bitbar.title>Rclone Mount</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Quickly mount endpoints in rclone.</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>bash</bitbar.dependencies>


TARGET=${HOME}/encrypted
RCLONE=/usr/local/bin/rclone
RCLONE_CONFIG_PASS=""

# export RCLONE_CONFIG_PASS=$(/usr/local/bin/pass Macbert/rclone)
export RCLONE_CONFIG_PASS=$(/usr/local/bin/gpg -o - -d ${HOME}/.password-store/Macbert/rclone.gpg 2>/dev/null)
# [[ -f /tmp/rclonconfipass.sh ]] && . /tmp/rclonconfipass.sh
# export RCLONE_CONFIG_PASS

function rcloneimage() {
  icon="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
"
}

function mountpoint() {
  mount | grep -q "$1"
  return $?

}

function isremote() {
  ${RCLONE} --ask-password=false listremotes | while read remote; do
    if [[ "$1" == "${remote}" ]] ; then
      return 0
    fi
  done
  return 1
}

function domount() {
  mountpoint "${TARGET}" && return 1
  ${RCLONE} --ask-password=false mount --daemon "${1}" "${TARGET}" >/dev/null 2>&1
  return $?
}

function listremotes() {
  echo "---"
  ${RCLONE} --ask-password=false listremotes | while read remote; do
    _item=$(printf "${remote}" | tr -d ':')
    if mountpoint ${remote} ; then
      color="color=green"
      emoji=":floppy_disk:"
    else
      color=""
      emoji=""
    fi
    echo "${emoji}  ${_item}| bash='$0' param1=${remote} refresh=true terminal=false ${color}"
  done
}

if [[ -n "$1" ]] && mountpoint "$1" ; then
  diskutil unmount ${TARGET} >/dev/null 2>&1
  sleep 1
  exit
elif [[ -n "$1" ]] && isremote "$1" ; then
  domount "${1}"
  sleep 3
  exit
fi


rcloneimage
echo " | image=${icon}"
listremotes
