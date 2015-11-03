import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys

from variables import *
from shared_modules import *

def doAutoShutdown(admin, Time_Shutdown, Time_DelayN):
	autoshutdown = xbmc.getInfoLabel('Skin.HasSetting(AutoShutdown)')
	'''---------------------------'''
	if autoshutdown:
		#Time_Shutdown = getsetting('Time_Shutdown')
		dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
		playerhasmedia = xbmc.getCondVisibility('Player.HasMedia')
		playerhasaudio = xbmc.getCondVisibility('Player.HasAudio')
		systemscreensaveractive = xbmc.getCondVisibility('System.ScreenSaverActive')
		scriptpythonslideshowW = xbmc.getCondVisibility('Window.IsVisible(script-python-slideshow.xml)')
		playerpaused = xbmc.getCondVisibility('Player.Paused')
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)')
		'''---------------------------'''
		if Time_Shutdown == "0":
			addon = 'script.htpt.smartbuttons'
			if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				if systemplatformwindows or systemplatformandroid: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=52)')
				else: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=53)')
 
			if playerhasmedia: xbmc.executebuiltin('Action(Stop)')
			xbmc.sleep(5000)
			scripthtptdebug_General_ScriptON = getsetting_scripthtptdebug('General_ScriptON')
			count = 0
			while count < 10 and scripthtptdebug_General_ScriptON == "true" and not xbmc.abortRequested:
				if count == 0: xbmc.executebuiltin('Notification($VAR[StartupMessage2],$INFO[Skin.String(ID1)],5000)')
				count += 1
				xbmc.sleep(1000)
				scripthtptdebug_General_ScriptON = getsetting_scripthtptdebug('General_ScriptON')
			
			setsetting_custom1('service.htpt.debug','General_ScriptON',"true")
			xbmc.sleep(1000)
			#xbmc.executebuiltin('XBMC.Reset()')
			xbmc.executebuiltin('XBMC.Powerdown()')
			xbmc.sleep(5000)
			'''---------------------------'''
			
		elif systemscreensaveractive or scriptpythonslideshowW:
			xbmc.executebuiltin('Action(Back)')
			if playerhasaudio: xbmc.executebuiltin('Action(Stop)')
			'''---------------------------'''
		elif (not playerhasmedia or playerpaused) and (not dialogokW or dialogHeader != localize(79532)):
			xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=11)')
			'''---------------------------'''
			
		elif dialogokW and Time_DelayN > 6900:
			if dialogHeader == localize(79532):
				if Time_Shutdown == "":
					#setsetting_custom1('service.htpt','Time_Shutdown',"120")
					setsetting('Time_Shutdown',"20")
					'''---------------------------'''
				else:
					Time_Shutdown = calculate('service.htpt','Time_Shutdown',"2",Time_Shutdown)
					notification(localize(79535) % (Time_Shutdown), localize(79533),"",1000)
					'''---------------------------'''
					if Time_Shutdown == "7":
						libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
						if libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
						'''---------------------------'''
		if admin:
			print printfirst + "autoshutdown" + space + "dialogHeader" + space2 + str(dialogHeader)
			print printfirst + "autoshutdown" + space + "localize(79532)" + space2 + localize(79532)
			'''---------------------------'''

def screensaver(admin, playerhasvideo):
	'''------------------------------
	---SCREEN-SAVER------------------
	------------------------------'''
	from variables import systemplatformwindows
	name = 'SCREEN-SAVER'
	printpoint = ""
	TypeError = ""
	systemscreensaveractive = xbmc.getCondVisibility('System.ScreenSaverActive')
	scriptpythonslideshowW = xbmc.getCondVisibility('Window.IsVisible(script-python-slideshow.xml)')
	playerhasaudio = xbmc.getCondVisibility('Player.HasAudio')
	'''---------------------------'''
	
	if not systemscreensaveractive and not scriptpythonslideshowW and not playerhasvideo and (not systemplatformwindows or admin):
		printpoint = printpoint + "1"
		if not playerhasaudio:
			printpoint = printpoint + "2"
			if os.path.exists(skin_music_path + "playHTPT.mp3"):
				xbmc.executebuiltin('PlayMedia('+skin_music_path+'playHTPT.mp3)')
			xbmc.executebuiltin('SetVolume(70)')
			'''---------------------------'''
			
		addon = 'screensaver.picture.slideshow'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunScript(screensaver.picture.slideshow)')
		else: installaddon(admin, addon, "")
		xbmc.sleep(1000)
		
		count = 0
		while count < 10 and (not systemscreensaveractive and not scriptpythonslideshowW) and not xbmc.abortRequested:
			count += 1
			xbmc.sleep(1000)
			systemscreensaveractive = xbmc.getCondVisibility('System.ScreenSaverActive')
			scriptpythonslideshowW = xbmc.getCondVisibility('Window.IsVisible(script-python-slideshow.xml)')
			'''---------------------------'''
		if count < 10: printpoint = printpoint + "7"
		else: printpoint = printpoint + "9"
		
		
	else: printpoint = printpoint + "8"
	'''---------------------------'''
	if "8" in printpoint: pass
	if "9" in printpoint: xbmc.executebuiltin('Action(Back)')
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + "_LV" + printpoint + space + "systemscreensaveractive" + space2 + str(systemscreensaveractive) + space + "scriptpythonslideshowW" + space2 + str(scriptpythonslideshowW)
	if TypeError != "": print printfirst + name + space + "TypeError" + space2 + str(TypeError)
	'''---------------------------'''

