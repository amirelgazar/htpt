#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
#import datetime
from variables import *

def bash(bashCommand,bashname):
	'''run BASH commands'''
	import subprocess
	if not systemplatformwindows:
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		if bashname == "zip":
			if "adding: " in output or "updating: " in output or "freshening: " in output:
				returned == 'ok'
			else:
				returned == 'skip'
			print printfirst + bashname + space2 + output + " ( " + returned + " )"
			return returned
		if bashname == "ifconfig":
			print printfirst + bashname + space2 + output	
			return output
		if bashname == "df":
			print printfirst + bashname + space2 + output	
			return output

def testStream(admin, General_ConnectionScore, General_CustomVAR, playerhasvideo):
	'''------------------------------
	---SMOOTH-TRUE/FALSE-------------
	------------------------------'''
	#General_ConnectionScore = getsetting('General_ConnectionScore')
	#General_CustomVAR = getsetting('General_CustomVAR')
	if admin: notification("General_ConnectionScore_2=" + General_ConnectionScore,"","",2000)
	count = 0
	countS = str(count)
	printpoint = ""
	smooth = ""
	xbmc.executebuiltin('Action(Play)') #TRY TO PREVENT PAUSE OF THIS SERVICE IF CACHE
	xbmc.sleep(200)
	while count < 10 and playerhasvideo and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
		playerpaused = xbmc.getCondVisibility('Player.Paused')
		playercache = xbmc.getInfoLabel('Player.CacheLevel')
		'''---------------------------'''
		if count > 0: xbmc.sleep(1000)
		count += 1
		countS = str(count)
		'''---------------------------'''
		if count > 0:
			'''------------------------------
			--APPLY-MANY---------------------
			------------------------------'''	
			if not systemplatformwindows and not connected: setGeneral_Connected(connected)
			if smooth == "":
				if not playerpaused: xbmc.executebuiltin('Action(Pause)')
				printpoint = printpoint + "1"
				
			elif smooth == "true":
				'''------------------------------
				--VARIABLES----------------------
				------------------------------'''	
				containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
				istv2 = (xbmc.getInfoLabel('VideoPlayer.TVShowTitle') != "" and xbmc.getInfoLabel('VideoPlayer.Season') != "" and xbmc.getInfoLabel('VideoPlayer.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
				ismovie2 = (xbmc.getInfoLabel('VideoPlayer.Year') != "" or xbmc.getInfoLabel('VideoPlayer.Country') != "" or xbmc.getInfoLabel('VideoPlayer.Tagline') != "") and not istv2
				videoplayerhassubtitles = xbmc.getCondVisibility('VideoPlayer.HasSubtitles')
				'''---------------------------'''
				if playerpaused: xbmc.executebuiltin('Action(Play)')
				#if not "2" in printpoint and not videoplayerhassubtitles and (istv2 or ismovie2): xbmc.executebuiltin('ActivateWindow(subtitlesearch)')
				if not "2" in printpoint: setGeneral_ConnectionScore(admin, General_ConnectionScore, "", smooth)
				printpoint = printpoint + "2"
			elif smooth == "fix":
				if count == 6:
					if playerpaused: xbmc.executebuiltin('Action(Play)')
					xbmc.executebuiltin('Action(FastForward)')
				elif count == 7:
					xbmc.executebuiltin('Action(Rewind)')
				elif count == 8:
					if playerpaused: xbmc.executebuiltin('Action(Play)')
					xbmc.executebuiltin('Action(SmallStepBack)')
				elif count == 9:
					if playercache != '100':
						'''------------------------------
						--SMOOTH-FIX-FALSE---------------
						------------------------------'''	
						smooth = "false"	
						if not "3" in printpoint: setGeneral_ConnectionScore(admin, General_ConnectionScore, "", smooth)
						General_ConnectionScore2 = getsetting('General_ConnectionScore')
						if General_ConnectionScore2 == "0": notification(addonString(225),addonString(227),"",5000) #RESET ROUTER
						elif General_CustomVAR == 5: notification(addonString(235),addonString(234),"",7000) #NITUV LO TAKIN
						elif General_CustomVAR != 5: notification(addonString(233),addonString(236),"",10000) #HOMES BESHART ZEH
						printpoint = printpoint + "3"
				printpoint = printpoint + "5"
				'''---------------------------'''
		if count == 1:
			'''------------------------------
			--APPLY-ONCE---------------------
			------------------------------'''
			notification(addonString(270),addonString(271),"",2000)
			'''---------------------------'''
		elif smooth != "true" and count > 2 and count < 9 and playercache == '100':
			'''------------------------------
			--SMOOTH-TRUE--------------------
			------------------------------'''	
			smooth = "true"
			count = 7
			notification(addonString(272),addonString(273),"",2000)
			'''---------------------------'''
		elif count == 5 and playercache != '100':
			'''------------------------------
			--SMOOTH-?-----------------------
			------------------------------'''	
			smooth = "fix"
			notification('$LOCALIZE[79505]','$LOCALIZE[31407]',"",10000)
			if playerpaused: xbmc.executebuiltin('Action(Play)')
			'''---------------------------'''
	#if "2" in printpoint and not videoplayerhassubtitles and (istv2 or ismovie2): xbmc.executebuiltin('ActivateWindow(subtitlesearch)')
	#if General_CustomVAR == "6" or General_CustomVAR == "20": openDialogOK("")
	print printfirst + "testStream" + space + "smooth" + space2 + smooth + space + "count" + space2 + countS + space + "LV_" + printpoint + space3
	'''---------------------------'''
	
def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)
	
def dialogyesno(heading,line1):
	'''------------------------------
	---DIALOG-YESNO------------------
	------------------------------'''
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	returned = 'skip'
	if dialog.yesno(heading,line1): returned = 'ok'
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "dialogyesno" + space2 + heading + space3 + line1 + "( " + returned + " )"
	return returned
	'''---------------------------'''

def notification(heading, message, icon, time):
	'''------------------------------
	---Show a Notification alert.----
	------------------------------'''
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
	if (not "+" in heading and "addonString(" in heading) and (not "+" in message and "addonString(" in message): print printfirst + "notification" + space2 + heading + space3 + message + space + time
	else:
		print printfirst + "notification" + "..."
	'''---------------------------'''
	
def getDialogW(custom):
	'''------------------------------
	---DIALOG-Windows----------------
	------------------------------'''
	from variables import Current_Dialog
	dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
	dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
	dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
	dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
	dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
	dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
	dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
	videofullscreenW = xbmc.getCondVisibility('Window.IsVisible(VideoFullScreen.xml)')
	
	'''---------------------------'''
	if dialogselectW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)') ### Skin.HasSetting(Admin) | !StringCompare(Control.GetLabel(1),Genesis)
		dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(100)') ###CUSTOM
		dialogMessage = ""
		dialogMessageCustom = ""
		returned_Dialog = "dialogselectW"
		'''---------------------------'''
	elif dialogyesnoW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)') ###
		dialogHeaderCustom = ""
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(9)') ###TEXTBOX
		dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		returned_Dialog = "dialogyesnoW"
		'''---------------------------'''
	elif dialogkeyboardW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(311)')
		dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(317)')
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(312)') ###EDIT
		dialogMessageCustom = "" ###NONE
		returned_Dialog = "dialogkeyboardW"
		'''---------------------------'''
	elif dialogprogressW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)')
		dialogHeaderCustom = ""
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(9)') ###TEXTBOX
		dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		returned_Dialog = "dialogprogressW"
		'''---------------------------'''
	elif dialogbusyW:
		dialogHeader = "" ###NONE
		dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(100)') ###CUSTOM
		dialogMessage = "" ###NONE
		dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		returned_Dialog = "dialogbusyW"
		'''---------------------------'''
	elif dialogokW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)') ### Skin.HasSetting(Admin) | StringCompare(Control.GetLabel(100),) | StringCompare(Control.GetLabel(1),$LOCALIZE[19240])
		dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(100)') ###CUSTOM
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(9)') ###TEXTBOX
		dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		returned_Dialog = "dialogokW"
		'''---------------------------'''
	elif dialogsubtitlesW:
		dialogHeader = ""
		dialogHeaderCustom = ""
		dialogMessage = xbmc.getInfoLabel('Container(120).ListItem.Label2') ###FILE NAME
		dialogMessageCustom = xbmc.getInfoLabel('Container(120).ListItem.Label') ###FILE LANGUAGE
		returned_Dialog = "dialogsubtitlesW"
		'''---------------------------'''
	elif videofullscreenW:
		dialogHeader = ""
		dialogHeaderCustom = ""
		dialogMessage = ""
		dialogMessageCustom = ""
		returned_Dialog = "videofullscreenW"
		'''---------------------------'''
	else:
		'''------------------------------
		---NOTHING-SPECIFIC--------------
		------------------------------'''
		dialogHeader = ""
		dialogHeaderCustom = ""
		dialogMessage = ""
		dialogMessageCustom = ""
		returned_Dialog = ""
		'''---------------------------'''
		
	if custom == "dialog":
		setsetting_custom1('script.htpt.refresh','Current_Dialog',returned_Dialog)
		return returned_Dialog

	elif custom == "header":
		returned_Header = dialogHeader
		return returned_Header
	
	elif custom == "message":
		returned_Message = dialogMessage
		return returned_Message
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if returned_Dialog != "" or admin: print printfirst + "getDialogW" + space2 + "Current_Dialog" + space2 + Current_Dialog + " - " + returned_Dialog + space + dialogHeader + space3 + dialogHeaderCustom + space3 + dialogMessage + space3 + dialogMessageCustom + space3

