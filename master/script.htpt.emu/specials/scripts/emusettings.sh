#!/bin/bash
SETTINGS_PATH=/storage/emulators/retroarch
FILE1=retroarch.cfg
FILE2=nestopia_libretro.so.cfg
FILE3=snes9x_next_libretro.so.cfg
FILE4=genesis_plus_gx_libretro.so.cfg
FILE5=mame2014_libretro.so.cfg
FILE6=mednafen_pce_fast_libretro.so.cfg
FILE7=mednafen_psx_libretro.so.cfg
FILE8=mupen64plus_libretro.so.cfg
FILE9=desmume_libretro.so.cfg
#FILE10=desmume_libretro.so.cfg

###VIDEO###
VIDEO1='video_black_frame_insertion'
VIDEO2='<setting id="video_refresh_rate=" value='
#VIDEO3='"video_black_frame_insertion" value='

###AUDIO###
AUDIO1='<setting id="audio_device" value='
AUDIO2='<setting id="audio_latency" value='
AUDIO3='<setting id="audio_out_rate" value='
AUDIO4='<setting id="audio_sync" value='

###VAR GENERAL###
E='""'
T='"true"'
F='"false"'
ALL='"[^ ]*"'
NUM1='"1"'
NUM0='"0"'

###GET AUDIO1###
SETTINGS='/storage/.kodi/userdata/addon_data/script.htpt.emu/settings.xml'
FINDIN=$SETTINGS
FINDWHAT=$VIDEO1
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '=[^ ]*'`
#FINDEXACT=`echo $FINDLINE | grep -o 'value="[^ ]*"' | sed 's/[<>]//g'`
VIDEO1='"'$FINDEXACT'"'
echo VIDEO1: $VIDEO1 '('$FINDEXACT')'


exit
###SED RealDebrid###
if [ $REALDEBRID == $T ] || [ $ID9 == $TRIAL ] || [ $ID2 == $DATENOW ]; then
	if [ `echo $REALDEBRID2 | grep 'htpt' ` ] && [ $ID != $REALDEBRID2 ] && [ $ID9 != $TRIAL ] && [ $ID2 != $DATENOW ]; then
		sed -i "s/$REALDEDRIDUSER$ALL/$REALDEDRIDUSER$ID/g" $SETTINGS
		sed -i "s/$REALDEDRIDPASS$ALL/$REALDEDRIDPASS$IDP/g" $SETTINGS
		echo REALDEBRID RESET '('$ID != $REALDEBRID2')'
	else
		if [ $ID9 == $TRIAL ] || [ $ID2 == $DATENOW ]; then
			sed -i "s/$REALDEDRIDUSER$ALL/$REALDEDRIDUSER$IDTRIAL/g" $SETTINGS
			sed -i "s/$REALDEDRIDPASS$ALL/$REALDEDRIDPASS$IDPTRIAL/g" $SETTINGS
			echo REALDEBRID TRIAL '('$ID9')' OR DATENOW '('$DATENOW')'
		else
			sed -i "s/$REALDEDRIDUSER$E/$REALDEDRIDUSER$ID/g" $SETTINGS
			sed -i "s/$REALDEDRIDPASS$E/$REALDEDRIDPASS$IDP/g" $SETTINGS
			echo REALDEBRID DEFAULT
		fi
		
	fi
else
	sed -i "s/$REALDEDRIDUSER$ALL/$REALDEDRIDUSER$E/g" $SETTINGS
	sed -i "s/$REALDEDRIDPASS$ALL/$REALDEDRIDPASS$E/g" $SETTINGS
	echo REALDEBRID NONE
fi

###SED USERS###
sed -i "s/$FURKUSER$ALL/$FURKUSER$E/g" $SETTINGS
sed -i "s/$FURKPASS$ALL/$FURKPASS$E/g" $SETTINGS
sed -i "s/$MOVREELUSER$ALL/$MOVREELUSER$ID/g" $SETTINGS
sed -i "s/$MOVREELPASS$ALL/$MOVREELPASS$IDP/g" $SETTINGS
sed -i "s/$TRACKTUSER$ALL/$TRACKTUSER$ID/g" $SETTINGS
sed -i "s/$TRACKTPASS$ALL/$TRACKTPASS$IDP/g" $SETTINGS
###SED USERS REMOVE###
#sed -i "s/$TRACKTUSER$ALL/$TRACKTUSER$E/g" $SETTINGS
#sed -i "s/$TRACKTPASS$ALL/$TRACKTPASS$E/g" $SETTINGS

###SED FIX###
sed -i "s/$CHECKLIBRARY$F/$CHECKLIBRARY$T/g" $SETTINGS ###AVOID DUPLICATES ON###
sed -i "s|$DOWNLOADS$ALL|$DOWNLOADS$DOWNLOADSPATH|g" $SETTINGS ###FIXED PATH###
sed -i "s|$HOSTSELECT$ALL|$HOSTSELECT$NUM0|g" $SETTINGS ###HOST SELECTION WINDOW = DIALOG###
sed -i "s|$IMDBUSER$ALL|$IMDBUSER$IMDBSTRING|g" $SETTINGS ###FIXED###
sed -i "s|$MOVIELIBRARY$ALL|$MOVIELIBRARY$MOVIEPATH|g" $SETTINGS ###FIXED PATH###
sed -i "s/$PLAYHD$F/$PLAYHD$T/g" $SETTINGS ###DETAILS ON###
sed -i "s/$RESUMEPLAYBACK$F/$RESUMEPLAYBACK$T/g" $SETTINGS ###RESUME ON###
sed -i "s/$ROOTMOVIES$ALL/$ROOTMOVIES$NUM0/g" $SETTINGS ###ROOT LINKS OFF###
sed -i "s/$ROOTEPISODESTRAKT$ALL/$ROOTEPISODESTRAKT$NUM0/g" $SETTINGS ###ROOT LINKS OFF###
sed -i "s/$ROOTEPISODES$ALL/$ROOTEPISODES$NUM0/g" $SETTINGS ###ROOT LINKS OFF###
sed -i "s/$ROOTCALENDAR$ALL/$ROOTCALENDAR$NUM0/g" $SETTINGS ###ROOT LINKS OFF###
sed -i "s|$SERVICEINTERVAL$ALL|$SERVICEINTERVAL$NUM0|g" $SETTINGS ###AUTO UPDATE TIME = 2H###
sed -i "s/$SERVICELIMIT$T/$SERVICELIMIT$F/g" $SETTINGS ###ADD ONLY LAST SEASON (AUTO UPDATE) OFF###
sed -i "s/$SERVICEUPDATE$F/$SERVICEUPDATE$T/g" $SETTINGS ###AUTO UPDATE EPISODES ON###
sed -i "s|$SUBLANG1$ALL|$SUBLANG1$HE|g" $SETTINGS ###AUTO SUB = HEBREW###
sed -i "s|$SUBLANG2$ALL|$SUBLANG2$EN|g" $SETTINGS ###AUTO SUB = ENGLISH###
sed -i "s/$SUBTITLES$F/$SUBTITLES$T/g" $SETTINGS ###AUTO SUB ON###
sed -i "s|$TVLIBRARY$ALL|$TVLIBRARY$TVPATH|g" $SETTINGS ###FIXED PATH###
sed -i "s/$UPDATELIBRARY$F/$UPDATELIBRARY$T/g" $SETTINGS ###FIXED PATH###
sed -i "s/$WATCHEDLIBRARY$F/$WATCHEDLIBRARY$T/g" $SETTINGS ###MARK AS WATCHED ON###
sed -i "s/$WATCHEDTRAKT$F/$WATCHEDTRAKT$T/g" $SETTINGS ###MARK AS WATCHED ON###
#sed -i "s/$META$F/$META$T/g" $SETTINGS ###METADATA ON??? ###REMOVED###
#sed -i "s/$WATCHEDMETAHANDLER$F/$WATCHEDMETAHANDLER$T/g" $SETTINGS ###REMOVED###
#sed -i "s/$WATCHEDSYNC$F/$WATCHEDSYNC$T/g" $SETTINGS ###REMOVED###

CACHE=$HOME/.kodi/userdata/addon_data/plugin.video.genesis/cache.db
rm -f $CACHE