def LibraryUpdate(admin, Library_CleanDate, Library_UpdateDate):
	from variables import datenowS
	name = 'LibraryUpdate'
	extra = ""
	printpoint = ""
	TypeError = ""
	'''---------------------------'''
	libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
	'''---------------------------'''
	
	'''---------------------------'''
	if Library_CleanDate != "" and datenowS != "":
		import datetime as dt
		datenowD = stringtodate(datenowS,'%Y-%m-%d')
		Library_CleanDateD = stringtodate(Library_CleanDate,'%Y-%m-%d')
		Library_CleanDate2D = Library_CleanDateD + dt.timedelta(days=7)
		'''---------------------------'''
		if datenowD > Library_CleanDate2D: printpoint = printpoint + "7"
		'''---------------------------'''
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		xbmc.executebuiltin('CleanLibrary(video)')
		setsetting('Library_CleanDate',datenowS)
		'''---------------------------'''

	elif Library_CleanDate == datenowS: printpoint = printpoint + "1"
	
	else:
		if libraryisscanningvideo: printpoint = printpoint + "6"
		elif datenowS != Library_UpdateDate:
			printpoint = printpoint + "7"
			setsetting('Library_UpdateDate',datenowS)
			addonsettings2('plugin.video.genesis','',"",'',"",'check_episode_link',"false",'check_library',"false",'check_movie_link',"false")
			xbmc.executebuiltin('UpdateLibrary(video)')
			'''---------------------------'''
		else:
			printpoint = printpoint + "9"
			'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if TypeError != "": extra = newline + space + "TypeError" + space2 + str(TypeError)
	#if admin: 
	print printfirst + name + "_LV" + printpoint + space + "Library_UpdateDate" + space2 + str(Library_UpdateDate) + space + "Library_CleanDate" + space2 + str(Library_CleanDate) + space + extra
	'''---------------------------'''
	
def setTime_Start(admin):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	Time_Start = getsetting('Time_Start')
	#timenow = datetime.datetime.now()
	#timenowS = timenow.strftime("%H:%M")
	'''---------------------------'''
	#setsettings('Time_Start', timenow2S)
	setsetting('Time_Start',timenow2S)
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	Time_Start2 = getsetting('Time_Start')
	print printfirst + "setTime_Start" + space2 + "Time_Start" + space2 + Time_Start + " - " + Time_Start2 + space3
	'''---------------------------'''

def videoplayertweak(admin,playerhasvideo):
	if playerhasvideo:
		#if admin: xbmc.executebuiltin('Notification(Admin,fix bug with subtitles (1),1000)')
		playerfolderpath = xbmc.getInfoLabel('Player.FolderPath')
		videoplayersubtitlesenabled = xbmc.getInfoLabel('VideoPlayer.SubtitlesEnabled')
		videoplayerhassubtitles = xbmc.getInfoLabel('VideoPlayer.HasSubtitles')
		'''fix bug with subtitles'''
		if videoplayerhassubtitles and videoplayersubtitlesenabled:
			fix = 'no'
			if '.sdarot.w' in playerfolderpath: fix = 'yes'
			elif xbmc.getCondVisibility('!VideoPlayer.Content(Movies)') and xbmc.getCondVisibility('!VideoPlayer.Content(Episodes)') and xbmc.getCondVisibility('IsEmpty(VideoPlayer.Year)') and xbmc.getCondVisibility('IsEmpty(VideoPlayer.Plot)') and xbmc.getCondVisibility('!SubString(Player.Title,S0)') and xbmc.getCondVisibility('!SubString(Player.Title,S1)') and xbmc.getCondVisibility('!SubString(VideoPlayer.Title,TNPB)') and xbmc.getCondVisibility('!SubString(VideoPlayer.Title,Staael)') and xbmc.getCondVisibility('!SubString(Player.Filename,YIFY)'): fix = 'yes'
			if fix == 'yes':
				if admin: xbmc.executebuiltin('Notification(Admin,fix bug with subtitles,1000)')
				xbmc.executebuiltin('Action(ShowSubtitles)')
				'''---------------------------'''
				
		'''video osd auto close'''
		videoosd = xbmc.getCondVisibility('Window.IsVisible(VideoOSD.xml)')
		systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
		videoosdsettingsW = xbmc.getCondVisibility('Window.IsVisible(VideoOSDSettings.xml)')
		if videoosd and systemidle10 and not videoosdsettingsW:
			subtitleosdbutton = xbmc.getCondVisibility('Control.HasFocus(703)') #subtitleosdbutton
			volumeosdbutton = xbmc.getCondVisibility('Control.HasFocus(707)') #volumeosdbutton
			dialogpvrchannelsosd = xbmc.getCondVisibility('Window.IsVisible(DialogPVRChannelsOSD.xml)')
			'''---------------------------'''
			if (not subtitleosdbutton or not videoplayerhassubtitles) and not volumeosdbutton and not dialogpvrchannelsosd:
				if admin: xbmc.executebuiltin('Notification(Admin,videoosdauto,1000)')
				xbmc.executebuiltin('Dialog.Close(VideoOSD.xml)')
				'''---------------------------'''
			else:
				systemidle20 = xbmc.getCondVisibility('System.IdleTime(20)')
				if systemidle20: xbmc.executebuiltin('Dialog.Close(VideoOSD.xml)')
				'''---------------------------'''
	
