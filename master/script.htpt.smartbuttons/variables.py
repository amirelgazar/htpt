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

#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)

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
livetvbutton = xbmc.getCondVisibility('Container(9000).HasFocus(355)')
livetvbutton2 = xbmc.getCondVisibility('Container(9000).HasFocus(3550)')

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