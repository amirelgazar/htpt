#!/bin/bash

SERVICE_PATH=/storage/.kodi/addons/service.htpt
COPY_PATH=$SERVICE_PATH/specials/scripts/copy
USERDATA_PATH=$HOME/.kodi/userdata
MAIN_PATH=$HOME/.kodi

###GET Admin###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.Admin"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ADMIN='"'$FINDEXACT'"'
echo ADMIN: $Admin '('$FINDEXACT')'

if [ $ADMIN == '"false"' ]; then
	###ONCE###
	FOLDER_NAME=addon_data
	FOLDER1_PATH=$COPY_PATH/once/userdata
	FOLDER2_PATH=$USERDATA_PATH
	if [ -d $FOLDER1_PATH/$FOLDER_NAME ]; then
		cp -f -r $FOLDER1_PATH/$FOLDER_NAME/* $FOLDER2_PATH/$FOLDER_NAME
		echo COPY FOLDER: $FOLDER_NAME
		rm -r $FOLDER1_PATH/$FOLDER_NAME
		echo REMOVING FOLDER: $FOLDER_NAME
	fi
	
	FOLDER_NAME=addons
	FOLDER1_PATH=$COPY_PATH/once
	FOLDER2_PATH=$MAIN_PATH
	if [ -d $FOLDER1_PATH/$FOLDER_NAME ]; then
		cp -f -r $FOLDER1_PATH/$FOLDER_NAME/* $FOLDER2_PATH/$FOLDER_NAME
		echo COPY FOLDER: $FOLDER_NAME
		rm -r $FOLDER1_PATH/$FOLDER_NAME
		echo REMOVING FOLDER: $FOLDER_NAME
	fi
	
	###REPEAT###
	FOLDER_NAME=addons
	FOLDER1_PATH=$COPY_PATH/repeat/
	FOLDER2_PATH=$MAIN_PATH
	if [ -d $FOLDER1_PATH/$FOLDER_NAME ]; then
		cp -f -r $FOLDER1_PATH/$FOLDER_NAME/* $FOLDER2_PATH/$FOLDER_NAME
		echo COPY FOLDER: $FOLDER_NAME
	fi
	
	FOLDER_NAME=userdata
	FOLDER1_PATH=$COPY_PATH/repeat/
	FOLDER2_PATH=$MAIN_PATH/userdata
	if [ -d $FOLDER1_PATH/$FOLDER_NAME ]; then
		cp -f -r $FOLDER1_PATH/$FOLDER_NAME/* $FOLDER2_PATH/$FOLDER_NAME
		echo COPY FOLDER: $FOLDER_NAME
	fi
fi