def memkeyboard(admin):
	smartkeyboard = xbmc.getInfoLabel('Skin.HasSetting(smartkeyboard)')
	dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
	systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
	count = 0
	while count < 400 and smartkeyboard and dialogkeyboard and not systemidle3:
		xbmc.sleep(100)
		count += 1
		dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
		systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
		input = xbmc.getInfoLabel('Control.GetLabel(312)')
		smartkeyboardh0 = xbmc.getInfoLabel('Skin.String(smartkeyboardH0)')
		if input != smartkeyboardh0:
			xbmc.executebuiltin('Skin.SetString(smartkeyboardH0,'+ input +')')
			if admin: xbmc.executebuiltin('Notification(Admin memkeyboard,'+ input +',1000)')
		#xbmc.executebuiltin('Notification(Admin memkeyboard,'+ input +',1000)')
		
def connectioncheck(admin, admin2, count, systemidle3, Ping_Now, Ping_Connected):
	'''------------------------------
	---NETWORK-STATUS----------------
	------------------------------'''
	printpoint = "" ; TypeError = "" ; extra = ""
	mainwindow = xbmc.getCondVisibility('Window.IsVisible(mainWindow.xml)')
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
	connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
	networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
	netsettingsbutton = (xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(108)')) or xbmc.getCondVisibility('Container(52).HasFocus(40)') or (xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(10)'))
	count10 = [10, 20, 30, 40, 50, 60]
	
	if count == 0: printpoint = printpoint + "0"
	
	if Ping_Connected != "true" and (not count in count10 or count == 0):
		if Ping_Now == 'None':
			if networkipaddress == "" or networkipaddress == None:
				setSkinSetting("1","Connected2","false")
				setSkinSetting("1","Connected3","false")
			else:
				setSkinSetting("1","Connected2","true")
				setSkinSetting("1","Connected3","true")
			
			if "169.254." in networkipaddress:
				setSkinSetting("1","Connected","false")
			else:
				setSkinSetting("1","Connected","true")
			
		printpoint = printpoint + "9"
	else: pass
	
	if ((count in count10 or count == 0) or mainwindow or ((not connected and (connected2 or connected3)) or (connected and not connected2 and not connected3))) and not "9" in printpoint:
		'''------------------------------
		---Connected2-(WLAN)-------------
		------------------------------'''
		if systemplatformandroid:
			output = terminal('ifconfig wlan0',"Connected2")
		elif systemplatformwindows: output = terminal('netsh wlan show interfaces',"Connected2")
		elif systemplatformlinux or systemplatformlinuxraspberrypi: output = terminal('ifconfig wlan0',"Connected2")
		else: output = terminal('ifconfig wlan0',"Connected2")
		
		if networkipaddress != "" and networkipaddress != None and not "169.254." in networkipaddress:
			if systemplatformandroid:
				if not "Cannot assign" in output and "up broadcast" in output: printpoint = printpoint + "1"
				elif output == "": printpoint = printpoint + "Q"
			elif systemplatformlinux or systemplatformlinuxraspberrypi:
				if not "packets:0" in output and "inet addr" in output: printpoint = printpoint + "1"			
			elif systemplatformwindows:
				if not "disconnected" in output and "connected" in output: printpoint = printpoint + "1"
				elif "disconnected" in output: printpoint = printpoint + "2"
				elif "netsh" in output and "is not recognized" in output: printpoint = printpoint + "Q"
			else: printpoint = printpoint + "1"
				
		else: printpoint = printpoint + "2"
		
		if "1" in printpoint:
			'''CONNECTED'''
			setSkinSetting('1','Connected2','true')
			#if not connected2: xbmc.executebuiltin('Skin.ToggleSetting(Connected2)')
		elif "Q" in printpoint:
			'''DEMI CONNECTED'''
			if not connected2: xbmc.executebuiltin('Skin.ToggleSetting(Connected2)')
		else:
			'''NOT CONNECTED'''
			setSkinSetting('1','Connected2','false')
			#if connected2: xbmc.executebuiltin('Skin.ToggleSetting(Connected2)')
			
		'''------------------------------
		---Connected3-(LAN)--------------
		------------------------------'''
		if systemplatformandroid: output = terminal('ifconfig eth0',"Connected2")
		elif systemplatformwindows: output = terminal('netsh lan show interfaces',"Connected3")
		elif systemplatformlinux or systemplatformlinuxraspberrypi: output = terminal('ifconfig eth0',"Connected2")
		else: output = terminal('ifconfig eth0',"Connected2")
		
		if networkipaddress != "" and networkipaddress != None and not "169.254." in networkipaddress:
			if systemplatformandroid:
				if not "down broadcast" in output and "up broadcast" in output: printpoint = printpoint + "3"
				else: printpoint = printpoint + "Q"
			elif systemplatformlinux or systemplatformlinuxraspberrypi:
				if not "packets:0" in output and "inet addr" in output: printpoint = printpoint + "3"
			elif systemplatformwindows:
				if ("Enabled" in output and "Wired LAN" in output) or "is not running" in output: printpoint = printpoint + "3"
				elif "disconnected" in output: printpoint = printpoint + "4"
				elif "netsh" in output and "is not recognized" in output: printpoint = printpoint + "Q"
			else: printpoint = printpoint + "Q"
		
		else: printpoint = printpoint + "4"
		
		if "3" in printpoint:
			'''CONNECTED'''
			setSkinSetting('1','Connected3','true')
			if not connected3: pass
		elif "Q" in printpoint:
			'''DEMI CONNECTED'''
			pass
		else:
			'''NOT CONNECTED'''
			setSkinSetting('1','Connected3','false')
			#if connected3: xbmc.executebuiltin('Skin.ToggleSetting(Connected3)')
			
	if ((count > 1 and (connected2 or connected3)) or count == 0 or "Q" in printpoint) and not "9" in printpoint:
		'''------------------------------
		---Connected-(INTERNET)----------
		------------------------------'''
		if not "Q" in printpoint:
			if connected and (count in count10):
				if systemplatformwindows: output = terminal('ping en.wikipedia.org -n 1',"Connected")
				elif systemplatformlinux or systemplatformlinuxraspberrypi: output = terminal('ping -W 1 -w 1 -4 -q en.wikipedia.org',"Connected")
				elif systemplatformandroid: output = terminal('ping -W 1 -w 1 -c 1 en.wikipedia.org',"Connected")
				else: output = ""
			else:
				if systemplatformwindows: output = terminal('ping www.google.co.il -n 1',"Connected")
				elif systemplatformlinux or systemplatformlinuxraspberrypi: output = terminal('ping -W 1 -w 1 -4 -q www.google.co.il',"Connected")
				elif systemplatformandroid: output = terminal('ping -W 1 -w 1 -c 1 www.google.co.il',"Connected")
				else: output = ""
				
			if output != "" and not "could not find" in output and not "Netwok is unreachable" in output:
				if systemplatformlinux or systemplatformlinuxraspberrypi:
					if "1 packets received" in output or not "100% packet loss" in output: printpoint = printpoint + "5"			
				elif systemplatformwindows:
					if "Received = 1" in output or not "100% loss" in output: printpoint = printpoint + "5"
				elif systemplatformandroid:
					if not "down broadcast" in output and "up broadcast" in output: printpoint = printpoint + "5"
			else:
				printpoint = printpoint + "Z"
				#extra = extra + newline + "output" + space2 + str(output)
				
			if not "5" in printpoint and not "6" in printpoint:
				'''Try another host'''
				if systemplatformwindows: output = terminal('ping www.facebook.com -n 1',"Connected")
				elif systemplatformlinux or systemplatformlinuxraspberrypi: output = terminal('ping -W 1 -w 1 -4 -q www.facebook.com',"Connected")
				elif systemplatformandroid: output = terminal('ping -W 1 -w 1 -c 1 www.facebook.com',"Connected")
				else: output = ""
				
				if output != "" and not "could not find" in output and not "Netwok is unreachable" in output:
					if systemplatformlinux or systemplatformlinuxraspberrypi:
						if "1 packets received" in output or not "100% packet loss" in output: printpoint = printpoint + "5"
						elif "bad address" in output or output == None: printpoint = printpoint + "6"
					elif systemplatformwindows:
						if "Received = 1" in output or not "100% loss" in output: printpoint = printpoint + "5"
					elif systemplatformandroid:
						if not "down broadcast" in output and "up broadcast" in output: printpoint = printpoint + "5"
				elif output != "" and "Q" in printpoint: pass
				else: printpoint = printpoint + "6"
			
			if "5" in printpoint:
				'''CONNECTED'''
				setSkinSetting('1','Connected','true')
				if not connected: printpoint = printpoint + "_UP_"
				else: printpoint = printpoint + "7"
			elif "6" in printpoint:
				'''NOT CONNECTED'''
				setSkinSetting('1','Connected','false')
				if connected: printpoint = printpoint + "_DOWN_"
				printpoint = printpoint + "9"
			else:
				'''SEMI CONNECTED'''
				printpoint = printpoint + "Q"

			'''---------------------------'''
			'''1 packets transmitted, 0 packets received, 100% packet loss'''
			'''1 packets transmitted, 1 packets received, 0% packet loss
			   round-trip min/avg/max = 70.325/70.325/70.325 ms'''
			'''---------------------------'''

		if not "9" in printpoint and not "Q" in printpoint:
			'''------------------------------
			---setPing-ms--------------------
			------------------------------'''
			output2 = output
			output2len = len(output2)
			output2lenS = str(output2len)
			
			if systemplatformlinux or systemplatformlinuxraspberrypi: start_len = output2.find("min/avg/max =", 0, output2len)
			elif systemplatformwindows: start_len = output2.find("Average =", 0, output2len)
			elif systemplatformandroid: start_len = output2.find("min/avg/max/mdev =", 0, output2len)
			
			start_lenS = str(start_len)
			if systemplatformlinux or systemplatformlinuxraspberrypi: start_lenN = int(start_lenS) + 14
			elif systemplatformwindows: start_lenN = int(start_lenS) + 10
			elif systemplatformandroid: start_lenN = int(start_lenS) + 19
			
			if systemplatformlinux or systemplatformlinuxraspberrypi: end_len = output2.find("/", start_lenN, output2len)
			elif systemplatformwindows: end_len = output2.find("ms", start_lenN, output2len)
			elif systemplatformandroid: end_len = output2.find("/", start_lenN, output2len)
			
			end_lenS = str(end_len)
			end_lenN = int(end_lenS)
			found = output2[start_lenN:end_lenN]
			foundS = str(found)
			try: foundF = float(foundS)
			except: foundF = ""
			'''---------------------------'''
			if not systemplatformwindows:
				mid_len = output2.find(".", start_lenN, end_lenN)
				mid_lenS = str(mid_len)
				mid_lenN = int(mid_lenS)
				totalnumN = mid_lenN - start_lenN
				totalnumS = str(start_lenN)
				'''---------------------------'''
				if foundF != "":
					found2 = round(foundF)
					found2S = str(found2)
				else:
					found2S = foundS
				if ".0" in found2S: found2S = found2S.replace(".0","",1)
				'''---------------------------'''
			else:
				found2S = foundS
				mid_lenS = ""
				'''---------------------------'''
			if admin and admin2: extra = newline + "output2len" + space2 + output2lenS + space + "start_len" + space2 + start_lenS + space + "end_len" + space2 + end_lenS + space + "found/2" + space2 + foundS + "/" + found2S + space + "mid_len" + space2 + mid_lenS
			'''---------------------------'''
		elif "9" in printpoint:
			found2S = "D/C"
		else:
			found2S = "None"
			
		'''------------------------------
		---setPing-----------------------
		------------------------------'''
		A1  = [1 , 11, 21, 31, 41 , 51]
		A2  = [2 , 12, 22, 32, 42 , 52]
		A3  = [3 , 13, 23, 33, 43 , 53]
		A4  = [4 , 14, 24, 34, 44 , 54]
		A5  = [5 , 15, 25, 35, 45 , 55]
		A6  = [6 , 16, 26, 36, 46 , 56]
		A7  = [7 , 17, 27, 37, 47 , 57]
		A8  = [8 , 18, 28, 38, 48 , 58]
		A9  = [9 , 19, 29, 39, 49 , 59]
		A10 = [10, 20, 30, 40, 50 , 60]
		'''---------------------------'''
		setsetting('Ping_Now',found2S)
		setSkinSetting("0", 'Ping_Now', found2S)
		if   count in A1:  setsetting('Ping_1',  found2S)
		elif count in A2:  setsetting('Ping_2',  found2S)
		elif count in A3:  setsetting('Ping_3',  found2S)
		elif count in A4:  setsetting('Ping_4',  found2S)
		elif count in A5:  setsetting('Ping_5',  found2S)
		elif count in A6:  setsetting('Ping_6',  found2S)
		elif count in A7:  setsetting('Ping_7',  found2S)
		elif count in A8:  setsetting('Ping_8',  found2S)
		elif count in A9:  setsetting('Ping_9',  found2S)
		elif count in A10: setsetting('Ping_10', found2S)
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if not "Q" in printpoint and not "9" in printpoint: setsetting('Ping_Connected',"true")
	else: setsetting('Ping_Connected',"false")
	if connected2 != "": connected2S = "true"
	else: connected2S = "false"
	if connected3 != "": connected3S = "true"
	else: connected3S = "false"
	if (admin and admin2 and admin3 and 1 + 1 == 3) or count == 0 or "_DOWN_" in printpoint or "_UP_" in printpoint:
		print printfirst + space + "connectioncheck_LV" + printpoint + space + "count" + space2 + str(count) + space + "connected2/3" + space2 + connected2S + "/" + connected3S + extra
		'''---------------------------'''

