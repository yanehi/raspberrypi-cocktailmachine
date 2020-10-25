#!/usr/bin/env sh

# https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/
# update raspberrypi
apt-get update -y && apt upgrade -y

# install python3.8 prerequisites
apt-get install -y mongodb git build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim

systemctl enable mongodb
systemctl start mongodb

# download python3.8
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz

# install python3.8
tar zxf Python-3.8.0.tgz
cd Python-3.8.0
./configure --enable-optimizations
make -j 4
make altinstall

# set python3.8 as default
echo "alias python=/usr/local/bin/python3.8" >>~/.bashrc
echo "alias python3=/usr/local/bin/python3.8" >>~/.bashrc
source ~/.bashrc

# check python version
python -V

# remove the installation binaries
cd
rm -r Python-3.8.0
rm Python-3.8.0.tgz

# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install --upgrade pip
echo "alias pip=/usr/local/bin/pip3.8" >>~/.bashrc

# set PATH and create virtualenv

export PATH="$PATH:/home/pi/.local/bin"
virtualenv cocktailmachine
source cocktailmachine/bin/activate

# clone project and install dependencies

git clone https://github.com/yanehi/raspberrypi-cocktailmachine.git
cd raspberrypi-cocktailmachine
pip install -r requirements.txt
apt-get install python3-dev python3-rpi.gpio -y