#!/bin/sh
echo "Open README first
Choose:
  1 to install only fbcp
  2 to install only FBCPconfig software for BlockComPi (install fbcp first)"
read option
#####fbcp###################################################################
if [ $option -eq 1 ]
then
cd /tmp
sudo apt-get install cmake
git clone https://github.com/tasanakorn/rpi-fbcp
cd rpi-fbcp/
mkdir build
cd build
cmake ..
make
sudo install fbcp /usr/local/bin/fbcp
cd -
echo 'Done installing fbcp'
####HDMIconfig####################################################################
elif [ $option -eq 2 ]
then
echo "Enter the directory the App.py file of the BlockComPi software is in"
echo "eg. /home/pi/BlockComPiSoftware/App.py"
read Appdir
echo "Enter the App folder (after copying it over)"
echo "eg. /home/pi/FBCPconfig"
read Installdir
echo "def app():
  os.system('cd "$Installdir" && python FBCPconfig.py &')
def exit():
  os.system('pkill fbcp')
  os.system('pkill -f FBCPconfig.py')
  os.system('sleep 1')
  os.system('rmmod fb_ili9340')# Change rotation
  os.system('rmmod fbtft_device')# Change rotation
  os.system('modprobe fbtft_device name=pitft rotate=180')# Change rotation
  os.system('adafruit-pitft-touch-cal -f -r 180')# Change rotation
FBCPconf = ('FBCPconf', orange, 24, app, exit)
programs.append(FBCPconf)" >> $Appdir
echo 'Done installing FBCPconfig software for BlockComPi'
fi
