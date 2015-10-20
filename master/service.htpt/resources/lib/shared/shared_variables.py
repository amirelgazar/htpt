import xbmc, xbmcgui, xbmcaddon, sys, os

try: addonID2 = xbmcaddon.Addon().getAddonInfo("id")
except: addonID2 = "N/A"
#except Exception, TypeError: print "addonID2-TypeError: " + str(TypeError)
try: printfirst = xbmcaddon.Addon().getAddonInfo("name") + ": !@# "
except: printfirst = "N/A"
'''---------------------------'''

'''------------------------------
---DEFAULT-----------------------
------------------------------'''
space = " "
space2 = ": "
space3 = "_"
space4 = " / "
space5 = " - "
newline = "\n"
TypeError = ""
dialog = xbmcgui.Dialog()
systemplatformwindows = xbmc.getCondVisibility('System.Platform.Windows')
systemplatformlinux = xbmc.getCondVisibility('System.Platform.Linux')
systemplatformlinuxraspberrypi = xbmc.getCondVisibility('System.Platform.Linux.RaspberryPi')
systemplatformandroid = xbmc.getCondVisibility('System.Platform.Android')
systemplatformosx = xbmc.getCondVisibility('System.Platform.OSX')
systemplatformios = xbmc.getCondVisibility('System.Platform.IOS')

systemidle0 = xbmc.getCondVisibility('System.IdleTime(0)')
systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
systemidle7 = xbmc.getCondVisibility('System.IdleTime(7)')
systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
systemidle40 = xbmc.getCondVisibility('System.IdleTime(40)')
systemidle120 = xbmc.getCondVisibility('System.IdleTime(120)')
systemidle300 = xbmc.getCondVisibility('System.IdleTime(300)')
systemidle5400 = xbmc.getCondVisibility('System.IdleTime(5400)') #1.5H
systemidle6900 = xbmc.getCondVisibility('System.IdleTime(6900)') #2H-5min
systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
systemcurrentwindow = xbmc.getInfoLabel('System.CurrentWindow')
gh1 = 'https://github.com/'
gh2 = 'htpthtpt/htpt/raw/master/'
gh3 = 'xbmc-adult/xbmc-adult/raw/ghmaster/'
gh4 = 'cubicle-vdo/xbmc-israel/raw/master/repo/'
'''---------------------------'''




'''------------------------------
---xbmcaddon.Addon---------------
------------------------------'''
addon = 'service.htpt.fix'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_servicehtptfix         = xbmcaddon.Addon(addon).getSetting
	setsetting_servicehtptfix         = xbmcaddon.Addon(addon).setSetting
	'''---------------------------'''
	servicehtptfix_General_DownloadON = getsetting_servicehtptfix('General_DownloadON')
	servicehtptfix_Ads_Date = getsetting_servicehtptfix('Ads_Date')
	servicehtptfix_Ads_Timezone = getsetting_servicehtptfix('Ads_Timezone')
	'''---------------------------'''
	servicehtptfix_Fix_Done = getsetting_servicehtptfix('Fix_Done')
	servicehtptfix_Fix_LastDate = getsetting_servicehtptfix('Fix_LastDate')
	servicehtptfix_Red_Done = getsetting_servicehtptfix('Red_Done')
	servicehtptfix_Red_LastDate = getsetting_servicehtptfix('Red_LastDate')
	'''---------------------------'''
	
else:
	servicehtptfix_General_DownloadON = ""
	servicehtptfix_Ads_Date = ""
	servicehtptfix_Ads_Timezone = ""
	'''---------------------------'''
	servicehtptfix_Fix_Done = ""
	servicehtptfix_Fix_LastDate = ""
	servicehtptfix_Red_Done = ""
	servicehtptfix_Red_LastDate = ""
	'''---------------------------'''

addon = 'script.htpt.smartbuttons'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_scripthtptsmartbuttons         = xbmcaddon.Addon(addon).getSetting
	setsetting_scripthtptsmartbuttons         = xbmcaddon.Addon(addon).setSetting
	'''---------------------------'''
	scripthtptsmartbuttons_General_ScriptON = getsetting_scripthtptsmartbuttons('General_ScriptON')
	scripthtptsmartbuttonsLibraryData_LocalMoviesFiles = getsetting_scripthtptsmartbuttons('LibraryData_LocalMoviesFiles')
	scripthtptsmartbuttonsLibraryData_LocalTvshowsFiles = getsetting_scripthtptsmartbuttons('LibraryData_LocalTvshowsFiles')
	'''---------------------------'''
else:
	scripthtptsmartbuttonsLibraryData_LocalMoviesFiles = "0"
	scripthtptsmartbuttonsLibraryData_LocalTvshowsFiles = "0"
	scripthtptsmartbuttons_General_ScriptON = ""
	'''---------------------------'''
	
addon = 'script.htpt.install'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_scripthtptinstall         = xbmcaddon.Addon(addon).getSetting
	setsetting_scripthtptinstall         = xbmcaddon.Addon(addon).setSetting
	'''---------------------------'''
	scripthtptinstall_General_ScriptON = getsetting_scripthtptinstall('General_ScriptON')
	scripthtptinstall_User_ID = getsetting_scripthtptinstall('User_ID')
	scripthtptinstall_Skin_Default = getsetting_scripthtptinstall('Skin_Default')
	scripthtptinstall_Skin_Installed = getsetting_scripthtptinstall('Skin_Installed')
	scripthtptinstall_Skin_FirstBoot = getsetting_scripthtptinstall('Skin_FirstBoot')
	scripthtptinstall_Skin_DateInstalled = getsetting_scripthtptinstall('Skin_DateInstalled')
	scripthtptinstall_Skin_DateInstalled_ = getsetting_scripthtptinstall('Skin_DateInstalled_')
	'''---------------------------'''
else:
	scripthtptinstall_General_ScriptON = ""
	scripthtptinstall_User_ID = ""
	scripthtptinstall_Skin_Default = ""
	scripthtptinstall_Skin_Installed = ""
	scripthtptinstall_Skin_FirstBoot = ""
	scripthtptinstall_Skin_DateInstalled = ""
	scripthtptinstall_Skin_DateInstalled_ = ""
	'''---------------------------'''
	
addon = 'script.htpt.refresh'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and addonID2 != "script.htpt.refresh" and xbmc.getCondVisibility('IntegerGreaterThan(System.Uptime,1)'): #service.htpt.debug - only! (else bugged!)
	getsetting_scripthtptrefresh       = xbmcaddon.Addon(addon).getSetting
	setsetting_scripthtptrefresh         = xbmcaddon.Addon(addon).setSetting
	scripthtptrefresh_General_ConnectionScore = getsetting_scripthtptrefresh('General_ConnectionScore')
	scripthtptrefresh_General_CountWait = getsetting_scripthtptrefresh('General_CountWait')
	scripthtptrefresh_General_CustomVAR = getsetting_scripthtptrefresh('General_CustomVAR')
	scripthtptrefresh_General_StartWindow = getsetting_scripthtptrefresh('General_StartWindow')
	scripthtptrefresh_General_ScriptON = getsetting_scripthtptrefresh('General_ScriptON')
	'''---------------------------'''
	scripthtptrefresh_Current_M_T = getsetting_scripthtptrefresh('Current_M_T')
	scripthtptrefresh_Current_Watched = getsetting_scripthtptrefresh('Current_Watched')
	scripthtptrefresh_Current_WatchTime = getsetting_scripthtptrefresh('Current_WatchTime')
	scripthtptrefresh_Current_Name = getsetting_scripthtptrefresh('Current_Name')
	scripthtptrefresh_Current_Year = getsetting_scripthtptrefresh('Current_Year')
	scripthtptrefresh_Current_Source = getsetting_scripthtptrefresh('Current_Source')
	scripthtptrefresh_Current_Duration = getsetting_scripthtptrefresh('Current_Duration')
	scripthtptrefresh_Current_Subtitle = getsetting_scripthtptrefresh('Current_Subtitle')
	scripthtptrefresh_Current_Subtitle1 = getsetting_scripthtptrefresh('Current_Subtitle1')
	'''---------------------------'''
	scripthtptrefresh_LastMovie_Date = getsetting_scripthtptrefresh('LastMovie_Date')
	scripthtptrefresh_LastMovie_Name = getsetting_scripthtptrefresh('LastMovie_Name')
	scripthtptrefresh_LastMovie_Source = getsetting_scripthtptrefresh('LastMovie_Source')
	scripthtptrefresh_LastMovie_Subtitle = getsetting_scripthtptrefresh('LastMovie_Subtitle')
	scripthtptrefresh_LastMovie_Subtitle1 = getsetting_scripthtptrefresh('LastMovie_Subtitle1')
	scripthtptrefresh_LastMovie_Watched = getsetting_scripthtptrefresh('LastMovie_Watched')
	scripthtptrefresh_LastMovie_WatchTime = getsetting_scripthtptrefresh('LastMovie_WatchTime')
	scripthtptrefresh_LastMovie_Year = getsetting_scripthtptrefresh('LastMovie_Year')
	'''---------------------------'''
	scripthtptrefresh_LastTV_Date = getsetting_scripthtptrefresh('LastTV_Date')
	scripthtptrefresh_LastTV_Name = getsetting_scripthtptrefresh('LastTV_Name')
	scripthtptrefresh_LastTV_Source = getsetting_scripthtptrefresh('LastTV_Source')
	scripthtptrefresh_LastTV_Subtitle = getsetting_scripthtptrefresh('LastTV_Subtitle')
	scripthtptrefresh_LastTV_Subtitle1 = getsetting_scripthtptrefresh('LastTV_Subtitle1')
	scripthtptrefresh_LastTV_Watched = getsetting_scripthtptrefresh('LastTV_Watched')
	scripthtptrefresh_LastTV_WatchTime = getsetting_scripthtptrefresh('LastTV_WatchTime')
	scripthtptrefresh_LastTV_Year = getsetting_scripthtptrefresh('LastTV_Year')
	'''---------------------------'''
	scripthtptrefresh_LastIsraelTV_Date = getsetting_scripthtptrefresh('LastIsraelTV_Date')
	scripthtptrefresh_LastIsraelTV_Name = getsetting_scripthtptrefresh('LastIsraelTV_Name')
	scripthtptrefresh_AutoPlay2 = getsetting_scripthtptrefresh('AutoPlay2')
	scripthtptrefresh_LastIsraelTV_Watched = getsetting_scripthtptrefresh('LastIsraelTV_Watched')
	scripthtptrefresh_LastIsraelTV_WatchTime = getsetting_scripthtptrefresh('LastIsraelTV_WatchTime')
	'''---------------------------'''
	
else:
	scripthtptrefresh_General_ConnectionScore = ""
	scripthtptrefresh_General_CountWait = ""
	scripthtptrefresh_General_CustomVAR = ""
	scripthtptrefresh_General_StartWindow = ""
	scripthtptrefresh_General_ScriptON = ""
	'''---------------------------'''
	scripthtptrefresh_Current_M_T = ""
	scripthtptrefresh_Current_Watched = ""
	scripthtptrefresh_Current_WatchTime = ""
	scripthtptrefresh_Current_Name = ""
	scripthtptrefresh_Current_Year = ""
	scripthtptrefresh_Current_Source = ""
	scripthtptrefresh_Current_Duration = ""
	scripthtptrefresh_Current_Subtitle = ""
	scripthtptrefresh_Current_Subtitle1 = ""
	'''---------------------------'''
	scripthtptrefresh_LastMovie_Date = ""
	scripthtptrefresh_LastMovie_Name = ""
	scripthtptrefresh_LastMovie_Source = ""
	scripthtptrefresh_LastMovie_Subtitle = ""
	scripthtptrefresh_LastMovie_Subtitle1 = ""
	scripthtptrefresh_LastMovie_Watched = ""
	scripthtptrefresh_LastMovie_WatchTime = ""
	scripthtptrefresh_LastMovie_Year = ""
	'''---------------------------'''
	scripthtptrefresh_LastTV_Date = ""
	scripthtptrefresh_LastTV_Name = ""
	scripthtptrefresh_LastTV_Source = ""
	scripthtptrefresh_LastTV_Subtitle = ""
	scripthtptrefresh_LastTV_Subtitle1 = ""
	scripthtptrefresh_LastTV_Watched = ""
	scripthtptrefresh_LastTV_WatchTime = ""
	scripthtptrefresh_LastTV_Year = ""
	'''---------------------------'''
	scripthtptrefresh_LastIsraelTV_Name = ""
	scripthtptrefresh_LastIsraelTV_Date = ""
	scripthtptrefresh_AutoPlay2 = ""
	scripthtptrefresh_LastIsraelTV_Watched = ""
	scripthtptrefresh_LastIsraelTV_WatchTime = ""
	'''---------------------------'''
	

