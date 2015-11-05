import xbmc, xbmcgui, xbmcaddon
import os, sys
#import subprocess

xbmc.sleep(1000)

from variables import *
from modules import *
setAutoSettings("1")

class ResetSettings:
	setsetting('Addon_ServiceON',"true")
	setsetting('General_ScriptON',"false")
	setsetting('General_Terminal',"true")
	setsetting('Subtitle_Search',"")
	setsetting('Subtitle_Service',"")
	'''---------------------------'''


		
class Startup:
	
	while xbmc.getSkinDir() != 'skin.htpt' and not xbmc.abortRequested:
		xbmc.sleep(10000)
		
	if xbmc.getSkinDir() == "skin.htpt":
		'''---------------------------'''
		mode215('_',admin,'','')
		if totalmouse and systemplatformwindows: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=101)')
		setSkinSetting("0", 'smartkeyboardHN', "1")
		setSkinSetting("0", 'smartkeyboardCN', "1")
		setSkinSetting("0", 'smartkeyboardPN', "1")
		setSkinSetting("1", 'smartkeyboard', "false") #WIP
		'''---------------------------'''
		printpoint = printpoint + "1"
		setAutoSettings("3")
		xbmc.sleep(10000)
		count = 0
		while count < 5 and not xbmc.abortRequested:
			admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
			dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
			dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
			dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
			dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
			dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
			custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
			startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
			homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
			if homeW and not dialogprogressW and not dialogokW and not dialogbusyW and not dialogtextviewerW and not dialogyesnoW and not startupW and not custom1191W:
				if count == 0: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=100)') ; xbmc.sleep(10000)
				elif count == 1: xbmc.executebuiltin('RunScript('+ addonID +',,?mode=55)') ; xbmc.sleep(10000)
				count += 1
				xbmc.sleep(5000)
				'''---------------------------'''
			else:	
				if admin: xbmc.sleep(5000)
				else: xbmc.sleep(10000)
				'''---------------------------'''
			if admin: print printfirst + "service.py" + space + "count" + space2 + str(count)
		
		
		'''---------------------------'''
	
class exit:
	if admin: notification(addonID + space + "service.py","Clean Exit","",5000)
	setsetting('Addon_ServiceON',"false")
	sys.exit()





