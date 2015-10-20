#!/usr/bin/python
import xbmc, os, subprocess, sys
import xbmcgui, xbmcaddon

from variables import *
from modules import *
from shared_modules3 import get_params

printpoint = ""
'''---------------------------'''
try: params=get_params()
except Exception, TypeError:
	#notification_common("18")
	printpoint = printpoint + "F"
mode=None
subject=None
content=None
file=None
'''---------------------------'''
try: mode=int(params["mode"])
except: pass
try: subject=urllib.unquote_plus(params["subject"])
except: pass
try: content=urllib.unquote_plus(params["content"])
except: pass
try: file=urllib.unquote_plus(params["file"])
except: pass
'''---------------------------'''

if "F" in printpoint: mode = 1
#exitlist = [4, 7, 8, 10]
#if mode in exitlist and General_ScriptON == "true": sys.exit()

setGeneral_ScriptON("0", General_ScriptON, "")

if ((mode != None and mode != 0 and mode != 100 and mode != 1) or (mode == 1 and ModeOn_1 == "true")) and mode != 10:
	notification_common("2")
	if None in [subject, content, file]: subject, content, file = getAll(mode) ; printpoint = printpoint + "Q"
	if not None in [mode, subject, content, file]: printpoint = printpoint + SendDebug(mode, subject, content, file) ; printpoint = printpoint + "W"
	printpoint = printpoint + "E"
	'''---------------------------'''
elif mode == 0:
	pass
	'''---------------------------'''
	
elif mode == 1 and ModeOn_1 == "false":
	'''------------------------------
	---DEBUG-BUTTON------------------
	------------------------------'''
	if not connected: notification_common("5")
	else:
		'''Current_Name'''
		returned = dialogkeyboard(User_Name, localize(1014) + space + "(" + addonString_servicehtpt(22).encode('utf-8') + ")", 0, '1', 'User_Name', 'service.htpt.debug')
		if returned == 'skip': notification_common("3")
		else:
			'''User_Email'''
			returned = dialogkeyboard(User_Email,"Email",0,'1','User_Email', 'service.htpt.debug')
			if returned == 'skip': notification_common("3")
			else:
				'''User_Tel'''
				try:
					if int(User_Tel) > 010000000 and int(User_Tel) < 9999999999: returned, value = dialognumeric(0,addonString_servicehtpt(12).encode('utf-8'),User_Tel,"0","User_Tel",'service.htpt.debug')
					else:
						returned, value = dialognumeric(0,addonString_servicehtpt(12).encode('utf-8'),"0","0","User_Tel", 'service.htpt.debug')
				except Exception, TypeError:
					xbmc.executebuiltin('Notification(1,1,1000)')
					returned, value = dialognumeric(0,addonString_servicehtpt(12).encode('utf-8'),"0","0","User_Tel", 'service.htpt.debug')
					print printfirst + "dialognumeric" + space + "TypeError" + space2 + str(TypeError)
					'''---------------------------'''
				notification(str(returned),"","",2000)
				if returned == 'skip': notification_common("3")
				elif returned == 'skip0': notification(localize(257),addonString(79539).encode('utf-8'),"",2000)
				elif returned == 'ok':
					'''User_Issue'''
					returned = dialogkeyboard(User_Issue,addonString(79058).encode("utf-8"),0,'1','User_Issue', 'service.htpt.debug')
					if returned == 'skip': notification_common("3")
					else:
						'''send debug prompt'''
						returned = dialogyesno(addonString(79219), addonString(79059))
						if returned == 'skip': notification('$LOCALIZE[257]',addonString_servicehtpt(10).encode('utf-8'),"",2000)
						elif returned == 'ok':
							'''------------------------------
							---RERUN-SCRIPT-WITH-NEW-VAR-----
							------------------------------'''
							setsetting('ModeOn_1',"true")
							setsetting('General_ScriptON',"false") ; xbmc.sleep(200) ; printpoint = printpoint + "x"
							xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=1)')
							#if None in [subject, content, file]: subject, content, file = getAll(mode)
							#if not None in [mode, subject, content, file]: SendDebug(mode, subject, content, file)
							'''---------------------------'''	

elif mode == 10:
	'''------------------------------
	---Activate/Deactivate-Service---
	------------------------------'''
	if allowdebug:
		setSkinSetting("1",'AllowDebug',"false")
		setsetting('General_AllowDebug',"false")
		'''---------------------------'''
	else:
		setSkinSetting("1",'AllowDebug',"true")
		setsetting('General_AllowDebug',"true")
		'''---------------------------'''
	
elif mode == 100:
	'''------------------------------
	---DEBUG-TRIGGER-----------------
	------------------------------'''
	if admin: print printfirst + "DEBUG-TRIGGER-1" + space + "ModeOn_12" + space2 + ModeOn_12
	debugtrigger(admin, connected, General_ScriptON, General_Start, General_Pass, ModeOn_1, ModeOn_2, ModeOn_3, ModeOn_4, ModeOn_5, ModeOn_6, ModeOn_7, ModeOn_8, ModeOn_9, ModeOn_10, ModeOn_11, ModeOn_12, ModeOn_13, ModeOn_14, ModeOn_15, ModeOn_16, ModeOn_17, ModeOn_18, ModeOn_19, ModeOn_20, ModeOn_21)
	if admin: print printfirst + "DEBUG-TRIGGER-2" + space + "ModeOn_12" + space2 + ModeOn_12
	'''---------------------------'''
	
if not "x" in printpoint: setGeneral_ScriptON("1", General_ScriptON, "")
if "9" in printpoint:
	setsetting('General_ServiceON',"false")
	setsetting_custom1('service.htpt.debug','General_ServiceON',"false")
if admin:
	if subject == None: subject = str(subject)
	else: subject = str(subject.encode('utf-8'))
	#if content == None: content = str(content)
	#else: content = str(content.encode('utf-8'))

	print printfirst + "default.py" + space + "mode" + space2 + str(mode) + space + "subject" + space2 + subject