addon = 'service.htpt'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_servicehtpt = xbmcaddon.Addon(addon).getSetting
	setsetting_servicehtpt = xbmcaddon.Addon(addon).setSetting
	addonString_servicehtpt = xbmcaddon.Addon(addon).getLocalizedString
	servicehtpt_Skin_UpdateLog = getsetting_servicehtpt('Skin_UpdateLog')
	servicehtpt_Skin_Name = getsetting_servicehtpt('Skin_Name') #TEMP
	'''---------------------------'''
else:
	servicehtpt_Skin_UpdateLog = ""
	servicehtpt_Skin_Name = ""
	addonString_servicehtpt = ""
	'''---------------------------'''

addon = 'plugin.video.israelive'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_pluginvideoisraelive          = xbmcaddon.Addon(addon).getSetting
	setsetting_pluginvideoisraelive          = xbmcaddon.Addon(addon).setSetting
	israelive_set1 = getsetting_pluginvideoisraelive('remoteSettingsUrl')
	'''---------------------------'''
else:
	israelive_set1 = ""
	'''---------------------------'''
	
addon = 'plugin.video.sdarot.tv'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_pluginvideosdarottv          = xbmcaddon.Addon(addon).getSetting
	setsetting_pluginvideosdarottv          = xbmcaddon.Addon(addon).setSetting
	#addonString_sdarot           = xbmcaddon.Addon(addon).getLocalizedString
	
	sdarottv_user = getsetting_pluginvideosdarottv('username')
	sdarottv_password = getsetting_pluginvideosdarottv('user_password')
	sdarottv_domain = getsetting_pluginvideosdarottv('domain')
	'''---------------------------'''
else:
	sdarottv_user = ""
	sdarottv_password = ""
	sdarottv_domain = ""
	'''---------------------------'''

addon = 'service.subtitles.subtitle'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_servicesubtitlessubtitle          = xbmcaddon.Addon(addon).getSetting
	subtitle_set1 = getsetting_servicesubtitlessubtitle('SUBemail')
	subtitle_set2 = getsetting_servicesubtitlessubtitle('SUBpassword')
	'''---------------------------'''
else:
	subtitle_set1 = ""
	subtitle_set2 = ""
	'''---------------------------'''

addon = 'service.htpt.debug'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_scripthtptdebug         = xbmcaddon.Addon(addon).getSetting
	setsetting_scripthtptdebug         = xbmcaddon.Addon(addon).setSetting
	'''---------------------------'''
	scripthtptdebug_General_AllowDebug = getsetting_scripthtptdebug('General_AllowDebug')
	scripthtptdebug_General_ScriptON = getsetting_scripthtptdebug('General_ScriptON')
	'''---------------------------'''
	scripthtptdebug_Info_Bluetooth = getsetting_scripthtptdebug('Info_Bluetooth')
	scripthtptdebug_Info_Intel = getsetting_scripthtptdebug('Info_Intel')
	scripthtptdebug_Info_Model = getsetting_scripthtptdebug('Info_Model')
	scripthtptdebug_Info_SystemName = getsetting_scripthtptdebug('Info_SystemName')
	scripthtptdebug_Info_TotalMemory = getsetting_scripthtptdebug('Info_TotalMemory')
	scripthtptdebug_Info_TotalSpace = getsetting_scripthtptdebug('Info_TotalSpace')
	'''---------------------------'''
	scripthtptdebug_User_ID = getsetting_scripthtptdebug('User_ID')
	scripthtptdebug_User_Name = getsetting_scripthtptdebug('User_Name')
	scripthtptdebug_User_Email = getsetting_scripthtptdebug('User_Email')
	scripthtptdebug_User_Tel = getsetting_scripthtptdebug('User_Tel')
	scripthtptdebug_User_Issue = getsetting_scripthtptdebug('User_Issue')
	'''---------------------------'''
else:
	scripthtptdebug_General_AllowDebug = ""
	scripthtptdebug_General_ScriptON = ""
	'''---------------------------'''
	scripthtptdebug_Info_Bluetooth = ""
	scripthtptdebug_Info_Intel = ""
	scripthtptdebug_Info_Model = ""
	scripthtptdebug_Info_SystemName = ""
	scripthtptdebug_Info_TotalMemory = ""
	scripthtptdebug_Info_TotalSpace = ""
	'''---------------------------'''
	scripthtptdebug_User_ID = ""
	scripthtptdebug_User_Name = ""
	scripthtptdebug_User_Email = ""
	scripthtptdebug_User_Tel = ""
	scripthtptdebug_User_Issue = ""
	'''---------------------------'''
	
addon = 'plugin.video.genesis'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	'''------------------------------
	---plugin.video.genesis----------
	------------------------------'''
	addonString_genesis           = xbmcaddon.Addon(addon).getLocalizedString #BACKUP
	addonString_pluginvideogenesis            = xbmcaddon.Addon(addon).getLocalizedString
	getsetting_pluginvideogenesis             = xbmcaddon.Addon(addon).getSetting
	addonVersion_pluginvideogenesis          = xbmcaddon.Addon(addon).getAddonInfo("version")
	'''---------------------------'''
	imdb_user = getsetting_pluginvideogenesis('imdb_user')
	realdedrid_user = getsetting_pluginvideogenesis('realdedrid_user')
	realdedrid_password = getsetting_pluginvideogenesis('realdedrid_password')
	trakt_user = getsetting_pluginvideogenesis('trakt_user')
	trakt_password = getsetting_pluginvideogenesis('trakt_password')
	movreel_user = getsetting_pluginvideogenesis('movreel_user')
	movreel_password = getsetting_pluginvideogenesis('movreel_password')
	noobroom_mail = getsetting_pluginvideogenesis('noobroom_mail')
	noobroom_password = getsetting_pluginvideogenesis('noobroom_password')
	premiumize_user = getsetting_pluginvideogenesis('premiumize_user')
	premiumize_password = getsetting_pluginvideogenesis('premiumize_password')
	furk_user = getsetting_pluginvideogenesis('furk_user')
	furk_password = getsetting_pluginvideogenesis('furk_password')
	'''---------------------------'''
	genesis_set1 = getsetting_pluginvideogenesis('autoplay_library') #TEMP?
	genesis_set2 = getsetting_pluginvideogenesis('autoplay_hd') #TEMP?
	genesis_set3 = getsetting_pluginvideogenesis('autoplay') #TEMP?
	genesis_set4 = getsetting_pluginvideogenesis('hosthd50001')
	genesis_set5 = getsetting_pluginvideogenesis('hosthd50002')
	genesis_set6 = getsetting_pluginvideogenesis('hosthd50003')
	genesis_set9 = getsetting_pluginvideogenesis('movie_library')
	genesis_set10 = getsetting_pluginvideogenesis('tv_library')
	'''---------------------------'''
	genesis30341str = addonString_pluginvideogenesis(30341) #ARE YOU SURE?
	'''---------------------------'''
	
else:
	addonString_genesis = ""
	addonVersion_pluginvideogenesis = ""
	imdb_user = ""
	realdedrid_user = ""
	realdedrid_password = ""
	trakt_user = ""
	trakt_password = ""
	movreel_user = ""
	movreel_password = ""
	noobroom_mail = ""
	noobroom_password = ""
	premiumize_user = ""
	premiumize_password = ""
	furk_user = ""
	furk_password = ""
	'''---------------------------'''
	genesis_set1 = ""
	genesis_set2 = ""
	genesis_set3 = ""
	genesis_set4 = ""
	genesis_set5 = ""
	genesis_set6 = ""
	genesis_set7 = "" #TEMP
	genesis_set8 = "" #TEMP
	genesis_set9 = ""
	genesis_set10 = ""
	'''---------------------------'''
	genesis30341str = ""
	'''---------------------------'''
	
'''------------------------------
---Window.-----------------------
------------------------------'''

custom1115W = xbmc.getCondVisibility('Window.IsVisible(Custom1115.xml)')
custom1124W = xbmc.getCondVisibility('Window.IsVisible(Custom1124.xml)')
custom1125W = xbmc.getCondVisibility('Window.IsVisible(Custom1125.xml)')
custom1132W = xbmc.getCondVisibility('Window.IsVisible(Custom1132.xml)')
#custom1133W = xbmc.getCondVisibility('Window.IsVisible(Custom1133.xml)')
custom1134W = xbmc.getCondVisibility('Window.IsVisible(Custom1134.xml)')
custom1135W = xbmc.getCondVisibility('Window.IsVisible(Custom1135.xml)')
custom1136W = xbmc.getCondVisibility('Window.IsVisible(Custom1136.xml)')
custom1170W = xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)')
custom1171W = xbmc.getCondVisibility('Window.IsVisible(Custom1171.xml)')
custom1172W = xbmc.getCondVisibility('Window.IsVisible(Custom1172.xml)')
custom1176W = xbmc.getCondVisibility('Window.IsVisible(Custom1176.xml)')
custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
scriptpythonslideshowW = xbmc.getCondVisibility('Window.IsVisible(script-python-slideshow.xml)')

customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
dialogaddoninfoW = xbmc.getCondVisibility('Window.IsVisible(DialogAddonInfo.xml)')
addonbrowserW = xbmc.getCondVisibility('Window.IsVisible(AddonBrowser.xml)')
dialogaddonsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogAddonSettings.xml)')
dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
dialogcontextmenuW = xbmc.getCondVisibility('Window.IsVisible(DialogContextMenu.xml)')
dialogfavouritesW = xbmc.getCondVisibility('Window.IsVisible(DialogFavourites.xml)')
dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)') ###fix to W
dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
dialogvideoinfoW = xbmc.getCondVisibility('Window.IsVisible(DialogVideoInfo.xml)')
dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
filemanagerW = xbmc.getCondVisibility('Window.IsVisible(FileManager.xml)')
loginscreenW = xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)')
loginscreen_aW = xbmc.getCondVisibility('Window.IsActive(LoginScreen.xml)')
mainwindow = xbmc.getCondVisibility('Window.IsVisible(mainWindow.xml)') #OpenELEC ###fix to W
mainwindowW = xbmc.getCondVisibility('Window.IsVisible(mainWindow.xml)') #OpenELEC
mypicsW = xbmc.getCondVisibility('Window.IsVisible(MyPics.xml)')
myprogramsW = xbmc.getCondVisibility('Window.IsVisible(MyPrograms.xml)')
mymusicnavW = xbmc.getCondVisibility('Window.IsVisible(MyMusicNav.xml)')
myvideonavW = xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)')
myweatherW = xbmc.getCondVisibility('Window.IsVisible(MyWeather.xml)')
videoosdW = xbmc.getCondVisibility('Window.IsVisible(VideoOSD.xml)')
videoosdsettingsW = xbmc.getCondVisibility('Window.IsVisible(VideoOSDSettings.xml)')
dialogpvrchannelsosd = xbmc.getCondVisibility('Window.IsVisible(DialogPVRChannelsOSD.xml)')
mypvrchannels = xbmc.getCondVisibility('Window.IsVisible(MyPVRChannels.xml)')
mypvrguide = xbmc.getCondVisibility('Window.IsVisible(MyPVRGuide.xml)')
homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
home_pW = xbmc.getCondVisibility('Window.Previous(0)')
home_aW = xbmc.getCondVisibility('Window.IsActive(0)')

