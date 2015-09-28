#!/bin/bash
SETTINGS=$HOME/.kodi/userdata/guisettings.xml


T='true'
F='false'
ALL='[^ ]*<'
RESET=$F
VALIDATION2='"skin.htpt.VALIDATION2">'
MAC1='"skin.htpt.MAC1">'
MAC2='"skin.htpt.MAC2">'
ID1='"skin.htpt.ID1">'
ID2='"skin.htpt.ID2">'
ID3='"skin.htpt.ID3">'
ID4='"skin.htpt.ID4">'
ID5='"skin.htpt.ID5">'
ID6='"skin.htpt.ID6">'
ID7='"skin.htpt.ID7">'
ID8='"skin.htpt.ID8">'
ID9='"skin.htpt.ID9">'
ID10='"skin.htpt.ID10">'
VALIDATION2=`cat $USERDATA_PATH/guisettings.xml | grep -i $VALIDATION2$F | wc -l`
TRIAL2='"skin.htpt.Trial2">'
TRIALDATE2='"skin.htpt.TrialDate2">'
TRIALDATE='"skin.htpt.TrialDate">'
###GET USER ID###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID='"'$FINDEXACT'"'
IDP='"gkalni"'
echo ID: $ID '('$FINDEXACT')'

###GET USER ID9###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID9"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID9='"'$FINDEXACT'"'
echo ID9: $ID9 '('$FINDEXACT')'

###GET USER ID2###
GUI='/storage/.kodi/userdata/guisettings.xml'
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID2"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID2='"'$FINDEXACT'"'
echo ID2: $ID2 '('$FINDEXACT')'

if [ $VALIDATION2 -eq 1 ]; then
	echo VALIDATION2 = FALSE ON LAST RUN!
else
	###PLEASE CONFIRM WITH YOUR TECHNICAL OR CLIENT BEFORE REMOVING THE SETTINGS BELOW###
	if [ $ID == '"htptuser"' ]; then
		#VALUE='C0:3F:D5:68:A8:DC<'
		#sed -i "s/$MAC1$ALL/$MAC1$VALUE/g" $SETTINGS ###LAN
		#VALUE='A0:A8:CD:31:F7:D6<'
		#sed -i "s/$MAC2$ALL/$MAC2$VALUE/g" $SETTINGS ###WLAN
		echo CHANGING MAC FOR $ID
	fi
fi

exit	
	if [ $TRIAL2 == $T ]; then
		
	if [ $ID == '"htptuser4"' ]; then
		#VALUE='C0:3F:D5:68:A8:DC<'
		#sed -i "s/$MAC1$ALL/$MAC1$VALUE/g" $SETTINGS ###LAN
		#VALUE='A0:A8:CD:31:F7:D6<'
		#sed -i "s/$MAC2$ALL/$MAC2$VALUE/g" $SETTINGS ###WLAN
		echo CHANGING MAC FOR $ID
	fi
fi
