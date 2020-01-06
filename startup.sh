#!/bin/bash
#################################################################################################################
# Author : Wali Morris 
# Date   : 01/06/2020
# File   : startup.sh
# Notes  :
# This script is for first time users of The Personal Library System, it installs both the Library Management 
# system and dialog. Lastly, this script creates a symbolic link from your home directory to dialog.py which 
# allows users to run The Personal Library System directly from their Home directory by running 'python3 library'.
# This script is used to automate this short process and allow user's to easily use The Library Management Sys
# quickly. If you would like to manually set-up yourself, you'll only need to clone the repository. You can find
# more info by viewing this project's README file. 
##################################################################################################################

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

