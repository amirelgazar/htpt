'''------------------------------
---shared_variables--------------
------------------------------'''
import xbmc, xbmcaddon, sys, os
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
#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)

getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

printfirst = addonName + ": !@# "
'''triggers'''
admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
remotebutton = xbmc.getCondVisibility('Container(50).HasFocus(81)') or xbmc.getInfoLabel('ListItem.Label') == addonName or (xbmc.getCondVisibility('Window.IsVisible(Settings.xml)') and xbmc.getInfoLabel('System.CurrentControl') == addonString(5).encode('utf-8'))

# (xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(102)'))
#systemidle40 = xbmc.getCondVisibility('System.IdleTime(40)')

printpoint = ""

remotes_path = os.path.join(htptservice_path, 'resources', 'remotes', '')
'''ADDON SETTINGS'''
Remote_Name = getsetting('Remote_Name')
Remote_Name2 = getsetting('Remote_Name2')
General_Debug = getsetting('General_Debug')
General_ScriptON = getsetting('General_ScriptON')
General_ServiceON = getsetting('General_ServiceON')
Remote_Support = getsetting('Remote_Support')
Remote_TestingTime = getsetting('Remote_TestingTime')
Remote_LastDate = getsetting('Remote_LastDate')