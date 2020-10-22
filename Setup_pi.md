## Prepare your RaspberryPi

I our case we use a RaspberryPi Zero. Execute the following steps or use our `setup_pi` script for the installation.

* Python3.8 **Prerequisites**

```
sudo apt-get install -y git build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
```

* Download Python3.8

```
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
```

* Install Python3.8

```
tar zxf Python-3.8.0.tgz
cd Python-3.8.0
./configure --enable-optimizations
# !attention! this takes very long...
make -j 4
make altinstall
```
* Set python3.8 as default and check version

```
echo "alias python=/usr/local/bin/python3.8" >>~/.bashrc
echo "alias python3=/usr/local/bin/python3.8" >>~/.bashrc
source ~/.bashrc
python -V
```

* Remove the installation binaries

```
cd
rm -r Python-3.8.0
rm Python-3.8.0.tgz
```

* Install pip

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install --upgrade pip
```

* Set PATH and create virtualenv

```
export PATH="$PATH:/home/pi/.local/bin"
virtualenv cocktailmachine
source cocktailmachine/bin/activate
```

* Clone project and install dependencies

```
git clone https://github.com/janosch09/cocktail-pi.git
cd cocktail-pi
pip install -r requirements.txt
apt-get install python3-dev python3-rpi.gpio -y
```

* Start the cocktailmachine!
    * ATTENTION: You need to add this to your settings.py: `ALLOWED_HOSTS = ["<RaspberryPi_IP>"]`
```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```