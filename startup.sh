!/bin/bash

printf "Welcome to the Home Library system! Are you a first time user?\n"
printf "[WARNING!] Selecting 'Y' will update your system, install dialog and set-up this program. Continue? Y/n "

read -r setup

if [ $setup = 'Y' ] || [ $setup = 'y' ]; then
    sudo apt-get install python3-dialog
    ln -s startup.sh Library
fi

printf "The Home Library is setup on this system. From this point you can run ./Library from this directory to run this program.\n"
