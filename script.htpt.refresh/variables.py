#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import datetime
import sys
'''------------------------------
---script.htpt.refresh-------------
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonString            = xbmcaddon.Addon().getLocalizedString

General_TimeZone = getsetting('General_TimeZone')
General_Refresh = getsetting('General_Refresh')
General_StartWindow = getsetting('General_StartWindow')
General_Connected = getsetting('General_Connected')
General_ConnectionScore = getsetting('General_ConnectionScore')
try: General_ConnectionScoreN = int(General_ConnectionScore)
except: pass
General_ScriptON = getsetting('General_ScriptON')
General_CountWait = getsetting('General_CountWait')
General_CustomVAR = getsetting('General_CustomVAR')
''''''
Current_Dialog = getsetting('Current_Dialog')
Current_M_T = getsetting('Current_M_T')
Current_Watched = getsetting('Current_Watched')
Current_Name = getsetting('Current_Name')
Current_Source = getsetting('Current_Source')
Current_RefreshPoint = getsetting('Current_RefreshPoint')
Current_Subtitle = getsetting('Current_Subtitle')
Current_Subtitle1 = getsetting('Current_Subtitle1')
Current_Subtitle2 = getsetting('Current_Subtitle2')
Current_Subtitle3 = getsetting('Current_Subtitle3')
Current_Subtitle4 = getsetting('Current_Subtitle4')
Current_Subtitle5 = getsetting('Current_Subtitle5')
Current_Subtitle6 = getsetting('Current_Subtitle6')
Current_Subtitle7 = getsetting('Current_Subtitle7')
Current_Subtitle8 = getsetting('Current_Subtitle8')
Current_Subtitle9 = getsetting('Current_Subtitle9')
Current_Subtitle10 = getsetting('Current_Subtitle10')
''''''
LastMovie_Name = getsetting('LastMovie_Name')
LastMovie_Source = getsetting('LastMovie_Source')
''''''
LastTV_Name = getsetting('LastTV_Name')
LastTV_Source = getsetting('LastTV_Source')
''''''
AutoPlay_Pause = getsetting('AutoPlay_Pause')
AutoPlay_SD = getsetting('AutoPlay_SD')
AutoPlay_HD = getsetting('AutoPlay_HD')
''''''
SE_ColorRed = getsetting('SE_ColorRed')
SE_ColorRed2 = getsetting('SE_ColorRed2')
SE_ColorRed3 = getsetting('SE_ColorRed3')
SE_ColorGreen = getsetting('SE_ColorGreen')
SE_ColorGreen2 = getsetting('SE_ColorGreen2')
SE_ColorGreen3 = getsetting('SE_ColorGreen3')
SE_ColorPurple = getsetting('SE_ColorPurple')
SE_ColorPurple2 = getsetting('SE_ColorPurple2')
SE_ColorPurple3 = getsetting('SE_ColorPurple3')

'''------------------------------
---DEFAULT-----------------------
------------------------------'''
printfirst = addonName + ": !@# "
space = " "
space2 = ": "
space3 = "_"
dialog = xbmcgui.Dialog()
systemplatformwindows = xbmc.getCondVisibility('system.platform.windows')
systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')

'''------------------------------
---Skin.HasSetting---------------
------------------------------'''
admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
autoplaysd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlaySD)')
autoplaypause = xbmc.getInfoLabel('Skin.HasSetting(AutoPlay_Pause)')
autoplay_hd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlay_HD)')
autoplay_sd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlay_SD)')
validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')

'''------------------------------
---ACCOUNTS----------------------
------------------------------'''
Account1_Active = xbmc.getInfoLabel('Skin.HasSetting(Account1_Active)')
Account1_Period = xbmc.getInfoLabel('Skin.String(Account1_Period)')
Account1_EndDate = xbmc.getInfoLabel('Skin.String(Account1_EndDate)')
Account2_Active = xbmc.getInfoLabel('Skin.HasSetting(Account2_Active)')
Account2_Period = xbmc.getInfoLabel('Skin.String(Account2_Period)')
Account2_EndDate = xbmc.getInfoLabel('Skin.String(Account2_EndDate)')

'''------------------------------
---System.-----------------------
------------------------------'''
systeminternetstate = xbmc.getInfoLabel('System.InternetState')
systemuptime = xbmc.getInfoLabel('System.Uptime')
systemcputemperature = xbmc.getInfoLabel('System.CPUTemperature')

'''------------------------------
---DATES-----------------------
------------------------------'''	
datenow = datetime.date.today()
datenowS = str(datenow)
yearnow = datenow.strftime("%Y")
yearnowS = str(yearnow)
daynow = datenow.strftime("%a")
daynowS = str(daynow)
timenow = datetime.datetime.now()
timenow2 = timenow.strftime("%H:%M")
timenow3 = timenow.strftime("%H")
timenow2S = str(timenow2)
timenow3S = str(timenow3)
timenow3N = int(timenow3S)
#timenow = datenow.strftime("%I:%M:%S %p")
if timenow3N > 03 and timenow3N < 12: timezone = "A"
elif timenow3N > 11 and timenow3N < 20: timezone = "B"
elif timenow3N > 19 or timenow3N < 04: timezone = "C"
if admin: print printfirst + datenowS + space + daynowS + space + timenow2S + space + "timezone: " + timezone

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
skinsettingsW = xbmc.getCondVisibility('Window.IsVisible(SkinSettings.xml)')
dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
custom1170W = xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)')
custom1115W = xbmc.getCondVisibility('Window.IsVisible(Custom1115.xml)')

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
listitemtvshowtitlestr = xbmc.getInfoLabel('Skin.String(ListItemTVShowTitle)')
listitemseason = xbmc.getInfoLabel('ListItem.Season')
listitemepisode = xbmc.getInfoLabel('ListItem.Episode')
listitemgenrestr = xbmc.getInfoLabel('Skin.String(ListItemGenre)')
listitemduration = xbmc.getInfoLabel('Skin.String(ListItemDuration)')
listitemratingstr = xbmc.getInfoLabel('Skin.String(ListItemRating)')
listitemyearstr = xbmc.getInfoLabel('Skin.String(ListItemYear)')
customvar = xbmc.getInfoLabel('Skin.String(General_CustomVAR)')
'''------------------------------
---LISTITEM-------------
------------------------------'''
listitempath = xbmc.getInfoLabel('ListItem.Path')
listitemyear = xbmc.getInfoLabel('ListItem.Year)')


'''------------------------------
---CUSTOM-------------
------------------------------'''

dialogselectsources = xbmc.getInfoLabel('Skin.String(DialogSelectSources)')
dialogselectsources2 = xbmc.getInfoLabel('Skin.String(DialogSelectSources2)')
dialogselectsources3 = xbmc.getInfoLabel('Skin.String(DialogSelectSources3)')
dialogselectsources5 = xbmc.getInfoLabel('Skin.String(DialogSelectSources5)')

cancelstr = xbmc.getInfoLabel('$LOCALIZE[222]')

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
hasinternet = systeminternetstate != "" and networkipaddress != "" and (connected or systemplatformwindows)
istv = (xbmc.getInfoLabel('ListItem.TVShowTitle') != "" and xbmc.getInfoLabel('ListItem.Season') != "" and xbmc.getInfoLabel('ListItem.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
istvS = str(istv)
istv2 = (xbmc.getInfoLabel('VideoPlayer.TVShowTitle') != "" and xbmc.getInfoLabel('VideoPlayer.Season') != "" and xbmc.getInfoLabel('VideoPlayer.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
ismovie2 = xbmc.getInfoLabel('VideoPlayer.Content') == "movies" or ((xbmc.getInfoLabel('VideoPlayer.Year') != "" or xbmc.getInfoLabel('VideoPlayer.Country') != "") and xbmc.getInfoLabel('VideoPlayer.Tagline') != "") and not istv2
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
refreshbutton = xbmc.getCondVisibility('Control.HasFocus(9092)')
cancelbutton = xbmc.getCondVisibility('Control.HasFocus(10)') and xbmc.getCondVisibility('Window.IsActive(DialogProgress.xml)')
autoplaypausebutton = (xbmc.getCondVisibility('Window.IsVisible(Home.xml)') and xbmc.getCondVisibility('Control.HasFocus(9093)')) or (xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)') and xbmc.getCondVisibility('Control.HasFocus(111)'))
controlisvisible311 = xbmc.getCondVisibility('Control.IsVisible(311)') or xbmc.getCondVisibility('Control.HasFocus(340)')
controlisvisible311S = str(controlisvisible311)
controlisvisible312 = xbmc.getCondVisibility('Control.IsVisible(312)') or xbmc.getCondVisibility('Control.HasFocus(341)')
controlisvisible312S = str(controlisvisible312)
controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name

'''------------------------------
---$LOCALIZE--------------------
------------------------------'''
truestr = xbmc.getInfoLabel('$LOCALIZE[20122]')
falsestr = xbmc.getInfoLabel('$LOCALIZE[20424]')
'''------------------------------
---ID----------------------------
------------------------------'''
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

idtrial = 'htptuser'
idpstr = xbmc.getInfoLabel('$LOCALIZE[79246]')
idp2str = xbmc.getInfoLabel('$LOCALIZE[79247]')