'''------------------------------
---DEFAULT-----------------------
------------------------------'''
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
	line3 = str(line3.encode('utf-8'))

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

def get_daynow(custom):
	daynow = datenow.strftime("%a")
	daynowS = str(daynow)
	return daynowS

def get_timenow(custom):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	customS = str(custom)
	timenow = datetime.datetime.now()
	timenow3 = timenow.strftime("%H")
	timenow3S = str(timenow3)
	timenow3N = int(timenow3)
	'''---------------------------'''
	if timenow3N > 03 and timenow3N < 12: timezone = "A"
	elif timenow3N > 11 and timenow3N < 20: timezone = "B"
	elif timenow3N > 19 or timenow3N < 04: timezone = "C"
	if admin: notification("get_timenow",timenow3S + timezone,"",1000)
	if custom == 1:
		'''------------------------------
		---TIMEZONE----------------------
		------------------------------'''
		return timezone
		'''---------------------------'''
	else:
		return "NONE"
		
def addonsettings(name, addon,skinsettingS, skinsetting2S, usernameS, passwordS, set3,opt1,opt2,opt3):
	'''------------------------------
	---SET-USERNAME-AND-PASSWORD-----
	------------------------------'''
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	setsetting_custom          = xbmcaddon.Addon(addon).setSetting
	
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	skinsetting = xbmc.getInfoLabel('Skin.HasSetting('+ skinsettingS +')')
	skinsetting2 = xbmc.getInfoLabel('Skin.String('+ skinsetting2S +')')
	#if setting_custom == truestr: setting_custom = "true"
	#else: setting_custom = "false"
	try: skinsetting2N = int(skinsetting2)
	except: skinsetting2N = 0
	username = getsetting_custom(usernameS)
	password = getsetting_custom(passwordS)
	setting3 = getsetting_custom(set3)
	printpoint = ""
	'''---------------------------'''
	if (skinsetting or id9str == 'Trial' or id2str == datenowS) and usernameS != "" and passwordS != "":
		if admin: notification("test0","","",1000)
		if ('htpt' in username and not "finalmakerr" in idstr) and idstr != username and id9str != 'Trial' and id2str != datenowS:
			'''------------------------------
			---SET-DEFAULT-------------------
			------------------------------'''
			setsetting_custom(usernameS,idstr)
			setsetting_custom(passwordS,idpstr)
			printpoint = printpoint + "1"
			if admin: notification("test1","","",1000)
			'''---------------------------'''
		elif id9str == 'Trial' or id2str == datenowS:
			'''------------------------------
			---SET-TRIAL---------------------
			------------------------------'''
			setsetting_custom(usernameS,idtrial)
			setsetting_custom(passwordS,idp2str)
			printpoint = printpoint + "2"
			if admin: notification("test2","","",1000)
			'''---------------------------'''
		elif skinsetting and ((username == "" or password == "") or skinsetting2 == "0"):
			'''------------------------------
			---SET-NONE----------------------
			------------------------------'''
			setsetting_custom(usernameS,"")
			setsetting_custom(passwordS,"")
			printpoint = printpoint + "5"
			if admin: notification("test1.2","","",1000)
			'''---------------------------'''
		elif skinsetting:
			'''------------------------------
			---NO-CHANGES--------------------
			------------------------------'''
			printpoint = printpoint + "6"
			if admin: notification("test1.3","","",1000)
			'''---------------------------'''
	else:
		'''------------------------------
		---NO-ACCOUNT-OR-TRIAL-----------
		------------------------------'''
		daynowS = get_daynow(1)
		timezone = get_timenow(1)
		General_TimeZone = getsetting('General_TimeZone')
		if name == 'REALDEBRID' and (daynowS == opt1 or General_TimeZone != opt2):
			'''------------------------------
			---SET-NONE----------------------
			------------------------------'''
			setsetting_custom(usernameS,"")
			setsetting_custom(passwordS,"")
			printpoint = printpoint + "3"
			'''---------------------------'''
		else:
			'''------------------------------
			---SET-DEFAULT-------------------
			------------------------------'''
			setsetting_custom(usernameS,idstr)
			setsetting_custom(passwordS,idpstr)
			printpoint = printpoint + "4"
			'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if printpoint == "0": print printfirst + "addonsettings LV_0" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "?"
	if printpoint == "1": print printfirst + "addonsettings LV_1" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "RESET"
	elif printpoint == "2": print printfirst + "addonsettings LV_2" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "Trial / DATENOW"
	elif printpoint == "3": print printfirst + "addonsettings LV_3" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "NONE" + space + "ID: " + idstr + space + "daynowS" + space2 + daynowS + space + "timenow3S" + space2 + timenow3S + space + "datenowS" + space2 + datenowS + space + "timezone" + space2 + timezone
	elif printpoint == "4": print printfirst + "addonsettings LV_4" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "DEFAULT" + space + "ID: " + idstr + space + "timezone" + space2 + timezone
	elif printpoint == "5": print printfirst + "addonsettings LV_5" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "skinsetting2" + space2 + skinsetting2 + "UNREGISTER"
	elif printpoint == "6": print printfirst + "addonsettings LV_6" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "REGISTERED"
	elif printpoint == "": print printfirst + "addonsettings LV_0-Error?"
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
	from variables import admin, truestr

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
	if setting1 != set1v or admin: print printfirst + "setSkinSetting" + space3 + custom + space + set1 + space2 + setting1 + " - " + set1v + space3 + "( " + "setting2" + space2 + setting2 + " ) "
	'''---------------------------'''

def setSkinSetting5(custom,set1,set1v,set2,set2v,set3,set3v,set4,set4v,set5,set5v):
	'''------------------------------
	---SET-SKIN-SETTING-5------------
	------------------------------'''
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
	print printfirst + "setSkinSetting5" + space2 + set1 + space + set2 + space + set3 + space + set4 + space + set5 + space3
	'''---------------------------'''
	
def calculate(addon,set1,custom, opt):
	'''------------------------------
	---RETURN-CALCULATE-NUMBER-------
	------------------------------'''	
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
	if admin: print printfirst + "calculate" + space + addon + space + set1 + space + "set1v" + space + set1v + space + "set2v" + space + set2v
	return set1v
	'''---------------------------'''
	
	
	
'''------------------------------
---CUSTOM------------------------
------------------------------'''

def setGeneral_TimeZone(General_ScriptON):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	General_TimeZone = getsetting('General_TimeZone')
	timezone = get_timenow(1)
	'''---------------------------'''
	if General_TimeZone != timezone:
		'''------------------------------
		---TIMEZONE-SWIFT----------------
		------------------------------'''
		setsetting_custom1('script.htpt.refresh','General_TimeZone',timezone)
		GenesisSettings("2")
		General_TimeZone2 = getsetting('General_TimeZone')
		
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if General_TimeZone != timezone: print printfirst + "setGeneral_TimeZone" + space2 + General_TimeZone + " - " + General_TimeZone2 + " (" + timezone + " )" + space3

def findvar(what):
	pass

