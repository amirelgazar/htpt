#!/bin/bash

SERVICE_PATH=/storage/.kodi/addons/service.htpt
COPY_PATH=$SERVICE_PATH/specials/scripts/copy
RETROARCH_PATH=$HOME/emulators/retroarch
RETROARCH_PATH2=$COPY_PATH/repeat/emulators/retroarch
USERDATA_PATH=$HOME/.kodi/userdata

#if [ ! -d "$HOME/emulators/" ]; then
	#echo CREATING EMULATORS_PATH!!!
	#mkdir -p $HOME/emulators/
#fi

###GET USER ID###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID='"'$FINDEXACT'"'
IDP='"gkalni"'
echo ID: $ID '('$FINDEXACT')'

###GET VALIDATION2###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.VALIDATION2"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
VALIDATION2='"'$FINDEXACT'"'
echo VALIDATION2: $VALIDATION2 '('$FINDEXACT')'

###GET ID10###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID10"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID10='"'$FINDEXACT'"'
echo ID10: $ID10 '('$FINDEXACT')'

if [ $VALIDATION2 == '"true"' ]; then
	if [ $ID10 == '"A"' ]; then

		FOLDER_NAME=config
		FOLDER1_PATH=$RETROARCH_PATH2/$FOLDER_NAME
		FOLDER2_PATH=$RETROARCH_PATH/$FOLDER_NAME
		if [ ! -d "$FOLDER2_PATH" ]; then
			echo CREATING FOLDER: $FOLDER_NAME
			mkdir -p $FOLDER2_PATH
		fi
		PERMISSION_FILE_SAMPLE=retroarch.cfg
		PERMISSION1=`ls -l $FOLDER2_PATH/$PERMISSION_FILE_SAMPLE | awk {'print $1'}`
		cp -f -r $FOLDER1_PATH/.* $FOLDER2_PATH/
		chmod +x $FOLDER2_PATH/*
		PERMISSION2=`ls -l $FOLDER2_PATH/$PERMISSION_FILE_SAMPLE | awk {'print $1'}`
		echo COPY FOLDER: $FOLDER_NAME - $PERMISSION1 -'>' $PERMISSION2

		FOLDER_NAME=cfg
		FOLDER1_PATH=$RETROARCH_PATH2/save/mame/$FOLDER_NAME
		FOLDER2_PATH=$RETROARCH_PATH/save/mame/$FOLDER_NAME
		if [ ! -d "$FOLDER2_PATH" ]; then
			echo CREATING FOLDER: $FOLDER_NAME
			mkdir -p $FOLDER2_PATH
		fi
		PERMISSION_FILE_SAMPLE=default.cfg
		PERMISSION1=`ls -l $FOLDER2_PATH/$PERMISSION_FILE_SAMPLE | awk {'print $1'}`
		cp -f $FOLDER1_PATH/* $FOLDER2_PATH/
		chmod +x $FOLDER2_PATH/*
		PERMISSION2=`ls -l $FOLDER2_PATH/$PERMISSION_FILE_SAMPLE | awk {'print $1'}`
		echo COPY FOLDER: $FOLDER_NAME - $PERMISSION1 -'>' $PERMISSION2

	fi
else
	echo VALIDATION2 = $VALIDATION2 '('copy cfg files')'
fi

###GET ADULT###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.Adult"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ADULT='"'$FINDEXACT'"'
echo ADULT: $ADULT '('$FINDEXACT')'



LAUNCHER_FILE=launchers.xml
LAUNCHER_PATH=$USERDATA_PATH/addon_data/skin.htpt/userdata
if [ ! -d "$LAUNCHER_PATH" ]; then
	echo CREATING FOLDER: $LAUNCHER_PATH
	mkdir -p $LAUNCHER_PATH
fi
LAUNCHER_PATH2=$COPY_PATH/repeat/launchers


if [ $ID10 == '"A"' ] && [ $ADULT == '"false"' ]; then
	LAUNCHER_FILE2=launchers_A.xml
	PERMISSION1=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	cp -f $LAUNCHER_PATH2/$LAUNCHER_FILE2 $LAUNCHER_PATH/$LAUNCHER_FILE
	chmod +x $LAUNCHER_PATH/$LAUNCHER_FILE
	PERMISSION2=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	echo COPY FILE: $LAUNCHER_FILE2 - $PERMISSION1 -'>' $PERMISSION2
fi

if [ $ID10 == '"A"' ] && [ $ADULT == '"true"' ]; then
	LAUNCHER_FILE2=launchers_AA.xml
	PERMISSION1=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	cp -f $LAUNCHER_PATH2/$LAUNCHER_FILE2 $LAUNCHER_PATH/$LAUNCHER_FILE
	chmod +x $LAUNCHER_PATH/$LAUNCHER_FILE
	PERMISSION2=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	echo COPY FILE: $LAUNCHER_FILE2 - $PERMISSION1 -'>' $PERMISSION2
fi

if [ $ID10 == '"B"' ] && [ $ADULT == '"false"' ]; then
	LAUNCHER_FILE2=launchers_B.xml
	PERMISSION1=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	cp -f $LAUNCHER_PATH2/$LAUNCHER_FILE2 $LAUNCHER_PATH/$LAUNCHER_FILE
	chmod +x $LAUNCHER_PATH/$LAUNCHER_FILE
	PERMISSION2=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	echo COPY FILE: $LAUNCHER_FILE2 - $PERMISSION1 -'>' $PERMISSION2
fi

if [ $ID10 == '"B"' ] && [ $ADULT == '"true"' ]; then
	LAUNCHER_FILE2=launchers_BA.xml
	PERMISSION1=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	cp -f $LAUNCHER_PATH2/$LAUNCHER_FILE2 $LAUNCHER_PATH/$LAUNCHER_FILE
	chmod +x $LAUNCHER_PATH/$LAUNCHER_FILE
	PERMISSION2=`ls -l $LAUNCHER_PATH/$LAUNCHER_FILE | awk {'print $1'}`
	echo COPY FILE: $LAUNCHER_FILE2 - $PERMISSION1 -'>' $PERMISSION2
fi