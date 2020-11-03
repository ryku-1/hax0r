#!/bin/sh

echo "####################################"
echo "#                                  #"
echo "#         Kalifiguration           #"
echo "#           by Ryku-01             #"
echo "#                                  #"
echo "####################################"

#update and upgrade 

sudo apt-get upgrade

sudo apt-get update 

#add user

read -p "Enter Username: " username
echo "Creating user: " $username

##will prompt for password
adduser $username 

#make sudo
usermod -aG sudo $username

#switch to new user to finish configs
su $username

#install sublime-text

cd /tmp

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - 

echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

sudo apt update && sudo apt install sublime-text 

#install pip 

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py

#set screen timer to 30 minutes
gsettings set org.gnome.desktop.session idle-delay 1800
#set the system to lock on screen blank
gsettings set org.gnome.desktop.screensaver lock-delay 0
gsettings set org.gnome.desktop.screensaver lock-enabled true

#install konsole 

sudo apt-get install konsole

#install pt-repo, big ups to nighter!!

cd ~/

git clone https://github.com/mikaelkall/HackingAllTheThings.git

mv HackingAllTheThings pt-repo

echo "Kalifiguration Done!!!"