def setCurrent_Year(General_ScriptON, Current_Name, Current_M_T2):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	Current_Year = getsetting('Current_Year')
	listitemyear = xbmc.getInfoLabel('ListItem.Year')
	listitemyear2 = Current_Name[-6:]
	listitemyear2 = str(listitemyear2)
	listitemyear2 = listitemyear2.replace("(","")
	listitemyear2 = listitemyear2.replace(")","")
	listitemyear2len = len(listitemyear2)
	listitemyear2len = str(listitemyear2len)
	'''---------------------------'''
	
	if General_ScriptON == "true":
		'''------------------------------
		---Current_Year-SETUP------------
		------------------------------'''
		if listitemyear != "": setsetting_custom1('script.htpt.refresh','Current_Year',listitemyear)
		elif listitemyear2len == "4": setsetting_custom1('script.htpt.refresh','Current_Year',listitemyear2)
		elif listitemyear2len != "4" and listitemyear2len != "": print printfirst + "listitemyear2len" + " Error " + listitemyear2len
		'''---------------------------'''
	elif General_ScriptON == "false":
		'''------------------------------
		---Current_Year-HISTORY----------
		------------------------------'''
		if Current_Year != "":
			if Current_M_T2 == "0":
				'''------------------------------
				---ismovie-----------------------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','LastMovie_Year',Current_Year)
				'''---------------------------'''
			elif Current_M_T2 == "1":
				'''------------------------------
				---istv--------------------------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','LastTV_Year',Current_Year)
				'''---------------------------'''
			setsetting_custom1('script.htpt.refresh','Current_Year',"")

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if General_ScriptON == "true": print printfirst + space + "setCurrent_Year_" + General_ScriptON + space2 + "listitemyear2 =" + listitemyear2 + " (" + listitemyear2len + ") " + "listitemyear=" + listitemyear
	elif General_ScriptON == "false": print printfirst + space + "setCurrent_Year_" + General_ScriptON + space2 + "Current_Year" + space2 + Current_Year + space + "Current_M_T2" + space2 + Current_M_T2
	if admin: notification(listitemyear2 + " - " + listitemyear,"","",5000)
	
def setGeneral_Refresh(General_ScriptON):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import getsetting
	General_Refresh = getsetting('General_Refresh')

	if General_Refresh != "":
		xbmc.executebuiltin('RunScript(script.htpt.refresh)')
		xbmc.sleep(500)
	elif General_Refresh == "":
		pass
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	General_Refresh2 = getsetting('General_Refresh')
	if General_Refresh != General_Refresh2: print printfirst + "setGeneral_Refresh" + space2 + General_Refresh + " - " + General_Refresh2 + space3
	'''---------------------------'''
	
def setGeneral_StartWindow(General_ScriptON, General_StartWindow):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import getsetting
	homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
	myvideonavW = xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)')
	

	if General_ScriptON == "true":
		if myvideonavW: setsetting_custom1('script.htpt.refresh','General_StartWindow',"0")
		elif homeW: setsetting_custom1('script.htpt.refresh','General_StartWindow',"1")
	elif General_ScriptON == "false":
		setsetting_custom1('script.htpt.refresh','General_StartWindow',"")
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	General_StartWindow2 = getsetting('General_StartWindow')
	homeW = str(homeW)
	myvideonavW = str(myvideonavW)
	
	if admin: print printfirst + "setGeneral_StartWindow" + space2 + General_StartWindow + " - " + General_StartWindow2 + space3 + "General_ScriptON" + space2 + General_ScriptON + space3 + "myvideonavW/homeW" + space2 + myvideonavW + "/" + homeW + space3
	'''---------------------------'''
	
def setCurrent_M_T(General_StartWindow):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import containerfolderpath
	#from variables import istv4, ismovie4, istv4S, ismovie4S
	#from variables import istv, ismovie, istvS, ismovieS
	#from variables import dialogselectsources3
	dialogselectsources3 = xbmc.getInfoLabel('Skin.String(DialogSelectSources3)')
	istv = (xbmc.getInfoLabel('ListItem.TVShowTitle') != "" and xbmc.getInfoLabel('ListItem.Season') != "" and xbmc.getInfoLabel('ListItem.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
	istvS = str(istv)
	ismovie = (xbmc.getInfoLabel('ListItem.Year') != "" or xbmc.getInfoLabel('ListItem.Country') != "" or xbmc.getInfoLabel('ListItem.Tagline') != "") and not istv
	ismovieS = str(ismovie)
	
	istv4 = " S" in dialogselectsources3 and " E" in dialogselectsources3
	istv4S = str(istv4)
	ismovie4 = " (" in dialogselectsources3 and ")" in dialogselectsources3 and not istv4
	ismovie4S = str(ismovie4)
	'''---------------------------'''
	if General_StartWindow == "0":
		'''------------------------------
		---LIBRARY-----------------------
		------------------------------'''
		if ismovie: setsetting_custom1('script.htpt.refresh','Current_M_T',"0")
		elif istv: setsetting_custom1('script.htpt.refresh','Current_M_T',"1")
		'''---------------------------'''	
	elif General_StartWindow == "1":
		'''------------------------------
		---HOME--------------------------
		------------------------------'''
		if ismovie4: setsetting_custom1('script.htpt.refresh','Current_M_T',"0")
		elif istv4: setsetting_custom1('script.htpt.refresh','Current_M_T',"1")
		
		'''---------------------------'''	
	elif General_StartWindow == "":
		'''------------------------------
		---NONE--------------------------
		------------------------------'''
		setsetting_custom1('script.htpt.refresh','Current_M_T',"")
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "setCurrent_M_T" + space2 + "ismovieS" + space2 + ismovieS + space + "istvS" + space2 + istvS + space + "istv4S" + space2 + istv4S + space + "ismovie4S" + space2 + ismovie4S + space + "General_StartWindow" + space2 + General_StartWindow + space3
	'''---------------------------'''
			
def topvideoinformation(General_StartWindow,Current_M_T):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	topvideoinformation1 = xbmc.getInfoLabel('$VAR[TopVideoInformation1]')
	topvideoinformation2 = xbmc.getInfoLabel('$VAR[TopVideoInformation2]')	
	topvideoinformation3 = xbmc.getInfoLabel('$VAR[TopVideoInformation3]')
	topvideoinformation4 = xbmc.getInfoLabel('$VAR[TopVideoInformation4]')
	topvideoinformation5 = xbmc.getInfoLabel('$VAR[TopVideoInformation5]')
	topvideoinformation6 = xbmc.getInfoLabel('$VAR[TopVideoInformation6]')
	topvideoinformation7 = xbmc.getInfoLabel('$VAR[TopVideoInformation7]')
	topvideoinformation8 = xbmc.getInfoLabel('$VAR[TopVideoInformation8]')
	topvideoinformation9 = xbmc.getInfoLabel('$VAR[TopVideoInformation9]')
	''''''
	topvideoinformation1a = xbmc.getInfoLabel('Skin.String(TopVideoInformation1)')
	topvideoinformation2a = xbmc.getInfoLabel('Skin.String(TopVideoInformation2)')	
	topvideoinformation3a = xbmc.getInfoLabel('Skin.String(TopVideoInformation3)')
	topvideoinformation4a = xbmc.getInfoLabel('Skin.String(TopVideoInformation4)')
	topvideoinformation5a = xbmc.getInfoLabel('Skin.String(TopVideoInformation5)')
	topvideoinformation6a = xbmc.getInfoLabel('Skin.String(TopVideoInformation6)')
	topvideoinformation7a = xbmc.getInfoLabel('Skin.String(TopVideoInformation7)')
	topvideoinformation8a = xbmc.getInfoLabel('Skin.String(TopVideoInformation8)')
	topvideoinformation9a = xbmc.getInfoLabel('Skin.String(TopVideoInformation9)')

	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	'''---------------------------'''
	if Current_M_T == "0":
		'''------------------------------
		---ismovie-----------------------
		------------------------------'''
		pass
		'''---------------------------'''	
	elif Current_M_T == "1":
		'''------------------------------
		---istv--------------------------
		------------------------------'''
		if General_StartWindow == "0":
			'''------------------------------
			---LIBRARY-----------------------
			------------------------------'''
			if admin: xbmc.executebuiltin('Notification(Admin, '+ topvideoinformation7 +',1000)')
			if topvideoinformation1 and not topvideoinformation1a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation1, '+ topvideoinformation1 +')')
			if topvideoinformation2 and not topvideoinformation2a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation2, '+ topvideoinformation2 +')')
			if topvideoinformation3 and not topvideoinformation3a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation3, '+ topvideoinformation3 +')')
			#if topvideoinformation4 and not topvideoinformation4a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation4, '+ topvideoinformation4 +')')
			if topvideoinformation5 and not topvideoinformation5a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation5, '+ topvideoinformation5 +')')
			if topvideoinformation6 and not topvideoinformation6a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation6, '+ topvideoinformation6 +')')
			if topvideoinformation7 and not topvideoinformation7a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation7, '+ topvideoinformation7 +')')
			if topvideoinformation8 and not topvideoinformation8a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation8, '+ topvideoinformation8 +')')
			#if topvideoinformation9 and not topvideoinformation9a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation9, '+ topvideoinformation9 +')')
			
			'''------------------------------
			---PRINT-END---------------------
			------------------------------'''
			print printfirst + "topvideoinformation" + space2 + "setting TopVideoInformation" + "(" + General_StartWindow + ") "
			'''---------------------------'''	
	elif Current_M_T == "":
		'''------------------------------
		---NONE--------------------------
		------------------------------'''
		if topvideoinformation8a != topvideoinformation8:
			'''------------------------------
			---STRING vs CURRENT TITLE-------
			------------------------------'''
			if topvideoinformation1a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation1,)')
			if topvideoinformation2a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation2,)')
			if topvideoinformation3a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation3,)')
			if topvideoinformation4a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation4,)')
			if topvideoinformation5a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation5,)')
			if topvideoinformation6a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation6,)')
			if topvideoinformation7a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation7,)')
			if topvideoinformation8a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation8,)')
			if topvideoinformation9a: xbmc.executebuiltin('Skin.SetString(TopVideoInformation9,)')
			'''------------------------------
			---PRINT-END---------------------
			------------------------------'''
			if admin: print printfirst + "topvideoinformation" + space2 + "clear TopVideoInformation"
			'''---------------------------'''
			