settingsW = xbmc.getCondVisibility('Window.IsVisible(Settings.xml)')
settingscategoryW = xbmc.getCondVisibility('Window.IsVisible(SettingsCategory.xml)')
skinsettingsW = xbmc.getCondVisibility('Window.IsVisible(SkinSettings.xml)')
startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
startup_aW = xbmc.getCondVisibility('Window.IsActive(Startup.xml)')
startup_pW = xbmc.getCondVisibility('Window.Previous(Startup.xml)')
videofullscreenW = xbmc.getCondVisibility('Window.IsVisible(VideoFullScreen.xml)')
dialogvideonfoEW = xbmc.getCondVisibility('Window.IsVisible(script-ExtendedInfo Script-DialogVideoInfo.xml)')
'''---------------------------'''

'''------------------------------
---VideoPlayer-------------------
------------------------------'''
videoplayercontentEPISODE = xbmc.getCondVisibility('VideoPlayer.Content(episodes)')
videoplayercontentMOVIE = xbmc.getCondVisibility('VideoPlayer.Content(movies)')
videoplayercontentSEASON = xbmc.getCondVisibility('VideoPlayer.Content(seasons)')
videoplayercontentTV = xbmc.getCondVisibility('VideoPlayer.Content(tvshows)')
videoplayercountry = xbmc.getInfoLabel('VideoPlayer.Country')
videoplayerhassubtitles = xbmc.getCondVisibility('VideoPlayer.HasSubtitles')
videoplayerisfullscreen = xbmc.getCondVisibility('VideoPlayer.IsFullscreen')
videoplayerseason = xbmc.getInfoLabel('VideoPlayer.Season')
videoplayerepisode = xbmc.getInfoLabel('VideoPlayer.Episode')
videoplayertagline = xbmc.getInfoLabel('VideoPlayer.Tagline')
videoplayertitle = xbmc.getInfoLabel('VideoPlayer.Title')
videoplayertvshowtitle = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
videoplayeryear = xbmc.getInfoLabel('VideoPlayer.Year')
videoplayervideoresolution = xbmc.getInfoLabel('VideoPlayer.VideoResolution')
videoplayervideocodec = xbmc.getInfoLabel('VideoPlayer.VideoCodec')
videoplayeraudiochannels = xbmc.getInfoLabel('VideoPlayer.AudioChannels')
videoplayeraudiocodec = xbmc.getInfoLabel('VideoPlayer.AudioCodec')
videoplayerhassubtitles = xbmc.getCondVisibility('VideoPlayer.HasSubtitles')
videoplayersubtitlesenabled = xbmc.getInfoLabel('VideoPlayer.SubtitlesEnabled')


'''---------------------------'''

'''------------------------------
---System.X-Version--------------
------------------------------'''
if xbmc.getCondVisibility('System.HasAddon(service.htpt)'): htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)') + "+"
elif xbmc.getCondVisibility('!System.HasAddon(service.htpt)'): htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)') + "-"
buildversion = xbmc.getInfoLabel('System.BuildVersion')
systemprofilename = xbmc.getInfoLabel('System.ProfileName')
systemlanguage = xbmc.getInfoLabel('System.Language')
htptdebugversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.debug)')
htptserviceversion = xbmc.getInfoLabel('system.AddonVersion(service.htpt)')
htpthelpversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.help)')
htpthomebuttonsversion = xbmc.getInfoLabel('System.AddonVersion(emulator.retroarch)')
htptinstallversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.install)')
htptremoteversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.remote)')
htptrefreshversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.refresh)')
htptsmartbuttonsversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.smartbuttons)')
htptfixversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.fix)')
htptskinversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)')
htptemuversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.emu)')
htptkidsversion = xbmc.getInfoLabel('System.AddonVersion(plugin.video.htpt.kids)')
htptgoproversion = xbmc.getInfoLabel('System.AddonVersion(plugin.video.htpt.gopro)')
htptmusicversion = xbmc.getInfoLabel('System.AddonVersion(plugin.video.htpt.music)')
'''---------------------------'''



'''------------------------------
---System.GetBool----------------
------------------------------'''
sgbservicesairplay = xbmc.getCondVisibility('System.GetBool(services.airplay)')
sgbserviceszeroconf = xbmc.getCondVisibility('System.GetBool(services.zeroconf)')
sgbpvrmanagerenabled = xbmc.getCondVisibility('System.GetBool(pvrmanager.enabled)')
sgbsubtitlespauseonsearch = xbmc.getCondVisibility('System.GetBool(subtitles.pauseonsearch)')
'''---------------------------'''

'''------------------------------
---System.HasAddon---------------
------------------------------'''
systemhasaddon_urlresolver = xbmc.getCondVisibility('System.HasAddon(script.module.urlresolver)')
systemhasaddon_genesis = xbmc.getCondVisibility('System.HasAddon(plugin.video.genesis)')
systemhasaddon_sdarottv = xbmc.getCondVisibility('System.HasAddon(plugin.video.sdarot.tv)')
systemhasaddon_aob = xbmc.getCondVisibility('System.HasAddon(plugin.video.aob)')
systemhasaddon_fantasticc = xbmc.getCondVisibility('System.HasAddon(plugin.video.fantasticc)')
systemhasaddon_videodevil = xbmc.getCondVisibility('System.HasAddon(plugin.video.videodevil)')
systemhasaddon_videopulsar = xbmc.getCondVisibility('System.HasAddon(plugin.video.pulsar)')
systemhasaddon_metadatauniversal = xbmc.getCondVisibility('System.HasAddon(metadata.universal)')
systemhasaddon_metadatathemoviedb = xbmc.getCondVisibility('System.HasAddon(metadata.themoviedb.org)')

systemhasaddon_servicesubtitlessubtitle = xbmc.getCondVisibility('System.HasAddon(service.subtitles.subtitle)')
systemhasaddon_pluginvideoisraelive = xbmc.getCondVisibility('System.HasAddon(plugin.video.israelive)')
systemhasaddon_pluginvideoyoutube = xbmc.getCondVisibility('System.HasAddon(plugin.video.youtube)')
systemhasaddon_pluginvideop2pstreams = xbmc.getCondVisibility('System.HasAddon(plugin.video.p2p-streams)')
systemhasaddon_serviceautosubs = xbmc.getCondVisibility('System.HasAddon(service.autosubs)')
'''---------------------------'''

systemhasaddon_htptdebug = xbmc.getCondVisibility('System.HasAddon(service.htpt.debug)')
systemhasaddon_scripthtptdebug = xbmc.getCondVisibility('System.HasAddon(service.htpt.debug)')
systemhasaddon_htptemu = xbmc.getCondVisibility('System.HasAddon(script.htpt.emu)')
systemhasaddon_htptinstall = xbmc.getCondVisibility('System.HasAddon(script.htpt.install)')
systemhasaddon_scripthtptrefresh = xbmc.getCondVisibility('System.HasAddon(script.htpt.refresh)')
systemhasaddon_scripthtptsmartbuttons = xbmc.getCondVisibility('System.HasAddon(script.htpt.smartbuttons)')
systemhasaddon_htptfix = xbmc.getCondVisibility('System.HasAddon(service.htpt.fix)')
systemhasaddon_servicehtpt = xbmc.getCondVisibility('System.HasAddon(service.htpt)')
systemhasaddon_htptkids = xbmc.getCondVisibility('System.HasAddon(plugin.video.htpt.kids)')
systemhasaddon_htptmusic = xbmc.getCondVisibility('System.HasAddon(plugin.video.htpt.music)')
systemhasaddon_htptgopro = xbmc.getCondVisibility('System.HasAddon(plugin.video.htpt.gopro)')
'''---------------------------'''

'''------------------------------
---System.All--------------------
------------------------------'''
systemtotalspace = xbmc.getInfoLabel('System.TotalSpace')
systeminternetstate = xbmc.getInfoLabel('System.InternetState')
systemuptime = xbmc.getInfoLabel('System.Uptime')
systemuptime1 = xbmc.getCondVisibility('!IntegerGreaterThan(System.Uptime,1)')
systemuptime5 = xbmc.getCondVisibility('!IntegerGreaterThan(System.Uptime,5)')
systemtotaluptime = xbmc.getInfoLabel('System.TotalUptime')
systemcputemperature = xbmc.getInfoLabel('System.CPUTemperature')
systemgputemperature = xbmc.getInfoLabel('System.GPUTemperature')
systemhddtemperature = xbmc.getInfoLabel('System.HddTemperature')
systemcpuusage = xbmc.getInfoLabel('System.CpuUsage')
systemfanspeed = xbmc.getInfoLabel('System.FanSpeed')
systemfreememory = xbmc.getInfoLabel('System.FreeMemory')
systemmemorytotal = xbmc.getInfoLabel('System.Memory(total)')
systemcurrentwindow = xbmc.getInfoLabel('System.CurrentWindow')
screenresolution = xbmc.getInfoLabel('System.ScreenResolution')
systemuptime2 = xbmc.getInfoLabel('System.Uptime') + " / " + xbmc.getInfoLabel('System.TotalUptime') 
freespace2 = xbmc.getInfoLabel('System.TotalSpace') + " / " + xbmc.getInfoLabel('System.FreeSpacePercent')
systemscreensaveractive = xbmc.getCondVisibility('System.ScreenSaverActive')
'''---------------------------'''

'''------------------------------
---Skin.HasSetting---------------
------------------------------'''
admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
adult = xbmc.getInfoLabel('Skin.HasSetting(Adult)')
adult2 = xbmc.getInfoLabel('Skin.HasSetting(Adult2)')
autoplay_hd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlay_HD)')
autoplaysd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlaySD)')
autoplaypause = xbmc.getInfoLabel('Skin.HasSetting(AutoPlay_Pause)')
autoview = xbmc.getInfoLabel('!Skin.HasSetting(AutoView)')
autoviewoff = xbmc.getInfoLabel('Skin.HasSetting(AutoViewoff)')
connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
dialogselectopen = xbmc.getInfoLabel('Skin.HasSetting(DialogSelectOpen)')
tvshowsep = xbmc.getInfoLabel('Skin.HasSetting(tvshowsep)')
musicsep = xbmc.getInfoLabel('Skin.HasSetting(musicsep)')
musicseptip = xbmc.getInfoLabel('Skin.HasSetting(musicseptip)')
kidsep = xbmc.getInfoLabel('Skin.HasSetting(kidsep)')
kidseptip = xbmc.getInfoLabel('Skin.HasSetting(kidseptip)')

myhtpt2 = xbmc.getInfoLabel('!Skin.HasSetting(myHTPT2)')
myhtpt3 = xbmc.getInfoLabel('Skin.HasSetting(myHTPT3)')
allowdebug = xbmc.getInfoLabel('Skin.HasSetting(AllowDebug)') #TEMP
realdebrid = xbmc.getInfoLabel('Skin.HasSetting(RealDebrid)') #TEMP
sdarottv = xbmc.getInfoLabel('Skin.HasSetting(SdarotTV)') #TEMP
validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')
validation2 = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION2)')
validation5 = xbmc.getInfoLabel('Skin.String(VALIDATION5)')
autoshutdown = xbmc.getInfoLabel('Skin.HasSetting(AutoShutdown)')
customgui = xbmc.getInfoLabel('Skin.HasSetting(CustomGUI)')
performance = xbmc.getInfoLabel('Skin.HasSetting(Performance)')
showdialog = xbmc.getInfoLabel('Skin.HasSetting(ShowDialog)')
totalmouse = xbmc.getInfoLabel('Skin.HasSetting(TotalMouse)')
customas = xbmc.getInfoLabel('Skin.HasSetting(CustomAS)')
customasources = xbmc.getInfoLabel('Skin.HasSetting(CustomSources)')
customkeymaps = xbmc.getInfoLabel('Skin.HasSetting(CustomKeymaps)')

