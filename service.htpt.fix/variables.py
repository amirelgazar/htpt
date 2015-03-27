#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import datetime
import sys

'''------------------------------
---service.htpt.fix--------------
------------------------------'''
getsetting         = xbmcaddon.Addon('service.htpt.fix').getSetting
setsetting         = xbmcaddon.Addon('service.htpt.fix').setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString

'''---------------------------'''
Addon_Update = getsetting('Addon_Update')
Addon_UpdateDate = getsetting('Addon_UpdateDate')
Addon_UpdateLog = getsetting('Addon_UpdateLog')
Addon_Version = getsetting('Addon_Version')
Addon_ServiceON = getsetting('Addon_ServiceON')
'''---------------------------'''
Fix_1 = getsetting('Fix_1')
Fix_2 = getsetting('Fix_2')
Fix_3 = getsetting('Fix_3')
Fix_4 = getsetting('Fix_4')
Fix_5 = getsetting('Fix_5')
'''---------------------------'''
Fix_10 = getsetting('Fix_10')
Fix_11 = getsetting('Fix_11')
Fix_12 = getsetting('Fix_12')
Fix_13 = getsetting('Fix_13')
Fix_14 = getsetting('Fix_14')
'''---------------------------'''
Fix_100 = getsetting('Fix_100')
Fix_101 = getsetting('Fix_101')
Fix_102 = getsetting('Fix_102')
Fix_103 = getsetting('Fix_103')
Fix_104 = getsetting('Fix_104')
Fix_L = [Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104]
Fix_LastDate = getsetting('Fix_LastDate')
Fix_Done = getsetting('Fix_Done')
'''---------------------------'''
Red_Alert = getsetting('Red_Alert')
Red_LV1 = getsetting('Red_LV1')
Red_LV2 = getsetting('Red_LV2')
Red_LV3 = getsetting('Red_LV3')
Red_LV4 = getsetting('Red_LV4')
Red_LV5 = getsetting('Red_LV5')
Red_L = [Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5]
Red_LastDate = getsetting('Red_LastDate')
Red_Done = getsetting('Red_Done')
'''---------------------------'''



'''------------------------------
---DEFAULT-----------------------
------------------------------'''
printfirst = addonName + ": !@# "
space = " "
space2 = ": "
space3 = "_"
space4 = " / "
dialog = xbmcgui.Dialog()
systemplatformwindows = xbmc.getCondVisibility('system.platform.windows')
systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
systemidle7 = xbmc.getCondVisibility('System.IdleTime(7)')
systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
systemidle120 = xbmc.getCondVisibility('System.IdleTime(120)')
systemidle300 = xbmc.getCondVisibility('System.IdleTime(300)')
systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
systemcurrentwindow = xbmc.getInfoLabel('System.CurrentWindow')

'''------------------------------
---systemhasaddon----------------
------------------------------'''
systemhasaddon_metadatauniversal = xbmc.getCondVisibility('System.HasAddon(metadata.universal)')
systemhasaddon_metadatathemoviedb = xbmc.getCondVisibility('System.HasAddon(metadata.themoviedb.org)')
systemhasaddon_scripthtptdebug = xbmc.getCondVisibility('System.HasAddon(script.htpt.debug)')
'''---------------------------'''

'''------------------------------
---Skin.HasSetting---------------
------------------------------'''
admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
autoplaysd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlaySD)')
autoplaypause = xbmc.getInfoLabel('Skin.HasSetting(AutoPlay_Pause)')
validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')

'''------------------------------
---System.-----------------------
------------------------------'''
systeminternetstate = xbmc.getInfoLabel('System.InternetState')
systemuptime = xbmc.getInfoLabel('System.Uptime')
systemcputemperature = xbmc.getInfoLabel('System.CPUTemperature')
screenresolution = xbmc.getInfoLabel('System.ScreenResolution')
dhcpaddress = xbmc.getInfoLabel('Network.DHCPAddress')
systemuptime2 = xbmc.getInfoLabel('System.Uptime') + " / " + xbmc.getInfoLabel('System.TotalUptime') 
freespace2 = xbmc.getInfoLabel('System.TotalSpace') + " / " + xbmc.getInfoLabel('System.FreeSpacePercent')
if xbmc.getCondVisibility('System.HasAddon(service.htpt)'): htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)') + "+"
elif xbmc.getCondVisibility('!System.HasAddon(service.htpt)'): htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)') + "-"
buildversion = xbmc.getInfoLabel('System.BuildVersion')
htptdebugversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.debug)')
htptserviceversion = xbmc.getInfoLabel('system.AddonVersion(service.htpt)')
htpthelpversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.help)')
htpthomebuttonsversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.homebuttons)')
htptremoteversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.remote)')
htptrefreshversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.refresh)')
htptfixversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.fix)')