def setCurrent_Name(Current_Name2,Current_Source2,Current_M_T2,General_StartWindow):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import admin
	Current_M_T = getsetting('Current_M_T')
	dialogselectsources3 = xbmc.getInfoLabel('Skin.String(DialogSelectSources3)')
	'''---------------------------'''
	if Current_M_T == "0":
		'''------------------------------
		---ismovie-----------------------
		------------------------------'''
		setsetting_custom1('script.htpt.refresh','Current_Name',dialogselectsources3)
		setSkinSetting("0",'DialogSelectSources5',dialogselectsources3)
		'''---------------------------'''
		if General_StartWindow == "0":
			'''------------------------------
			---LIBRARY-----------------------
			------------------------------'''
			pass
			'''---------------------------'''	
		elif General_StartWindow == "1":
			'''------------------------------
			---HOME--------------------------
			------------------------------'''
			pass
			'''---------------------------'''	
		
	elif Current_M_T == "1":
		'''------------------------------
		---istv--------------------------
		------------------------------'''
		setsetting_custom1('script.htpt.refresh','Current_Name',dialogselectsources3)
		setSkinSetting("0",'DialogSelectSources5',dialogselectsources3)
		'''---------------------------'''
		if General_StartWindow == "0":
			'''------------------------------
			---LIBRARY-----------------------
			------------------------------'''
			pass
			'''---------------------------'''	
		elif General_StartWindow == "1":
			'''------------------------------
			---HOME--------------------------
			------------------------------'''
			pass
			'''---------------------------'''
	elif Current_M_T == "" and Current_Name2 != "":
		'''------------------------------
		---NONE-& Current_Name-----------
		------------------------------'''
		setsetting_custom1('script.htpt.refresh','Current_Name',"")
		setSkinSetting("0",'DialogSelectSources3',"")
		setsetting_custom1('script.htpt.refresh','Current_Source',"")
		setSkinSetting("0",'DialogSelectSources',"")
		if Current_M_T2 == "0":
			'''------------------------------
			---LastMovie_Name-------------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','LastMovie_Name',Current_Name2)
			setsetting_custom1('script.htpt.refresh','LastMovie_Source',Current_Source2)
			'''---------------------------'''	
		elif Current_M_T2 == "1":
			'''------------------------------
			---LastTV_Name-------------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','LastTV_Name',Current_Name2)
			setsetting_custom1('script.htpt.refresh','LastTV_Source',Current_Source2)
			'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	Current_Name2 = getsetting('Current_Name')
	Current_M_T2 = getsetting('Current_M_T')
	print printfirst + "setCurrent_Name" + space2 + Current_Name + " - " + Current_Name2 + space + "M_T" + space2 + Current_M_T + " - " + Current_M_T2
	'''---------------------------'''
	
def setLast_Subtitle(Current_M_T,Current_M_T2,Current_Name2):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import getsetting, addonString
	from variables import LastMovie_Name, LastTV_Name
	from variables import Current_Subtitle, Current_Subtitle1, Current_Subtitle2, Current_Subtitle3, Current_Subtitle4, Current_Subtitle5, Current_Subtitle6, Current_Subtitle7, Current_Subtitle8, Current_Subtitle9, Current_Subtitle10
	'''---------------------------'''
	if Current_M_T == "":
		'''------------------------------
		---NONE--------------------------
		------------------------------'''
		setSkinSetting("0",'dialogsubtitles',"")
		setSkinSetting("0",'dialogsubtitles2',"")
		setSkinSetting5("0",'dialogsubtitlesna1',"",'dialogsubtitlesna2',"",'dialogsubtitlesna3',"",'dialogsubtitlesna4',"",'dialogsubtitlesna5',"")
		setSkinSetting5("0",'dialogsubtitlesna6',"",'dialogsubtitlesna7',"",'dialogsubtitlesna8',"",'dialogsubtitlesna9',"",'dialogsubtitlesna10',"")
		
		if Current_M_T2 == "0":
			'''------------------------------
			---ismovie-----------------------
			------------------------------'''
			if Current_Name2 == LastMovie_Name:
				setsetting_custom1('script.htpt.refresh','LastMovie_Subtitle',Current_Subtitle)
				addonsettings2('script.htpt.refresh','LastMovie_Subtitle1',Current_Subtitle1,'LastMovie_Subtitle2',Current_Subtitle2,'LastMovie_Subtitle3',Current_Subtitle3,'LastMovie_Subtitle4',Current_Subtitle4,'LastMovie_Subtitle5',Current_Subtitle5)
				addonsettings2('script.htpt.refresh','LastMovie_Subtitle6',Current_Subtitle6,'LastMovie_Subtitle7',Current_Subtitle7,'LastMovie_Subtitle8',Current_Subtitle8,'LastMovie_Subtitle9',Current_Subtitle9,'LastMovie_Subtitle10',Current_Subtitle10)
			else:
				print printfirst + "Error" + space2 + "Current_Name2" + space2 + Current_Name2 + " != " + "LastMovie_Name" + space2 + LastMovie_Name + space3
				'''---------------------------'''	
		elif Current_M_T2 == "1":
			'''------------------------------
			---istv--------------------------
			------------------------------'''
			if Current_Name2 == LastTV_Name:
				setsetting_custom1('script.htpt.refresh','LastTV_Subtitle',Current_Subtitle)
				addonsettings2('script.htpt.refresh','LastTV_Subtitle1',Current_Subtitle1,'LastTV_Subtitle2',Current_Subtitle2,'LastTV_Subtitle3',Current_Subtitle3,'LastTV_Subtitle4',Current_Subtitle4,'LastTV_Subtitle5',Current_Subtitle5)
				addonsettings2('script.htpt.refresh','LastTV_Subtitle6',Current_Subtitle6,'LastTV_Subtitle7',Current_Subtitle7,'LastTV_Subtitle8',Current_Subtitle8,'LastTV_Subtitle9',Current_Subtitle9,'LastTV_Subtitle10',Current_Subtitle10)
			else:
				print printfirst + "Error" + space2 + "Current_Name2" + space2 + Current_Name2 + " != " + "LastTV_Name" + space2 + LastTV_Name + space3
				'''---------------------------'''
	else:
		pass
			
		
		
		
	print printfirst + "setLast_Subtitle" + space2 + "Current_M_T" + space2 + Current_M_T + "Current_M_T2" + space2 + Current_M_T2 + "Current_Name2" + space2 + Current_Name2 + space3
	'''---------------------------'''

def setGeneral_Connected(connectedv2):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import systemplatformwindows, getsetting, setsetting
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
	connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
	General_ScriptON = getsetting('General_ScriptON')
	General_CountWait = getsetting('General_CountWait')
	General_Connected = getsetting('General_Connected')
	General_ConnectedN = int(General_Connected)
	printpoint = ""
	'''---------------------------'''
	
	if not systemplatformwindows:
		printpoint = printpoint + "1"
		if General_ScriptON == "true":
			'''------------------------------
			---General_ScriptON-ON-----------
			------------------------------'''
			printpoint = printpoint + "2"
			if connected2 or connected3:
				'''------------------------------
				---NETWORK-IS-UP-----------------
				------------------------------'''
				printpoint = printpoint + "3"
				if not connected:
					'''------------------------------
					---PING-FAILED-------------------
					------------------------------'''
					printpoint = printpoint + "4"
					calculate('script.htpt.refresh','General_Connected',"1","")
					'''---------------------------'''
				else:
					'''------------------------------
					---PING-OK-----------------------
					------------------------------'''
					printpoint = printpoint + "5"
					'''---------------------------'''
			else:
				'''------------------------------
				---NETWORK-IS-DOWN-----------------
				------------------------------'''
				printpoint = printpoint + "6"
				'''---------------------------'''
		else:
			'''------------------------------
			---General_ScriptON-OFF----------
			------------------------------'''
			#General_CountWait
			#if General_ConnectedN > 0: dialogok(
			printpoint = printpoint + "7"
			setsetting_custom1('script.htpt.refresh','General_Connected',"0")
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		General_Connected2 = getsetting(General_Connected)
		if General_Connected2 != General_Connected: print printfirst + "setGeneral_Connected_LV" + printpoint + space2 + General_Connected + " - " + General_Connected2 + space3
		'''---------------------------'''
		