if xbmc.getSkinDir() == 'skin.htpt':
	'''------------------------------
	---SKIN-DESIGN=------------------
	------------------------------'''
	
	skincurrenttheme = xbmc.getInfoLabel('Skin.CurrentTheme')
	
	selectionmarker = xbmc.getInfoLabel('Skin.HasSetting(SelectionMarker)')
	selectionmarker2 = xbmc.getInfoLabel('Skin.HasSetting(SelectionMarker2)')
	shadowbutton = xbmc.getInfoLabel('Skin.HasSetting(ShadowButton)')
	overlaybutton = xbmc.getInfoLabel('Skin.HasSetting(OverlayButton)')
	
	background = xbmc.getInfoLabel('Skin.HasSetting(background)')
	backgroundoverlay = xbmc.getInfoLabel('Skin.String(BackgroundOverlay)')
	
	iconoverlaybutton = xbmc.getInfoLabel('Skin.String(IconOverlayButton)')
	menubuttonsoverlay = xbmc.getInfoLabel('Skin.String(MenuButtonsOverlay)')
	mainbackgroundoverlay = xbmc.getInfoLabel('Skin.String(MainBackgroundOverlay)')
	topmainbackgroundoverlay = xbmc.getInfoLabel('Skin.String(TopMainBackgroundOverlay)')
	leftmenuoverlay = xbmc.getInfoLabel('Skin.String(LeftMenuOverlay)')
	bottommenuoverlay = xbmc.getInfoLabel('Skin.String(BottomMenuOverlay)')
	centermenuoverlay = xbmc.getInfoLabel('Skin.String(CenterMenuOverlay)')
	topvideoinformationoverlay = xbmc.getInfoLabel('Skin.String(TopVideoInformationOverlay)')
	topinformationoverlay = xbmc.getInfoLabel('Skin.String(TopInformationOverlay)')
	
	mainbackgroundtexture = xbmc.getInfoLabel('Skin.String(MainBackgroundTexture)')
	topbackgroundtexture = xbmc.getInfoLabel('Skin.String(TopBackgroundTexture)')
	
	menucolor = xbmc.getInfoLabel('Skin.String(MenuColor)')
	menucolorname = xbmc.getInfoLabel('Skin.String(MenuColor.name)')
	mainbackgroundcolor = xbmc.getInfoLabel('Skin.String(MainBackgroundColor)')
	mainbackgroundcolorname = xbmc.getInfoLabel('Skin.String(MainBackgroundColor.name)')
	topbackgroundcolor = xbmc.getInfoLabel('Skin.String(TopBackgroundColor)')
	topbackgroundcolorname = xbmc.getInfoLabel('Skin.String(TopBackgroundColor.name)')
	topinformationcolor = xbmc.getInfoLabel('Skin.String(TopInformationColor)')
	topinformationcolorname = xbmc.getInfoLabel('Skin.String(TopInformationColor.name)')
	topvideoinformationcolor = xbmc.getInfoLabel('Skin.String(TopVideoInformationColor)')
	topvideoinformationcolorname = xbmc.getInfoLabel('Skin.String(TopVideoInformationColor.name)')
	iconunfocuscolor = xbmc.getInfoLabel('Skin.String(IconUnFocusColor)')
	iconunfocuscolorname = xbmc.getInfoLabel('Skin.String(IconUnFocusColor.name)')
	iconfocuscolor = xbmc.getInfoLabel('Skin.String(IconFocusColor)')
	iconfocuscolorname = xbmc.getInfoLabel('Skin.String(IconFocusColor.name)')
	
	color340 = xbmc.getInfoLabel('Skin.String(color340)')
	color341 = xbmc.getInfoLabel('Skin.String(color341)')
	color342 = xbmc.getInfoLabel('Skin.String(color342)')
	color343 = xbmc.getInfoLabel('Skin.String(color343)')
	color344 = xbmc.getInfoLabel('Skin.String(color344)')
	color320 = xbmc.getInfoLabel('Skin.String(color320)')
	color321 = xbmc.getInfoLabel('Skin.String(color321)')
	color345 = xbmc.getInfoLabel('Skin.String(color345)')
	color507 = xbmc.getInfoLabel('Skin.String(color507)')
	color323 = xbmc.getInfoLabel('Skin.String(color323)')
	color351 = xbmc.getInfoLabel('Skin.String(color351)')
	color327 = xbmc.getInfoLabel('Skin.String(color327)')
	color325 = xbmc.getInfoLabel('Skin.String(color325)')
	color508 = xbmc.getInfoLabel('Skin.String(color508)')
	color322 = xbmc.getInfoLabel('Skin.String(color322)')
	color324 = xbmc.getInfoLabel('Skin.String(color324)')
	color331 = xbmc.getInfoLabel('Skin.String(color331)')
	color330 = xbmc.getInfoLabel('Skin.String(color330)')
	color352 = xbmc.getInfoLabel('Skin.String(color352)')
	color355 = xbmc.getInfoLabel('Skin.String(color355)')
	color357 = xbmc.getInfoLabel('Skin.String(color357)')
	color401 = xbmc.getInfoLabel('Skin.String(color401)')
	color402 = xbmc.getInfoLabel('Skin.String(color402)')
	color403 = xbmc.getInfoLabel('Skin.String(color403)')
	color404 = xbmc.getInfoLabel('Skin.String(color404)')
	color405 = xbmc.getInfoLabel('Skin.String(color405)')
	color601 = xbmc.getInfoLabel('Skin.String(color601)')
	color602 = xbmc.getInfoLabel('Skin.String(color602)')
	color603 = xbmc.getInfoLabel('Skin.String(color603)')
	color606 = xbmc.getInfoLabel('Skin.String(color606)')
	color605 = xbmc.getInfoLabel('Skin.String(color605)')
	color346 = xbmc.getInfoLabel('Skin.String(color346)')
	color348 = xbmc.getInfoLabel('Skin.String(color348)')
	color349 = xbmc.getInfoLabel('Skin.String(color349)')
	
	icon340 = xbmc.getInfoLabel('Skin.String(icon340)')
	icon341 = xbmc.getInfoLabel('Skin.String(icon341)')
	icon342 = xbmc.getInfoLabel('Skin.String(icon342)')
	icon343 = xbmc.getInfoLabel('Skin.String(icon343)')
	icon344 = xbmc.getInfoLabel('Skin.String(icon344)')
	icon320 = xbmc.getInfoLabel('Skin.String(icon320)')
	icon321 = xbmc.getInfoLabel('Skin.String(icon321)')
	icon345 = xbmc.getInfoLabel('Skin.String(icon345)')
	icon507 = xbmc.getInfoLabel('Skin.String(icon507)')
	icon323 = xbmc.getInfoLabel('Skin.String(icon323)')
	icon351 = xbmc.getInfoLabel('Skin.String(icon351)')
	icon327 = xbmc.getInfoLabel('Skin.String(icon327)')
	icon325 = xbmc.getInfoLabel('Skin.String(icon325)')
	icon508 = xbmc.getInfoLabel('Skin.String(icon508)')
	icon322 = xbmc.getInfoLabel('Skin.String(icon322)')
	icon324 = xbmc.getInfoLabel('Skin.String(icon324)')
	icon331 = xbmc.getInfoLabel('Skin.String(icon331)')
	icon330 = xbmc.getInfoLabel('Skin.String(icon330)')
	icon352 = xbmc.getInfoLabel('Skin.String(icon352)')
	icon355 = xbmc.getInfoLabel('Skin.String(icon355)')
	icon357 = xbmc.getInfoLabel('Skin.String(icon357)')
	icon401 = xbmc.getInfoLabel('Skin.String(icon401)')
	icon402 = xbmc.getInfoLabel('Skin.String(icon402)')
	icon403 = xbmc.getInfoLabel('Skin.String(icon403)')
	icon404 = xbmc.getInfoLabel('Skin.String(icon404)')
	icon405 = xbmc.getInfoLabel('Skin.String(icon405)')
	icon601 = xbmc.getInfoLabel('Skin.String(icon601)')
	icon602 = xbmc.getInfoLabel('Skin.String(icon602)')
	icon603 = xbmc.getInfoLabel('Skin.String(icon603)')
	icon606 = xbmc.getInfoLabel('Skin.String(icon606)')
	icon605 = xbmc.getInfoLabel('Skin.String(icon605)')
	icon346 = xbmc.getInfoLabel('Skin.String(icon346)')
	icon348 = xbmc.getInfoLabel('Skin.String(icon348)')
	icon349 = xbmc.getInfoLabel('Skin.String(icon349)')
	
	background340 = xbmc.getInfoLabel('Skin.String(background340)')
	background341 = xbmc.getInfoLabel('Skin.String(background341)')
	background342 = xbmc.getInfoLabel('Skin.String(background342)')
	background343 = xbmc.getInfoLabel('Skin.String(background343)')
	background344 = xbmc.getInfoLabel('Skin.String(background344)')
	background320 = xbmc.getInfoLabel('Skin.String(background320)')
	background321 = xbmc.getInfoLabel('Skin.String(background321)')
	background345 = xbmc.getInfoLabel('Skin.String(background345)')
	background507 = xbmc.getInfoLabel('Skin.String(background507)')
	background323 = xbmc.getInfoLabel('Skin.String(background323)')
	background351 = xbmc.getInfoLabel('Skin.String(background351)')
	background327 = xbmc.getInfoLabel('Skin.String(background327)')
	background325 = xbmc.getInfoLabel('Skin.String(background325)')
	background508 = xbmc.getInfoLabel('Skin.String(background508)')
	background322 = xbmc.getInfoLabel('Skin.String(background322)')
	background324 = xbmc.getInfoLabel('Skin.String(background324)')
	background331 = xbmc.getInfoLabel('Skin.String(background331)')
	background330 = xbmc.getInfoLabel('Skin.String(background330)')
	background352 = xbmc.getInfoLabel('Skin.String(background352)')
	background355 = xbmc.getInfoLabel('Skin.String(background355)')
	background357 = xbmc.getInfoLabel('Skin.String(background357)')
	background401 = xbmc.getInfoLabel('Skin.String(background401)')
	background402 = xbmc.getInfoLabel('Skin.String(background402)')
	background403 = xbmc.getInfoLabel('Skin.String(background403)')
	background404 = xbmc.getInfoLabel('Skin.String(background404)')
	background405 = xbmc.getInfoLabel('Skin.String(background405)')
	background601 = xbmc.getInfoLabel('Skin.String(background601)')
	background602 = xbmc.getInfoLabel('Skin.String(background602)')
	background603 = xbmc.getInfoLabel('Skin.String(background603)')
	background606 = xbmc.getInfoLabel('Skin.String(background606)')
	background605 = xbmc.getInfoLabel('Skin.String(background605)')
	background346 = xbmc.getInfoLabel('Skin.String(background346)')
	background348 = xbmc.getInfoLabel('Skin.String(background348)')
	background349 = xbmc.getInfoLabel('Skin.String(background349)')

if xbmc.getSkinDir() == 'skin.htpt':
	'''------------------------------
	---SKIN-STRINGS------------------
	------------------------------'''
	startupmusic = xbmc.getInfoLabel('!Skin.HasSetting(StartUpMusic)')
	startupmusicstr = xbmc.getInfoLabel('Skin.String(StartUpMusic)')
	startupvolumestr = xbmc.getInfoLabel('Skin.String(StartUpVolume)')

	customvar = xbmc.getInfoLabel('Skin.String(General_CustomVAR)')
	customsettingtemp = xbmc.getInfoLabel('Skin.String(Custom_Setting_Temp)') #TEMP
	