'''------------------------------
---DATES-----------------------
------------------------------'''	
datenow = datetime.date.today()
datenowS = str(datenow)

dateafter = datenow + datetime.timedelta(days=7)
dateafterS = str(dateafter)

daynow = datenow.strftime("%a")
daynowS = str(daynow)
timenow = datetime.datetime.now()
timenowS = timenow.strftime("%H:%M")

'''------------------------------
---CONTAINER---------------------
------------------------------'''
containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
container120numitems = xbmc.getInfoLabel('Container(120).NumItems') #DialogSubtitles

'''------------------------------
---Window.-----------------------
------------------------------'''
homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
home_pW = xbmc.getCondVisibility('Window.Previous(0)')
home_aW = xbmc.getCondVisibility('Window.IsActive(0)')
mypicsW = xbmc.getCondVisibility('Window.IsVisible(mypicsW.xml)')
mymusicnavW = xbmc.getCondVisibility('Window.IsVisible(MyMusicNav.xml)')
myvideonavW = xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)')
startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
startup_aW = xbmc.getCondVisibility('Window.IsActive(Startup.xml)')
startup_pW = xbmc.getCondVisibility('Window.Previous(Startup.xml)')
videofullscreenW = xbmc.getCondVisibility('Window.IsVisible(VideoFullScreen.xml)')
dialogvideoinfoW = xbmc.getCondVisibility('Window.IsVisible(DialogVideoInfo.xml)')
dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
custom1170W = xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)')
custom1191W = xbmc.getInfoLabel('Skin.String(custom1191)')
settingsW = xbmc.getCondVisibility('Window.IsVisible(Settings.xml)')
myprogramsW = xbmc.getCondVisibility('Window.IsVisible(MyPrograms.xml)')
filemanagerW = xbmc.getCondVisibility('Window.IsVisible(FileManager.xml)')
loginscreenW = xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)')
loginscreen_aW = xbmc.getCondVisibility('Window.IsActive(LoginScreen.xml)')
myweatherW = xbmc.getCondVisibility('Window.IsVisible(MyWeather.xml)')
dialogfavouritesW = xbmc.getCondVisibility('Window.IsVisible(DialogFavourites.xml)')
dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
dialogcontextmenuW = xbmc.getCondVisibility('Window.IsVisible(DialogContextMenu.xml)')
skinsettingsW = xbmc.getCondVisibility('Window.IsVisible(SkinSettings.xml)')
dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
custom1170W = xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)')
custom1115W = xbmc.getCondVisibility('Window.IsVisible(Custom1115.xml)')
mainwindow = xbmc.getCondVisibility('Window.IsVisible(mainWindow.xml)')

'''------------------------------
---Network.----------------------
------------------------------'''
networkgatewayaddress = xbmc.getInfoLabel('Network.GatewayAddress')
networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
'''------------------------------
---VIDEO-------------------------
------------------------------'''
playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
playerpaused = xbmc.getCondVisibility('Player.Paused')
videoplayerhassubtitles = xbmc.getCondVisibility('VideoPlayer.HasSubtitles')
playercache = xbmc.getInfoLabel('Player.CacheLevel')
playertitle = xbmc.getInfoLabel('Player.Title')
'''---------------------------'''	
playertime = xbmc.getInfoLabel("Player.Time(hh)") + xbmc.getInfoLabel("Player.Time(mm)") + xbmc.getInfoLabel("Player.Time(ss)")
playertimeremaining = xbmc.getInfoLabel("Player.TimeRemaining(hh)") + xbmc.getInfoLabel("Player.TimeRemaining(mm)") + xbmc.getInfoLabel("Player.TimeRemaining(ss)")
playerduration = xbmc.getInfoLabel("Player.Duration(hh)") + xbmc.getInfoLabel("Player.Duration(mm)") + xbmc.getInfoLabel("Player.Duration(ss)")

'''---------------------------'''
playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
playlistlengthN = int(playlistlength)
playlistposition = xbmc.getInfoLabel('Playlist.Position(video)')
playlistpositionN = int(playlistposition)
'''---------------------------'''
videoplayertitle = xbmc.getInfoLabel('VideoPlayer.Title')
videoplayerseason = xbmc.getInfoLabel('VideoPlayer.Season')
videoplayertvshowtitle = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
videoplayeryear = xbmc.getInfoLabel('VideoPlayer.Year')
videoplayertagline = xbmc.getInfoLabel('VideoPlayer.Tagline')
videoplayercountry = xbmc.getInfoLabel('VideoPlayer.Country')
videoplayerseason = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
#videoplayerseason = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
#videoplayerseason = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
#videoplayerseason = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
videoplayercontentMOVIE = xbmc.getCondVisibility('VideoPlayer.Content(movies)')
videoplayercontentTV = xbmc.getCondVisibility('VideoPlayer.Content(tvshows)')
videoplayercontentSEASON = xbmc.getCondVisibility('VideoPlayer.Content(seasons)')
videoplayercontentEPISODE = xbmc.getCondVisibility('VideoPlayer.Content(episodes)')