def setGeneral_CustomVAR(General_CustomVAR, General_ScriptON, Current_Dialog2):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import systemplatformwindows, getsetting, setsetting
	from variables import SE_ColorGreen, SE_ColorGreen2, SE_ColorGreen3, SE_ColorPurple, SE_ColorPurple2, SE_ColorPurple3
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	networkgatewayaddress = xbmc.getInfoLabel('Network.GatewayAddress')
	networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
	'''---------------------------'''
	AutoPlay_Pause = getsetting('AutoPlay_Pause')
	Current_Dialog = getsetting('Current_Dialog')
	Current_Source = getsetting('Current_Source')
	General_ConnectionScore = getsetting('General_ConnectionScore')
	General_ConnectionScoreN = int(General_ConnectionScore)
	General_CountWait = getsetting('General_CountWait')
	General_CountWaitN = int(General_CountWait)
	General_Connected = getsetting('General_Connected')
	General_ConnectedN = int(General_Connected)
	General_ConnectedN_ = General_ConnectedN * 10
	General_ConnectedN_S = str(General_ConnectedN_)
	'''---------------------------'''
	
	if General_ScriptON == "false":
		if General_CustomVAR != "" and Current_Dialog == "" and Current_Dialog2 == "":
			'''------------------------------
			---CustomVAR-""------------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','General_CustomVAR',"")
			'''---------------------------'''
	elif General_ScriptON == "true":
		if networkgatewayaddress == "" or networkipaddress == "":
			'''------------------------------
			---NO-NETWORK-(20)---------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','General_CustomVAR',"20")
			'''---------------------------'''
		elif Current_Dialog2 == "dialogselectW" and Current_Dialog == "dialogokW":
			'''------------------------------
			---ACTION-ABORTED-(1)------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','General_CustomVAR',"1")
			'''---------------------------'''
		elif General_CustomVAR != "1":
			if (Current_Dialog2 == "dialogselectW" and Current_Dialog != "dialogokW" and Current_Source != "") or Current_Dialog == "dialogprogressW": 
				'''------------------------------
				---SOURCES-NOT-FOUND-(4)---------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','General_CustomVAR',"4")
				'''---------------------------'''
			elif Current_Dialog == "dialogkeyboardW":
				'''------------------------------
				---SCREEN-VALIDATION-FAILED-(2)--
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','General_CustomVAR',"2")
				'''---------------------------'''
			elif General_ConnectedN_ > General_CountWaitN:
				'''------------------------------
				---INTERNET-DROP-(6)-------------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','General_CustomVAR',"6")
				'''---------------------------'''
			elif General_CountWaitN > 0 and General_CountWaitN < 2:
				'''------------------------------
				---SOURCES-NOT-FOUND-(4)---------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','General_CustomVAR',"4")
				'''---------------------------'''
			elif Current_Dialog == "dialogbusyW" and General_CountWaitN < 5:
				'''------------------------------
				---UNABLE-TO-STREAM-(...)--------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','General_CustomVAR',"...")
				'''---------------------------'''
			elif (General_CountWaitN > 5 and General_CountWaitN < 30):
				if Current_Dialog == "dialogprogressW" or Current_Dialog == "dialogbusyW":
					if SE_ColorGreen in Current_Source or SE_ColorGreen2 in Current_Source or SE_ColorGreen3 in Current_Source:
						'''------------------------------
						---OVERLOADED-HOST-SERVER-(5)----
						------------------------------'''
						setsetting_custom1('script.htpt.refresh','General_CustomVAR',"5")
						'''---------------------------'''
					else:
						'''------------------------------
						---UNABLE-TO-STREAM-(...)--------
						------------------------------'''
						setsetting_custom1('script.htpt.refresh','General_CustomVAR',"...")
						'''---------------------------'''
						
			elif General_CountWaitN > 30 and General_CustomVAR != "3":
				'''------------------------------
				---SLOW-SERVER---(3/5)-----------
				------------------------------'''
				if General_CountWaitN == 40 and (General_ConnectionScoreN < 2 or admin): notification(addonString(239),addonString(248),"",5000)
				if Current_Dialog == "dialogprogressW" and General_ConnectionScoreN < 4 and AutoPlay_Pause == "true":
					xbmc.executebuiltin('Action(Select)')
					xbmc.sleep(1000)
				'''---------------------------'''
				if General_CustomVAR != "5": setsetting_custom1('script.htpt.refresh','General_CustomVAR',"3")
				#elif General_CustomVAR == "5": setsetting_custom1('script.htpt.refresh','General_CustomVAR',"5")
				#xbmc.sleep(200)
				
	'''------------------------------
	---RESULT------------------------
	------------------------------'''
	General_CustomVAR2 = getsetting('General_CustomVAR')
	setSkinSetting("0",'General_CustomVAR',General_CustomVAR2)
	if General_CustomVAR != General_CustomVAR2: print printfirst + "setGeneral_CustomVAR" + space2 + General_CustomVAR + " - " + General_CustomVAR2 + space + "Current_Dialog" + space2 + Current_Dialog + " - " + Current_Dialog + space + "General_ConnectedN_S" + General_ConnectedN_S + space3
	'''---------------------------'''
	
def setGeneral_ConnectionScore(admin, General_ConnectionScore, Current_Dialog2,smooth):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import addonString, getsetting, setsetting
	#General_ConnectionScore = getsetting('General_ConnectionScore')
	notification("setGeneral_ConnectionScore=" + General_ConnectionScore,"","",2000)
	General_ConnectionScoreN = int(General_ConnectionScore)
	General_ConnectionScore2 = General_ConnectionScore
	General_ConnectionScore2N = int(General_ConnectionScore2)
	Current_Dialog = getsetting('Current_Dialog')
	General_CustomVAR = getsetting('General_CustomVAR')
	General_CountWait = getsetting('General_CountWait')
	AutoPlay_Pause = getsetting('AutoPlay_Pause')
	AutoPlay_SD = getsetting('AutoPlay_SD')
	AutoPlay_HD = getsetting('AutoPlay_HD')
	printpoint = ""
	'''---------------------------'''
	
	if not xbmc.Player().isPlayingVideo():
		printpoint = printpoint + "1"
		if Current_Dialog == "dialogokW":
			'''------------------------------
			---REDUCE-NO-VIDEO---------------
			------------------------------'''
			if General_ConnectionScoreN == 5:
				'''------------------------------
				---GENESIS-SETTINGS-RESET--------
				------------------------------'''
				GenesisSettings("0")
				xbmc.sleep(200)
				'''---------------------------'''
			if General_ConnectionScoreN > 0:
				if General_CustomVAR != "1" and General_CustomVAR != "2" and General_CustomVAR != "4" and General_CustomVAR != "20":
					'''------------------------------
					---REDUCE------------------------
					------------------------------'''
					if AutoPlay_SD or AutoPlay_HD and not AutoPlay_Pause: calculate('script.htpt.refresh','General_ConnectionScore',"2",General_ConnectionScore)
					elif General_CustomVAR == "5" or General_CustomVAR == "3": calculate('script.htpt.refresh','General_ConnectionScore',"2",General_ConnectionScore)
					General_ConnectionScore2N = General_ConnectionScoreN - 1
					printpoint = printpoint + "4"
					'''---------------------------'''
	elif xbmc.Player().isPlayingVideo():
		printpoint = printpoint + "5"
		if smooth == "false":
			'''------------------------------
			---REDUCE-VIDEO------------------
			------------------------------'''
			if General_ConnectionScoreN > 0:
				calculate('script.htpt.refresh','General_ConnectionScore',"2",General_ConnectionScore)
				General_ConnectionScore2N = General_ConnectionScoreN -1
				'''---------------------------'''
			if General_ConnectionScore2N == 0: notification(addonString(225),addonString(227),"",5000) #RESET ROUTER
			elif General_CustomVAR == 5: notification(addonString(235),addonString(234),"",5000) #NITUV LO TAKIN
			elif General_CustomVAR != 5: notification(addonString(233),addonString(236),"",10000) #HOMES BESHART ZEH
			printpoint = printpoint + "6"
			'''---------------------------'''
		elif smooth == "true":	
			'''------------------------------
			---INCREASE---------------------
			------------------------------'''
			if General_ConnectionScoreN < 5:
				calculate('script.htpt.refresh','General_ConnectionScore',"1",General_ConnectionScore)
				General_ConnectionScore2N = General_ConnectionScoreN + 1
				printpoint = printpoint + "7"
				'''---------------------------'''
			else: printpoint = printpoint + "8"
	
	General_ConnectionScore2 = str(General_ConnectionScore2N)
	setSkinSetting("0",'General_ConnectionScore',General_ConnectionScore2)
	if General_ConnectionScore != General_ConnectionScore2 or admin: print printfirst + "setGeneral_ConnectionScore_LV" + printpoint + space2 + General_ConnectionScore + " - " + General_ConnectionScore2 + space + "Current_Dialog" + space2 + Current_Dialog + space + "smooth" + space2 + smooth