def setPing_Rate(admin, admin2, Ping_Rate, Ping_1, Ping_2, Ping_3, Ping_4, Ping_5, Ping_6, Ping_7, Ping_8, Ping_9, Ping_10):
	'''------------------------------
	---1=LOW---5=HIGH----------------
	------------------------------'''
	try:
		Ping_1N  = int(Ping_1)
		Ping_2N  = int(Ping_2)
		Ping_3N  = int(Ping_3)
		Ping_4N  = int(Ping_4)
		Ping_5N  = int(Ping_5)
		Ping_6N  = int(Ping_6)
		Ping_7N  = int(Ping_7)
		Ping_8N  = int(Ping_8)
		Ping_9N  = int(Ping_9)
		Ping_10N = int(Ping_10)
		'''---------------------------'''
		pingtotalN = Ping_1N + Ping_2N + Ping_3N + Ping_4N + Ping_5N + Ping_6N + Ping_7N + Ping_8N + Ping_9N + Ping_10N
		pingtotalS = str(pingtotalN)
		pingtotal2N = pingtotalN / 10
		pingtotal2S = str(pingtotal2N)
		'''---------------------------'''
		pinglevel5 = 100
		pinglevel4 = 150
		pinglevel3 = 200
		pinglevel2 = 250
		pinglevel1 = 300
		'''---------------------------'''
		if pingtotal2N < pinglevel5: Ping_Rate2 = "5"
		elif pingtotal2N < pinglevel4: Ping_Rate2 = "4"
		elif pingtotal2N < pinglevel3: Ping_Rate2 = "3"
		elif pingtotal2N < pinglevel2: Ping_Rate2 = "2"
		else: Ping_Rate2 = "1"
		'''---------------------------'''
		#Ping_Rate2 = getsetting('Ping_Rate')
		setsetting('Ping_Rate',Ping_Rate2)
		setSkinSetting("0", 'Ping_Rate', Ping_Rate2)
		'''---------------------------'''
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if admin and admin2 and admin3 and 1 + 1 == 3: print printfirst + space + "setPing_Rate" + space2 + "pingtotal/2" + space2 + pingtotalS + " / 10 = " + pingtotal2S + space + "Ping_Rate" + space2 + Ping_Rate + " - " + Ping_Rate2
		'''---------------------------'''
	except:
		setsetting('Ping_Rate',"1")
		setSkinSetting("0", 'Ping_Rate', "1")
		if admin and admin2 and admin3 and 1 + 1 == 3: print printfirst + space + "setPing_Rate" + space2 + "Ping_Rate" + space2 + "1"
		'''---------------------------'''