'''------------------------------
---SKIN STRINGS-------------
------------------------------'''
listitemtvshowtitle = xbmc.getInfoLabel('Skin.String(ListItemTVShowTitle)')
listitemseason = xbmc.getInfoLabel('ListItem.Season')
listitemepisode = xbmc.getInfoLabel('ListItem.Episode')
listitemgenre = xbmc.getInfoLabel('Skin.String(ListItemGenre)')
listitemduration = xbmc.getInfoLabel('Skin.String(ListItemDuration)')
listitemrating = xbmc.getInfoLabel('Skin.String(ListItemRating)')
listitemyear = xbmc.getInfoLabel('Skin.String(ListItemYear)')

'''------------------------------
---LISTITEM-------------
------------------------------'''
listitempath = xbmc.getInfoLabel('ListItem.Path')



'''------------------------------
---CUSTOM-------------
------------------------------'''

dialogselectsources = xbmc.getInfoLabel('Skin.String(DialogSelectSources)')
dialogselectsources2 = xbmc.getInfoLabel('Skin.String(DialogSelectSources2)')
dialogselectsources3 = xbmc.getInfoLabel('Skin.String(DialogSelectSources3)')
dialogselectsources5 = xbmc.getInfoLabel('Skin.String(DialogSelectSources5)')

dialogsubtitles2 = xbmc.getInfoLabel('Skin.String(DialogSubtitles2)')
dialogsubtitlesna1 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA1)')
dialogsubtitlesna2 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA2)')
dialogsubtitlesna3 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA3)')
dialogsubtitlesna4 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA4)')
dialogsubtitlesna5 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA5)')
dialogsubtitlesna6 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA6)')
dialogsubtitlesna7 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA7)')
dialogsubtitlesna8 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA8)')
dialogsubtitlesna9 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA9)')
dialogsubtitlesna10 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA10)')


