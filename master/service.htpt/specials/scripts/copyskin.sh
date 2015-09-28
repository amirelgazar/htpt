#!/bin/bash

DATENOW=`(date +%F)`
#echo $DATENOW

###GET USER ID###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID=$FINDEXACT
#echo ID: $ID

###GET USER ID10###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID10"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID10=$FINDEXACT
#echo ID10: $ID10

LOGFILE='/storage/copyskin.log'

exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>$LOGFILE 2>&1

echo ----------------------------------------
echo MODEL: $ID10   '|'   DATE: $DATENOW   '|'   USERID: $ID
echo ----------------------------------------

USERDATA_PATH=$HOME/.kodi/userdata
GUISETTINGS_FILE_CON1=`cat $USERDATA_PATH/guisettings.xml | grep -i "<skin>skin.htpt</skin>" | wc -l`
SKIN_PATH=/storage/.kodi/addons/skin.htpt
SERVICE_PATH=/storage/.kodi/addons/service.htpt
chmod +x $SKIN_PATH/specials/scripts/*
chmod +x $SERVICE_PATH/specials/scripts/*
chmod +x /storage/.config/autostart.sh
SKIN_FOLDER_SIZE=`du $SKIN_PATH/ -s | awk {'print $1'}`

{ #SKIN_CHECK
PRINTPOINT=""
echo
echo ----------------------------------------
echo GUISETTINGS_FILE_CON1: $GUISETTINGS_FILE_CON1
echo SKIN_FOLDER_SIZE: $SKIN_FOLDER_SIZE
if [ $GUISETTINGS_FILE_CON1 -eq 0 ] && [ $SKIN_FOLDER_SIZE -le 50000 ] || [ $GUISETTINGS_FILE_CON1 -eq 0 ] && [ ! -d "$SKIN_PATH" ]; then
	PRINTPOINT=$PRINTPOINT\1
	ls $HOME/.kodi/addons/packages/skin.htpt* -r | awk {'print $1'} | tee /storage/skinpackage.log
	SKIN_FILE1=`head -1 skinpackage.log`
	SKIN_FILE1_SIZE=`du $SKIN_FILE1 -s | awk {'print $1'}`
	SKIN_FILE2=`sed -n 2p skinpackage.log`
	SKIN_FILE2_SIZE=`du $SKIN_FILE2 -s | awk {'print $1'}`
	SKIN_FILE3=`sed -n 3p skinpackage.log`
	SKIN_FILE3_SIZE=`du $SKIN_FILE3 -s | awk {'print $1'}`
	echo SKIN_FILE3: $SKIN_FILE3 - $SKIN_FILE3_SIZE
	echo SKIN_FILE2: $SKIN_FILE2 - $SKIN_FILE2_SIZE
	echo SKIN_FILE1: $SKIN_FILE1 - $SKIN_FILE1_SIZE
	
	if [ $SKIN_FILE3_SIZE -gt 30000 ] && [ -f $SKIN_FILE3 ] && [ $SKIN_FILE3_SIZE -le 120000 ]; then
		echo EXTRACTING SKIN_FILE3
		unzip -o -q $SKIN_FILE3 -d /storage/.kodi/addons/
		rm $SKIN_FILE3
	else
		if [ $SKIN_FILE2_SIZE -gt 30000 ] && [ -f $SKIN_FILE2 ] && [ $SKIN_FILE2_SIZE -le 120000 ]; then
			echo EXTRACTING SKIN_FILE2
			unzip -o -q $SKIN_FILE2 -d /storage/.kodi/addons/
			rm $SKIN_FILE2
		else
			if [ $SKIN_FILE1_SIZE -gt 30000 ] && [ -f $SKIN_FILE1 ] && [ $SKIN_FILE1_SIZE -le 120000 ]; then
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
	
else
	PRINTPOINT=$PRINTPOINT\7
fi
echo
echo SKIN_CHECK_LV: $PRINTPOINT
echo ----------------------------------------
}

if [ $GUISETTINGS_FILE_CON1 -eq 0 ] && [ -d "$SKIN_PATH" ]; then
	/storage/.kodi/addons/skin.htpt/specials/scripts/copy.sh
	SKIN='<skin>'
	SKIN2='<skin default="true">'
	SKIN_='skin.htpt<'
	ALL='[^ ]*<'
	
	echo executing copy.sh from skin && sleep 1 && echo killall && killall -9 kodi.bin && sed -i "s/$SKIN$ALL/$SKIN$SKIN_/g" $GUI && sed -i "s/$SKIN2$ALL/$SKIN$SKIN_/g" $GUI
fi