def openDialogOK(Current_Dialog2):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import addonString, getsetting, setsetting
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	Current_Source = getsetting('Current_Source')
	Current_M_T = getsetting('Current_M_T')
	Current_Name = getsetting('Current_Name')
	Current_Year = getsetting('Current_Year')
	General_Connected = getsetting('General_Connected')
	General_CountWait = getsetting('General_CountWait')
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
	connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
	AutoPlay_Pause = getsetting('AutoPlay_Pause')
	AutoPlay_SD = getsetting('AutoPlay_SD')
	AutoPlay_HD = getsetting('AutoPlay_HD')
	General_CustomVAR = getsetting('General_CustomVAR')
	General_ConnectionScore = getsetting('General_ConnectionScore')
	General_ConnectionScoreN = int(General_ConnectionScore)
	'''---------------------------'''
	if admin: notification("General_CustomVAR:",General_CustomVAR,"",1000)
	if General_CustomVAR == "1":
		'''------------------------------
		---ACTION-ABORTED-(1)------------
		------------------------------'''
		if admin: notification("General_CustomVAR 1","","",1000)
		dialogok(addonString(220),"","","")
		'''---------------------------'''
	elif General_CustomVAR == "20":
		'''------------------------------
		---NO-NETWORK-(20)---------------
		------------------------------'''
		dialogok(addonString(250), addonString(251),"","")
		'''---------------------------'''
	elif General_CustomVAR == "6":
		'''------------------------------
		---INTERNET-DROP-(6)-------------
		------------------------------'''
		if connected2 and connected3:
			'''------------------------------
			---WLAN-AND-LAN------------------
			------------------------------'''
			dialogok(addonString(241) % (General_Connected, General_CountWait),addonString(242),addonString(243),"")
			'''---------------------------'''
		elif connected2:
			'''------------------------------
			---WLAN--------------------------
			------------------------------'''
			dialogok(addonString(241) % (General_Connected, General_CountWait),addonString(244),addonString(245),"")
			'''---------------------------'''
		elif connected3:
			'''------------------------------
			---LAN---------------------------
			------------------------------'''
			dialogok(addonString(241) % (General_Connected, General_CountWait),addonString(246),addonString(247),addonString(248))
			'''---------------------------'''
			
	elif General_CustomVAR == "4":
		'''------------------------------
		---SOURCES-NOT-FOUND-(4)---------
		------------------------------'''
		if Current_Source == "" and General_ConnectionScoreN == 0: dialogok(addonString(229),addonString(231),"","")
		elif Current_Year == yearnowS and Current_M_T == "0":
			'''------------------------------
			---ismovie-new-------------------
			------------------------------'''
			if AutoPlay_Pause == "false": dialogok(addonString(229),addonString(219),addonString(206),addonString(218))
			else: dialogok(addonString(229),addonString(219),addonString(206),"")
		else: dialogok(addonString(229),'[COLOR=Red]' + Current_Source + '[/COLOR]',addonString(230),"")
		'''---------------------------'''
		
	elif AutoPlay_Pause != "true" and (AutoPlay_HD == "true" or AutoPlay_SD == "true"):
		'''------------------------------
		---AUTOPLAY-HD-OFF---------------
		------------------------------'''
		if AutoPlay_HD == "true":
			'''------------------------------
			---AUTOPLAY-SD-ON-----------------
			------------------------------'''
			dialogok(addonString(204) + " (HD) ", addonString(200) + " (SD) ", '[COLOR=Yellow]' + addonString(205) + '[/COLOR]',"")
			'''---------------------------'''
		elif AutoPlay_SD == "true": 
			'''------------------------------
			---MANUALPLAY-ON-----------------
			------------------------------'''
			dialogok(addonString(204) + " (SD) ", addonString(201), '[COLOR=Yellow]' + addonString(205) + '[/COLOR]',"")
			'''---------------------------'''
		elif AutoPlay_HD == "false" and AutoPlay_SD == "false":
			'''------------------------------
			---AUTOPLAY-SD-OFF---------------
			------------------------------'''
			dialogok(addonString(204) + " (SD) ", addonString(202), '[COLOR=Yellow]' + addonString(205) + '[/COLOR]',"")
			'''---------------------------'''
			
	elif General_CustomVAR == "2":
		'''------------------------------
		---LETTER-VALIDATION-FAILED-(2)--
		------------------------------'''
		dialogok(addonString(222),addonString(223),"","")
		'''---------------------------'''
		
	elif General_ConnectionScore == "0":
		'''------------------------------
		---TURN-ROUTER-OFF-10M-----------
		------------------------------'''
		dialogok(addonString(225),addonString(226),"","")
		'''---------------------------'''
		
	elif General_CustomVAR == "5":
		'''------------------------------
		---OVERLOADED-HOST-SERVER-(5)----
		------------------------------'''
		notification("!","","",1000)
		if Current_Source != "": dialogok(addonString(229),'[COLOR=Red]' + Current_Source + '[/COLOR]',addonString(230),"")
		elif Current_Source == "": dialogok(addonString(229),addonString(231),"","")
		'''---------------------------'''
			
	elif General_CustomVAR == "...":
		'''------------------------------
		---UNABLE-TO-STREAM-(...)--------
		------------------------------'''
		if Current_Source != "": dialogok(addonString(235),'[COLOR=Red]' + Current_Source + '[/COLOR]',addonString(234),"")
		elif Current_Source == "": dialogok(addonString(235),addonString(234),"","")
		'''---------------------------'''
	elif General_CustomVAR == "3":
		'''------------------------------
		---SLOW-STREAM-------------------
		------------------------------'''
		if General_ConnectionScoreN < 2:
			'''------------------------------
			---YOUR-INTERNET-----------------
			------------------------------'''
			if Current_Source != "": dialogok(addonString(225),'[COLOR=Red]' + Current_Source + '[/COLOR]',addonString(228),"")
			elif Current_Source == "": dialogok(addonString(225),addonString(228),"","")
			'''---------------------------'''
		else:	
			'''------------------------------
			---THE-SPECIFIC-SERVER-----------
			------------------------------'''
			if Current_Source != "": dialogok(addonString(237),'[COLOR=Red]' + Current_Source + '[/COLOR]',addonString(234),"")
			elif Current_Source == "": dialogok(addonString(237),addonString(234),"","")
			'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "openDialogOK" + space2 + "General_CustomVAR" + space2 + General_CustomVAR + space3
	'''---------------------------'''
	
