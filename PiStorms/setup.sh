#!/bin/bash
#
# Copyright (c) 2015 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# Oct. 2015 Nitin       Library and Driver installation
# Oct. 2015 Michael     I2C configuration and startup

#setup i2c and spi 
if [ -e /boot/config.txt ]
then
    echo "Updating config files..."
    sudo rm -f /boot/config.txt
    sudo cp config.txt /boot/config.txt
else
    echo "Copying config files..."
    sudo cp config.txt /boot/config.txt
fi
#
#
echo "Updating installations files. This may take several minutes..."
sudo apt-get update -qq
echo "Installing packages..."
sudo apt-get install -qq mpg123 build-essential python-dev python-smbus python-pip python-imaging python-numpy git
#
#

sudo sed -i 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/g' /etc/modprobe.d/raspi-blacklist.conf
grep i2c-bcm2708 /etc/modules > /dev/null
if [ $? == 0 ]
then
    echo "i2c-bcm2708 already installed"
else
    sudo sed -i -e '$i \i2c-bcm2708\n' /etc/modules
    #sudo echo 'i2c-bcm2708' >> /etc/modules
fi

grep i2c-dev /etc/modules > /dev/null
if [ $? == 0 ]
then
    echo "i2c-dev already installed"
else
    sudo sed -i -e '$i \i2c-dev\n' /etc/modules
    #sudo echo 'i2c-dev' >> /etc/modules
fi
sudo pip install -qq RPi.GPIO

echo "Copying libraries..."
#for pistorms only
sudo cp PiStorms.py /usr/local/lib/python2.7/dist-packages/PiStorms.py
sudo cp PiStormsDriver.py /usr/local/lib/python2.7/dist-packages/PiStormsDriver.py

sudo cp PiStormsBrowser.py /usr/local/lib/python2.7/dist-packages/PiStormsBrowser.py
sudo cp PiStormsCom.py /usr/local/lib/python2.7/dist-packages/PiStormsCom.py
#common files
sudo cp mindsensors_i2c.py /usr/local/lib/python2.7/dist-packages/mindsensors_i2c.py
sudo cp mindsensorsUI.py /usr/local/lib/python2.7/dist-packages/mindsensorsUI.py
sudo cp mindsensors.py /usr/local/lib/python2.7/dist-packages/mindsensors.py

sudo mkdir -p /usr/local/lib/python2.7/dist-packages/mindsensors_images
sudo cp *.png /usr/local/lib/python2.7/dist-packages/mindsensors_images/
sudo chmod a+r /usr/local/lib/python2.7/dist-packages/mindsensors_images/*

echo "Copying drivers..."
sudo cp PiStormsDriver.sh /etc/init.d
sudo cp PiStormsBrowser.sh /etc/init.d

#
# insert into startup scripts for subsequent use
#
echo "Updating Startup scripts..."
sudo update-rc.d PiStormsDriver.sh defaults 95 05
sudo update-rc.d PiStormsBrowser.sh defaults 96 04

#setup messenger
echo "Setting up messenger...."
sudo cp ps_messenger_check.py /usr/local/lib/python2.7/dist-packages
sudo touch /var/tmp/ps_data.json
sudo chmod a+rw /var/tmp/ps_data.json
# setup crontab entry for root
sudo crontab -l -u root | grep ps_messenger_check > /dev/null
if [ $? != 0 ]
then
    (sudo crontab -l -u root 2>/dev/null; echo "*/5 * * * * python /usr/local/lib/python2.7/dist-packages/ps_messenger_check.py") | sudo crontab - -u root
fi
# run the messenger once
python /usr/local/lib/python2.7/dist-packages/ps_messenger_check.py > /dev/null


echo "Installing image libraries..."
cd ~
git clone -qq https://github.com/adafruit/Adafruit_Python_ILI9341.git
cd Adafruit_Python_ILI9341
sudo python setup.py -q install
cd  .. 
sudo rm -rf Adafruit_Python_ILI9341

echo "-----------------------------"
echo "Install completed.   "
echo "Please reboot your Raspberry Pi for changes to take effect."
echo "-----------------------------"
