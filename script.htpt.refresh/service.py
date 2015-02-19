import xbmc, os, subprocess, sys
import xbmcgui, xbmcaddon

#from variables import *
from modules import *

def OnOff(value):
	from variables import getsetting, admin
	'''------------------------------
	---General_ScriptON--------------
	------------------------------'''
	setsetting_custom1('script.htpt.refresh','General_ScriptON',value)
	xbmc.sleep(100)
	General_ScriptON = getsetting('General_ScriptON')
	'''---------------------------'''
	
	'''------------------------------
	---setGeneral_Refresh------------
	------------------------------'''
	setGeneral_Refresh(General_ScriptON)
	'''---------------------------'''
	
	'''------------------------------
	---General_StartWindow-----------
	------------------------------'''
	General_StartWindow = getsetting('General_StartWindow')
	setGeneral_StartWindow(General_ScriptON, General_StartWindow)
	General_StartWindow = getsetting('General_StartWindow')
	'''---------------------------'''
	
	'''------------------------------
	---Current_M_T-------------------
	------------------------------'''
	Current_M_T2 = getsetting('Current_M_T')
	setCurrent_M_T(General_StartWindow)
	xbmc.sleep(100)
	Current_M_T = getsetting('Current_M_T')
	'''---------------------------'''
	
	'''------------------------------
	---topvideoinformation-----------
	------------------------------'''
	topvideoinformation(General_StartWindow,Current_M_T)
	'''---------------------------'''
	
	'''------------------------------
	---Current/Last_Name/Source------
	------------------------------'''
	Current_Name2 = getsetting('Current_Name')
	Current_Source2 = getsetting('Current_Source')
	setCurrent_Name(Current_Name2,Current_Source2,Current_M_T2,General_StartWindow)
	xbmc.sleep(100)
	Current_Name = getsetting('Current_Name')
	'''---------------------------'''
	
	'''------------------------------
	---LastMovie/TV_Subtitle---------
	------------------------------'''
	setLast_Subtitle(Current_M_T,Current_M_T2,Current_Name2)
	'''---------------------------'''
	
	'''------------------------------
	---General_TimeZone--------------
	------------------------------'''
	setGeneral_TimeZone(General_ScriptON)
	'''---------------------------'''
	
	if value == "true":
		'''------------------------------
		---General_ScriptON-TRUE---------
		------------------------------'''
		addonsettings2('script.htpt.refresh','General_CustomVAR',"",'General_CountWait',"0",'',"",'',"",'',"")
		
		#xbmc.sleep(1000)
		#xbmc.executebuiltin('RunScript(script.htpt.refresh)')		
		'''---------------------------'''
	else:
		'''------------------------------
		---General_ScriptON-FALSE--------
		------------------------------'''
		#xbmc.sleep(1000)
		if xbmc.Player().isPlayingVideo():
			notification("Video Stop","","",4000)
			xbmc.executebuiltin('Action(Stop)')
			
		addonsettings2('script.htpt.refresh','General_StartWindow',"",'Current_M_T',"",'General_Connected',"0",'Current_Watched',"false",'',"")
		addonsettings2('script.htpt.refresh','Current_Duration',"",'Current_RefreshPoint',"",'',"",'',"",'',"")
		setsetting_custom1('script.htpt.refresh','AutoPlay_Pause',"false")
		#General_Refresh
		'''---------------------------'''
		
	xbmc.sleep(200)
	RefreshSettings()
	
	print printfirst + "OnOff (END)" + space2 + General_ScriptON
	
