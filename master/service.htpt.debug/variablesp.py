import xbmcaddon, sys, os

from shared_variables import *
'''---------------------------'''
#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)

'''------------------------------
---service.htpt.debug-------------
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

printpoint = ""
printfirst = addonName + ": !@# "
'''---------------------------'''
General_AllowDebug = getsetting('General_AllowDebug')
General_MailService = getsetting('General_MailService')
General_MailService_ = 4
General_ServiceON = getsetting('General_ServiceON')
General_ScriptON = getsetting('General_ScriptON')

General_Start = getsetting('General_Start')
General_Pass = getsetting('General_Pass')
'''---------------------------'''
Info_Bluetooth = getsetting('Info_Bluetooth')
Info_Intel = getsetting('Info_Intel')
Info_Model = getsetting('Info_Model')
Info_SystemName = getsetting('Info_SystemName')
Info_TotalMemory = getsetting('Info_TotalMemory')
Info_TotalSpace = getsetting('Info_TotalSpace')
'''---------------------------'''
User_Name = getsetting('User_Name')
User_Email = getsetting('User_Email')
User_ID = getsetting('User_ID')
User_Tel = getsetting('User_Tel')
User_Issue = getsetting('User_Issue')
'''---------------------------'''
ModeOn_1 = getsetting('ModeOn_1')
ModeOn_2 = getsetting('ModeOn_2')
ModeOn_3 = getsetting('ModeOn_3')
ModeOn_4 = getsetting('ModeOn_4')
ModeOn_5 = getsetting('ModeOn_5')
ModeOn_6 = getsetting('ModeOn_6')
ModeOn_7 = getsetting('ModeOn_7')
ModeOn_8 = getsetting('ModeOn_8')
ModeOn_9 = getsetting('ModeOn_9')
ModeOn_10 = getsetting('ModeOn_10')
ModeOn_11 = getsetting('ModeOn_11')
ModeOn_12 = getsetting('ModeOn_12')
ModeOn_13 = getsetting('ModeOn_13')
ModeOn_14 = getsetting('ModeOn_14')
ModeOn_15 = getsetting('ModeOn_15')
ModeOn_16 = getsetting('ModeOn_16')
ModeOn_17 = getsetting('ModeOn_17')
ModeOn_18 = getsetting('ModeOn_18')
ModeOn_19 = getsetting('ModeOn_19')
ModeOn_20 = getsetting('ModeOn_20')
ModeOn_21 = getsetting('ModeOn_21')
'''---------------------------'''
ModeTime_4 = getsetting('ModeTime_4')
ModeTime_7 = getsetting('ModeTime_7')
ModeTime_8 = getsetting('ModeTime_8')
ModeTime_9 = getsetting('ModeTime_9')
ModeTime_10 = getsetting('ModeTime_10')
'''---------------------------'''
Sum_1 = getsetting('Sum_1')
Sum_2 = getsetting('Sum_2')
Sum_3 = getsetting('Sum_3')
Sum_4 = getsetting('Sum_4')
Sum_5 = getsetting('Sum_5')
Sum_6 = getsetting('Sum_6')
Sum_7 = getsetting('Sum_7')
Sum_8 = getsetting('Sum_8')
Sum_9 = getsetting('Sum_9')
Sum_10 = getsetting('Sum_10')
Sum_11 = getsetting('Sum_11')
Sum_12 = getsetting('Sum_12')
Sum_13 = getsetting('Sum_13')
Sum_14 = getsetting('Sum_14')
Sum_15 = getsetting('Sum_15')
Sum_16 = getsetting('Sum_16')
Sum_17 = getsetting('Sum_17')
Sum_18 = getsetting('Sum_18')
Sum_19 = getsetting('Sum_19')
Sum_20 = getsetting('Sum_20')
Sum_21 = getsetting('Sum_21')
'''---------------------------'''

'''------------------------------
---service.htpt.debug-3-----------
------------------------------'''
if systemplatformwindows:
	file1 = os.path.join(home_path, 'kodi.log')
	file2 = os.path.join(home_path, 'kodi.old.log')
else:
	file1 = os.path.join(temp_path, 'kodi.log')
	file2 = os.path.join(temp_path, 'kodi.old.log')

file3 = os.path.join(userdata_path, 'kodi.log')
file5 = "/storage/.kodi/temp/htptlog.zip"


files = "Z:\logpath"
#filenames = [os.path.join(files, f) for f in os.listdir(files)]
'''---------------------------'''

'''------------------------------
---service.htpt.debug-2-----------
------------------------------'''
sendostr = "htptout@gmail.com"
sendostr2 = "htptout11@gmail.com"
recipentstr = "htptin1@gmail.com"

if xbmc.getSkinDir() != "skin.htpt": leftmenustartupmessages2 = ""
else:
	leftmenustartupmessages2 = xbmc.getInfoLabel('$VAR[LeftMenuStartupMessages2]')
	messagechangelog = xbmc.getInfoLabel('MessagesChangeLog')
	forcemac = ['F8:1A:67:19:EC:34', 'C4:4E:AC:00:99:58', '0C:8B:FD:9D:2F:CE']
	if "HTPT SYSTEM v" in leftmenustartupmessages2: leftmenustartupmessages2 = "ChangeLog"
	elif leftmenustartupmessages2 == messagescustom:
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[CR]"," ")
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[B]"," ")
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[/B]"," ")
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[COLOR=Yellow]"," ")
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[/COLOR]"," ")
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[COLOR=Green]"," ")
		leftmenustartupmessages2 = leftmenustartupmessages2.replace("[COLOR=Blue]"," ")
		'''---------------------------'''
	
if playerhasvideo:
	videoplayertitle = videoplayertitle.replace("[CR]"," ")
	videoplayertitle = videoplayertitle.replace("[B]"," ")
	videoplayertitle = videoplayertitle.replace("[/B]"," ")
	videoplayertitle = videoplayertitle.replace("[COLOR=Yellow]"," ")
	videoplayertitle = videoplayertitle.replace("[/COLOR]"," ")
	videoplayertitle = videoplayertitle.replace("[COLOR=Green]"," ")
	videoplayertitle = videoplayertitle.replace("[COLOR=Blue]"," ")
	videoplayertitle = videoplayertitle.replace("[COLOR yellow]"," ")
	videoplayertitle = videoplayertitle.replace("[COLOR floralwhite]"," ")
	videoplayertitle = videoplayertitle.replace("[COLOR none]"," ")
	'''---------------------------'''
	playertitle = playertitle.replace("[CR]"," ")
	playertitle = playertitle.replace("[B]"," ")
	playertitle = playertitle.replace("[/B]"," ")
	playertitle = playertitle.replace("[COLOR=Yellow]"," ")
	playertitle = playertitle.replace("[/COLOR]"," ")
	playertitle = playertitle.replace("[COLOR=Green]"," ")
	playertitle = playertitle.replace("[COLOR=Blue]"," ")
	playertitle = playertitle.replace("[COLOR yellow]"," ")
	playertitle = playertitle.replace("[COLOR floralwhite]"," ")
	playertitle = playertitle.replace("[COLOR none]"," ")
	'''---------------------------'''
	



'''------------------------------
---service.htpt.debug-4-----------
------------------------------'''
content0 = '''

