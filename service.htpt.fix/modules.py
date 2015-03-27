#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import os, subprocess, sys
#import datetime
from variables import *

'''------------------------------
---service.htpt.fix--------------
------------------------------'''
def Trial_Renew(idstr_, htptfixversion_, Addon_Version, htptfixversion):
	'''------------------------------
	---***---------------------------
	------------------------------'''
	from variables import datenowS, dateafterS, trialstr, trial2str
	printpoint = ""
	if trial2 and not trial and id9str == 'TrailEnd' and id3str == 'TrailEnd' and verrorstr != 'NONE':
		printpoint = printpoint + "1"
		if trialdate != "" and trialdate2 != "":
			printpoint = printpoint + "2"
			if (Addon_Version != htptfixversion and htptfixversion_ == htptfixversion) and idstr_ == idstr:
				printpoint = printpoint + "3"
				'''execute'''
				setSkinSetting("0",'TrialDate',datenowS)
				setSkinSetting("0",'TrialDate2',dateafterS)
				setSkinSetting("0",'ID3',trial2str)
				setSkinSetting("0",'ID9',trialstr)
				dialogok(addonString(10),addonString(11) + space2 + trialdate + " - " + trialdate2, addonString(12) + space2 + datenowS + " - " + dateafterS, '$LOCALIZE[79084]')
				dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
				if dialogyesnoW: xbmc.executebuiltin('Action(close)')
				'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "Trial_Renew_LV" + printpoint + space + "idstr_" + space2 + idstr_ + space + "idstr" + space2 + idstr
	if not "1" in printpoint: print printfirst + "Trial_Renew1" + space + "trial/2" + space2 + trial + " / " + trial2 + space + "id9str" + space2 + id9str + space + "id3str" + space2 + id3str + space + "verrorstr" + space2 + verrorstr
	if not "3" in printpoint: print printfirst + "Trial_Renew2" + space + "htptfixversion_" + space2 + htptfixversion_ + space + "htptfixversion" + space2 + htptfixversion + space + "Addon_Version" + space2 + Addon_Version + space + "trialdate/2" + space + trialdate + " / " + trialdate2 + space
	if "3" in printpoint: print printfirst + "Trial_Renew3" + space2 + "datenowS" + space2 + datenowS + space + "dateafterS" + space2 + dateafterS
	'''---------------------------'''
				
def ID_Rewrite(idstr_, htptfixversion_, Addon_Version, htptfixversion, idstr2, id1str2, id2str2, id3str2, id4str2, id5str2, id6str2, id7str2, id8str2, id9str2, id10str2, id11str2, id12str2, id60str2):
	'''------------------------------
	---***---------------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	
	if (Addon_Version != htptfixversion and htptfixversion_ == htptfixversion) and idstr_ == idstr:
		idstr2 = idstr2.encode('utf-8')
		id1str2 = id1str2.encode('utf-8')
		id2str2 = id2str2.encode('utf-8')
		id3str2 = id3str2.encode('utf-8')
		id4str2 = id4str2.encode('utf-8')
		id5str2 = id5str2.encode('utf-8')
		id6str2 = id6str2.encode('utf-8')
		id7str2 = id7str2.encode('utf-8')
		id8str2 = id8str2.encode('utf-8')
		id9str2 = id9str2.encode('utf-8')
		id10str2 = id10str2.encode('utf-8')
		id11str2 = id11str2.encode('utf-8')
		id12str2 = id12str2.encode('utf-8')
		id60str2 = id60str2.encode('utf-8')
		'''idstr = USERNAME EN , id1str = USERNAME HE, id2str = INSTALLATION DATE, id3str = WARRENTY END, id4str = ADDRESS, id5str = TELEPHONE NUMBER, id6str = PAYMENT TERMS,
		id7str = QUESTION, id8str = TECHNICAL NAME, id9str = CODE RED, id10str = HTPT'S MODEL, ID11 = MAC1, ID12 = MAC2'''
		if idstr2 != "": setSkinSetting("0",'ID',idstr2)
		if id1str2 != "": setSkinSetting("0",'ID1',id1str2)
		if id2str2 != "": setSkinSetting("0",'ID2',id2str2)
		if id3str2 != "": setSkinSetting("0",'ID3',id3str2)
		if id4str2 != "": setSkinSetting("0",'ID4',id4str2)
		if id5str2 != "": setSkinSetting("0",'ID5',id5str2)
		if id6str2 != "": setSkinSetting("0",'ID6',id6str2)
		if id7str2 == "": setSkinSetting("0",'ID7',id7str2)
		if id8str2 != "": setSkinSetting("0",'ID8',id8str2)
		if id9str2 != "": setSkinSetting("0",'ID9',id9str2)
		if id10str2 != "": setSkinSetting("0",'ID10',id10str2)
		if id11str2 != "": setSkinSetting("0",'ID11',id11str2)
		if id12str2 != "": setSkinSetting("0",'ID12',id12str2)
		if id60str2 != "": setSkinSetting("0",'ID60',id60str2)
		'''---------------------------'''
		print printfirst + "ID_Rewrite: " + datenowS + space
		'''---------------------------'''
		
def setFix_(idstr_, htptfixversion_, Addon_Version, htptfixversion, Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104):
	'''------------------------------
	---APPLY-FIXS--------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	printpoint = ""
	if Addon_Version != htptfixversion:
		printpoint = printpoint + "1"
		if htptfixversion_ == htptfixversion:
			printpoint = printpoint + "2"
			if (idstr_ == idstr or idstr_ == "N/A"):
				printpoint = printpoint + "7"
				'''CHOOSEN FIXS TO APPLY'''
				if "true" in Fix_1: setsetting('Fix_1',"true")
				if "true" in Fix_2: setsetting('Fix_2',"true")
				if "true" in Fix_3: setsetting('Fix_3',"true")
				if "true" in Fix_4: setsetting('Fix_4',"true")
				if "true" in Fix_5: setsetting('Fix_5',"true")
				'''---------------------------'''
				if "true" in Fix_10: setsetting('Fix_10',"true")
				if "true" in Fix_11: setsetting('Fix_11',"true")
				if "true" in Fix_12: setsetting('Fix_12',"true")
				if "true" in Fix_13: setsetting('Fix_13',"true")
				if "true" in Fix_14: setsetting('Fix_14',"true")
				'''---------------------------'''
				if "true" in Fix_100: setsetting('Fix_100',"true")
				if "true" in Fix_101: setsetting('Fix_101',"true")
				if "true" in Fix_102: setsetting('Fix_102',"true")
				if "true" in Fix_103: setsetting('Fix_103',"true")
				if "true" in Fix_104: setsetting('Fix_104',"true")
				'''---------------------------'''
				setsetting('Fix_LastDate',datenowS)
				'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if printpoint == "": print printfirst + "setFix_LV" + printpoint + space + "Addon_Version" + space2 + Addon_Version + space +  "htptfixversion" + space2 + htptfixversion
	elif printpoint == "1": print printfirst + "setFix_LV" + printpoint + space + "htptfixversion_" + space2 + htptfixversion_ + space +  "htptfixversion" + space2 + htptfixversion
	elif printpoint == "12": print printfirst + "setFix_LV" + printpoint + space + "idstr_" + space2 + idstr_ + space +  "idstr" + space2 + idstr
	elif "7" in printpoint:
		print printfirst + "setFix_1/2/3/4/5" + space2 + Fix_1 + " / " + Fix_2 + " / " + Fix_3 + " / " + Fix_4 + " / " + Fix_5
		print printfirst + "setFix_100/101/102/103/104" + space2 + Fix_100 + " / " + Fix_101 + " / " + Fix_102 + " / " + Fix_103 + " / " + Fix_104
		'''---------------------------'''

def setRed_LV(idstr_, htptfixversion_, Addon_Version, htptfixversion, Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5):
	'''------------------------------
	---APPLY-CODE-RED----------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	printpoint = ""
	if Addon_Version != htptfixversion and htptfixversion_ == htptfixversion and idstr_ == idstr:
		'''CHOOSEN RED CODES TO APPLY'''
		if "true" in Red_LV1: setsetting('Red_LV1',"true")
		if "true" in Red_LV2: setsetting('Red_LV2',"true")
		if "true" in Red_LV3: setsetting('Red_LV3',"true")
		if "true" in Red_LV4: setsetting('Red_LV4',"true")
		if "true" in Red_LV5: setsetting('Red_LV5',"true")
		setsetting('Red_LastDate',datenowS)
		setsetting('Red_Alert',"true")
		
		returned = datenowS + space + datenowS + space + idstr_ + space
		'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if printpoint == "": print printfirst + "setRed_LV" + printpoint + space2 + "datenowS" + space2 + datenowS + space + "idstr_" + space2 + idstr_ + space + "htptfixversion / _" + space2 + htptfixversion + " / " + htptfixversion_ + space + "Addon_Version" + space2 + Addon_Version
	elif printpoint == "1":
		print printfirst + "setRed_LV1/2/3/4/5" + space2 + Red_LV1 + " / " + Red_LV2 + " / " + Red_LV3 + " / " + Red_LV4 + " / " + Red_LV5
		'''---------------------------'''
	