def setSkin_Name(Skin_Name):
	Skin_Name2 = xbmc.getSkinDir()
			
	if Skin_Name != Skin_Name2:
		setsetting('Skin_Name',Skin_Name2)
		print printfirst + space + "setSkin_Name" + space2 + Skin_Name + space4 + Skin_Name2
	'''---------------------------'''
	return Skin_Name2
	
def setTime_Delay(admin, admin2, Time_Delay, count, systemidle3, playerhasvideo, playerhasmedia, playerpaused, performance, Ping_Connected):
	#from variable import A10
	
	if count in A10:
		name = 'setTime_Delay' ; Time_Delay2 = Time_Delay ; playerfilename = xbmc.getInfoLabel('Player.Filename')
		
		if performance or Ping_Connected == 'false': value = 100
		else: value = 20
		
		if not systemidle3:
			setsetting('Time_Delay', "0")
			Time_Delay2 = "0"
		elif playerhasmedia and not playerpaused and not "playHTPT.mp3" in playerfilename: pass
		else:
			Time_Delay2 = calculate('service.htpt','Time_Delay', value ,Time_Delay)
			setsetting('Time_Delay',Time_Delay2)
		
		if admin and admin2: print printfirst + name + space + "Time_Delay/2" + space2 + str(Time_Delay) + space4 + str(Time_Delay2) + space + "count" + space2 + str(count) + space + "systemidle3" + space2 + str(systemidle3) + space + "playerpaused" + space2 + str(playerpaused)
		'''---------------------------'''
	elif int(Time_Delay) > 300 and not systemidle3: setsetting('Time_Delay', "0")

