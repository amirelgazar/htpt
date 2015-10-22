import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys
from variables import *
from shared_modules import *

def setRemote_Support(General_Debug, Remote_Support, General_ServiceON):
	name = 'setRemote_Support' ; output = ""
	if not systemplatformwindows:
		output = terminal('ir-keytable','ir-keytable')
		if "No such file or directory" in output or output == "":
			setsetting('Remote_Support','false')
			Remote_Support = 'false'
		else:
			setsetting('Remote_Support','true')
			Remote_Support = 'true'
	
	if General_ServiceON == "true": pass
	else:
		if Remote_Support == "false": dialogok(addonString(13).encode('utf-8'), addonString(12).encode('utf-8'), '', '')
		elif Remote_Support == "true": dialogok(addonString(13).encode('utf-8'), addonString(11).encode('utf-8'), '', '')
	
		if Remote_Support != "true" and General_Debug == "true":
			Remote_Support = "true"
			notification(addonString(12).encode('utf-8'), "Proceeding only cause Debug Mode is active!", "", 2000)
		
	if General_Debug == "true":
		print printfirst + name + space + "Remote_Support" + space2 + str(Remote_Support) + space + "General_ServiceON" + space2 + str(General_ServiceON) + newline + \
		"output" + space2 + str(output)
	
	return Remote_Support

def setRemote_Name(General_Debug, Remote_Name, Remote_TestingTime):
	name = 'setRemote_Name' ; printpoint = ""
	list = []
	list.append('Exit')
	list.append('None')
	list.append('samsung')
	list.append('lg')
	list.append('philips')
	list.append('toshiba')
	list.append('pilot')
	#list.append('sharp'
	
	returned, value = dialogselect(addonString(6).encode('utf-8') + space + "(" + str(Remote_Name) + ")", list,0)

	if returned == -1 or returned == 0:
		if not remotebutton: dialogok(localize(16200), "", "", "") #Abort/Exit
	elif returned == 1: cleartable() #None
	else:
		'''------------------------------
		---NEW-REMOTE-TEST---------------
		------------------------------'''
		Remote_Name2 = value
		
		if not os.path.exists(remotes_path + Remote_Name2):
			printpoint = printpoint + "9"
			notification_common("17")
		else:
			setsetting('Remote_Name2',Remote_Name2)
			setSkinSetting("0", 'IRtype', Remote_Name2)
			'''---------------------------'''
			#if not systemplatformwindows: os.system('sh /storage/.kodi/addons/script.htpt.remote/remote.sh')
			
			Activate(General_Debug, Remote_Name, Remote_Name2)
	
	if General_Debug == "true":
		print printfirst + name + "_LV" + printpoint + space + "returned" + space2 + str(returned) + space + "value" + space2 + str(value)
	
	return printpoint
	
def Activate(General_Debug, Remote_Name, Remote_Name2):
	printpoint = "" ; name = "Activate" ; Remote_Type = ""
	
	if Remote_Name2 != "" and Remote_Name2 != "None":
		printpoint = printpoint + "1"
		Remote_Type = getRemote_Type(Remote_Name2)
		'''Test New Remote'''
		if systemplatformlinux or systemplatformlinuxraspberrypi: terminal('ir-keytable -c','ir-keytable -c')
	
	elif Remote_Name != "" and Remote_Name != "None":
		'''Activate Current Remote'''
		printpoint = printpoint + "2"
		Remote_Type = getRemote_Type(Remote_Name)
	
	else: pass
	
	if Remote_Type != "":
		if "1" in printpoint:
			'''Test New Remote'''
			path = os.path.join(remotes_path, Remote_Name2)
		elif "2" in printpoint:
			'''Activate Current Remote'''
			path = os.path.join(remotes_path, Remote_Name)
		
		else: path = "" ; printpoint = printpoint + "9"
		
		print "wow" + space + str(path)
		
		if systemplatformlinux or systemplatformlinuxraspberrypi:
			terminal('ir-keytable -p '+Remote_Type+' -w '+path+' -D 700 -P 200','ir-keytable')
		
		if "1" in printpoint: testRemote(Remote_Name, Remote_Name2, Remote_TestingTime)
	
	if General_Debug == "true":
		print printfirst + name + space + "Remote_Name" + space2 + str(Remote_Name) + space + "Remote_Name2" + space2 + str(Remote_Name2) + newline + \
		"Remote_Type" + space2 + str(Remote_Type)
		
def testRemote(Remote_Name, Remote_Name2, Remote_TestingTime):
	printpoint = ""
	dialogok(addonString(1).encode('utf-8'), addonString(2).encode('utf-8') + space2 + Remote_Name2, addonString(3).encode('utf-8') + space + "(" + Remote_TestingTime + ")","")
	'''---------------------------'''
	try:
		if int(Remote_TestingTime) < 5 or int(Remote_TestingTime) > 30:
			Remote_TestingTime = "10"
	except Exception, TypeError: Remote_TestingTime = "10"
	
	count = 0
	while count < int(Remote_TestingTime) and not xbmc.abortRequested:
		count += 1
		notification(addonString(3).encode('utf-8') + space2 + Remote_TestingTime + space4 + str(count),"","",1000)
		xbmc.sleep(1000)
		if count == int(Remote_TestingTime):
			printpoint = printpoint + "5"
			returned = dialogyesno(addonString(9).encode('utf-8'), addonString(2).encode('utf-8') + space2 + Remote_Name2)
			if returned == 'ok':
				'''------------------------------
				---NEW-REMOTE-CHOOSEN------------
				------------------------------'''
				printpoint = printpoint + "6"
				notification(addonString(8).encode('utf-8') + space2 + Remote_Name2,"","",4000)
				setsetting('Remote_Name',Remote_Name2)
				setsetting('Remote_LastDate',datenowS)
				'''---------------------------'''
				
			else:
				'''------------------------------
				---KEEP-PREVIOUS-REMOTE----------
				------------------------------'''
				printpoint = printpoint + "7"
				notification_common("9")
				setSkinSetting("0", 'IRtype', Remote_Name)
				if not remotebutton: dialogok(addonString(5).encode('utf-8'), addonString_servicehtpt(10).encode('utf-8'),'[CR]' + localize(74828),"")
				'''---------------------------'''

def cleartable():
	#printpoint = printpoint + "1"
	dialogok(addonString(5).encode('utf-8') + space + localize(1223), addonString_servicehtpt(18).encode('utf-8'), "", localize(78984))
	setsetting('Remote_Name', 'None')
	setSkinSetting("0", 'IRtype', 'None')
	setsetting('Remote_LastDate', datenowS)
	if systemplatformlinux or systemplatformlinuxraspberrypi: terminal('ir-keytable -c', 'Old keytable cleared')

def getRemote_Type(value):
	Remote_Type = ""
	if value == 'samsung':
		Remote_Type = 'nec,rc-6'
	elif value == 'lg':
		Remote_Type = 'nec,rc-6'
	elif value == 'philips':
		Remote_Type = 'nec,rc-6'
	elif value == 'toshiba':
		Remote_Type = 'nec,rc-6'
	elif value == 'pilot':
		Remote_Type = 'nec,rc-6'
	elif value == 'sharp':
		Remote_Type = 'nec,rc-6'
	elif value == 'lg':
		Remote_Type = 'nec,rc-6'
	
	return Remote_Type