def UserBlock(custom):
	
	if custom == "ON": bash('pgrep kodi.bin | xargs kill -SIGSTOP',"UserBlock-ON")
	else: bash('pgrep kodi.bin | xargs kill -SIGCONT',"UserBlock-OFF")
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if custom != "ON": custom = "OFF"
	print printfirst + space + "UserBlock=" + custom
	'''---------------------------'''

def findin_systemcurrentcontrol(custom,what,sleep,action,action2):
	'''action = not found | action2 = when found'''
	'''---------------------------'''
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	
	if custom == "0" and (what != "" and systemcurrentcontrol != what and action != ""): xbmc.executebuiltin(''+ action +'')
	elif custom == "1" and (what != "" and not what in systemcurrentcontrol and action != ""): xbmc.executebuiltin(''+ action +'')
	'''---------------------------'''
	xbmc.sleep(sleep)
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	xbmc.sleep(sleep)
	'''---------------------------'''
	if custom == "0" and (what != "" and systemcurrentcontrol == what and action2 != ""): xbmc.executebuiltin(''+ action2 +'')
	elif custom == "1" and (what != "" and what in systemcurrentcontrol and action2 != ""): xbmc.executebuiltin(''+ action2 +'')
	'''---------------------------'''
	return systemcurrentcontrol

def findin_controlhasfocus(custom,what,sleep,action,action2):
	'''action = not found | action2 = when found'''
	'''---------------------------'''
	what = str(what)
	controlhasfocus = xbmc.getCondVisibility('Control.HasFocus('+ what +')')
	
	if custom == "0" and (what != "" and not controlhasfocus and action != ""): xbmc.executebuiltin(''+ action +'')
	'''---------------------------'''
	xbmc.sleep(sleep)
	controlhasfocus = xbmc.getCondVisibility('Control.HasFocus('+ what +')')
	#systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	xbmc.sleep(sleep)
	'''---------------------------'''
	if custom == "0" and (what != "" and controlhasfocus and action != ""): xbmc.executebuiltin(''+ action2 +'')
	'''---------------------------'''
	return controlhasfocus


	
def doFix_100(printpoint):
	'''---------------------------'''
	dialogok(addonString(46) + '[CR]' + '[COLOR=Yellow]' + addonString(90) + '[/COLOR]', addonString(47), addonString(48), addonString(56))
	#if not systemplatformwindows: UserBlock("ON")
	setSkinSetting("1",'Admin',"true")
	printpoint = ""
	'''---------------------------'''
	notification(addonString(46),'[COLOR=Yellow]' + addonString(90) + '[/COLOR]' + space + addonString(2) + space,"",4000)
	xbmc.executebuiltin('ActivateWindow(10025,plugin://metadata.universal)')
	xbmc.executebuiltin('Action(Down)')
	xbmc.executebuiltin('Action(Select)')
	xbmc.sleep(20000)
	#xbmc.executebuiltin('Action(Close)')
	
	'''---------------------------'''
	xbmc.executebuiltin('ActivateWindow(10025,special://userdata/library/,return)')
	xbmc.sleep(500)
	printpoint = doFix_100A(printpoint)
	'''---------------------------'''
	if not "9" in printpoint: printpoint = doFix_100I(printpoint)
	'''---------------------------'''	
	if not "9" in printpoint: printpoint = doFix_100M(printpoint)
	'''---------------------------'''
	if not "9" in printpoint and "C" in printpoint: printpoint = doFix_100A(printpoint)
	'''---------------------------'''
	if not "9" in printpoint and "C" in printpoint: printpoint = doFix_100I(printpoint)
	'''---------------------------'''	
	if not "9" in printpoint and "C" in printpoint: printpoint = doFix_100M(printpoint)
	'''---------------------------'''
	if not "9" in printpoint: 
		xbmc.sleep(1000)
		dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
		count = 0
		count2 = 0
		while count < 10 and dialogkaitoastW and count2 > -2 and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			xbmc.sleep(500)
			dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
			xbmc.sleep(500)
			if count == 1: printpoint = printpoint + "6"
			if dialogkaitoastW: count2 += 1
			elif count2 > 0: count2 += -1
			if count == 10:
				printpoint = printpoint + "9"
				print "error_count=10"
				'''---------------------------'''
	if not "9" in printpoint: printpoint = printpoint + "7"
	
	'''---------------------------'''
	dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
	if dialogcontentsettingsW: xbmc.executebuiltin('Action(Close)')
	xbmc.sleep(500)
	xbmc.executebuiltin('ReplaceWindow(Home)')
	setSkinSetting("1",'Admin',"false")
	#if not systemplatformwindows: UserBlock("OFF")
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + space + "doFix_100_LV" + printpoint + space + systemcurrentcontrol
	'''---------------------------'''
	return printpoint

