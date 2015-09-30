'''------------------------------
---shared_variables--------------
------------------------------'''
import xbmc, xbmcgui, xbmcaddon, sys, os
addon = 'service.htpt'
if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	printpoint = "" ; count = 0
	dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
	dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
	if not dialogyesnoW and not dialogprogressW:
		printpoint = printpoint + "1"
		xbmc.executebuiltin('Notification(Required addon is missing!,'+addon+',4000)')
		xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addon +'),returned') ; xbmc.sleep(2000)
		'''---------------------------'''
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		while count < 10 and (not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or dialogbusyW) and not xbmc.abortRequested:
			if count == 0: printpoint = printpoint + "2"
			count += 1
			if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('Dialog.Close(busydialog)')
			xbmc.sleep(500)
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
			xbmc.sleep(500)
			'''---------------------------'''
		if count < 10:
			printpoint = printpoint + "7"
			xbmc.executebuiltin('Action(Back)') ; xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(1000)
			xbmc.executebuiltin('Notification(Required addon installed!,Try again!,4000)')
			'''---------------------------'''
		else: printpoint = printpoint + "9"
		
	else: printpoint = printpoint + "8"
	
	print 'service.htpt_install_LV' + printpoint + " count: " + str(count)
	sys.exit(1)
else:
	servicehtptPath          = xbmcaddon.Addon('service.htpt').getAddonInfo("path")
	sharedlibDir = os.path.join(servicehtptPath, 'resources', 'lib', 'shared')
	sys.path.insert(0, sharedlibDir)
	from shared_variables import *
	'''---------------------------'''

'''------------------------------
---service.htpt------------------
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonFanart = os.path.join(addonPath, "fanart.jpg")
addonFanart2 = os.path.join(addonPath, "resources", "media", "fanart.jpg")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

printfirst = addonName + ": !@# "
'''---------------------------'''
General_PageSize = getsetting('General_PageSize')
General_TVModeDialog = getsetting('General_TVModeDialog')
General_TVModeShuffle = getsetting('General_TVModeShuffle')
General_AutoView = getsetting('General_AutoView')
'''---------------------------'''
Addon_ShowLog = getsetting('Addon_ShowLog')
Addon_ShowLog2 = getsetting('Addon_ShowLog2')
Addon_Update = getsetting('Addon_Update')
Addon_UpdateDate = getsetting('Addon_UpdateDate')
Addon_UpdateLog = getsetting('Addon_UpdateLog')
Addon_Version = getsetting('Addon_Version')
'''---------------------------'''
Fanart_Enable = getsetting('Fanart_Enable')
Fanart_EnableCustom = getsetting('Fanart_EnableCustom')
'''---------------------------'''
YOUTUBE_CHANNEL_ID = "GoProCamera"