def setGeneral_Timer(admin, admin2, General_Timer, count):
	TypeError = "" ; extra = ""
	General_Timer2 = calculate('service.htpt','General_Timer','1',General_Timer)
	try: General_Timer2 = int(General_Timer2)
	except Exception, TypeError: extra = newline + "TypeError" + space2 + str(TypeError)
	if TypeError == "":
		if General_Timer2 >= 60: General_Timer2 = 1
		General_Timer2S = str(General_Timer2)
		#setsetting_custom1('service.htpt','General_Timer',General_Timer2S)
		setsetting('General_Timer', General_Timer2S)
	if admin and admin2 or extra != "": print printfirst + space + "General_Timer" + space2 + str(count) + extra
	'''---------------------------'''
	
def SetTime_Pass(admin, admin2, Time_Pass):
	Time_Pass2 = calculate('service.htpt','Time_Pass','1',Time_Pass)
	setsetting('Time_Pass',Time_Pass2)
	#setsetting_custom1('service.htpt','Time_Pass',Time_Pass2)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and admin2: print printfirst + "setTime_Pass" + space2 + "Time_Pass" + space2 + Time_Pass + " - " + Time_Pass2
	'''---------------------------'''

def SetSkin_UpdateTimer(admin, admin2, Skin_UpdateTimer):
	'''------------------------------
	---Skin_UpdateTimer--------------
	------------------------------'''
	Skin_UpdateTimer2 = calculate('service.htpt','Skin_UpdateTimer','2',Skin_UpdateTimer)
	setsetting('Skin_UpdateTimer',Skin_UpdateTimer2)
	#setsetting_custom1('service.htpt','Skin_UpdateTimer',Skin_UpdateTimer2)
	'''---------------------------'''
	if Skin_UpdateTimer == "119": notification(localize(24092) + ".", addonString_servicehtpt(10),"",1000) #Checking for add-on updates
	elif Skin_UpdateTimer == "118": notification(localize(24092) + "..", addonString_servicehtpt(10),"",1000) #Checking for add-on updates
	elif Skin_UpdateTimer == "117": notification(localize(24092) + "...", addonString_servicehtpt(10),"",1000) #Checking for add-on updates
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and admin2: print printfirst + "Skin_UpdateTimer" + space2 + Skin_UpdateTimer + " - " + Skin_UpdateTimer2
	'''---------------------------'''
	