'''------------------------------
---MIXED-------------------------
------------------------------'''
hasinternet = systeminternetstate != "" and networkipaddress != "" and not "169.254." in networkipaddress and (connected or systemplatformwindows)
mac = xbmc.getInfoLabel('Network.MacAddress') + " ( " + xbmc.getInfoLabel('Skin.String(MAC1)') + " / " + xbmc.getInfoLabel('Skin.String(MAC2)') + " )"
istv = (xbmc.getInfoLabel('ListItem.TVShowTitle') != "" and xbmc.getInfoLabel('ListItem.Season') != "" and xbmc.getInfoLabel('ListItem.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
istvS = str(istv)
ismovie = (xbmc.getInfoLabel('ListItem.Year') != "" or xbmc.getInfoLabel('ListItem.Country') != "" or xbmc.getInfoLabel('ListItem.Tagline') != "") and not istv
ismovieS = str(ismovie)
istv4 = " S" in dialogselectsources3 and " E" in dialogselectsources3
istv4S = str(istv4)
ismovie4 = " (" in dialogselectsources3 and ")" in dialogselectsources3 and not istv4
ismovie4S = str(ismovie4)
istvmoviep = (videoplayertitle in dialogselectsources3 or videoplayertitle in dialogselectsources5)
isgenesis = "videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath or "plugin://plugin.video.genesis/" in containerfolderpath
'''------------------------------
---CONTROL-----------------------
------------------------------'''
cancelbutton = xbmc.getCondVisibility('Control.HasFocus(10)') and xbmc.getCondVisibility('Window.IsActive(DialogProgress.xml)')
autoplaypausebutton = (xbmc.getCondVisibility('Window.IsVisible(Home.xml)') and xbmc.getCondVisibility('Control.HasFocus(9093)')) or (xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)') and xbmc.getCondVisibility('Control.HasFocus(111)'))
debugbutton = xbmc.getCondVisibility('Container(50).HasFocus(5)') or (xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(102)'))
controlisvisible311 = xbmc.getCondVisibility('Control.IsVisible(311)') or xbmc.getCondVisibility('Control.HasFocus(340)')
controlisvisible311S = str(controlisvisible311)
controlisvisible312 = xbmc.getCondVisibility('Control.IsVisible(312)') or xbmc.getCondVisibility('Control.HasFocus(341)')
controlisvisible312S = str(controlisvisible312)
controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
controlhasfocus20 = xbmc.getCondVisibility('Control.HasFocus(20)')

	
'''------------------------------
---$LOCALIZE--------------------
------------------------------'''
truestr = xbmc.getInfoLabel('$LOCALIZE[20122]')
trialstr = xbmc.getInfoLabel('$LOCALIZE[70001]')
trial2str = xbmc.getInfoLabel('$LOCALIZE[70002]')
verrorstr = xbmc.getInfoLabel('$VAR[VERROR]')
id6v1str = xbmc.getInfoLabel('$LOCALIZE[70014]')
id6v2str = xbmc.getInfoLabel('$LOCALIZE[70015]')
id6v3str = xbmc.getInfoLabel('$LOCALIZE[70016]')
str20442 = xbmc.getInfoLabel('$LOCALIZE[20442]') #Change content
str20333 = xbmc.getInfoLabel('$LOCALIZE[20333]') #Set content
str342 = xbmc.getInfoLabel('$LOCALIZE[342]') #Movies
str36901 = xbmc.getInfoLabel('$LOCALIZE[36901]') #movies
str231 = xbmc.getInfoLabel('$LOCALIZE[231]') #None
str16018 = xbmc.getInfoLabel('$LOCALIZE[16018]') #None
str36909 = xbmc.getInfoLabel('$LOCALIZE[36909]') #musicvideos
str20389 = xbmc.getInfoLabel('$LOCALIZE[20389]') #Music videos
str36903 = xbmc.getInfoLabel('$LOCALIZE[36903]') #TV shows
str20343 = xbmc.getInfoLabel('$LOCALIZE[20343]') #TV shows
str186 = xbmc.getInfoLabel('$LOCALIZE[186]') #OK
str12321 = xbmc.getInfoLabel('$LOCALIZE[186]') #Ok
str106 = xbmc.getInfoLabel('$LOCALIZE[106]') #No
str107 = xbmc.getInfoLabel('$LOCALIZE[107]') #Yes
str222 = xbmc.getInfoLabel('$LOCALIZE[222]') #Cancel
str20329 = xbmc.getInfoLabel('$LOCALIZE[20329]') #Movies are in separate folders that match the movie title
str20346 = xbmc.getInfoLabel('$LOCALIZE[20346]') #Scan recursively


'''------------------------------
---LIST--------------------------
------------------------------'''
#ChangeContentL = ["(" + str20442 + ")","(" + str342 + ")","(" + str36901 + ")","(" + str231 + ")","(" + str16018 + ")","(" + str36909 + ")","(" + str20389 + ")","(" + str36903 + ")","(" + str20343 + ")"] #Change content
ChangeContentL = [str20442,str342,str36901,str231,str16018,str36909,str20389,str36903,str20343] #Change content



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
id60str = xbmc.getInfoLabel('Skin.String(ID60)')
''''''
idnamestr = xbmc.getInfoLabel('$LOCALIZE[1014]')
id2namestr = xbmc.getInfoLabel('$LOCALIZE[70010]')
id3namestr = xbmc.getInfoLabel('$LOCALIZE[70011]')
id4namestr = xbmc.getInfoLabel('$LOCALIZE[19115]')
id5namestr = xbmc.getInfoLabel('$LOCALIZE[75006]')
id6namestr = xbmc.getInfoLabel('$LOCALIZE[70012]')
id60namestr = xbmc.getInfoLabel('$LOCALIZE[70012]')
id7namestr = 'Question'
id8namestr = xbmc.getInfoLabel('$LOCALIZE[70013]')
id9namestr = 'CODE RED'
id10namestr = xbmc.getInfoLabel('$LOCALIZE[79031]')
id11namestr = 'MAC1 (LAN)'
id12namestr = 'MAC2 (WLAN)'
''''''
fixip = xbmc.getInfoLabel('Skin.String(fixip)')
trial = xbmc.getInfoLabel('Skin.HasSetting(Trial)')
trial2 = xbmc.getInfoLabel('Skin.HasSetting(Trial2)')
trialdate = xbmc.getInfoLabel('Skin.String(TrialDate)')
trialdate2 = xbmc.getInfoLabel('Skin.String(TrialDate2)')

idtrial = 'htptuser'
#idtrial = 'htptuser27'
idpstr = xbmc.getInfoLabel('$LOCALIZE[79246]')
#idp2str = xbmc.getInfoLabel('$LOCALIZE[79246]')
idp2str = xbmc.getInfoLabel('$LOCALIZE[79247]')
