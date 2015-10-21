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

getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonFanart = os.path.join(addonPath, "fanart.jpg")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

printfirst = addonName + ": !@# "
'''---------------------------'''
General_ScriptON = getsetting('General_ScriptON')
'''---------------------------'''
Skin_Default = getsetting('Skin_Default')
Skin_Installed = getsetting('Skin_Installed')
Skin_FirstBoot = getsetting('Skin_FirstBoot')
'''---------------------------'''
User_ID = getsetting('User_ID')
Skin_DateInstalled = getsetting('Skin_DateInstalled')
'''---------------------------'''

printpoint = ""
TypeError = ""
extra = ""
name = ""
backupname = "htpt_backup"
backupname2 = "htpt_backup2"
backuppath = home_path
#backupfullpath = os.path.join(backuppath, backupname) #UNUSED HOMEPATH//
#backupfullpath2 = os.path.join(backuppath, backupname2) #UNUSED HOMEPATH//
if systemplatformwindows: restorepath = home_path
else: restorepath = '/storage/'
currentcopydir = os.path.join(addonPath, 'specials', 'scripts', 'copy', '')
htptintalledcopy_path = os.path.join(addonPath, 'specials', 'scripts', 'copy','')
skininstalledtxt = os.path.join(htptintalledcopy_path, 'Skin_Installed.txt')

scriptxbmcbackup_remote_path_2_ = "special://userdata/addon_data/skin.htpt/userdata/backup/" #temp