irtype = xbmc.getInfoLabel('Skin.String(IRtype)')
listitemtvshowtitlestr = xbmc.getInfoLabel('Skin.String(ListItemTVShowTitle)')
listitemgenrestr = xbmc.getInfoLabel('Skin.String(ListItemGenre)')
listitemdurationstr = xbmc.getInfoLabel('Skin.String(ListItemDuration)')
listitemratingstr = xbmc.getInfoLabel('Skin.String(ListItemRating)')
listitemyearstr = xbmc.getInfoLabel('Skin.String(ListItemYear)')
macstr = xbmc.getInfoLabel('Skin.String(MAC)')
mac1str = xbmc.getInfoLabel('Skin.String(MAC1)')
mac2str = xbmc.getInfoLabel('Skin.String(MAC2)')
mac3str = xbmc.getInfoLabel('Skin.String(MAC3)')
mac5str = xbmc.getInfoLabel('Skin.String(MAC5)')
macbL = ['B8:27:EB:CF:0C:19', 'F8:1A:67:19:EC:34', 'C4:4E:AC:00:99:58', '00:AA:05:01:B4:34']
messagescustom = xbmc.getInfoLabel('Skin.String(MessagesCustom)')

librarydataremotedatestr = xbmc.getInfoLabel('Skin.String(LibraryData_RemoteDate)')
librarydatalocaldatestr = xbmc.getInfoLabel('Skin.String(LibraryData_LocalDate)')
librarydataautoupdate = xbmc.getInfoLabel('!Skin.HasSetting(LibraryData_AutoUpdate)')

moviesestartup = xbmc.getInfoLabel('Skin.String(moviesestartup)')
musiclinkstr = xbmc.getInfoLabel('Skin.String(MusicLink)')
pingnow = xbmc.getInfoLabel('Skin.String(Ping_Now)')
pingrate = xbmc.getInfoLabel('Skin.String(Ping_Rate)')
settingslevel = xbmc.getInfoLabel('Skin.String(SettingsLevel)')
tvshowsestartup = xbmc.getInfoLabel('Skin.String(tvshowsestartup)')
varcurrentpicvidpath = xbmc.getInfoLabel('Skin.String(VarCurrentPicVidPath)')
usb1str = xbmc.getInfoLabel('Skin.String(USB1)')
usb2str = xbmc.getInfoLabel('Skin.String(USB2)')
usb3str = xbmc.getInfoLabel('Skin.String(USB3)')
usb4str = xbmc.getInfoLabel('Skin.String(USB4)')
usb5str = xbmc.getInfoLabel('Skin.String(USB5)')
'''---------------------------'''
overclocklevel = xbmc.getInfoLabel('Skin.String(OverClockLevel)')
countrystr = xbmc.getInfoLabel('Skin.String(Country)')
skinnamestr = xbmc.getInfoLabel('Skin.String(Skin_Name)')

'''------------------------------
---ID----------------------------
------------------------------'''
'''idstr = USERNAME EN , id1str = USERNAME HE, id2str = INSTALLATION DATE, id3str = WARRENTY END, id4str = ADDRESS, id5str = TELEPHONE NUMBER, id6str = PAYMENT TERMS, id7str = QUESTION, id8str = TECHNICAL NAME, id9str = CODE RED, id10str = HTPT'S MODEL, ID11 = MAC1, ID12 = MAC2'''
idstr = xbmc.getInfoLabel('Skin.String(ID)')
id1str = xbmc.getInfoLabel('Skin.String(ID1)')
id2str = xbmc.getInfoLabel('Skin.String(ID2)')
id3str = xbmc.getInfoLabel('Skin.String(ID3)')
id4str = xbmc.getInfoLabel('Skin.String(ID4)')
id5str = xbmc.getInfoLabel('Skin.String(ID5)')
id6str = xbmc.getInfoLabel('Skin.String(ID6)')
id7str = xbmc.getInfoLabel('Skin.String(ID7)')
id8str = xbmc.getInfoLabel('Skin.String(ID8)')
id9str = xbmc.getInfoLabel('Skin.String(ID9)')
id10str = xbmc.getInfoLabel('Skin.String(ID10)')
id11str = xbmc.getInfoLabel('Skin.String(ID11)')
id12str = xbmc.getInfoLabel('Skin.String(ID12)')
id40str = xbmc.getInfoLabel('Skin.HasSetting(ID40)') #Installed
id60str = xbmc.getInfoLabel('Skin.String(ID60)')
''''''
id2namestr = xbmc.getInfoLabel('$LOCALIZE[70010]') #Installation Date
id3namestr = xbmc.getInfoLabel('$LOCALIZE[70011]')
id5namestr = xbmc.getInfoLabel('$LOCALIZE[75006]')
id7namestr = 'Question'
id8namestr = xbmc.getInfoLabel('$LOCALIZE[70013]')
id9namestr = 'CODE RED'
id10namestr = xbmc.getInfoLabel('$LOCALIZE[79031]')
id11namestr = 'MAC1 (LAN)'
id12namestr = 'MAC2 (WLAN)'
''''''
trial = xbmc.getInfoLabel('Skin.HasSetting(Trial)') #TEMP
trialdate = xbmc.getInfoLabel('Skin.String(TrialDate)')
trialdate2 = xbmc.getInfoLabel('Skin.String(TrialDate2)')

idtrial = 'htptuser'
idpstr = xbmc.getInfoLabel('$LOCALIZE[79246]')
idp2str = xbmc.getInfoLabel('$LOCALIZE[79247]')


'''------------------------------
---ACCOUNTS----------------------
------------------------------'''
'''REALDEBRID'''
Account1_Active = xbmc.getInfoLabel('Skin.HasSetting(Account1_Active)')
Account1_Period = xbmc.getInfoLabel('Skin.String(Account1_Period)')
Account1_EndDate = xbmc.getInfoLabel('Skin.String(Account1_EndDate)')
#Account1_User = xbmc.getInfoLabel('Skin.String(Account1_User)')
#Account1_Pass = xbmc.getInfoLabel('Skin.String(Account1_Pass)')
'''SDAROT TV'''
Account2_Active = xbmc.getInfoLabel('Skin.HasSetting(Account2_Active)')
Account2_Period = xbmc.getInfoLabel('Skin.String(Account2_Period)')
Account2_EndDate = xbmc.getInfoLabel('Skin.String(Account2_EndDate)')
'''MOVREEL'''
Account3_Active = xbmc.getInfoLabel('Skin.HasSetting(Account3_Active)')
Account3_Period = xbmc.getInfoLabel('Skin.String(Account3_Period)')
Account3_EndDate = xbmc.getInfoLabel('Skin.String(Account3_EndDate)')
'''PREMIUMIZE'''
Account4_Active = xbmc.getInfoLabel('Skin.HasSetting(Account4_Active)')
Account4_Period = xbmc.getInfoLabel('Skin.String(Account4_Period)')
Account4_EndDate = xbmc.getInfoLabel('Skin.String(Account4_EndDate)')
'''NOOBROOM'''
Account5_Active = xbmc.getInfoLabel('Skin.HasSetting(Account5_Active)')
Account5_Period = xbmc.getInfoLabel('Skin.String(Account5_Period)')
Account5_EndDate = xbmc.getInfoLabel('Skin.String(Account5_EndDate)')
''''''
Account6_Active = xbmc.getInfoLabel('Skin.HasSetting(Account6_Active)')
Account6_Period = xbmc.getInfoLabel('Skin.String(Account6_Period)')
Account6_EndDate = xbmc.getInfoLabel('Skin.String(Account6_EndDate)')
''''''
Account7_Active = xbmc.getInfoLabel('Skin.HasSetting(Account7_Active)')
Account7_Period = xbmc.getInfoLabel('Skin.String(Account7_Period)')
Account7_EndDate = xbmc.getInfoLabel('Skin.String(Account7_EndDate)')
''''''
Account8_Active = xbmc.getInfoLabel('Skin.HasSetting(Account8_Active)')
Account8_Period = xbmc.getInfoLabel('Skin.String(Account8_Period)')
Account8_EndDate = xbmc.getInfoLabel('Skin.String(Account8_EndDate)')
''''''
Account9_Active = xbmc.getInfoLabel('Skin.HasSetting(Account9_Active)')
Account9_Period = xbmc.getInfoLabel('Skin.String(Account9_Period)')
Account9_EndDate = xbmc.getInfoLabel('Skin.String(Account9_EndDate)')
''''''
Account10_Active = xbmc.getInfoLabel('Skin.HasSetting(Account10_Active)')
Account10_Period = xbmc.getInfoLabel('Skin.String(Account10_Period)')
Account10_EndDate = xbmc.getInfoLabel('Skin.String(Account10_EndDate)')
'''---------------------------'''
	
'''------------------------------
---Playlist----------------------
------------------------------'''
playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
playlistlengthN = int(playlistlength)
playlistposition = xbmc.getInfoLabel('Playlist.Position(video)')
playlistpositionN = int(playlistposition)
playlistrepeat = xbmc.getInfoLabel('Playlist.Repeat')
playlistrandom = xbmc.getInfoLabel('Playlist.Random')
'''---------------------------'''


'''------------------------------
---Player------------------------
------------------------------'''
playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
playerpaused = xbmc.getCondVisibility('Player.Paused')
playercache = xbmc.getInfoLabel('Player.CacheLevel')
playertitle = xbmc.getInfoLabel('Player.Title')
playerfilename = xbmc.getInfoLabel('Player.Filename')
playerhasaudio = xbmc.getCondVisibility('Player.HasAudio')
playerhasmedia = xbmc.getCondVisibility('Player.HasMedia')
playerfolderpath = xbmc.getInfoLabel('Player.FolderPath')
playertime = xbmc.getInfoLabel("Player.Time(hh)") + xbmc.getInfoLabel("Player.Time(mm)") + xbmc.getInfoLabel("Player.Time(ss)")
playertimeremaining = xbmc.getInfoLabel("Player.TimeRemaining(hh)") + xbmc.getInfoLabel("Player.TimeRemaining(mm)") + xbmc.getInfoLabel("Player.TimeRemaining(ss)")
playerduration = xbmc.getInfoLabel("Player.Duration(hh)") + xbmc.getInfoLabel("Player.Duration(mm)") + xbmc.getInfoLabel("Player.Duration(ss)")
'''---------------------------'''

'''------------------------------
---PATH--------------------------
------------------------------'''
israeltvhome = 'plugin://plugin.video.sdarot.tv/'
videorootpath = 'library://video/'
temp_path = os.path.join(xbmc.translatePath("special://temp/").decode("utf-8"))
home_path = os.path.join(xbmc.translatePath("special://home/").decode("utf-8"))
xbmc_path = os.path.join(xbmc.translatePath("special://xbmc/").decode("utf-8"))
addons_path = os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"))
addonsDir = os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8")) #TEMP
userdata_path = os.path.join(xbmc.translatePath("special://userdata/").decode("utf-8"))
#
thumbnails_path = os.path.join(xbmc.translatePath("special://thumbnails").decode("utf-8"))
database_path = os.path.join(xbmc.translatePath("special://database").decode("utf-8"))
varmedia_path = os.path.join('/','var','media', '')

keymaps_path = os.path.join(userdata_path,'keymaps', '')
library_path = os.path.join(userdata_path,'library', '')
rom_path = os.path.join('storage','emulators','retroarch','rom','')
emulators_path = os.path.join('storage','emulators','')
config_path = os.path.join('/storage/','.config','')
flash_path = os.path.join('/flash', '')
downloads_path = os.path.join(library_path,'downloads','')
music_path = os.path.join(library_path,'music','')
pictures_path = os.path.join(library_path,'pictures','')
movies_path = os.path.join(library_path,'movies','')
tvshows_path = os.path.join(library_path,'tvshows','')
addondata_path = os.path.join(userdata_path,'addon_data','')
skin_music_path = os.path.join(addondata_path,'skin.htpt', 'music', '')
skin_userdata_path = os.path.join(addondata_path,'skin.htpt', 'userdata', '')
packages_path = os.path.join(addons_path,'packages','')