def RefreshSettings():
	'''------------------------------
	---script.htpt.refresh-----------
	------------------------------'''
	from variables import getsetting, setsetting
	from variables import dialogselectsources, dialogselectsources2, dialogselectsources3, dialogselectsources5
	from variables import playerhasvideo
	'''---------------------------'''
	#dialogsubtitles2 = xbmc.getInfoLabel('Skin.String(DialogSubtitles2)') ###Current_Subtitle
	#dialogsubtitlesna1 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA1)') ###Current_Subtitle2
	#dialogsubtitlesna2 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA2)')
	#dialogsubtitlesna3 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA3)')
	#dialogsubtitlesna4 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA4)')
	#dialogsubtitlesna5 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA5)')
	#dialogsubtitlesna6 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA6)')
	#dialogsubtitlesna7 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA7)')
	#dialogsubtitlesna8 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA8)')
	#dialogsubtitlesna9 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA9)')
	#dialogsubtitlesna10 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA10)')
	'''---------------------------'''
	setsetting_custom1('script.htpt.refresh','Current_Subtitle',dialogsubtitles2)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle1',dialogsubtitlesna1)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle2',dialogsubtitlesna2)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle3',dialogsubtitlesna3)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle4',dialogsubtitlesna4)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle5',dialogsubtitlesna5)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle6',dialogsubtitlesna6)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle7',dialogsubtitlesna7)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle8',dialogsubtitlesna8)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle9',dialogsubtitlesna9)
	setsetting_custom1('script.htpt.refresh','Current_Subtitle10',dialogsubtitlesna10)
	'''---------------------------'''
	
	'''------------------------------
	---General_...-------------------
	------------------------------'''
	General_Refresh = getsetting('General_Refresh')
	General_StartWindow = getsetting('General_StartWindow')
	General_TimeZone = getsetting('General_TimeZone')
	General_Connected = getsetting('General_Connected')
	'''---------------------------'''
	General_ScriptON = getsetting('General_ScriptON')
	setSkinSetting("1",'General_ScriptON',General_ScriptON)
	'''---------------------------'''
	General_ConnectionScore = getsetting('General_ConnectionScore')
	setSkinSetting("0",'General_ConnectionScore',General_ConnectionScore)
	'''---------------------------'''
	General_CountWait = getsetting('General_CountWait')
	setSkinSetting("0",'General_CountWait',General_CountWait)
	'''---------------------------'''
	General_CustomVAR = getsetting('General_CustomVAR')
	setSkinSetting("0",'General_CustomVAR',General_CustomVAR)
	'''------------------------------
	---AUTOPLAY----------------------
	------------------------------'''
	if not dialogselectW and not dialogprogressW and not dialogbusyW: GenesisSettings("4")
	#else:
		#AutoPlay_Pause = getsetting('AutoPlay_Pause')
		#AutoPlay_SD = getsetting('AutoPlay_SD')
		#AutoPlay_HD = getsetting('AutoPlay_HD')
	'''---------------------------'''
	
	'''------------------------------
	---Current_...-------------------
	------------------------------'''
	Current_M_T = getsetting('Current_M_T')
	Current_Watched = getsetting('Current_Watched')
	Current_Name = getsetting('Current_Name')
	Current_Year = getsetting('Current_Year')
	#setsetting('Current_Name',dialogselectsources5)
	Current_Source = getsetting('Current_Source')
	Current_Dialog = getsetting('Current_Dialog')
	Current_Duration = getsetting('Current_Duration')
	Current_RefreshPoint = getsetting('Current_RefreshPoint')
	#setsetting('Current_Source',dialogselectsources2)
	#setSkinSetting("0",'DialogSelectSources2',dialogselectsources)
	'''---------------------------'''
	
	'''------------------------------
	---LastMovie_...-----------------
	------------------------------'''
	LastMovie_Name = getsetting('LastMovie_Name')
	LastMovie_Year = getsetting('LastMovie_Year')
	LastMovie_Source = getsetting('LastMovie_Source')
	'''---------------------------'''
	
	'''------------------------------
	---LastTV_...--------------------
	------------------------------'''
	LastTV_Name = getsetting('LastTV_Name')
	LastTV_Year = getsetting('LastTV_Year')
	LastTV_Source = getsetting('LastTV_Source')
	'''---------------------------'''
	
	'''------------------------------
	---SE_Color...-------------------
	------------------------------'''
	#setsetting_custom1('script.htpt.refresh','SE_ColorRed',"NONE")
	#setSkinSetting("0",'SE_ColorRed',SE_ColorRed)
	#setsetting_custom1('script.htpt.refresh','SE_ColorRed2',"BILLIONUPLOADS")
	#setSkinSetting("0",'SE_ColorRed2',SE_ColorRed2)
	#setsetting_custom1('script.htpt.refresh','SE_ColorRed3',"NONE")
	#setSkinSetting("0",'SE_ColorRed3',SE_ColorRed3)
	'''---------------------------'''
	#setsetting_custom1('script.htpt.refresh','SE_ColorGreen',"ORORO")
	#setSkinSetting("0",'SE_ColorGreen',SE_ColorGreen)
	#setsetting_custom1('script.htpt.refresh','SE_ColorGreen2',"VK")
	#setSkinSetting("0",'SE_ColorGreen2',SE_ColorGreen2)
	#setsetting_custom1('script.htpt.refresh','SE_ColorGreen3',"NONE")
	#setSkinSetting("0",'SE_ColorGreen3',SE_ColorGreen3)
	'''---------------------------'''
	#setsetting_custom1('script.htpt.refresh','SE_ColorPurple',"REALDEBRID")
	#setSkinSetting("0",'SE_ColorPurple',SE_ColorPurple)
	#setsetting_custom1('script.htpt.refresh','SE_ColorPurple2',"NONE")
	#setSkinSetting("0",'SE_ColorPurple2',SE_ColorPurple2)
	#setsetting_custom1('script.htpt.refresh','SE_ColorPurple3',"NONE")
	#setSkinSetting("0",'SE_ColorPurple3',SE_ColorPurple3)
	'''---------------------------'''		
	xbmc.sleep(500) ###For skinsettings to take effect
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "RefreshSettings" + space2 + "AutoPlay_Pause" + space2 + AutoPlay_Pause + space + "General_ScriptON" + space2 + General_ScriptON
	'''---------------------------'''
	
