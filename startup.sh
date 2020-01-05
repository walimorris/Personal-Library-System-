!/bin/bash

printf "Welcome to the Home Library system!\n"
printf "[WARNING!] Selecting 'Y' will update your system, install dialog and set-up this program. Continue? Y/n "

read -r setup

if [ $setup = 'Y' ] || [ $setup = 'y' ]; then
    sudo apt-get install python3-dialog
    ln -s Lib_dialog.py library
    printf "The Home Library is setup on this system. From this point you can run 'python3 library' from this directory to run this program.\n"
fi

if [ $setup != 'Y' ] || [ $setup != 'y' ]; then
    exit(0)
fi     

