#!/bin/bash
#### Written by: TEAM HTPT - infohtpt@gmail.com
exit
SETTINGS=$HOME/.kodi/userdata/guisettings.xml

{ ###GET USER ID10###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID10"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID10='"'$FINDEXACT'"'
echo ID10: $ID10 '('$FINDEXACT')'


###GET USER ID40###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.ID40"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
ID40='"'$FINDEXACT'"'
echo ID40: $ID40 '('$FINDEXACT')'

###GET USER CustomGUI###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.CustomGUI"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
CustomGUI='"'$FINDEXACT'"'
echo CustomGUI: $CustomGUI '('$FINDEXACT')'

###GET USER SubHebOnly###
GUI='/storage/.kodi/userdata/guisettings.xml'
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.SubHebOnly"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
SUBHEBONLY='"'$FINDEXACT'"'
echo SUBHEBONLY: $SUBHEBONLY '('$FINDEXACT')'

}

###VAR GENERAL###
E='<'
T='true<'
F='false<'
ALL='[^ ]*<'
ALL2='[^ ]*|*<' #TEST
ALL3='[^ ]<' #TEST
NUM0='0<'
NUM1='1<'
NUM2='2<'
NUM3='3<'
NUM4='4<'
NUM5='5<'
NUM10='10<'
NUM60='60<'
NUM720='720<'
HTPT='HTPT<'
DEFAULT='DEFAULT<'
SKINDEFAULT='SKINDEFAULT<'
ORIGINAL='original<'
MSHTPT='MSHTPT<'
DEFAULT_TRUE='default="true">'

