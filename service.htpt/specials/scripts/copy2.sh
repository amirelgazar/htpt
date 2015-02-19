#!/bin/bash

SERVICE_PATH=/storage/.kodi/addons/service.htpt
COPY_PATH=$SERVICE_PATH/specials/scripts/copy
USERDATA_PATH=$HOME/.kodi/userdata

###GET Admin###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.Admin"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ADMIN='"'$FINDEXACT'"'
echo ADMIN: $Admin '('$FINDEXACT')'

if [ $ADMIN == '"false"' ]; then
	FILENAME=autostart.sh
	FILE1_PATH=$SERVICE_PATH/specials/scripts/copy/repeat/config
	FILE2_PATH=$HOME/.config
	PERMISSION1=`ls -l $FILE2_PATH/$FILENAME | awk {'print $1'}`
	cp -f $FILE1_PATH/$FILENAME $FILE2_PATH/$FILENAME
	chmod +x $FILE2_PATH/$FILENAME
	PERMISSION2=`ls -l $FILE2_PATH/$FILENAME | awk {'print $1'}`
	echo COPY: $FILENAME - $PERMISSION1 -'>' $PERMISSION2
	
	FILENAME=samba.conf
	PERMISSION1=`ls -l $FILE2_PATH/$FILENAME | awk {'print $1'}`
	cp -f $FILE1_PATH/$FILENAME $FILE2_PATH/$FILENAME
	chmod +x $FILE2_PATH/$FILENAME
	PERMISSION2=`ls -l $FILE2_PATH/$FILENAME | awk {'print $1'}`
	echo COPY: $FILENAME - $PERMISSION1 -'>' $PERMISSION2
	
	FILENAME=oemsplash.png
	FILE1_PATH=$SERVICE_PATH/specials/scripts/copy/repeat/flash
	FILE2_PATH=/flash
	if [ ! -f $FILE2_PATH/$FILENAME ]; then
		mount -o remount,rw /flash
		PERMISSION1=`ls -l $FILE2_PATH/$FILENAME | awk {'print $1'}`
		cp -f $FILE1_PATH/$FILENAME $FILE2_PATH/$FILENAME
		chmod +x $FILE2_PATH/$FILENAME
		PERMISSION2=`ls -l $FILE2_PATH/$FILENAME | awk {'print $1'}`
		echo COPY: $FILENAME - $PERMISSION1 -'>' $PERMISSION2
	fi	
	
fi




