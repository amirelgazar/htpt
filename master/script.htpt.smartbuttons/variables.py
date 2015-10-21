'''------------------------------
---shared_variables--------------
------------------------------'''
import xbmc, xbmcaddon, sys, os
addon = 'service.htpt'
if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	xbmc.executebuiltin('Notification(Required addon is missing!,'+addon+',4000)')
	xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addon +'),returned') ; xbmc.sleep(1000)
	sys.exit(1)
else:
	servicehtptPath          = xbmcaddon.Addon('service.htpt').getAddonInfo("path")
	sharedlibDir = os.path.join(servicehtptPath, 'resources', 'lib', 'shared')
	#sharedlibwikipediaDir = os.path.join(servicehtptPath, 'resources', 'lib', 'shared', 'wikipedia')
	sys.path.insert(0, sharedlibDir)
	#sys.path.insert(1, sharedlibwikipediaDir)
	
	from shared_variables import *
	'''---------------------------'''

'''------------------------------
---script.htpt.smartkeyboard-----
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

libDir = os.path.join(addonPath, 'resources', 'lib')
sys.path.insert(1, libDir)

printfirst = addonName + ": !@# "

Addon_ServiceON = getsetting('Addon_ServiceON')
General_ScriptON = getsetting('General_ScriptON')
Current_Input = getsetting('Current_Input')
Current_Input2 = getsetting('Current_Input2')
Current_Option = getsetting('Current_Option')
'''---------------------------'''
LibraryData_RemoteMoviesFiles = getsetting('LibraryData_RemoteMoviesFiles')
LibraryData_RemoteTvshowsFiles = getsetting('LibraryData_RemoteTvshowsFiles')
LibraryData_LocalMoviesFiles = getsetting('LibraryData_LocalMoviesFiles')
LibraryData_LocalTvshowsFiles = getsetting('LibraryData_LocalTvshowsFiles')
'''---------------------------'''
Skin_SaveDesign1 = getsetting('Skin_SaveDesign1')
Skin_SaveDesign2 = getsetting('Skin_SaveDesign2')
Skin_SaveDesign2 = getsetting('Skin_SaveDesign3')
'''---------------------------'''
Subtitle_Service = getsetting('Subtitle_Service')
Subtitle_Search = getsetting('Subtitle_Search')
'''---------------------------'''
copydir = os.path.join(addonPath, 'specials', 'scripts','copy', '')
copylibrarydir = os.path.join(copydir, 'library','')
copymoviesdir = os.path.join(copylibrarydir, 'movies','')
copytvshowsdir = os.path.join(copylibrarydir, 'tvshows','')

output = ""
printpoint = ""
'''------------------------------
---SMART-KEYBOARD----------------
------------------------------'''

'''---------------------------'''
smartkeyboardcopy = xbmc.getCondVisibility('Control.HasFocus(202)')
'''---------------------------'''
smartkeyboardPN = xbmc.getInfoLabel('Skin.String(smartkeyboardPN)')
smartkeyboardC1 = xbmc.getInfoLabel('Skin.String(smartkeyboardC1)')
smartkeyboardC2 = xbmc.getInfoLabel('Skin.String(smartkeyboardC2)')
smartkeyboardC3 = xbmc.getInfoLabel('Skin.String(smartkeyboardC3)')
smartkeyboardC4 = xbmc.getInfoLabel('Skin.String(smartkeyboardC4)')
smartkeyboardC5 = xbmc.getInfoLabel('Skin.String(smartkeyboardC5)')
'''---------------------------'''
smartkeyboardhistory = xbmc.getCondVisibility('Control.HasFocus(201)')
'''---------------------------'''
smartkeyboardHN = xbmc.getInfoLabel('Skin.String(smartkeyboardHN)')
smartkeyboardH0 = xbmc.getInfoLabel('Skin.String(smartkeyboardH0)')
smartkeyboardH1 = xbmc.getInfoLabel('Skin.String(smartkeyboardH1)')
smartkeyboardH2 = xbmc.getInfoLabel('Skin.String(smartkeyboardH2)')
smartkeyboardH3 = xbmc.getInfoLabel('Skin.String(smartkeyboardH3)')
smartkeyboardH4 = xbmc.getInfoLabel('Skin.String(smartkeyboardH4)')
smartkeyboardH5 = xbmc.getInfoLabel('Skin.String(smartkeyboardH5)')
smartkeyboardHL = [smartkeyboardH1, smartkeyboardH2, smartkeyboardH3, smartkeyboardH4, smartkeyboardH5]
'''---------------------------'''
smartkeyboardpaste = xbmc.getCondVisibility('Control.HasFocus(204)')
'''---------------------------'''


'''------------------------------
---OTHERS------------------------
------------------------------'''
includes_homecontent_file = os.path.join(skin_path, '1080i', 'Includes_HomeContent.xml') #DEFAULT
includes_homecontent2_file = os.path.join(skin_userdata_path, 'Includes_HomeContent.xml') #USERDATA
includes_homecontent3_file = file3 = os.path.join(skin_specials_userdata_path, 'Includes_HomeContent.xml') #BACKUP
includes_subcontent_file = os.path.join(skin_path, '1080i', 'Includes_SubContent.xml') #DEFAULT
includes_subcontent2_file = os.path.join(skin_userdata_path, 'Includes_SubContent.xml') #USERDATA
includes_subcontent3_file = file3 = os.path.join(skin_specials_userdata_path, 'Includes_SubContent.xml') #BACKUP

listitemlabel2 = xbmc.getInfoLabel('ListItem.Label2')

homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
customhomecustomizer2W = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomize2.xml)')
custom1138W = xbmc.getCondVisibility('Window.IsVisible(Custom1138.xml)')
custom1139W = xbmc.getCondVisibility('Window.IsVisible(Custom1139.xml)')
custom1175W = xbmc.getCondVisibility('Window.IsVisible(Custom1175.xml)')
custom1173W = xbmc.getCondVisibility('Window.IsVisible(Custom1173.xml)')

'''BASE ID'''
container50_buttonid_ = xbmc.getInfoLabel('Container(50).ListItemNoWrap(0).Property(id)')
container9000_buttonid_ = xbmc.getInfoLabel('Container(9000).ListItemNoWrap(0).Property(id)')
container9005_buttonid_ = xbmc.getInfoLabel('Container(9005).ListItemNoWrap(0).Property(id)')

'''DYNAMIC ID'''
container50_buttonid = xbmc.getInfoLabel('Container(50).ListItem(0).Label2')
container9000_buttonid = xbmc.getInfoLabel('Container(9000).ListItem(0).Label2')
container9005_buttonid = xbmc.getInfoLabel('Container(9005).ListItem(0).Label2')

#container50_previousbuttonid = xbmc.getInfoLabel('Container(50).ListItem(-1).Label2')
#container50_nextsbuttonid = xbmc.getInfoLabel('Container(50).ListItem(1).Label2')

container9005_previoususbbuttonid2 = xbmc.getInfoLabel('Container(9005).ListItem(-1).Label2')
container9005_nextsusbbuttonid2 = xbmc.getInfoLabel('Container(9005).ListItem(1).Label2')

property_temp = xbmc.getInfoLabel('Window(home).Property(TEMP)')
property_temp2 = xbmc.getInfoLabel('Window(home).Property(TEMP2)')
property_buttonid = xbmc.getInfoLabel('Window(home).Property(Button.ID)') #DYNAMIC
property_buttonid_ = xbmc.getInfoLabel('Window(home).Property(Button.ID_)') #BASE
property_buttonname = xbmc.getInfoLabel('Window(home).Property(Button.Name)')

property_subbuttonid = xbmc.getInfoLabel('Window(home).Property(SubButton.ID)')
property_subbuttonid_ = xbmc.getInfoLabel('Window(home).Property(SubButton.ID_)')
property_subbuttonname = xbmc.getInfoLabel('Window(home).Property(SubButton.Name)')
property_previoussubbuttonid = xbmc.getInfoLabel('Window(home).Property(Previous_SubButton.ID)')
property_previoussubbuttonid_ = xbmc.getInfoLabel('Window(home).Property(Previous_SubButton.ID_)')
property_nextsubbuttonid = xbmc.getInfoLabel('Window(home).Property(Next_SubButton.ID)')
property_nextsubbuttonid_ = xbmc.getInfoLabel('Window(home).Property(Next_SubButton.ID_)')

property_reloadskin = xbmc.getInfoLabel('Window(home).Property(ReloadSkin)')
reloadskin_check = xbmc.getInfoLabel('Control.GetLabel(700105)')

property_submenutip = xbmc.getInfoLabel('Window(home).Property(SubMenuTip)')
'''Prevent error'''
try: property_buttonid = property_buttonid.replace('"',"")
except: pass
try: property_buttonid_ = property_buttonid_.replace('"',"")
except: pass
try: property_temp = property_temp.replace('"',"")
except: pass
try: property_temp2 = property_temp2.replace('"',"")
except: pass

addon = 'script.openelec.rpi.config'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_scriptopenelecrpiconfig         = xbmcaddon.Addon(addon).getSetting
	setsetting_scriptopenelecrpiconfig         = xbmcaddon.Addon(addon).setSetting
	'''---------------------------'''
	scriptopenelecrpiconfigoverclock_preset = getsetting_scriptopenelecrpiconfig('overclock_preset')
	'''---------------------------'''
else:
	scriptopenelecrpiconfigoverclock_preset = ""
	'''---------------------------'''