def checkStream(admin):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import getsetting, setsetting
	#from variables import AutoPlay_Pause, AutoPlay_SD, AutoPlay_HD
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	General_CountWait = getsetting('General_CountWait')
	General_Connected = getsetting('General_Connected')
	dialogselectsources = xbmc.getInfoLabel('Skin.String(dialogselectsources)')
	dialogselectsources2 = xbmc.getInfoLabel('Skin.String(dialogselectsources2)')
	General_ScriptON = getsetting('General_ScriptON')
	General_CustomVAR = getsetting('General_CustomVAR')
	Current_Source = getsetting('Current_Source')
	General_CountWaitN = int(General_CountWait)
	'''---------------------------'''
	Current_Dialog2 = getsetting('Current_Dialog')
	'''---------------------------'''
	'''returned_Dialog = Curent_Dialog'''
	returned_Dialog = getDialogW("dialog")
	xbmc.sleep(500)
	
	#if admin: print printfirst + "checkStream" + space2 + "General_ScriptON" + space2 + General_ScriptON
	
	if (General_ScriptON == "true" or General_Connected != "0") and returned_Dialog != "dialogokW":
		'''------------------------------
		---setGeneral_Connected----------
		------------------------------'''
		setGeneral_Connected(connected)
		'''---------------------------'''
		
	if General_ScriptON == "true" or General_CustomVAR != "":
		'''------------------------------
		---setGeneral_CustomVAR----------
		------------------------------'''
		setGeneral_CustomVAR(General_CustomVAR, General_ScriptON, Current_Dialog2)
		'''---------------------------'''
		
	if General_ScriptON == "false":
		'''------------------------------
		---General_ScriptON-FALSE---------
		------------------------------'''
		if returned_Dialog == "dialogprogressW" or returned_Dialog == "dialogselectW":
			'''------------------------------
			-dialogprogress-/-dialogselectW--
			------------------------------'''
			returned_Header = getDialogW("header")
			if returned_Header == "Genesis":
				if admin:
					notification("OnOff-true (1)","","",1000)
					print printfirst + "OnOff-true (1)" 
				OnOff("true")
			#else:
				#print printfirst + "Error returned_Dialog ==" + space2 + returned_Dialog + space + "General_ScriptON" + space2 + General_ScriptON + space3
		elif returned_Dialog == "dialogbusyW":
			'''------------------------------
			---dialogbusyW-&-isgenesis-------
			------------------------------'''
			homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
			dialogselectsources3 = xbmc.getInfoLabel('Skin.String(DialogSelectSources3)')
			containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
			isgenesis = "videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath or "plugin://plugin.video.genesis/" in containerfolderpath
			if isgenesis:
				istv = (xbmc.getInfoLabel('ListItem.TVShowTitle') != "" and xbmc.getInfoLabel('ListItem.Season') != "" and xbmc.getInfoLabel('ListItem.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
				ismovie = (xbmc.getInfoLabel('ListItem.Year') != "" or xbmc.getInfoLabel('ListItem.Country') != "" or xbmc.getInfoLabel('ListItem.Tagline') != "") and not istv
				if istv or ismovie:
					if admin:
						notification("OnOff-true (2)","","",1000)
						print printfirst + "OnOff-true (2)" 
					OnOff("true")
				'''---------------------------'''
			elif homeW and dialogselectsources3:
				if admin:
					notification("OnOff-true (3)","","",1000)
					print printfirst + "OnOff-true (3)" 
				OnOff("true")
				'''---------------------------'''
	elif General_ScriptON == "true":
		'''------------------------------
		---General_ScriptON-TRUE---------
		------------------------------'''
		if returned_Dialog == "dialogokW":
			'''------------------------------
			---dialogokW-ON------------------
			------------------------------'''
			if Current_Dialog2 != "dialogokW":
				if admin: notification("Current_Dialog2 != dialogokW ","true",General_CustomVAR,1000)
				setGeneral_ConnectionScore(Current_Dialog2,"")
				if admin: notification("Current_Dialog2 != dialogokW ","true",General_CustomVAR,1000)
				openDialogOK(Current_Dialog2)
			else:
				if admin: notification("Current_Dialog2 != dialogokW ","false",General_CustomVAR,2000)
			'''---------------------------'''
		elif returned_Dialog == "dialogselectW":
			'''------------------------------
			---dialogselectW-ON--------------
			------------------------------'''
			if admin: notification("dialogselectW-ON",dialogselectsources2,General_CustomVAR,1000)
			#setsetting_custom1('script.htpt.refresh','Current_Source',dialogselectsources)
			#setSkinSetting("0",'DialogSelectSources2',dialogselectsources)
			if Current_Dialog2 != "dialogselectW":
				if admin: notification("dialogselectW-ON (2)",dialogselectsources2,General_CustomVAR,1000)
				pass
				#setsetting_custom1('script.htpt.refresh','Current_Source',dialogselectsources)
				#setSkinSetting("0",'DialogSelectSources2',dialogselectsources)
		elif Current_Dialog2 == "dialogselectW": # and General_CustomVAR != "1" and General_CustomVAR != "4"
			'''------------------------------
			---Current_Source----------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','Current_Source',dialogselectsources)
			setSkinSetting("0",'DialogSelectSources2',dialogselectsources)
			'''---------------------------'''
		
		elif returned_Dialog == "dialogbusyW":
			'''------------------------------
			---dialogbusyW-------------------
			------------------------------'''
			calculate('script.htpt.refresh','General_CountWait',"1")
			General_CountWait2 = getsetting('General_CountWait')
			setSkinSetting("0",'General_CountWait',General_CountWait2)
			setGeneral_Connected(connected)
			'''---------------------------'''

		elif returned_Dialog == "dialogyesnoW":
			'''------------------------------
			---dialogyesnoW-ON---------------
			------------------------------'''
			pass
			'''---------------------------'''
			
		elif returned_Dialog == "dialogprogressW":
			'''------------------------------
			--dialogprogress-ON--------------
			------------------------------'''
			calculate('script.htpt.refresh','General_CountWait',"1")
			General_CountWait2 = getsetting('General_CountWait')
			setSkinSetting("0",'General_CountWait',General_CountWait2)
			setGeneral_Connected(connected)
			'''---------------------------'''
			
		elif returned_Dialog == "" and Current_Dialog2 == "":
			'''------------------------------
			--dialog-OFF---------------------
			------------------------------'''
			OnOff("false")
			'''---------------------------'''
		if returned_Dialog != Current_Dialog2: print printfirst + "checkStream" + space2 + "Current_Dialog" + space2 + Current_Dialog + space + "General_ScriptON" + space2 + General_ScriptON + space3
		#RefreshSettings()
		'''---------------------------'''

def testStream(admin):
	count = 0
	countS = str(count)
	printpoint = ""
	smooth = ""
	if admin: notification("_","","",2000)
	xbmc.executebuiltin('Action(Play)') #TRY TO PREVENT PAUSE OF THIS SERVICE IF CACHE
	while count < 10 and xbmc.Player().isPlayingVideo() and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		from variables import getsetting, setsetting
		connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
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
			if not connected and not systemplatformwindows: notification('$LOCALIZE[79512]',addonString(20),"",5000)
			
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
				if not "2" in printpoint and not videoplayerhassubtitles and (istv2 or ismovie2): xbmc.executebuiltin('ActivateWindow(subtitlesearch)')
				if not "2" in printpoint: setGeneral_ConnectionScore("",smooth)
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
						setGeneral_ConnectionScore("",smooth)						
						if General_ConnectionScoreN == 0: notification(addonString(225),addonString(227),"",5000) #RESET ROUTER
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
	print printfirst + "testStream" + space + "smooth" + space2 + smooth + space + "count" + space2 + countS + space + "LV_" + printpoint + space3
	'''---------------------------'''

def getPlayerInfo(admin):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import admin, systemidle3
	from variables import getsetting, setsetting
	playerpaused = xbmc.getCondVisibility('Player.Paused')
	playerduration = xbmc.getInfoLabel("Player.Duration(hh)") + xbmc.getInfoLabel("Player.Duration(mm)") + xbmc.getInfoLabel("Player.Duration(ss)")
	playerdurationN = int(playerduration)
	refreshtimeN = playerdurationN * 0.90
	refreshtimeN = int(round(refreshtimeN,-1))
	refreshtime = str(refreshtimeN)
	'''---------------------------'''
	setsetting('Current_Duration',playerduration)
	setsetting('Current_RefreshPoint',refreshtime)
	'''---------------------------'''
	return playerdurationN
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "getPlayerInfo" + "playerduration" + space2 + playerduration + space + "refreshtime" + space2 + refreshtime + space3
	'''---------------------------'''
	
def setCurrent_Watched(admin):
	try:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		from variables import getsetting, setsetting
		Current_RefreshPoint = getsetting('Current_RefreshPoint')
		Current_Watched = getsetting('Current_Watched')
		General_Refresh = getsetting('General_Refresh')
		General_StartWindow = getsetting('General_StartWindow')
		Current_RefreshPointN = int(Current_RefreshPoint)
		Current_M_T = getsetting('Current_M_T')
		playertime = xbmc.getInfoLabel("Player.Time(hh)") + xbmc.getInfoLabel("Player.Time(mm)") + xbmc.getInfoLabel("Player.Time(ss)")
		playertimeN = int(playertime)
		'''---------------------------'''
		
		if playertimeN > Current_RefreshPointN: setsetting_custom1('script.htpt.refresh','Current_Watched',"true")
		elif playertimeN < Current_RefreshPointN: setsetting_custom1('script.htpt.refresh','Current_Watched',"false")
		'''---------------------------'''
		Current_Watched2 = getsetting('Current_Watched')
		if admin and Current_Watched != Current_Watched2: notification("Admin","Current_Watched Switched!","",1000)
		'''---------------------------'''
		
		if Current_Watched == "false":
			'''------------------------------
			---General_Refresh-OFF-----------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','General_Refresh',"false")
			'''---------------------------'''
			
		else:
			'''------------------------------
			---General_Refresh-ON------------
			------------------------------'''
			if Current_M_T == "0": setsetting_custom1('script.htpt.refresh','General_Refresh',"0")
			elif Current_M_T == "1": setsetting_custom1('script.htpt.refresh','General_Refresh',"1")
			'''---------------------------'''
			playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
			playlistlengthN = int(playlistlength)
			playlistposition = xbmc.getInfoLabel('Playlist.Position(video)')
			playlistpositionN = int(playlistposition)
			playertimeremaining = xbmc.getInfoLabel("Player.TimeRemaining(hh)") + xbmc.getInfoLabel("Player.TimeRemaining(mm)") + xbmc.getInfoLabel("Player.TimeRemaining(ss)")
			playertimeremainingN = int(playertimeremaining)
			'''---------------------------'''
			if playertimeremainingN < 15:
				if playlistpositionN < playlistlengthN and playlistlengthN > 1:
					'''------------------------------
					---PLAYLIST-TIME-ABOUT-TO-END----
					------------------------------'''
					GenesisSettings("5")
					setsetting_custom1('script.htpt.refresh','General_CountWait',"0")
					'''---------------------------'''
			
				elif General_StartWindow == "1":
					'''------------------------------
					---counter dialogselectW bug!----
					------------------------------'''
					print printfirst + "counter dialogselectW bug!" + space + playertimeremaining + space3
					if admin: notification("Admin","counter dialogselectW bug!!!","","",2000)
					xbmc.executebuiltin('Action(Pause)')
					xbmc.sleep(200)
					xbmc.executebuiltin('Action(Stop)')
					OnOff("false")
					'''---------------------------'''
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		Current_Watched2 = getsetting('Current_Watched')
		if Current_Watched != Current_Watched2: print printfirst + "setCurrent_Watched" + "playertime" + space2 + playertime + "playerduration" + space2 + playerduration + space3 + "Current_RefreshPoint" + space2 + Current_RefreshPoint + space3
		'''---------------------------'''
	except:
		print printfirst + "setCurrent_Watched" + space + "except-pass" + space3
	

def setGeneral_SubSearch(count):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	dialogsubtitlesW = getsetting('dialogsubtitlesW')
	count2 = 0
	'''---------------------------'''
	while count2 < 100 and dialogsubtitlesW and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		from variables import getsetting, setsetting
		dialogsubtitlesW = getsetting('dialogsubtitlesW')
		General_SubSearch = getsetting('General_SubSearch')
		dialogsubtitles2 = xbmc.getInfoLabel('Skin.String(DialogSubtitles2)')
		dialogsubtitles = xbmc.getInfoLabel('Skin.String(DialogSubtitles)')
		container120numitems = xbmc.getInfoLabel('Container(120).NumItems') #DialogSubtitles
		controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
		'''---------------------------'''
		xbmc.sleep(1000)
		count2 += 1
		'''---------------------------'''
		#onClick(self, int controlId)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "setGeneral_SubSearch" + space2 + General_SubSearch + space + "count/2" + space2 + count + " / " + count2 + space 
	'''---------------------------'''

class main:
	'''------------------------------
	---STARTUP-----------------------
	------------------------------'''
	xbmc.sleep(7000)
	OnOff("false")
	addonsettings2('script.htpt.refresh','General_Connected',"0",'General_ConnectionScore',"5",'General_CustomVAR',"",'General_Refresh',"",'Current_Source',"")
	addonsettings2('script.htpt.refresh','',"",'Current_Watched',"false",'',"",'',"",'',"")
	setSkinSetting("0",'DialogSelectSources3',"")
	setSkinSetting("0",'DialogSelectSources',"")
	if not systemplatformwindows: bash('rm -rf /storage/.kodi/userdata/addon_data/plugin.video.genesis',"plugin.video.genesis")
	xbmc.sleep(5000)
	GenesisSettings("0")
	GenesisSettings("2")
	GenesisSettings("4")
	RefreshSettings()
	
	'''---------------------------'''
	while 1 and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		from variables import getsetting
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		istvmoviep = (videoplayertitle in dialogselectsources3 or videoplayertitle in dialogselectsources5)
		systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
		General_ScriptON = getsetting('General_ScriptON')
		'''---------------------------'''
		print printfirst + "service.py " + space + "main class"
		xbmc.sleep(1000)
		count = 0

		while systemidle10 and General_ScriptON == "false" and not xbmc.abortRequested:
			'''------------------------------
			---IDLE TIME---------------------
			------------------------------'''
			from variables import admin, getsetting
			systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
			General_ScriptON = getsetting('General_ScriptON')
			'''---------------------------'''
			xbmc.sleep(1000)
			count += 1

			'''---------------------------'''
			#if count == 2: setGeneral_TimeZone(General_ScriptON)
			if count == 2 or admin: print printfirst + "service.py" + space + "idletime10"
			
			'''---------------------------'''
		count = 0
		while not xbmc.Player().isPlayingVideo() and (not systemidle10 or General_ScriptON == "true") and not xbmc.abortRequested:
			'''------------------------------
			---VIDEO-OFF---------------------
			------------------------------'''
			from variables import getsetting
			admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
			systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
			General_ScriptON = getsetting('General_ScriptON')
			'''---------------------------'''
			xbmc.sleep(500) #+500 in checkStream!
			count += 1
			'''---------------------------'''
			checkStream(admin)
			if count == 2 or admin: print printfirst + "service.py " + "VIDEO-OFF"
			'''---------------------------'''
		count = 0
		videoplayertitle = xbmc.getInfoLabel('VideoPlayer.Title')
		dialogselectsources3 = xbmc.getInfoLabel('Skin.String(DialogSelectSources3)')
		dialogselectsources5 = xbmc.getInfoLabel('Skin.String(DialogSelectSources5)')
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		istv4 = " S" in dialogselectsources3 and " E" in dialogselectsources3
		ismovie4 = " (" in dialogselectsources3 and ")" in dialogselectsources3 and not istv4
		istv2 = (xbmc.getInfoLabel('VideoPlayer.TVShowTitle') != "" and xbmc.getInfoLabel('VideoPlayer.Season') != "" and xbmc.getInfoLabel('VideoPlayer.Episode') != "") or ("videodb://tvshows" in containerfolderpath or "library://video/tvshows" in containerfolderpath)
		ismovie2 = xbmc.getInfoLabel('VideoPlayer.Content') == "movies" or ((xbmc.getInfoLabel('VideoPlayer.Year') != "" or xbmc.getInfoLabel('VideoPlayer.Country') != "") and xbmc.getInfoLabel('VideoPlayer.Tagline') != "") and not istv2
		istvmoviep = "false"
		#if (videoplayertitle in dialogselectsources3 or videoplayertitle in dialogselectsources5) and videoplayertitle != "": istvmoviep = "true"
		if istv2 or ismovie2: istvmoviep = "true"
		
		if istvmoviep == "true": notification("test","istvmoviep","",2000)
			
		'''---------------------------'''
		while xbmc.Player().isPlayingVideo() and (General_ScriptON == "true" or istvmoviep == "true") and not xbmc.abortRequested:
			'''------------------------------
			---VIDEO-ON----------------------
			------------------------------'''
			if count == 0:
				addonsettings2('script.htpt.refresh','',"",'',"",'General_CustomVAR',"",'',"",'',"")
			if count > 0: xbmc.sleep(1000)
			count += 1
			playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
			'''---------------------------'''
			from variables import getsetting
			admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
			systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
			General_ScriptON = getsetting('General_ScriptON')
			systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
			playerpaused = xbmc.getCondVisibility('Player.Paused')
			'''------------------------------'''
			if count == 1: 
				try: playerdurationN = getPlayerInfo(admin)
				except:
					xbmc.sleep(1000)
					try: playerdurationN = getPlayerInfo(admin)
					except:
						xbmc.sleep(1000)
						try: playerdurationN = getPlayerInfo(admin)
						except: onoff("false")
			if count == 2:
				print printfirst + "service.py " + "VIDEO-ON"
				if playerdurationN > 1500: testStream(admin)
				else:
					onoff("false")
			elif istvmoviep and General_ScriptON == "false": OnOff("true")
			
			if not playerhasvideo: pass
			elif count > 7 and not systemidle3:
				returned_Dialog = getDialogW("dialog")
				if returned_Dialog == "dialogprogressW" or returned_Dialog == "dialogselectW":
					'''------------------------------
					-dialogprogress-/-dialogselectW--
					------------------------------'''
					returned_Header = getDialogW("header")
					if returned_Header == "Genesis":
						'''------------------------------
						--General_ScriptON-OFF-----------
						------------------------------'''
						print printfirst + "service.py" + "General_ScriptON-OFF"
						OnOff("false")
				elif returned_Dialog == "dialogsubtitlesW":
					'''------------------------------
					---dialogsubtitlesW--------------
					------------------------------'''
					pass
					#setGeneral_SubSearch(count)
					#xbmc.executebuiltin('RunScript(script.htpt.refresh)')
			else:
				'''------------------------------
				---WATCHED-CHECK-----------------
				------------------------------'''
				if count > 60 and not playerpaused and systemidle3: setCurrent_Watched(admin)
				'''---------------------------'''
			
				'''------------------------------'''	
		#while General_ScriptON == "true" and not xbmc.abortRequested:
			#xbmc.sleep(1000)
			
		
		#while General_ScriptON == "false" and not xbmc.abortRequested:
			#xbmc.sleep(1000)
