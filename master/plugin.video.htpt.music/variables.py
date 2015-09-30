# -*- coding: utf-8 -*-

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
---plugin.video.htpt.music-------
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

addonName2 = str2 + space + "HTPT"
printfirst = addonName + ": !@# "
'''---------------------------'''

#libDir = os.path.join(xbmc.translatePath("special://home/addons/"), addonID, 'resources', 'lib')
#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)

General_AutoView = getsetting('General_AutoView')
General_TVModeShuffle = getsetting('General_TVModeShuffle')
General_TVModeDialog = getsetting('General_TVModeDialog')
'''---------------------------'''
Addon_ShowLog = getsetting('Addon_ShowLog')
Addon_ShowLog2 = getsetting('Addon_ShowLog2')
Addon_Update = getsetting('Addon_Update')
Addon_UpdateDate = getsetting('Addon_UpdateDate')
Addon_UpdateLog = getsetting('Addon_UpdateLog')
Addon_Version = getsetting('Addon_Version')
'''---------------------------'''
#Addon_SavedButtons1 = getsetting('Addon_SavedButtons1')
#Addon_SavedButtons2 = getsetting('Addon_SavedButtons2')
#Addon_SavedButtons3 = getsetting('Addon_SavedButtons3')
'''---------------------------'''
#Addon_SavedButton1 = getsetting('Addon_SavedButtons1')
#Addon_SavedButton2 = getsetting('Addon_SavedButtons2')
#Addon_SavedButton3 = getsetting('Addon_SavedButtons3')
'''---------------------------'''
Fanart_Enable = getsetting('Fanart_Enable') #.lower
Fanart_EnableCustom = getsetting('Fanart_EnableCustom') #.lower
Fanart_Custom100 = getsetting('Fanart_Custom100')
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
Fanart_Custom111 = getsetting('Fanart_Custom111')
Fanart_Custom112 = getsetting('Fanart_Custom112')
Fanart_Custom113 = getsetting('Fanart_Custom113')
Fanart_Custom114 = getsetting('Fanart_Custom114')
Fanart_Custom115 = getsetting('Fanart_Custom115')
Fanart_Custom116 = getsetting('Fanart_Custom116')
Fanart_Custom117 = getsetting('Fanart_Custom117')
Fanart_Custom118 = getsetting('Fanart_Custom118')
Fanart_Custom119 = getsetting('Fanart_Custom119')
Fanart_Custom120 = getsetting('Fanart_Custom120')
Fanart_Custom121 = getsetting('Fanart_Custom121')
Fanart_Custom122 = getsetting('Fanart_Custom122')
Fanart_Custom123 = getsetting('Fanart_Custom123')
Fanart_Custom124 = getsetting('Fanart_Custom124')
Fanart_Custom125 = getsetting('Fanart_Custom125')
Fanart_Custom126 = getsetting('Fanart_Custom126')
Fanart_Custom127 = getsetting('Fanart_Custom127')
Fanart_Custom128 = getsetting('Fanart_Custom128')
Fanart_Custom129 = getsetting('Fanart_Custom129')
Fanart_Custom130 = getsetting('Fanart_Custom130')
'''---------------------------'''
Custom_Playlist1_ID = getsetting('Custom_Playlist1_ID')
Custom_Playlist1_Name = getsetting('Custom_Playlist1_Name')
Custom_Playlist1_Thumb = getsetting('Custom_Playlist1_Thumb')
Custom_Playlist1_Description = getsetting('Custom_Playlist1_Description')
Custom_Playlist1_Fanart = getsetting('Custom_Playlist1_Fanart')
Custom_Playlist2_ID = getsetting('Custom_Playlist2_ID')
Custom_Playlist2_Name = getsetting('Custom_Playlist2_Name')
Custom_Playlist2_Thumb = getsetting('Custom_Playlist2_Thumb')
Custom_Playlist2_Description = getsetting('Custom_Playlist2_Description')
Custom_Playlist2_Fanart = getsetting('Custom_Playlist2_Fanart')
Custom_Playlist3_ID = getsetting('Custom_Playlist3_ID')
Custom_Playlist3_Name = getsetting('Custom_Playlist3_Name')
Custom_Playlist3_Thumb = getsetting('Custom_Playlist3_Thumb')
Custom_Playlist3_Description = getsetting('Custom_Playlist3_Description')
Custom_Playlist3_Fanart = getsetting('Custom_Playlist3_Fanart')
Custom_Playlist4_ID = getsetting('Custom_Playlist4_ID')
Custom_Playlist4_Name = getsetting('Custom_Playlist4_Name')
Custom_Playlist4_Thumb = getsetting('Custom_Playlist4_Thumb')
Custom_Playlist4_Description = getsetting('Custom_Playlist4_Description')
Custom_Playlist4_Fanart = getsetting('Custom_Playlist4_Fanart')
Custom_Playlist5_ID = getsetting('Custom_Playlist5_ID')
Custom_Playlist5_Name = getsetting('Custom_Playlist5_Name')
Custom_Playlist5_Thumb = getsetting('Custom_Playlist5_Thumb')
Custom_Playlist5_Description = getsetting('Custom_Playlist5_Description')
Custom_Playlist5_Fanart = getsetting('Custom_Playlist5_Fanart')
Custom_Playlist6_ID = getsetting('Custom_Playlist6_ID')
Custom_Playlist6_Name = getsetting('Custom_Playlist6_Name')
Custom_Playlist6_Thumb = getsetting('Custom_Playlist6_Thumb')
Custom_Playlist6_Description = getsetting('Custom_Playlist6_Description')
Custom_Playlist6_Fanart = getsetting('Custom_Playlist6_Fanart')
Custom_Playlist7_ID = getsetting('Custom_Playlist7_ID')
Custom_Playlist7_Name = getsetting('Custom_Playlist7_Name')
Custom_Playlist7_Thumb = getsetting('Custom_Playlist7_Thumb')
Custom_Playlist7_Description = getsetting('Custom_Playlist7_Description')
Custom_Playlist7_Fanart = getsetting('Custom_Playlist7_Fanart')
Custom_Playlist8_ID = getsetting('Custom_Playlist8_ID')
Custom_Playlist8_Name = getsetting('Custom_Playlist8_Name')
Custom_Playlist8_Thumb = getsetting('Custom_Playlist8_Thumb')
Custom_Playlist8_Description = getsetting('Custom_Playlist8_Description')
Custom_Playlist8_Fanart = getsetting('Custom_Playlist8_Fanart')
Custom_Playlist9_ID = getsetting('Custom_Playlist9_ID')
Custom_Playlist9_Name = getsetting('Custom_Playlist9_Name')
Custom_Playlist9_Thumb = getsetting('Custom_Playlist9_Thumb')
Custom_Playlist9_Description = getsetting('Custom_Playlist9_Description')
Custom_Playlist9_Fanart = getsetting('Custom_Playlist9_Fanart')
Custom_Playlist10_ID = getsetting('Custom_Playlist10_ID')
Custom_Playlist10_Name = getsetting('Custom_Playlist10_Name')
Custom_Playlist10_Thumb = getsetting('Custom_Playlist10_Thumb')
Custom_Playlist10_Description = getsetting('Custom_Playlist10_Description')
Custom_Playlist10_Fanart = getsetting('Custom_Playlist10_Fanart')
'''---------------------------'''
Custom_PlaylistL = [Custom_Playlist1_ID, Custom_Playlist2_ID, Custom_Playlist3_ID, Custom_Playlist4_ID, Custom_Playlist5_ID, Custom_Playlist6_ID, Custom_Playlist7_ID, Custom_Playlist8_ID, Custom_Playlist9_ID, Custom_Playlist10_ID]
'''---------------------------'''
commonsearch101 = "זמר"
commonsearch102 = "קריוקי"
commonsearch104 = "הופעה"
commonsearch111 = "Singer"
commonsearch112 = "Karaoke"
commonsearch114 = "LiveShow"