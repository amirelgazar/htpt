#!/usr/bin/python
import xbmc, sys, xbmcaddon
import xbmcgui, os

from variables import *
from modules import *

Remote_Support = setRemote_Support(General_Debug, Remote_Support, General_ServiceON)

if Remote_Support != "true":
	if General_ServiceON != "true": dialogok(addonString(12).encode('utf-8'), "- Make sure you have IR adapter!", "-Make sure your OS is supported!","For Support see Facebook page or related forum!")
	else: setsetting('General_ServiceON','false')
	sys.exit()
	
setGeneral_ScriptON("0", General_ScriptON, "")
setSkinSetting("0", 'IRtype', Remote_Name)

class main:
	if Remote_Name == "":
		printpoint = printpoint + "1"
		setSkinSetting("0", 'IRtype', "")
		returned = dialogyesno(addonString(5).encode('utf-8'), addonString(4).encode('utf-8') + '[CR]' + addonString(19194).encode('utf-8'))
		if returned == 'skip': printpoint = printpoint + "9"
	
	if not "9" in printpoint:
		if remotebutton or Remote_Name == "":
			printpoint = printpoint + "2"
			printpoint = setRemote_Name(General_Debug, Remote_Name, Remote_TestingTime)
			
		else:
			if Remote_Name != "":
				printpoint = printpoint + "3"
				Activate(General_Debug, Remote_Name, Remote_Name2)
				#if not systemplatformwindows: os.system('sh /storage/.kodi/addons/script.htpt.remote/remote.sh')
				#print printfirst + "remote.sh; remote type: " + Remote_Name
				if datenowS == Remote_LastDate:
					returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
					if returned_Dialog == "": dialogok(addonString(5).encode('utf-8'), addonString(14).encode('utf-8'), "", addonString(15).encode('utf-8'))
				
	setsetting('Remote_Name2',"")
	
	if not "9" in printpoint:
		xbmc.sleep(1000)
		if systemplatformlinux or systemplatformlinuxraspberrypi:
			Remote_Name = getsetting('Remote_Name')
			if Remote_Name != "None": os.system('sh /storage/.kodi/addons/script.htpt.remote/remote.sh')
		
		Remote_Name2 = getsetting('Remote_Name')
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "default.py_LV" + printpoint + space + "Remote_Name" + space2 + Remote_Name + space + "Remote_Name2" + space2 + Remote_Name2
	'''---------------------------'''
	
setGeneral_ScriptON("1", General_ScriptON, "")