------------------------------
USERNAME:          %s (%s)
------------------------------

''' % (User_ID, User_Name)

content0u = '''

------------------------------
USERNAME:          %s
USER ID:       %s

EMAIL:             %s
TEL:               %s

USER WRITE:        %s
SYSTEM UP TIME:    %s
------------------------------

''' % (User_Name, User_ID, User_Email, User_Tel, User_Issue, systemuptime)

content1 = '''

------------------------------
INFO
------------------------------
INSTALLATION DATE: %s
HTPT MODEL:        %s (%s)
INTEL:             %s
TOTAL SPACE:       %s
SYSTEM NAME:       %s
TOTAL MEMORY:      %s
BLUETOOTH:         %s
------------------------------

''' % (scripthtptinstall_Skin_DateInstalled, id10str, scripthtptdebug_Info_Model, scripthtptdebug_Info_Intel, scripthtptdebug_Info_TotalSpace, scripthtptdebug_Info_SystemName, scripthtptdebug_Info_TotalMemory, scripthtptdebug_Info_Bluetooth)

content1r = '''
------------------------------
RED-ALERT
------------------------------
RED ALERT ISSUED:  %s
AVAILABLE DATE:    %s
------------------------------

''' % (servicehtptfix_Red_Done, servicehtptfix_Red_LastDate)

content1f = '''
------------------------------
FIX-INFO
------------------------------
ERROR NO:          %s
FIXED ISSUED:      %s
AVAILABLE DATE:    %s
------------------------------
''' % ("?", servicehtptfix_Fix_Done, servicehtptfix_Fix_LastDate)

content2 = '''
------------------------------
?
------------------------------
?
------------------------------
'''

'''------------------------------'''
htptretroarchversion = xbmc.getInfoLabel('System.AddonVersion(emulator.retroarch)')
htptrepositoryversion = xbmc.getInfoLabel('System.AddonVersion(repository.htpt)')
htptdebugversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.debug)')
'''------------------------------'''
content3 = '''
------------------------------
VERSION
------------------------------
HTPT VER:          %s
BUILD VER:         %s
HTPT REPO:         %s
HTPT DEBUG VER:    %s
HTPT FIX VER:      %s
HTPT INSTALL VER:  %s
HTPT HELP VER:     %s
HTPT EMU VER:      %s
HTPT RETRO VER:    %s
HTPT KIDS VER:     %s
HTPT GOPRO VER:    %s
HTPT MUSIC VER:    %s
HTPT REFRESH VER:  %s
HTPT REMOTE VER:   %s
HTPT SERVICE VER:  %s
HTPT SMART.B VER:  %s
------------------------------
''' % (htptversion, buildversion, htptrepositoryversion, htptdebugversion, htptfixversion, htptinstallversion, htpthelpversion, htptemuversion, htptretroarchversion, htptkidsversion, htptgoproversion, htptmusicversion, htptrefreshversion, htptremoteversion, htptserviceversion, htptsmartbuttonsversion)

content4 = '''
------------------------------
NETWORK-INFO
------------------------------
LOCAL IP:          %s
GATEWAY:           %s
DHCPADDRESS:       %s
MAC(1=lan/2=wlan): %s
connected:         %s (%s)
connected2/3:      %s / %s
pingnow/pingrate:  %s / (%s)
------------------------------
''' % (networkipaddress, networkgatewayaddress, dhcpaddress, macstr2, connected, systeminternetstate, connected2, connected3, pingnow, pingrate)

content5 = '''
------------------------------
MISC
------------------------------
CURRENT CONTROL:   %s
CURRENT WINDOW:    %s
SCREEN RESOLUTION: %s
FREE SPACE:        %s
------------------------------
''' % (systemcurrentcontrol, systemcurrentwindow, screenresolution, freespace2)

content6 = '''
------------------------------
MessagesCustom
------------------------------
MessagesCustom:    %s
Ads_Date:          %s
Ads_Timezone:      %s
------------------------------
''' % (leftmenustartupmessages2, servicehtptfix_Ads_Date, servicehtptfix_Ads_Timezone)

content7 = '''
------------------------------
Current-Video-1
------------------------------
Title:             %s
Title2:            %s
Year:              %s
Duration:          %s / %s
Resolution:        %s
Video Codec:       %s
Audio Channels:    %s
Audio Codec:       %s
Filename:          %s
------------------------------
''' % (videoplayertitle, playertitle, videoplayeryear, playerduration, playertimeremaining, videoplayervideoresolution, videoplayervideocodec, videoplayeraudiochannels, videoplayeraudiocodec, playerfilename)

content8 = '''
------------------------------
Current-Video-2
------------------------------
Title:             %s
User_Name:      %s
Year:              %s
Source:            %s
Current M_T:       %s
Current Watched    %s
Watched Time:      %s
Duration:          %s / %s
Subtitle:          %s
Subtitle1:         %s
Resolution:        %s
Video Codec:       %s
Audio Channels:    %s
Audio Codec:       %s
Filename:          %s
Connection Score:  %s
Count Wait:        %s
StartWindow:       %s
------------------------------
''' % (videoplayertitle, scripthtptrefresh_Current_Name, scripthtptrefresh_Current_Year, scripthtptrefresh_Current_Source, scripthtptrefresh_Current_M_T, scripthtptrefresh_Current_Watched, scripthtptrefresh_Current_WatchTime, scripthtptrefresh_Current_Duration, playertimeremaining, scripthtptrefresh_Current_Subtitle, scripthtptrefresh_Current_Subtitle1, videoplayervideoresolution, videoplayervideocodec, videoplayeraudiochannels, videoplayeraudiocodec, playerfilename, scripthtptrefresh_General_ConnectionScore, scripthtptrefresh_General_CountWait, scripthtptrefresh_General_StartWindow)

content9 = '''
------------------------------
Last-Movie
------------------------------
Title:             %s
Year:              %s
Source:            %s
Date:              %s
Watched:           %s
WatchTime:         %s
Subtitle:          %s
Subtitle1:         %s
------------------------------
''' % (scripthtptrefresh_LastMovie_Name, scripthtptrefresh_LastMovie_Year, scripthtptrefresh_LastMovie_Source, scripthtptrefresh_LastMovie_Date, scripthtptrefresh_LastMovie_Watched, scripthtptrefresh_LastMovie_WatchTime, scripthtptrefresh_LastMovie_Subtitle, scripthtptrefresh_LastMovie_Subtitle1)

content10 = '''
------------------------------
Last-TV
------------------------------
Title:             %s
Year:              %s
Source:            %s
Date:              %s
Watched:           %s
WatchTime:         %s
Subtitle:          %s
Subtitle1:         %s
------------------------------
''' % (scripthtptrefresh_LastTV_Name, scripthtptrefresh_LastTV_Year, scripthtptrefresh_LastTV_Source, scripthtptrefresh_LastTV_Date, scripthtptrefresh_LastTV_Watched, scripthtptrefresh_LastTV_WatchTime, scripthtptrefresh_LastTV_Subtitle, scripthtptrefresh_LastTV_Subtitle1)

content11 = '''
------------------------------
Last-IsraeliTV
------------------------------
Title:             %s
AutoPlay2:         %s
Date:              %s
Watched:           %s
WatchTime:         %s
------------------------------
''' % (scripthtptrefresh_LastIsraelTV_Name, scripthtptrefresh_AutoPlay2, scripthtptrefresh_LastIsraelTV_Date, scripthtptrefresh_LastIsraelTV_Watched, scripthtptrefresh_LastIsraelTV_WatchTime)

content19 = '''
------------------------------
WARNINGS
------------------------------
CPU TEMP:          %s
GPU TEMP:          %s
HDD TEMP:          %s
CPU USAGE:         %s
FAN SPEED:         %s
MEMORY:            %s / %s
FREE SPACE:        %s
------------------------------
''' % (systemcputemperature, systemgputemperature, systemhddtemperature, systemcpuusage, systemfanspeed, systemmemorytotal, systemfreememory, freespace2)

if 1 + 1 == 2:
	if sdarottv_password != "": sdarottv_password = "***"
	if subtitle_set2 != "": subtitle_set2 = "***"
	if realdedrid_password != "": realdedrid_password = "***"
	'''------------------------------'''

content20 = '''
------------------------------
ADDONS-SETTINGS
------------------------------
LIVE TV URL:       %s
ISRAELI TV URL:    %s
ISRAELI TV USER:   %s - %s (%s -%s)
SUBTITLES.CO.IL:   %s - %s
GENESIS HD HOSTS:  %s - %s - %s
genesis_set7/8     %s - %s (%s -%s)
genesis_set9/10    %s - %s
------------------------------
''' % (israelive_set1, sdarottv_domain, sdarottv_user, sdarottv_password, Account2_Active, Account2_Period, subtitle_set1, subtitle_set2, genesis_set4, genesis_set5, genesis_set6, realdedrid_user, realdedrid_password, Account1_Active, Account1_Period, genesis_set9, genesis_set10)

content21 = '''
------------------------------
SETTINGS
------------------------------
CURRENT CONTROL:   %s
SCREEN RESOLUTION: %s
FREE SPACE:        %s
------------------------------
''' % (systemcurrentcontrol, screenresolution, freespace2)