def doFix_100_0(printpoint):
	'''---------------------------'''
	systeminternetstate = xbmc.getInfoLabel('System.InternetState')
	try: networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
	except: print printfirst + "main_Error_" + "networkipaddress"
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	hasinternet = systeminternetstate != "" and networkipaddress != "" and not "169.254." in networkipaddress and (connected or systemplatformwindows)
	xbmc.sleep(500)
	'''---------------------------'''
	if systemhasaddon_metadatauniversal and not systemplatformwindows:
		'''------------------------------
		---metadata.universal------------
		------------------------------'''
		printpoint = printpoint + "9"
		path = '/storage/.kodi/addons/'
		list = [os.path.exists(path + 'metadata.universal'), os.path.exists(path + 'metadata.common.impa.com'), os.path.exists(path + 'metadata.common.port.hu')]
		listS = str(list)
		if "True" in listS:
			notification(addonString(46),'[COLOR=Yellow]' + addonString(90) + '[/COLOR]' + space + addonString(2) + space,"",4000)
			bash('rm -rf /storage/.kodi/addons/metadata.universal',"metadata.universal")
			#bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.universal',"metadata.universal -userdata")
			bash('rm -rf /storage/.kodi/addons/metadata.common.impa.com',"metadata.common.impa.com")
			bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.common.impa.com',"metadata.common.impa.com -userdata")
			bash('rm -rf /storage/.kodi/addons/metadata.common.movieposterdb.com',"metadata.common.movieposterdb.com")
			bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.common.movieposterdb.com',"metadata.common.movieposterdb.com -userdata")
			bash('rm -rf /storage/.kodi/addons/metadata.common.ofdb.de',"metadata.common.ofdb.de")
			bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.common.ofdb.de',"metadata.common.ofdb.de -userdata")
			bash('rm -rf /storage/.kodi/addons/metadata.common.port.hu',"metadata.common.port.hu")
			bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.common.port.hu',"metadata.common.port.hu -userdata")
			bash('rm -rf /storage/.kodi/addons/metadata.common.rt.com',"metadata.common.rt.com")
			bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.common.rt.com',"metadata.common.rt.com -userdata")
			#bash('rm -rf /storage/.kodi/addons/metadata.common.trakt.tv',"metadata.common.trakt.tv")
			#bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.common.trakt.tv',"metadata.common.trakt.tv -userdata")
		else: print listS	

	elif hasinternet:
		printpoint = printpoint + "0"
		'''---------------------------'''
	'''---------------------------'''
	return printpoint

