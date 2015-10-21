#!/bin/bash

LOGFILE='/storage/remote.log'

DATENOW=`(date +%F)`
PRINTPOINT=""
#echo $DATENOW

exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>$LOGFILE 2>&1

echo ----------------------------------------
echo DATE: $DATENOW
echo ----------------------------------------

IREXE='FALSE'

ADDON_NAME=script.htpt.remote
ADDON_PATH=$HOME/.kodi/addons/$ADDON_NAME
ADDON_USERDATA_PATH=$HOME/.kodi/userdata/addon_data/$ADDON_NAME
ADDON_SETTINGS=$ADDON_USERDATA_PATH/settings.xml

REMOTES_PATH=$ADDON_PATH/resources/remotes

#echo `cat $ADDON_SETTINGS`
FINDIN=$ADDON_SETTINGS
FINDWHAT='"Remote_Name"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o 'value="[^ ]*"' | grep -o '"[^ ]*"' | sed 's/[<">]//g'`
REMOTE_TYPE=$FINDEXACT
echo REMOTE_TYPE: $REMOTE_TYPE

FINDIN=$ADDON_SETTINGS
FINDWHAT='"Remote_Name2"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o 'value="[^ ]*"' | grep -o '"[^ ]*"' | sed 's/[<">]//g'`
REMOTE_TYPE_TEMP=$FINDEXACT

echo REMOTE_TYPE_TEMP: $REMOTE_TYPE_TEMP

USERDATA_PATH=$HOME/.kodi/userdata
GUI=$USERDATA_PATH/guisettings.xml
FINDIN=$GUI
FINDWHAT='"skin.htpt.IRtype"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
IRTYPE=$FINDEXACT
echo IRTYPE: $IRTYPE '('$FINDEXACT')'


echo __________________________
{ #
if [ $REMOTE_TYPE_TEMP != "" ] && [ $REMOTE_TYPE_TEMP != None ]; then
	PRINTPOINT=$PRINTPOINT\1
	REMOTE_FILE=$REMOTE_TYPE_TEMP
	
	if [ $REMOTE_TYPE_TEMP == samsung ] || [ $REMOTE_TYPE_TEMP == lg ] || [ $REMOTE_TYPE_TEMP == philips ] || [ $REMOTE_TYPE_TEMP == toshiba ] || [ $REMOTE_TYPE_TEMP == pilot ] || [ $REMOTE_TYPE_TEMP == sharp ]; then
		PRINTPOINT=$PRINTPOINT\2
		R_TYPE=nec,rc-6
	fi
	echo TESTING REMOTE: $REMOTE_TYPE_TEMP '('$R_TYPE')'
	ir-keytable -c
	sleep 1

else
	PRINTPOINT=$PRINTPOINT\4
	if [ $REMOTE_TYPE != "" ] && [ $REMOTE_TYPE != None ]; then
		PRINTPOINT=$PRINTPOINT\5
		REMOTE_FILE=$REMOTE_TYPE
	
		if [ $REMOTE_TYPE == samsung ] || [ $REMOTE_TYPE == lg ] || [ $REMOTE_TYPE == philips ] || [ $REMOTE_TYPE == toshiba ] || [ $REMOTE_TYPE == pilot ] || [ $REMOTE_TYPE == sharp ]; then
			PRINTPOINT=$PRINTPOINT\6
			R_TYPE=nec,rc-6
		fi
		echo CHOOSEN REMOTE: $REMOTE_TYPE '('$R_TYPE')'
	else
		PRINTPOINT=$PRINTPOINT\9
	fi
fi
}

echo REMOTE FILE: $REMOTES_PATH/$REMOTE_FILE
{ #
if [ $REMOTE_TYPE_TEMP != "" ] || [ $REMOTE_TYPE != "" ]; then
	PRINTPOINT=$PRINTPOINT\A
	echo "1"
	if [ $REMOTE_TYPE != None ]; then
		PRINTPOINT=$PRINTPOINT\B
		IREXE='TRUE'
	fi
	if [ $REMOTE_TYPE_TEMP != None ]; then
		PRINTPOINT=$PRINTPOINT\C
		IREXE='TRUE'
	fi
	
	if [ $IREXE == 'TRUE' ]; then
		PRINTPOINT=$PRINTPOINT\D
		ir-keytable -p $R_TYPE -w $REMOTES_PATH/$REMOTE_FILE -D 700 -P 200
	else
		PRINTPOINT=$PRINTPOINT\F
	fi
else
	PRINTPOINT=$PRINTPOINT\G
fi
}

echo
echo REMOTE_CHECK_LV: $PRINTPOINT
echo ----------------------------------------