def setSkin_UpdateCount2(admin, Skin_UpdateCount, Time_Pass):
	'''------------------------------
	---Skin_UpdateCount2-+1----------
	------------------------------'''
	Skin_UpdateCount2 = Skin_UpdateCount
	TimeSequenceN = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020]
	Time_PassN = int(Time_Pass)
	if Time_PassN in TimeSequenceN:
		Skin_UpdateCount2 = calculate('service.htpt','Skin_UpdateCount','1',Skin_UpdateCount)
		setsetting('Skin_UpdateCount2', Skin_UpdateCount2)
		#setsetting_custom1('service.htpt','Skin_UpdateCount2',Skin_UpdateCount2)
		'''---------------------------'''	
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if Skin_UpdateCount2 != Skin_UpdateCount: print printfirst + "setSkin_UpdateCount2" + space2 + "Time_Pass" + space2 + Time_Pass + space + "Skin_UpdateCount" + space2 + Skin_UpdateCount + " - " + Skin_UpdateCount2
	'''---------------------------'''	
	return Skin_UpdateCount2
	
def UpdateAddons(admin, Skin_UpdateCount, Skin_UpdateCount2):
	'''------------------------------
	---UPDATE-REPO+ADDONS------------
	------------------------------'''
	TypeError = ""
	addon = 'repository.pulsarunofficial'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		try: removeaddons(addon,"123")
		except Exception, TypeError: TypeError = Newline + "TypeError" + space2 + str(TypeError)
		setsetting_custom1('service.htpt.fix','Fix_2',"true")
		'''---------------------------'''
	else:
		xbmc.executebuiltin('UpdateAddonRepos')
		xbmc.executebuiltin('UpdateLocalAddons')
		'''---------------------------'''
	setsetting('Skin_UpdateTimer',"120")
	'''---------------------------'''
	
	'''------------------------------
	---Skin_UpdateCount-+1-----------
	------------------------------'''
	setsetting('Skin_UpdateCount',Skin_UpdateCount2)
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + space + "UpdateAddons" + space + "Skin_UpdateCount/2" + space2 + Skin_UpdateCount + " - " + Skin_UpdateCount2 + str(TypeError)
	'''---------------------------'''

def setSkin_Update(admin, Skin_Version, htptskinversion, Skin_Update):
	'''------------------------------
	---CHECK-FOR-SKIN-UPDATE---------
	------------------------------'''
	if Skin_Version != htptskinversion and Skin_Update == "false":
		Skin_Update2 = "true"
		setsetting('Skin_UpdateLog',"true")
		xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=19)')
	else:
		Skin_Update2 = "false"
		
	if Skin_Update != Skin_Update2: setsetting('Skin_Update',Skin_Update2)
	'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if Skin_Update != Skin_Update2: print printfirst + "setSkin_Update" + space2 + "Skin_Update" + space2 + Skin_Update + " - " + Skin_Update2 + space + "htptskinversion" + space2 + str(htptskinversion)
	'''---------------------------'''
	
def setSkin_UpdateDate(admin, Skin_Version, htptskinversion, Skin_Update, Skin_UpdateDate):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import datenowS
	'''---------------------------'''
	#setsetting_custom1('service.htpt','Skin_UpdateDate',datenowS)
	if Skin_UpdateDate != datenowS:
		setsetting('Skin_UpdateDate',datenowS)
	#dateleft = stringtodate(skinsetting3,'%Y-%m-%d')
	#dateleft2 = str(dateleft)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "setSkin_UpdateDate" + space2 + "Skin_UpdateDate" + space2 + Skin_UpdateDate + " - " + datenowS
	'''---------------------------'''
	