#skin_path = os.path.join(xbmc.translatePath("special://skin").decode("utf-8"))
skin_path = os.path.join(addons_path,'skin.htpt','') #WIP
skin_specials_userdata_path = os.path.join(skin_path, 'specials', 'scripts', 'copy', 'userdata', '')
htptservice_path = os.path.join(addons_path,'service.htpt','')
htptservicemedia_path = os.path.join(htptservice_path, 'resources', 'media', '')
htptservicecopy_path = os.path.join(htptservice_path,'specials','scripts','copy','')
packagesDir = os.path.join(addonsDir,'packages') #TEMP
'''---------------------------'''
if admin and not admin2 and 1 + 1 == 3:
	print printfirst + "variables paths list" + space2 + \
	newline + "skin_path" + space2 + skin_path + \
	newline + "home_path" + space2 + home_path + \
	newline + "addons_path" + space2 + addons_path + \
	newline + "skin_userdata_path" + space2 + skin_userdata_path + \
	newline + "packages_path" + space2 + packages_path + \
	newline + "varmedia_path" + space2 + varmedia_path + \
	newline + "temp_path" + space2 + temp_path

'''------------------------------
---?--------------------------
------------------------------'''
skinlog_file = os.path.join(skin_path,'changelog.txt')
skininstalledtxt2 = os.path.join(home_path, 'Skin_Installed.txt')
guisettings_file = os.path.join(userdata_path, 'guisettings.xml')
guisettings2_file = os.path.join(skin_userdata_path, 'guisettings.xml')
guisettings3_file = os.path.join(skin_userdata_path, 'guisettings2.xml')
guisettings4_file = os.path.join(skin_userdata_path, 'guisettings_.xml')
'''---------------------------'''

'''------------------------------
---Network.----------------------
------------------------------'''
dhcpaddress = xbmc.getInfoLabel('Network.DHCPAddress')
macaddress = xbmc.getInfoLabel('Network.MacAddress')
networkgatewayaddress = xbmc.getInfoLabel('Network.GatewayAddress')
networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
systemhasnetwork = xbmc.getCondVisibility('System.HasNetwork')
'''---------------------------'''

'''------------------------------
---MIXED-------------------------
------------------------------'''

'''---------------------------'''

if xbmc.getSkinDir() == 'skin.htpt':
	'''------------------------------
	---$VAR--------------------------
	------------------------------'''
	startupmessage2 = xbmc.getInfoLabel('$VAR[StartupMessage2]')
	'''---------------------------'''
	topvideoinformation1var = xbmc.getInfoLabel('$VAR[TopVideoInformation1]') #Duration+
	topvideoinformation2var = xbmc.getInfoLabel('$VAR[TopVideoInformation2]') #Year+
	topvideoinformation3var = xbmc.getInfoLabel('$VAR[TopVideoInformation3]') #Rating
	topvideoinformation4var = xbmc.getInfoLabel('$VAR[TopVideoInformation4]') #Poster+
	topvideoinformation5var = xbmc.getInfoLabel('$VAR[TopVideoInformation5]') #Plot
	topvideoinformation6var = xbmc.getInfoLabel('$VAR[TopVideoInformation6]') #Genre
	topvideoinformation7var = xbmc.getInfoLabel('$VAR[TopVideoInformation7]') #Tag+
	topvideoinformation8var = xbmc.getInfoLabel('$VAR[TopVideoInformation8]') #Title
	topvideoinformation9var = xbmc.getInfoLabel('$VAR[TopVideoInformation9]') #Episode Thumb
	'''---------------------------'''
	topinformation2var = xbmc.getInfoLabel('$VAR[TopInformation2]') #Left
	topinformation3var = xbmc.getInfoLabel('$VAR[TopInformation3]') #Middle

'''------------------------------
---CUSTOM------------------------
------------------------------'''
htpt_a1 = 'htpt'
htpt_a2 = 'TULU'

'''------------------------------
---$LOCALIZE-PRIMARY-------------
------------------------------'''
str1 = xbmc.getInfoLabel('$LOCALIZE[1]').decode('utf-8') #Pictures
str2 = xbmc.getInfoLabel('$LOCALIZE[2]').decode('utf-8') #Music
str3 = xbmc.getInfoLabel('$LOCALIZE[3]').decode('utf-8') #Videos
settingslevelstr1 = xbmc.getInfoLabel('$LOCALIZE[10036]') #Basic
settingslevelstr2 = xbmc.getInfoLabel('$LOCALIZE[10037]') #Standard
settingslevelstr3 = xbmc.getInfoLabel('$LOCALIZE[10038]') #Advanced
settingslevelstr4 = xbmc.getInfoLabel('$LOCALIZE[10039]') #Expert

str20161 = xbmc.getInfoLabel('$LOCALIZE[20161]') #Total
str20329 = xbmc.getInfoLabel('$LOCALIZE[20329]') #Movies are in separate folders that match the movie title
str20333 = xbmc.getInfoLabel('$LOCALIZE[20333]') #Set content
str20343 = xbmc.getInfoLabel('$LOCALIZE[20343]').decode('utf-8') #TV shows
str20346 = xbmc.getInfoLabel('$LOCALIZE[20346]').decode('utf-8') #Scan recursively
str20389 = xbmc.getInfoLabel('$LOCALIZE[20389]') #Music videos
falsestr = xbmc.getInfoLabel('$LOCALIZE[20424]') #False
str20442 = xbmc.getInfoLabel('$LOCALIZE[20442]') #Change content
str24056 = xbmc.getInfoLabel('$LOCALIZE[24056]').decode('utf-8') #Last updated %s
str24063 = xbmc.getInfoLabel('$LOCALIZE[24063]').decode('utf-8') #Auto update
str24065 = xbmc.getInfoLabel('$LOCALIZE[24065]').decode('utf-8') #Add-on updated
str24068 = xbmc.getInfoLabel('$LOCALIZE[24068]').decode('utf-8') #Update available
str22082 = xbmc.getInfoLabel('$LOCALIZE[22082]').decode('utf-8') #More...
str24021 = xbmc.getInfoLabel('$LOCALIZE[24021]').decode('utf-8') #Disable
str24022 = xbmc.getInfoLabel('$LOCALIZE[24022]').decode('utf-8') #Enable
str24055 = xbmc.getInfoLabel('$LOCALIZE[24055]').decode('utf-8') #Check for updates
str24074 = xbmc.getInfoLabel('$LOCALIZE[24074]').decode('utf-8') #Needs to restart
str33078 = xbmc.getInfoLabel('$LOCALIZE[33078]').decode('utf-8') #Next page
str36901 = xbmc.getInfoLabel('$LOCALIZE[36901]').decode('utf-8') #movies
str36903 = xbmc.getInfoLabel('$LOCALIZE[36903]').decode('utf-8') #TV shows
str36909 = xbmc.getInfoLabel('$LOCALIZE[36909]') #musicvideos
'''---------------------------'''