def doFix_100A(printpoint):
	xbmc.sleep(200)
	containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
	count = 0
	while count < 10 and containerfolderpath != "special://userdata/library/" and not "9" in printpoint and not xbmc.abortRequested:
		'''------------------------------
		---containerfolderpath-----------
		------------------------------'''
		xbmc.sleep(100)
		count += 1
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		xbmc.sleep(100)
		if count == 1: printpoint = printpoint + "A"
		if count == 10: printpoint = printpoint + "9"
		'''---------------------------'''
	if not "9" in printpoint:
		'''------------------------------
		---ContextMenu-MOVIES.-----------
		------------------------------'''
		xbmc.executebuiltin('Action(PageUp)')
		xbmc.sleep(200)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		count = 0
		while count < 10 and systemcurrentcontrol != "[movies]" and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("0","[movies]",100,'Action(Down)','Action(ContextMenu)')
			if count == 1: printpoint = printpoint + "B"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		if not "9" in printpoint:
			count = 0
			while count < 10 and not xbmc.abortRequested: 
				count += 1
				if count <= 7: xbmc.executebuiltin('Action(Up)')
				else: xbmc.executebuiltin('Action(Down)')
				'''---------------------------'''
		xbmc.sleep(200)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		count = 0
		while count < 10 and systemcurrentcontrol != str20442 and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---Change-content----------------
			------------------------------'''
			count += 1
			countS = str(count)
			'''---------------------------'''
			systemcurrentcontrol = findin_systemcurrentcontrol("0",str20442,100,'Action(Down)','Action(Select)') #Change content
			'''---------------------------'''
			if systemcurrentcontrol == str20442: printpoint = printpoint + "C"
			'''---------------------------'''
			
		if count == 10:
			count = 0
			while count < 10 and not xbmc.abortRequested: 
				count += 1
				if count <= 7: xbmc.executebuiltin('Action(Up)')
				else: xbmc.executebuiltin('Action(Down)')
				'''---------------------------'''
			
			xbmc.sleep(200)
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			count = 0
			while count < 10 and systemcurrentcontrol != str20333 and not "9" in printpoint and not xbmc.abortRequested:
				'''------------------------------
				---Set-content-------------------
				------------------------------'''
				count += 1
				countS = str(count)
				'''---------------------------'''
				systemcurrentcontrol = findin_systemcurrentcontrol("0",str20333,100,'Action(Down)','Action(Select)') #Set content
				'''---------------------------'''
				if systemcurrentcontrol == str20333: printpoint = printpoint + "D"
				if count == 10: printpoint = printpoint + "9" + space3 + systemcurrentcontrol
				'''---------------------------'''
		
		dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
		count = 0
		while count < 10 and not dialogcontentsettingsW and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---dialogcontentsettingsW--------
			------------------------------'''
			count += 1
			xbmc.sleep(100)
			dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
			xbmc.sleep(100)
			if count == 1: printpoint = printpoint + "E"
			if count == 10: printpoint = printpoint + "9" + space3 + systemcurrentcontrol
			'''---------------------------'''
		
		controlhasfocus20 = xbmc.getCondVisibility('Control.HasFocus(20)')
		count = 0
		while count < 10 and not controlhasfocus20 and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---controlhasfocus20-------------
			------------------------------'''
			count += 1
			controlhasfocus20 = findin_controlhasfocus("0",20,100,'Control.SetFocus(20)',"")
			if count == 1: printpoint = printpoint + "F"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
			
		'''	
		count = 0
		while count < 10 and not systemcurrentcontrol in ChangeContentL and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("1",ChangeContentL,100,'Action(Up)','Action(Select)')
			if count == 1: printpoint = printpoint + "H"
			if count == 10: printpoint = printpoint + "9"'''
		'''---------------------------'''
				
	'''---------------------------'''
	return printpoint

def doFix_100I(printpoint):
	xbmc.sleep(500)
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	if "C" in printpoint and not "M" in printpoint:
		'''------------------------------
		---Change-content----------------
		------------------------------'''
		count = 0
		while count < 10 and (not str231 in systemcurrentcontrol or not str16018 in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			if count < 5: systemcurrentcontrol = findin_systemcurrentcontrol("1",str231,100,'Action(Select)','Action(Down)')
			elif count >=5: systemcurrentcontrol = findin_systemcurrentcontrol("1",str16018,100,'Action(Select)','Action(Down)')
			if count == 1: printpoint = printpoint + "I"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		
	elif "D" in printpoint or "M" in printpoint:
		'''------------------------------
		---Set-content-------------------
		------------------------------'''
		count = 0
		while count < 10 and (not str342 in systemcurrentcontrol and not str36901 in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			if count < 5: systemcurrentcontrol = findin_systemcurrentcontrol("1",str342,100,'Action(Select)','Action(Down)')
			elif count >=5: systemcurrentcontrol = findin_systemcurrentcontrol("1",str36901,100,'Action(Select)','Action(Down)')
			if count == 1: printpoint = printpoint + "Q"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		
		'''---------------------------'''
		value = "Universal Movie Scraper" #"The Movie Database" #"Universal Movie Scraper"
		'''---------------------------'''
		xbmc.executebuiltin('Control.SetFocus(20)')
		xbmc.sleep(200)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		count = 0
		while count < 10 and not value in systemcurrentcontrol and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---SCRAPER-NAME------------------
			------------------------------'''
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("1",value,300,'Action(Down)','Action(Select)')
			if value in systemcurrentcontrol: xbmc.executebuiltin('Action(Select)')
			if count == 5: xbmc.executebuiltin('Control.SetFocus(20)')
			if count == 1: printpoint = printpoint + "R"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		
		xbmc.sleep(400)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		count = 0
		while count < 10 and (not str20329 in systemcurrentcontrol or not "(*)" in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---Movies are in separate folders that match the movie title - ON
			------------------------------'''
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("1",str20329,400,'Action(Down)','')
			if count == 1: printpoint = printpoint + "S"
			if count == 10: printpoint = printpoint + "9"
			if str20329 in systemcurrentcontrol: systemcurrentcontrol = findin_systemcurrentcontrol("1","(*)",400,'Action(Select)','')
			'''---------------------------'''
			
		xbmc.sleep(400)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		count = 0
		while count < 10 and (not str20346 in systemcurrentcontrol or "(*)" in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---Scan recursively - OFF--------
			------------------------------'''
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("1",str20346,400,'Action(Down)','')
			if count == 1: printpoint = printpoint + "T"
			if count == 10: printpoint = printpoint + "9"
			if str20346 in systemcurrentcontrol: systemcurrentcontrol = findin_systemcurrentcontrol("1","( )",400,'Action(Select)','')
			'''---------------------------'''
			
	'''count = 0
	while count < 10 and (systemcurrentcontrol != str186 or systemcurrentcontrol != str12321) and not "9" in printpoint and not xbmc.abortRequested:
		count += 1
		if count < 4: xbmc.executebuiltin('Action(Down)')
		if count < 5: systemcurrentcontrol = findin_systemcurrentcontrol("0",str186,100,'Action(Left)','Action(Select)')
		elif count >=5: systemcurrentcontrol = findin_systemcurrentcontrol("0",str12321,100,'Action(Left)','Action(Select)')
		if count == 1: printpoint = printpoint + "J"
		if count == 10: printpoint = printpoint + "9"'''

	if not "9" in printpoint:
		dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
		controlhasfocus28 = xbmc.getCondVisibility('Control.HasFocus(28)')
		count = 0
		while count < 10 and not controlhasfocus28 and dialogcontentsettingsW and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---controlhasfocus28-------------
			------------------------------'''
			count += 1
			dialogcontentsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogContentSettings.xml)')
			controlhasfocus28 = findin_controlhasfocus("0",28,400,'Control.SetFocus(28)','Action(Select)')
			if count == 1: printpoint = printpoint + "J"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		
	'''---------------------------'''
	return printpoint
	
def doFix_100M(printpoint):
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	xbmc.sleep(1000)
	dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
	if dialogyesnoW:
		count = 0
		while count < 10 and (systemcurrentcontrol != str107) and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("0",str107,100,'Action(Down)','Action(Select)')
			if count == 1: printpoint = printpoint + "M"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		xbmc.sleep(1000)
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		count = 0
		count2 = 0
		while count < 500 and dialogprogressW and count2 > -2 and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			xbmc.sleep(1000)
			dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
			xbmc.sleep(1000)
			if count == 1:
				printpoint = printpoint + "N"
				notification(addonString(36) + '[CR]' + '[COLOR=Yellow]' + addonString(90) + '[/COLOR]',addonString(3),"",5000)
			if not dialogprogressW: count2 += -1
			elif count2 < 0: count2 += 1
			if count == 500:
				printpoint = printpoint + "9"
				print "error_count=500"
				'''---------------------------'''
			
	'''---------------------------'''
	return printpoint

def doFix_101(printpoint):
	pass
	
def doFix_2(printpoint):
	'''------------------------------
	---REMOVE-REPOSITORIES-----------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/repository.divingmule.addons',"repository.divingmule.addons")
	bash('rm -rf /storage/.kodi/addons/repository.tknorris.release',"repository.tknorris.release")
	bash('rm -rf /storage/.kodi/addons/repository.addonscriptorde-beta',"repository.addonscriptorde-beta")
	bash('rm -rf /storage/.kodi/addons/repository.superrepo.org.helix.others.adult',"repository.superrepo.org.helix.others.adult")
	
	'''---------------------------'''
	
	'''------------------------------
	---REMOVE-ADDONS-----------------
	------------------------------'''
	
	bash('rm -rf /storage/.kodi/addons/metadata.thexem.de',"metadata.thexem.de")
	bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.thexem.de',"metadata.thexem.de -userdata")
	'''---------------------------'''
	bash('rm -rf /storage/.kodi/addons/plugin.video.howstuffworks_com',"plugin.video.howstuffworks_com")
	bash('rm -rf /storage/.kodi/addons/plugin.video.howstuffworks_com-2.0.4',"plugin.video.howstuffworks_com-2.0.4")
	bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.howstuffworks_com',"plugin.video.howstuffworks_com -userdata")
	'''---------------------------'''
	bash('rm -rf /storage/.kodi/addons/plugin.video.MikeysKaraoke',"plugin.video.MikeysKaraoke")
	bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.MikeysKaraoke',"plugin.video.MikeysKaraoke")
	'''---------------------------'''
	
	'''------------------------------
	---plugin.video.the666sicco------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/plugin.video.the666sicco',"plugin.video.the666sicco")
	bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.the666sicco',"plugin.video.the666sicco")
	setSkinSetting("1",'GoPro.25',"true")
	'''---------------------------'''
	
	'''------------------------------
	---plugin.video.aob--------------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/plugin.video.aob',"plugin.video.aob")
	bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.aob',"plugin.video.aob")
	bash('rm -rf /storage/.kodi/addons/script.module.TheYid.common',"script.module.TheYid.common")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.TheYid.common',"script.module.TheYid.common")
	'''---------------------------'''
	
	'''------------------------------
	---plugin.video.salts------------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/plugin.video.aob',"plugin.video.aob")
	bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.aob',"plugin.video.aob")
	bash('rm -rf /storage/.kodi/addons/script.module.addon.common',"script.module.addon.common")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.addon.common',"script.module.addon.common")
	bash('rm -rf /storage/.kodi/addons/script.module.myconnpy',"script.module.myconnpy")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.myconnpy',"script.module.myconnpy")
	'''---------------------------'''
	
	
	'''------------------------------
	---script.extendedinfo-----------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/script.extendedinfo',"script.extendedinfo")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.extendedinfo',"script.extendedinfo -userdata")
	bash('rm -rf /storage/.kodi/addons/script.module.youtube.dl',"script.module.youtube.dl")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.youtube.dl',"script.module.youtube.dl -userdata")
	bash('rm -rf /storage/.kodi/addons/script.module.pil',"script.module.pil")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.pil',"script.module.pil -userdata")
	bash('rm -rf /storage/.kodi/addons/script.module.unidecode',"script.module.unidecode")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.unidecode',"script.module.unidecode -userdata")
	'''---------------------------'''
	
	'''------------------------------
	---script.toolbox----------------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/script.toolbox',"script.toolbox")
	#bash('rm -rf /storage/.kodi/addons/script.module.pil',"script.module.pil")
	'''---------------------------'''
	
	'''------------------------------
	---plugin.video.testtube---------
	------------------------------'''
	bash('rm -rf /storage/.kodi/addons/plugin.video.testtube',"plugin.video.testtube")
	bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.testtube',"plugin.video.testtube -userdata")
	bash('rm -rf /storage/.kodi/addons/script.module.simple.downloader',"script.module.simple.downloader")
	bash('rm -rf /storage/.kodi/userdata/addon_data/script.module.simple.downloader',"script.module.simple.downloader -userdata")
	setSkinSetting("1",'YouTube.23',"true")
	'''---------------------------'''

def doFix_3(printpoint):
	'''------------------------------
	---SET-FILES-AND-FOLDERS---------
	------------------------------'''
	bash('rm -rf /storage/.kodi/userdata/userdata',"/storage/.kodi/userdata/userdata")
	#bash('rm -rf /storage/.kodi/userdata/userdata',"/storage/.kodi/userdata/guisettings-copy.xml")
	'''---------------------------'''
	
def Execute_Fix(admin, Fix_Done, Fix_L, Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104):
	'''------------------------------
	---EXECUTE-AUTO-FIX--------------
	------------------------------'''
	printpoint = ""
	printpoint2 = ""
	if "true" in Fix_L:
		printpoint = printpoint + "1"
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
		dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
		home_aW = xbmc.getCondVisibility('Window.IsActive(0)')
		startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
		validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')
		validation2 = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION2)')
		'''---------------------------'''
		
		if validation or validation2:
			printpoint = printpoint + "3"
			'''---------------------------'''
			if Fix_10 == 'true':
				'''------------------------------
				---------------------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_10',"false")
				'''---------------------------'''
			if Fix_11 == 'true':
				'''------------------------------
				---------------------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_111',"false")
				'''---------------------------'''
			if Fix_12 == 'true':
				'''------------------------------
				---RED-CODE-LV-BASE--------------
				------------------------------'''
				setSkinSetting("0",'ID7',"")
				setSkinSetting("0",'ID9',"TULU")
				Fix_Done = Fix_Done + space4 + 'Fix_12'
				setsetting_custom1('service.htpt.fix','Fix_12',"false")
				dialogok(addonString(40) + '[CR]' + '[COLOR=Yellow]' + addonString(72) + '[/COLOR]',addonString(54), "", addonString(42))
				'''---------------------------'''
			if Fix_13 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_13',"false")
				'''---------------------------'''
			if Fix_14 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_14',"false")
				'''---------------------------'''	
				
		elif home_aW and not dialogbusyW and not dialogokW and not dialogprogressW and not dialogselectW and not dialogtextviewerW and not dialogyesnoW and not startupW:
			printpoint = printpoint + "2"
			'''---------------------------'''
			if Fix_1 == 'true':
				'''------------------------------
				---LIVE-TV-----------------------
				------------------------------'''
				bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.israelive',"plugin.video.israelive")
				dialogok(addonString(40) + '[CR]' + '[COLOR=Yellow]' + addonString(60) + '[/COLOR]',addonString(35), "", addonString(42))
				Fix_Done = Fix_Done + space4 + 'Fix_1'
				setsetting_custom1('service.htpt.fix','Fix_1',"false")
				#setsetting('Fix_1',"false")
				'''---------------------------'''
			if Fix_2 == 'true':
				'''------------------------------
				---REMOVE-ADDONS-----------------
				------------------------------'''
				doFix_2(printpoint2)
				dialogok(addonString(40) + '[CR]' + '[COLOR=Yellow]' + addonString(61) + '[/COLOR]',addonString(34), "", addonString(42))
				Fix_Done = Fix_Done + space4 + 'Fix_2'
				setsetting_custom1('service.htpt.fix','Fix_2',"false")
				#setsetting('Fix_2',"false")
				'''---------------------------'''
			if Fix_3 == 'true':
				'''------------------------------
				---SET-FILES-AND-FOLDERS---------
				------------------------------'''
				doFix_3(printpoint2)
				dialogok(addonString(40) + '[CR]' + '[COLOR=Yellow]' + addonString(62) + '[/COLOR]',addonString(34), "", addonString(42))
				Fix_Done = Fix_Done + space4 + 'Fix_3'
				setsetting_custom1('service.htpt.fix','Fix_3',"false")
				'''---------------------------'''
			if Fix_4 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_4',"false")
				'''---------------------------'''
			if Fix_5 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_5',"false")
				'''---------------------------'''
			'''---------------------------'''
			if Fix_100 == 'true':
				'''------------------------------
				---SCRAPER-FIX-2-----------------
				------------------------------'''
				printpoint2 = ""
				printpoint2 = doFix_100_0(printpoint2)
				'''---------------------------'''
				if not "9" in printpoint2 and "0" in printpoint2:
					dialogok(addonString(41) + '[CR]' + '[COLOR=Yellow]' + addonString(90) + '[/COLOR]', addonString(43), addonString(44),"")
					returned = dialogyesno(addonString(41),'[COLOR=Yellow]' + addonString(90) + '[/COLOR]' + '[CR]' + addonString(45))
					if returned == 'ok': printpoint2 = doFix_100(admin)
					else: printpoint2 = printpoint2 + "8"
					'''---------------------------'''
					if "7" in printpoint2:
						dialogok(addonString(40) + '[CR]' + '[COLOR=Yellow]' + addonString(90) + '[/COLOR]',addonString(38), addonString(39), "")
						#setsetting_custom1('service.htpt.fix','Fix_100',"false")
						setsetting('Fix_100',"false")
						Fix_Done = Fix_Done + space4 + 'Fix_100'
						'''---------------------------'''
					elif "9" in printpoint2: dialogok(addonString(49) + '[CR]' + '[COLOR=Yellow]' + addonString(90) + '[/COLOR]',"", addonString(37), "")
					'''---------------------------'''		
			elif Fix_101 == 'true':
				'''------------------------------
				---SCRAPER-FIX-1-----------------
				------------------------------'''
				#bash('rm -rf /storage/.kodi/addons/metadata.universal',"metadata.universal")
				#bash('rm -rf /storage/.kodi/userdata/addon_data/metadata.universal',"metadata.universal -userdata")
				#dialogok(addonString(40),'[COLOR=Yellow]' + addonString(61) + '[/COLOR]', "", addonString(42))
				#Fix_Done_ = Fix_Done_ + Fix_2 + "/"
				setsetting_custom1('service.htpt.fix','Fix_101',"false")
				'''---------------------------'''
			elif Fix_102 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_102',"false")
				'''---------------------------'''
			elif Fix_103 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_103',"false")
				'''---------------------------'''
			elif Fix_104 == 'true':
				'''------------------------------
				---?-FIX-------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_104',"false")
				'''---------------------------'''
			
			#setsetting_custom1('service.htpt.fix','Fix_Done',Fix_Done)
			setsetting('Fix_Done',Fix_Done)
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	Fix_L = str(Fix_L)
	if admin and printpoint == "": print printfirst + space + "ExecuteFix_LV" + printpoint + space + "Fix_L" + space2 + Fix_L + space + "Fix_1" + space2 + Fix_1 + space + "Fix_100" + space2 + Fix_100
	else: print printfirst + space + "ExecuteFix_LV" + printpoint + space + "Fix_Done" + space2 + Fix_Done
	'''---------------------------'''
	return Fix_Done
	