def GenesisSettings(custom):
	'''------------------------------
	---plugin.video.genesis----------
	------------------------------'''
	from variables import getsetting, setsetting
	autoplaysd = xbmc.getInfoLabel('Skin.HasSetting(AutoPlaySD)')
	General_ConnectionScore = getsetting('General_ConnectionScore')
	General_ScriptON = getsetting('General_ScriptON')
	AutoPlay_Pause = getsetting('AutoPlay_Pause')
	General_ConnectionScoreN = int(General_ConnectionScore)
	printpoint = ""
	'''---------------------------'''
	
	if custom == "0":
		'''ACCOUNTS'''
		#addonsettings('REALDEBRID', 'plugin.video.genesis', 'Account1_Active', 'Account1_Period', 'realdedrid_user', 'realdedrid_password', "", "Sun", "A", "")
		addonsettings2('plugin.video.genesis','trakt_user',idstr,'trakt_password',idpstr,'movreel_user',idstr,'movreel_password',idpstr,'',"")
		addonsettings2('plugin.video.genesis','noobroom_mail',"",'noobroom_password',"",'furk_user',"",'furk_password',"",'',"")
		addonsettings2('plugin.video.genesis','premiumize_user',"",'premiumize_password',"",'furk_user',"",'furk_password',"",'',"")
		'''ALWAYS ON'''
		addonsettings2('plugin.video.genesis','check_library',"true",'play_hd',"true",'service_update',"true",'watched_library',"true",'watched_trakt',"true")
		addonsettings2('plugin.video.genesis','update_library',"true",'trakt_episodes',"true",'service_limit',"false",'resume_playback',"true",'playback_info',"true")
		addonsettings2('plugin.video.genesis','movie_library',"special://userdata/library/movies/",'tv_library',"special://userdata/library/tvshows/",'latest_episodes',"1",'imdb_user',"ur42807646",'host_select',"0")
		addonsettings2('plugin.video.genesis','service_interval',"0",'root_movies',"1",'root_episodes_trakt',"0",'root_episodes',"0",'root_calendar',"0")
		addonsettings2('plugin.video.genesis','fanart',"true",'downloads',"special://userdata/library/downloads/",'appearance',"GOne",'',"",'view47',"true")
		addonsettings2('plugin.video.genesis','subtitles',"true",'sublang1',"Hebrew",'sublang2',"English",'',"",'',"")
		'''AUTOPLAY - in GenesisSettings(4)'''
		#addonsettings2('plugin.video.genesis','autoplay',"true",'autoplay_hd',"true",'autoplay_library',"true",'',"",'',"")
		#addonsettings2('plugin.video.genesis','autoplay',"true",'autoplay_hd',"true",'autoplay_library',"true",'',"",'',"")
		#addonsettings2('script.htpt.refresh','AutoPlay_Pause',"false",'AutoPlay_HD',"true",'AutoPlay_SD',"false",'',"",'',"")
		'''HOSTS ALWAYS ON'''
		addonsettings2('plugin.video.genesis','animeultima_tv',"true",'clickplay_tv',"true",'directdl_tv',"true",'einthusan',"true",'',"")
		addonsettings2('plugin.video.genesis','icefilms',"true",'icefilms_tv',"true",'g2g',"true",'iwatchonline',"true",'iwatchonline_tv',"true")
		addonsettings2('plugin.video.genesis','merdb',"true",'merdb_tv',"true",'movie25',"true",'movieshd',"true",'',"")
		addonsettings2('plugin.video.genesis','moviestorm',"true",'moviestorm_tv',"true",'movietube',"true",'movietube_tv',"true",'moviezone',"true")
		addonsettings2('plugin.video.genesis','movietv',"true",'movietv_tv',"true",'muchmovies',"true",'myvideolinks',"true",'niter',"true")
		addonsettings2('plugin.video.genesis','onlinemovies',"true",'ororo_tv',"true",'primewire',"true",'primewire_tv',"true",'sweflix',"true")
		addonsettings2('plugin.video.genesis','tvrelease_tv',"true",'twomovies',"true",'twomovies_tv',"true",'vkbox',"true",'vkbox_tv',"true")
		addonsettings2('plugin.video.genesis','watchseries_tv',"true",'wso',"true",'wso_tv',"true",'yify',"true",'zumvo',"true")
		
		'''HOSTS ON/OFF'''
		addonsettings2('plugin.video.genesis','furk',"false",'furk_tv',"false",'noobroom',"false",'noobroom_tv',"false",'',"")
		#addonsettings2('plugin.video.genesis','furk',"false",'furk_tv',"false",'noobroom',"false",'noobroom_tv',"false",'',"")

		'''HOSTS PRIORITY HD'''
		addonsettings2('plugin.video.genesis','hosthd1',"GVideo",'hosthd2',"Sweflix",'hosthd3',"Niter",'hosthd4',"Muchmovies",'hosthd5',"Videomega")
		addonsettings2('plugin.video.genesis','hosthd6',"YIFY",'hosthd7',"Einthusan",'hosthd8',"Movreel",'hosthd9',"VK",'hosthd10',"")
		addonsettings2('plugin.video.genesis','hosthd11',"",'hosthd12',"",'hosthd13',"",'hosthd14',"",'hosthd15',"")
		addonsettings2('plugin.video.genesis','hosthd16',"",'hosthd17',"",'hosthd18',"",'hosthd19',"",'hosthd20',"")

		'''HOSTS PRIORITY SD'''
		addonsettings2('plugin.video.genesis','host1',"Ororo",'host2',"Streamin",'host3',"MovieTV",'host4',"iShared",'host5',"VK")
		addonsettings2('plugin.video.genesis','host6',"",'host7',"",'host8',"",'host9',"",'host10',"")
		addonsettings2('plugin.video.genesis','host11',"",'host12',"",'host13',"",'host14',"",'host15',"")
		addonsettings2('plugin.video.genesis','host16',"",'host17',"",'host18',"",'host19',"",'host20',"")
		'''---------------------------'''
		printpoint = printpoint + "1"
		
	elif custom == "2":
		'''------------------------------
		---ON-TIMEZONE-------------------
		------------------------------'''
		General_TimeZone = getsetting('General_TimeZone')
		'''---------------------------'''
		'''ACCOUNTS'''
		addonsettings('REALDEBRID', 'plugin.video.genesis', 'Account1_Active', 'Account1_Period', 'realdedrid_user', 'realdedrid_password', "", "Sun", "A", "")
		'''---------------------------'''
		if General_TimeZone == "A":
			printpoint = printpoint + "1"
		elif General_TimeZone == "B":
			printpoint = printpoint + "2"
		elif General_TimeZone == "C":
			printpoint = printpoint + "3"
			
	elif custom == "4":
		'''------------------------------
		---AUTOPLAY-GENERAL--------------
		------------------------------'''
		#if General_ScriptON == "false":	
		if General_ConnectionScore == "5" or (General_ConnectionScore == "4" and not autoplaysd):
			'''------------------------------
			---General_ConnectionScore-5-----
			------------------------------'''
			if AutoPlay_Pause == "true":
				'''------------------------------
				---AutoPlay_Pause-true----------
				------------------------------'''
				addonsettings2('plugin.video.genesis','autoplay',"false",'autoplay_hd',"true",'autoplay_library',"false",'playback_info',"false",'',"")
				addonsettings2('script.htpt.refresh','',"",'AutoPlay_HD',"true",'AutoPlay_SD',"false",'',"",'',"")
				printpoint = printpoint + "2"
				setSkinSetting("1",'AutoPlay_Pause',"true")
				setSkinSetting("1",'AutoPlay_HD',"true")
				setSkinSetting("1",'AutoPlay_SD',"false")
				'''---------------------------'''
			else:
				'''------------------------------
				---AutoPlay_Pause-false----------
				------------------------------'''
				addonsettings2('plugin.video.genesis','autoplay',"true",'autoplay_hd',"true",'autoplay_library',"true",'playback_info',"true",'',"")
				addonsettings2('script.htpt.refresh','',"",'AutoPlay_HD',"true",'AutoPlay_SD',"false",'',"",'',"")
				printpoint = printpoint + "3"
				setSkinSetting("1",'AutoPlay_Pause',"false")
				setSkinSetting("1",'AutoPlay_HD',"true")
				setSkinSetting("1",'AutoPlay_SD',"false")
				'''---------------------------'''
				
		elif General_ConnectionScore == "4" and autoplaysd:
			'''------------------------------
			---General_ConnectionScore-4-----
			------------------------------'''
			if AutoPlay_Pause == "true":
				'''------------------------------
				---AutoPlay_Pause-true----------
				------------------------------'''
				addonsettings2('plugin.video.genesis','autoplay',"false",'autoplay_hd',"false",'autoplay_library',"false",'playback_info',"false",'',"")
				addonsettings2('script.htpt.refresh','',"",'AutoPlay_HD',"false",'AutoPlay_SD',"true",'',"",'',"")
				printpoint = printpoint + "4"
				setSkinSetting("1",'AutoPlay_Pause',"true")
				setSkinSetting("1",'AutoPlay_HD',"false")
				setSkinSetting("1",'AutoPlay_SD',"true")
				'''---------------------------'''
			else:
				'''------------------------------
				---AutoPlay_Pause-false----------
				------------------------------'''
				addonsettings2('plugin.video.genesis','autoplay',"true",'autoplay_hd',"false",'autoplay_library',"true",'playback_info',"true",'',"")
				addonsettings2('script.htpt.refresh','',"",'AutoPlay_HD',"false",'AutoPlay_SD',"true",'',"",'',"")
				printpoint = printpoint + "5"
				setSkinSetting("1",'AutoPlay_Pause',"false")
				setSkinSetting("1",'AutoPlay_HD',"false")
				setSkinSetting("1",'AutoPlay_SD',"true")
				'''---------------------------'''
		elif General_ConnectionScoreN < 4:
			'''------------------------------
			---General_ConnectionScore-0-3---
			------------------------------'''
			'''------------------------------
			---AutoPlay_Pause-true----------
			------------------------------'''
			addonsettings2('plugin.video.genesis','autoplay',"false",'autoplay_hd',"true",'autoplay_library',"false",'playback_info',"false",'',"")
			addonsettings2('script.htpt.refresh','AutoPlay_Pause',"true",'AutoPlay_HD',"false",'AutoPlay_SD',"false",'',"",'',"")
			printpoint = printpoint + "6"
			setSkinSetting("1",'AutoPlay_Pause',"true")
			setSkinSetting("1",'AutoPlay_HD',"false")
			setSkinSetting("1",'AutoPlay_SD',"false")
			'''---------------------------'''
	elif custom == "5":
		'''------------------------------
		---AUTOPLAY-FORCE----------------
		------------------------------'''
		if General_ConnectionScoreN < 5:
			'''------------------------------
			---General_ConnectionScore-5-----
			------------------------------'''
			if autoplaysd:
				addonsettings2('plugin.video.genesis','autoplay',"true",'autoplay_hd',"false",'autoplay_library',"true",'',"",'',"")
				addonsettings2('script.htpt.refresh','AutoPlay_Pause',"false",'AutoPlay_HD',"false",'AutoPlay_SD',"true",'',"",'',"")
				printpoint = printpoint + "9"
				'''---------------------------'''
			else:
				addonsettings2('plugin.video.genesis','autoplay',"true",'autoplay_hd',"true",'autoplay_library',"true",'',"",'',"")
				addonsettings2('script.htpt.refresh','AutoPlay_Pause',"false",'AutoPlay_HD',"true",'AutoPlay_SD',"false",'',"",'',"")
				printpoint = printpoint + "10"
				'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if General_ScriptON == "false" or custom == "5": print printfirst + "GenesisSettings" + space3 + custom + space + "( " + General_ConnectionScore + " ) " + "LV_" + printpoint
	'''---------------------------'''