#!/bin/bash

printf "Welcome to the Home Library system!\n"
printf "[WARNING!] Selecting 'Y' will update your system, install dialog and set-up this program. Continue? Y/n "

read -r setup

if [ $setup = 'Y' ] || [ $setup = 'y' ]; then
    sudo apt-get install python3-dialog
    fdir=$(pwd)/Lib_dialog.py
    cd --; ln -s $fdir library
    printf "The Home Library is setup on this system. From this point forward, you can run 'python3 library' from your Home directory to run this program.\n"
else
    exit 0 
fi