def Execute_Red(admin, Red_Done, Red_L, Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5):
	'''------------------------------
	---EXECUTE-CODE-RED--------------
	------------------------------'''
	printpoint = ""
	if "true" in Red_L:
		'''------------------------------
		---Red_Alert+LV------------------
		------------------------------'''
		if Red_LV1 == "true":
			'''------------------------------
			---SIMPLE-LOCK-DOWN--------------
			------------------------------'''
			setSkinSetting("0",'ID7',"40")
			Red_Done = Red_Done + space4 + 'Red_LV1'
			#setsetting_custom1('service.htpt.fix','Red_LV1',"false")
			setsetting('Red_LV1',"false")
			printpoint == printpoint + "1"
			'''---------------------------'''
		
		if Red_LV2 == "true":
			'''------------------------------
			---???---------------------------
			------------------------------'''
			Red_Done = Red_Done + space4 + 'Red_LV2'
			#setsetting_custom1('service.htpt.fix','Red_LV2',"false")
			setsetting('Red_LV2',"false")
			printpoint == printpoint + "2"
			'''---------------------------'''
			
		if Red_LV3 == "true":
			'''------------------------------
			---REMOVE-ADDONS-----------------
			------------------------------'''
			if not systemplatformwindows: os.system('sh /storage/.kodi/addons/service.htpt.fix/specials/scripts/Red_LV3.sh')
			Red_Done = Red_Done + space4 + 'Red_LV3'
			#setsetting_custom1('service.htpt.fix','Red_LV3',"false")
			setsetting('Red_LV3',"false")
			printpoint == printpoint + "3"
			'''---------------------------'''
		
		if Red_LV4 == "true":
			'''------------------------------
			---GAMES-------------------------
			------------------------------'''
			if not systemplatformwindows: os.system('sh /storage/.kodi/addons/service.htpt.fix/specials/scripts/Red_LV4.sh')
			Red_Done = Red_Done + space4 + 'Red_LV4'
			#setsetting_custom1('service.htpt.fix','Red_LV4',"false")
			setsetting('Red_LV4',"false")
			printpoint == printpoint + "4"
			'''---------------------------'''
		
		if Red_LV5 == "true":
			'''------------------------------
			---TOTAL-------------------------
			------------------------------'''
			bash('rm -rf /storage',"Red_LV5")
			Red_Done = Red_Done + space4 + 'Red_LV5'
			#setsetting_custom1('service.htpt.fix','Red_LV5',"false")
			setsetting('Red_LV5',"false")
			printpoint == printpoint + "5"
			'''---------------------------'''
	
		if printpoint != "" and printpoint != "5":
			'''------------------------------
			---Red_LV+printpoint-------------
			------------------------------'''	
			setSkinSetting("0",'ID7',"40")
			setSkinSetting("0",'ID9',"RED_LV" + printpoint)
			'''---------------------------'''
		
		setsetting('Red_Done',Red_Done)
		setsetting('Red_Alert',"false")
		
	else:
		'''------------------------------
		---Red_Alert-WARNING-------------
		------------------------------'''
		dialogok(addonString(50),'[COLOR=Red]' + addonString(51) + '[/COLOR]', addonString(51), addonString(42))
		setsetting('Red_Alert',"false")
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	Red_L = str(Red_L)
	if admin and printpoint == "": print printfirst + space + "Execute_RedLV" + printpoint + space + "Red_L" + space2 + Red_L + space + "Red_LV1" + space2 + Red_LV1
	else:
		print printfirst + space + "Execute_RedLV" + printpoint + space + "Red_Done" + space2 + Red_Done
		dialogok(addonString(50),'[COLOR=Red]' + addonString(53) + space2 + printpoint + '[/COLOR]', addonString(52), addonString(42))
		'''---------------------------'''
	'''---------------------------'''
	return Red_Done
	
