import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon

'''OTHERS'''
xbmc.sleep(10000)

from variables import *
from modules import *

class startup:
	if 1 + 1 == 3:
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
		systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
		returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
		while returned_Dialog != "" or not homeW or not systemidle10 and not xbmc.abortRequested:
			xbmc.sleep(10000)
			admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
			homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
			systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
			returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
			'''---------------------------''' 
	if xbmc.getSkinDir() == "skin.htpt" and (scripthtptinstall_Skin_Installed == "true" or scripthtptinstall_Skin_FirstBoot == "true" or skinnamestr != "skin.htpt"): pass
	elif dialogyesnoW: pass
	else:
		setsetting('General_ScriptON','false')
		setsetting('General_ServiceON','true')
		
		xbmc.executebuiltin('RunScript(script.htpt.remote)')
	
	#print printfirst + "service.py" + space + "homeW" + space2 + str(homeW) + space + "systemidle10" + space2 + str(systemidle10) + space + "returned_Dialog" + space2 + str(returned_Dialog)