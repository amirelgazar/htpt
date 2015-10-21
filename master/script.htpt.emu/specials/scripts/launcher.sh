#!/bin/bash

USERDATA_PATH=$HOME/.kodi/userdata
LAUNCHER_FILE=launchers.xml
LAUNCHER_PATH=$USERDATA_PATH/addon_data/plugin.program.advanced.launcher
LAUNCHER_PATH2=$USERDATA_PATH/addon_data/script.htpt.emu

if [ ! -d $LAUNCHER_PATH ]; then
	echo CREATING FOLDER: $LAUNCHER_PATH
	mkdir $LAUNCHER_PATH
	/storage/.kodi/addons/service.htpt/specials/scripts/copyonce.sh
fi
LAUNCHER_FILE_SIZE=`du -k "$LAUNCHER_PATH/$LAUNCHER_FILE" | cut -f1`
LAUNCHER_FILE2_SIZE=`du -k "$LAUNCHER_PATH2/$LAUNCHER_FILE" | cut -f1`
echo LAUNCHER_FILE_SIZE '(1/2-original)': $LAUNCHER_FILE_SIZE/$LAUNCHER_FILE2_SIZE

if [ $LAUNCHER_FILE_SIZE != $LAUNCHER_FILE2_SIZE  ] || [ ! -f "$LAUNCHER_PATH/$LAUNCHER_FILE" ]; then
	LAUNCHER_FILE2=launchers_A.xml
	PERMISSION1=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	cp -f $LAUNCHER_PATH2/$LAUNCHER_FILE $LAUNCHER_PATH/$LAUNCHER_FILE
	chmod +x $LAUNCHER_PATH/$LAUNCHER_FILE
	PERMISSION2=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	echo COPY FILE: $LAUNCHER_FILE - $PERMISSION1 -'>' $PERMISSION2
	sleep 1
fi

exit
###BLUETOOTH TEST###
#modprobe btusb #Load the generic bluetooth driver, if not already loaded
#systemctl start bluetooth #To start the bluetooth systemd service
#systemctl enable bluetooth #To enable the bluetooth service at boot time

#rm -rf /storage/.cache/bluetooth/* 

#test1 = echo -e bluetoothctl | bluetoothctl
#val=$(cut -d " " -f3 $test1)
#echo test1
#echo $val
#test2 = `test1 | grep -i "xx_xx_xx_xx_xx_xx" | wc -l`
#echo test2
#sleep 1
#echo -e nquit
#echo -e 'power on\nconnect \t \nquit' | bluetoothctl
#devices = echo -e 'power on\nconnect \t \nquit' | bluetoothctl | grep -o 'name=[^ ,]\+' | wc -l

#quit
#devices
#devices =' grep
#devices =`devices | grep -i "xx_xx_xx_xx_xx_xx" | wc -l`

#echo awk '{print $3}`


#echo "eth0 ($LAN2) --> Turned on!"

#cp $HOME/.kodi/addons/skin.htpt/specials/scripts/copy/keymaps/* $HOME/.kodi/userdata/keymaps/
#cp $HOME/.kodi/addons/skin.htpt/specials/scripts/copy/userdata/* $HOME/.kodi/userdata/
#BACKUP=$HOME/.kodi/addons/skin.htpt/specials/launchers.xml
#RESTORE=$HOME/.kodi/userdata/addon_data/plugin.program.advanced.launcher/
#
#cp $BACKUP $RESTORE