def setAddon_Update(admin, Addon_Version, htptfixversion, Addon_Update):
	'''------------------------------
	---CHECK-FOR-FIX-UPDATE----------
	------------------------------'''
	if Addon_Version != htptfixversion and Addon_Update == "false":
		Addon_Update2 = "true"
		setsetting('Addon_UpdateLog',"true")
		'''---------------------------'''
	else:
		Addon_Update2 = "false"
		'''---------------------------'''
		
	if Addon_Update != Addon_Update2: setsetting('Addon_Update',Addon_Update2)
	'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and Addon_Update != Addon_Update2: print printfirst + "setAddon_Update" + space2 + "Addon_Update" + space2 + Addon_Update + " - " + Addon_Update2
	'''---------------------------'''	

def setAddon_UpdateDate(admin, Addon_Version, htptfixversion, Addon_Update, Addon_UpdateDate):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	import datetime
	datenow = datetime.date.today()
	datenowS = str(datenow)
	'''---------------------------'''
	#setsetting_custom1('service.htpt','Skin_UpdateDate',datenowS)
	if Addon_UpdateDate != datenowS:
		setsetting('Addon_UpdateDate',datenowS)
	#dateleft = stringtodate(skinsetting3,'%Y-%m-%d')
	#dateleft2 = str(dateleft)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if Addon_Update == "true" or Addon_UpdateDate == "": print printfirst + "setAddon_UpdateDate" + space2 + "Addon_UpdateDate" + space2 + Addon_UpdateDate + " - " + datenowS
	'''---------------------------'''
	
def setAddon_Version(admin, Addon_Version, htptfixversion):
	'''------------------------------
	---CHECK-FOR-ADDON-UPDATE-2------
	------------------------------'''
	if Addon_Version != htptfixversion:
		setsetting('Addon_Version',htptfixversion)
		'''---------------------------'''	
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "setAddon_Version" + space2 + "Addon_Version" + space2 + Addon_Version + " - " + htptfixversion
		'''---------------------------'''	

def setAddon_UpdateLog(admin, Addon_Version, Addon_UpdateDate, Fix_Done):	
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	datenowD = stringtodate(datenowS,'%Y-%m-%d')
	datedifferenceD = stringtodate(Addon_UpdateDate,'%Y-%m-%d')
	datedifferenceS = str(datedifferenceD)
	number2 = datenowD - datedifferenceD
	number2S = str(number2)
	if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
	elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
	else: number2S = "0"
	if admin: notification("number2S:" + number2S,"","",2000)
	number2N = int(number2S)
	'''---------------------------'''

	if number2N == 0: header = '[COLOR=Yellow]' + addonString(40) + space + Addon_Version + '[/COLOR]'
	else: header = ""
	'''---------------------------'''
	#message2 = ""
	#if header != "": xbmc.executebuiltin('RunScript(script.toolbox,info=textviewer,header='+ header +',text='+ message2 +')')
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "setAddon_UpdateLog" + space2 + "Addon_UpdateDate" + space2 + Addon_UpdateDate + " - " + datenowS + space + "(" + number2S + ")"
	'''---------------------------'''
	
