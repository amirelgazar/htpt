import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon

xbmc.sleep(5000)

from variables import *
from modules import *
	
class resetsettings:
	setGeneral_Start(admin)
	try:
		if int(General_MailService) > General_MailService_: setsetting('General_MailService',"1")
	except: setsetting('General_MailService',"1")
	
	setsetting('General_ServiceON',"true")
	setsetting('General_ScriptON',"false")
	setsetting('User_Issue',"")
	setsetting('ModeOn_1',"false")
	'''---------------------------'''
	setsetting('General_Pass',"1")
	setsetting('General_Start',"0")
	'''---------------------------'''
	if General_AllowDebug == "true":
		setSkinSetting("1",'AllowDebug',"true")
		setsetting('ModeOn_12',"true")
		#setsetting('ModeOn_13',"false")
		setsetting('ModeOn_14',"true")
		setsetting('ModeOn_15',"true")
		setsetting('ModeOn_17',"true")
		'''---------------------------'''
	else: setSkinSetting("1",'AllowDebug',"false")
	
	
class main:
	'''------------------------------
	---STARTUP-----------------------
	------------------------------'''
	xbmc.sleep(55000)
	setInfo(admin)
	count = 0
	while 1 and not xbmc.abortRequested:
		'''------------------------------
		---SERVICE-LOOP------------------
		------------------------------'''
		#count += 1
		'''---------------------------'''
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
		connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
		'''---------------------------'''
		getsetting         = xbmcaddon.Addon().getSetting
		setsetting         = xbmcaddon.Addon().setSetting
		General_ScriptON = getsetting('General_ScriptON')
		General_ServiceON = getsetting('General_ServiceON')
		ModeOn_1 = getsetting('ModeOn_1')
		ModeOn_6 = getsetting('ModeOn_6')
		'''---------------------------'''
		if admin3 and admin and not admin2: xbmc.sleep(10000)
		else: xbmc.sleep(60000)
		if count == 0:
			SetGeneral_Pass(admin)
			if ModeOn_1 == "true": pass
			elif General_ScriptON == "true": setGeneral_ScriptON("1", General_ScriptON, "")
			elif General_ServiceON == "true":
				if General_AllowDebug == "true": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=100)')
				elif ModeOn_6 == "true": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=100)')
			elif General_ServiceON != "true": sys.exit(0)
			count = 0
			'''---------------------------'''
		
		if admin and not admin2:
			print printfirst + "service.py_LV" + space + "count" + space2 + str(count) + space + "General_ScriptON" + space2 + str(General_ScriptON) + space + "General_ServiceON" + space2 + str(General_ServiceON) + space + "General_AllowDebug" + space2 + str(General_AllowDebug)
	if xbmc.abortRequested:
		notification("AbortRequest","","",1500)