def setSkin_Version(admin, Skin_Version, htptskinversion):
	'''------------------------------
	---CHECK-FOR-SKIN-UPDATE-2-------
	------------------------------'''
	if Skin_Version != htptskinversion:
		setsetting('Skin_Version',htptskinversion)
		'''---------------------------'''	
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "setSkin_Version" + space2 + "Skin_Version" + space2 + Skin_Version + " - " + htptskinversion
		'''---------------------------'''	

def setSkin_UpdateLog(admin, Skin_Version, Skin_UpdateDate, datenowS, Skin_Name):	
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	printpoint = ""
	number2S = ""
	datenowD = stringtodate(datenowS,'%Y-%m-%d')
	datedifferenceD = stringtodate(Skin_UpdateDate, '%Y-%m-%d')
	datedifferenceS = str(datedifferenceD)
	if "error" in [datenowD, datedifferenceD]: printpoint = printpoint + "9"
	try:
		number2 = datenowD - datedifferenceD
		number2S = str(number2)
		printpoint = printpoint + "2"
		'''---------------------------'''
	except:
		printpoint = printpoint + "9"
		'''---------------------------'''
	if not "9" in printpoint and xbmc.getSkinDir() == 'skin.htpt':
		printpoint = printpoint + "4"
		if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
		elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
		else: number2S = "0"
		if admin: notification("number2S:" + number2S,"","",2000)
		number2N = int(number2S)
		'''---------------------------'''
		if number2N == 0: header = '[COLOR=Yellow]' + localize(79201) + space + localize(33006) + " - " + Skin_Version + '[/COLOR]'
		elif number2N == 1: header = '[COLOR=Green]' + localize(79201) + space + addonString_servicehtpt(5).encode('utf-8') + " - " + Skin_Version + '[/COLOR]'
		elif number2N <= 7: header = '[COLOR=Purple]' + localize(79201) + space + addonString_servicehtpt(6).encode('utf-8') + " - " + Skin_Version + '[/COLOR]'
		else: header = ""
		'''---------------------------'''
		if os.path.exists(skinlog_file) and scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true":
			log = open(skinlog_file, 'r')
			message2 = log.read()
			log.close()
			message2S = str(message2)
			message3 = message2[70:8000]
			message3 = '"' + message3 + '"'
			message3S = str(message3)
			if header != "": diaogtextviewer(header, message2)
			'''---------------------------'''
			#setSkinSetting("0", 'MessagesChangeLog', message3S)
			setsetting('Skin_UpdateLog',"false")
			'''---------------------------'''
			
	setsetting('Skin_UpdateLog',"false")
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "setSkin_UpdateLog_LV" + printpoint + space2 + "Skin_UpdateDate" + space2 + Skin_UpdateDate + " - " + datenowS + space + "(" + number2S + ")" + space + "Skin_UpdateLog" + space2 + Skin_UpdateLog
	'''---------------------------'''

def startup(admin):
	xbmc.sleep(5500)
	
	if os.path.exists(skin_path) and xbmc.getCondVisibility('System.HasAddon(skin.htpt)'):
		from shared_modules4 import *
		printpoint, guisettings_file_ = guicheck(admin)
		guikeeper(admin, guicheck=printpoint, guiread=guisettings_file_)
		xbmc.sleep(1000)
	
	if xbmc.getSkinDir() == 'skin.htpt':
		connectioncheck(admin, admin2, 0, systemidle3, Ping_Now, Ping_Connected) ; xbmc.sleep(1000)
		if not startupmusic:
			if os.path.exists(skin_music_path + "playHTPT2.flac") and not startupmusicstr:
				xbmc.executebuiltin('PlayMedia('+skin_music_path+'playHTPT2.flac)')
			else:
				notification("Trying to play custom file","","",1000)
				xbmc.executebuiltin('PlayMedia($INFO[Skin.String(StartUpMusic)]')
		
		if not startupvolumestr: xbmc.executebuiltin('SetVolume(70)')
		else: xbmc.executebuiltin('SetVolume('+startupvolumestr+')')
		
		addon = 'script.htpt.install'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunScript(script.htpt.install,,?mode=27)')
	
	addon = 'plugin.video.htpt.kids'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'):
		setsetting_custom1(addon, 'Addon_UpdateLog', "true")
	
	addon = 'plugin.video.htpt.gopro'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'):
		setsetting_custom1(addon, 'Addon_UpdateLog', "true")
	
	addon = 'plugin.video.htpt.music'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'):
		setsetting_custom1(addon, 'Addon_UpdateLog', "true")
		
	resources_path = os.path.join(addonPath, 'resources', '')
	icons_file = os.path.join(resources_path, 'icons.zip')
	if os.path.exists(icons_file):
		if admin: notification("Extracting icons folder","...","",4000)
		ExtractAll(icons_file, resources_path)
		admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
		if not admin3: removefiles(icons_file)
		xbmc.sleep(500)
	elif admin: print printfirst + icons_file