'''------------------------------
---DEFAULT-----------------------
------------------------------'''
def bash(bashCommand,bashname):
	'''------------------------------
	---RUN-BASH-COMMANDS-------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	if not systemplatformwindows:
		#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		process = subprocess.Popen(bashCommand,stdout=subprocess.PIPE,shell=True)
		output = process.communicate()[0]
		'''---------------------------'''
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if admin and admin2: print printfirst + bashname + space2 + output	
		'''---------------------------'''
		return output

def get_daynow(custom):
	daynow = datenow.strftime("%a")
	daynowS = str(daynow)
	return daynowS
	
def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)
	
def stringtodate(dt_str, dt_func):
	from datetime import datetime
	#dt_str = '9/24/2010 5:03:29 PM'
	#dt_func = '%m/%d/%Y %I:%M:%S %p'
	try:
		dt_obj = datetime.strptime(dt_str, dt_func)
		return dt_obj
	except:
		notification("stringtodate_ERROR!","sys.exit()","",5000)
		sys.exit()
	
	
def dialogok(heading,line1,line2,line3):
	'''------------------------------
	---DIALOG-OK---------------------
	------------------------------'''
	dialog = xbmcgui.Dialog()
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	if '$LOCALIZE' in line2 or '$ADDON' in line2: line2 = xbmc.getInfoLabel(line2)
	if '$LOCALIZE' in line3 or '$ADDON' in line3: line3 = xbmc.getInfoLabel(line3)
	heading = str(heading.encode('utf-8'))
	line1 = str(line1.encode('utf-8'))
	line2 = str(line2.encode('utf-8'))
	try: line3 = str(line3.encode('utf-8'))
	except: line3 = str(line3)

	dialog.ok(heading,line1,line2,line3)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + heading + space2 + line1 + space2 + line2 + space2 + line3
	'''---------------------------'''

def dialogprogress(heading,line1,line2,line3): 
	'''------------------------------
	---DIALOG-OK-***BROKEN***--------
	------------------------------'''
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	if '$LOCALIZE' in line2 or '$ADDON' in line2: line2 = xbmc.getInfoLabel(line2)
	if '$LOCALIZE' in line3 or '$ADDON' in line3: line3 = xbmc.getInfoLabel(line3)
	heading = str(heading.encode('utf-8'))
	line1 = str(line1.encode('utf-8'))
	line2 = str(line2.encode('utf-8'))
	line3 = str(line3.encode('utf-8'))
	
	pDialog = xbmcgui.DialogProgress()
	#pDialog.create(heading,line1,line2,line3)
	pDialog.update(10,line1,line2,line3)
	
	#pDialog = xbmcgui.DialogProgressBG()
	#pDialog.create(heading, line1)
	
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "dialogprogress" + space2 + heading + space2 + line1 + space2 + line2 + space2 + line3
	'''---------------------------'''

def dialogselect(heading, list, autoclose):
	'''------------------------------
	---DIALOG-SELECT-----------------
	------------------------------'''
	dialog = xbmcgui.Dialog()
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	
	returned = dialog.select(heading,list,autoclose)
	returned = str(returned)
	
	print printfirst + heading + "( " + returned + " )"
	return returned
	'''---------------------------'''
	
def dialogkeyboard(input, heading, option, custom, addonsetting, addonsetting2):
	''''''
	if '$LOCALIZE' in heading: heading = xbmc.getInfoLabel(heading)
	dialog = xbmcgui.Dialog()
	keyboard = xbmc.Keyboard(input,heading,option)
	keyboard.doModal()
	returned = 'skip'
	if (keyboard.isConfirmed()):
		input2 = keyboard.getText()
		if custom == '1' and input2 != "": returned = 'ok'
		if custom == '2' and input2 == input: returned = 'ok'
		if custom == '3':
			if input2 != input and input2 != "" and option == 0: xbmc.executebuiltin('Notification('+ heading +': '+ input2 +',,4000)')
			if input2 != "": returned = 'ok'
			
		if option == 0: print printfirst + heading + space2 + input2 + " ( " + returned + " )"
		elif option != 0: print printfirst + heading + space2 + "*******" + " ( " + returned + " )"
	if returned == 'ok':
		returned == input2
		if addonsetting2 == "0": setsetting(addonsetting, input2)
		elif 'genesis' in addonsetting2:
			setsetting_genesis          = xbmcaddon.Addon('plugin.video.genesis').setSetting
			setsetting_genesis(addonsetting, input2)
		elif 'sdarot.tv' in addonsetting2:
			setsetting_sdarottv          = xbmcaddon.Addon('plugin.video.sdarot.tv').setSetting
			setsetting_sdarottv(addonsetting, input2)
	return returned

def dialognumeric(type,heading,input,custom,addonsetting):
	'''type: 0 = #, 1 = DD/MM/YYYY, 2 = HH:MM, 3 = #.#.#.#, message2 = heading, message1 = content'''
	if '$LOCALIZE' in heading: heading = xbmc.getInfoLabel(heading)
	try:
		input = int(input)
	except:
		input = 0
	returned = 'skip'
	try:
		if int(input) > 001000000 and int(input) < 9999999999 and input != "": input = str(input)
	except TypeError:
		input = 0
		print printfirst + "dialognumeric " + "except TypeError (1)"
	input = str(input)
	input2 = xbmcgui.Dialog().numeric(type, heading, input)
	try:
		if input2 != "": input2 = int(input2)
	except TypeError:
		xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[31406],2000)')
		sys.exit()
	if custom == '0':
		try:
			if input2 > 001000000 and input2 < 9999999999: returned = 'ok'
			elif input2 < 001000000 or input2 > 9999999999: returned = 'skip0'
		except TypeError:
			returned = 'skip'
	if custom == '1':
		if input2 != "": returned = 'ok'
	if custom == '2':
		if input2 == "": input2 = 0
		elif input2 != 0: returned = 'ok'
	#if type == '2' and input == message1: returned = 'ok'
	
	input = str(input)
	input2 = str(input2)
	print printfirst + heading + space2 + input2 + "( " + returned + " )"
	if returned == 'ok':
		if custom != "2":
			returned == input
			setsetting(addonsetting, input2)
		elif custom == "2":
			returned == input
			if returned == "": returned = 0
			setSkinSetting("0", addonsetting, input2)
			#setsetting(addonsetting, input2)
			
	return returned

def dialogyesno(heading,line1):
	'''------------------------------
	---DIALOG-YESNO------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	returned = 'skip'
	if dialog.yesno(heading,line1): returned = 'ok'
	heading = str(heading.encode('utf-8'))
	line1 = str(line1.encode('utf-8'))
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "dialogyesno" + space2 + heading + space3 + line1 + "( " + returned + " )"
	'''---------------------------'''
	return returned
	'''---------------------------'''

def notification(heading, message, icon, time):
	'''------------------------------
	---Show a Notification alert.----
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	'''heading : string - dialog heading | message : string - dialog message. | icon : [opt] string - icon to use. (default xbmcgui.NOTIFICATION_INFO/NOTIFICATION_WARNING/NOTIFICATION_ERROR) | time : [opt] integer - time in milliseconds (default 5000) | sound : [opt] bool - play notification sound (default True)'''
	
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in message or '$ADDON' in message: message = xbmc.getInfoLabel(message)
	
	icon = "misc/logo/logo8.png"
	
	dialog.notification(heading, message, icon, time)
	
	#if "addonString" in heading and not "+" in heading: heading = str(heading.encode('utf-8'))
	if "addonString" in heading: heading = str(heading.encode('utf-8'))
	elif '$LOCALIZE' in heading or '$ADDON' in heading: heading = str(heading)
	if "addonString" in message: message = str(message.encode('utf-8'))
	elif '$LOCALIZE' in message or '$ADDON' in message: message = str(message)
	
	time = str(time)
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin:
		try: print printfirst + "notification" + space2 + heading + space3 + message + space + time
		except: print printfirst + "notification" + "..."
		'''---------------------------'''

