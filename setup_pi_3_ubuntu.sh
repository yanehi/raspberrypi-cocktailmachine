#!/usr/bin/env sh

# https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/
# update raspberrypi
apt-get update -y && apt upgrade -y

# install python3.8 prerequisites
apt-get install -y git python3-dev build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim

# Install MongoDBv4
# https://developer.mongodb.com/how-to/mongodb-on-raspberry-pi
# Install the MongoDB 4.4 GPG key:
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
# Add the source location for the MongoDB packages:
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
# Download the package details for the MongoDB packages:
apt-get update
# Install MongoDB:
apt-get install -y mongodb-org
# Ensure mongod config is picked up:
systemctl daemon-reload
# Tell systemd to run mongod on reboot:
systemctl enable mongod
# Start up mongod!
systemctl start mongod

# set python3.8 as default
echo "alias python=python3" >>~/.bashrc
source ~/.bashrc

# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install --upgrade pip

# set PATH and create virtualenv
export PATH="$PATH:/home/ubuntu/.local/bin"
pip install virtualenv==20.0.35
virtualenv cocktailmachine
source cocktailmachine/bin/activate

# clone project and install dependencies
mkdir git
cd git
git clone https://github.com/yanehi/raspberrypi-cocktailmachine.git
cd raspberrypi-cocktailmachine
cp env/mongodb-express.env.dummmy env/mongodb-express.env
pip install -r requirements.txt
cd api
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# create database cocktailmachine
# create user barkeeper with password barkeeper with read/write access on db cocktailmachine
# $ mongo
# > use cocktailmachine
# db.createUser(
#   {
#     user: "barkeeper",
#     pwd: "barkeeper",
#     roles: [ { role: "readWrite", db: "cocktailmachine" } ]
#   }
# );
# MongoDB connection string: MongoClient('mongodb://barkeeper:barkeeper@127.0.0.1/cocktailmachine')