if xbmc.getSkinDir() == 'skin.htpt':
	'''------------------------------
	---$LOCALIZE-SKIN----------------
	------------------------------'''

	if not admin3: str31407 = xbmc.getInfoLabel('$LOCALIZE[31407]').decode('utf-8') #Please wait
	str70000 = xbmc.getInfoLabel('$LOCALIZE[70000]') #!
	todaystr = xbmc.getInfoLabel('$LOCALIZE[33006]') #Today (remove?)
	id6v1str = xbmc.getInfoLabel('$LOCALIZE[70014]').decode('utf-8') #One-Time
	id6v2str = xbmc.getInfoLabel('$LOCALIZE[70015]').decode('utf-8') #Per-Month
	id6v3str = xbmc.getInfoLabel('$LOCALIZE[70016]').decode('utf-8') #Per-2Months
	str70020 = xbmc.getInfoLabel('$LOCALIZE[70020]') #WOULD YOU LIKE TO ADD THIS CONTENT TO HTPT?
	str72101 = xbmc.getInfoLabel('$LOCALIZE[72101]').decode('utf-8') #Today
	str72102 = xbmc.getInfoLabel('$LOCALIZE[72102]').decode('utf-8') #Yesterday
	str72103 = xbmc.getInfoLabel('$LOCALIZE[72103]').decode('utf-8') #This Week
	str73440 = xbmc.getInfoLabel('$LOCALIZE[73440]').decode('utf-8') #GoPro

	str74481 = xbmc.getInfoLabel('$LOCALIZE[74481]').decode('utf-8') #Starting a Send Report
	str74482 = xbmc.getInfoLabel('$LOCALIZE[74482]').decode('utf-8') #Sending Report (%s/%s)
	str74483 = xbmc.getInfoLabel('$LOCALIZE[74483]').decode('utf-8') #The report has been sent successfully
	str74484 = xbmc.getInfoLabel('$LOCALIZE[74484]').decode('utf-8') #Report has failed!
	str74485 = xbmc.getInfoLabel('$LOCALIZE[74485]').decode('utf-8') #htpt

	str74540 = xbmc.getInfoLabel('$LOCALIZE[74540]').decode('utf-8') #Your htpt model is %s
	str74541 = xbmc.getInfoLabel('$LOCALIZE[74541]').decode('utf-8') #This model support external media storage only!
	str74542 = xbmc.getInfoLabel('$LOCALIZE[74542]').decode('utf-8') #[CR][CR][COLOR=White2]For support please contact us by using the help button in the home screen.[/COLOR]
	str74543 = xbmc.getInfoLabel('$LOCALIZE[74543]').decode('utf-8') #This model has no support for %s
	str74544 = xbmc.getInfoLabel('$LOCALIZE[74544]').decode('utf-8') #This model has support for %s
	str74545 = xbmc.getInfoLabel('$LOCALIZE[74545]').decode('utf-8') #
	str74546 = xbmc.getInfoLabel('$LOCALIZE[74546]').decode('utf-8') #
	str74547 = xbmc.getInfoLabel('$LOCALIZE[74547]').decode('utf-8') #
	str74548 = xbmc.getInfoLabel('$LOCALIZE[74548]').decode('utf-8') #
	str74549 = xbmc.getInfoLabel('$LOCALIZE[74549]').decode('utf-8') #
	str74550 = xbmc.getInfoLabel('$LOCALIZE[74550]').decode('utf-8') #Add %s to library
	str74551 = xbmc.getInfoLabel('$LOCALIZE[74551]').decode('utf-8') #
	str74552 = xbmc.getInfoLabel('$LOCALIZE[74552]').decode('utf-8') #
	str74553 = xbmc.getInfoLabel('$LOCALIZE[74553]').decode('utf-8') #Unlocking device
	str74554 = xbmc.getInfoLabel('$LOCALIZE[74554]').decode('utf-8') #Reset skin settings
	str74555 = xbmc.getInfoLabel('$LOCALIZE[74555]').decode('utf-8') #
	str74556 = xbmc.getInfoLabel('$LOCALIZE[74556]').decode('utf-8') #
	str74557 = xbmc.getInfoLabel('$LOCALIZE[74557]').decode('utf-8') #
	str74558 = xbmc.getInfoLabel('$LOCALIZE[74558]').decode('utf-8') #
	str74559 = xbmc.getInfoLabel('$LOCALIZE[74559]').decode('utf-8') #
	str74560 = xbmc.getInfoLabel('$LOCALIZE[74560]').decode('utf-8') #
	str74561 = xbmc.getInfoLabel('$LOCALIZE[74561]').decode('utf-8') #
	str74562 = xbmc.getInfoLabel('$LOCALIZE[74562]').decode('utf-8') #
	str74563 = xbmc.getInfoLabel('$LOCALIZE[74563]').decode('utf-8') #
	str74564 = xbmc.getInfoLabel('$LOCALIZE[74564]').decode('utf-8') #
	str74565 = xbmc.getInfoLabel('$LOCALIZE[74565]').decode('utf-8') #
	str74566 = xbmc.getInfoLabel('$LOCALIZE[74566]').decode('utf-8') #
	str74567 = xbmc.getInfoLabel('$LOCALIZE[74567]').decode('utf-8') #
	str74568 = xbmc.getInfoLabel('$LOCALIZE[74568]').decode('utf-8') #
	str74569 = xbmc.getInfoLabel('$LOCALIZE[74569]').decode('utf-8') #
	str74570 = xbmc.getInfoLabel('$LOCALIZE[74570]').decode('utf-8') #
	str74571 = xbmc.getInfoLabel('$LOCALIZE[74571]').decode('utf-8') #
	str74572 = xbmc.getInfoLabel('$LOCALIZE[74572]').decode('utf-8') #
	str74573 = xbmc.getInfoLabel('$LOCALIZE[74573]').decode('utf-8') #
	str74574 = xbmc.getInfoLabel('$LOCALIZE[74574]').decode('utf-8') #
	str74575 = xbmc.getInfoLabel('$LOCALIZE[74575]').decode('utf-8') #
	str74576 = xbmc.getInfoLabel('$LOCALIZE[74576]').decode('utf-8') #
	str74577 = xbmc.getInfoLabel('$LOCALIZE[74577]').decode('utf-8') #
	str74578 = xbmc.getInfoLabel('$LOCALIZE[74578]').decode('utf-8') #
	str74579 = xbmc.getInfoLabel('$LOCALIZE[74579]').decode('utf-8') #
	str74580 = xbmc.getInfoLabel('$LOCALIZE[74580]').decode('utf-8') #
	str74581 = xbmc.getInfoLabel('$LOCALIZE[74581]').decode('utf-8') #
	str74582 = xbmc.getInfoLabel('$LOCALIZE[74582]').decode('utf-8') #
	str74583 = xbmc.getInfoLabel('$LOCALIZE[74583]').decode('utf-8') #
	str74584 = xbmc.getInfoLabel('$LOCALIZE[74584]').decode('utf-8') #
	str74585 = xbmc.getInfoLabel('$LOCALIZE[74585]').decode('utf-8') #
	str74586 = xbmc.getInfoLabel('$LOCALIZE[74586]').decode('utf-8') #
	str74587 = xbmc.getInfoLabel('$LOCALIZE[74587]').decode('utf-8') #
	str74588 = xbmc.getInfoLabel('$LOCALIZE[74588]').decode('utf-8') #
	str74589 = xbmc.getInfoLabel('$LOCALIZE[74589]').decode('utf-8') #
	str74590 = xbmc.getInfoLabel('$LOCALIZE[74590]').decode('utf-8') #
	str74591 = xbmc.getInfoLabel('$LOCALIZE[74591]').decode('utf-8') #
	str74592 = xbmc.getInfoLabel('$LOCALIZE[74592]').decode('utf-8') #
	str74593 = xbmc.getInfoLabel('$LOCALIZE[74593]').decode('utf-8') #
	str74594 = xbmc.getInfoLabel('$LOCALIZE[74594]').decode('utf-8') #
	str74595 = xbmc.getInfoLabel('$LOCALIZE[74595]').decode('utf-8') #
	str74596 = xbmc.getInfoLabel('$LOCALIZE[74596]').decode('utf-8') #
	str74597 = xbmc.getInfoLabel('$LOCALIZE[74597]').decode('utf-8') #
	str74598 = xbmc.getInfoLabel('$LOCALIZE[74598]').decode('utf-8') #
	str74599 = xbmc.getInfoLabel('$LOCALIZE[74599]').decode('utf-8') #
	str74600 = xbmc.getInfoLabel('$LOCALIZE[74600]').decode('utf-8') #
	str74601 = xbmc.getInfoLabel('$LOCALIZE[74601]').decode('utf-8') #
	str74602 = xbmc.getInfoLabel('$LOCALIZE[74602]').decode('utf-8') #
	str74603 = xbmc.getInfoLabel('$LOCALIZE[74603]').decode('utf-8') #
	str74604 = xbmc.getInfoLabel('$LOCALIZE[74604]').decode('utf-8') #
	str74605 = xbmc.getInfoLabel('$LOCALIZE[74605]').decode('utf-8') #
	str74606 = xbmc.getInfoLabel('$LOCALIZE[74606]').decode('utf-8') #
	str74607 = xbmc.getInfoLabel('$LOCALIZE[74607]').decode('utf-8') #
	str74608 = xbmc.getInfoLabel('$LOCALIZE[74608]').decode('utf-8') #
	str74609 = xbmc.getInfoLabel('$LOCALIZE[74609]').decode('utf-8') #
	str75209 = xbmc.getInfoLabel('$LOCALIZE[75209]').decode('utf-8') #Test the fix by adding %s to the library (search/add + menu button)
	str78971 = xbmc.getInfoLabel('$LOCALIZE[78971]').decode('utf-8') #Doing Manual Fix
	str78974 = xbmc.getInfoLabel('$LOCALIZE[78974]').decode('utf-8') #Fix failed!
	str78978 = xbmc.getInfoLabel('$LOCALIZE[78978]').decode('utf-8') #The system has found an unfair use!!!
	str78981 = xbmc.getInfoLabel('$LOCALIZE[78981]').decode('utf-8') #Would you like to proceed with the fix at this time?
	str78985 = xbmc.getInfoLabel('$LOCALIZE[78985]').decode('utf-8') #Manual fix is available!
	str78986 = xbmc.getInfoLabel('$LOCALIZE[78986]').decode('utf-8') #Fix Succeeded!
	str79058 = xbmc.getInfoLabel('$LOCALIZE[79058]').decode('utf-8') #Describe your issue in short
	str79089 = xbmc.getInfoLabel('$LOCALIZE[79089]').decode('utf-8') #
	str79495 = xbmc.getInfoLabel('$LOCALIZE[79495]').decode('utf-8') #Try again
	str79496 = xbmc.getInfoLabel('$LOCALIZE[79496]').decode('utf-8') #This feature is under development
	str79497 = xbmc.getInfoLabel('$LOCALIZE[79497]').decode('utf-8') #Thank you for your patience
	str79504 = xbmc.getInfoLabel('$LOCALIZE[79504]').decode('utf-8') #Would you like to try again?
	str79545 = xbmc.getInfoLabel('$LOCALIZE[79545]').decode('utf-8') #
	str79550 = xbmc.getInfoLabel('$LOCALIZE[79550]').decode('utf-8') #
	str79551 = xbmc.getInfoLabel('$LOCALIZE[79551]').decode('utf-8') #SERVICE CALL RECEIVED
	str79552 = xbmc.getInfoLabel('$LOCALIZE[79552]').decode('utf-8') #TRIAL RENEWED
	str79553 = xbmc.getInfoLabel('$LOCALIZE[79553]').decode('utf-8') #TRIAL ENDED
	str79554 = xbmc.getInfoLabel('$LOCALIZE[79554]').decode('utf-8') #DEVICE SUSPEND
	str79555 = xbmc.getInfoLabel('$LOCALIZE[79555]').decode('utf-8') #DEVICE SABOTAGE
	str79556 = xbmc.getInfoLabel('$LOCALIZE[79556]').decode('utf-8') #DEVICE FIXED
	str79557 = xbmc.getInfoLabel('$LOCALIZE[79557]').decode('utf-8') #DEVICE SOFT-REBOOTED
	str79558 = xbmc.getInfoLabel('$LOCALIZE[79558]').decode('utf-8') #DEVICE REBOOTED
	str79559= xbmc.getInfoLabel('$LOCALIZE[79559]').decode('utf-8') #DEVICE POWEROFF
	str79560 = xbmc.getInfoLabel('$LOCALIZE[79560]').decode('utf-8') #DEVICE POWEROFF %s
	str79561 = xbmc.getInfoLabel('$LOCALIZE[79561]').decode('utf-8') #DEVICE AUTO POWEROFF
	str79562 = xbmc.getInfoLabel('$LOCALIZE[79562]').decode('utf-8') #DEVICE ACTIVATED
	str79563 = xbmc.getInfoLabel('$LOCALIZE[79563]').decode('utf-8') #UNAUTHORIZED
	str79564 = xbmc.getInfoLabel('$LOCALIZE[79564]').decode('utf-8') #DEVICE AT STARTUP 12m
	str79565 = xbmc.getInfoLabel('$LOCALIZE[79565]').decode('utf-8') #DEVICE ACTIVATE 2h
	str79566 = xbmc.getInfoLabel('$LOCALIZE[79566]').decode('utf-8') #DEVICE ERROR %s
	str79567 = xbmc.getInfoLabel('$LOCALIZE[79567]').decode('utf-8') #DEVICE ACTIVATE 1h
	str79568 = xbmc.getInfoLabel('$LOCALIZE[79568]').decode('utf-8') #DEVICE PURCHASED
	str79569 = xbmc.getInfoLabel('$LOCALIZE[79569]').decode('utf-8') #VERSION UPDATED
	str79570 = xbmc.getInfoLabel('$LOCALIZE[79570]').decode('utf-8') #INSTALLED
	str79571 = xbmc.getInfoLabel('$LOCALIZE[79571]').decode('utf-8') #UNINSTALLED
	str79573 = xbmc.getInfoLabel('$LOCALIZE[79573]').decode('utf-8') #Previous period
	str79574 = xbmc.getInfoLabel('$LOCALIZE[79574]').decode('utf-8') #New period

	str79577 = xbmc.getInfoLabel('$LOCALIZE[79577]').decode('utf-8') #Update Movies and Tvshows library
	str79583 = xbmc.getInfoLabel('$LOCALIZE[79583]').decode('utf-8') #Added
	str79584 = xbmc.getInfoLabel('$LOCALIZE[79584]').decode('utf-8') #


	str75004 = xbmc.getInfoLabel('$LOCALIZE[75004]').decode('utf-8') #Local Music
	str75687 = xbmc.getInfoLabel('$LOCALIZE[75687]').decode('utf-8') #Update History
	str78992 = xbmc.getInfoLabel('$LOCALIZE[78992]').decode('utf-8') #All the Music
	str79046 = xbmc.getInfoLabel('$LOCALIZE[79046]').decode('utf-8') #Deactivated
	str79072 = xbmc.getInfoLabel('$LOCALIZE[79072]').decode('utf-8') #
	str79081 = xbmc.getInfoLabel('$LOCALIZE[79081]').decode('utf-8') #email
	str79211 = xbmc.getInfoLabel('$LOCALIZE[79211]').decode('utf-8') #Trial Period Has Ended
	str79311 = xbmc.getInfoLabel('$LOCALIZE[79311]').decode('utf-8') #%s Button Version Updated
	str73220 = xbmc.getInfoLabel('$LOCALIZE[73220]').decode('utf-8') #Kids
	str75005 = xbmc.getInfoLabel('$LOCALIZE[75005]').decode('utf-8') #Israeli Music
	str79041 = xbmc.getInfoLabel('$LOCALIZE[79041]') #YUKU*
	str79201 = xbmc.getInfoLabel('$LOCALIZE[79201]').decode('utf-8') #System Version Updated
	str79215 = xbmc.getInfoLabel('$LOCALIZE[79215]') #Warning: Internet Browsing
	str79216 = xbmc.getInfoLabel('$LOCALIZE[79216]') #VERIFY YOU HAVE A KEYBOARD BEFORE PROCEEDING!
	str79217 = xbmc.getInfoLabel('$LOCALIZE[79217]') #Use the following keys in order to return:
	str79218 = xbmc.getInfoLabel('$LOCALIZE[79218]') #ESC / ALT-TAB / ALT+F4
	str79498 = xbmc.getInfoLabel('$LOCALIZE[79498]').decode('utf-8') #EXTERNAL DEVICES
	str79520 = xbmc.getInfoLabel('$LOCALIZE[79520]').decode('utf-8') #Quick Play
	str79521 = xbmc.getInfoLabel('$LOCALIZE[79521]').decode('utf-8') #More Results
	str79522 = xbmc.getInfoLabel('$LOCALIZE[79522]').decode('utf-8') #View Playlist
	str79523 = xbmc.getInfoLabel('$LOCALIZE[79523]').decode('utf-8') #Activate TV Mode?
	str79524 = xbmc.getInfoLabel('$LOCALIZE[79524]').decode('utf-8') #
	str79525 = xbmc.getInfoLabel('$LOCALIZE[79525]').decode('utf-8') #TV Mode
	str79526 = xbmc.getInfoLabel('$LOCALIZE[79526]').decode('utf-8') #Quick-Play (Description)...
	str79527 = xbmc.getInfoLabel('$LOCALIZE[79527]').decode('utf-8') #Play List (Description)...
	str79528 = xbmc.getInfoLabel('$LOCALIZE[79528]').decode('utf-8') #More Result (Description)...
	str79529 = xbmc.getInfoLabel('$LOCALIZE[79529]').decode('utf-8') #Preparing TV Mode...
	str79530 = xbmc.getInfoLabel('$LOCALIZE[79530]').decode('utf-8') #Various performances
	str79531 = xbmc.getInfoLabel('$LOCALIZE[79531]').decode('utf-8') #The system issued an automatic abort
	str79535 = xbmc.getInfoLabel('$LOCALIZE[79535]').decode('utf-8') #
	str79536 = xbmc.getInfoLabel('$LOCALIZE[79536]').decode('utf-8') #Begining: %s   |   End: %s
	str79537 = xbmc.getInfoLabel('$LOCALIZE[79537]').decode('utf-8') #
	str79538 = xbmc.getInfoLabel('$LOCALIZE[79538]').decode('utf-8') #Hello %s,
	str79539 = xbmc.getInfoLabel('$LOCALIZE[79539]').decode('utf-8') #Invalid Phone Number!


	str79540 = xbmc.getInfoLabel('$LOCALIZE[79540]').decode('utf-8') #%s Files found in %s Folder
	str79541 = xbmc.getInfoLabel('$LOCALIZE[79541]').decode('utf-8') #Would you like to delete those files?
	str79542 = xbmc.getInfoLabel('$LOCALIZE[79542]').decode('utf-8') #Fix issued successfuly
	str79543 = xbmc.getInfoLabel('$LOCALIZE[79543]').decode('utf-8') #Cleaning Library No. %s %s
	str79544 = xbmc.getInfoLabel('$LOCALIZE[79544]').decode('utf-8') #Last Service Call
	str79548 = xbmc.getInfoLabel('$LOCALIZE[79548]').decode('utf-8') #
	str79549 = xbmc.getInfoLabel('$LOCALIZE[79549]').decode('utf-8') #
	numinumistr = xbmc.getInfoLabel('$LOCALIZE[79068]')
	idpstr = xbmc.getInfoLabel('$LOCALIZE[79246]')
	idp2str = xbmc.getInfoLabel('$LOCALIZE[79247]')