{ #
if [ $CustomGUI != '"true"' ]; then
	{ ###SMB
	WORKGROUP='<workgroup>'
	WORKGROUP2='<workgroup default="true">'
	###SED
	sed -i "s/$WORKGROUP$ALL/$WORKGROUP$MSHTPT/g" $SETTINGS
	sed -i "s/$WORKGROUP2$ALL/$WORKGROUP$MSHTPT/g" $SETTINGS
	}

	{ ###WEATHER
	ADDON='<addon>'
	ADDON2='<addon default="true">'
	WEATHERADDON='weather.yahoo<'
	###SED
	sed -i "s/$ADDON$ALL/$ADDON$WEATHERADDON/g" $SETTINGS
	sed -i "s/$ADDON2$ALL/$ADDON$WEATHERADDON/g" $SETTINGS
	}

	{ ###VAR services###
	AIRPLAY='<airplay>'
	AIRPLAYIOS8COMPAT='<airplayios8compat>'
	AIRPLAYPASSWORD='<airplaypassword>'
	AIRPLAYVOLUMECONTROL='<airplayvolumecontrol>'
	DEVICENAME='<devicename>'
	DEVICENAME2='<devicename default="true">'
	ENABLEJOYSTICK='<enablejoystick>'
	ENABLEMOUSE='<enablemouse>'
	ESALLINTERFACES='<esallinterfaces>'
	ESALLINTERFACES2='<esallinterfaces default="true">'
	ESENABLED='<esenabled>'
	HTTPPROXYPORT='<httpproxyport>'
	HTTPPROXYPORT2='8080<'
	UPNPSERVER='<upnpserver>'
	UPNPRENDERED='<upnprenderer>'
	SETTINGLEVEL='<settinglevel>'
	WEBSERVERPORT='<webserverport>'
	WEBSERVERPORT2='<webserverport default="true">'
	WEBSERVERNAME='<webserverusername>'
	WEBSERVERNAME2='<webserverusername default="true">'
	WEBSERVER='<webserver>'
	WEBSERVERPASSWORD='<webserverpassword>'
	ZEROCONF='<zeroconf>'
	###SED services###
	sed -i "s/$AIRPLAY$F/$AIRPLAY$T/g" $SETTINGS
	sed -i "s/$AIRPLAYIOS8COMPAT$F/$AIRPLAYIOS8COMPAT$T/g" $SETTINGS
	sed -i "s/$AIRPLAYPASSWORD$ALL/$AIRPLAYPASSWORD$E/g" $SETTINGS
	sed -i "s/$AIRPLAYVOLUMECONTROL$F/$AIRPLAYVOLUMECONTROL$T/g" $SETTINGS
	sed -i "s/$ENABLEJOYSTICK$F/$ENABLEJOYSTICK$T/g" $SETTINGS
	if [ $ID40 == '"false"' ]; then
		sed -i "s/$ENABLEMOUSE$T/$ENABLEMOUSE$F/g" $SETTINGS
		sed -i "s/$SETTINGLEVEL$ALL/$SETTINGLEVEL$NUM0/g" $SETTINGS #
	fi
	sed -i "s/$ESENABLED$F/$ESENABLED$T/g" $SETTINGS
	sed -i "s/$ESALLINTERFACES2$F/$ESALLINTERFACES$T/g" $SETTINGS

	sed -i "s/$WEBSERVERPASSWORD$ALL/$WEBSERVERPASSWORD$E/g" $SETTINGS
	sed -i "s/$HTTPPROXYPORT$ALL/$HTTPPROXYPORT$HTTPPROXYPORT2/g" $SETTINGS
	sed -i "s/$UPNPSERVER$T/$UPNPSERVER$F/g" $SETTINGS

	sed -i "s/$UPNPRENDERED$T/$UPNPRENDERED$F/g" $SETTINGS

	sed -i "s/$WEBSERVERPORT2$ALL/$WEBSERVERPORT$HTTPPROXYPORT2/g" $SETTINGS
	sed -i "s/$WEBSERVERNAME$ALL/$WEBSERVERNAME$HTPT/g" $SETTINGS
	sed -i "s/$WEBSERVERNAME2$ALL/$WEBSERVERNAME$HTPT/g" $SETTINGS
	sed -i "s/$DEVICENAME$ALL/$DEVICENAME$HTPT/g" $SETTINGS
	sed -i "s/$DEVICENAME2$ALL/$DEVICENAME$HTPT/g" $SETTINGS
	sed -i "s/$WEBSERVERPASSWORD$ALL/$WEBSERVERPASSWORD$E/g" $SETTINGS
	sed -i "s/$ZEROCONF$F/$ZEROCONF$T/g" $SETTINGS

	}

	{ ###locale
	AUDIOLANGUAGE='<audiolanguage>'
	CHARSET='<charset>'
	COUNTRY='<country>'
	KEYBOARDLAYOUTS='<keyboardlayouts>'
	KEYBOARDLAYOUTS2='<keyboardlayouts default="true">English QWERTY<'
	KEYBOARDLAYOUTS_ISRAEL='English ABC|Hebrew ABC<'
	KEYBOARDLAYOUTS_FIX1='English QWERTY|Hebrew QWERTY'
	KEYBOARDLAYOUTS_FIX2='Hebrew QWERTY'
	COUNTRY_ISRAEL1='ISRAEL (12h)'
	COUNTRY_ISRAEL2='ISRAEL (24h)'

	TIMEZONE='<timezone>'
	TIMEZONECOUNTRY2='<timezone default="true">'
	TIMEZONECOUNTRY='<timezonecountry>'
	TIMEZONECOUNTRY2='<timezonecountry default="true">'
	TIMEZONECOUNTRY_ISRAEL='Israel<'
	######
	sed -i "s/$AUDIOLANGUAGE$ALL/$AUDIOLANGUAGE$ORIGINAL/g" $SETTINGS
	sed -i "s/$CHARSET$ALL/$CHARSET$DEFAULT/g" $SETTINGS
	sed -i "s/$COUNTRY$COUNTRY_ISRAEL1/$COUNTRY$COUNTRY_ISRAEL2/g" $SETTINGS

	#sed -i "s/$KEYBOARDLAYOUTS2/$KEYBOARDLAYOUTS$KEYBOARDLAYOUTS_ISRAEL/g" $SETTINGS
	sed -i "s/$KEYBOARDLAYOUTS$KEYBOARDLAYOUTS_FIX1/$KEYBOARDLAYOUTS$KEYBOARDLAYOUTS_ISRAEL/g" $SETTINGS
	sed -i "s/$KEYBOARDLAYOUTS$KEYBOARDLAYOUTS_FIX2/$KEYBOARDLAYOUTS$KEYBOARDLAYOUTS_ISRAEL/g" $SETTINGS
	
	sed -i "s/$KEYBOARDLAYOUTS2/$KEYBOARDLAYOUTS$KEYBOARDLAYOUTS_ISRAEL/g" $SETTINGS
	
	sed -i "s/$TIMEZONECOUNTRY2$ALL/$TIMEZONECOUNTRY$TIMEZONECOUNTRY_ISRAEL/g" $SETTINGS ###UNTESTED
	}

	{ ###VAR filelists###
	ALLOWFILEDELETION='<allowfiledeletion>'
	ALLOWFILEDELETION2='<allowfiledeletion default="true">'
	IGNORETHEWHENSORTING='<ignorethewhensorting>'
	SHOWADDSOURCEBUTTONS='<showaddsourcebuttons>'
	SHOWEXTENSIONS='<showextensions>'
	SHOWPARENTDIRITTEMS='<showparentdiritems>'
	SHOWHIDDEN='<showhidden>'

	###SET filelists###
	sed -i "s/$ALLOWFILEDELETION2$F/$ALLOWFILEDELETION$T/g" $SETTINGS
	sed -i "s/$IGNORETHEWHENSORTING$F/$IGNORETHEWHENSORTING$T/g" $SETTINGS ###Allows for certain tokens to be ignored during sort operations. For example, with this option enabled, "The Simpsons" would simply be sorted as "Simpsons".###
	sed -i "s/$SHOWADDSOURCEBUTTONS$F/$SHOWADDSOURCEBUTTONS$T/g" $SETTINGS ###Enables showing the add source button from root sections of the user interface.
	sed -i "s/$SHOWEXTENSIONS$F/$SHOWEXTENSIONS$T/g" $SETTINGS ###Determines the display of the extensions on media files. For example, "You Enjoy Myself.mp3" would be simply be displayed as "You Enjoy Myself".
	sed -i "s/$SHOWPARENTDIRITTEMS$F/$SHOWPARENTDIRITTEMS$T/g" $SETTINGS ###Determines the display of the parent folder icon (..).
	sed -i "s/$SHOWHIDDEN$T/$SHOWHIDDEN$F/g" $SETTINGS ###Shows hidden files and directories.
	
	}
	
	{ ###VAR lookandfeel + audiooutput###
	SOUNDSKIN='<soundskin>'
	SOUNDSKIN2='<soundskin default="true">'
	SKINZOON='<skinzoom>' #ON HTPT DEFAULT
	STREAMSILENCE='<streamsilence>'
	STREAMSILENCE2='<streamsilence default="true">'
	GUISOUNDMODE='<guisoundmode>'
	GUISOUNDMODE2='<guisoundmode default="true">'
	
	###SET lookandfeel###
	if [ $ID10 == '"A"' ] || [ $ID10 == '"B"' ]; then
		###EMU!###
		sed -i "s/$SOUNDSKIN$ALL/$SOUNDSKIN$SKINDEFAULT/g" $SETTINGS ###Allows you to select or disable the sound scheme used in the User Interface.
		sed -i "s/$SOUNDSKIN2$ALL/$SOUNDSKIN$SKINDEFAULT/g" $SETTINGS ###Allows you to select or disable the sound scheme used in the User Interface.
		sed -i "s/$GUISOUNDMODE$ALL/$GUISOUNDMODE$NUM0/g" $SETTINGS #A/V sync method
		sed -i "s/$GUISOUNDMODE2$ALL/$GUISOUNDMODE$NUM0/g" $SETTINGS #A/V sync method
	fi
	
	sed -i "s/$STREAMSILENCE$ALL/$STREAMSILENCE$NUM0/g" $SETTINGS
	sed -i "s/$STREAMSILENCE2$ALL/$STREAMSILENCE$NUM0/g" $SETTINGS

	###SET audiooutput###


	}

	{ #musiclibrary
	REPEAT='<repeat>'
	SHUFFLE='<shuffle>'
	
	#sed -i "s/$REPEAT$ALL/$REPEAT$F/g" $SETTINGS
	#sed -i "s/$SHUFFLE$ALL/$SHUFFLE$F/g" $SETTINGS
	}

	{ #pictures
	SHOWVIDEOS='<showvideos>'
	SHOWVIDEOS2='<showvideos default="true">'
	sed -i "s/$SHOWVIDEOS2$ALL/$SHOWVIDEOS$F/g" $SETTINGS
	
	}
	
	{ #scrapers
	MOVIESDEFAULT='<moviesdefault>'
	MOVIESDEFAULT='<moviesdefault default="true">'
	MOVIESDEFAULT_='metadata.universal<'
	TVSHOWSDEFAULT='<tvshowsdefault>'
	TVSHOWSDEFAULT_='metadata.tvdb.com<'
	#sed -i "s/$MOVIESDEFAULT$ALL/$MOVIESDEFAULT$MOVIESDEFAULT_/g" $SETTINGS #BUG?
	#sed -i "s/$MOVIESDEFAULT2$ALL/$MOVIESDEFAULT$MOVIESDEFAULT_/g" $SETTINGS
	#sed -i "s/$TVSHOWSDEFAULT$ALL/$TVSHOWSDEFAULT$TVSHOWSDEFAULT_/g" $SETTINGS
	
	}
	
	{ ###VAR VIDEOLIBRARY###
	GROUPMOVIESETS='<groupmoviesets>'
	SHOWUNWATCHEDPLOTS='<showunwatchedplots>'
	UPDATEONSTARTUP='<updateonstartup>'
	FLATTENTVSHOWS='<flattentvshows>'
	BACKGROUNDUPDATE='<backgroundupdate>'

	###SED VIDEOLIBRARY###
	sed -i "s/$GROUPMOVIESETS$F/$GROUPMOVIESETS$T/g" $SETTINGS
	sed -i "s/$SHOWUNWATCHEDPLOTS$F/$SHOWUNWATCHEDPLOTS$T/g" $SETTINGS
	sed -i "s/$UPDATEONSTARTUP$T/$UPDATEONSTARTUP$F/g" $SETTINGS
	sed -i "s/$FLATTENTVSHOWS$ALL/$FLATTENTVSHOWS$NUM1/g" $SETTINGS
	sed -i "s/$BACKGROUNDUPDATE$T/$BACKGROUNDUPDATE$F/g" $SETTINGS
	}

	{ ###screensaver###
	TIME='<time>'
	TIME2='<time default="true">'
	MODE='<mode>'
	MODE2='<mode default="true">'
	MODE_='screensaver.picture.slideshow<'
	USEDIMONPAUSE='<usedimonpause>'
	USEDIMONPAUSE2='<usedimonpause default="true">'
	USEMUSICVISINSTEAD='<usemusicvisinstead>'
	USEMUSICVISINSTEAD2='<usemusicvisinstead default="true">'
	###
	sed -i "s/$MODE$ALL/$MODE$E/g" $SETTINGS
	sed -i "s/$MODE2$ALL/$MODE$E/g" $SETTINGS
	sed -i "s/$TIME$ALL/$TIME$NUM60/g" $SETTINGS
	sed -i "s/$TIME2$NUM3/$TIME$NUM60/g" $SETTINGS
	sed -i "s/$USEDIMONPAUSE2$T/$USEDIMONPAUSE$F/g" $SETTINGS
	sed -i "s/$USEMUSICVISINSTEAD2$T/$USEMUSICVISINSTEAD$F/g" $SETTINGS
	}

	{ ###VAR pvrmanager###
	SYNCCHANNELGROUPS='<syncchannelgroups>'
	PLAYMINIMIZED='<playminimized>'
	PREVENTUPDATESWHILEPLAYINGTV='<preventupdateswhileplayingtv>'
	PREVENTUPDATESWHILEPLAYINGTV2='<preventupdateswhileplayingtv default="true">'
	HIDENOINFOAVAILABLE='<hidenoinfoavailable>'
	IGNOREDBFORCLIENT='<ignoredbforclient>'
	SELECTACTION='<selectaction>'
	DAYSTODISPLAY='<daystodisplay>'
	DAYSTODISPLAY2='<daystodisplay default="true">'
	STARTLAST='<startlast>'
	###SED pvrmanager###
	sed -i "s/$SYNCCHANNELGROUPS$F/$SYNCCHANNELGROUPS$T/g" $SETTINGS
	sed -i "s/$PLAYMINIMIZED$F/$PLAYMINIMIZED$T/g" $SETTINGS
	sed -i "s/$PREVENTUPDATESWHILEPLAYINGTV2$F/$PREVENTUPDATESWHILEPLAYINGTV$T/g" $SETTINGS
	sed -i "s/$HIDENOINFOAVAILABLE$F/$HIDENOINFOAVAILABLE$T/g" $SETTINGS 
	sed -i "s/$IGNOREDBFORCLIENT$T/$IGNOREDBFORCLIENT$F/g" $SETTINGS ###DONT USE DATEBASE EPG###
	sed -i "s/$SELECTACTION$ALL/$SELECTACTION$NUM2/g" $SETTINGS ###DEFAULT ACTION ON TVGUIDE###
	sed -i "s/$DAYSTODISPLAY$ALL/$DAYSTODISPLAY$NUM2/g" $SETTINGS ###TOTAL DAYS IN TVGUIDE###
	sed -i "s/$DAYSTODISPLAY2$ALL/$DAYSTODISPLAY$NUM2/g" $SETTINGS ###TOTAL DAYS IN TVGUIDE###
	sed -i "s/$STARTLAST$ALL/$STARTLAST$NUM0/g" $SETTINGS ###LAUNCH LAST CHANNEL ON STARTUP###

	}
	
	{ ###VAR VIDEOSCREEN###
	VSYNC='<vsync>'
	VSYNC2='<vsync default="true">'
	SCREENMODE='<screenmode>'
	SCREENMODE2='00192001080060.00000pstd<'
	RESOLUTION='<resolution>'
	RESOLUTION2='18<'

	###SED
	sed -i "s/$VSYNC$ALL/$VSYNC$NUM2/g" $SETTINGS
	sed -i "s/$VSYNC2$ALL/$VSYNC$NUM2/g" $SETTINGS
	sed -i "s/$SCREENMODE$ALL/$SCREENMODE$SCREENMODE2/g" $SETTINGS
	sed -i "s/$RESOLUTION$ALL/$RESOLUTION$RESOLUTION2/g" $SETTINGS


	}


	{ ###VAR VIDEOPLAYER###
	ADJUSTREFRESHRATE='<adjustrefreshrate>'
	AUTOPLAYNEXTITEM='<autoplaynextitem>'
	PAUSEAFTERREFRESHCHANGE='<pauseafterrefreshchange>'
	USEDISPLAYASCLOCK='<usedisplayasclock>'
	USEDISPLAYASCLOCK2='<usedisplayasclock default="true">'
	SYNCTYPE='<synctype>'
	SYNCTYPE2='<synctype default="true">'
	HQSCALERS='<hqscalers>'
		
	sed -i "s/$ADJUSTREFRESHRATE$ALL/$ADJUSTREFRESHRATE$NUM0/g" $SETTINGS #Adjust display refresh rate to match video
	sed -i "s/$AUTOPLAYNEXTITEM$T/$AUTOPLAYNEXTITEM$F/g" $SETTINGS #Play next video automatically
	sed -i "s/$PAUSEAFTERREFRESHCHANGE$ALL/$PAUSEAFTERREFRESHCHANGE$NUM0/g" $SETTINGS #Pause during refresh rate change
	sed -i "s/$USEDISPLAYASCLOCK2$F/$USEDISPLAYASCLOCK$T/g" $SETTINGS #Sync playback to display
	sed -i "s/$SYNCTYPE$ALL/$SYNCTYPE$NUM1/g" $SETTINGS #A/V sync method
	sed -i "s/$SYNCTYPE2$NUM2/$SYNCTYPE$NUM1/g" $SETTINGS #SA/V sync method
	sed -i "s/$HQSCALERS$ALL/$HQSCALERS$NUM0/g" $SETTINGS #Enable HQ scalers for scaling above #?

	}

	{ ###VAR SUBTITLES1###
	TV='<tv>'
	MOVIE='<movie>'
	PAUSEONSEARCH='<pauseonsearch>'
	PAUSEONSEARCH2='<pauseonsearch default="true">'
	LANGUAGES='<languages>'
	LANGUAGES2='<languages default="true">'
	LANGUAGES_EN='English<'
	LANGUAGES_EN_HE='English,Hebrew<'
	LANGUAGES_HE='Hebrew<'
	DOWNLOADFIRST='downloadfirst default="true">'
	###VAR SUBTITLES2###
	SUBCENTER='service.subtitles.subscenter<'
	OPENSUBTITLES='service.subtitles.opensubtitles<'
	SUBTITLES='service.subtitles.subtitle<'
	TOREC='service.subtitles.torec<'
	
	

	###SED SUBTITLES###
	sed -i "s/$MOVIE$ALL/$MOVIE$SUBCENTER/g" $SETTINGS #MOVIE MAIN
	sed -i "s/$TV$ALL/$TV$SUBCENTER/g" $SETTINGS #TV MAIN
	
	#sed -i "s/$TV$ALL/$TV$OPENSUBTITLES/g" $SETTINGS #TV SECONDARY
	
	#sed -i "s/$MOVIE$ALL/$MOVIE$OPENSUBTITLES/g" $SETTINGS #MOVIE SECONDARY
	
	#sed -i "s/$PAUSEONSEARCH2$T/$PAUSEONSEARCH$F/g" $SETTINGS #PAUSE ON SEARCH (OFF)
	sed -i "s/$PAUSEONSEARCH$F/$PAUSEONSEARCH2$T/g" $SETTINGS #PAUSE ON SEARCH (ON)

	}

	

	sed -i "s/$LANGUAGES$ALL/$LANGUAGES$LANGUAGES_EN_HE/g" $SETTINGS #LANGUAGE HEBREW ONLY!
	sed -i "s/$LANGUAGES2$ALL/$LANGUAGES$LANGUAGES_EN_HE/g" $SETTINGS #LANGUAGE HEBREW ONLY!
	#sed -i "s/$LANGUAGES$LANGUAGES_EN/$LANGUAGES$LANGUAGES_EN_HE/g" $SETTINGS #LANGUAGE HEBREW ONLY!
	#sed -i "s/$LANGUAGES2$LANGUAGES_EN/$LANGUAGES$LANGUAGES_EN_HE/g" $SETTINGS #LANGUAGE HEBREW ONLY!



	{ # MODEL A
	if [ $ID10 == '"A"' ]; then
		###INTEL NUC 2820###
		RENDERMETHOD='<rendermethod>'
		
		DECODINGMETHOD='<decodingmethod>'
		USEVAAPI='<usevaapi>'
		USEVAAPIMEPG2='<usevaapimpeg2>'
		USEVAAPIMEPG22='<usevaapimpeg2 default="true">'
		USEVAAPIMEPG4='<usevaapimpeg4>'
		USEVAAPIVC1='<usevaapivc1>'
		USEVAAPIVC12='<usevaapivc1 default="true">'
		PREFERVAAPIRENDER='<prefervaapirender>'
		PREFERVAAPIRENDER2='<prefervaapirender default="true">'
		
		###VAR VIDEO ACCELERATION 2###
		USEVAAPIVC1_='<usevaapivc1>'
		
		###SED VIDEO ACCELERATION###
		sed -i "s/$RENDERMETHOD$ALL/$RENDERMETHOD$NUM0/g" $SETTINGS #RENDER METHOD
		sed -i "s/$DECODINGMETHOD$NUM0/$DECODINGMETHOD$NUM1/g" $SETTINGS #DECODING METHOD
		sed -i "s/$USEVAAPI$F/$USEVAAPI$T/g" $SETTINGS #ALLOW VAAPI
		sed -i "s/$USEVAAPIMEPG2$T/$USEVAAPIMEPG2$F/g" $SETTINGS #MEPG2
		sed -i "s/$USEVAAPIMEPG22$T/$USEVAAPIMEPG2$F/g" $SETTINGS #MEPG2
		sed -i "s/$USEVAAPIMEPG4$F/$USEVAAPIMEPG4$T/g" $SETTINGS #MEPG4
		sed -i "s/$USEVAAPIVC1$T/$USEVAAPIVC1_$F/g" $SETTINGS #VC1
		sed -i "s/$USEVAAPIVC12$T/$USEVAAPIVC1_$F/g" $SETTINGS #VC1
		sed -i "s/$PREFERVAAPIRENDER$T/$PREFERVAAPIRENDER$F/g" $SETTINGS #PREFER VAAPI
		sed -i "s/$PREFERVAAPIRENDER2$T/$PREFERVAAPIRENDER$F/g" $SETTINGS #PREFER VAAPI

	fi

	}

	{ # MODEL C
	if [ $ID10 == '"C"' ]; then
		PIXELRATIO='<pixelratio>'
		PIXELRATION2='1.250000>'
		TEXTURES32='<textures32>'
		LIMITGUI='<limitgui>'
		LIMITGUI2='<limitgui default="true">'
		###SED
		#sed -i "s/$PIXELRATIO$ALL/$PIXELRATIO$PIXELRATION2/g" $SETTINGS #UNTESTED - UNVARIFIED
		sed -i "s/$LIMITGUI$ALL/$LIMITGUI$NUM0/g" $SETTINGS
		#sed -i "s/$LIMITGUI2$NUM0/$LIMITGUI$NUM720/g" $SETTINGS
		#sed -i "s/$TEXTURES32$T/$TEXTURES32$F/g" $SETTINGS
		
	fi

	}

fi

}

{ #REPEAT
ADDONNOTIFICATIONS='<addonnotifications>'
ADDONNOTIFICATIONS2='<addonnotifications default="true">'
ADDONUPDATES='<addonupdates>'
ADDONFOREIGNFILTER='<addonforeignfilter>'

sed -i "s/$ADDONNOTIFICATIONS2$ALL/$ADDONNOTIFICATIONS$F/g" $SETTINGS #DISABLE ADDON NOTIFICATION
sed -i "s/$ADDONUPDATES$ALL/$ADDONUPDATES$NUM0/g" $SETTINGS #ENABLE AUTOMATIC ADDON UPDATE
sed -i "s/$ADDONFOREIGNFILTER$ALL/$ADDONFOREIGNFILTER$F/g" $SETTINGS #
}

sleep 1