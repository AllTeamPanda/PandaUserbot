
## Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



PANDA="\n°Panda Userbot Install•"
PANDA+="\n "
PANDA+="\nMenjalankan Panda Userbot di Vps"
PANDA+="\n⚡ Sebelumnya Joinn Grup/Channel ⚡"
PANDA+="\n "
PANDA+="\n📣 Channel: @PandaUserbot"
PANDA+="\n📢 GrupSupport: @TeamSquadUserbotSupport"
PANDA+="\n "
LUQ="\n "
echo -e $PANDA
echo -e $LUQ
echo "Waiting..."
echo -e $LUQ
apt update && upgrade -y
apt install git -y
clear
echo -e $PANDA
echo -e $LUQ
echo "Menginstal python3"
echo -e $LUQ
apt install python3
pip3 install --upgrade pip
apt install postgresql
apt install neofetch
apt install ffmpeg
apt install curl
apt install megatools
apt install unzip
apt install wget
apt install liblapack-dev
apt install aria2
apt install zip
apt install sudo
apt install postgresql-client
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
cle
echo -e $PANDA
echo -e $LUQ
echo "⚙️ Github Installer"
echo -e $LUQ
clear
echo -e $PANDA
echo -e $LUQ
echo "Cloning Panda Userbot"
echo -e $LUQ
git clone https://github.com/ilhammansiz/PandaX_Userbot
clear
echo -e $PANDA
echo -e $LUQ
echo "Menginstall Pakages"
echo -e $LUQ
cd PandaX_Userbot
pip3 install -U -r requirements.txt
python installer/termux.py
