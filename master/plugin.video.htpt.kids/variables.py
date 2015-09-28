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
---script.htpt.htpt.kids---------
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonFanart = os.path.join(addonPath, "fanart.jpg")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

addonName2 = addonString_servicehtpt(9).encode('utf-8')
printfirst = addonName + ": !@# "
'''---------------------------'''

#libDir = os.path.join(xbmc.translatePath("special://home/addons/"), addonID, 'resources', 'lib')
#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)
addonMediaPath = os.path.join(addonPath, 'resources', 'media', '')
General_AutoView = getsetting('General_AutoView')
General_AutoView_A = getsetting('General_AutoView_A')
General_AutoView_B = getsetting('General_AutoView_B')
General_AutoView_C = getsetting('General_AutoView_C')
General_TrustedOnly = getsetting('General_TrustedOnly')
General_TVModeDialog = getsetting('General_TVModeDialog')
General_TVModeShuffle = getsetting('General_TVModeShuffle')
'''---------------------------'''
Addon_ShowLog = getsetting('Addon_ShowLog')
Addon_ShowLog2 = getsetting('Addon_ShowLog2')
Addon_Update = getsetting('Addon_Update')
Addon_UpdateDate = getsetting('Addon_UpdateDate')
Addon_UpdateLog = getsetting('Addon_UpdateLog')
Addon_Version = getsetting('Addon_Version')
'''---------------------------'''
Fanart_Enable = getsetting('Fanart_Enable').lower
Fanart_EnableCustom = getsetting('Fanart_EnableCustom').lower
Fanart_Custom101 = getsetting('Fanart_Custom101')
Fanart_Custom102 = getsetting('Fanart_Custom102')
Fanart_Custom103 = getsetting('Fanart_Custom103')
Fanart_Custom104 = getsetting('Fanart_Custom104')
Fanart_Custom105 = getsetting('Fanart_Custom105')
Fanart_Custom106 = getsetting('Fanart_Custom106')
Fanart_Custom107 = getsetting('Fanart_Custom107')
Fanart_Custom108 = getsetting('Fanart_Custom108')
Fanart_Custom109 = getsetting('Fanart_Custom109')
Fanart_Custom110 = getsetting('Fanart_Custom110')
'''---------------------------'''

'''------------------------------
---ON/OFF------------------------
------------------------------'''
OFF_1 = getsetting('OFF_1')
OFF_2 = getsetting('OFF_2')
OFF_3 = getsetting('OFF_3')
OFF_4 = getsetting('OFF_4')
OFF_5 = getsetting('OFF_5')
OFF_6 = getsetting('OFF_6')
OFF_7 = getsetting('OFF_7')
OFF_8 = getsetting('OFF_8')
OFF_9 = getsetting('OFF_9')
OFF_10 = getsetting('OFF_10')
OFF_11 = getsetting('OFF_11')
OFF_12 = getsetting('OFF_12')
OFF_13 = getsetting('OFF_13')
OFF_14 = getsetting('OFF_14')
OFF_15 = getsetting('OFF_15')
OFF_16 = getsetting('OFF_16')
OFF_17 = getsetting('OFF_17')
OFF_18 = getsetting('OFF_18')
OFF_19 = getsetting('OFF_19')
OFF_20 = getsetting('OFF_20')
OFF_21 = getsetting('OFF_21')
'''---------------------------'''