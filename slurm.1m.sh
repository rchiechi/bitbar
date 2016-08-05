#!/bin/bash

# <bitbar.title>Slurm Status</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Checks for running jobs on a slurm cluster.</bitbar.desc>
# <bitbar.dependencies>bash</bitbar.dependencies>


HOST=SLURM_HOST
UN=YOUR_LOGIN

#
# You must have public key authentication for this HOST/UN
#

function checkrunning() {
    q=$(ssh ${HOST} "squeue -u ${UN} -h")
    if [ $(printf "${q}" | grep -c ' R ') -gt 0 ]; then
        printf 2
    elif [ -n "${q}" ]; then
        printf 1
    else
        printf 0
    fi
}

function checkQ() {
    ssh ${HOST} "squeue ${1} -S U --format='%.18i %.8j %.2t %.10M %.6D %R'" | while read job; do
        if [ $(printf "${job}" | grep -c 'JOBID') -gt 0 ]; then
            echo "--${job} | color=black"
        elif [ $(printf "${job}" | grep -c ' R ') -gt 0 ]; then
            echo "--${job} | color=green"
        else
            echo "--${job} | color=indianred"
        fi
    done
}

printf "["
if [ $(checkrunning) == 0 ]; then
    printf ":sleeping:"
elif [ $(checkrunning) == 1 ]; then 
    printf ":pensive:"
elif [ $(checkrunning) == 2 ]; then
    printf ":smiley:"
fi
printf "]\n"
echo "---"
echo "My Jobs | color=black"
checkQ "-u ${UN}"
echo "All Jobs | color=black"
checkQ
