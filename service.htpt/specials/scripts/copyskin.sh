#!/bin/bash

USERDATA_PATH=$HOME/.kodi/userdata
GUISETTINGS_FILE_CON1=`cat $USERDATA_PATH/guisettings.xml | grep -i "<skin>skin.htpt</skin>" | wc -l`
SKIN_PATH=/storage/.kodi/addons/skin.htpt
SERVICE_PATH=/storage/.kodi/addons/service.htpt
chmod +x $SKIN_PATH/specials/scripts/*
chmod +x $SERVICE_PATH/specials/scripts/*
chmod +x /storage/.config/autostart.sh
SKIN_FOLDER_SIZE=`du $SKIN_PATH/ -s | awk {'print $1'}`
if [ $GUISETTINGS_FILE_CON1 -eq 0 ] && [ $SKIN_FOLDER_SIZE -le 50000 ] || [ $GUISETTINGS_FILE_CON1 -eq 0 ] && [ ! -d "$SKIN_PATH" ]; then
	echo ERROR: SKIN FOLDER '(SIZE/EMPTY)'
	ls $HOME/.kodi/addons/packages/skin.htpt* -r | awk {'print $1'} | tee /storage/skinpackage.log
	SKIN_FILE1=`head -1 skinpackage.log`
	SKIN_FILE1_SIZE=`du $SKIN_FILE1 -s | awk {'print $1'}`
	SKIN_FILE2=`sed -n 2p skinpackage.log`
	SKIN_FILE2_SIZE=`du $SKIN_FILE2 -s | awk {'print $1'}`
	SKIN_FILE3=`sed -n 3p skinpackage.log`
	SKIN_FILE3_SIZE=`du $SKIN_FILE3 -s | awk {'print $1'}`
	
	if [ $SKIN_FILE3_SIZE -gt 50000 ] && [ -f SKIN_FILE3 ]; then
		echo EXTRACTING SKIN_FILE3
		unzip -o -q $SKIN_FILE3 -d /storage/.kodi/addons/
		rm $SKIN_FILE3
	else
		if [ $SKIN_FILE2_SIZE -gt 50000 ] && [ -f SKIN_FILE2 ]; then
			echo EXTRACTING SKIN_FILE2
			unzip -o -q $SKIN_FILE2 -d /storage/.kodi/addons/
			rm $SKIN_FILE2
		else
			if [ $SKIN_FILE1_SIZE -gt 50000 ] && [ -f SKIN_FILE1 ]; then
				echo EXTRACTING SKIN_FILE1
				unzip -o -q $SKIN_FILE1 -d /storage/.kodi/addons/
				#rm $SKIN_FILE1
			else
				echo ERROR: NO ZIP FILES TO EXTRACT!!!
				#SKIN_FILE4=`ls $SERVICE_PATH/specials/scripts/copy/skin.htpt*.zip -r | awk {'print $1'}`
				#echo EXTRACTING FROM service.htpt
				#unzip -o -q $SKIN_FILE4 -d /storage/.kodi/addons/
			fi
		fi		
	fi	
	
	sleep 5 && chmod +x $SKIN_PATH/specials/scripts/* && echo killall && killall -9 kodi.bin
	exit
fi
if [ $GUISETTINGS_FILE_CON1 -eq 0 ]; then
	/storage/.kodi/addons/skin.htpt/specials/scripts/copy.sh
	echo executing copy.sh from skin && echo killall && killall -9 kodi.bin
fi