def addonsettings2(addon,set1,set1v,set2,set2v,set3,set3v,set4,set4v,set5,set5v):
	'''------------------------------
	---SET-ADDON-SETTING-5-----------
	------------------------------'''
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	setsetting_custom          = xbmcaddon.Addon(addon).setSetting

	setting1 = getsetting_custom(set1)
	setting2 = getsetting_custom(set2)
	setting3 = getsetting_custom(set3)
	setting4 = getsetting_custom(set4)
	setting5 = getsetting_custom(set5)
	
	checkChange = "false"
	'''---------------------------'''
	if set1 != "" and set1v != setting1:
		setsetting_custom(set1,set1v)
		if checkChange != "true": checkChange = "true"
	if set2 != "" and set2v != setting2:
		setsetting_custom(set2,set2v)
		if checkChange != "true": checkChange = "true"
	if set3 != "" and set3v != setting3:
		setsetting_custom(set3,set3v)
		if checkChange != "true": checkChange = "true"
	if set4 != "" and set4v != setting4:
		setsetting_custom(set4,set4v)
		if checkChange != "true": checkChange = "true"
	if set5 != "" and set5v != setting5:
		setsetting_custom(set5,set5v)
		if checkChange != "true": checkChange = "true"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if checkChange == "true": print printfirst + "addonsettings2 " + addon + space + set1 + space2 + set1v + space + set2 + space2 + set2v + space + set3 + space2 + set3v + space + set4 + space2 + set4v + space + set5 + space2 + set5v + space
	'''---------------------------'''
	
def setsetting_custom1(addon,set1,set1v):
	'''------------------------------
	---SET-ADDON-SETTING-1-----------
	------------------------------'''
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	setsetting_custom          = xbmcaddon.Addon(addon).setSetting
	
	set = getsetting_custom(set1)
	'''---------------------------'''
	if set != set1v:
		setsetting_custom(set1,set1v)
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "setsetting_custom1" + space2 + addon + space + set1 + space2 + set1v + space3
		'''---------------------------'''
		
def setSkinSetting(custom,set1,set1v):
	'''------------------------------
	---SET-SKIN-SETTING-1------------
	------------------------------'''
	from variables import truestr
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')

	''' custom: 0 = Skin.String, 1 = Skin.HasSetting'''
	'''---------------------------'''
	if custom == "0":
		setting1 = xbmc.getInfoLabel('Skin.String('+ set1 +')')
		setting2 = ""
		if setting1 != set1v: xbmc.executebuiltin('Skin.SetString('+ set1 +','+ set1v +')')
		'''---------------------------'''
		
	elif custom == "1":
		setting2 = xbmc.getInfoLabel('Skin.HasSetting('+ set1 +')')
		if setting2 == truestr: setting1 = "true"
		else:
			setting1 = "false"
		if setting1 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set1 +')')
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if setting1 != set1v and admin and admin2: print printfirst + "setSkinSetting" + space3 + custom + space + set1 + space2 + setting1 + " - " + set1v + space3 + "( " + "setting2" + space2 + setting2 + " ) "
	'''---------------------------'''

def setSkinSetting5(custom,set1,set1v,set2,set2v,set3,set3v,set4,set4v,set5,set5v):
	'''------------------------------
	---SET-SKIN-SETTING-5------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	''' custom: 0 = Skin.String, 1 = Skin.HasSetting'''
	if custom == "0":
		setting1 = xbmc.getInfoLabel('Skin.String('+ set1 +')')
		setting2 = xbmc.getInfoLabel('Skin.String('+ set2 +')')
		setting3 = xbmc.getInfoLabel('Skin.String('+ set3 +')')
		setting4 = xbmc.getInfoLabel('Skin.String('+ set4 +')')
		setting5 = xbmc.getInfoLabel('Skin.String('+ set5 +')')
	elif custom == "1":
		setting1 = xbmc.getInfoLabel('Skin.HasSetting('+ set1 +')')
		setting2 = xbmc.getInfoLabel('Skin.HasSetting('+ set2 +')')
		setting3 = xbmc.getInfoLabel('Skin.HasSetting('+ set3 +')')
		setting4 = xbmc.getInfoLabel('Skin.HasSetting('+ set4 +')')
		setting5 = xbmc.getInfoLabel('Skin.HasSetting('+ set5 +')')
	'''---------------------------'''
	if custom == "0":
		if setting1 != set1v: xbmc.executebuiltin('Skin.SetString('+ set1 +','+ set1v +')')
		if setting2 != set2v: xbmc.executebuiltin('Skin.SetString('+ set2 +','+ set2v +')')
		if setting3 != set3v: xbmc.executebuiltin('Skin.SetString('+ set3 +','+ set3v +')')
		if setting4 != set4v: xbmc.executebuiltin('Skin.SetString('+ set4 +','+ set4v +')')
		if setting5 != set5v: xbmc.executebuiltin('Skin.SetString('+ set5 +','+ set5v +')')
	elif custom == "1":
		if setting1 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set1 +')')
		if setting2 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set2 +')')
		if setting3 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set3 +')')
		if setting4 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set4 +')')
		if setting5 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set5 +')')
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''	
	if admin and (setting1 != set1v or setting2 != set2v or setting3 != set3v or setting4 != set4v or setting5 != set5v): print printfirst + "setSkinSetting5" + space2 + set1 + space + set2 + space + set3 + space + set4 + space + set5 + space3
	'''---------------------------'''
	
def calculate(addon, set1, custom, opt):
	'''------------------------------
	---RETURN-CALCULATE-NUMBER-------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	setsetting_custom          = xbmcaddon.Addon(addon).setSetting
		
	set1v = getsetting_custom(set1)
	set1v = int(set1v)
	
	if opt != "": set2v = int(opt)
	else: set2v = ""
	'''---------------------------'''
	if custom == '1':
		set1v += 1
		if opt != "": set2v += 1
		'''---------------------------'''
	elif custom == '2':
		set1v += -1
		if opt != "": set2v += -1
		'''---------------------------'''
	set1v = str(set1v)
	if opt != "": set2v = str(set2v)
	'''---------------------------'''
	if opt != "": setsetting_custom(set1, set2v)
	else: setsetting_custom(set1, set1v)

	
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''	
	if admin and admin2: print printfirst + "calculate" + space + addon + space + set1 + space + "set1v" + space + set1v + space + "set2v" + space + set2v
	if opt != "": return set2v
	else: return set1v
	'''---------------------------'''
	
	
	
'''------------------------------
---CUSTOM------------------------
------------------------------'''