'''------------------------------
---CUSTOM-$LOCALIZE--------------
------------------------------'''
blockedL = ["htptuser3", "htptuser9"]
macstr2 = xbmc.getInfoLabel('Network.MacAddress') + " ( " + xbmc.getInfoLabel('Skin.String(MAC1)') + " / " + xbmc.getInfoLabel('Skin.String(MAC2)') + " )"
'''---------------------------'''

'''------------------------------
---LIST--------------------------
------------------------------'''

'''---------------------------'''

'''------------------------------
---DEBUG-------------------------
------------------------------'''
ap = "r"
bp = "o"
cp = "m"
dp = "1"
ep = "2"
fp = "3"
gp = "4"
hp = "5"
hi = "6"
ip = "d"
jp = "D"
kp = "#"
sendtostr = "htptdebugout@gmail.com"
sendtostr1 = "htptdebugout@mail.com"
sendtostr2 = "htptdebugout2@gmail.com"
sendtostr3 = "htptdebugout3@gmail.com"
sendtostr4 = "htptdebugout4@gmail.com"
sendtostr5 = "htptdebugout@outlook.com"
sendtostr14 = "htptdebugout@yahoo.com"
recipientstr = "fixhtpt@gmail.com"
mystr = ap + bp + cp + dp + ep + fp + gp + hp + hi
mystr2 = ap + bp + cp + dp + ep + fp + gp + hp
'''---------------------------'''

'''------------------------------
---Window(Home).Property(key)----
------------------------------'''
windowhomeproperty_moviescount = xbmc.getInfoLabel('Window(Home).Property(Movies.Count)')
windowhomeproperty_tvshowscount = xbmc.getInfoLabel('Window(Home).Property(TVShows.Count)')
'''---------------------------'''


'''------------------------------
---LISTITEM-------------
------------------------------'''
listitemduration = xbmc.getInfoLabel('ListItem.Duration')
listitemepisode = xbmc.getInfoLabel('ListItem.Episode')
listitemgenre = xbmc.getInfoLabel('ListItem.Genre')
listitempath = xbmc.getInfoLabel('ListItem.Path')
listitemrating = xbmc.getInfoLabel('ListItem.Rating')
listitemseason = xbmc.getInfoLabel('ListItem.Season')
listitemtitle = xbmc.getInfoLabel('ListItem.Title')
listitemtvshowtitle = xbmc.getInfoLabel('ListItem.TVShowTitle')
listitemlabel = xbmc.getInfoLabel('ListItem.Label')
listitemyear = xbmc.getInfoLabel('ListItem.Year')
listitemimdbnumber = xbmc.getInfoLabel('ListItem.IMDBNumber')
listitemdbid = xbmc.getInfoLabel('ListItem.DBID')
listitemdirector = xbmc.getInfoLabel('ListItem.Director')
listitemisselected = xbmc.getCondVisibility('ListItem.IsSelected')
'''---------------------------'''

'''------------------------------
---Library.----------------------
------------------------------'''
libraryhascontentmovies = xbmc.getCondVisibility('Library.HasContent(Movies)')
libraryhascontentmoviesets = xbmc.getCondVisibility('Library.HasContent(MovieSets)')
libraryhascontentmusic = xbmc.getCondVisibility('Library.HasContent(Music)')
libraryhascontentmusicvideos = xbmc.getCondVisibility('Library.HasContent(MusicVideos)')
libraryhascontenttvshows = xbmc.getCondVisibility('Library.HasContent(TVShows)')
libraryhascontentvideo = xbmc.getCondVisibility('Library.HasContent(Video)')
libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
libraryisscanningmusic = xbmc.getCondVisibility('Library.IsScanningMusic')
'''---------------------------'''

'''------------------------------
---EMPTY-------------------------
------------------------------'''
controlhasfocus698 = ""
controlhasfocus699 = ""



'''------------------------------
---CONTROL-----------------------
------------------------------'''
autoplaypausebutton = (xbmc.getCondVisibility('Window.IsVisible(Home.xml)') and xbmc.getCondVisibility('Control.HasFocus(9093)')) or (xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)') and xbmc.getCondVisibility('Control.HasFocus(111)'))
subtitleosdbutton = xbmc.getCondVisibility('Control.HasFocus(703)') #subtitleosdbutton
volumeosdbutton = xbmc.getCondVisibility('Control.HasFocus(707)') #volumeosdbutton

button99 = xbmc.getCondVisibility('Control.HasFocus(99)')
button100 = xbmc.getCondVisibility('Control.HasFocus(100)')
button101 = xbmc.getCondVisibility('Control.HasFocus(101)')
button102 = xbmc.getCondVisibility('Control.HasFocus(102)')
button103 = xbmc.getCondVisibility('Control.HasFocus(103)')
button104 = xbmc.getCondVisibility('Control.HasFocus(104)')
button105 = xbmc.getCondVisibility('Control.HasFocus(105)')

cancelbutton = xbmc.getCondVisibility('Control.HasFocus(10)') and xbmc.getCondVisibility('Window.IsActive(DialogProgress.xml)')
controlgetlabel1 = xbmc.getInfoLabel('Control.GetLabel(1)')
controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
controlhasfocus10 = xbmc.getCondVisibility('Control.HasFocus(10)') #No button
controlhasfocus11 = xbmc.getCondVisibility('Control.HasFocus(11)') #Yes button
controlhasfocus20 = xbmc.getCondVisibility('Control.HasFocus(20)')
controlisvisible311 = xbmc.getCondVisibility('Control.IsVisible(311)') or xbmc.getCondVisibility('Control.HasFocus(340)')
controlisvisible311S = str(controlisvisible311)
controlisvisible312 = xbmc.getCondVisibility('Control.IsVisible(312)') or xbmc.getCondVisibility('Control.HasFocus(341)')
controlisvisible312S = str(controlisvisible312)

debugbutton = xbmc.getCondVisibility('Container(50).HasFocus(5)') or (xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(102)'))
leftmenubutton110 = xbmc.getCondVisibility('Control.HasFocus(110)')
controlhasfocus32 = xbmc.getCondVisibility('Control.HasFocus(32)') #UPDATE LIVE TV CHANNELS
refreshbutton = xbmc.getCondVisibility('Control.HasFocus(9092)')
settinglevelbutton = xbmc.getCondVisibility('Control.HasFocus(20)')
'''---------------------------'''

'''------------------------------
---CONTAINER---------------------
------------------------------'''
container120numitems = xbmc.getInfoLabel('Container(120).NumItems') #DialogSubtitles
containernumitems = xbmc.getInfoLabel('Container.NumItems')
viewmode = xbmc.getInfoLabel('Container.Viewmode')
containerviewmode = xbmc.getInfoLabel('Container.Viewmode')
containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
containerfoldername = xbmc.getInfoLabel('Container.FolderName')
container50position = xbmc.getInfoLabel('Container(50).Position')
container57position = xbmc.getInfoLabel('Container(57).Position')
if homeW: container9000pos = xbmc.getInfoLabel('Container(9000).Position')
container50listitemlabel = xbmc.getInfoLabel('Container(50).ListItem.Label') #Actors #UNUSED!

'''------------------------------
---OPENELEC----------------------
------------------------------'''
openelec1 = xbmc.getInfoLabel('$ADDON[service.openelec.settings 32002]') #system
openelec2 = xbmc.getInfoLabel('$ADDON[service.openelec.settings 32000]') #network
openelec3 = xbmc.getInfoLabel('$ADDON[service.openelec.settings 32100]') #connections
openelec4 = xbmc.getInfoLabel('$ADDON[service.openelec.settings 32001]') #services
openelec5 = xbmc.getInfoLabel('$ADDON[service.openelec.settings 32331]') #bluetooth
openelec6 = xbmc.getInfoLabel('$ADDON[service.openelec.settings 32196]') #about
'''---------------------------'''

'''------------------------------
---DATES-----------------------
------------------------------'''
import datetime as dt
import time

datenow = dt.date.today()
datenowS = str(datenow)
'''---------------------------'''
dateafter = datenow + dt.timedelta(days=7)
dateafterS = str(dateafter)
'''---------------------------'''
yearnow = datenow.strftime("%Y")
yearnowS = str(yearnow)
'''---------------------------'''
daynow = datenow.strftime("%a")
daynowS = str(daynow)
timenow = dt.datetime.now()
timenowS = str(timenow)
timenow2 = timenow.strftime("%H:%M")
timenow2S = str(timenow2)
timenow2N = int(timenow2S.replace(":","",1)) #GAL CHECK # PAREMTERS WHY?
timenow3 = timenow.strftime("%H")
timenow3S = str(timenow3)
timenow3N = int(timenow3S)
timenow4 = timenow.strftime("%S")
timenow4S = str(timenow4)
timenow5 = timenow.strftime("%a %b %d %X %Y") #date and time representation
'''---------------------------'''
if timenow3N > 03 and timenow3N < 12: timezone = "A"
elif timenow3N > 11 and timenow3N < 20: timezone = "B"
elif timenow3N > 19 or timenow3N < 04: timezone = "C"
else: timezone = ""
#if admin: print printfirst + datenowS + space + daynowS + space + timenow2S + space + "timezone: " + timezone
'''---------------------------'''
if (daynowS == "Sat" and timenow2N < 2000) or (daynowS == "Fri" and timenow2N > 1900): yomshabat = "true"
else: yomshabat = "false"