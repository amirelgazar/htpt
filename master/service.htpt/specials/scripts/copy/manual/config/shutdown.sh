#!/bin/sh

LOGFILE='/storage/shutdown.log'

#DATENOW=`(date +%F)`
#TIMENOW=`(date +%H:%M)`
DATETIMENOW=`(date +%F__%H:%M)`
echo $DATETIMENOW

exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>$LOGFILE 2>&1

echo ----------------------------------------
#echo MODEL: $ID10   '|'   DATE: $DATENOW   '|'   USERID: $ID
echo ----------------------------------------

E='"'
F='false"'
T='true"'
VALUE=' value="'
ALL='[^ ]*"'
ModeOn_4='<setting id="ModeOn_4"' #SUSPEND
ModeOn_8='<setting id="ModeOn_8"' #REBOOT
ModeOn_10='<setting id="ModeOn_10"' #SPECIAL-POWEROFF

ModeTime_4='<setting id="ModeTime_4"' #SUSPEND
ModeTime_8='<setting id="ModeTime_8"' #REBOOT
ModeTime_10='<setting id="ModeTime_10"' #SPECIAL-POWEROFF

{ #GET ModeOn_10
SETTINGS='/storage/.kodi/userdata/addon_data/service.htpt.debug/settings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$SETTINGS
FINDWHAT='"ModeOn_10"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o 'value="[^ ]*"' | grep -o '"[^ ]*"' | sed 's/[""]//g'`
ModeOn_10='"'$FINDEXACT'"'
#echo $FINDLINE
echo ModeOn_10: $ModeOn_10 '('$FINDEXACT')'
}

{ #GET General_ScriptON
SETTINGS='/storage/.kodi/userdata/addon_data/service.htpt.debug/settings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$SETTINGS
FINDWHAT='"General_ScriptON"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o 'value="[^ ]*"' | grep -o '"[^ ]*"' | sed 's/[""]//g'`
General_ScriptON='"'$FINDEXACT'"'
echo $FINDLINE
echo General_ScriptON: $General_ScriptON '('$FINDEXACT')'
}

if [ $General_ScriptON == '"false"' ]; then
	echo General_ScriptON IS FALSE
	#echo SETTING ModeOn_4 '('HALT')' '=' TRUE
	sed -i "s/$ModeOn_4$VALUE$F/$ModeOn_4$VALUE$T/g" $SETTINGS
else
	echo General_ScriptON IS TRUE, ABORTING!
fi

exit
case "$1" in
  halt)
    # your commands here
	if [ $General_ScriptON == '"false"' ]; then
		echo General_ScriptON IS FALSE
		echo SETTING ModeOn_4 '('HALT')' '=' TRUE
		sed -i "s/$ModeOn_4$VALUE$F/$ModeOn_4$VALUE$T/g" $SETTINGS
		sed -i "s/$ModeTime_4$VALUE$ALL/$ModeTime_4$VALUE$DATETIMENOW$E/g" $SETTINGS
	else
		echo General_ScriptON IS TRUE, ABORTING!
	fi	
    ;;
  poweroff)
    # your commands here
	if [ $General_ScriptON == '"false"' ]; then
		echo General_ScriptON IS FALSE
		echo SETTING ModeOn_8 '('REBOOT')' '=' TRUE
		sed -i "s/$ModeOn_8$VALUE$F/$ModeOn_8$VALUE$T/g" $SETTINGS
		sed -i "s/$ModeTime_8$VALUE$ALL/$ModeTime_8$VALUE$DATETIMENOW$E/g" $SETTINGS
	else
		echo General_ScriptON IS TRUE, ABORTING!
	fi
    ;;
  reboot)
    # your commands here
	if [ $General_ScriptON == '"false"' ]; then
		echo General_ScriptON IS FALSE
		echo SETTING ModeOn_10 '('SPECIAL-POWEROFF')' '=' TRUE
		sed -i "s/$ModeOn_10$VALUE$F/$ModeOn_10$VALUE$T/g" $SETTINGS
		sed -i "s/$ModeTime_10$VALUE$ALL/$ModeTime_10$VALUE$DATETIMENOW$E/g" $SETTINGS
	else
		echo General_ScriptON IS TRUE, ABORTING!
	fi
    ;;
  *)
    # your commands here
    ;;
esac