#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys
#import datetime, time
from variables import *
from shared_modules import *

def mode0(admin, name, printpoint):
	'''------------------------------
	---TEST--------------------------
	------------------------------'''
	#print "localize(20122)" + space2 + localize(20122)
	#xbmc.executebuiltin('Skin.Theme(SKINDEFAULT)')
	#x1 = 'Skin.Theme'
	#x2 = 'SKINDEFAULT'
	#xbmc.executebuiltin(''+x1+'('+ x2 +')')
	#import py_compile
	#file = os.path.join(addonPath, '', 'modules.py')
	#py_compile.compile(file)
	if 1 + 1 == 3:
		log = open(skinlog_file, 'r')
		message2 = log.read()
		log.close()
		message2S = str(message2)
		message3 = message2[70:8000]
		message3 = '"' + message3 + '"'
		message3S = str(message3)
		header = "test"
		diaogtextviewer(header, message2)
		
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=201&value=1)')
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#value = []
	#value.append("copylibrarydir" + space2 + copylibrarydir + newline)
	#value.append("library_path" + space2 + library_path + newline)
	
	#print printfirst + "mode0-test: "  + str(value)
	'''---------------------------'''
	#htptservice_path = os.path.join(addons_path,'service.htpt','')
	#path = os.path.join(htptservice_path, 'specials', 'tools', 'EAT-start')
	#terminal('TASKKILL /im EAT_gil900.exe /f',"EAT-end")
	
	
	#import zlib
	#p2pstreams_path = os.path.join(addondata_path, 'plugin.video.p2p-streams', '')
	#xbmc.executebuiltin('RunScript(plugin.program.advanced.launcher,?rom=SEARCH_COMMAND/launcher=%%SEARCH%%)')
	#xbmc.executebuiltin('ActivateWindow(10001,"plugin://plugin.program.advanced.launcher/?%%GET_INFO%%")')
	#xbmc.executebuiltin('ActivateWindow(10001,"plugin://plugin.program.advanced.launcher/?$INFO[Skin.String(search1)]/%%SEARCH_ITEM%%")')
	#notification("ext","","",2000)
	#file = "Arcade_4P.zip"
	#ExtractAll(temp_path + file, temp_path)
	
	#terminal('"'+path+'"', 'EAT_gil900.exe')
	
	#xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=13)')
	#mode64(admin, "1")
	
	#systemmemorytotal2 = systemmemorytotal.replace("MB","")
	
	#print systemmemorytotal2
	#Skin_Name2 = terminal('find "<skin>" '+userdata_path+'guisetings.xml',"GUI1") #UNTESTED
	#output = terminal('find "<skin>" '+userdata_path+'guisettings.xml',"GUI1") #UNTESTED
	#Skin_Name2 = CleanString(output, filter=['----------', userdata_path + 'guisettings.xml', '<skin>', '</skin>'])
	
	#print "Skin_Name22" + space + Skin_Name2 + newline + "userdata_path" + space2 + userdata_path
	'''---------------------------'''
	#setSkinSetting('0', 'TopVideoInformation4', 'special://thumbnails/http%3a%2f%2fthetvdb.com%2fbanners%2fposters%2f74845-2.jpg')
	
	#echo executing copy.sh from skin && sleep 1 && echo killall && killall -9 kodi.bin && sed -i "s/$SKIN$ALL/$SKIN$SKIN_/g" $GUI && sed -i "s/$SKIN2$ALL/$SKIN$SKIN_/g" $GUI
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=50)') ; xbmc.sleep(1000)
	#autoexec_path = os.path.join(userdata_path, 'Autoexec.py')
	
	#xbmc.executebuiltin('RunScript('+autoexec_path+')')
	#removefiles(guisettings_file)
	#copyfiles(guisettings2_file, guisettings_file, chmod="", mount=False)
	#import shutil
	#shutil.copyfile(guisettings_file, guisettings4_file)
	#from shared_modules4 import *
	#guiset(admin, guiread="")
	#print "ahh" + space + xbmc.getInfoLabel('System.BuildVersion')
	#addonid2 = 'service.subtitles.torec'
	#xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addonid2 +'),returned')
	#xbmc.executebuiltin('Action(Down)')
	#xbmc.executebuiltin('Action(Select)')
	#setAutoSettings("0", addonid2="")
	#xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=20)')
	#xbmc.executebuiltin('SetFocus(9001)')
	#checkID(admin, idstr, 'ID1')
	#print "test" + space2 + xbmc_path
	#addonid2 = 'repository.ninbora'
	#xbmc.executebuiltin('ActivateWindow(10040,plugin://'+ addonid2 +'),returned')
	#xbmc.executebuiltin("UpdateLocalAddons")
	if 1 + 1 == 3:
		backupname = "htpt_backup"
		backupname2 = "htpt_backup2"
		backuppath = home_path
		backupsize = getFileAttribute(2, backuppath + backupname + ".zip")
		notification("backupsize", str(backupsize), "", 4000)
	#CreateZip(config_path, backuppath + backupname, filteron=['samba.conf', 'autostart.sh'], level=0, append=False, ZipFullPath=True, temp=True)
	#CreateZip(userdata_path.encode('utf-8'), backuppath + backupname, filteron=['advancedsettings.xml', 'sources.xml', 'keymaps'], filteroff=[], level=0, append=True, ZipFullPath=True, temp=False)
	#printpoint = installaddon2(admin, 'metadata.common.imdb.com', update=False)
	#shutil.copyfile(guisettings4_file, guisettings_file) ; killall(admin)
	#copyfiles(guisettings2_file, guisettings_file, chmod="", mount=False)
	
	#image://http%3a%2f%2fthetvdb.com%2fbanners%2fposters%2f74845-2.jpg/
	#ExtractAll("E:\\4P.zip", 'E:\\')
	'''---------------------------'''
	#xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedactorinfo,name=Dwayne)')
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=100)')
	#mode55(admin)
	#systemtemperatureunits = xbmc.getInfoLabel('System.TemperatureUnits')
	#if xbmc.getCondVisibility('SubString(System.TemperatureUnits,F)'): notification(systemtemperatureunits, "yes", "", 2000)
	#sgbsubtitlespauseonsearch = xbmc.getCondVisibility('System.GetBool(subtitles.pauseonsearch)')
	#notification(str(sgbsubtitlespauseonsearch), "", "", 1000)
	'''---------------------------'''
	#playlistid = 'PLPWc8VdaIIsDcjHMTBavJG-Rm8p0wvvW_'
	#xbmc.executebuiltin('RunScript(script.extendedinfo,info=youtubeplaylist,id=PLPWc8VdaIIsDcjHMTBavJG-Rm8p0wvvW_)')
	#xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?playlist_id='+playlistid+')')
	'''---------------------------'''
	
	if 1 + 1 == 3:
		backupname = "htpt_backup"
		backupname2 = "htpt_backup2"
		backuppath = home_path
		if systemplatformwindows: restorepath = home_path
		else: restorepath = '/storage'
		ExtractAll(backuppath + backupname + ".zip", restorepath)
	
	
	
	'''---------------------------'''
	
	
	'''---------------------------'''
	
	
	'''---------------------------'''
	
	#xbmc.executebuiltin('RunScript(script.htpt.refresh,,?mode=3)')
	if 1+ 1 == 3:
		if systemplatformwindows: infile = "Z:/addons/plugin.video.sdarot.tv/sdarottv.py"
		else: infile = "/storage/.kodi/addons/plugin.video.sdarot.tv/sdarottv.py"
		old_word = "finalVideoUrl,VID = getFinalVideoUrl(series_id,season_id,epis,silent=True)"
		new_word = "finalVideoUrl,VID = getFinalVideoUrl(series_id,season_id,epis,silent=False)"
		replace_word(infile,old_word,new_word)
		#xbmc.executebuiltin('ActivateWindow(10025,special://home/addons)')
		#xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id=gnZuo0he5kk)')
	pass
	#notification(xbmc.getInfoLabel('System.ProfileName'),"","",5000)
	#xbmc.executebuiltin('Action(PageUp)')
	#xbmc.sleep(500)
	#xbmc.executebuiltin('Control.SetFocus(2)')
	#xbmc.executebuiltin('ActivateWindow(10025,special://userdata/library/,return)')
	#terminal('xcopy '+htptservicecopy_path+'manual\\advancedsettings.xml '+userdata_path+' /s /i /y >NUL','advancedsettings.xml')
	#print xbmc.getInfoLabel('System.TotalSpace')
	
	#xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=40)')
	#ExtractAll("D:\\rom\\Arcade\\_GEAR.rar","C:\\")
	#ExtractAll("C:\\_1P.tar","C:\\")
	#ExtractAll("C:\\_1P.7z","C:\\_1P")
	#Clean_Library("10")
	#xbmc.executebuiltin('RunScript(plugin.video.genesis,,?action=library_imdb_watchlist)')
	#Clean_Library("1")
	

	
	
	#xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=20)')
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=0)')
	#xbmc.executebuiltin('RunScript(screensaver.picture.slideshow)')
	#xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=12)')

	#from commondownloader import *
	#returned = doDownload("https://docs.google.com/uc?export=download&id=0B3SUm7A8M6ctNTRhQ21jYUw0ZVk", "C:\\test3.zip", "google", "", "", "")
	#from commondownloader import *
	#doDownload("https://www.dropbox.com/s/zz2se5mfpmt5wbn/Sega%20Master%20System.zip?dl=1", "C:\\test2.zip", 'Media', "", "", "")
	#dialogok("download done","","","")
	#import urllib2
	#import urllib, urllib2, os, sys

	###The pydrive package download
	###page='https://pypi.python.org/packages/source/P/PyDrive/PyDrive-1.0.0.tar.gz'
	###request=urllib.urlretrieve(page, "C:\\" + "pydrive.tar.gz") #pydrive.tar.gz
	###if os.path.exists(os.path.join("C:\\","pydrive.tar.gz")): #os.path.dirname
		###print "YUP THE FILE EXISTS"
		###notification("yes!","","",2000)
	###else:
		###print "nope"			#response = urllib2.urlopen('https://drive.google.com/file/d/0B3SUm7A8M6ctNTRhQ21jYUw0ZVk/view?usp=sharing')
	#html = response.read()
	#f=open("1", 'w')
	#f.write(html)
	#f.close()
	#from downloader import *
	#download("https://www.dropbox.com/s/kxwmwbnjf7f040j/skin.htpt.zip?dl=1", "c:\\test.zip", dp = None) #temp_path #https://drive.google.com/file/d/0B3SUm7A8M6ctNTRhQ21jYUw0ZVk/view?usp=sharing
	
	#DownloadFile("https://drive.google.com/uc?export=download&id=0B3SUm7A8M6ctNTRhQ21jYUw0ZVk", "Media", "C:\\", "C:\\1")
	#systemmemorytotal2 = systemmemorytotal.replace("MB","")
	#notification(systemmemorytotal2,"","",10000)
	#content = ReadList('/storage/shutdown.log')
	#print "HERE" + space2 + newline + str(content)
	#returned, value = getRandom("0",percent=10)
	#if returned == "ok": notification("yeyeye","","",4000)
		
	#xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.genesis/?action=library_imdb_watchlist,return)')
	#removeaddons(['plugin.program.advanced.launcher', 'script.htpt.emu', 'tools.lm_sensors', 'debug.tools.smem', 'screensaver.randomtrailers'],"12")
	#addon = 'plugin.program.advanced.launcher'
	#output = terminal('ls '+addons_path+''+ addon +'/',"script.htpt.emu")
	#output = terminal('ls '+addondata_path+''+ addon +'/',"script.htpt.emu")
	#output = terminal('rm -rf '+addondata_path+''+ addon +'/',addon)
	#print output
	#dp = dialogprogress("",0,"heading","line1","line2","line3")
	#xbmc.sleep(2000)
	#dp = dialogprogress(dp, 10,"heading","line1","line2","line3")
	#xbmc.sleep(2000)
	#dp = dialogprogress(dp, 100,"heading","line1","line2","line3")
	#xbmc.sleep(2000)
	
	'''---------------------------'''
	#print printfirst + space + "test2button" + space2 + az
	'''---------------------------'''
	
	'''---------------------------'''
	
def mode1(admin, name, printpoint):
	'''------------------------------
	---SMART-KEYBOARD-SAVE-VALUE-----
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	if General_ScriptON != "true":
		'''---------------------------'''
		printpoint = printpoint + "1"
		heading = xbmc.getInfoLabel('Control.GetLabel(311)')
		#keyboard = xbmc.Keyboard(Current_Input,heading,int(Current_Option))
		#input = keyboard.getText()
		#setsetting_custom1('script.htpt.smartkeyboard','Current_Input',input)
		#setGeneral_ScriptON("0", General_ScriptON, str(mode))
		'''---------------------------'''
		input = dialogkeyboard(Current_Input, heading, 0, '1', "", "")
		#keyboard = xbmc.Keyboard()
		#input = keyboard.getText()
		#input = "test"
		setsetting_custom1('script.htpt.smartkeyboard','Current_Input',input)
		setsetting_custom1('script.htpt.smartkeyboard','Current_Option',0)
		'''------------------------------
		---SMART-KEYBOARD-SAVE-VALUE-----
		------------------------------'''
		if input != "skip":
			printpoint = printpoint + "2"
			setSkinSetting("0", 'smartkeyboardH0', input)
			xbmc.sleep(1000) #time to set setting
			if not input in smartkeyboardHL:
				'''------------------------------
				---NEW-VALUE---------------------
				------------------------------'''
				printpoint = printpoint + "3"
				setSkinSetting("0", 'smartkeyboardH5', smartkeyboardH4)
				setSkinSetting("0", 'smartkeyboardH4', smartkeyboardH3)
				setSkinSetting("0", 'smartkeyboardH3', smartkeyboardH2)
				setSkinSetting("0", 'smartkeyboardH2', smartkeyboardH1)
				setSkinSetting("0", 'smartkeyboardH1', input)
				'''---------------------------'''
			else:
				'''------------------------------
				---EXIST-VALUE-------------------
				------------------------------'''
				printpoint = printpoint + "4"
				if input != smartkeyboardH1:
					if input == smartkeyboardH2:
						printpoint = printpoint + "5"
						setSkinSetting("0", 'smartkeyboardH1', input)
						setSkinSetting("0", 'smartkeyboardH2', smartkeyboardH1)
						'''---------------------------'''
					elif input == smartkeyboardH3:
						printpoint = printpoint + "6"
						setSkinSetting("0", 'smartkeyboardH1', input)
						setSkinSetting("0", 'smartkeyboardH3', smartkeyboardH1)
						'''---------------------------'''
					elif input == smartkeyboardH4:
						printpoint = printpoint + "7"
						setSkinSetting("0", 'smartkeyboardH1', input)
						setSkinSetting("0", 'smartkeyboardH4', smartkeyboardH1)
						'''---------------------------'''
					elif input == smartkeyboardH5:
						printpoint = printpoint + "8"
						setSkinSetting("0", 'smartkeyboardH1', input)
						setSkinSetting("0", 'smartkeyboardH5', smartkeyboardH1)
						'''---------------------------'''
					else: printpoint = printpoint + "9"
				else: printpoint = printpoint + "9"
				'''---------------------------'''
		
		setsetting_custom1('script.htpt.smartkeyboard','Current_Input',"")
		setsetting_custom1('script.htpt.smartkeyboard','Current_Option',0)

	'''---------------------------'''
	#setGeneral_ScriptON("1", General_ScriptON, str(mode))
	'''---------------------------'''

def mode2(admin, name, printpoint):
	'''------------------------------
	---SMART-KEYBOARD-COPY-----------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	printpoint = printpoint + "1"
	#keyboard.doModal()
	#input2 = keyboard.getText()
	#notification("input2: " + input2,"input: " + input,"",2000)
	setSkinSetting("0", "smartkeyboardC" + smartkeyboardPN, Current_Input)
	'''---------------------------'''

def mode3(admin, name, printpoint):
	'''------------------------------
	---SMART-KEYBOARD-HISTORY--------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	import json
	xbmc.executebuiltin('Action(Close)')
	xbmc.sleep(200)
	if smartkeyboardHN == '1': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardH1 +'","done":false}}')
	if smartkeyboardHN == '2': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardH2 +'","done":false}}')
	if smartkeyboardHN == '3': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardH3 +'","done":false}}')
	if smartkeyboardHN == '4': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardH4 +'","done":false}}')
	if smartkeyboardHN == '5': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardH5 +'","done":false}}')
	xbmc.executebuiltin('SetFocus(3000)')
	'''---------------------------'''

def mode4(admin, name, printpoint):
	'''------------------------------
	---SMART-KEYBOARD-PASTE----------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	import json
	xbmc.executebuiltin('Action(Close)')
	xbmc.sleep(200)
	if smartkeyboardPN == '1': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardC1 +'","done":false}}')
	if smartkeyboardPN == '2': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardC2 +'","done":false}}')
	if smartkeyboardPN == '3': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardC3 +'","done":false}}')
	if smartkeyboardPN == '4': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardC4 +'","done":false}}')
	if smartkeyboardPN == '5': xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ smartkeyboardC5 +'","done":false}}')
	xbmc.executebuiltin('SetFocus(3000)')
	'''---------------------------'''
	
def mode5(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode5(admin, name, printpoint)
	'''---------------------------'''

def mode6(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode6(admin, name, printpoint)
	'''---------------------------'''

def mode7(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode7(admin, name, printpoint)
	'''---------------------------'''
	
def mode8(admin, name, printpoint):
	'''------------------------------
	---SMART-SUBTITLE-SEARCH---------
	------------------------------'''
	import json
	name = 'SMART-SUBTITLE-SEARCH'
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	extra = newline + ""
	input = ""
	isTV = 'false'
	isMovie = 'false'
	printpoint = ""
	TypeError = ""
	TypeError2 = ""
	listL = ["0","1"]
	
	'''------------------------------
	---MOVIE/TV----------------------
	------------------------------'''
	if scripthtptrefresh_Current_M_T in listL:
		if scripthtptrefresh_Current_M_T == "0": isMovie = 'true'
		elif scripthtptrefresh_Current_M_T == "1": isTV = 'true'
		'''---------------------------'''
	else:
		if (videoplayertvshowtitle != "" and videoplayerseason != "" and videoplayerepisode != "") or scripthtptrefresh_Current_M_T == "1": isTV = 'true'
		elif (videoplayertitle != "" and (videoplayeryear != "" or videoplayercountry != "" or videoplayertagline != "")) or scripthtptrefresh_Current_M_T == "0": isMovie = 'true'
		'''---------------------------'''
		
	xbmc.executebuiltin('SendClick(160)')

	'''------------------------------
	---INPUT-------------------------
	------------------------------'''
	
	if scripthtptrefresh_Current_M_T in listL and scripthtptrefresh_Current_Name != "":
		try:
			hebtest = scripthtptrefresh_Current_Name.decode('utf-8')
			#setSkinSetting("1","Test",hebtest)
			print hebtest
			printpoint = printpoint + "1"
			'''---------------------------'''
		except Exception, TypeError: TypeError2 = str(TypeError2) + str(TypeError)
	else: extra = extra + space + "Current_M_T" + space2 + str(scripthtptrefresh_Current_M_T)
	
	if not "1" in printpoint:
		try:
			if isMovie == "true": hebtest = videoplayertitle.decode('utf-8')
			elif isTV == "true": hebtest = videoplayertvshowtitle.decode('utf-8')
			#setSkinSetting("1","Test",hebtest)
			print hebtest
			printpoint = printpoint + "2"
			'''---------------------------'''
		except Exception, TypeError:
			TypeError2 = str(TypeError2) + str(TypeError)
			try:
				hebtest = playertitle.decode('utf-8')
				#setSkinSetting("1","Test",hebtest)
				print hebtest
				printpoint = printpoint + "3"
				'''---------------------------'''
			except Exception, TypeError:
				TypeError2 = str(TypeError2) + str(TypeError)
				printpoint = printpoint + "9"
	
	if "1" in printpoint: input = scripthtptrefresh_Current_Name
	elif "2" in printpoint:
		if isMovie == 'true': input = videoplayertitle + space + videoplayeryear # + space + videoplayervideoresolution #+ space + videoplayervideocodec
		elif isTV == 'true':
			try: seasonN = int(videoplayerseason)
			except: seasonN = ""
			try: episodeN = int(videoplayerepisode)
			except: episodeN = ""
			if seasonN == "" or episodeN == "" or videoplayertvshowtitle == "": input = videoplayertitle
			elif seasonN < 10 and episodeN < 10: input = videoplayertvshowtitle + " " + 'S0' + videoplayerseason + 'E0' + videoplayerepisode
			elif seasonN > 10 and episodeN > 10: input = videoplayertvshowtitle + " " + 'S' + videoplayerseason + 'E' + videoplayerepisode
			elif seasonN > 10 and episodeN < 10: input = videoplayertvshowtitle + " " + 'S' + videoplayerseason + 'E0' + videoplayerepisode
			elif seasonN < 10 and episodeN > 10: input = videoplayertvshowtitle + " " + 'S0' + videoplayerseason + 'E' + videoplayerepisode
			'''---------------------------'''
	elif "3" in printpoint: input = playertitle
	'''---------------------------'''
	if "3" in printpoint or "9" in printpoint:
		input = ""
		notification('$LOCALIZE[75099]','$LOCALIZE[75098]',"",2000)
		'''---------------------------'''
	
	dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
	count = 0
	while count < 10 and not dialogkeyboard and not xbmc.abortRequested:
		count += 1
		xbmc.sleep(100)
		dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
		'''---------------------------'''
	if count < 10: xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ input +'","done":false}}')
	'''---------------------------'''
	if TypeError2 != "": extra = newline + extra + space + "TypeError" + space2 + str(TypeError2)
	print printfirst + name + "_LV" + printpoint + space + "videoplayertvshowtitle = " + videoplayertvshowtitle + " | videoplayerseason = " + videoplayerseason + " | videoplayerepisode = " + videoplayerepisode + " | videoplayertitle = " + videoplayertitle + " | videoplayeryear = " + videoplayeryear + " | videoplayertitle = " + videoplayertitle + space + "playertitle =" + playertitle + space + "VideoCodec" + space2 + videoplayervideocodec + space + "VideoResolution" + space2 + videoplayervideoresolution + extra
	'''---------------------------'''

def mode9(admin, name, Current_Year, Current_M_T):
	'''------------------------------
	---SEMI-AUTO-SUBTITLE-FIND-------
	------------------------------'''
	from variables import yearnowS
	dialogsubtitles2 = xbmc.getInfoLabel('Skin.String(DialogSubtitles2)')
	dialogsubtitlesna1 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA1)')
	dialogsubtitlesna2 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA2)')
	dialogsubtitlesna3 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA3)')
	dialogsubtitlesna4 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA4)')
	dialogsubtitlesna5 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA5)')
	dialogsubtitlesna6 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA6)')
	dialogsubtitlesna7 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA7)')
	dialogsubtitlesna8 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA8)')
	dialogsubtitlesna9 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA9)')
	dialogsubtitlesna10 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA10)')
	subL = [dialogsubtitles2, dialogsubtitlesna1, dialogsubtitlesna2, dialogsubtitlesna3, dialogsubtitlesna4, dialogsubtitlesna5, dialogsubtitlesna6, dialogsubtitlesna7, dialogsubtitlesna8, dialogsubtitlesna9, dialogsubtitlesna10]
	listL = ['Subscenter.org', 'Subtitle.co.il', 'OpenSubtitles.org', 'Torec']
	Subtitle_Service = getsetting('Subtitle_Service')
	dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
	controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)')
	controlhasfocus120 = xbmc.getCondVisibility('Control.HasFocus(120)') #MAIN
	controlhasfocus150 = xbmc.getCondVisibility('Control.HasFocus(150)') #SIDE
	controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
	controlgroup70hasfocus0 = xbmc.getCondVisibility('ControlGroup(70).HasFocus(0)') #OSD BUTTONS
	container120listitemlabel2 = xbmc.getInfoLabel('Container(120).ListItem.Label2')
	container120numitems = 0
	tip = "true"
	count = 0
	count2 = 0 #container120numitems
	countidle = 0
	'''---------------------------'''
	while countidle < 40 and dialogsubtitlesW and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
		if dialogsubtitlesW:
			container120numitems2 = container120numitems
			container120numitems = xbmc.getInfoLabel('Container(120).NumItems') #DialogSubtitles
			try: container120numitems = int(container120numitems)
			except: container120numitems = ""
			'''---------------------------'''
			controlhasfocus120 = xbmc.getCondVisibility('Control.HasFocus(120)') #MAIN
			controlhasfocus150 = xbmc.getCondVisibility('Control.HasFocus(150)') #SIDE
			controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
			controlgroup70hasfocus0 = xbmc.getCondVisibility('ControlGroup(70).HasFocus(0)') #OSD BUTTONS
			'''---------------------------'''
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			container120listitemlabel2 = xbmc.getInfoLabel('Container(120).ListItem.Label2')
			'''---------------------------'''
			
		Subtitle_Search = getsetting('Subtitle_Search')
		dialogsubtitles = xbmc.getInfoLabel('Skin.String(DialogSubtitles)')
		dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
		playerpaused = xbmc.getCondVisibility('Player.Paused')
		'''---------------------------'''
		systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
		systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
		systemidle7 = xbmc.getCondVisibility('System.IdleTime(7)')
		systemidle40 = xbmc.getCondVisibility('System.IdleTime(40)')
		'''---------------------------'''
		
		if controlhasfocus120 and container120numitems > 0 and count2 != 0: count2 = 0
		
		if not dialogkeyboardW and container120numitems != "" and controlgetlabel100 != "":
			
			if count == 0 and Subtitle_Service != "" and Subtitle_Service != controlgetlabel100 and controlgetlabel100 != "":
				'''------------------------------
				---Last_SubService---------------
				------------------------------'''
				if controlhasfocus120: xbmc.executebuiltin('Action(Left)')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",Subtitle_Service,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",Subtitle_Service,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",Subtitle_Service,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",Subtitle_Service,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",Subtitle_Service,100,'Action(Down)','Action(Select)')
				'''---------------------------'''
					
			elif controlhasfocus120 and container120numitems > 0:
				if (container120listitemlabel2 in subL or container120listitemlabel2 == dialogsubtitles2):
					if container120numitems2 != container120numitems:
						'''------------------------------
						---Last_SubService---------------
						------------------------------'''
						count3 = 0
						while count3 < 5 and systemidle1 and not xbmc.abortRequested:
							count3 += 1
							container120listitemlabel2 = xbmc.getInfoLabel('Container(120).ListItem.Label2')
							systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
							if (container120listitemlabel2 in subL or container120listitemlabel2 == dialogsubtitles2): xbmc.executebuiltin('Action(Down)')
							xbmc.sleep(100)
							'''---------------------------'''
							
					elif tip == "true" and countidle == 3:
						if container120listitemlabel2 == dialogsubtitles2: notification('$LOCALIZE[78947]',dialogsubtitles2,"",3000)
						elif container120listitemlabel2 in subL: notification('$LOCALIZE[78949]',dialogsubtitles2,"",3000)
						
						tip = "false"
						'''---------------------------'''
				
			elif controlhasfocus150 and container120numitems == 0:
				count2 += 1
				
				if countidle >= 1 and count2 == 1:
					'''------------------------------
					---LOOKING-FOR-SUBTITLE----------
					------------------------------'''
					notification('$LOCALIZE[78952]',"","",4000)
					'''---------------------------'''
				
				elif countidle > 3 and count2 == 10 and systemcurrentcontrol == controlgetlabel100:
					'''------------------------------
					---REFRESH-----------------------
					------------------------------'''
					if controlgetlabel100 == "Subtitle.co.il": xbmc.sleep(1000)
					notification('$LOCALIZE[78951]',"","",2000)
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,100,'Action(Down)','Action(Select)')
					'''---------------------------'''
					
				elif countidle > 5 and count2 >= 20 and controlgetlabel100 != "":
					'''------------------------------
					---CHANGE-SUBTITLE-SERVICE-------
					------------------------------'''
					notification('$LOCALIZE[78950]',"","",2000)
					if controlgetlabel100 in listL: listL.remove(controlgetlabel100) #listL = 
					
					systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,100,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,200,'Action(Down)','Action(Select)')
					
					count2 = 0
					'''---------------------------'''
		
		dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
		if dialogsubtitlesW:
			if not controlgroup70hasfocus0 and not sgbsubtitlespauseonsearch:
				if systemidle3 and playerpaused: xbmc.executebuiltin('Action(Play)')
				elif not systemidle3 and not playerpaused: xbmc.executebuiltin('Action(Pause)')
				'''---------------------------'''
			xbmc.sleep(1000)
			'''---------------------------'''
			count += 1
			if systemidle1: countidle += 1
			else: countidle = 0
			'''---------------------------'''
		
	if count > 20 and count < 100 and count2 > 20 and Current_Year == yearnowS and Current_M_T == "0":
		'''------------------------------
		---NEW-MOVIE---------------------
		------------------------------'''
		notification('$LOCALIZE[78944]','$LOCALIZE[78948]',"",4000)
		'''---------------------------'''
	
	systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
	systemidle7 = xbmc.getCondVisibility('System.IdleTime(7)')
	
	if systemidle1 and not systemidle7:
		'''------------------------------
		---SET-NEW-SUBTITLE--------------
		------------------------------'''
		dialogsubtitles = xbmc.getInfoLabel('Skin.String(DialogSubtitles)')
		setSkinSetting("0",'DialogSubtitles2',dialogsubtitles)
		if dialogsubtitles2 != "": setSubHisotry(admin, dialogsubtitles, dialogsubtitles2)
		if Subtitle_Service != controlgetlabel100 and controlgetlabel100 != "": setsetting_custom1('script.htpt.smartbuttons','Subtitle_Service',controlgetlabel100)
		'''---------------------------'''
		
	#if dialogsubtitlesW: xbmc.executebuiltin('Dialog.Close(subtitlesearch)')
	setSkinSetting("0",'DialogSubtitles',"")
	playerpaused = xbmc.getCondVisibility('Player.Paused')
	if playerpaused: xbmc.executebuiltin('Action(Play)')
	'''---------------------------'''
	
	if dialogsubtitlesna6 and not dialogsubtitlesna7:
		'''------------------------------
		---SHOW-TIPS---------------------
		------------------------------'''
		playerpaused = xbmc.getCondVisibility('Player.Paused')
		if not playerpaused: xbmc.executebuiltin('Action(Pause)')
		header = '[COLOR=Yellow]' + xbmc.getInfoLabel('$LOCALIZE[78946]') + '[/COLOR]'
		message2 = xbmc.getInfoLabel('$LOCALIZE[78945]')
		w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
		w.doModal()
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + space + "count/2" + space2 + str(count) + space4 + str(count2) + space + "countidle" + space2 + str(countidle) + space + "controlgetlabel100" + space2 + str(controlgetlabel100) + space + "controlhasfocus120" + space2 + str(controlhasfocus120) + space + "controlhasfocus150" + space2 + str(controlhasfocus150) + space + "container120numitems/2" + space2 + str(container120numitems) + space4 + str(container120numitems2) + newline + "listL" + space2 + str(listL) + space + "Subtitle_Search" + space2 + str(Subtitle_Search) + space + "Subtitle_Service" + space2 + str(Subtitle_Service) + newline + "systemcurrentcontrol" + space2 + str(systemcurrentcontrol) + space + space + "container120listitemlabel2" + space2 + str(container120listitemlabel2) + space + "subL" + space2 + str(subL) + space + "playerpaused" + space2 + str(playerpaused)
	'''---------------------------'''

def mode10(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	#mode10(admin, name, printpoint)
	'''---------------------------'''

def mode11(value, admin, name, printpoint):
	'''------------------------------
	---INSTALL-ADDON2----------------
	------------------------------'''
	installaddon2(admin, value, update=True) ; xbmc.sleep(1000) ; xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(1000)
	'''---------------------------'''
	
def mode12(admin, name, printpoint):
	'''------------------------------
	---UPDATE-LIVE-TV-PVR------------
	------------------------------'''
	if connected:
		notification("UPDATE-LIVE-TV-PVR","","",1000)

		path = os.path.join(addondata_path, 'plugin.video.israelive', '')
		removefiles(path)
		path = os.path.join(database_path, 'Epg8.db')
		removefiles(path)
		xbmc.sleep(1000)
		xbmc.executebuiltin('RunScript(plugin.video.israelive,,mode=32)') #Update IPTVSimple settings
		xbmc.sleep(500)
		xbmc.executebuiltin('RunScript(plugin.video.israelive,,mode=34)') #REFRESH ALL SETTINGS
		'''---------------------------'''
	else: notification_common("5")
	'''---------------------------'''

def mode13(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode13(admin, name, printpoint)
	'''---------------------------'''

def mode14(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode14(admin, name, printpoint)
	'''---------------------------'''
	
def mode15(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode15(admin, name, printpoint)
	'''---------------------------'''
	
def mode16(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode16(admin, name, printpoint)
	'''---------------------------'''

def mode17(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode17(admin, name, printpoint)
	'''---------------------------'''

def mode18(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode18(admin, name, printpoint)
	'''---------------------------'''

def mode19(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode19(admin, name, printpoint)
	'''---------------------------'''

def mode20(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode20(admin, name, printpoint)
	'''---------------------------'''
	
def mode21(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode21(admin, name, printpoint)
	'''---------------------------'''

def mode22(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode22(admin, name, printpoint)
	'''---------------------------'''

def mode23(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode23(admin, name, printpoint)
	'''---------------------------'''

def mode24(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode24(admin, name, printpoint)
	'''---------------------------'''

def mode25(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode25(admin, name, printpoint)
	'''---------------------------'''

def mode26(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode26(admin, name, printpoint)
	'''---------------------------'''

def mode27(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode27(admin, name, printpoint)
	'''---------------------------'''

def mode28(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode28(admin, name, printpoint)
	'''---------------------------'''

def mode29(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode29(admin, name, printpoint)
	'''---------------------------'''
	
def mode30(admin, name):
	'''------------------------------
	---HTPT-CHANNEL------------------
	------------------------------'''
	
	xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.youtube/channel/UCcYT8oPT83Yuw4_GUZ3mMFg/)')			
	print "123" + space + skinlog_file
	if os.path.exists(skinlog_file):
		log = open(skinlog_file, 'r')
		message = log.read()
		log.close()
		diaogtextviewer('[COLOR=Yellow]' + htptskinversion + '[/COLOR]' + str75687 + "-", message)
		'''---------------------------'''

def mode31(admin, name, printpoint):
	'''------------------------------
	---?--------------------
	------------------------------'''
	pass
	'''---------------------------'''
	
def mode32(admin, name, printpoint):
	'''------------------------------
	---?--------------------
	------------------------------'''
	pass
	'''---------------------------'''
	
def mode33(admin, name, printpoint):
	'''------------------------------
	---?--------------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode34(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode34(admin, name, printpoint)
	'''---------------------------'''

def mode35(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode35(admin, name, printpoint)
	'''---------------------------'''

def mode36(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode36(admin, name, printpoint)
	'''---------------------------'''

def mode37(admin, name, printpoint):
	'''------------------------------
	---TERMS-------------------------
	------------------------------'''
	list0 = xbmc.getInfoLabel('$LOCALIZE[70014]')
	list1 = xbmc.getInfoLabel('$LOCALIZE[70015]')
	list2 = xbmc.getInfoLabel('$LOCALIZE[70016]')
	returned, value = dialogselect('$LOCALIZE[70012]',[list0, list1, list2],0)
	returned = int(returned)
	returnedS = str(returned)
	returned2 = "list" + returnedS
	if returned == -1: pass
	else: setSkinSetting("0",'ID6',value)
	'''---------------------------'''

def mode38(admin, name, printpoint):
	'''------------------------------
	---TOGGLE-ADULT-BUTTON-----------
	------------------------------'''
	xbmc.executebuiltin('Skin.ToggleSetting(Adult)')
	if not systemplatformwindows:
		xbmc.sleep(1000)
		os.system('sh /storage/.kodi/addons/script.htpt.emu/specials/scripts/copyemu.sh')
	if not adult:
		'''------------------------------
		---ADULT-BUTTON-OFF->ON----------
		------------------------------'''
		returned = dialogyesno(localize(75791), localize(75792))
		if returned == "ok":
			'''------------------------------
			---ADULT-ALWAYS-ON---------------
			------------------------------'''
			setSkinSetting("1",'Adult2',"true")
			'''---------------------------'''
		else:
			'''------------------------------
			---ADULT-ALWAYS-OFF--------------
			------------------------------'''
			setSkinSetting("1",'Adult2',"false")
			'''---------------------------'''
		setSkinSetting("1",'Admin2',"false")
		'''---------------------------'''
		list0 = xbmc.getInfoLabel('$LOCALIZE[75003]')
		list1 = xbmc.getInfoLabel('$LOCALIZE[15016]')
		returned, value = dialogselect(localize(75793), [list0, list1],0)
		if returned == -1:
			dialogok(localize(75790), localize(75781), "", "") #Quick startup has canceled
		else:
			xbmc.executebuiltin('ActivateWindow(Home.xml)')
			xbmc.sleep(200)
			'''---------------------------'''
			if returned == 0: mode520(admin, name, printpoint)
			elif returned == 1:
				gamesbutton_(admin)
				xbmc.sleep(1000)
				xbmc.executebuiltin('Action(PageDown)')
				'''---------------------------'''
				
	else: setSkinSetting("1",'Adult2',"false")
	'''---------------------------'''
	
def mode39(admin, name, printpoint):
	'''------------------------------
	---Reset-Network-Settings--------
	------------------------------'''
	'''tweak and reload the network adapters'''
	xbmc.executebuiltin('Notification([COLOR Red] $VAR[CurrentMAC][/COLOR] $LOCALIZE[79061],$LOCALIZE[79062],5000)')
	if systemplatformwindows:
		output = terminal('ipconfig /renew', 'ipconfig /renew')
		dialogok(name, output, "", "")
	else:
		os.system('sh /storage/.kodi/addons/skin.htpt/specials/scripts/resetnetwork.sh')
		xbmc.sleep(1000)
		oewindow("Network")
		'''---------------------------'''
		
def mode40(admin, name, printpoint):
	'''------------------------------
	---Skin.ResetSettings------------
	------------------------------'''
	returned = ""
	skinsettingsW = xbmc.getCondVisibility('Window.IsVisible(SkinSettings.xml)')
	if skinsettingsW: returned = dialogyesno(localize(74554) , localize(74556))
	if returned == 'ok' and skinsettingsW:
		'''------------------------------
		---DELETE-USER-FILES-------------
		------------------------------'''
		pass
		#Clean_Library("10")
		#Clean_Library("11")
		#Clean_Library("12")
		#Clean_Library("13")
	
	if returned == 'ok' or not skinsettingsW:	
		xbmc.executebuiltin('Skin.ResetSettings')
		notification_common("2")
		xbmc.sleep(4000)
		
		'''------------------------------
		---Apply-USER-IDS----------------
		------------------------------'''
		setSkinSetting5("0",'ID',idstr,'ID1',id1str,'ID2',id2str,'ID3',id3str,'ID4',id4str)
		setSkinSetting5("0",'ID5',id5str,'ID6',id6str,'ID7',id7str,'ID8',id8str,'ID9',id9str)
		setSkinSetting5("0",'ID10',id10str,'ID11',id11str,'ID12',id12str,'ID60',id60str,'',"")
		setSkinSetting5("0",'MAC',macstr,'MAC1',mac1str,'MAC2',mac2str,'',"",'MAC5',mac5str)
		setSkinSetting5("0",'',"",'',"",'TrialDate',trialdate,'TrialDate2',trialdate2,'Country',countrystr)
		setSkinSetting5("1",'Admin3',admin3,'',"",'ID40',id40str,'',"",'',"")
		'''---------------------------'''
		setSkinSetting5("1",'Account1_Active',Account1_Active,'Account2_Active',Account2_Active,'Account3_Active',Account3_Active,'Account4_Active',Account4_Active,'Account5_Active',Account5_Active)
		setSkinSetting5("1",'',"",'',"",'',"",'',"",'Account10_Active',Account10_Active)
		setSkinSetting5("0",'Account1_Period',Account1_Period,'Account2_Period',Account2_Period,'Account3_Period',Account3_Period,'Account4_Period',Account4_Period,'Account5_Period',Account5_Period)
		setSkinSetting5("0",'Account6_Period',Account6_Period,'Account7_Period',Account7_Period,'Account8_Period',Account8_Period,'Account9_Period',Account9_Period,'Account10_Period',Account10_Period)
		'''---------------------------'''
		setSkinSetting5("0",'Account1_EndDate',Account1_EndDate,'Account2_EndDate',Account2_EndDate,'Account3_EndDate',Account3_EndDate,'Account4_EndDate',Account4_EndDate,'Account5_EndDate',Account5_EndDate)
		setSkinSetting5("0",'Account6_EndDate',Account6_EndDate,'Account7_EndDate',Account7_EndDate,'Account8_EndDate',Account8_EndDate,'Account9_EndDate',Account9_EndDate,'Account10_EndDate',Account10_EndDate)
		'''---------------------------'''
		setSkinSetting5("0",'LibraryData_RemoteDate',librarydataremotedatestr,'LibraryData_LocalDate',librarydatalocaldatestr,'',"",'',"",'',"")
		'''---------------------------'''
		
		'''------------------------------
		---Apply-PREFERED-SETTINGS-------
		------------------------------'''
		setSkinSetting5("0",'MusicLink',"Albums",'moviesestartup',"1",'tvshowsestartup',"1",'Skin_Name',skinnamestr,'IRtype',irtype) #SKIN SETTINGS
		'''---------------------------'''
		setSkinSetting5("1",'',"",'',"",'AutoPlaySD',"true",'',"",'ShowFileInfo',"true") #SKIN SETTINGS
		setSkinSetting5("1",'',"",'AutoShutdown',"true",'',"",'',"",'',"") #SKIN SETTINGS
		setSkinSetting5("1",'hidetest',"true",'',"",'',"",'3dmovs',"true",'',"") #HOMEBUTTONS
		'''---------------------------'''
		
		'''------------------------------
		---Widgets-----------------------
		------------------------------'''
		
		'''---------------------------'''
		
		'''------------------------------
		---performance-------------------
		------------------------------'''
		listL = ["C", "D"]
		if id10str in listL: setSkinSetting("1",'Performance',"true")
		'''---------------------------'''
	
	if 1 + 1 == 3:
		if skinsettingsW: returned = dialogyesno(localize(74557), localize(74556))
		if returned == 'ok' and skinsettingsW:
			'''------------------------------
			---RESET-ADDONS-SETTINGS---------
			------------------------------'''
			if skinsettingsW: dialogok('USERDATA DELETED!','[CR]' + 'THERE IS NO WAY BACK NOW...',"","")
			if not admin3:
				addonsL = []
				addonsL.append('script.htpt.homebuttons')
				addonsL.append('script.htpt.emu')
				addonsL.append('service.htpt')
				addonsL.append('plugin.video.htpt.kids')
				addonsL.append('plugin.video.htpt.music')
				addonsL.append('plugin.video.htpt.gopro')
				addonsL.append('script.htpt.smartbuttons')
				addonsL.append('plugin.video.p2p-streams')
				addonsL.append('plugin.program.advanced.launcher')
				addonsL.append('plugin.video.genesis')
				addonsL.append('plugin.video.youtube')
				'''---------------------------'''
				if admin:
					addonsL.append('script.htpt.remote')
					addonsL.append('script.htpt.fix')
					addonsL.append('service.htpt.debug')
					'''---------------------------'''
				removeaddons(addonsL,"23")
				'''---------------------------'''
			else:
				'''------------------------------
				---Apply-CURRENT-USER-SETTINGS---
				------------------------------'''
				setSkinSetting5("0",'MusicLink',musiclinkstr,'',"",'',"",'',"",'',"") #SKIN SETTINGS
				setSkinSetting5("1",'Adult',adult,'Adult2',adult2,'',"",'',"",'',"") #SKIN SETTINGS
				'''---------------------------'''
		elif skinsettingsW: notification_common("9")

def mode41(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode41(admin, name, printpoint)
	'''---------------------------'''

def mode42(admin, name, mac5str):
	'''------------------------------
	---FORMAT------------------------
	------------------------------'''
	printpoint = ""
	returned = dialogyesno('FORMAT YOUR DEVICE TOOL','CHOOSE YES TO PROCEED')
	if returned == 'ok':
		'''asking for a password'''
		returned = dialogkeyboard(mac5str,"Enter Password",5,'1','MAC5',"")
		if returned != 'skip':
			xbmc.sleep(1000)
			mac5str = xbmc.getInfoLabel('Skin.String(MAC5)')
			if mac5str != "":
				if mac5str == str70000:
					printpoint = printpoint + "7"
					notification("FORMAT WILL START IN 10 MIN!","REBOOT ASAP FOR CANCELING THE PROCESS!","",10000)
					'''---------------------------'''
				elif mac5str != str70000:
					printpoint = printpoint + "8"
					notification('$LOCALIZE[12342]',"BE SURE YOU KNOW WHAT YOU ARE DOING!!!","",10000)
					setSkinSetting("1",'ADMIN',"false")
					setSkinSetting("0",'ID9',"FTOOL")
					xbmc.executebuiltin('ReplaceWindow(Startup.xml)')
					xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=13)')
					'''---------------------------'''
					
	elif mac5str: xbmc.executebuiltin('Skin.SetString(MAC5,)')
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + "_LV" + printpoint + space + "mac5str" + space2 + str(mac5str) + space + " ( " + returned + " ) "
	'''---------------------------'''

def mode43(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode43(admin, name, printpoint)
	'''---------------------------'''

def mode44(admin, name):
	'''------------------------------
	---OVERCLOCK---------------------
	------------------------------'''
	if not systemplatformlinuxraspberrypi and not admin3: notification_common("22")
	else:
		printpoint = ""
		setSkinSetting("0",'OverClockLevel', scriptopenelecrpiconfigoverclock_preset)
		list = ['-> (Exit)','Status','OverClocking'] #,'Stability Test'
		
		returned, value = dialogselect('$LOCALIZE[74433]',list,0)

		if returned == -1:
			printpoint = printpoint + "9"
			#notification_common("9")
		elif returned == 0: printpoint = printpoint + "8"
		elif returned == 1:
			'''------------------------------
			---STATUS------------------------
			------------------------------'''
			config_file = '/flash/config.txt'
			if not os.path.exists(config_file): dialogok("config.txt is missing!", "" ,"" ,"")
			else:
				output = catfile('/flash/config.txt')
				diaogtextviewer(config_file, output)
				'''---------------------------'''
		elif returned == 2: mode46(admin, 'OVERCLOCKING')
		#elif returned == 3: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=45)')

def mode45(admin, name):
	'''------------------------------
	---STABILITY-TEST----------------
	------------------------------'''
	path = os.path.join(addonPath, 'specials', 'scripts', 'stabilitytest.sh')
	os.system('sh '+path+'')
	#xbmc

def mode46(admin,name):
	'''------------------------------
	---OVERCLOCKING------------------
	------------------------------'''
	printpoint = ""
	addon = 'script.openelec.rpi.config'
	if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		installaddonP(admin, addon)
	else: xbmc.executebuiltin('RunScript('+addon+')')
	
def mode47(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode47(admin, name, printpoint)
	'''---------------------------'''

def mode48(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode48(admin, name, printpoint)
	'''---------------------------'''
	
def mode49(admin, name, printpoint):
	'''------------------------------
	---SCRAPER-FIX-------------------
	------------------------------'''
	setsetting_custom1('service.htpt.fix','Fix_100',"true")
	setsetting_custom1('service.htpt.fix','Fix_101',"true")
	
	xbmc.executebuiltin('ActivateWindow(0)')
	xbmc.sleep(500)
	notification_common("2")
	xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=3)')	
	
	
def mode50(admin, name, printpoint):
	'''------------------------------
	---SOFT-RESTART------------------
	------------------------------'''
	CloseSession()
		
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	setsetting_custom1('service.htpt.debug','General_ScriptON',"true")
	setsetting_custom1('service.htpt.debug','ModeOn_7',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_7',datenowS + "__" + timenow2S)
	killall(admin, custom="1")
	
	#xbmc.sleep(5000)
	#xbmc.executebuiltin('XBMC.Reset()')
	'''---------------------------'''

def mode51(admin, name, printpoint):
	'''------------------------------
	---RESTART-----------------------
	------------------------------'''
	CloseSession()
	setsetting_custom1('service.htpt.debug','General_ScriptON',"true")
	setsetting_custom1('service.htpt.debug','ModeOn_8',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_8',datenowS + "__" + timenow2S)
	#xbmc.sleep(1000)
	#xbmc.executebuiltin('XBMC.Reset()')
	killall(admin, custom="r")
	'''---------------------------'''

def mode52(admin, name, printpoint):
	'''------------------------------
	---SUSPEND-----------------------
	------------------------------'''
	setsetting_custom1('service.htpt.debug','General_ScriptON',"true")
	setsetting_custom1('service.htpt.debug','ModeOn_4',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_4',datenowS + "__" + timenow2S)
	xbmc.sleep(1000)
	xbmc.executebuiltin('XBMC.Suspend()')
	'''---------------------------'''

def mode53(admin, name, printpoint):
	'''------------------------------
	---POWEROFF----------------------
	------------------------------'''
	CloseSession()
	setsetting_custom1('service.htpt.debug','ModeOn_10',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_10',datenowS + "__" + timenow2S)
	#notification('$LOCALIZE[13016]',addonString_servicehtpt(10),"",4000)
	notification(startupmessage2,id1str,"",5000)
	killall(admin, custom="s") ; xbmc.sleep(1000)
	if not systemplatformwindows: xbmc.executebuiltin('XBMC.Powerdown()')
	'''---------------------------'''

def mode54(admin, name, printpoint):
	'''------------------------------
	---QUIT--------------------------
	------------------------------'''
	CloseSession()
	#from shared_modules4 import *
	#setsetting_custom1('service.htpt.debug','ModeTime_10',datenowS + "__" + timenow2S)
	#xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=10)')
	#notification('$LOCALIZE[13016]',addonString_servicehtpt(10),"",4000)
	#guiset(admin, guiread)
	xbmc.sleep(500)
	killall(admin, custom="")
	xbmc.sleep(1000)
	xbmc.executebuiltin('RestartApp')
	#notification(startupmessage2,id1str,"",5000)
	'''---------------------------'''


def mode55(admin, admin3, name, printpoint):
	'''------------------------------
	---LibraryData-------------------
	------------------------------'''
	#from variables import * #GAL TEST THIS!
	library_file = os.path.join(copydir, 'library.zip')
	if os.path.exists(library_file):
		notification("Looking for remote files","Please Wait","",10000)
		ExtractAll(library_file, copydir)
		notification("Comparing remote to local files","Please Wait.","",4000)
		admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
		if not admin3: removefiles(library_file)
		xbmc.sleep(500)
	elif admin: print printfirst + copydir + "library.zip"
	
	if not admin3 or 1 + 1 == 2:
		Afolders_count, Afolders_count2, Afiles_count = bash_count(copymoviesdir+'*')
		Bfolders_count, Bfolders_count2, Bfiles_count = bash_count(copytvshowsdir+'*')
		Cfolders_count, Cfolders_count2, Cfiles_count = bash_count(movies_path+'*')
		Dfolders_count, Dfolders_count2, Dfiles_count = bash_count(tvshows_path+'*')
		'''---------------------------'''
		setsetting_custom1(addonID,'LibraryData_RemoteMoviesFiles',Afolders_count2)
		setsetting_custom1(addonID,'LibraryData_RemoteTvshowsFiles',Bfolders_count2)
		setsetting_custom1(addonID,'LibraryData_LocalMoviesFiles',Cfolders_count2)
		setsetting_custom1(addonID,'LibraryData_LocalTvshowsFiles',Dfolders_count2)
		'''---------------------------'''
		LibraryData_RemoteMoviesFiles2 = getsetting('LibraryData_RemoteMoviesFiles')
		LibraryData_RemoteTvshowsFiles2 = getsetting('LibraryData_RemoteTvshowsFiles')
		if LibraryData_RemoteMoviesFiles != LibraryData_RemoteMoviesFiles2 or LibraryData_RemoteTvshowsFiles != LibraryData_RemoteTvshowsFiles2 or librarydataremotedatestr == "":
			notification(str24068.encode('utf-8') + space5 + datenowS,str79577.encode('utf-8'),"",4000) #Update available, Update Movies and Tvshows library
			setSkinSetting("0", 'LibraryData_RemoteDate', datenowS)
			'''---------------------------'''
		if admin: print printfirst + "LibraryData" + space + "Afolders_count2" + space2 + Afolders_count2 + space + "Bfolders_count2" + space2 + Bfolders_count2 + newline + \
		"LibraryData_RemoteMoviesFiles/2" + space2 + LibraryData_RemoteMoviesFiles + space4 + LibraryData_RemoteMoviesFiles2 + space + "LibraryData_RemoteTvshowsFiles/2" + space2 + LibraryData_RemoteTvshowsFiles + space4 + LibraryData_RemoteTvshowsFiles2

	xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=56)')
	
def mode56(admin, name, LibraryData_RemoteMoviesFiles, LibraryData_RemoteTvshowsFiles, LibraryData_LocalMoviesFiles, LibraryData_LocalTvshowsFiles, librarydataremotedatestr):
	'''------------------------------
	---LibrarySync-------------------
	------------------------------'''
	#from variables import * #GAL TEST THIS!
	printpoint = "" ; TypeError = ""
	
	try: LibraryData_RemoteMoviesFiles = int(LibraryData_RemoteMoviesFiles)
	except Exception, TypeError: LibraryData_RemoteMoviesFiles = 0
	try: LibraryData_RemoteTvshowsFiles = int(LibraryData_RemoteTvshowsFiles)
	except Exception, TypeError: LibraryData_RemoteTvshowsFiles = 0
	try: LibraryData_LocalMoviesFiles = int(LibraryData_LocalMoviesFiles)
	except Exception, TypeError: LibraryData_LocalMoviesFiles = 0
	try: LibraryData_LocalTvshowsFiles = int(LibraryData_LocalTvshowsFiles)
	except Exception, TypeError: LibraryData_LocalTvshowsFiles = 0
	Remotevslocal1 = LibraryData_RemoteMoviesFiles - LibraryData_LocalMoviesFiles
	Remotevslocal2 = LibraryData_RemoteTvshowsFiles - LibraryData_LocalTvshowsFiles
	'''---------------------------'''
	
	'''------------------------------
	---CHECK-FOR-LibrarySync_ON------
	------------------------------'''
	if librarydataremotedatestr != "":
		printpoint = printpoint + "0"
		if (Remotevslocal1 + Remotevslocal2) > 0 or librarydataremotedatestr != librarydatalocaldatestr or librarydatalocaldatestr == "":
			printpoint = printpoint + "1"
			if librarydatalocaldatestr == "" and librarydataremotedatestr == librarydatalocaldatestr: setSkinSetting("0", 'LibraryData_LocalDate', librarydatalocaldatestr + "*")
		else: notification("Your library is up to date!", "", "", 2000)
	elif librarydataremotedatestr != "" and librarydataremotedatestr == librarydatalocaldatestr and (Remotevslocal1 + Remotevslocal2) <= 0:
		printpoint = printpoint + "2"
		if skinsettingsW: notification('$LOCALIZE[79578]', '$LOCALIZE[79579]',"",4000) #The library already synced		
	else:
		printpoint = printpoint + "9"
		#notification_common("17")
		'''---------------------------'''
	#if librarydataremotedatestr == librarydataremotedate2str: setSkinSetting("0", 'LibraryData_LocalDate', librarydataremotedate2str + "?")
	if "1" in printpoint:
		'''------------------------------
		---CONTINUE----------------------
		------------------------------'''
		returned, value = getRandom("0",percent=40)
		if skinsettingsW or admin or "special://userdata/library/movies/" or "special://userdata/library/tvshows/" or returned == "ok":
			'''------------------------------
			---CONTINUE----------------------
			------------------------------'''
			printpoint = printpoint + "3"
			if librarydatalocaldatestr != "": option = str24056.encode('utf-8') % (librarydatalocaldatestr)
			else: option = '$LOCALIZE[79580]'
			
			dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
			while dialogyesnoW and not xbmc.abortRequested:
				xbmc.sleep(2500)
				dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
				xbmc.sleep(2500)
			if librarydataautoupdate or scripthtptinstall_Skin_FirstBoot == "true" or scripthtptinstall_Skin_Installed == "true" or not libraryhascontentmovies or not libraryhascontenttvshows:
				returned = dialogyesno('[COLOR=Yellow]' + str79577.encode('utf-8') + '[/COLOR]',str24068.encode('utf-8') + ', ' + localize(12354) + '[CR]' + option)
				if "ok" in returned:
					'''------------------------------
					---CONTINUE----------------------
					------------------------------'''
					printpoint = printpoint + "7"
					copyfiles(os.path.join(copylibrarydir, '*'), library_path)
					xbmc.sleep(1000)
					setSkinSetting("0", 'LibraryData_LocalDate', librarydataremotedatestr)
					containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
					libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
					if not libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
					if not admin:
						if Remotevslocal1 < 0: Remotevslocal1 = 0
						if Remotevslocal2 < 0: Remotevslocal2 = 0
						'''---------------------------'''
					if str(Remotevslocal1) != "0" or str(Remotevslocal2) != "0" and scripthtptinstall_Skin_FirstBoot != "true": dialogok(localize(79577) + '[CR]' + localize(79072), str79584 % (str(Remotevslocal1),str(Remotevslocal2)), "", "", line1c="Yellow")
					else: notification(localize(79577), localize(79072), "", 4000)
					'''---------------------------'''
				else: notification_common("9")
			elif not librarydataautoupdate: notification(localize(79577), localize(16039), "", 2000)
			else: notification(localize(79577) + space + localize(13610), localize(78930), "", 2000) #Update Movies and Tvshows library
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if TypeError != "": print printfirst + "LibrarySync" + space + "TypeError" + space2 + str(TypeError)
	if admin: print printfirst + "LibrarySync_LV" + printpoint + space + "Remotevslocal1" + space2 + str(Remotevslocal1) + space + "Remotevslocal2" + space2 + str(Remotevslocal2)
	'''---------------------------'''

def mode57(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode57(admin, name, printpoint)
	'''---------------------------'''

def mode58(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode58(admin, name, printpoint)
	'''---------------------------'''
	
def mode59(admin, name, printpoint):
	'''------------------------------
	---Choose-Country----------------
	------------------------------'''
	
	list = ['-> (Exit)', 'Israel', 'Foreign (English)']
	if scripthtptinstall_Skin_Installed == "true" or countrystr == "": list.remove(list[0])
	
	returned, value = dialogselect('$LOCALIZE[74433]',list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
		
	if "7" in printpoint or countrystr == "" or scripthtptinstall_Skin_Installed == "true":
		if value != "": setSkinSetting('0', 'Country', value)
		else: value = 'Israel'
		if value == "Israel": xbmc.executebuiltin('SetGUILanguage(Hebrew)')
		elif "Foreign" in value: xbmc.executebuiltin('SetGUILanguage(English)')
		xbmc.sleep(1000)
		setAutoSettings("3")
		dialogok("Your current country is: "+value+"", "The system will change all contents and settings in order to fit your choosen country!", "Please note this feature is WIP and may not work at all atm..", "")	
	
	print printfirst + name + "_LV" + printpoint + space + "list" + space2 + str(list) + space + "returned" + space2 + str(returned)

def mode60(admin, name, printpoint):
	'''------------------------------
	---?--------------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode61(admin, name, printpoint):
	'''------------------------------
	---?--------------------
	------------------------------'''
	pass
	'''---------------------------'''
	
def mode62(admin, name, printpoint):
	'''------------------------------
	---?--------------------
	------------------------------'''
	pass
	'''---------------------------'''
	

def mode63(admin, name):
	'''------------------------------
	---Texture-Cache-Removal---------
	------------------------------'''
	returned = dialogyesno("Are you sure?", "Doing so will delete your database and thumbnails folder!")
	if returned == "ok":
		dp = xbmcgui.DialogProgress()
		dp.create("HTPT Texture-Cache-Removal", "Removing Datebase", " ")
		removefiles(database_path)
		dp.update(20,"Removing Thumbnails"," ")
		removefiles(thumbnails_path)
		dp.update(90,str79072.encode('utf-8')," ")
		setsetting_custom1('service.htpt.fix','Fix_100',"true")
		setsetting_custom1('service.htpt.fix','Fix_101',"true")
		xbmc.sleep(1000)
		dp.update(100,str79072.encode('utf-8')," ")
		dp.close
		dialogok("Reboot Required!", "Click OK", "", "")
		xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=50)')
		
	else: notification_common("9")

def mode64(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode64(admin, name, printpoint)
	'''---------------------------'''

def mode65(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode65(admin, name, printpoint)
	'''---------------------------'''

def mode66(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode66(admin, name, printpoint)
	'''---------------------------'''

def mode67(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode67(admin, name, printpoint)
	'''---------------------------'''

def mode68(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode68(admin, name, printpoint)
	'''---------------------------'''

def mode69(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode69(admin, name, printpoint)
	'''---------------------------'''

def mode70(admin, name):
	'''------------------------------
	---ExtendedInfo------------------
	------------------------------'''
	addon = 'script.extendedinfo' ; input = "" ; input2 = 'name' ; printpoint = "" ; container50listitemlabel2 = "" ; dialogselectsources7 = xbmc.getInfoLabel('Skin.String(DialogSelectSources7)') ; dialogselectsources7_ = ""
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		if dialogselectsources7 != "" and dialogselectW:
			printpoint = printpoint + "1"
			xbmc.executebuiltin('dialog.close(selectdialog)')
			xbmc.sleep(500)
			if dialogselectsources7 == listitemdirector:
				printpoint = printpoint + "2"
				name = name + space2 + "Director"
				input = dialogselectsources7
				if input != "":
					printpoint = printpoint + "3"
					input2 = 'director'
					xbmc.executebuiltin('RunScript('+addon+',info=directormovies,'+input2+'='+input+')')
				else: printpoint = printpoint + "4"
			else:
				printpoint = printpoint + "5"
				name = name + space2 + "Actors"
				if xbmc.getInfoLabel('$LOCALIZE[20347]') in dialogselectsources7:
					dialogselectsources7_ = find_string(dialogselectsources7, dialogselectsources7[:1], xbmc.getInfoLabel('$LOCALIZE[20347]'))
					str20347_len = len(xbmc.getInfoLabel('$LOCALIZE[20347]'))
					dialogselectsources7_ = dialogselectsources7_[:-str20347_len]
					input = dialogselectsources7_
				else: input = dialogselectsources7
				if input != "":
					xbmc.executebuiltin('RunScript('+addon+',info=extendedactorinfo,'+input2+'='+input+')')
		else:
			name = name + space2 + "Movie Info"
			printpoint = printpoint + "1"
			if listitemtvshowtitle != "":
				printpoint = printpoint + "2"
				input = listitemtvshowtitle
				if 1 + 1 == 3:
					try: listitemdbidN = int(listitemdbid)
					except: listitemdbidN = ""
					if listitemdbidN != "":
						printpoint = printpoint + "3"
						input = listitemdbid
						input2 = 'dbid'
					else: input = listitemtvshowtitle
			elif listitemtitle != "": input = listitemtitle
			elif listitemlabel != "": input = listitemlabel
			'''---------------------------'''
			
			if input != "":
				#RunScript(script.extendedinfo,info=extendedinfo,name=MOVIENAME)
				#xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedinfo,name=MOVIENAME')
				xbmc.executebuiltin('RunScript('+addon+',info=extendedinfo,'+input2+'='+input+')')
				count = 0 ; dialogvideonfoEW = xbmc.getCondVisibility('Window.IsVisible(script-ExtendedInfo Script-DialogVideoInfo.xml)')
				while count < 10 and not dialogvideonfoEW and not xbmc.abortRequested:
					count += 1
					xbmc.sleep(500)
					dialogvideonfoEW = xbmc.getCondVisibility('Window.IsVisible(script-ExtendedInfo Script-DialogVideoInfo.xml)')
				if count < 10: printpoint = printpoint + "7"
				else: printpoint = printpoint + "9"
			else:
				printpoint = printpoint + "8"
				notification_common("17")
				'''---------------------------'''
	else:
		printpoint = printpoint + "9"
		installaddon(admin, addon, "")
	if admin: print printfirst + name + "_LV" + printpoint + space + "input" + space2 + input + space + space + "input2" + space2 + input2 + space + newline + "INFO" + space2 + "listitemlabel" + space2 + listitemlabel + newline + "listitemtvshowtitle" + space2 + listitemtvshowtitle + newline + "listitemtitle" + space2 + listitemtitle + newline + "listitemimdbnumber" + space2 + listitemimdbnumber + newline + "listitemdbid" + space2 + listitemdbid + newline + "containerfolderpath" + space2 + containerfolderpath + newline + "dialogselectsources7" + space2 + dialogselectsources7 + space + "dialogselectsources7_" + space2 + str(dialogselectsources7_) + newline + "listitemdirector" + space2 + listitemdirector
	'''---------------------------'''

def mode71(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode71(admin, name, printpoint)
	'''---------------------------'''

def mode72(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode72(admin, name, printpoint)
	'''---------------------------'''

def mode73(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode73(admin, name, printpoint)
	'''---------------------------'''

def mode74(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode74(admin, name, printpoint)
	'''---------------------------'''

def mode75(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode75(admin, name, printpoint)
	'''---------------------------'''

def mode76(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode76(admin, name, printpoint)
	'''---------------------------'''

def mode77(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode77(admin, name, printpoint)
	'''---------------------------'''

def mode78(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode78(admin, name, printpoint)
	'''---------------------------'''

def mode79(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode79(admin, name, printpoint)
	'''---------------------------'''
	
def mode80(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode80(admin, name, printpoint)
	'''---------------------------'''

def mode81(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode81(admin, name, printpoint)
	'''---------------------------'''

def mode82(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode82(admin, name, printpoint)
	'''---------------------------'''

def mode83(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode83(admin, name, printpoint)
	'''---------------------------'''

def mode84(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode84(admin, name, printpoint)
	'''---------------------------'''

def mode85(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode85(admin, name, printpoint)
	'''---------------------------'''

def mode86(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode86(admin, name, printpoint)
	'''---------------------------'''

def mode87(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode87(admin, name, printpoint)
	'''---------------------------'''

def mode88(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode88(admin, name, printpoint)
	'''---------------------------'''

def mode89(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode89(admin, name, printpoint)
	'''---------------------------'''
	
def mode90(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode90(admin, name, printpoint)
	'''---------------------------'''

def mode91(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode91(admin, name, printpoint)
	'''---------------------------'''

def mode92(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode92(admin, name, printpoint)
	'''---------------------------'''

def mode93(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode93(admin, name, printpoint)
	'''---------------------------'''
	
def mode94(admin):
	if systemhasaddon_genesis:
		'''------------------------------
		---TRAKT-TV-BUTTON---------------
		------------------------------'''
		account_button('TRAKT TV','plugin.video.genesis', 'trakt_user', 'trakt_password', trakt_user, trakt_password, 'Account10_Active', '', '', Account10_Active, "N/A", "N/A", "")
		'''---------------------------'''

def mode95(admin):
	if systemhasaddon_sdarottv:
		'''------------------------------
		---SDAROT-TV-BUTTON--------------
		------------------------------'''
		account_button('SDAROT TV','plugin.video.sdarot.tv', 'username', 'user_password', sdarottv_user, sdarottv_password, 'Account2_Active', 'Account2_Period', 'Account2_EndDate', Account2_Active, Account2_Period, Account2_EndDate, "")
		'''---------------------------'''

def mode96(admin):
	if systemhasaddon_genesis:
		'''------------------------------
		---NOOBROOM-BUTTON---------------
		------------------------------'''
		notification_common("10")
		#account_button('NOOBROOM','plugin.video.genesis', 'noobroom_mail', 'noobroom_password', noobroom_mail, noobroom_password, 'Account5_Active', 'Account5_Period', 'Account5_EndDate', Account5_Active, Account5_Period, Account5_EndDate, "")
		'''---------------------------'''
		
def mode97(admin):
	if systemhasaddon_genesis:
		'''------------------------------
		---PREMIUMIZE-BUTTON-------------
		------------------------------'''
		notification_common("10")
		#account_button('PREMIUMIZE','plugin.video.genesis', 'premiumize_user', 'premiumize_password', premiumize_user, premiumize_password, 'Account4_Active', 'Account4_Period', 'Account4_EndDate', Account4_Active, Account4_Period, Account4_EndDate, "")
		'''---------------------------'''

def mode98(admin):
	if systemhasaddon_genesis:
		'''------------------------------
		---MOVREEL-BUTTON----------------
		------------------------------'''
		notification_common("10")
		#account_button('MOVREEL','plugin.video.genesis', 'movreel_user', 'movreel_password', movreel_user, movreel_password, 'Account3_Active', 'Account3_Period', 'Account3_EndDate', Account3_Active, Account3_Period, Account3_EndDate, "")
		'''---------------------------'''

def mode99(admin):
	if systemhasaddon_genesis:
		'''------------------------------
		---REALDEBRID-BUTTON-------------
		------------------------------'''
		account_button('REALDEBRID','plugin.video.genesis', 'realdedrid_user', 'realdedrid_password', realdedrid_user, realdedrid_password, 'Account1_Active', 'Account1_Period', 'Account1_EndDate', Account1_Active, Account1_Period, Account1_EndDate, "")
		'''---------------------------'''

def mode100(admin, name):
	'''------------------------------
	---STARTUP-TRIGGER---------------
	------------------------------'''
	printpoint = "" ; dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
	while dialogtextviewerW and not xbmc.abortRequested:
		xbmc.sleep(1000)
		dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		'''---------------------------'''

	setAutoSettings("0")
	xbmc.sleep(500)
	externalusb("", 100)
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + name + "_LV" + printpoint
	'''---------------------------'''

def mode101(admin,name):
	'''------------------------------
	---TOTAL-MOUSE-------------------
	------------------------------'''
	path = os.path.join(htptservice_path, 'specials', 'tools', 'EAT_gil900.exe')
	if os.path.exists(path):
		if skinsettingsW: xbmc.executebuiltin('Skin.ToggleSetting(TotalMouse)')
		notification("TotalMouse by gil900", "", "", 2000) ; xbmc.sleep(1000)
		totalmouse = xbmc.getInfoLabel('Skin.HasSetting(TotalMouse)')
		terminal('TASKKILL /im EAT_gil900.exe /f',"EAT-end") ; xbmc.sleep(200) ; terminal('TASKKILL /im EAT_gil900.exe /f',"EAT-end") ; xbmc.sleep(200)
		if totalmouse: terminal('"'+path+'"', 'EAT-start')
		else: pass
		'''---------------------------'''
	elif custom1170W: notification("File is missing!", "", "", 2000)

def mode102(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode102(admin, name, printpoint)
	'''---------------------------'''
	
def mode103(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode103(admin, name, printpoint)
	'''---------------------------'''

def mode104(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode104(admin, name, printpoint)
	'''---------------------------'''

def mode105(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode105(admin, name, printpoint)
	'''---------------------------'''

def mode106(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode106(admin, name, printpoint)
	'''---------------------------'''

def mode107(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode107(admin, name, printpoint)
	'''---------------------------'''

def mode108(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode108(admin, name, printpoint)
	'''---------------------------'''

def mode109(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode109(admin, name, printpoint)
	'''---------------------------'''

def mode110(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode140(admin, name, printpoint)
	'''---------------------------'''
	
def mode111(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode111(admin, name, printpoint)
	'''---------------------------'''

def mode112(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode112(admin, name, printpoint)
	'''---------------------------'''

def mode113(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode113(admin, name, printpoint)
	'''---------------------------'''

def mode114(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode114(admin, name, printpoint)
	'''---------------------------'''

def mode115(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode115(admin, name, printpoint)
	'''---------------------------'''

def mode116(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode116(admin, name, printpoint)
	'''---------------------------'''

def mode117(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode117(admin, name, printpoint)
	'''---------------------------'''

def mode118(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode118(admin, name, printpoint)
	'''---------------------------'''

def mode119(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode119(admin, name, printpoint)
	'''---------------------------'''

def mode120(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode120(admin, name, printpoint)
	'''---------------------------'''
	
def mode121(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode121(admin, name, printpoint)
	'''---------------------------'''

def mode122(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode122(admin, name, printpoint)
	'''---------------------------'''

def mode123(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode123(admin, name, printpoint)
	'''---------------------------'''

def mode124(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode124(admin, name, printpoint)
	'''---------------------------'''

def mode125(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode125(admin, name, printpoint)
	'''---------------------------'''

def mode126(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode126(admin, name, printpoint)
	'''---------------------------'''

def mode127(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode127(admin, name, printpoint)
	'''---------------------------'''

def mode128(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode128(admin, name, printpoint)
	'''---------------------------'''

def mode129(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode129(admin, name, printpoint)
	'''---------------------------'''

def mode130(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode130(admin, name, printpoint)
	'''---------------------------'''
	
def mode131(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode131(admin, name, printpoint)
	'''---------------------------'''

def mode132(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode132(admin, name, printpoint)
	'''---------------------------'''

def mode133(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode133(admin, name, printpoint)
	'''---------------------------'''

def mode134(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode134(admin, name, printpoint)
	'''---------------------------'''

def mode135(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode135(admin, name, printpoint)
	'''---------------------------'''

def mode136(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode136(admin, name, printpoint)
	'''---------------------------'''

def mode137(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode137(admin, name, printpoint)
	'''---------------------------'''

def mode138(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode138(admin, name, printpoint)
	'''---------------------------'''

def mode139(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode139(admin, name, printpoint)
	'''---------------------------'''

def mode140(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode140(admin, name, printpoint)
	'''---------------------------'''
	
def mode141(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode141(admin, name, printpoint)
	'''---------------------------'''

def mode142(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode142(admin, name, printpoint)
	'''---------------------------'''

def mode143(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode143(admin, name, printpoint)
	'''---------------------------'''

def mode144(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode144(admin, name, printpoint)
	'''---------------------------'''

def mode145(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode145(admin, name, printpoint)
	'''---------------------------'''

def mode146(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode146(admin, name, printpoint)
	'''---------------------------'''

def mode147(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode147(admin, name, printpoint)
	'''---------------------------'''

def mode148(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode148(admin, name, printpoint)
	'''---------------------------'''

def mode149(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode149(admin, name, printpoint)
	'''---------------------------'''

def mode150(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode150(admin, name, printpoint)
	'''---------------------------'''

def mode151(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode151(admin, name, printpoint)
	'''---------------------------'''

def mode152(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode152(admin, name, printpoint)
	'''---------------------------'''

def mode153(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode153(admin, name, printpoint)
	'''---------------------------'''

def mode154(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode154(admin, name, printpoint)
	'''---------------------------'''

def mode155(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode155(admin, name, printpoint)
	'''---------------------------'''

def mode156(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode156(admin, name, printpoint)
	'''---------------------------'''

def mode157(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode157(admin, name, printpoint)
	'''---------------------------'''

def mode158(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode158(admin, name, printpoint)
	'''---------------------------'''

def mode159(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode159(admin, name, printpoint)
	'''---------------------------'''

def mode160(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode160(admin, name, printpoint)
	'''---------------------------'''

def mode161(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode161(admin, name, printpoint)
	'''---------------------------'''

def mode162(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode162(admin, name, printpoint)
	'''---------------------------'''

def mode163(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode163(admin, name, printpoint)
	'''---------------------------'''

def mode164(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode164(admin, name, printpoint)
	'''---------------------------'''

def mode165(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode165(admin, name, printpoint)
	'''---------------------------'''

def mode166(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode166(admin, name, printpoint)
	'''---------------------------'''

def mode167(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode167(admin, name, printpoint)
	'''---------------------------'''

def mode168(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode168(admin, name, printpoint)
	'''---------------------------'''

def mode169(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode169(admin, name, printpoint)
	'''---------------------------'''

def mode170(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode170(admin, name, printpoint)
	'''---------------------------'''

def mode171(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode171(admin, name, printpoint)
	'''---------------------------'''

def mode172(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode172(admin, name, printpoint)
	'''---------------------------'''

def mode173(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode173(admin, name, printpoint)
	'''---------------------------'''

def mode174(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode174(admin, name, printpoint)
	'''---------------------------'''

def mode175(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode175(admin, name, printpoint)
	'''---------------------------'''

def mode176(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode176(admin, name, printpoint)
	'''---------------------------'''

def mode177(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode177(admin, name, printpoint)
	'''---------------------------'''

def mode178(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode178(admin, name, printpoint)
	'''---------------------------'''

def mode179(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode179(admin, name, printpoint)
	'''---------------------------'''
	
def mode180(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode180(admin, name, printpoint)
	'''---------------------------'''

def mode181(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode181(admin, name, printpoint)
	'''---------------------------'''

def mode182(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode182(admin, name, printpoint)
	'''---------------------------'''

def mode183(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode183(admin, name, printpoint)
	'''---------------------------'''

def mode184(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode184(admin, name, printpoint)
	'''---------------------------'''

def mode185(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode185(admin, name, printpoint)
	'''---------------------------'''

def mode186(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode186(admin, name, printpoint)
	'''---------------------------'''

def mode187(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode187(admin, name, printpoint)
	'''---------------------------'''

def mode188(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode188(admin, name, printpoint)
	'''---------------------------'''

def mode189(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode189(admin, name, printpoint)
	'''---------------------------'''
	
def mode190(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode190(admin, name, printpoint)
	'''---------------------------'''

def mode191(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode191(admin, name, printpoint)
	'''---------------------------'''

def mode192(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode192(admin, name, printpoint)
	'''---------------------------'''

def mode193(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode193(admin, name, printpoint)
	'''---------------------------'''

def mode194(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode194(admin, name, printpoint)
	'''---------------------------'''

def mode195(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode195(admin, name, printpoint)
	'''---------------------------'''

def mode196(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode196(admin, name, printpoint)
	'''---------------------------'''

def mode197(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode197(admin, name, printpoint)
	'''---------------------------'''

def mode198(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode198(admin, name, printpoint)
	'''---------------------------'''

def mode199(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode199(admin, name, printpoint)
	'''---------------------------'''
	
def mode200(admin, name, printpoint):
	'''------------------------------
	---DIALOG-SELECT-(10-100)--------
	------------------------------'''
	list = ['-> (Exit)', 'default', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
	value = ""
	
	container50hasfocus210 = xbmc.getCondVisibility('Container(50).HasFocus(210)') #Selected Icon
	container50hasfocus250 = xbmc.getCondVisibility('Container(50).HasFocus(250)') #Main background
	container50hasfocus254 = xbmc.getCondVisibility('Container(50).HasFocus(254)') #TopInformationOverlay
	container50hasfocus256 = xbmc.getCondVisibility('Container(50).HasFocus(256)') #TopVideoInformationOverlay
	container50hasfocus265 = xbmc.getCondVisibility('Container(50).HasFocus(265)') #TopMainBackgroundOverlay
	container50hasfocus270 = xbmc.getCondVisibility('Container(50).HasFocus(270)') #LeftMenuOverlay
	container50hasfocus273 = xbmc.getCondVisibility('Container(50).HasFocus(273)') #BottomMenuOverlay
	container50hasfocus276 = xbmc.getCondVisibility('Container(50).HasFocus(276)') #CenterMenuOverlay
	container50hasfocus260 = xbmc.getCondVisibility('Container(50).HasFocus(260)') #MenuButtonsOverlay
	
	container50hasfocus16 = xbmc.getCondVisibility('Container(50).HasFocus(16)') #StartUpVolume
	
	if not container50hasfocus210 and not container50hasfocus250 and not container50hasfocus254 and not container50hasfocus256 and not container50hasfocus265 and not container50hasfocus270 and not container50hasfocus273 and not container50hasfocus276 and not container50hasfocus16 and not container50hasfocus260: returned = 'skip'
	else: returned, value = dialogselect('$LOCALIZE[74433]',list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		if container50hasfocus210:
			if value == 'default': setSkinSetting('0', 'IconOverlayButton', "")
			elif value != "": setSkinSetting('0', 'IconOverlayButton', value)
			else: value = '40'
		elif container50hasfocus250:
			if value == 'default': setSkinSetting('0', 'MainBackgroundOverlay', "")
			elif value != "": setSkinSetting('0', 'MainBackgroundOverlay', value)
			else: value = '40'
		elif container50hasfocus254:
			if value == 'default': setSkinSetting('0', 'TopInformationOverlay', "")
			elif value != "": setSkinSetting('0', 'TopInformationOverlay', value)
			else: value = '70'
		elif container50hasfocus256:
			if value == 'default': setSkinSetting('0', 'TopVideoInformationOverlay', "")
			elif value != "": setSkinSetting('0', 'TopVideoInformationOverlay', value)
			else: value = '70'
		elif container50hasfocus265:
			if value == 'default': setSkinSetting('0', 'TopMainBackgroundOverlay', "")
			elif value != "": setSkinSetting('0', 'TopMainBackgroundOverlay', value)
			else: value = '70'
		elif container50hasfocus270:
			if value == 'default': setSkinSetting('0', 'LeftMenuOverlay', "")
			elif value != "": setSkinSetting('0', 'LeftMenuOverlay', value)
			else: value = '70'
		elif container50hasfocus273:
			if value == 'default': setSkinSetting('0', 'BottomMenuOverlay', "")
			elif value != "": setSkinSetting('0', 'BottomMenuOverlay', value)
			else: value = '70'
		elif container50hasfocus276:
			if value == 'default': setSkinSetting('0', 'CenterMenuOverlay', "")
			elif value != "": setSkinSetting('0', 'CenterMenuOverlay', value)
			else: value = '70'
		
		elif container50hasfocus260:
			if value == 'default': setSkinSetting('0', 'MenuButtonsOverlay', "")
			elif value != "": setSkinSetting('0', 'MenuButtonsOverlay', value)
			else: value = '70'		
			
		elif container50hasfocus16:
			if value == 'default': setSkinSetting('0', 'StartUpVolume', "")
			elif value != "": setSkinSetting('0', 'StartUpVolume', value)
			else: value = '70'
			printpoint = printpoint + "1"
		
		if not "1" in printpoint:
			notification(".","","",1000)
			xbmc.sleep(200)
			xbmc.executebuiltin('Action(Back)')
			xbmc.sleep(800)
			notification("..","","",1000)
			xbmc.sleep(200)
			xbmc.executebuiltin('ReloadSkin()')
	
	print printfirst + name + "_LV" + printpoint + space + "list" + space2 + str(list) + space + "returned" + space2 + str(returned) + space + "value" + space2 + str(value)
	'''---------------------------'''

def mode201(value, admin, name, printpoint):
	'''------------------------------
	---RESET-TO-DEFAULT--------------
	------------------------------'''
	returned = ""
	container50hasfocus390 = xbmc.getCondVisibility('Container(50).HasFocus(390)') #BUTTONS
	
	if container50hasfocus390:
		list = ['-> (Exit)', localize(10035) + space + "(" + localize(593) + ")", localize(590) + space + "(" + localize(593) + ")", \
		localize(74840) + space + "(" + localize(78219) + ")", localize(74840) + space + localize(590) + space + "(" + localize(78219) + ")", \
		localize(74840) + space + "(" + localize(593) + ")", localize(74840) + space + localize(590) + space + "(" + localize(593) + ")", \
		localize(10035) + space + localize(78215) + space + "(" + localize(593) + ")", localize(10035) + space + localize(78215) + space + localize(590) + space + "(" + localize(593) + ")"]
	else: list = []
	
	if list != []:
		returned, value = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
		
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		if (returned == 1 or value == "1"): printpoint = printpoint + "ACEG" #RESET-ALL
		elif returned == 2: printpoint = printpoint + "BDFH" #RANDOM-ALL
		elif returned == 3: printpoint = printpoint + "C" #RESET-BUTTONS-COLORS
		elif returned == 4: printpoint = printpoint + "D" #RANDOM-BUTTONS-COLORS
		elif returned == 5: printpoint = printpoint + "CE" #RESET-ALL-COLORS
		elif returned == 6: printpoint = printpoint + "DF" #RANDOM-ALL-COLORS
		elif returned == 7: printpoint = printpoint + "G" #RESET-ALL-TRANSPERANCY
		elif returned == 8: printpoint = printpoint + "H" #RANDOM-ALL-TRANSPERANCY
	
	if "A" in printpoint:	
		setSkinSetting5('0', 'IconOverlayButton', '', 'MainBackgroundTexture', "", 'TopBackgroundTexture', "", '', "", '', "")
		setSkinSetting5('1', 'SelectionMarker', 'false', 'SelectionMarker2', 'false', 'ShadowButton', 'false', 'OverlayButton', 'false', 'background', "false")
		'''---------------------------'''
	
	if "B" in printpoint:
		returned1, value1 = getRandom("0", min=0, max=100, percent=50)
		returned2, value2 = getRandom("0", min=0, max=100, percent=50)
		returned3, value3 = getRandom("0", min=0, max=100, percent=50)
		returned4, value4 = getRandom("0", min=0, max=100, percent=50)
		returned5, value5 = getRandom("0", min=0, max=100, percent=50)
					
		if returned1 == 'ok': value1 = "true"
		else: value1 = "false"
		if returned2 == 'ok': value2 = "true"
		else: value2 = "false"
		if returned3 == 'ok': value3 = "true"
		else: value3 = "false"
		if returned4 == 'ok': value4 = "true"
		else: value4 = "false"
		if returned5 == 'ok': value5 = "true"
		else: value5 = "false"
			
		setSkinSetting5('1', 'SelectionMarker', value1, 'SelectionMarker2', value2, 'ShadowButton', value3, 'OverlayButton', value4, 'background', value5)
		'''---------------------------'''
		
	if "C" in printpoint:
		value1 = ''
		setSkinSetting5('0', 'color340', value1, 'color341', value1, 'color342', value1, 'color343', value1, 'color344', value1)
		setSkinSetting5('0', 'color320', value1, 'color321', value1, 'color345', value1, 'color507', value1, 'color323', value1)
		setSkinSetting5('0', 'color351', value1, 'color327', value1, 'color325', value1, 'color508', value1, 'color322', value1)
		setSkinSetting5('0', 'color324', value1, 'color331', value1, 'color330', value1, 'color352', value1, 'color355', value1)
		setSkinSetting5('0', 'color357', value1, '', "", '', "", '', "", '', "")
		setSkinSetting5('0', 'color401', value1, 'color402', value1, 'color403', value1, 'color404', value1, 'color405', value1)
		setSkinSetting5('0', 'color601', value1, 'color602', value1, 'color603', value1, 'color604', value1, 'color605', value1)
		setSkinSetting5('0', 'color346', value1, 'color348', value1, 'color349', value1, '', "", '', "")
		'''---------------------------'''
	
	if "D" in printpoint:
		returned, value1 = getRandom("0", min=0, max=70, percent=50)
		returned, value2 = getRandom("0", min=0, max=70, percent=50)
		returned, value3 = getRandom("0", min=0, max=70, percent=50)
		returned, value4 = getRandom("0", min=0, max=70, percent=50)
		returned, value5 = getRandom("0", min=0, max=70, percent=50)
		listL = [value1, value2, value3, value4, value5]
		count = 0
		for value in listL:
			count += 1
			if value > 0 and value <= 5: value = ''
			elif value > 5 and value <= 10: value = 'base'
			elif value > 10 and value <= 15: value = 'lightblue'
			elif value > 15 and value <= 20: value = 'red'
			elif value > 20 and value <= 25: value = 'green'
			elif value > 25 and value <= 30: value = 'bluegray'
			elif value > 30 and value <= 35: value = 'progcolor'
			elif value > 35 and value <= 40: value = 'purple'
			elif value > 40 and value <= 45: value = 'teak'
			elif value > 45 and value <= 50: value = 'darkorange'
			elif value > 50 and value <= 55: value = 'darkblue'
			elif value > 55 and value <= 60: value = 'darkgreen'
			elif value > 60 and value <= 65: value = 'lightyellow'
			elif value > 65 and value <= 70: value = 'pink'
			
			if count == 1: value1 = value
			elif count == 2: value2 = value
			elif count == 3: value3 = value
			elif count == 4: value4 = value
			elif count == 5: value5 = value
			
		
		setSkinSetting5('0', 'color340', value1, 'color341', value2, 'color342', value3, 'color343', value4, 'color344', value5)
		setSkinSetting5('0', 'color320', value1, 'color321', value2, 'color345', value3, 'color507', value4, 'color323', value5)
		setSkinSetting5('0', 'color351', value1, 'color327', value2, 'color325', value3, 'color508', value4, 'color322', value5)
		setSkinSetting5('0', 'color324', value1, 'color331', value2, 'color330', value3, 'color352', value4, 'color355', value5)
		setSkinSetting5('0', 'color357', value1, '', "", '', "", '', "", '', "")
		setSkinSetting5('0', 'color401', value1, 'color402', value2, 'color403', value3, 'color404', value4, 'color405', value5)
		setSkinSetting5('0', 'color601', value1, 'color602', value2, 'color603', value3, 'color604', value4, 'color605', value5)
		setSkinSetting5('0', 'color346', value1, 'color348', value2, 'color349', value3, '', "", '', "")
		'''---------------------------'''
	
	if "E" in printpoint:
		setSkinSetting5('0', 'TopInformationColor', "", 'TopInformationColor_', "", 'TopVideoInformationColor', "", 'TopVideoInformationColor_', "", '', "")
		setSkinSetting5('0', 'MainBackgroundColor', "", 'MainBackgroundColor_', "", 'TopBackgroundColor', "", 'TopBackgroundColor_', "", '', "")
		'''---------------------------'''

	if "F" in printpoint:
		returned, value1 = getRandom("0", min=0, max=50, percent=50)
		returned, value2 = getRandom("0", min=0, max=50, percent=50)
		returned, value3 = getRandom("0", min=0, max=50, percent=50)
		returned, value4 = getRandom("0", min=0, max=50, percent=50)
		returned, value5 = getRandom("0", min=0, max=50, percent=50)
		listL = [value1, value2, value3, value4, value5]
		count = 0
		for value in listL:
			count += 1
			if value > 0 and value <= 5:
				value = ''
				value_ = 'Default'
			if value > 5 and value <= 10:
				value = 'A0'
				value_ = 'None'
			if value > 10 and value <= 15:
				value = 'A1'
				value_ = localize(762)
			if value > 15 and value <= 20:
				value = 'A2'
				value_ = localize(13343)
			if value > 20 and value <= 25:
				value = 'A3'
				value_ = localize(79151)
			if value > 25 and value <= 30:
				value = 'A4'
				value_ = localize(79152)
			if value > 30 and value <= 35:
				value = 'A5'
				value_ = localize(766)
			if value > 35 and value <= 40:
				value = 'A6'
				value_ = localize(767)
			if value > 40 and value <= 45:
				value = 'A7'
				value_ = localize(743)
			if value > 45 and value <= 50:
				value = 'A8'
				value_ = localize(353)
			
			if count == 1: value1 = value ; value1_ = value_
			elif count == 2: value2 = value ; value2_ = value_
			elif count == 3: value3 = value ; value3_ = value_
			elif count == 4: value4 = value ; value4_ = value_
			elif count == 5: value5 = value ; value5_ = value_
			
		
		setSkinSetting5('0', 'TopInformationColor', value1, 'TopInformationColor_', value1_, 'TopVideoInformationColor', value2, 'TopVideoInformationColor_', value2_, '', "")
		setSkinSetting5('0', 'MainBackgroundColor', value3, 'MainBackgroundColor_', value3_, 'TopBackgroundColor', value4, 'TopBackgroundColor_', value4_, '', "")
		'''---------------------------'''
		
	if "G" in printpoint:
		setSkinSetting5('0', 'IconOverlayButton', "", '', "", '', "", '', "", '', "") #BUTTONS
		setSkinSetting5('0', 'MenuButtonsOverlay', "", '', "", 'LeftMenuOverlay', "", 'BottomMenuOverlay', "", 'CenterMenuOverlay', "") #MENU
		setSkinSetting5('0', 'TopVideoInformationOverlay', "", 'TopMainBackgroundOverlay', "", 'TopInformationOverlay', "", 'MainBackgroundOverlay', "", 'BackgroundOverlay', "") #OTHERS
		setSkinSetting5('0', 'Background2Overlay', "", '', "", '', "", '', "", '', "") #OTHERS
		
		'''---------------------------'''
		
	if "H" in printpoint:
		returned, value1 = getRandom("0", min=0, max=55, percent=50)
		returned, value2 = getRandom("0", min=0, max=55, percent=50)
		returned, value3 = getRandom("0", min=0, max=55, percent=50)
		returned, value4 = getRandom("0", min=0, max=55, percent=50)
		returned, value5 = getRandom("0", min=0, max=55, percent=50)
		listL = [value1, value2, value3, value4, value5]
		count = 0
		for value in listL:
			count += 1
			if value > 0 and value <= 5: value = ''
			elif value > 5 and value <= 10: value = '10'
			elif value > 10 and value <= 15: value = '20'
			elif value > 15 and value <= 20: value = '30'
			elif value > 20 and value <= 25: value = '40'
			elif value > 25 and value <= 30: value = '50'
			elif value > 30 and value <= 35: value = '60'
			elif value > 35 and value <= 40: value = '70'
			elif value > 40 and value <= 45: value = '80'
			elif value > 45 and value <= 50: value = '90'
			elif value > 50 and value <= 55: value = '100'
			
			if count == 1: value1 = str(value)
			elif count == 2: value2 = str(value)
			elif count == 3: value3 = str(value)
			elif count == 4: value4 = str(value)
			elif count == 5: value5 = str(value)
			'''---------------------------'''
		
		setSkinSetting5('0', 'IconOverlayButton', value1, '', "", '', "", '', "", '', "") #BUTTONS
		setSkinSetting5('0', 'MenuButtonsOverlay', value1, '', "", 'LeftMenuOverlay', value1, 'BottomMenuOverlay', value2, 'CenterMenuOverlay', value3) #MENU
		setSkinSetting5('0', 'TopVideoInformationOverlay', value1, 'TopMainBackgroundOverlay', value2, 'TopInformationOverlay', value3, 'MainBackgroundOverlay', value2, 'BackgroundOverlay', value5) #OTHERS
		setSkinSetting5('0', 'Background2Overlay', value1, '', "", '', "", '', "", '', "") #OTHERS
		'''---------------------------'''
	
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		notification(".","","",1000)
		xbmc.sleep(200)
		xbmc.executebuiltin('Action(Back)')
		xbmc.sleep(800)
		notification("..","","",1000)
		xbmc.sleep(200)
		xbmc.executebuiltin('ReloadSkin()')
	print printfirst + name + "_LV" + printpoint + space + "list" + space2 + str(list) + space + "returned" + space2 + str(returned)
	'''---------------------------'''

def mode202(admin, name, printpoint):
	'''------------------------------
	---CHOOSE-COLORS-2---------------
	------------------------------'''
	container50hasfocus236 = xbmc.getCondVisibility('Container(50).HasFocus(236)') #TopBackgroundColor
	container50hasfocus251 = xbmc.getCondVisibility('Container(50).HasFocus(251)') #MainBackgroundColor
	container50hasfocus253 = xbmc.getCondVisibility('Container(50).HasFocus(253)') #TopInformationColor
	container50hasfocus255 = xbmc.getCondVisibility('Container(50).HasFocus(255)') #TopVideoInformationColor
	
	x = xbmc.getInfoLabel('Container(9003).ListItem(0).Label')
	x2 = xbmc.getInfoLabel('Container(9003).ListItemNoWrap(0).Property(colorID)')
	y = xbmc.getInfoLabel('Container(9003).ListItemNoWrap(0).Property(color)')
	listitempropertycolor = xbmc.getInfoLabel('ListItem.Property(color)')
	
	if customsettingtemp != "":
		printpoint = printpoint + "2"
		setSkinSetting('0', customsettingtemp, x2)
		if x2 != "": setSkinSetting('0', customsettingtemp + '_', x)
		else: setSkinSetting('0', customsettingtemp + '_', "")
		notification(localize(78020) + space + localize(78017), x, "", 2000)
		xbmc.executebuiltin('Action(Close)')
		'''---------------------------'''
	elif customhomecustomizerW and container50hasfocus236:
		printpoint = printpoint + "1"
		setSkinSetting('0', 'TopBackgroundColor', x2)
		if x2 != "": setSkinSetting('0', 'TopBackgroundColor_', x)
		else: setSkinSetting('0', 'TopBackgroundColor_', "")
		notification(localize(78020) + space + localize(78017), x, "", 2000)
		xbmc.executebuiltin('SetFocus(50)')
		'''---------------------------'''
	elif customhomecustomizerW and container50hasfocus251:
		printpoint = printpoint + "1"
		setSkinSetting('0', 'MainBackgroundColor', x2)
		if x2 != "": setSkinSetting('0', 'MainBackgroundColor_', x)
		else: setSkinSetting('0', 'MainBackgroundColor_', "")
		notification(localize(78020) + space + localize(78020), x, "", 2000)
		xbmc.executebuiltin('SetFocus(50)')
		'''---------------------------'''
	elif customhomecustomizerW and container50hasfocus253:
		printpoint = printpoint + "1"
		setSkinSetting('0', 'TopInformationColor', x2)
		if x2 != "": setSkinSetting('0', 'TopInformationColor_', x)
		else: setSkinSetting('0', 'TopInformationColor_', "")
		notification(localize(78020) + space + localize(78019), x, "", 2000)
		xbmc.executebuiltin('SetFocus(50)')
		'''---------------------------'''
	elif customhomecustomizerW and container50hasfocus255:
		printpoint = printpoint + "1"
		setSkinSetting('0', 'TopVideoInformationColor', x2)
		if x2 != "": setSkinSetting('0', 'TopVideoInformationColor_', x)
		else: setSkinSetting('0', 'TopVideoInformationColor_', "")
		notification(localize(78020) + space + localize(20159), x, "", 2000)
		xbmc.executebuiltin('SetFocus(50)')
		'''---------------------------'''
			
	else: printpoint = printpoint + "9"
	setSkinSetting("0",'Custom_Setting_Temp',"")
	print printfirst + name + "_LV" + printpoint + space + "x" + space2 + str(x) + space + "x2" + space2 + str(x2) + space + "y" + space2 + str(y)
	'''---------------------------'''

def mode203(value, admin, admin3, name, printpoint):
	'''------------------------------
	---Save and Load your skin design
	------------------------------'''
	extra = "" ; formula = "" ; formula_ = "" ; path = "" ; file1 = "" ; file2 = "" ; file3 = "" ; returned = ""
	container50hasfocus391 = xbmc.getCondVisibility('Container(50).HasFocus(391)') #BUTTONS
	if container50hasfocus391: list = ['-> (Exit)', 'Save', 'Load', 'Templates']
	else: list = []
	
	if list != []:
		returned, value = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
		
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		
		if returned == 1 or returned == 2 or (returned == "" and value == "Templates"): path = skin_userdata_path
		elif returned == 3: path = skin_specials_userdata_path
		else: path = ""
		
		if path != "":
			'''read existing files'''
			file1 = os.path.join(path, "Skin_SaveDesign1.txt")
			file2 = os.path.join(path, "Skin_SaveDesign2.txt")
			file3 = os.path.join(path, "Skin_SaveDesign3.txt")
			
			if os.path.exists(file1):
				infile1 = read_from_file(file1, silent=True)
				filename1 = regex_from_to(infile1, "&name=", "&", excluding=True)
			else: filename1 = None
			if os.path.exists(file2):
				infile2 = read_from_file(file2, silent=True)
				filename2 = regex_from_to(infile2, "&name=", "&", excluding=True)
			else: filename2 = None
			if os.path.exists(file3):
				infile3 = read_from_file(file3, silent=True)
				filename3 = regex_from_to(infile3, "&name=", "&", excluding=True)
			else: filename3 = None
			
			value1 = value + space + "1" + space + "(" + str(filename1) + ")"
			value2 = value + space + "2" + space + "(" + str(filename2) + ")"
			value3 = value + space + "3" + space + "(" + str(filename3) + ")"
			
			'''save/load'''
			if filename1 == None: value1 = '[COLOR=Red]' + value1 + '[/COLOR]'
			if filename2 == None: value2 = '[COLOR=Red]' + value2 + '[/COLOR]'
			if filename3 == None: value3 = '[COLOR=Red]' + value3 + '[/COLOR]'
		
		list = ['-> (Exit)', value1, value2, value3]
		
		returned2, value2 = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
		
		if returned2 == -1: printpoint = printpoint + "9"
		elif returned2 == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
		if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		
			if returned2 == 1: printpoint = printpoint + "1" #1
			elif returned2 == 2: printpoint = printpoint + "2" #2
			elif returned2 == 3: printpoint = printpoint + "3" #3
			
			if returned == 1: printpoint = printpoint + "A" #SAVE
			elif returned == 2 or (returned == "" and value == "Templates"): printpoint = printpoint + "B" #LOAD
			elif returned == 3: printpoint = printpoint + "C" #DEFAULT
	
			if "A" in printpoint:
				'''------------------------------
				---Save--------------------------
				------------------------------'''
				formula = ""
				#notification(shadowbutton.encode('utf-8'), selectionmarker, "", 4000)
				
				formula = "Skin.Theme=2" + skincurrenttheme
				
				formula = formula + newline + "SelectionMarker=1" + selectionmarker
				formula = formula + newline + "SelectionMarker2=1" + selectionmarker2
				formula = formula + newline + "ShadowButton=1" + shadowbutton
				formula = formula + newline + "OverlayButton=1" + overlaybutton
				
				formula = formula + newline + "background=1" + background
				formula = formula + newline + "BackgroundOverlay=0" + backgroundoverlay
				
				formula = formula + newline + "IconOverlayButton=0" + iconoverlaybutton
				formula = formula + newline + "MenuButtonsOverlay=0" + menubuttonsoverlay
				formula = formula + newline + "MainBackgroundOverlay=0" + mainbackgroundoverlay
				
				formula = formula + newline + "TopMainBackgroundOverlay=0" + topmainbackgroundoverlay
				formula = formula + newline + "LeftMenuOverlay=0" + leftmenuoverlay
				formula = formula + newline + "BottomMenuOverlay=0" + bottommenuoverlay
				formula = formula + newline + "CenterMenuOverlay=0" + centermenuoverlay
				formula = formula + newline + "TopVideoInformationOverlay=0" + topvideoinformationoverlay
				formula = formula + newline + "TopInformationOverlay=0" + topinformationoverlay
				
				formula = formula + newline + "MainBackgroundTexture=0" + mainbackgroundtexture
				formula = formula + newline + "TopBackgroundTexture=0" + topbackgroundtexture
				
				formula = formula + newline + "MainBackgroundColor=0" + mainbackgroundcolor
				formula = formula + newline + "MainBackgroundColor_=0" + mainbackgroundcolor_
				formula = formula + newline + "TopBackgroundColor=0" + topbackgroundcolor
				formula = formula + newline + "TopBackgroundColor_=0" + topbackgroundcolor_
				formula = formula + newline + "TopInformationColor=0" + topinformationcolor
				formula = formula + newline + "TopInformationColor_=0" + topinformationcolor_
				formula = formula + newline + "TopVideoInformationColor=0" + topvideoinformationcolor
				formula = formula + newline + "TopVideoInformationColor_=0" + topvideoinformationcolor_
				
				formula = formula + newline + "color340=0" + color340
				formula = formula + newline + "color341=0" + color341
				formula = formula + newline + "color342=0" + color342
				formula = formula + newline + "color343=0" + color343
				formula = formula + newline + "color344=0" + color344
				formula = formula + newline + "color320=0" + color320
				formula = formula + newline + "color321=0" + color321
				formula = formula + newline + "color345=0" + color345
				formula = formula + newline + "color507=0" + color507
				formula = formula + newline + "color323=0" + color323
				formula = formula + newline + "color351=0" + color351
				formula = formula + newline + "color327=0" + color327
				formula = formula + newline + "color325=0" + color325
				formula = formula + newline + "color508=0" + color508
				formula = formula + newline + "color322=0" + color322
				formula = formula + newline + "color324=0" + color324
				formula = formula + newline + "color331=0" + color331
				formula = formula + newline + "color330=0" + color330
				formula = formula + newline + "color352=0" + color352
				formula = formula + newline + "color355=0" + color355
				formula = formula + newline + "color357=0" + color357
				formula = formula + newline + "color401=0" + color401
				formula = formula + newline + "color402=0" + color402
				formula = formula + newline + "color403=0" + color403
				formula = formula + newline + "color404=0" + color404
				formula = formula + newline + "color405=0" + color405
				formula = formula + newline + "color601=0" + color601
				formula = formula + newline + "color602=0" + color602
				formula = formula + newline + "color603=0" + color603
				formula = formula + newline + "color606=0" + color606
				formula = formula + newline + "color605=0" + color605
				formula = formula + newline + "color346=0" + color346
				formula = formula + newline + "color348=0" + color348
				formula = formula + newline + "color349=0" + color349
				
				formula = formula + newline + "icon340=0" + icon340
				formula = formula + newline + "icon341=0" + icon341
				formula = formula + newline + "icon342=0" + icon342
				formula = formula + newline + "icon343=0" + icon343
				formula = formula + newline + "icon344=0" + icon344
				formula = formula + newline + "icon320=0" + icon320
				formula = formula + newline + "icon321=0" + icon321
				formula = formula + newline + "icon345=0" + icon345
				formula = formula + newline + "icon507=0" + icon507
				formula = formula + newline + "icon323=0" + icon323
				formula = formula + newline + "icon351=0" + icon351
				formula = formula + newline + "icon327=0" + icon327
				formula = formula + newline + "icon325=0" + icon325
				formula = formula + newline + "icon508=0" + icon508
				formula = formula + newline + "icon322=0" + icon322
				formula = formula + newline + "icon324=0" + icon324
				formula = formula + newline + "icon331=0" + icon331
				formula = formula + newline + "icon330=0" + icon330
				formula = formula + newline + "icon352=0" + icon352
				formula = formula + newline + "icon355=0" + icon355
				formula = formula + newline + "icon357=0" + icon357
				formula = formula + newline + "icon401=0" + icon401
				formula = formula + newline + "icon402=0" + icon402
				formula = formula + newline + "icon403=0" + icon403
				formula = formula + newline + "icon404=0" + icon404
				formula = formula + newline + "icon405=0" + icon405
				formula = formula + newline + "icon601=0" + icon601
				formula = formula + newline + "icon602=0" + icon602
				formula = formula + newline + "icon603=0" + icon603
				formula = formula + newline + "icon606=0" + icon606
				formula = formula + newline + "icon605=0" + icon605
				formula = formula + newline + "icon346=0" + icon346
				formula = formula + newline + "icon348=0" + icon348
				formula = formula + newline + "icon349=0" + icon349
				
				formula = formula + newline + "background340=0" + background340
				formula = formula + newline + "background341=0" + background341
				formula = formula + newline + "background342=0" + background342
				formula = formula + newline + "background343=0" + background343
				formula = formula + newline + "background344=0" + background344
				formula = formula + newline + "background320=0" + background320
				formula = formula + newline + "background321=0" + background321
				formula = formula + newline + "background345=0" + background345
				formula = formula + newline + "background507=0" + background507
				formula = formula + newline + "background323=0" + background323
				formula = formula + newline + "background351=0" + background351
				formula = formula + newline + "background327=0" + background327
				formula = formula + newline + "background325=0" + background325
				formula = formula + newline + "background508=0" + background508
				formula = formula + newline + "background322=0" + background322
				formula = formula + newline + "background324=0" + background324
				formula = formula + newline + "background331=0" + background331
				formula = formula + newline + "background330=0" + background330
				formula = formula + newline + "background352=0" + background352
				formula = formula + newline + "background355=0" + background355
				formula = formula + newline + "background357=0" + background357
				formula = formula + newline + "background401=0" + background401
				formula = formula + newline + "background402=0" + background402
				formula = formula + newline + "background403=0" + background403
				formula = formula + newline + "background404=0" + background404
				formula = formula + newline + "background405=0" + background405
				formula = formula + newline + "background601=0" + background601
				formula = formula + newline + "background602=0" + background602
				formula = formula + newline + "background603=0" + background603
				formula = formula + newline + "background606=0" + background606
				formula = formula + newline + "background605=0" + background605
				formula = formula + newline + "background346=0" + background346
				formula = formula + newline + "background348=0" + background348
				formula = formula + newline + "background349=0" + background349
				
				#formula = CleanString(formula, filter=[])
				
				#formula = str(formula).replace(", ",",")
				#formula = str(formula).replace(",",newline)
				
				if "1" in printpoint:
					if filename1 == None: filename = ""
					else: filename = filename1
				elif "2" in printpoint:
					if filename2 == None: filename = ""
					else: filename = filename2
				elif "3" in printpoint:
					if filename3 == None: filename = ""
					else: filename = filename3
				
				filename = dialogkeyboard(filename, localize(21821), 0, "", "", "") #Description
				filename_ = "&name="+str(filename)+"&"
				formula = filename_ + newline + formula
				
				#formula.decode('utf-8').encode('utf-8')
				try: formula.encode('utf-8')
				except: pass
				
				if "1" in printpoint:
					write_to_file(skin_userdata_path + "Skin_SaveDesign1.txt", str(formula), append=False, silent=True, utf8=False)
					setsetting('Skin_SaveDesign1', str(formula))
				elif "2" in printpoint:
					write_to_file(skin_userdata_path + "Skin_SaveDesign2.txt", str(formula), append=False, silent=True, utf8=False)
					setsetting('Skin_SaveDesign2', str(formula))
				elif "3" in printpoint:
					write_to_file(skin_userdata_path + "Skin_SaveDesign3.txt", str(formula), append=False, silent=True, utf8=False)
					setsetting('Skin_SaveDesign3', str(formula))
				'''---------------------------'''
			
			elif "B" in printpoint or "C" in printpoint:
				'''------------------------------
				---Load/Templates----------------
				------------------------------'''

				if "1" in printpoint:
					if filename1 == None: printpoint = printpoint + "Q"
					else: file = file1
				elif "2" in printpoint:
					if filename2 == None: printpoint = printpoint + "Q"
					else: file = file2
				elif "3" in printpoint:
					if filename2 == None: printpoint = printpoint + "Q"
					else: file = file3
				
				if "Q" in printpoint or file == "":
					'''nothing to load'''
					notification("There is no data to load!", "You should create a save session", "", 4000)
				else:
					#formula_ = formula_.split(',')
					#formula_ = CleanString(formula_, filter=[])
					import fileinput
					for line in fileinput.input([file]):
						x = "" ; x1 = "" ; x2 = "" ; x3 = ""
						if "=0" in line:
							'''Skin.String'''
							x = line.replace("=0","=")
							x1 = find_string(x, "", "=")
							x2 = find_string(x, "=", "")
							x1 = x1.replace("=","")
							x2 = x2.replace("=","")
							x2 = x2.replace("\n","")
							setSkinSetting('0', str(x1), str(x2))
							
						elif "=1" in line:
							'''Skin.HasSetting'''
							x = line.replace("=1","=")
							x1 = find_string(x, "", "=")
							x2 = find_string(x, "=", "")
							x1 = x1.replace("=","")
							x2 = x2.replace("=","")
							x2 = x2.replace("\n","")
							if x2 == "": x3 = "false"
							else: x3 = "true" ; x2 = "*" + x2 + "*"
							setSkinSetting('1', str(x1), str(x3))
						
						elif "=2" in line:
							'''xbmc.executebuiltin'''
							x = line.replace("=2","=")
							x1 = find_string(x, "", "=")
							x2 = find_string(x, "=", "")
							x1 = x1.replace("=","")
							x2 = x2.replace("=","")
							x2 = x2.replace("\n","")
							
							if x1 == "Skin.Theme":
								pass
								#xbmc.executebuiltin('Skin.Theme(SKINDEFAULT)')
								#xbmc.executehttpapi( "SetGUISetting(3;lookandfeel.skintheme;%s)"  % x2 )
								#if x2 == "SKINDEFAULT": xbmc.executebuiltin('Skin.Theme(SKINDEFAULT)')
								#else: notification(str(x2),"","",3000)
							#xbmc.executebuiltin(''+x1+'('+ x2 +')')
							#xbmc.executebuiltin('AlarmClock(delayskinupdate, '+x1+'('+ x2 +'), 00:02, silent)')
						else: pass
							
						if admin3 and admin: extra = extra + newline + space + "line" + space2 + str(line) + space + "x" + space2 + str(x) + space + "x1" + space2 + str(x1) + space + "x2" + space2 + str(x2) + space + "x3" + space2 + str(x3)
						'''---------------------------'''
			
			if not "Q" in printpoint and not "A" in printpoint:
				notification(".","","",1000)
				xbmc.sleep(200)
				xbmc.executebuiltin('Action(Back)')
				xbmc.sleep(800)
				notification("..","","",1000)
				xbmc.sleep(200)
				xbmc.executebuiltin('ReloadSkin()')
				xbmc.executebuiltin('ActivateWindow(1173)')
				'''---------------------------'''

	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + newline + \
		"path" + space2 + str(path) + newline + \
		"file1" + space2 + str(file1) + newline + \
		"file2" + space2 + str(file2) + newline + \
		"file3" + space2 + str(file3) + newline + \
		"formula" + space2 + str(formula) + space + "formula_" + space2 + str(formula_) + newline + \
		"Skin_SaveDesign1" + space2 + str(Skin_SaveDesign1) + newline + \
		"extra" + space2 + str(extra)
		
def mode204(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode204(admin, name, printpoint)
	'''---------------------------'''

def mode205(admin, name, printpoint):
	'''------------------------------
	---SET-STARTUP-WINDOW------------
	------------------------------'''
	container50button320 = xbmc.getCondVisibility('Container(50).HasFocus(320)')
	container50button321 = xbmc.getCondVisibility('Container(50).HasFocus(321)')
	
	if container50button320:
		'''------------------------------
		---MOVIES------------------------
		------------------------------'''
		printpoint = printpoint + "1"
		heading = localize(512) + space + localize(342)
		list0 = "0. " + localize(20108) #root
		list1 = "1. " + addonString_genesis(30027).encode('utf-8') #Most Popular
		list2 = "2. " + addonString_genesis(30806).encode('utf-8') #Latest HD Movies
		list3 = "3. " + addonString_genesis(30009).encode('utf-8') #Search
		list4 = "4. " + addonString_genesis(30021).encode('utf-8') #Genres
		returned, value = dialogselect(heading,[list0, list1, list2, list3, list4],0)
		if returned != -1:
			setSkinSetting("0",'moviesestartup',str(returned))
			#setSkinSetting("0",'moviesestartup',value)
			'''---------------------------'''
		
	elif container50button321:
		'''------------------------------
		---TVSHOWS------------------------
		------------------------------'''
		printpoint = printpoint + "2"
		heading = localize(512) + space + localize(20343)
		list0 = "0. " + localize(20108) #root
		list1 = "1. " + addonString_genesis(30027).encode('utf-8') #Most Popular
		list2 = "2. " + addonString_genesis(30544).encode('utf-8') #Returning TV Shows
		list3 = "3. " + addonString_genesis(30009).encode('utf-8') #Search
		list4 = "4. " + addonString_genesis(30021).encode('utf-8') #Genres
		returned, value = dialogselect(heading,[list0, list1, list2, list3, list4],0)
		if returned != -1:
			setSkinSetting("0",'tvshowsestartup',str(returned))
			'''---------------------------'''
	else: printpoint = printpoint + "9"

def mode206(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode206(admin, name, printpoint)
	'''---------------------------'''

def mode207(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode207(admin, name, printpoint)
	'''---------------------------'''

def mode208(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode208(admin, name, printpoint)
	'''---------------------------'''

def mode209(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode209(admin, name, printpoint)
	'''---------------------------'''

def mode210(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode240(admin, name, printpoint)
	'''---------------------------'''
	
def mode211(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode211(admin, name, printpoint)
	'''---------------------------'''

def mode212(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode212(admin, name, printpoint)
	'''---------------------------'''

def mode213(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode213(admin, name, printpoint)
	'''---------------------------'''

def mode214(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode214(admin, name, printpoint)
	'''---------------------------'''

def mode215(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode215(admin, name, printpoint)
	'''---------------------------'''

def mode216(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode216(admin, name, printpoint)
	'''---------------------------'''

def mode217(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode217(admin, name, printpoint)
	'''---------------------------'''

def mode218(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode218(admin, name, printpoint)
	'''---------------------------'''

def mode219(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode219(admin, name, printpoint)
	'''---------------------------'''

def mode220(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode220(admin, name, printpoint)
	'''---------------------------'''
	
def mode221(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode221(admin, name, printpoint)
	'''---------------------------'''

def mode222(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode222(admin, name, printpoint)
	'''---------------------------'''

def mode223(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode223(admin, name, printpoint)
	'''---------------------------'''

def mode224(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode224(admin, name, printpoint)
	'''---------------------------'''

def mode225(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode225(admin, name, printpoint)
	'''---------------------------'''

def mode226(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode226(admin, name, printpoint)
	'''---------------------------'''

def mode227(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode227(admin, name, printpoint)
	'''---------------------------'''

def mode228(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode228(admin, name, printpoint)
	'''---------------------------'''

def mode229(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode229(admin, name, printpoint)
	'''---------------------------'''

def mode230(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode230(admin, name, printpoint)
	'''---------------------------'''
	
def mode231(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode231(admin, name, printpoint)
	'''---------------------------'''

def mode232(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode232(admin, name, printpoint)
	'''---------------------------'''

def mode233(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode233(admin, name, printpoint)
	'''---------------------------'''

def mode234(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode234(admin, name, printpoint)
	'''---------------------------'''

def mode235(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode235(admin, name, printpoint)
	'''---------------------------'''

def mode236(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode236(admin, name, printpoint)
	'''---------------------------'''

def mode237(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode237(admin, name, printpoint)
	'''---------------------------'''

def mode238(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode238(admin, name, printpoint)
	'''---------------------------'''

def mode239(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode239(admin, name, printpoint)
	'''---------------------------'''

def mode240(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode240(admin, name, printpoint)
	'''---------------------------'''
	
def mode241(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode241(admin, name, printpoint)
	'''---------------------------'''

def mode242(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode242(admin, name, printpoint)
	'''---------------------------'''

def mode243(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode243(admin, name, printpoint)
	'''---------------------------'''

def mode244(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode244(admin, name, printpoint)
	'''---------------------------'''

def mode245(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode245(admin, name, printpoint)
	'''---------------------------'''

def mode246(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode246(admin, name, printpoint)
	'''---------------------------'''

def mode247(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode247(admin, name, printpoint)
	'''---------------------------'''

def mode248(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode248(admin, name, printpoint)
	'''---------------------------'''

def mode249(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode249(admin, name, printpoint)
	'''---------------------------'''

def mode250(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode250(admin, name, printpoint)
	'''---------------------------'''

def mode251(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode251(admin, name, printpoint)
	'''---------------------------'''

def mode252(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode252(admin, name, printpoint)
	'''---------------------------'''

def mode253(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode253(admin, name, printpoint)
	'''---------------------------'''

def mode254(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode254(admin, name, printpoint)
	'''---------------------------'''

def mode255(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode255(admin, name, printpoint)
	'''---------------------------'''

def mode256(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode256(admin, name, printpoint)
	'''---------------------------'''

def mode257(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode257(admin, name, printpoint)
	'''---------------------------'''

def mode258(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode258(admin, name, printpoint)
	'''---------------------------'''

def mode259(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode259(admin, name, printpoint)
	'''---------------------------'''

def mode260(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode260(admin, name, printpoint)
	'''---------------------------'''

def mode261(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode261(admin, name, printpoint)
	'''---------------------------'''

def mode262(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode262(admin, name, printpoint)
	'''---------------------------'''

def mode263(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode263(admin, name, printpoint)
	'''---------------------------'''

def mode264(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode264(admin, name, printpoint)
	'''---------------------------'''

def mode265(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode265(admin, name, printpoint)
	'''---------------------------'''

def mode266(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode266(admin, name, printpoint)
	'''---------------------------'''

def mode267(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode267(admin, name, printpoint)
	'''---------------------------'''

def mode268(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode268(admin, name, printpoint)
	'''---------------------------'''

def mode269(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode269(admin, name, printpoint)
	'''---------------------------'''

def mode270(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode270(admin, name, printpoint)
	'''---------------------------'''

def mode271(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode271(admin, name, printpoint)
	'''---------------------------'''

def mode272(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode272(admin, name, printpoint)
	'''---------------------------'''

def mode273(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode273(admin, name, printpoint)
	'''---------------------------'''

def mode274(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode274(admin, name, printpoint)
	'''---------------------------'''

def mode275(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode275(admin, name, printpoint)
	'''---------------------------'''

def mode276(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode276(admin, name, printpoint)
	'''---------------------------'''

def mode277(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode277(admin, name, printpoint)
	'''---------------------------'''

def mode278(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode278(admin, name, printpoint)
	'''---------------------------'''

def mode279(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode279(admin, name, printpoint)
	'''---------------------------'''
	
def mode280(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode280(admin, name, printpoint)
	'''---------------------------'''

def mode281(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode281(admin, name, printpoint)
	'''---------------------------'''

def mode282(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode282(admin, name, printpoint)
	'''---------------------------'''

def mode283(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode283(admin, name, printpoint)
	'''---------------------------'''

def mode284(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode284(admin, name, printpoint)
	'''---------------------------'''

def mode285(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode285(admin, name, printpoint)
	'''---------------------------'''

def mode286(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode286(admin, name, printpoint)
	'''---------------------------'''

def mode287(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode287(admin, name, printpoint)
	'''---------------------------'''

def mode288(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode288(admin, name, printpoint)
	'''---------------------------'''

def mode289(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode289(admin, name, printpoint)
	'''---------------------------'''
	
def mode290(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode290(admin, name, printpoint)
	'''---------------------------'''

def mode291(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode291(admin, name, printpoint)
	'''---------------------------'''

def mode292(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode292(admin, name, printpoint)
	'''---------------------------'''

def mode293(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode293(admin, name, printpoint)
	'''---------------------------'''

def mode294(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode294(admin, name, printpoint)
	'''---------------------------'''

def mode295(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode295(admin, name, printpoint)
	'''---------------------------'''

def mode296(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode296(admin, name, printpoint)
	'''---------------------------'''

def mode297(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode297(admin, name, printpoint)
	'''---------------------------'''

def mode298(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode298(admin, name, printpoint)
	'''---------------------------'''

def mode299(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode299(admin, name, printpoint)
	'''---------------------------'''

def mode300(admin, name, printpoint):
	'''------------------------------
	---SEARCH-SDAROT-TV--------------
	------------------------------'''
	xbmc.executebuiltin('Control.SetFocus(50)')
	url = 'plugin://plugin.video.sdarot.tv/?mode=6&name=%5bCOLOR%20red%5d%20%d7%97%d7%a4%d7%a9%20%20%5b%2fCOLOR%5d&url=http%3a%2f%2fwww.sdarot.wf%2fsearch'
	ActivateWindow("1", 'plugin.video.sdarot.tv', url, 'return0', wait=False)
	'''---------------------------'''

def mode301(admin, name, printpoint):
	'''------------------------------
	---Numi-Numi---------------------
	------------------------------'''
	pl=xbmc.PlayList(1)
	pl.clear()
	count = 0
	while count < 7 and not xbmc.abortRequested:
		xbmc.sleep(10)
		count += 1
		listitem = xbmcgui.ListItem(numinumistr,
		thumbnailImage='special://skin/media/icons/kids.png')
		url = 'special://userdata/addon_data/skin.htpt/video/numinumi.mp4'
		xbmc.PlayList(1).add(url, listitem)

	xbmc.Player().play(pl)
	xbmc.executebuiltin('Action(Right)')
	xbmc.executebuiltin('Action(PageUp)')
	xbmc.executebuiltin('Action(FullScreen)')
	'''---------------------------'''

def mode302(admin, name, printpoint):
	'''------------------------------
	---SUBSLIDER---------------------
	------------------------------'''
	path = os.path.join(addonPath, 'specials', 'scripts', 'subslider.py')
	xbmc.executebuiltin('RunScript('+ path +', -10)')
	'''---------------------------'''

def mode303(admin, name, printpoint):
	'''------------------------------
	---HELP-DIALOG-------------------
	------------------------------'''
	myvideopath = xbmc.getCondVisibility('SubString(Container.FolderPath,special://userdata/library/videos)') or xbmc.getCondVisibility('SubString(Container.FolderPath,/var/media/)') or xbmc.getCondVisibility('SubString(Container.FolderPath,special://home/external/)') or xbmc.getCondVisibility('SubString(Container.FolderPath,sources://video/)') or xbmc.getCondVisibility('Skin.String(VarCurrentPicVid)')
	if mypicsW:
		HelpButton_Video_Pic(str1, 'pictures')
		'''---------------------------'''
	elif mymusicnavW:
		HelpButton_Video_Pic(str2, 'music')
		'''---------------------------'''
	elif (myvideonavW and myvideopath):
		HelpButton_Video_Pic(str3, 'videos')
		'''---------------------------'''

def mode304(admin, name, printpoint):
	'''------------------------------
	---USBTOGGLE---------------------
	------------------------------'''
	#videopath0 = xbmc.getCondVisibility('SubString(Container.FolderPath,special://userdata/library/videos/)')
	externalusb("", 304)
	if systemplatformwindows:
		path0 = 'special://userdata/library/'
		pathwin = 'special://home/external/'
		if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path0 +')'):
			if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ pathwin +'videos/,return)')
			if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ pathwin +'pictures/,return)')
		if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ pathwin +')'):
			if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'videos/,return)')
			if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'pictures/,return)')
			'''---------------------------'''

def mode305(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode305(admin, name, printpoint)
	'''---------------------------'''

def mode306(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode306(admin, name, printpoint)
	'''---------------------------'''

def mode307(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode307(admin, name, printpoint)
	'''---------------------------'''

def mode308(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode308(admin, name, printpoint)
	'''---------------------------'''

def mode309(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode309(admin, name, printpoint)
	'''---------------------------'''

def mode310(admin, name, printpoint):
	'''------------------------------
	---SPORT-1-LIVE------------------
	------------------------------'''
	if connected:
		count = ""
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		returned = ActivateWindow("1", 'plugin.video.vdubt', 'plugin://plugin.video.vdubt/', 0, wait=True)
		if "ok" in returned:
			printpoint = printpoint + "1"
			systemcurrentcontrol = findin_systemcurrentcontrol("0","[..]",0,'Action(PageUp)','')
			systemcurrentcontrol = findin_systemcurrentcontrol("0","[..]",100,'Action(PageUp)','Action(Down)')
			xbmc.sleep(100)
			notification(systemcurrentcontrol, "", "" ,2000)
			systemcurrentcontrol = findin_systemcurrentcontrol("1","Live",40,'Action(Down)','Action(Select)')
			systemcurrentcontrol = findin_systemcurrentcontrol("1","Live Sports",40,'Action(Down)','Action(Select)')
			xbmc.sleep(500)
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
			containernumitems = xbmc.getInfoLabel('Container.NumItems')
			count = 0
			while count < 10 and (dialogbusyW or containernumitems != "0") and not xbmc.abortRequested:
				count += 1
				xbmc.sleep(200)
				dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
				containernumitems = xbmc.getInfoLabel('Container.NumItems')
				systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
				if dialogbusyW and systemidle1: xbmc.sleep(500)
				'''---------------------------'''
			systemcurrentcontrol = findin_systemcurrentcontrol("0","[..]",100,'','Action(Down)')
			if systemcurrentcontrol == "[..]":
				container50listitem2label = xbmc.getInfoLabel('Container(50).ListItem(1).Label')
				if not "LIVE Sports 24/7" in container50listitem2label:
					'''------------------------------
					---NO-LIVE-MATCHS----------------
					------------------------------'''
					dialogok(localize(78918), localize(78916) + space2, localize(78920),"")
					'''---------------------------'''
				else:
					'''------------------------------
					---LIVE-MATCHS-FOUND!------------
					------------------------------'''
					dialogok(localize(78917), localize(78919) + '[CR]' + '[COLOR=Yellow]' + "LIVE FOOTBALL" + '[/COLOR]',"","")
					'''---------------------------'''
		if admin: print printfirst + "mode15_LV" + printpoint + space + "systemcurrentcontrol" + space2 + systemcurrentcontrol + space + "count" + space2 + str(count)
	elif not connected: notification_common("5")
	'''---------------------------'''
	
def mode311(admin, name, printpoint):
	'''------------------------------
	---SPORT-2-LIVE------------------
	------------------------------'''
	if connected:
		addon = 'plugin.video.p2p-streams'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			'''------------------------------
			---plugin.video.p2p-streams------
			------------------------------'''
			printpoint = printpoint + "1"
			addonsettings2(addon,'ace-debug',"false",'save',"false",'parser_sync',"true",'run_a_python_script',"http://bit.ly/allparsers",'russian_translation',"true")
			addonsettings2(addon,'addon_history',"true",'items_per_page',"20",'autoconfig',"true",'timezone_new',"496",'hide_porn',"true")
			addonsettings2(addon,'',"",'',"",'',"",'',"",'',"")
			addonsettings2(addon,'',"",'',"",'',"",'',"",'',"")
			
			parser_path = os.path.join(addondata_path, 'plugin.video.p2p-streams', 'parser' ,'')
			folders_count, folders_count2, files_count = bash_count(parser_path)
			if int(files_count) < 7:
				printpoint = printpoint + "2"
				xbmc.executebuiltin('XBMC.RunPlugin(plugin://plugin.video.p2p-streams/?mode=404&name=p2p&url=p2p)')
				import json
				dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
				count = 0
				while count < 10 and not dialogkeyboardW and not xbmc.abortRequested:
					dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
					xbmc.sleep(1000)
					count += 1
					'''---------------------------'''
				if count < 10:
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"http://bit.ly/allparsers","done":false}}')
					xbmc.sleep(100)
					xbmc.executebuiltin('Action(Select)')
					'''---------------------------'''
				else: xbmc.executebuiltin('Action(Back)')
			else: printpoint = printpoint + "3"
			
			if systemplatformwindows:
				p2pstreams_path = os.path.join(addondata_path, 'plugin.video.p2p-streams', '')
				ace_engine = os.path.join(addondata_path, 'plugin.video.p2p-streams', 'acestream', 'ace_engine.exe')
				ace_player = os.path.join(addondata_path, 'plugin.video.p2p-streams', 'player', 'ace_player.exe')
				if not os.path.exists(ace_engine) or not os.path.exists(ace_player):
					notification("downloading AceEngine...", "Please wait", "", 7000)
					file = "AceEngine.zip"
					fileID = getfileID(file)
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/AceEngine.zip?dl=1", file, temp_path, p2pstreams_path, silent=True)
				else: printpoint = printpoint + "A"
			
			returned = ActivateWindow("1", 'plugin.video.p2p-streams', 'plugin://plugin.video.p2p-streams/?iconimage=C%3a%5cUsers%5cgal%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.p2p-streams%5cresources%5ccore%5cparsers%5clivefootballws%5cicon.png&mode=401&name=Livefootball.ws&parser=livefootballws&url=https%3a%2f%2fcode.google.com%2fp%2fp2p-strm%2f', 0, wait=True)
			
			if "ok" in returned:
				printpoint = printpoint + "4"
				systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
				systemcurrentcontrol = findin_systemcurrentcontrol("0","[..]",100,'Action(PageUp)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0","[..]",100,'Action(PageUp)','Action(Down)')
				xbmc.sleep(500)
				containernumitems = xbmc.getInfoLabel('Container.NumItems')
				
				if not "(Online)" in xbmc.getInfoLabel('Container(50).ListItem(0).Label') and not "ONLINE" in xbmc.getInfoLabel('Container(50).ListItem(1).Label'):
					'''------------------------------
					---NO-LIVE-MATCHS----------------
					------------------------------'''
					dialogok(localize(78918), localize(78916) + space2, localize(78920),"")
					'''---------------------------'''
				else:
					'''------------------------------
					---LIVE-MATCHS-FOUND!------------
					------------------------------'''
					dialogok(addonString(40).encode('utf-8'),localize(78919) + '[CR]' + '[COLOR=Yellow]' + "LIVE FOOTBALL" + '[/COLOR]',"","")
					'''---------------------------'''
					
			else: printpoint = printpoint + "6"
			'''---------------------------'''
		else:
			#if "A" in id10str or "B" in id10str:
			printpoint = printpoint + "8"
			installaddon(admin, addon, "")
			'''---------------------------'''
		
	else: notification_common("5")
	'''---------------------------'''
	if admin: print printfirst + name + "_LV" + printpoint + space

def mode312(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode312(admin, name, printpoint)
	'''---------------------------'''

def mode313(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode313(admin, name, printpoint)
	'''---------------------------'''

def mode314(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode314(admin, name, printpoint)
	'''---------------------------'''

def mode315(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode315(admin, name, printpoint)
	'''---------------------------'''

def mode316(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode316(admin, name, printpoint)
	'''---------------------------'''

def mode317(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode317(admin, name, printpoint)
	'''---------------------------'''

def mode318(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode318(admin, name, printpoint)
	'''---------------------------'''

def mode319(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode319(admin, name, printpoint)
	'''---------------------------'''

def mode320(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode320(admin, name, printpoint)
	'''---------------------------'''
	
def mode321(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode321(admin, name, printpoint)
	'''---------------------------'''

def mode322(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode322(admin, name, printpoint)
	'''---------------------------'''

def mode323(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode323(admin, name, printpoint)
	'''---------------------------'''

def mode324(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode324(admin, name, printpoint)
	'''---------------------------'''

def mode325(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode325(admin, name, printpoint)
	'''---------------------------'''

def mode326(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode326(admin, name, printpoint)
	'''---------------------------'''

def mode327(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode327(admin, name, printpoint)
	'''---------------------------'''

def mode328(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode328(admin, name, printpoint)
	'''---------------------------'''

def mode329(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode329(admin, name, printpoint)
	'''---------------------------'''

def mode330(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode330(admin, name, printpoint)
	'''---------------------------'''
	
def mode331(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode331(admin, name, printpoint)
	'''---------------------------'''

def mode332(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode332(admin, name, printpoint)
	'''---------------------------'''

def mode333(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode333(admin, name, printpoint)
	'''---------------------------'''

def mode334(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode334(admin, name, printpoint)
	'''---------------------------'''

def mode335(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode335(admin, name, printpoint)
	'''---------------------------'''

def mode336(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode336(admin, name, printpoint)
	'''---------------------------'''

def mode337(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode337(admin, name, printpoint)
	'''---------------------------'''

def mode338(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode338(admin, name, printpoint)
	'''---------------------------'''

def mode339(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode339(admin, name, printpoint)
	'''---------------------------'''

def mode340(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode340(admin, name, printpoint)
	'''---------------------------'''
	
def mode341(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode341(admin, name, printpoint)
	'''---------------------------'''

def mode342(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode342(admin, name, printpoint)
	'''---------------------------'''

def mode343(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode343(admin, name, printpoint)
	'''---------------------------'''

def mode344(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode344(admin, name, printpoint)
	'''---------------------------'''

def mode345(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode345(admin, name, printpoint)
	'''---------------------------'''

def mode346(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode346(admin, name, printpoint)
	'''---------------------------'''

def mode347(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode347(admin, name, printpoint)
	'''---------------------------'''

def mode348(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode348(admin, name, printpoint)
	'''---------------------------'''

def mode349(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode349(admin, name, printpoint)
	'''---------------------------'''

def mode350(admin, name, printpoint):
	'''------------------------------
	---AIRPLAY-BUTTON----------------
	------------------------------'''
	from variables import sgbserviceszeroconf, sgbservicesairplay
	xbmc.executebuiltin('ActivateWindow(servicesettings)')
	settingscategoryW = xbmc.getCondVisibility('Window.IsVisible(SettingsCategory.xml)')
	count = 0
	while count < 10 and not settingscategoryW and not xbmc.abortRequested:
		if count == 0: printpoint = printpoint + "0"
		xbmc.sleep(40)
		settingscategoryW = xbmc.getCondVisibility('Window.IsVisible(SettingsCategory.xml)')
		count += 1
	settingslevelset("2")
	'''---------------------------'''
	if not sgbserviceszeroconf:
		printpoint = printpoint + "1"
		count = 0
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		while count < 5 and systemcurrentcontrol != localize(1259) and not xbmc.abortRequested:
			'''Zeroconf'''
			if count == 0: printpoint = printpoint + "2"
			systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1259),40,'Action(Left)','Action(Down)')
			count += 1
			'''---------------------------'''
		count = 0
		while count < 5 and not localize(1260) in systemcurrentcontrol and not xbmc.abortRequested:
			'''Announce these services to other systems via Zeroconf'''
			if count == 0:
				printpoint = printpoint + "3"
				systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(1260),40,'','Action(Select)')
			else: systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(1260),40,'Action(Down)','Action(Select)')
			count += 1
			'''---------------------------'''
		count = 0
		while count < 5 and systemcurrentcontrol != localize(1259) and not xbmc.abortRequested:
			'''Zeroconf'''
			if count == 0: printpoint = printpoint + "2"
			systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1259),40,'Action(Up)','Action(Right)')
			count += 1
			'''---------------------------'''
		sgbserviceszeroconf = xbmc.getCondVisibility('System.GetBool(services.zeroconf)')
		
	if sgbserviceszeroconf:
		printpoint = printpoint + "4"
		'''---------------------------'''
		systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1273),40,'Action(Left)','Action(Down)')
		count = 0
		while count < 5 and systemcurrentcontrol != localize(1273) and not xbmc.abortRequested:
			'''AirPlay'''
			if count == 0: printpoint = printpoint + "5"
			systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1273),40,'Action(Left)','Action(Down)')
			count += 1
			'''---------------------------'''
		
		systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(1273),40,'Action(Down)','')
		count = 0
		while count < 5 and not localize(1273) in systemcurrentcontrol and not xbmc.abortRequested:
			'''if Allow to receive AirPlay content'''
			if count == 0: printpoint = printpoint + "6"
			systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(1273),40,'Action(Down)','')
			count += 1
			'''---------------------------'''
		if count < 5:
			printpoint = printpoint + "8"
			systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(1273),40,'','Action(Select)')
			xbmc.sleep(500)
			if sgbservicesairplay: systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(1273),40,'','Action(Select)')
			'''---------------------------'''
		
		xbmc.executebuiltin('Action(Back)')
		xbmc.sleep(1000)
		xbmc.executebuiltin('Action(Down)')
		sgbservicesairplay = xbmc.getCondVisibility('System.GetBool(services.airplay)')
		sgbserviceszeroconf = xbmc.getCondVisibility('System.GetBool(services.zeroconf)')
		xbmc.sleep(500)
		if sgbserviceszeroconf and sgbservicesairplay:
			printpoint = printpoint + "7"
			notification_common("13")
			dialogok('[COLOR=Yellow]' + localize(75794) + '[/COLOR]', localize(75780), localize(75779), "")
			returned = dialogyesno(localize(75778), localize(75777))
			if returned != "ok":
				'''Extra Help with AirPlay'''
				dialogok('[COLOR=Yellow]' + localize(75778) + '[/COLOR]', localize(75785) + space2, localize(75776), "")
			#xbmc.executebuiltin('Notification($LOCALIZE[79063],$LOCALIZE[79064],5000)')
			
		elif not sgbserviceszeroconf: notification(localize(257),'$LOCALIZE[34302]',"",4000)
		else:
			printpoint = printpoint + "9"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "airplaybutton_LV" + printpoint
	'''---------------------------'''

	'''---------------------------'''

def settingslevelset(custom):
	'''custom: 1 = Basic, 2 = Standard, 3 = Advanced, 4 = Expert'''
	if custom == "1": custom = settingslevelstr1
	elif custom == "2": custom = settingslevelstr2
	elif custom == "3": custom = settingslevelstr3
	elif custom == "4": custom = settingslevelstr4
	else: sys.exit(1)
	'''---------------------------'''
	printpoint = ""
	settingslevel = xbmc.getInfoLabel('Skin.String(SettingsLevel)')
	'''---------------------------'''
	if settingslevel != custom:
		controlhasfocus = findin_controlhasfocus("0","20",40,'Control.SetFocus(20)','')
		count = 0
		while count < 5 and not controlhasfocus and not xbmc.abortRequested:
			if count == 0: printpoint = printpoint + "2"
			controlhasfocus = findin_controlhasfocus("0","20",40,'Control.SetFocus(20)','')
			count += 1
			'''---------------------------'''
		if controlhasfocus:
			printpoint = printpoint + "3"
			count = 0
			while count < 5 and settingslevel != custom and not xbmc.abortRequested:
				if count == 0: printpoint = printpoint + "5"
				count += 1
				systemcurrentcontrol = findin_systemcurrentcontrol("0",custom,10,'Action(Select)','Action(Down)')
				settingslevel = xbmc.getInfoLabel('Skin.String(SettingsLevel)')
				'''---------------------------'''
		else: printpoint = printpoint + "9"
	else:
		printpoint = printpoint + "8"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "settingslevelset_LV" + printpoint
	'''---------------------------'''
	
def mode351(admin, admin2, admin3, name, printpoint):
	'''------------------------------
	---MESSAGE-BUTTON----------------
	------------------------------'''
	if systemplatformwindows and admin and not admin2 and admin3:
		xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.programm.htptmail/mailbox/INBOX/,return)')
		'''---------------------------'''
	else: notification_common("10")
	'''---------------------------'''
	
def mode352(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode352(admin, name, printpoint)
	'''---------------------------'''

def mode353(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode353(admin, name, printpoint)
	'''---------------------------'''

def mode354(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode354(admin, name, printpoint)
	'''---------------------------'''

def mode355(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode355(admin, name, printpoint)
	'''---------------------------'''

def mode356(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode356(admin, name, printpoint)
	'''---------------------------'''

def mode357(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode357(admin, name, printpoint)
	'''---------------------------'''

def mode358(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode358(admin, name, printpoint)
	'''---------------------------'''

def mode359(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode359(admin, name, printpoint)
	'''---------------------------'''

def mode360(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode360(admin, name, printpoint)
	'''---------------------------'''

def mode361(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode361(admin, name, printpoint)
	'''---------------------------'''

def mode362(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode362(admin, name, printpoint)
	'''---------------------------'''

def mode363(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode363(admin, name, printpoint)
	'''---------------------------'''

def mode364(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode364(admin, name, printpoint)
	'''---------------------------'''

def mode365(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode365(admin, name, printpoint)
	'''---------------------------'''

def mode366(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode366(admin, name, printpoint)
	'''---------------------------'''

def mode367(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode367(admin, name, printpoint)
	'''---------------------------'''

def mode368(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode368(admin, name, printpoint)
	'''---------------------------'''

def mode369(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode369(admin, name, printpoint)
	'''---------------------------'''

def mode370(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode370(admin, name, printpoint)
	'''---------------------------'''

def mode371(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode371(admin, name, printpoint)
	'''---------------------------'''

def mode372(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode372(admin, name, printpoint)
	'''---------------------------'''

def mode373(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode373(admin, name, printpoint)
	'''---------------------------'''

def mode374(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode374(admin, name, printpoint)
	'''---------------------------'''

def mode375(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode375(admin, name, printpoint)
	'''---------------------------'''

def mode376(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode376(admin, name, printpoint)
	'''---------------------------'''

def mode377(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode377(admin, name, printpoint)
	'''---------------------------'''

def mode378(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode378(admin, name, printpoint)
	'''---------------------------'''

def mode379(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode379(admin, name, printpoint)
	'''---------------------------'''
	
def mode380(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode380(admin, name, printpoint)
	'''---------------------------'''

def mode381(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode381(admin, name, printpoint)
	'''---------------------------'''

def mode382(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode382(admin, name, printpoint)
	'''---------------------------'''

def mode383(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode383(admin, name, printpoint)
	'''---------------------------'''

def mode384(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode384(admin, name, printpoint)
	'''---------------------------'''

def mode385(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode385(admin, name, printpoint)
	'''---------------------------'''

def mode386(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode386(admin, name, printpoint)
	'''---------------------------'''

def mode387(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode387(admin, name, printpoint)
	'''---------------------------'''

def mode388(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode388(admin, name, printpoint)
	'''---------------------------'''

def mode389(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode389(admin, name, printpoint)
	'''---------------------------'''
	
def mode390(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode390(admin, name, printpoint)
	'''---------------------------'''

def mode391(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode391(admin, name, printpoint)
	'''---------------------------'''

def mode392(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode392(admin, name, printpoint)
	'''---------------------------'''

def mode393(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode393(admin, name, printpoint)
	'''---------------------------'''

def mode394(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode394(admin, name, printpoint)
	'''---------------------------'''

def mode395(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode395(admin, name, printpoint)
	'''---------------------------'''

def mode396(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode396(admin, name, printpoint)
	'''---------------------------'''

def mode397(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode397(admin, name, printpoint)
	'''---------------------------'''

def mode398(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode398(admin, name, printpoint)
	'''---------------------------'''

def mode399(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode399(admin, name, printpoint)
	'''---------------------------'''

def mode400(admin, name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode400(admin, name, printpoint)
	'''---------------------------'''

def mode401(admin,name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode401(admin, name, printpoint)
	'''---------------------------'''

def mode402(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode402(admin, name, printpoint)
	'''---------------------------'''
	
def mode403(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode403(admin, name, printpoint)
	'''---------------------------'''

def mode404(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode404(admin, name, printpoint)
	'''---------------------------'''

def mode405(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode405(admin, name, printpoint)
	'''---------------------------'''

def mode406(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode406(admin, name, printpoint)
	'''---------------------------'''

def mode407(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode407(admin, name, printpoint)
	'''---------------------------'''

def mode408(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode408(admin, name, printpoint)
	'''---------------------------'''

def mode409(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode409(admin, name, printpoint)
	'''---------------------------'''

def mode410(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode440(admin, name, printpoint)
	'''---------------------------'''
	
def mode411(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode411(admin, name, printpoint)
	'''---------------------------'''

def mode412(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode412(admin, name, printpoint)
	'''---------------------------'''

def mode413(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode413(admin, name, printpoint)
	'''---------------------------'''

def mode414(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode414(admin, name, printpoint)
	'''---------------------------'''

def mode415(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode415(admin, name, printpoint)
	'''---------------------------'''

def mode416(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode416(admin, name, printpoint)
	'''---------------------------'''

def mode417(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode417(admin, name, printpoint)
	'''---------------------------'''

def mode418(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode418(admin, name, printpoint)
	'''---------------------------'''

def mode419(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode419(admin, name, printpoint)
	'''---------------------------'''

def mode420(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode420(admin, name, printpoint)
	'''---------------------------'''
	
def mode421(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode421(admin, name, printpoint)
	'''---------------------------'''

def mode422(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode422(admin, name, printpoint)
	'''---------------------------'''

def mode423(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode423(admin, name, printpoint)
	'''---------------------------'''

def mode424(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode424(admin, name, printpoint)
	'''---------------------------'''

def mode425(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode425(admin, name, printpoint)
	'''---------------------------'''

def mode426(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode426(admin, name, printpoint)
	'''---------------------------'''

def mode427(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode427(admin, name, printpoint)
	'''---------------------------'''

def mode428(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode428(admin, name, printpoint)
	'''---------------------------'''

def mode429(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode429(admin, name, printpoint)
	'''---------------------------'''

def mode430(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode430(admin, name, printpoint)
	'''---------------------------'''
	
def mode431(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode431(admin, name, printpoint)
	'''---------------------------'''

def mode432(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode432(admin, name, printpoint)
	'''---------------------------'''

def mode433(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode433(admin, name, printpoint)
	'''---------------------------'''

def mode434(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode434(admin, name, printpoint)
	'''---------------------------'''

def mode435(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode435(admin, name, printpoint)
	'''---------------------------'''

def mode436(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode436(admin, name, printpoint)
	'''---------------------------'''

def mode437(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode437(admin, name, printpoint)
	'''---------------------------'''

def mode438(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode438(admin, name, printpoint)
	'''---------------------------'''

def mode439(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode439(admin, name, printpoint)
	'''---------------------------'''

def mode440(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode440(admin, name, printpoint)
	'''---------------------------'''
	
def mode441(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode441(admin, name, printpoint)
	'''---------------------------'''

def mode442(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode442(admin, name, printpoint)
	'''---------------------------'''

def mode443(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode443(admin, name, printpoint)
	'''---------------------------'''

def mode444(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode444(admin, name, printpoint)
	'''---------------------------'''

def mode445(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode445(admin, name, printpoint)
	'''---------------------------'''

def mode446(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode446(admin, name, printpoint)
	'''---------------------------'''

def mode447(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode447(admin, name, printpoint)
	'''---------------------------'''

def mode448(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode448(admin, name, printpoint)
	'''---------------------------'''

def mode449(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode449(admin, name, printpoint)
	'''---------------------------'''

def mode450(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode450(admin, name, printpoint)
	'''---------------------------'''

def mode451(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode451(admin, name, printpoint)
	'''---------------------------'''

def mode452(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode452(admin, name, printpoint)
	'''---------------------------'''

def mode453(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode453(admin, name, printpoint)
	'''---------------------------'''

def mode454(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode454(admin, name, printpoint)
	'''---------------------------'''

def mode455(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode455(admin, name, printpoint)
	'''---------------------------'''

def mode456(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode456(admin, name, printpoint)
	'''---------------------------'''

def mode457(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode457(admin, name, printpoint)
	'''---------------------------'''

def mode458(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode458(admin, name, printpoint)
	'''---------------------------'''

def mode459(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode459(admin, name, printpoint)
	'''---------------------------'''

def mode460(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode460(admin, name, printpoint)
	'''---------------------------'''

def mode461(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode461(admin, name, printpoint)
	'''---------------------------'''

def mode462(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode462(admin, name, printpoint)
	'''---------------------------'''

def mode463(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode463(admin, name, printpoint)
	'''---------------------------'''

def mode464(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode464(admin, name, printpoint)
	'''---------------------------'''

def mode465(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode465(admin, name, printpoint)
	'''---------------------------'''

def mode466(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode466(admin, name, printpoint)
	'''---------------------------'''

def mode467(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode467(admin, name, printpoint)
	'''---------------------------'''

def mode468(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode468(admin, name, printpoint)
	'''---------------------------'''

def mode469(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode469(admin, name, printpoint)
	'''---------------------------'''

def mode470(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode470(admin, name, printpoint)
	'''---------------------------'''

def mode471(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode471(admin, name, printpoint)
	'''---------------------------'''

def mode472(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode472(admin, name, printpoint)
	'''---------------------------'''

def mode473(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode473(admin, name, printpoint)
	'''---------------------------'''

def mode474(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode474(admin, name, printpoint)
	'''---------------------------'''

def mode475(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode475(admin, name, printpoint)
	'''---------------------------'''

def mode476(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode476(admin, name, printpoint)
	'''---------------------------'''

def mode477(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode477(admin, name, printpoint)
	'''---------------------------'''

def mode478(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode478(admin, name, printpoint)
	'''---------------------------'''

def mode479(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode479(admin, name, printpoint)
	'''---------------------------'''
	
def mode480(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode480(admin, name, printpoint)
	'''---------------------------'''

def mode481(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode481(admin, name, printpoint)
	'''---------------------------'''

def mode482(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode482(admin, name, printpoint)
	'''---------------------------'''

def mode483(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode483(admin, name, printpoint)
	'''---------------------------'''

def mode484(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode484(admin, name, printpoint)
	'''---------------------------'''

def mode485(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode485(admin, name, printpoint)
	'''---------------------------'''

def mode486(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode486(admin, name, printpoint)
	'''---------------------------'''

def mode487(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode487(admin, name, printpoint)
	'''---------------------------'''

def mode488(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode488(admin, name, printpoint)
	'''---------------------------'''

def mode489(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode489(admin, name, printpoint)
	'''---------------------------'''
	
def mode490(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode490(admin, name, printpoint)
	'''---------------------------'''

def mode491(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode491(admin, name, printpoint)
	'''---------------------------'''

def mode492(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode492(admin, name, printpoint)
	'''---------------------------'''

def mode493(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode493(admin, name, printpoint)
	'''---------------------------'''

def mode494(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode494(admin, name, printpoint)
	'''---------------------------'''

def mode495(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode495(admin, name, printpoint)
	'''---------------------------'''

def mode496(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode496(admin, name, printpoint)
	'''---------------------------'''

def mode497(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode497(admin, name, printpoint)
	'''---------------------------'''

def mode498(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode498(admin, name, printpoint)
	'''---------------------------'''

def mode499(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode500(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode501(admin,name, printpoint):
	'''------------------------------
	---MOVIES-BUTTON-----------------
	------------------------------'''
	libraryhascontentmovies = xbmc.getCondVisibility('Library.HasContent(Movies)')
	if libraryhascontentmovies:
		if admin: xbmc.executebuiltin('Notification(Admin,moviesbutton,1000)')
		xbmc.executebuiltin('ActivateWindow(Videos,MovieTitles,return)')
		if not autoview:
			xbmc.sleep(2000)
			if xbmc.getCondVisibility('System.IdleTime(2)'): notification(localize(98) + space + localize(1223), localize(79534), "", 4000)
	else:
		if not autoviewoff: setSkinSetting("1",'AutoViewoff',"true")
		#xbmc.executebuiltin('ActivateWindow(video,"special://userdata/library/movies/",return)')
		url = "special://userdata/library/movies/"
		returned = ActivateWindow("1", url, url, 0, wait=True)
		if returned != "":
			try:
				containernumitems = xbmc.getInfoLabel('Container.NumItems')
				if int(containernumitems) < 3: xbmc.executebuiltin('Notification($LOCALIZE[79079] $LOCALIZE[342] $LOCALIZE[79090],$LOCALIZE[79091],4000)')
				'''---------------------------'''
			except: pass
		if scripthtptsmartbuttonsLibraryData_LocalMoviesFiles == "0": xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=55)')
		else:
			if libraryisscanningvideo and not libraryhascontentmovies: xbmc.sleep(4000) ; xbmc.executebuiltin('UpdateLibrary(video)')
			else:
				setsetting_custom1('service.htpt.fix','Fix_100',"true")
				if scripthtptinstall_Skin_FirstBoot == "true": dialogok("Reboot Required!", "Please reboot in order to finish the first installation", "", "")
				else: xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=3)')
				xbmc.executebuiltin('ActivateWindow(0)')
				'''---------------------------'''
	
	setSkinSetting("1",'AutoViewoff',"false")
	'''---------------------------'''

def mode502(admin, name, printpoint):
	'''------------------------------
	---TVSHOWS-BUTTON----------------
	------------------------------'''
	libraryhascontenttvshows = xbmc.getCondVisibility('Library.HasContent(TVShows)')
	if libraryhascontenttvshows:
		if admin: xbmc.executebuiltin('Notification(Admin,tvshowsbutton,1000)')
		xbmc.executebuiltin('ActivateWindow(VideoLibrary,TVShowTitles,return)')
		if not autoview:
			xbmc.sleep(2000)
			if xbmc.getCondVisibility('System.IdleTime(2)'): notification(localize(98) + space + localize(1223), localize(79534), "", 4000)
	else:
		if not autoviewoff: setSkinSetting("1",'AutoViewoff',"true")
		#xbmc.executebuiltin('ActivateWindow(video,"special://userdata/library/tvshows/",return)')
		url = "special://userdata/library/tvshows/"
		returned = ActivateWindow("1", url, url, 0, wait=True)
		if returned != "":
			try:
				containernumitems = xbmc.getInfoLabel('Container.NumItems')
				if int(containernumitems) < 3: xbmc.executebuiltin('Notification($LOCALIZE[79079] $LOCALIZE[20343] $LOCALIZE[79090],$LOCALIZE[79091],4000)')
			except: pass
			'''---------------------------'''
		if scripthtptsmartbuttonsLibraryData_LocalTvshowsFiles == "0": xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=55)')
		else:
			if libraryisscanningvideo: xbmc.sleep(4000) ; xbmc.executebuiltin('UpdateLibrary(video)')
			else:
				setsetting_custom1('service.htpt.fix','Fix_101',"true")
				if scripthtptinstall_Skin_FirstBoot == "true": dialogok("Reboot Required!", "Please reboot in order to finish the first installation", "", "")
				else: xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=3)')
				xbmc.executebuiltin('ActivateWindow(0)')
				'''---------------------------'''
	setSkinSetting("1",'AutoViewoff',"false")
	'''---------------------------'''
	
def mode503(admin, name, printpoint):
	'''------------------------------
	---ISRAEL-TV-BUTTON--------------
	------------------------------'''
	addon = 'plugin.video.sdarot.tv'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		printpoint = printpoint + "1"
		if admin and not admin2:
			path = os.path.join(addondata_path, 'plugin.video.sdarot.tv', 'sdarot-cookiejar.txt')
			removefiles(path)
			notification("DELETING COOKIE","","",1000)
			xbmc.sleep(1000)
			'''---------------------------'''
		else:
			addonsettings2('plugin.video.sdarot.tv','DEBUG',"false",'cache',"24",'domain',"http://www.sdarot.wf",'',"",'',"")
			'''---------------------------'''
			
		url = 'plugin://plugin.video.sdarot.tv/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99&name=%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99&url=all-heb'
		returned = ActivateWindow("1", 'plugin.video.sdarot.tv', url, 'return0', wait=True)
		if returned == "": returned = ActivateWindow("0", 'plugin.video.sdarot.tv', url, 'return0', wait=True) ; printpoint = printpoint + "3"
		if returned == "":
			from shared_modules3 import urlcheck
			printpoint = printpoint + "4"
			returned = urlcheck('http://www.sdarot.wf', ping=False)
			if returned == "ok":
				printpoint = printpoint + "6"
			else:
				'''------------------------------
				---WEBSITE-DOWN------------------
				------------------------------'''
				notification('[COLOR=Red]' + localize(75787) + '[/COLOR]', localize(75788),"",4000)
				xbmc.executebuiltin('Action(Close)')
				'''---------------------------'''
	else: installaddon(admin, addon, "")
	'''---------------------------'''

def mode504(admin, name, printpoint):
	'''------------------------------
	---YOUTUBE-BUTTON----------------
	------------------------------'''
	addon = 'plugin.video.youtube'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		xbmc.executebuiltin('RunAddon(plugin.video.youtube)')
	else: installaddon(admin, addon, "")
	'''---------------------------'''

def mode505(admin, name, printpoint):
	'''------------------------------
	---GOPRO-BUTTON------------------
	------------------------------'''
	addon = 'plugin.video.htpt.gopro'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		returned = ActivateWindow("0", addon , 'plugin://'+addon+'/' , 0, wait=True)
		if returned == 'ok2' and 1 + 1 == 3:
			systemcurrentcontrol = findin_systemcurrentcontrol("0",str73440.encode('utf-8'),40,'Action(Down)','Action(Select)')
			count = 0
			systemidle0 = xbmc.getCondVisibility('System.IdleTime(0)')
			while count < 10 and systemcurrentcontrol != str73440.encode('utf-8') and systemidle0 and not xbmc.abortRequested:
				count += 1
				systemcurrentcontrol = findin_systemcurrentcontrol("0",str73440.encode('utf-8'),40,'Action(Down)','Action(Select)')
				systemidle0 = xbmc.getCondVisibility('System.IdleTime(0)')
				xbmc.sleep(200)
			if count < 10 and systemidle0: notification_common("14")
	else: installaddon(admin, addon, "")
		
				
		#returned = ActivateWindow("1", 'plugin.video.htpt.gopro' , 'plugin://plugin.video.htpt.gopro/?iconimage=https%3a%2f%2fyt3.ggpht.com%2f-sp0YiR_yyR0%2fAAAAAAAAAAI%2fAAAAAAAAAAA%2fkXU4u1ny2T4%2fs100-c-k-no%2fphoto.jpg&mode=9&name=GoPro&num=1&url=GoProCamera' , "", wait=True)
		#returned = ActivateWindow('plugin.video.htpt.gopro', 'plugin://plugin.video.htpt.gopro/?iconimage=https%3a%2f%2fyt3.ggpht.com%2f-sp0YiR_yyR0%2fAAAAAAAAAAI%2fAAAAAAAAAAA%2fkXU4u1ny2T4%2fs100-c-k-no%2fphoto.jpg&mode=9&name=GoPro&num=1&url=GoProCamera', "", wait=True)
		#returned = ActivateWindow("1", 'plugin.video.htpt.gopro' , 'plugin://plugin.video.htpt.gopro/?iconimage=https%3a%2f%2fyt3.ggpht.com%2f-sp0YiR_yyR0%2fAAAAAAAAAAI%2fAAAAAAAAAAA%2fkXU4u1ny2T4%2fs100-c-k-no%2fphoto.jpg&mode=9&name=GoPro&num=1&url=GoProCamera' , 0, wait=True)
		
		#returned = ActivateWindow("1", 'plugin.video.htpt.gopro', 'plugin://plugin.video.htpt.gopro/?iconimage=https%3a%2f%2fyt3.ggpht.com%2f-sp0YiR_yyR0%2fAAAAAAAAAAI%2fAAAAAAAAAAA%2fkXU4u1ny2T4%2fs100-c-k-no%2fphoto.jpg&mode=9&name=GoPro&num=1&url=GoProCamera', "", wait=True)
		#xbmc.sleep(5000)
		#xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.htpt.gopro/?iconimage=https%3a%2f%2fyt3.ggpht.com%2f-sp0YiR_yyR0%2fAAAAAAAAAAI%2fAAAAAAAAAAA%2fkXU4u1ny2T4%2fs100-c-k-no%2fphoto.jpg&mode=9&name=GoPro&num=1&url=GoProCamera,return)')
		#
	'''---------------------------'''

def mode506(value, admin, name, printpoint):
	'''------------------------------
	---MOVIESE-BUTTON----------------
	------------------------------'''
	if value == "101" or not moviesep:
		printpoint = printpoint + "5"
		url = 'plugin://plugin.video.genesis/?action=movieNavigator'
		returned = ActivateWindow("1", 'plugin.video.genesis', url, 0, wait=True)
		printpoint = printpoint + moviese_tvshowse(admin, name, printpoint, returned)
		'''---------------------------'''
	elif value == "102":
		'''------------------------------
		---PULSAR------------------------
		------------------------------'''
		addon = 'plugin.video.pulsar'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.pulsar/movies/,return)')
		else:
			installaddon(admin, addon, "") ; xbmc.sleep(500)
			if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				url = 'https://github.com/steeve/plugin.video.pulsar/releases/download/v0.6.1/plugin.video.pulsar-0.6.1.zip'
				DownloadFile(url, addon+".zip", packages_path, addons_path, silent=False) ; xbmc.executebuiltin("UpdateLocalAddons")
	
	elif value == "104":
		'''------------------------------
		---3D-MOVIES---------------------
		------------------------------'''
		notification_common("10")	
				
	else: printpoint = printpoint + "9"		
	'''---------------------------'''
	return printpoint
	
def mode507(value, admin, name, printpoint):
	'''------------------------------
	---TVSHOWSE-BUTTON---------------
	------------------------------'''
	if value == "101" or not tvshowsep:
		printpoint = printpoint + "5"
		url = 'plugin://plugin.video.genesis/?action=tvNavigator'
		returned = ActivateWindow("1", 'plugin.video.genesis', url, 0, wait=True)
		printpoint = printpoint + moviese_tvshowse(admin, name, printpoint, returned)
		'''---------------------------'''
	elif value == "102":
		'''------------------------------
		---PULSAR------------------------
		------------------------------'''
		addon = 'plugin.video.pulsar'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.pulsar/shows/,return)')
		else:
			installaddon(admin, addon, "") ; xbmc.sleep(500)
			if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				url = 'https://github.com/steeve/plugin.video.pulsar/releases/download/v0.6.1/plugin.video.pulsar-0.6.1.zip'
				DownloadFile(url, addon+".zip", packages_path, addons_path, silent=False) ; xbmc.executebuiltin("UpdateLocalAddons")
	else: printpoint = printpoint + "9"
	'''---------------------------'''
	return printpoint
	
def moviese_tvshowse(admin, name, printpoint, returned):
	
	addon = 'plugin.video.genesis'
	if returned == "" and xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		'''------------------------------
		---GENESIS-PATH-CHANGE-----------
		------------------------------'''
		printpoint = printpoint + "A"
		xbmc.sleep(500)
		returned = ActivateWindow("0", 'plugin.video.genesis', '', 0, wait=True)
		if returned != "":
			printpoint = printpoint + "B"
			containerfolderpath = xbmc.getCondVisibility('StringCompare(Container.FolderPath,plugin://plugin.video.genesis/)')
			if not containerfolderpath:
				xbmc.executebuiltin('Action(PageUp)')
				xbmc.executebuiltin('Action(PageUp)')
				xbmc.executebuiltin('Action(Select)')
				xbmc.sleep(800)
				containerfolderpath = xbmc.getCondVisibility('StringCompare(Container.FolderPath,plugin://plugin.video.genesis/)')
				#xbmc.sleep(1000)
			if containerfolderpath:
				xbmc.executebuiltin('Action(PageUp)')
				xbmc.executebuiltin('Action(Down)')
				if name == 'TVSHOWSE-BUTTON': xbmc.executebuiltin('Action(Down)')
				xbmc.executebuiltin('Action(Select)')
						
	if returned != "":
		'''------------------------------
		---GENESIS-OK!-------------------
		------------------------------'''
		count = 0
		containernumitems = xbmc.getInfoLabel('Container.NumItems')
		
		while count < 40 and (containernumitems == "0" or containernumitems == "") and not xbmc.abortRequested:
			xbmc.sleep(40)
			containernumitems = xbmc.getInfoLabel('Container.NumItems')
			count += 1
		#if admin: notification("testtttt-",containernumitems,"",3000)
		rootmovies = 'plugin://plugin.video.genesis/?action=movieNavigator'
		roottv = 'plugin://plugin.video.genesis/?action=tvNavigator'
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		if containerfolderpath == rootmovies or containerfolderpath == roottv:
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			if containerfolderpath == rootmovies:
				value2 = localize(342)
				xbmc.executebuiltin('Action(PageUp)')
				xbmc.executebuiltin('Action(PageUp)')
				if moviesestartup == "0": value = "" #root
				elif moviesestartup == "1": value = addonString_genesis(30027).encode('utf-8') #Most Popular
				elif moviesestartup == "2": value = addonString_genesis(30806).encode('utf-8') #Latest HD Movies
				elif moviesestartup == "3": value = addonString_genesis(30009).encode('utf-8') #Search
				elif moviesestartup == "4": value = addonString_genesis(30021).encode('utf-8') #Genres
				else: value = ""
				if value != "": value = "[" + value + "]"
				#if admin: notification("value: " + value,"","",1000)
				'''---------------------------'''
				count = 0
				while count < 17 and containerfolderpath == rootmovies and value != "" and not xbmc.abortRequested:
					if not xbmc.Player().isPlayingVideo():
						if moviesestartup == "3": systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Up)','')
						elif moviesestartup == "2": systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Up)','Action(Select)')
						else: systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Down)','Action(Select)')
					else:
						if moviesestartup == "3": systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Down)','')
						else: systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Down)','Action(Select)')
					
					if systemcurrentcontrol == value: count = 40
					containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
					count += 1
					'''---------------------------'''
				
			elif containerfolderpath == roottv:
				value2 = str20343 #str20343.decode('utf-8').encode('utf-8')
				xbmc.executebuiltin('Action(PageUp)')
				xbmc.executebuiltin('Action(PageUp)')
				if tvshowsestartup == "0": value = "" #root
				elif tvshowsestartup == "1": value = addonString_genesis(30027).encode('utf-8') #Most Popular
				elif tvshowsestartup == "2": value = addonString_genesis(30544).encode('utf-8') #Returning TV Shows
				elif tvshowsestartup == "3": value = addonString_genesis(30009).encode('utf-8') #Search
				elif tvshowsestartup == "4": value = addonString_genesis(30021).encode('utf-8') #Genres
				else: value = ""
				if value != "": value = "[" + value + "]"
				'''---------------------------'''
				count = 0
				while count < 17 and containerfolderpath == roottv and value != "" and not xbmc.abortRequested:
					if tvshowsestartup == "3" and not xbmc.Player().isPlayingVideo(): systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Up)','')
					elif tvshowsestartup == "3": systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Down)','')
					else: systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Down)','Action(Select)')
					
					if systemcurrentcontrol == value: count = 40
					containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
					count += 1
					'''---------------------------'''
			
			if value != "":
				'''------------------------------
				---STARTUP-WINDOW-NOTIFICATION---
				------------------------------'''
				xbmc.sleep(3000)
				containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
				if containerfolderpath == rootmovies or containerfolderpath == roottv:
					if moviesestartup != "3" and tvshowsestartup != "3": notification('[COLOR=Yellow]' + value + '[/COLOR]' + localize(512) + space2, localize(75782), "", 4000)
				elif moviesestartup == "3" or tvshowsestartup == "3": notification('[COLOR=Yellow]' + value + '[/COLOR]' + localize(512) + space2, localize(75782), "", 4000)
		elif admin: notification("containerfolderpath_Error","","",1000)
	
	return printpoint
	
def mode508(admin, name, printpoint):
	'''------------------------------
	---WEATHER-BUTTON----------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode509(admin, name, printpoint):
	'''------------------------------
	---PICTURES-BUTTON---------------
	------------------------------'''
	name2 = str1
	path2 = "pictures"
	pictures_videos(admin, name, printpoint, 509, name2, path2)
	'''---------------------------'''

def pictures_videos(admin, name, printpoint, mode, name2, path2):
	'''------------------------------
	---PICTURE-&-VIDEO-BUTTON--------
	------------------------------'''
	containernumitems = "" ; path = "" ; device = ""
		
	returned = supportcheck(name2, ["A", "B", "A?", "B?"], totalspace=100, Intel=False, silence=True)
	if returned == "ok": device = "0"
	elif scripthtptinstall_Skin_Installed == "true" or scripthtptinstall_Skin_FirstBoot == "true": printpoint = printpoint + "8"
	else: device = "1"

	
	if device == "0": path = "special://userdata/library/" + path2 + "/"
	else:
		externalusb(device, mode)
		usb1str = xbmc.getInfoLabel('Skin.String(USB1)')
		if usb1str == "" and not systemplatformwindows: printpoint = printpoint + "9"
		'''---------------------------'''
		if usb1str != "": path = varmedia_path + usb1str + '/' + path2
		elif systemplatformwindows: path = 'special://home/external/' + path2
		'''---------------------------'''
	if printpoint == "":
		if not os.path.exists(library_path + path2):
			os.mkdir(library_path + path2) ; xbmc.sleep(500)
			notification("Folder Created:", library_path + path2, "", 2000)
		xbmc.executebuiltin('ActivateWindow('+ path2 +','+ path +',return)')
		#xbmc.executebuiltin('ActivateWindow(Pictures,/var/media/'+ usb1str +',return)')
		#xbmc.executebuiltin('ActivateWindow(Pictures,special://userdata/library/pictures/,return)')
		if not admin and not playerhasmedia:
			if os.path.exists(skin_music_path + "playHTPT.mp3"): xbmc.executebuiltin('PlayMedia('+skin_music_path+'playHTPT.mp3)')
			
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		count = 0
		while count < 10 and containerfolderpath != path and not xbmc.abortRequested:
			'''------------------------------
			---containerfolderpath-----------
			------------------------------'''
			xbmc.sleep(100)
			count += 1
			containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
			xbmc.sleep(100)
			'''---------------------------'''
		containernumitems = xbmc.getInfoLabel('Container.NumItems')
		try: containernumitemsN = int(containernumitems)
		except: containernumitemsN = 0
		if device == "0": externalusb(device, mode)
			
		if containernumitemsN < 2:
			containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
			count = 0
			while count < 10 and containerfolderpath == path and not xbmc.abortRequested:
				'''------------------------------
				---containerfolderpath-----------
				------------------------------'''
				xbmc.sleep(500)
				count += 1
				containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
				if count == 1: notification(addonString(120) % (name2), localize(75786), "", 1000)
				elif count == 2: notification(addonString(120) % (name2), localize(75786) + ".", "", 1000)
				elif count == 3: notification(addonString(120) % (name2), localize(75786) + "..", "", 1000)
				elif count == 4: notification(addonString(120) % (name2), localize(75786) + "...", "", 1000)
				if count == 5:
					HelpButton_Video_Pic(name2, path2)
					
					
				xbmc.sleep(500)
				'''---------------------------'''
	if printpoint != "":
		if "9" in printpoint: dialogok('[COLOR=Yellow]' + localize(75798) + '[/COLOR]', addonString(124).encode('utf-8') % (id10str) + '[CR]' + localize(74541), localize(75799), localize(74542))
		elif "8" in printpoint: dialogok("Reboot Required!", "Please reboot in order to finish the first installation", "", "")
	if admin: print printfirst + "picturesbutton/videosbutton_LV" + printpoint + space2 + "containernumitems" + space2 + containernumitems + "id10str" + space2 + id10str

def externalusb(device, mode):
	'''detect connected USB'''
	name = 'externalusb' ; printpoint = ""
	setSkinSetting("1",'AutoViewoff',"true")
	videosbutton = xbmc.getCondVisibility('Container(9000).HasFocus(325)')
	picturesbutton = xbmc.getCondVisibility('Container(9000).HasFocus(507)')
	if device == "":
		printpoint = printpoint + "1"
		returned = supportcheck(name, ["A", "B", "A?", "B?"], totalspace=100, Intel=False, silence=True)
		if returned == 'ok': device = "0"
		else: device = "1"
		
	if not systemplatformwindows and myhtpt2:
		printpoint = printpoint + "2"
		if mode == 509 or mode == 510 or mode == 100:
			path = os.path.join(addonPath, 'specials', 'scripts', 'externalusb.sh')
			os.system('sh '+path+'')
			printpoint = printpoint + "3"
			#xbmc.sleep(500)
		if os.path.exists('/storage/externalusb.log'):
			log = open('/storage/externalusb.log', 'r')
			rows = log.readlines()
			rowscountN = len(rows)
			rowscount = str(rowscountN)
			log.close()
			row1 = ""
			row2 = ""
			row3 = ""
			row4 = ""
			row5 = ""
			if rowscountN > 0: row1 = rows[0][:-1]
			if rowscountN > 1: row2 = rows[1][:-1]
			if rowscountN > 2: row3 = rows[2][:-1]
			if rowscountN > 3: row4 = rows[3][:-1]
			if rowscountN > 4: row5 = rows[4][:-1]
			if mode == 509 or mode == 510 or mode == 100:
				printpoint = printpoint + "4"
				if usb1str != row1: xbmc.executebuiltin('Skin.SetString(USB1,'+ row1 +')')
				if usb2str != row2: xbmc.executebuiltin('Skin.SetString(USB2,'+ row2 +')')
				if usb3str != row3: xbmc.executebuiltin('Skin.SetString(USB3,'+ row3 +')')
				if usb4str != row4: xbmc.executebuiltin('Skin.SetString(USB4,'+ row4 +')')
				if usb5str != row5: xbmc.executebuiltin('Skin.SetString(USB5,'+ row5 +')')
				'''---------------------------'''
			if admin and rowscountN > 0: xbmc.executebuiltin('Notification(Admin,'+ rowscount +' '+ row1 +' ,1000)')
			path0 = 'special://userdata/library/'
			path1 = os.path.join(varmedia_path, row1)
			path2 = os.path.join(varmedia_path, row2)
			path3 = os.path.join(varmedia_path, row3)
			path4 = os.path.join(varmedia_path, row4)
			path5 = os.path.join(varmedia_path, row5)
			pathwin = 'special://home/external/'
			if rowscountN == 0 and myhtpt3: xbmc.executebuiltin('Skin.ToggleSetting(myHTPT3)')
			if rowscountN > 0 and not myhtpt3: xbmc.executebuiltin('Skin.ToggleSetting(myHTPT3)')
			'''---------------------------'''
			#myvideonavW = xbmc.getCondVisibility('Window.IsVisible(MyVideoNav.xml)')
			#mypicsW = xbmc.getCondVisibility('Window.IsVisible(MyPics.xml)')
			containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
			
			if (myvideonavW or mypicsW) and mode == 304:
				printpoint = printpoint + "5"
				#xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,)')
				#xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,)')
				if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path0 +')') and rowscountN > 0:
					if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,1)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path1 +')')
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path1 +')') and rowscountN > 1:
					if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path2 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path2 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,2)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path2 +')')
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path2 +')') and rowscountN > 2:
					if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path3 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path3 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,3)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path3 +')')
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path3 +')') and rowscountN > 3:
					if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path4 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path4 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,4)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path4 +')')
					'''---------------------------'''
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path4 +')') and rowscountN > 4:
					if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path5 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path5 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,5)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path5 +')')
					'''---------------------------'''
					
				else:
					#if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path1 +')') and rowscountN == 1 and 1 + 1 == 3:
					printpoint = printpoint + "A"
					if device == "1":
						notification('$LOCALIZE[74546]', '$LOCALIZE[74547]', '', 2000)
						if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
						'''---------------------------'''
					elif myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
					elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
				if 1 + 1 == 3:
					if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path2 +')') and rowscountN == 2:
						if device == "1":
							if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
					elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path3 +')') and rowscountN == 3:
						if device == "1":
							if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
					elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path4 +')') and rowscountN == 4:
						if device == "1":
							if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
					elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path5 +')') and rowscountN == 5:
						if device == "1":
							if myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif myvideonavW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
						'''---------------------------'''
				xbmc.sleep(20)
				containernumitems = xbmc.getInfoLabel('Container.NumItems')
				if containernumitems == 0: xbmc.executebuiltin('Action(Select)')
			elif device == "1":
				printpoint = printpoint + "8" ; extra = ""
				if videosbutton: extra = '/videos/'
				elif picturesbutton: extra = '/pictures/'
				
				if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path0 +')') and rowscountN > 0:
					setSkinSetting("0",'VarCurrentPicVid', "1")
					setSkinSetting("0",'VarCurrentPicVidPath', path1 + extra)
				else:
					setSkinSetting("0",'VarCurrentPicVid', "")
					setSkinSetting("0",'VarCurrentPicVidPath', "")
			
			if admin: print printfirst + name + "_LV" + printpoint + space + "mypicsW" + space2 + str(mypicsW) + space + "myvideonavW" + space2 + str(myvideonavW) + space + "containerfolderpath" + space2 + str(containerfolderpath) + space + "device" + space2 + str(device) + newline + "path1" + space2 + path1 + space + "rowscountN" + space2 + str(rowscountN) + newline + space
	setSkinSetting("1",'AutoViewoff',"false")
	
def HelpButton_Video_Pic(name, path2):
	returned = supportcheck(name, ["A", "B", "A?", "B?"], totalspace=100, Intel=False, silence=True)
	if returned == 'ok': device = "0"
	else: device = "1"
	containernumitems = xbmc.getInfoLabel('Container.NumItems')
	try: containernumitemsN = int(containernumitems)
	except: containernumitemsN = 0
	
	if containernumitemsN < 2: dialogok('[COLOR=Yellow]' + addonString(120) % (name) + '[/COLOR]', addonString(123) % (name),localize(75797),"") #You didn't added %s to library yet
	usb1str = xbmc.getInfoLabel('Skin.String(USB1)')
	
	'''---------------------------'''
	if name != str2:
		if device == "0": dialogok(addonString(124) % (id10str) + '[CR]' + scripthtptdebug_Info_Model, addonString(125) % (scripthtptdebug_Info_TotalSpace),addonString(126) % (name),"", line1c="Yellow")
		elif device == "1": dialogok(addonString(124) % (id10str) + '[CR]' + scripthtptdebug_Info_Model, localize(74541),addonString(155) % (usb1str),"", line1c="Yellow")
		'''---------------------------'''
	if systemplatformwindows:
		returned = dialogyesno(addonString(134) % (name),addonString(135) % (name, localize(74558).decode('utf-8')))
		if returned == "ok":
			header = space + "(" + localize(74558).decode('utf-8') + ")" + space + '[COLOR=Yellow]' + addonString(129) % (name) + '[/COLOR]'+ space
			extra = newline + "Your library path: " + pictures_path + newline
			if name == str1 or name == str3: message2 = addonString(132) % (name, path2, name) + extra + localize(74542).decode('utf-8')
			elif name == str2: message2 = addonString(172) % (name) + extra + localize(74542).decode('utf-8')
			w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
			w.doModal()
			'''---------------------------'''
			
	elif device == "0":
		returned = dialogyesno(addonString(134) % (name),addonString(135) % (name, localize(74558).decode('utf-8')))
		if returned == "ok":
			header = space + "(" + localize(74558).decode('utf-8') + ")" + space + '[COLOR=Yellow]' + addonString(129) % (name) + '[/COLOR]'+ space
			if name == str1 or name == str3: message2 = addonString(132) % (name, path2, name) + localize(74542).decode('utf-8')
			elif name == str2: message2 = addonString(172) % (name) + localize(74542).decode('utf-8')
			w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
			w.doModal()
			
			header = space + "(" + localize(74558).decode('utf-8') + ")" + space + '[COLOR=Yellow]' + addonString(136) % (name) + '[/COLOR]' + space
			if name == str1 or name == str3: message2 = addonString(137) % ("\\\\" + "htpt", path2, name, name) +localize(74542).decode('utf-8')
			elif name == str2: message2 = addonString(173) % ("\\\\" + "htpt", path2, name, name, name) + localize(74542).decode('utf-8')
			w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
			w.doModal()
			'''---------------------------'''
	
	elif device == "1":
		returned = dialogyesno(addonString(134) % (name),addonString(135) % (name, localize(74559).decode('utf-8')))
		if returned == "ok":
			header = space + "(" + localize(74559).decode('utf-8') + ")" + space + '[COLOR=Yellow]' + addonString(129) % (name) + '[/COLOR]' + space
			message2 = addonString(155) % (usb1str) + '[CR]' + addonString(156) % (path2) + '[CR]' + addonString(157) % (path2, name) + localize(74542).decode('utf-8')
			w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
			w.doModal()
			
			header = space + "(" + localize(74559).decode('utf-8') + ")" + space + '[COLOR=Yellow]' + addonString(136) % (name) + '[/COLOR]' + space
			message2 = addonString(137) % ("\\\\" + "htpt", str79498 + " -> " + usb1str + " -> " + path2 , name, name) + localize(74542).decode('utf-8')
			w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
			w.doModal()
			'''---------------------------'''
				
def mode510(admin, name, printpoint):
	'''------------------------------
	---GAMES-BUTTON------------------
	------------------------------'''
	name2 = localize(15016)

	returned = supportcheck(name2, ["A","A?","B","B?"], 200, platform="13456")
	if returned == "ok":
		addon = 'plugin.program.advanced.launcher'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			printpoint = printpoint + "7"
			'''---------------------------'''
		else:
			installaddon(admin, addon, "")
			'''---------------------------'''
		
		addon = 'script.htpt.emu'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			printpoint = printpoint + "7"
			'''---------------------------'''
		else:
			installaddon(admin, addon, "")
			'''---------------------------'''
		
		if "77" in printpoint:
			if not os.path.exists(os.path.join(addons_path,'emulator.retroarch')) and not admin3:
				file = "emu_htpt.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/emu_htpt.zip?dl=1", file, temp_path, addons_path)
				if os.path.exists(os.path.join(addons_path,'emulator.retroarch')): dialogok("Reboot required", "In order to start playing games, you should reboot your device", "", "")
			else: gamesbutton_(admin)
			'''---------------------------'''

def gamesbutton_(admin):
	if not systemplatformwindows: os.system('sh /storage/.kodi/addons/script.htpt.emu/specials/scripts/launcher.sh')
	xbmc.executebuiltin('RunAddon(plugin.program.advanced.launcher)')
	xbmc.sleep(2000)
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	containernumitems = xbmc.getInfoLabel('Container.NumItems')
	'''---------------------------'''
	if (systemcurrentcontrol == "[..]" or systemcurrentcontrol == "[Default]") and (containernumitems == "0" or containernumitems == "1"):
		'''------------------------------
		---FIX-CONFIGURATION-FILE--------
		------------------------------'''
		print printfirst + space + "gamesbutton" + space + "Possible Error in file: launcher.xml"
		dialogok(localize(75795), localize(75796),"","")
		if not systemplatformwindows: os.system('sh /storage/.kodi/addons/script.htpt.emu/specials/scripts/copyemu.sh')
		xbmc.executebuiltin('ActivateWindow(Home.xml)')
		xbmc.sleep(2000)
		xbmc.executebuiltin('RunAddon(plugin.program.advanced.launcher)')
		'''---------------------------'''
	else:
		if not os.path.exists(os.path.join(rom_path,'Sega Master System')) and not os.path.exists(os.path.join(rom_path,'TurboGrafx 16')) and not os.path.exists(os.path.join(rom_path,'Sega Genesis')):
			dialogok("You currently have no games!", "Choose the Advanced Options button (Left Menu), then Choose YES.", "Click once on the Downloading Games button, then Choose Confirm to dow", "")
		elif scripthtptdebug_Info_Bluetooth == "":
			returned = dialogyesno("Bluetooth support", "Click YES in order to learn how to sync your PS3 controller")
			if returned == 'ok':
				diaogtextviewer("How to sync your PS3 controller", "This guide assume your hardware have a supported bluetooth adapter.[CR]If it's not then note that you maybe able to play with your PS3 cable attached![CR][CR]1. Enable your bluetooth by Choosing the Joystick Status button (left menu) then go up + right into service tab.[CR]Select the Enable Bluetooth option.[CR]2. Plug in your PS3 cable (Use 2.0 usb slot), connect it to the PS3 controller.[CR]Note: If the lights are blinking then your controller is charging.[CR]3. Click the PS button once.[CR]Note: The blinked lights are now off and your 1 player slot should light up.[CR]4. Unplug the PS3 cable.[CR]Note: The lights will blink and the controller should be auto sync in a few seconds.[CR]If that's not occur it's recommend to reboot your device.[CR]5. If the 1P light isn't on but 2-4P, you should unplug your others bluetooth device (one time), disconnect your PS3 controller by using the Josytick Status button, then turn on the PS3 controller by using the PS3 button.[CR][CR]- You can enable up to 4 PS3 controllers at once, they are all able to control your interface and in-game (ofcourse).")
			
def mode511(admin, name, printpoint):
	'''------------------------------
	---TRAILERS-BUTTON---------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode512(admin, name, printpoint):
	'''------------------------------
	---INTERNET-BUTTON---------------
	------------------------------'''
	name = localize(443)
	if systemplatformwindows: terminal('start /max www.google.co.il','')
	else:
		returned = supportcheck(name, ["A","B"], 1, Intel=True, platform="456")
		if returned == "ok":
			if connected or connected2 or connected3:
				returned = dialogyesno(str79215,str79216)
				if returned == "ok":
					addon = 'browser.chromium-browser'
					if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
						notification(str79217, str79218, "", 4000)
						settingschange('SystemSettings','input.enablemouse','1','no',xbmc.getInfoLabel('$LOCALIZE[14094]'),xbmc.getInfoLabel('$LOCALIZE[21369]'))
						xbmc.sleep(1000)
						if not systemplatformwindows: xbmc.executebuiltin('RunAddon(browser.chromium-browser)')
						'''---------------------------'''
					else: installaddon(admin, addon, "")
				else:
					notification_common("8")
					#settingschange('SystemSettings','input.enablemouse','0','no',xbmc.getInfoLabel('$LOCALIZE[14094]'),xbmc.getInfoLabel('$LOCALIZE[21369]'))
					'''---------------------------'''
				
				
				
			else: notification_common("4")
	'''---------------------------'''

def mode513(admin, name, printpoint):
	'''------------------------------
	---VIDEOS-BUTTON-----------------
	------------------------------'''
	name2 = str3
	path2 = "videos" 
	pictures_videos(admin, name, printpoint, 513, name2, path2)
	'''---------------------------'''

def mode514(value, admin, name, printpoint):
	'''------------------------------
	---MUSIC-BUTTON------------------
	------------------------------'''
	if value == "101" or not musicsep:
		'''------------------------------
		---HTPT-MUSIC--------------------
		------------------------------'''
		addon = 'plugin.video.htpt.music'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +',,)')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		if not musicsep:
			if musicseptip or scripthtptinstall_Skin_FirstBoot == "true":
				notification_common("25")
				if musicseptip: setSkinSetting("1", 'musicseptip', "false")
				
	elif value == "102":
		'''------------------------------
		---NINBORA-MUSIC-----------------
		------------------------------'''
		addon = 'repository.ninbora'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, update=True) ; xbmc.sleep(1000) ; xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(1000)
		else:
			addon = 'plugin.video.ninbora-music'
			if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				xbmc.executebuiltin('RunAddon('+ addon +',,)')
				'''---------------------------'''
			else: installaddon(admin, addon, "")
	
	if value == "103":
		'''------------------------------
		---LOCAL-MUSIC-------------------
		------------------------------'''
		name2 = str75004.encode('utf-8')
		if libraryhascontentmusic:
			if musiclinkstr == "": xbmc.executebuiltin('ActivateWindow(502,return)')
			else: xbmc.executebuiltin('ActivateWindow(502,'+ musiclinkstr +',return)')
		else:
			xbmc.executebuiltin('ActivateWindow(501,root),return)')
			#xbmc.executebuiltin('ActivateWindow(501),return)')
			xbmc.sleep(1000)
			dialogok('[COLOR=Yellow]' + addonString(120) % (name2.decode('utf-8')) + '[/COLOR]', addonString(147) % (name2.decode('utf-8')), localize(75783), '')
			'''---------------------------'''
			returned = supportcheck(name2, ["A", "B", "A?", "B?"], totalspace=40, Intel=False, silence=False)
			if returned != 'ok': pass
	
	elif value == "104":
		'''------------------------------
		---RADIO-------------------------
		------------------------------'''
		addon = 'plugin.video.israelive'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			#xbmc.executebuiltin('RunAddon('+ addon +',,)')
			if xbmc.getCondVisibility('!System.GetBool(pvrmanager.enabled)'): xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.israelive/?categoryid=9999&description&displayname=10000&iconimage=http%3a%2f%2fmdmorrope.gob.pe%2fportalweb%2fimagenes%2fradioss.png&mode=2&name=%5bCOLOR%20chartreuse%5d%5bB%5d%5b%d7%a8%d7%93%d7%99%d7%95%5d%5b%2fB%5d%5b%2fCOLOR%5d&url,return)')
			else: xbmc.executebuiltin('ActivateWindow(MyPVRChannels.xml)')
			'''---------------------------'''
		else: installaddon(admin, addon, "")

	'''---------------------------'''

def mode515(value, admin, name, printpoint):
	'''------------------------------
	---KIDS-BUTTON-------------------
	------------------------------'''
	if value == "101" or not kidsep:
		'''------------------------------
		---HTPT-KIDS---------------------
		------------------------------'''
		addon = 'plugin.video.htpt.kids'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +',,)')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		if not kidsep:
			if kidseptip or scripthtptinstall_Skin_FirstBoot == "true":
				#notification_common("25")
				if kidseptip: setSkinSetting("1", 'kidseptip', "false")
	'''---------------------------'''

def mode516(admin, name, printpoint):
	'''------------------------------
	---FAVOURITES-BUTTON-------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode517(admin, name, printpoint):
	'''------------------------------
	---LIVE-TV-BUTTON----------------
	------------------------------'''
	extra = "" ; TypeError = ""
	containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
	if livetvbutton2:
		name = "livetvbutton2"
		xbmc.executebuiltin('ActivateWindow(TVChannels)')
		xbmc.sleep(1000)
		mypvrchannels = xbmc.getCondVisibility('Window.IsVisible(MyPVRChannels.xml)')
		count = 0
		while count < 10 and not mypvrchannels and not xbmc.abortRequested:
			xbmc.sleep(100)
			count += 1
			mypvrchannels = xbmc.getCondVisibility('Window.IsVisible(MyPVRChannels.xml)')
			xbmc.sleep(100)
		if mypvrchannels:
			containerfoldername = xbmc.getInfoLabel('Container.FolderName')
			containernumitems = xbmc.getInfoLabel('Container.NumItems')
			try:
				if int(containernumitems) < 2: printpoint = printpoint + "8"
				elif containerfoldername != localize(19287): dialogok('[COLOR=Yellow]' + '$LOCALIZE[19051]' + '[/COLOR]', str79548 % (containernumitems), str79549, "")
			except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)

		else: printpoint = printpoint + "9"
		if "8" in printpoint or "9" in printpoint:
			xbmc.executebuiltin('RunAddon(plugin.video.israelive)')
			dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
			count = 0
			while count < 10 and not dialogkaitoastW and not xbmc.abortRequested:
				count += 1
				xbmc.sleep(200)
				dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
			if count == 10:
				xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=10)')		
	else:
		if livetvbutton: name = "livetvbutton"
		else: name = "livetvcustom"
		returned = ActivateWindow("0", 'plugin.video.israelive', 'plugin://plugin.video.israelive/', 1, wait=True)
		if not "ok" in returned:
			printpoint = printpoint + "6"
			returned = ActivateWindow("1", 'plugin.video.israelive', 'plugin://plugin.video.israelive/', 1, wait=True)
		if "ok" in returned:
			printpoint = printpoint + "7"
			pass
		containernumitems = xbmc.getInfoLabel('Container.NumItems')
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		
	if admin or extra != "": print printfirst + name + "_LV" + printpoint + space + "containernumitems" + space2 + str(containernumitems) + space + "containerfolderpath" + space2 + containerfolderpath + extra
	'''---------------------------'''

def mode518(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode518(admin, name, printpoint)
	'''---------------------------'''

def mode519(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode519(admin, name, printpoint)
	'''---------------------------'''

def mode520(admin, name, printpoint):
	'''------------------------------
	---ADULT-MOVIE-BUTTON------------
	------------------------------'''
	addon = 'repository.xbmcadult'
	if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, update=True) ; xbmc.sleep(1000) ; xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(1000)

	addon = 'plugin.video.videodevil'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon(plugin.video.videodevil)')
	else: installaddon(admin, addon, "", update=True)
	'''---------------------------'''
	
def mode521(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode521(admin, name, printpoint)
	'''---------------------------'''

def mode522(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode522(admin, name, printpoint)
	'''---------------------------'''

def mode523(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode523(admin, name, printpoint)
	'''---------------------------'''

def mode524(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode524(admin, name, printpoint)
	'''---------------------------'''

def mode525(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode525(admin, name, printpoint)
	'''---------------------------'''

def mode526(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode526(admin, name, printpoint)
	'''---------------------------'''

def mode527(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode527(admin, name, printpoint)
	'''---------------------------'''

def mode528(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode528(admin, name, printpoint)
	'''---------------------------'''

def mode529(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode529(admin, name, printpoint)
	'''---------------------------'''

def mode530(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode530(admin, name, printpoint)
	'''---------------------------'''
	
def mode531(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode531(admin, name, printpoint)
	'''---------------------------'''

def mode532(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode532(admin, name, printpoint)
	'''---------------------------'''

def mode533(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode533(admin, name, printpoint)
	'''---------------------------'''

def mode534(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode534(admin, name, printpoint)
	'''---------------------------'''

def mode535(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode535(admin, name, printpoint)
	'''---------------------------'''

def mode536(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode536(admin, name, printpoint)
	'''---------------------------'''

def mode537(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode537(admin, name, printpoint)
	'''---------------------------'''

def mode538(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode538(admin, name, printpoint)
	'''---------------------------'''

def mode539(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode539(admin, name, printpoint)
	'''---------------------------'''

def mode540(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode540(admin, name, printpoint)
	'''---------------------------'''
	
def mode541(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode541(admin, name, printpoint)
	'''---------------------------'''

def mode542(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode542(admin, name, printpoint)
	'''---------------------------'''

def mode543(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode543(admin, name, printpoint)
	'''---------------------------'''

def mode544(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode544(admin, name, printpoint)
	'''---------------------------'''

def mode545(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode545(admin, name, printpoint)
	'''---------------------------'''

def mode546(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode546(admin, name, printpoint)
	'''---------------------------'''

def mode547(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode547(admin, name, printpoint)
	'''---------------------------'''

def mode548(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode548(admin, name, printpoint)
	'''---------------------------'''

def mode549(value, admin, name, printpoint):
	'''------------------------------
	---MORE-BUTTON-------------------
	------------------------------'''
	if value == "101":
		'''------------------------------
		---GAMER-TV----------------------
		------------------------------'''
		addon = 'plugin.video.g4tv'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +')')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		
	elif value == "102":
		'''------------------------------
		---GUITAR------------------------
		------------------------------'''
		addon = 'plugin.video.ultimateguitar'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +')')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
	
	elif value == "103":
		'''------------------------------
		---QUIZ--------------------------
		------------------------------'''
		addon = 'script.moviequiz'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +')')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
	
	elif value == "104":
		'''------------------------------
		---?--------------------------
		------------------------------'''
		addon = 'plugin.video.ultimateguitar'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +')')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
	'''---------------------------'''

def mode550(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode550(admin, name, printpoint)
	'''---------------------------'''

def mode551(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode551(admin, name, printpoint)
	'''---------------------------'''

def mode552(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode552(admin, name, printpoint)
	'''---------------------------'''

def mode553(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode553(admin, name, printpoint)
	'''---------------------------'''

def mode554(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode554(admin, name, printpoint)
	'''---------------------------'''

def mode555(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode555(admin, name, printpoint)
	'''---------------------------'''

def mode556(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode556(admin, name, printpoint)
	'''---------------------------'''

def mode557(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode557(admin, name, printpoint)
	'''---------------------------'''

def mode558(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode558(admin, name, printpoint)
	'''---------------------------'''

def mode559(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode559(admin, name, printpoint)
	'''---------------------------'''

def mode560(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode560(admin, name, printpoint)
	'''---------------------------'''

def mode561(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode561(admin, name, printpoint)
	'''---------------------------'''

def mode562(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode562(admin, name, printpoint)
	'''---------------------------'''

def mode563(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode563(admin, name, printpoint)
	'''---------------------------'''

def mode564(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode564(admin, name, printpoint)
	'''---------------------------'''

def mode565(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode565(admin, name, printpoint)
	'''---------------------------'''

def mode566(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode566(admin, name, printpoint)
	'''---------------------------'''

def mode567(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode567(admin, name, printpoint)
	'''---------------------------'''

def mode568(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode568(admin, name, printpoint)
	'''---------------------------'''

def mode569(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode569(admin, name, printpoint)
	'''---------------------------'''

def mode570(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode570(admin, name, printpoint)
	'''---------------------------'''

def mode571(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode571(admin, name, printpoint)
	'''---------------------------'''

def mode572(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode572(admin, name, printpoint)
	'''---------------------------'''

def mode573(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode573(admin, name, printpoint)
	'''---------------------------'''

def mode574(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode574(admin, name, printpoint)
	'''---------------------------'''

def mode575(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode575(admin, name, printpoint)
	'''---------------------------'''

def mode576(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode576(admin, name, printpoint)
	'''---------------------------'''

def mode577(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode577(admin, name, printpoint)
	'''---------------------------'''

def mode578(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode578(admin, name, printpoint)
	'''---------------------------'''

def mode579(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode579(admin, name, printpoint)
	'''---------------------------'''
	
def mode580(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode580(admin, name, printpoint)
	'''---------------------------'''

def mode581(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode581(admin, name, printpoint)
	'''---------------------------'''

def mode582(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode582(admin, name, printpoint)
	'''---------------------------'''

def mode583(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode583(admin, name, printpoint)
	'''---------------------------'''

def mode584(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode584(admin, name, printpoint)
	'''---------------------------'''

def mode585(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode585(admin, name, printpoint)
	'''---------------------------'''

def mode586(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode586(admin, name, printpoint)
	'''---------------------------'''

def mode587(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode587(admin, name, printpoint)
	'''---------------------------'''

def mode588(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode588(admin, name, printpoint)
	'''---------------------------'''

def mode589(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode589(admin, name, printpoint)
	'''---------------------------'''
	
def mode590(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode590(admin, name, printpoint)
	'''---------------------------'''

def mode591(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode591(admin, name, printpoint)
	'''---------------------------'''

def mode592(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode592(admin, name, printpoint)
	'''---------------------------'''

def mode593(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode593(admin, name, printpoint)
	'''---------------------------'''

def mode594(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode594(admin, name, printpoint)
	'''---------------------------'''

def mode595(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode595(admin, name, printpoint)
	'''---------------------------'''

def mode596(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode596(admin, name, printpoint)
	'''---------------------------'''

def mode597(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode597(admin, name, printpoint)
	'''---------------------------'''

def mode598(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode598(admin, name, printpoint)
	'''---------------------------'''

def mode599(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode599(admin, name, printpoint)
	'''---------------------------'''

def mode600(admin, name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode600(admin, name, printpoint)
	'''---------------------------'''

def mode601(admin,name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode601(admin, name, printpoint)
	'''---------------------------'''

def mode602(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode602(admin, name, printpoint)
	'''---------------------------'''
	
def mode603(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode603(admin, name, printpoint)
	'''---------------------------'''

def mode604(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode604(admin, name, printpoint)
	'''---------------------------'''

def mode605(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode605(admin, name, printpoint)
	'''---------------------------'''

def mode606(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode606(admin, name, printpoint)
	'''---------------------------'''

def mode607(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode607(admin, name, printpoint)
	'''---------------------------'''

def mode608(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode608(admin, name, printpoint)
	'''---------------------------'''

def mode609(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode609(admin, name, printpoint)
	'''---------------------------'''

def mode610(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode640(admin, name, printpoint)
	'''---------------------------'''
	
def mode611(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode611(admin, name, printpoint)
	'''---------------------------'''

def mode612(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode612(admin, name, printpoint)
	'''---------------------------'''

def mode613(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode613(admin, name, printpoint)
	'''---------------------------'''

def mode614(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode614(admin, name, printpoint)
	'''---------------------------'''

def mode615(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode615(admin, name, printpoint)
	'''---------------------------'''

def mode616(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode616(admin, name, printpoint)
	'''---------------------------'''

def mode617(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode617(admin, name, printpoint)
	'''---------------------------'''

def mode618(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode618(admin, name, printpoint)
	'''---------------------------'''

def mode619(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode619(admin, name, printpoint)
	'''---------------------------'''

def mode620(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode620(admin, name, printpoint)
	'''---------------------------'''
	
def mode621(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode621(admin, name, printpoint)
	'''---------------------------'''

def mode622(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode622(admin, name, printpoint)
	'''---------------------------'''

def mode623(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode623(admin, name, printpoint)
	'''---------------------------'''

def mode624(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode624(admin, name, printpoint)
	'''---------------------------'''

def mode625(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode625(admin, name, printpoint)
	'''---------------------------'''

def mode626(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode626(admin, name, printpoint)
	'''---------------------------'''

def mode627(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode627(admin, name, printpoint)
	'''---------------------------'''

def mode628(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode628(admin, name, printpoint)
	'''---------------------------'''

def mode629(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode629(admin, name, printpoint)
	'''---------------------------'''

def mode630(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode630(admin, name, printpoint)
	'''---------------------------'''
	
def mode631(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode631(admin, name, printpoint)
	'''---------------------------'''

def mode632(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode632(admin, name, printpoint)
	'''---------------------------'''

def mode633(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode633(admin, name, printpoint)
	'''---------------------------'''

def mode634(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode634(admin, name, printpoint)
	'''---------------------------'''

def mode635(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode635(admin, name, printpoint)
	'''---------------------------'''

def mode636(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode636(admin, name, printpoint)
	'''---------------------------'''

def mode637(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode637(admin, name, printpoint)
	'''---------------------------'''

def mode638(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode638(admin, name, printpoint)
	'''---------------------------'''

def mode639(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode639(admin, name, printpoint)
	'''---------------------------'''

def mode640(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode640(admin, name, printpoint)
	'''---------------------------'''
	
def mode641(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode641(admin, name, printpoint)
	'''---------------------------'''

def mode642(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode642(admin, name, printpoint)
	'''---------------------------'''

def mode643(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode643(admin, name, printpoint)
	'''---------------------------'''

def mode644(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode644(admin, name, printpoint)
	'''---------------------------'''

def mode645(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode645(admin, name, printpoint)
	'''---------------------------'''

def mode646(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode646(admin, name, printpoint)
	'''---------------------------'''

def mode647(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode647(admin, name, printpoint)
	'''---------------------------'''

def mode648(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode648(admin, name, printpoint)
	'''---------------------------'''

def mode649(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode649(admin, name, printpoint)
	'''---------------------------'''

def mode650(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode650(admin, name, printpoint)
	'''---------------------------'''

def mode651(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode651(admin, name, printpoint)
	'''---------------------------'''

def mode652(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode652(admin, name, printpoint)
	'''---------------------------'''

def mode653(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode653(admin, name, printpoint)
	'''---------------------------'''

def mode654(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode654(admin, name, printpoint)
	'''---------------------------'''

def mode655(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode655(admin, name, printpoint)
	'''---------------------------'''

def mode656(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode656(admin, name, printpoint)
	'''---------------------------'''

def mode657(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode657(admin, name, printpoint)
	'''---------------------------'''

def mode658(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode658(admin, name, printpoint)
	'''---------------------------'''

def mode659(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode659(admin, name, printpoint)
	'''---------------------------'''

def mode660(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode660(admin, name, printpoint)
	'''---------------------------'''

def mode661(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode661(admin, name, printpoint)
	'''---------------------------'''

def mode662(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode662(admin, name, printpoint)
	'''---------------------------'''

def mode663(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode663(admin, name, printpoint)
	'''---------------------------'''

def mode664(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode664(admin, name, printpoint)
	'''---------------------------'''

def mode665(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode665(admin, name, printpoint)
	'''---------------------------'''

def mode666(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode666(admin, name, printpoint)
	'''---------------------------'''

def mode667(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode667(admin, name, printpoint)
	'''---------------------------'''

def mode668(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode668(admin, name, printpoint)
	'''---------------------------'''

def mode669(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode669(admin, name, printpoint)
	'''---------------------------'''

def mode670(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode670(admin, name, printpoint)
	'''---------------------------'''

def mode671(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode671(admin, name, printpoint)
	'''---------------------------'''

def mode672(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode672(admin, name, printpoint)
	'''---------------------------'''

def mode673(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode673(admin, name, printpoint)
	'''---------------------------'''

def mode674(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode674(admin, name, printpoint)
	'''---------------------------'''

def mode675(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode675(admin, name, printpoint)
	'''---------------------------'''

def mode676(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode676(admin, name, printpoint)
	'''---------------------------'''

def mode677(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode677(admin, name, printpoint)
	'''---------------------------'''

def mode678(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode678(admin, name, printpoint)
	'''---------------------------'''

def mode679(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode679(admin, name, printpoint)
	'''---------------------------'''
	
def mode680(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode680(admin, name, printpoint)
	'''---------------------------'''

def mode681(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode681(admin, name, printpoint)
	'''---------------------------'''

def mode682(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode682(admin, name, printpoint)
	'''---------------------------'''

def mode683(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode683(admin, name, printpoint)
	'''---------------------------'''

def mode684(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode684(admin, name, printpoint)
	'''---------------------------'''

def mode685(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode685(admin, name, printpoint)
	'''---------------------------'''

def mode686(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode686(admin, name, printpoint)
	'''---------------------------'''

def mode687(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode687(admin, name, printpoint)
	'''---------------------------'''

def mode688(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode688(admin, name, printpoint)
	'''---------------------------'''

def mode689(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode689(admin, name, printpoint)
	'''---------------------------'''
	
def mode690(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode690(admin, name, printpoint)
	'''---------------------------'''

def mode691(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode691(admin, name, printpoint)
	'''---------------------------'''

def mode692(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode692(admin, name, printpoint)
	'''---------------------------'''

def mode693(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode693(admin, name, printpoint)
	'''---------------------------'''

def mode694(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode694(admin, name, printpoint)
	'''---------------------------'''

def mode695(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode695(admin, name, printpoint)
	'''---------------------------'''

def mode696(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode696(admin, name, printpoint)
	'''---------------------------'''

def mode697(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode697(admin, name, printpoint)
	'''---------------------------'''

def mode698(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode698(admin, name, printpoint)
	'''---------------------------'''

def mode699(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode699(admin, name, printpoint)
	'''---------------------------'''

def mode700(admin, name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode700(admin, name, printpoint)
	'''---------------------------'''

def mode701(admin,name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode701(admin, name, printpoint)
	'''---------------------------'''

def mode702(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode702(admin, name, printpoint)
	'''---------------------------'''
	
def mode703(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode703(admin, name, printpoint)
	'''---------------------------'''

def mode704(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode704(admin, name, printpoint)
	'''---------------------------'''

def mode705(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode705(admin, name, printpoint)
	'''---------------------------'''

def mode706(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode706(admin, name, printpoint)
	'''---------------------------'''

def mode707(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode707(admin, name, printpoint)
	'''---------------------------'''

def mode708(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode708(admin, name, printpoint)
	'''---------------------------'''

def mode709(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode709(admin, name, printpoint)
	'''---------------------------'''

def mode710(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode740(admin, name, printpoint)
	'''---------------------------'''
	
def mode711(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode711(admin, name, printpoint)
	'''---------------------------'''

def mode712(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode712(admin, name, printpoint)
	'''---------------------------'''

def mode713(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode713(admin, name, printpoint)
	'''---------------------------'''

def mode714(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode714(admin, name, printpoint)
	'''---------------------------'''

def mode715(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode715(admin, name, printpoint)
	'''---------------------------'''

def mode716(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode716(admin, name, printpoint)
	'''---------------------------'''

def mode717(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode717(admin, name, printpoint)
	'''---------------------------'''

def mode718(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode718(admin, name, printpoint)
	'''---------------------------'''

def mode719(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode719(admin, name, printpoint)
	'''---------------------------'''

def mode720(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode720(admin, name, printpoint)
	'''---------------------------'''
	
def mode721(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode721(admin, name, printpoint)
	'''---------------------------'''

def mode722(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode722(admin, name, printpoint)
	'''---------------------------'''

def mode723(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode723(admin, name, printpoint)
	'''---------------------------'''

def mode724(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode724(admin, name, printpoint)
	'''---------------------------'''

def mode725(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode725(admin, name, printpoint)
	'''---------------------------'''

def mode726(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode726(admin, name, printpoint)
	'''---------------------------'''

def mode727(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode727(admin, name, printpoint)
	'''---------------------------'''

def mode728(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode728(admin, name, printpoint)
	'''---------------------------'''

def mode729(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode729(admin, name, printpoint)
	'''---------------------------'''

def mode730(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode730(admin, name, printpoint)
	'''---------------------------'''
	
def mode731(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode731(admin, name, printpoint)
	'''---------------------------'''

def mode732(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode732(admin, name, printpoint)
	'''---------------------------'''

def mode733(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode733(admin, name, printpoint)
	'''---------------------------'''

def mode734(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode734(admin, name, printpoint)
	'''---------------------------'''

def mode735(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode735(admin, name, printpoint)
	'''---------------------------'''

def mode736(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode736(admin, name, printpoint)
	'''---------------------------'''

def mode737(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode737(admin, name, printpoint)
	'''---------------------------'''

def mode738(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode738(admin, name, printpoint)
	'''---------------------------'''

def mode739(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode739(admin, name, printpoint)
	'''---------------------------'''

def mode740(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode740(admin, name, printpoint)
	'''---------------------------'''
	
def mode741(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode741(admin, name, printpoint)
	'''---------------------------'''

def mode742(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode742(admin, name, printpoint)
	'''---------------------------'''

def mode743(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode743(admin, name, printpoint)
	'''---------------------------'''

def mode744(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode744(admin, name, printpoint)
	'''---------------------------'''

def mode745(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode745(admin, name, printpoint)
	'''---------------------------'''

def mode746(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode746(admin, name, printpoint)
	'''---------------------------'''

def mode747(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode747(admin, name, printpoint)
	'''---------------------------'''

def mode748(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode748(admin, name, printpoint)
	'''---------------------------'''

def mode749(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode749(admin, name, printpoint)
	'''---------------------------'''

def mode750(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode750(admin, name, printpoint)
	'''---------------------------'''

def mode751(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode751(admin, name, printpoint)
	'''---------------------------'''

def mode752(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode752(admin, name, printpoint)
	'''---------------------------'''

def mode753(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode753(admin, name, printpoint)
	'''---------------------------'''

def mode754(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode754(admin, name, printpoint)
	'''---------------------------'''

def mode755(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode755(admin, name, printpoint)
	'''---------------------------'''

def mode756(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode756(admin, name, printpoint)
	'''---------------------------'''

def mode757(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode757(admin, name, printpoint)
	'''---------------------------'''

def mode758(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode758(admin, name, printpoint)
	'''---------------------------'''

def mode759(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode759(admin, name, printpoint)
	'''---------------------------'''

def mode760(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode760(admin, name, printpoint)
	'''---------------------------'''

def mode761(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode761(admin, name, printpoint)
	'''---------------------------'''

def mode762(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode762(admin, name, printpoint)
	'''---------------------------'''

def mode763(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode763(admin, name, printpoint)
	'''---------------------------'''

def mode764(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode764(admin, name, printpoint)
	'''---------------------------'''

def mode765(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode765(admin, name, printpoint)
	'''---------------------------'''

def mode766(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode766(admin, name, printpoint)
	'''---------------------------'''

def mode767(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode767(admin, name, printpoint)
	'''---------------------------'''

def mode768(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode768(admin, name, printpoint)
	'''---------------------------'''

def mode769(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode769(admin, name, printpoint)
	'''---------------------------'''

def mode770(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode770(admin, name, printpoint)
	'''---------------------------'''

def mode771(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode771(admin, name, printpoint)
	'''---------------------------'''

def mode772(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode772(admin, name, printpoint)
	'''---------------------------'''

def mode773(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode773(admin, name, printpoint)
	'''---------------------------'''

def mode774(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode774(admin, name, printpoint)
	'''---------------------------'''

def mode775(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode775(admin, name, printpoint)
	'''---------------------------'''

def mode776(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode776(admin, name, printpoint)
	'''---------------------------'''

def mode777(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode777(admin, name, printpoint)
	'''---------------------------'''

def mode778(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode778(admin, name, printpoint)
	'''---------------------------'''

def mode779(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode779(admin, name, printpoint)
	'''---------------------------'''
	
def mode780(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode780(admin, name, printpoint)
	'''---------------------------'''

def mode781(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode781(admin, name, printpoint)
	'''---------------------------'''

def mode782(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode782(admin, name, printpoint)
	'''---------------------------'''

def mode783(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode783(admin, name, printpoint)
	'''---------------------------'''

def mode784(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode784(admin, name, printpoint)
	'''---------------------------'''

def mode785(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode785(admin, name, printpoint)
	'''---------------------------'''

def mode786(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode786(admin, name, printpoint)
	'''---------------------------'''

def mode787(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode787(admin, name, printpoint)
	'''---------------------------'''

def mode788(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode788(admin, name, printpoint)
	'''---------------------------'''

def mode789(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode789(admin, name, printpoint)
	'''---------------------------'''
	
def mode790(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode790(admin, name, printpoint)
	'''---------------------------'''

def mode791(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode791(admin, name, printpoint)
	'''---------------------------'''

def mode792(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode792(admin, name, printpoint)
	'''---------------------------'''

def mode793(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode793(admin, name, printpoint)
	'''---------------------------'''

def mode794(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode794(admin, name, printpoint)
	'''---------------------------'''

def mode795(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode795(admin, name, printpoint)
	'''---------------------------'''

def mode796(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode796(admin, name, printpoint)
	'''---------------------------'''

def mode797(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode797(admin, name, printpoint)
	'''---------------------------'''

def mode798(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode798(admin, name, printpoint)
	'''---------------------------'''

def mode799(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode799(admin, name, printpoint)
	'''---------------------------'''

def mode800(admin, name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode800(admin, name, printpoint)
	'''---------------------------'''

def mode801(admin,name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode801(admin, name, printpoint)
	'''---------------------------'''

def mode802(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode802(admin, name, printpoint)
	'''---------------------------'''
	
def mode803(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode803(admin, name, printpoint)
	'''---------------------------'''

def mode804(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode804(admin, name, printpoint)
	'''---------------------------'''

def mode805(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode805(admin, name, printpoint)
	'''---------------------------'''

def mode806(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode806(admin, name, printpoint)
	'''---------------------------'''

def mode807(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode807(admin, name, printpoint)
	'''---------------------------'''

def mode808(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode808(admin, name, printpoint)
	'''---------------------------'''

def mode809(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode809(admin, name, printpoint)
	'''---------------------------'''

def mode810(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode840(admin, name, printpoint)
	'''---------------------------'''
	
def mode811(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode811(admin, name, printpoint)
	'''---------------------------'''

def mode812(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode812(admin, name, printpoint)
	'''---------------------------'''

def mode813(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode813(admin, name, printpoint)
	'''---------------------------'''

def mode814(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode814(admin, name, printpoint)
	'''---------------------------'''

def mode815(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode815(admin, name, printpoint)
	'''---------------------------'''

def mode816(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode816(admin, name, printpoint)
	'''---------------------------'''

def mode817(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode817(admin, name, printpoint)
	'''---------------------------'''

def mode818(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode818(admin, name, printpoint)
	'''---------------------------'''

def mode819(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode819(admin, name, printpoint)
	'''---------------------------'''

def mode820(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode820(admin, name, printpoint)
	'''---------------------------'''
	
def mode821(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode821(admin, name, printpoint)
	'''---------------------------'''

def mode822(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode822(admin, name, printpoint)
	'''---------------------------'''

def mode823(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode823(admin, name, printpoint)
	'''---------------------------'''

def mode824(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode824(admin, name, printpoint)
	'''---------------------------'''

def mode825(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode825(admin, name, printpoint)
	'''---------------------------'''

def mode826(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode826(admin, name, printpoint)
	'''---------------------------'''

def mode827(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode827(admin, name, printpoint)
	'''---------------------------'''

def mode828(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode828(admin, name, printpoint)
	'''---------------------------'''

def mode829(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode829(admin, name, printpoint)
	'''---------------------------'''

def mode830(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode830(admin, name, printpoint)
	'''---------------------------'''
	
def mode831(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode831(admin, name, printpoint)
	'''---------------------------'''

def mode832(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode832(admin, name, printpoint)
	'''---------------------------'''

def mode833(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode833(admin, name, printpoint)
	'''---------------------------'''

def mode834(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode834(admin, name, printpoint)
	'''---------------------------'''

def mode835(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode835(admin, name, printpoint)
	'''---------------------------'''

def mode836(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode836(admin, name, printpoint)
	'''---------------------------'''

def mode837(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode837(admin, name, printpoint)
	'''---------------------------'''

def mode838(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode838(admin, name, printpoint)
	'''---------------------------'''

def mode839(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode839(admin, name, printpoint)
	'''---------------------------'''

def mode840(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode840(admin, name, printpoint)
	'''---------------------------'''
	
def mode841(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode841(admin, name, printpoint)
	'''---------------------------'''

def mode842(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode842(admin, name, printpoint)
	'''---------------------------'''

def mode843(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode843(admin, name, printpoint)
	'''---------------------------'''

def mode844(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode844(admin, name, printpoint)
	'''---------------------------'''

def mode845(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode845(admin, name, printpoint)
	'''---------------------------'''

def mode846(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode846(admin, name, printpoint)
	'''---------------------------'''

def mode847(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode847(admin, name, printpoint)
	'''---------------------------'''

def mode848(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode848(admin, name, printpoint)
	'''---------------------------'''

def mode849(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode849(admin, name, printpoint)
	'''---------------------------'''

def mode850(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode850(admin, name, printpoint)
	'''---------------------------'''

def mode851(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode851(admin, name, printpoint)
	'''---------------------------'''

def mode852(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode852(admin, name, printpoint)
	'''---------------------------'''

def mode853(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode853(admin, name, printpoint)
	'''---------------------------'''

def mode854(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode854(admin, name, printpoint)
	'''---------------------------'''

def mode855(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode855(admin, name, printpoint)
	'''---------------------------'''

def mode856(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode856(admin, name, printpoint)
	'''---------------------------'''

def mode857(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode857(admin, name, printpoint)
	'''---------------------------'''

def mode858(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode858(admin, name, printpoint)
	'''---------------------------'''

def mode859(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode859(admin, name, printpoint)
	'''---------------------------'''

def mode860(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode860(admin, name, printpoint)
	'''---------------------------'''

def mode861(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode861(admin, name, printpoint)
	'''---------------------------'''

def mode862(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode862(admin, name, printpoint)
	'''---------------------------'''

def mode863(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode863(admin, name, printpoint)
	'''---------------------------'''

def mode864(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode864(admin, name, printpoint)
	'''---------------------------'''

def mode865(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode865(admin, name, printpoint)
	'''---------------------------'''

def mode866(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode866(admin, name, printpoint)
	'''---------------------------'''

def mode867(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode867(admin, name, printpoint)
	'''---------------------------'''

def mode868(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode868(admin, name, printpoint)
	'''---------------------------'''

def mode869(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode869(admin, name, printpoint)
	'''---------------------------'''

def mode870(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode870(admin, name, printpoint)
	'''---------------------------'''

def mode871(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode871(admin, name, printpoint)
	'''---------------------------'''

def mode872(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode872(admin, name, printpoint)
	'''---------------------------'''

def mode873(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode873(admin, name, printpoint)
	'''---------------------------'''

def mode874(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode874(admin, name, printpoint)
	'''---------------------------'''

def mode875(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode875(admin, name, printpoint)
	'''---------------------------'''

def mode876(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode876(admin, name, printpoint)
	'''---------------------------'''

def mode877(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode877(admin, name, printpoint)
	'''---------------------------'''

def mode878(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode878(admin, name, printpoint)
	'''---------------------------'''

def mode879(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode879(admin, name, printpoint)
	'''---------------------------'''
	
def mode880(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode880(admin, name, printpoint)
	'''---------------------------'''

def mode881(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode881(admin, name, printpoint)
	'''---------------------------'''

def mode882(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode882(admin, name, printpoint)
	'''---------------------------'''

def mode883(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode883(admin, name, printpoint)
	'''---------------------------'''

def mode884(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode884(admin, name, printpoint)
	'''---------------------------'''

def mode885(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode885(admin, name, printpoint)
	'''---------------------------'''

def mode886(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode886(admin, name, printpoint)
	'''---------------------------'''

def mode887(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode887(admin, name, printpoint)
	'''---------------------------'''

def mode888(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode888(admin, name, printpoint)
	'''---------------------------'''

def mode889(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode889(admin, name, printpoint)
	'''---------------------------'''
	
def mode890(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode890(admin, name, printpoint)
	'''---------------------------'''

def mode891(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode891(admin, name, printpoint)
	'''---------------------------'''

def mode892(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode892(admin, name, printpoint)
	'''---------------------------'''

def mode893(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode893(admin, name, printpoint)
	'''---------------------------'''

def mode894(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode894(admin, name, printpoint)
	'''---------------------------'''

def mode895(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode895(admin, name, printpoint)
	'''---------------------------'''

def mode896(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode896(admin, name, printpoint)
	'''---------------------------'''

def mode897(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode897(admin, name, printpoint)
	'''---------------------------'''

def mode898(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode898(admin, name, printpoint)
	'''---------------------------'''

def mode899(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode899(admin, name, printpoint)
	'''---------------------------'''

def mode900(admin, name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode900(admin, name, printpoint)
	'''---------------------------'''

def mode901(admin,name):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode901(admin, name, printpoint)
	'''---------------------------'''

def mode902(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode902(admin, name, printpoint)
	'''---------------------------'''
	
def mode903(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode903(admin, name, printpoint)
	'''---------------------------'''

def mode904(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode904(admin, name, printpoint)
	'''---------------------------'''

def mode905(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode905(admin, name, printpoint)
	'''---------------------------'''

def mode906(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode906(admin, name, printpoint)
	'''---------------------------'''

def mode907(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode907(admin, name, printpoint)
	'''---------------------------'''

def mode908(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode908(admin, name, printpoint)
	'''---------------------------'''

def mode909(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode909(admin, name, printpoint)
	'''---------------------------'''

def mode910(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode940(admin, name, printpoint)
	'''---------------------------'''
	
def mode911(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode911(admin, name, printpoint)
	'''---------------------------'''

def mode912(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode912(admin, name, printpoint)
	'''---------------------------'''

def mode913(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode913(admin, name, printpoint)
	'''---------------------------'''

def mode914(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode914(admin, name, printpoint)
	'''---------------------------'''

def mode915(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode915(admin, name, printpoint)
	'''---------------------------'''

def mode916(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode916(admin, name, printpoint)
	'''---------------------------'''

def mode917(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode917(admin, name, printpoint)
	'''---------------------------'''

def mode918(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode918(admin, name, printpoint)
	'''---------------------------'''

def mode919(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode919(admin, name, printpoint)
	'''---------------------------'''

def mode920(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode920(admin, name, printpoint)
	'''---------------------------'''
	
def mode921(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode921(admin, name, printpoint)
	'''---------------------------'''

def mode922(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode922(admin, name, printpoint)
	'''---------------------------'''

def mode923(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode923(admin, name, printpoint)
	'''---------------------------'''

def mode924(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode924(admin, name, printpoint)
	'''---------------------------'''

def mode925(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode925(admin, name, printpoint)
	'''---------------------------'''

def mode926(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode926(admin, name, printpoint)
	'''---------------------------'''

def mode927(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode927(admin, name, printpoint)
	'''---------------------------'''

def mode928(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode928(admin, name, printpoint)
	'''---------------------------'''

def mode929(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode929(admin, name, printpoint)
	'''---------------------------'''

def mode930(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode930(admin, name, printpoint)
	'''---------------------------'''
	
def mode931(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode931(admin, name, printpoint)
	'''---------------------------'''

def mode932(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode932(admin, name, printpoint)
	'''---------------------------'''

def mode933(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode933(admin, name, printpoint)
	'''---------------------------'''

def mode934(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode934(admin, name, printpoint)
	'''---------------------------'''

def mode935(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode935(admin, name, printpoint)
	'''---------------------------'''

def mode936(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode936(admin, name, printpoint)
	'''---------------------------'''

def mode937(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode937(admin, name, printpoint)
	'''---------------------------'''

def mode938(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode938(admin, name, printpoint)
	'''---------------------------'''

def mode939(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode939(admin, name, printpoint)
	'''---------------------------'''

def mode940(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode940(admin, name, printpoint)
	'''---------------------------'''
	
def mode941(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode941(admin, name, printpoint)
	'''---------------------------'''

def mode942(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode942(admin, name, printpoint)
	'''---------------------------'''

def mode943(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode943(admin, name, printpoint)
	'''---------------------------'''

def mode944(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode944(admin, name, printpoint)
	'''---------------------------'''

def mode945(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode945(admin, name, printpoint)
	'''---------------------------'''

def mode946(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode946(admin, name, printpoint)
	'''---------------------------'''

def mode947(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode947(admin, name, printpoint)
	'''---------------------------'''

def mode948(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode948(admin, name, printpoint)
	'''---------------------------'''

def mode949(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode949(admin, name, printpoint)
	'''---------------------------'''

def mode950(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode950(admin, name, printpoint)
	'''---------------------------'''

def mode951(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode951(admin, name, printpoint)
	'''---------------------------'''

def mode952(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode952(admin, name, printpoint)
	'''---------------------------'''

def mode953(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode953(admin, name, printpoint)
	'''---------------------------'''

def mode954(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode954(admin, name, printpoint)
	'''---------------------------'''

def mode955(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode955(admin, name, printpoint)
	'''---------------------------'''

def mode956(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode956(admin, name, printpoint)
	'''---------------------------'''

def mode957(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode957(admin, name, printpoint)
	'''---------------------------'''

def mode958(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode958(admin, name, printpoint)
	'''---------------------------'''

def mode959(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode959(admin, name, printpoint)
	'''---------------------------'''

def mode960(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode960(admin, name, printpoint)
	'''---------------------------'''

def mode961(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode961(admin, name, printpoint)
	'''---------------------------'''

def mode962(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode962(admin, name, printpoint)
	'''---------------------------'''

def mode963(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode963(admin, name, printpoint)
	'''---------------------------'''

def mode964(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode964(admin, name, printpoint)
	'''---------------------------'''

def mode965(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode965(admin, name, printpoint)
	'''---------------------------'''

def mode966(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode966(admin, name, printpoint)
	'''---------------------------'''

def mode967(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode967(admin, name, printpoint)
	'''---------------------------'''

def mode968(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode968(admin, name, printpoint)
	'''---------------------------'''

def mode969(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode969(admin, name, printpoint)
	'''---------------------------'''

def mode970(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode970(admin, name, printpoint)
	'''---------------------------'''

def mode971(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode971(admin, name, printpoint)
	'''---------------------------'''

def mode972(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode972(admin, name, printpoint)
	'''---------------------------'''

def mode973(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode973(admin, name, printpoint)
	'''---------------------------'''

def mode974(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode974(admin, name, printpoint)
	'''---------------------------'''

def mode975(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode975(admin, name, printpoint)
	'''---------------------------'''

def mode976(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode976(admin, name, printpoint)
	'''---------------------------'''

def mode977(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode977(admin, name, printpoint)
	'''---------------------------'''

def mode978(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode978(admin, name, printpoint)
	'''---------------------------'''

def mode979(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode979(admin, name, printpoint)
	'''---------------------------'''
	
def mode980(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode980(admin, name, printpoint)
	'''---------------------------'''

def mode981(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode981(admin, name, printpoint)
	'''---------------------------'''

def mode982(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode982(admin, name, printpoint)
	'''---------------------------'''

def mode983(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode983(admin, name, printpoint)
	'''---------------------------'''

def mode984(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode984(admin, name, printpoint)
	'''---------------------------'''

def mode985(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode985(admin, name, printpoint)
	'''---------------------------'''

def mode986(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode986(admin, name, printpoint)
	'''---------------------------'''

def mode987(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode987(admin, name, printpoint)
	'''---------------------------'''

def mode988(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode988(admin, name, printpoint)
	'''---------------------------'''

def mode989(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode989(admin, name, printpoint)
	'''---------------------------'''
	
def mode990(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = ""
	mode990(admin, name, printpoint)
	'''---------------------------'''

def mode991(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode991(admin, name, printpoint)
	'''---------------------------'''

def mode992(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode992(admin, name, printpoint)
	'''---------------------------'''

def mode993(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode993(admin, name, printpoint)
	'''---------------------------'''

def mode994(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode994(admin, name, printpoint)
	'''---------------------------'''

def mode995(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode995(admin, name, printpoint)
	'''---------------------------'''

def mode996(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode996(admin, name, printpoint)
	'''---------------------------'''

def mode997(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode997(admin, name, printpoint)
	'''---------------------------'''

def mode998(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode998(admin, name, printpoint)
	'''---------------------------'''

def mode999(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode999(admin, name, printpoint)
	'''---------------------------'''
	
	
def account_button(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, custom):
	getsetting_addon         = xbmcaddon.Addon(addon).getSetting
	setsetting_addon         = xbmcaddon.Addon(addon).setSetting
	#setsetting_custom1(addon,set1,set1v)
	printpoint = ""
	'''---------------------------'''
	if skinsetting:
		'''------------------------------
		---DIALOG-YESNO-USER+PASS--------
		------------------------------'''
		try: x1 = addonString(73).encode('utf-8') % (username.decode('utf-8'))
		except: pass
		try: x2 = addonString(73).encode('utf-8') % (username)
		except: pass
		try: x3 = addonString(73) % (username)
		except: pass
		try: x4 = addonString(73) % (username.decode('utf-8'))
		except: pass
		try: returned = dialogyesno(localize(79483), localize(79484) + '[CR]' + x1)
		except:
			try: returned = dialogyesno(localize(79483), localize(79484) + '[CR]' + x2)
			except:
				try: returned = dialogyesno(localize(79483), localize(79484) + '[CR]' + x3)
				except: returned = dialogyesno(localize(79483), localize(79484) + '[CR]' + x4)
		if returned == 'ok':
			'''------------------------------
			---DIALOG-KEYBOARD-USER----------
			------------------------------'''
			printpoint = printpoint + "1"
			if 'htpt' in username: username = ""
			returned = dialogkeyboard(username,'$LOCALIZE[20142]',0,'3',usernameS,addon)
			if returned == 'skip':
				notification_common("3")
				printpoint = printpoint + "8"
				'''---------------------------'''
			else:
				'''------------------------------
				---DIALOG-KEYBOARD-PASS----------
				------------------------------'''
				printpoint = printpoint + "2"
				returned = dialogkeyboard(password,'$LOCALIZE[15052]',1,'3',passwordS,addon)
				if returned == 'skip':
					notification(localize(257),addonString(69).encode('utf-8'),"",2000)
					printpoint = printpoint + "8"
				else:
					printpoint = printpoint + "3"
					'''---------------------------'''
		'''------------------------------
		---DIALOG-YES-NO-PERIOD----------
		------------------------------'''
		if not "8" in printpoint and skinsetting2 != "N/A":
			returned = dialogyesno(localize(79482), addonString(71).encode('utf-8') % (skinsetting2))
			if returned == 'ok':
				printpoint = printpoint + "4"
				returned, set1v = dialognumeric(0, localize(12393),skinsetting2,'2',skinsetting2S,"")
				if returned == 'skip': notification(localize(257),addonString(69).encode('utf-8'),"",2000)
				else:
					printpoint = printpoint + "5"
					
		if printpoint == "" or "8" in printpoint:
			'''------------------------------
			---DIALOG-YES-NO-TURNOFF---------
			------------------------------'''
			try: returned = dialogyesno(localize(79479), addonString(73).encode('utf-8') % (username))
			except: returned = dialogyesno(localize(79479), addonString(73) % (username))
			if returned == 'ok':
				setSkinSetting("1", skinsettingS, "false")
				setSkinSetting("0", skinsetting2S, "")
				setSkinSetting("0", skinsetting3S, "")
				setsetting_custom1(addon,usernameS,"")
				setsetting_custom1(addon,passwordS,"")
				'''---------------------------'''
			else:
				notification_common("9")
				'''---------------------------'''
				
		if ("1" in printpoint and "3" in printpoint) or ("4" in printpoint and "5" in printpoint):
			'''------------------------------
			---DIALOG-OK-ACCOUNT-EDITED------
			------------------------------'''
			xbmc.sleep(500)
			skinsetting = xbmc.getInfoLabel('Skin.HasSetting('+ skinsettingS +')')
			skinsetting2 = xbmc.getInfoLabel('Skin.String('+ skinsetting2S +')')
			username = getsetting_addon(usernameS)
			password = getsetting_addon(passwordS)
			'''---------------------------'''
			
			if name == "REALDEBRID":
				'''------------------------------
				---REALDEBRID--------------------
				------------------------------'''
				dialogok(addonString(56).encode('utf-8') % ('[COLOR=Yellow]' + name + '[/COLOR]'),addonString(73).encode('utf-8') % (username),addonString(61).encode('utf-8') % (password),addonString(71).encode('utf-8') % (skinsetting2))
				dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + localize(79485) + space2 + localize(305), localize(79604) + space2, localize(79603), localize(79602))
				set_accountdate(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, "0")
				'''---------------------------'''
				
			elif name == "SDAROT TV":
				'''------------------------------
				---SDAROT-TV---------------------
				------------------------------'''
				dialogok(addonString(56).encode('utf-8') % ('[COLOR=Yellow]' + name + '[/COLOR]'),addonString(73).encode('utf-8') % (username),addonString(61).encode('utf-8') % (password),addonString(71).encode('utf-8') % (skinsetting2))
				dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + localize(79485) + space2 + localize(305), localize(79604) + space2, addonString(87).encode('utf-8'),addonString(88).encode('utf-8'))
				set_accountdate(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, "0")
				'''---------------------------'''
			
			elif name == "TRAKT TV":
				'''------------------------------
				---TRAKT-TV----------------------
				------------------------------'''
				dialogok(addonString(56).encode('utf-8') % ('[COLOR=Yellow]' + name + '[/COLOR]'),addonString(73).encode('utf-8') % (username),addonString(61).encode('utf-8') % (password),"")
				dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + localize(79485) + space2 + localize(305), localize(79604) + space2, localize(78914), localize(78915))
				'''---------------------------'''	

	else:
		'''------------------------------
		---DIALOG-YES-NO-HAVE-ACCOUNT?---
		------------------------------'''
		returned = dialogyesno(addonString(57).encode('utf-8') % (name), localize(79481))
		if returned == 'ok':
			'''------------------------------
			---DIALOG-KEYBOARD-USER----------
			------------------------------'''
			if admin or not 'htpt' in username: input = username
			else: input = ""
			returned = dialogkeyboard(input,'$LOCALIZE[20142]',0,'3',usernameS,addon)
			if returned == 'skip': pass
			else:
				'''------------------------------
				---DIALOG-KEYBOARD-PASS----------
				------------------------------'''
				returned = dialogkeyboard(password,'$LOCALIZE[15052]',1,'3',passwordS,addon)
				if returned == 'skip': pass
				else:
					'''------------------------------
					---DIALOG-NUMERIC--PERIOD--------
					------------------------------'''
					if skinsetting2 != "N/A": returned, value = dialognumeric(0, localize(12393),"30",'2',skinsetting2S,"")
					else: returned = 'ok'
					if returned == 'skip': pass
					else:
						'''------------------------------
						---DIALOG-OK-ACCOUNT-ON-------
						------------------------------'''
						setSkinSetting("1", skinsettingS, "true")
						xbmc.sleep(500)
						skinsetting = xbmc.getInfoLabel('Skin.HasSetting('+ skinsettingS +')')
						skinsetting2 = xbmc.getInfoLabel('Skin.String('+ skinsetting2S +')')
						skinsetting3 = xbmc.getInfoLabel('Skin.String('+ skinsetting3S +')')
						username = getsetting_addon(usernameS)
						password = getsetting_addon(passwordS)
						'''---------------------------'''
						
						if name == "REALDEBRID":
							'''------------------------------
							---REALDEBRID--------------------
							------------------------------'''
							dialogok(addonString(56).encode('utf-8') % ('[COLOR=Yellow]' + name + '[/COLOR]'),addonString(73).encode('utf-8') % (username),addonString(61).encode('utf-8') % (password),addonString(71).encode('utf-8') % (skinsetting2))
							dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + localize(79485) + space2 + localize(305), localize(79604) + space2, localize(79603), localize(79602))
							set_accountdate(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, "0")
							'''---------------------------'''
							
						elif name == "SDAROT TV":
							'''------------------------------
							---SDAROT-TV---------------------
							------------------------------'''
							dialogok(addonString(56).encode('utf-8') % ('[COLOR=Yellow]' + name + '[/COLOR]'),addonString(73).encode('utf-8') % (username),addonString(61).encode('utf-8') % (password),addonString(71).encode('utf-8') % (skinsetting2))
							dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + localize(79485) + space2 + localize(305), localize(79604) + space2, addonString(87).encode('utf-8'),addonString(88).encode('utf-8'))
							set_accountdate(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, "0")
							'''---------------------------'''
						
						elif name == "TRAKT TV":
							'''------------------------------
							---TRAKT-TV----------------------
							------------------------------'''
							dialogok(addonString(56).encode('utf-8') % ('[COLOR=Yellow]' + name + '[/COLOR]'),addonString(73).encode('utf-8') % (username),addonString(61).encode('utf-8') % (password),"")
							dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + localize(79485) + space2 + localize(305), localize(79604) + space2, localize(85), localize(78915))
							'''---------------------------'''
							
			if returned == 'skip':
				'''------------------------------
				---DIALOG-NOTIFICATION-TURNOFF---
				------------------------------'''
				notification(localize(257),addonString(69).encode('utf-8'),"",2000)
				setSkinSetting("1", skinsettingS, "false")
				setSkinSetting("0", skinsetting2S, "")
				setSkinSetting("0", skinsetting3S, "")
				setsetting_custom1(addon,usernameS,"")
				setsetting_custom1(addon,passwordS,"")
				'''---------------------------'''
		else:
			'''------------------------------
			---DIALOG-OK-SIGNUP-INFO---------
			------------------------------'''
			if name == "REALDEBRID": dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + 'https://real-debrid.com/', localize(79480), '[CR]' + localize(79477),'[CR]' + localize(79476))
			elif name == "SDAROT TV": dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + 'http://sdarot.wf/', localize(79480), '[CR]' + localize(78912),'[CR]' + localize(78913))
			elif name == "TRAKT TV": dialogok('[COLOR=Yellow]' + name + '[/COLOR]' + '[CR]' + 'http://trakt.tv/', localize(79480), '[CR]' + addonString(89).encode('utf-8'),"")
			'''---------------------------'''
	
	if name == "REALDEBRID":
		'''------------------------------
		---urlresolver-------------------
		------------------------------'''
		if systemhasaddon_urlresolver: addonsettings2('script.module.urlresolver','RealDebridResolver_login',"true",'RealDebridResolver_enabled',"true",'RealDebridResolver_priority',"101",'RealDebridResolver_username',username,'RealDebridResolver_password',password)
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "account_button LV_" + printpoint + space2 + name + space + addon + space3
	'''---------------------------'''

def set_accountdate(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, custom):
	'''------------------------------
	---CALCULATE-END-DATES-----------
	------------------------------'''
	printpoint = "" ; custom1172W = xbmc.getCondVisibility('Window.IsVisible(Custom1172.xml)')
	try: numberN = int(skinsetting2)
	except: numberN = 0
	
	#try: username = username.encode('utf-8')
	#except: pass
	
	if skinsetting3 != "":
		#notification("test",skinsetting3,"",2000)
		dateleft = stringtodate(skinsetting3,'%Y-%m-%d')
		dateleft2 = str(dateleft)
		dateleft2S = str(dateleft2)
		datenow2 = stringtodate(datenowS,'%Y-%m-%d')
		number2 = dateleft - datenow2
		number2S = str(number2)
		if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
		elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
		else: number2S = "0"
		if admin: notification("number2S:" + number2S,"","",2000)
		number2N = int(number2S)
	else:
		number2S = "0"
		number2N = int(number2S)
	if number2N < 0: 
		number2S = "0"
		number2N = int(number2S)
		'''---------------------------'''
	
	if custom == "0":
		'''------------------------------
		---MANUAL-SET--------------------
		------------------------------'''
		import datetime as dt
		dateafter2 = datenow + dt.timedelta(days=numberN)
		dateafter2S = str(dateafter2)
		#setsetting(skinsetting3, dateafter2S)
		setSkinSetting("0", skinsetting3S, dateafter2S)
		'''---------------------------'''
		
		'''---------------------------'''
	if custom == "1":
		'''------------------------------
		---AUTO-SET----------------------
		------------------------------'''
		
		'''---------------------------'''
		if skinsetting2 != "" or skinsetting3 != "": setSkinSetting("0", skinsetting2S, number2S)
		'''---------------------------'''
		
		if skinsetting and (username == "" or password == ""):
			'''------------------------------
			---NO-USERNAME-OR-PASSWORD-------
			------------------------------'''
			if number2N > 0 and number2N < 7: dialogok(localize(75204) + '[CR]' + '[COLOR=Yellow]' + name + '[/COLOR]',"",addonString(73).encode('utf-8') % (username) + '[CR]' + addonString(71).encode('utf-8') % (number2S),"")
			'''---------------------------'''
			
			'''------------------------------
			---DIALOG-YESNO-REMAKE-----------
			------------------------------'''
			returned = dialogyesno(localize(75202) + space + name,localize(75206) + '[CR]' + localize(75205) + '[CR]' + addonString(73).encode('utf-8') % (username))
			if returned == "ok": printpoint = printpoint + "3"
			else: printpoint = printpoint + "4"
			'''---------------------------'''
			
		elif skinsetting and number2N < 7:
			'''------------------------------
			---PERIOD-ABOUT-TO-END-----------
			------------------------------'''
			if number2N > 0 and number2N < 7: dialogok(localize(75200) + '[CR]' + '[COLOR=Yellow]' + name + '[/COLOR]',"",addonString(73).encode('utf-8') % (username) + '[CR]' + addonString(71).encode('utf-8') % (number2S),"")
			elif skinsetting and number2N == 0: dialogok(localize(75201) + '[CR]' + '[COLOR=Yellow]' + name + '[/COLOR]',"",addonString(73).encode('utf-8') % (username) + '[CR]' + addonString(71).encode('utf-8') % (number2S),"")
			'''---------------------------'''
			
			'''------------------------------
			---DIALOG-YESNO-REMAKE-----------
			------------------------------'''
			returned = dialogyesno(localize(75202) + space + name,localize(75203) + '[CR]' + addonString(73) % (username))
			if returned == "ok": printpoint = printpoint + "5"
			else: printpoint = printpoint + "6"
			'''---------------------------'''
	
		elif not skinsetting and number2N > 0:
			'''------------------------------
			---SETTING-SHOULD-BE-ON?---------
			------------------------------'''
			pass
			
		if "3" in printpoint or "5" in printpoint:
			'''------------------------------
			---USER-SET-SETTINGS-------------
			------------------------------'''
			custom1172W = xbmc.getCondVisibility('Window.IsVisible(Custom1172.xml)')
			if not custom1172W: xbmc.executebuiltin('ActivateWindow(1172)')
			'''---------------------------'''
			count = 0
			while count < 40 and not custom1172W and not xbmc.abortRequested:
				'''------------------------------
				---custom1172W-PENDING---------
				------------------------------'''
				xbmc.sleep(40)
				count += 1
				custom1172W = xbmc.getCondVisibility('Window.IsVisible(Custom1172.xml)')
				'''---------------------------'''
				
			if custom1172W:
				'''------------------------------
				---custom1172W-TRUE------------
				------------------------------'''
				xbmc.executebuiltin('Control.SetFocus(100,1)')
				xbmc.executebuiltin('Control.SetFocus(50,1)')
				xbmc.executebuiltin('Action(PageUp)')
				xbmc.sleep(40)
				'''---------------------------'''
				count = 0
				systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
				while count < 10 and not name in systemcurrentcontrol and not xbmc.abortRequested:
					'''------------------------------
					---systemcurrentcontrol=name-----
					------------------------------'''
					count += 1
					systemcurrentcontrol = findin_systemcurrentcontrol("1",name,40,'Action(Down)',"")
					if admin: print printfirst + space + "set_accountdate" + space2 + "systemcurrentcontrol=name" + space2 + systemcurrentcontrol + " != " + name + space3
					'''---------------------------'''
			
			if name == 'REALDEBRID': account_button(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, custom)
			elif name == 'SDAROT TV': account_button(name, addon, usernameS, passwordS, username, password, skinsettingS, skinsetting2S, skinsetting3S, skinsetting, skinsetting2, skinsetting3, custom)
			'''---------------------------'''
		
		elif (custom1172W and number2N == 0) or "4" in printpoint:
			'''------------------------------
			---SETTING-OFF-------------------
			------------------------------'''
			setSkinSetting("1", skinsettingS, "false")
			setSkinSetting("0", skinsetting2S, "")
			setSkinSetting("0", skinsetting3S, "")
			notification(addonString(57).encode('utf-8') % (name) + space + str79046.encode('utf-8'),"","",4000)
			'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and custom == "1": print printfirst + "set_accountdate_LV" + printpoint + space + "name" + space2 + name + space + skinsetting + space + skinsetting2 + space + "number2N" + space2 + str(number2N) + space + "custom" + space2 + str(custom)
	'''---------------------------'''

def setAutoSettings(custom, addonid2=""):
	
	countrystr = xbmc.getInfoLabel('Skin.String(Country)')
	
	if custom == "0":
		'''------------------------------
		---INSTALL-ADDONS----------------
		------------------------------'''
		if scripthtptinstall_Skin_Installed == "true": notification("Installing additional addons", "Please Wait!", "", 10000)
		addon = 'plugin.video.pulsar'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and 1 + 1 == 3:
			'''------------------------------
			---plugin.video.pulsar-----------
			------------------------------'''
			#addonsettings2(addon,'max_upload_rate',"",'max_download_rate',"",'',"",'',"",'',"")
			'''---------------------------'''
			
			#addon = 'script.pulsar.btjunkie-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			addon = 'script.pulsar.KickAssTorrents'
			if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				installaddon(admin, addon, "", update=False)
				if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): notification("Provider Installed!", addon, "", 2000)
			#addon = 'script.pulsar.extratorrent-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.omg'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.yourbittorrent-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.torrenthound-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			addon = 'script.pulsar.yify-mc'
			if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				installaddon(admin, addon, "", update=False)
				if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): notification("Provider Installed!", addon, "", 2000)
			addon = 'script.pulsar.thepiratebay-mc'
			if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				installaddon(admin, addon, "", update=False)
				if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): notification("Provider Installed!", addon, "", 2000)
			#addon = 'script.pulsar.publichd-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.magnetdl-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.oldpiratebay-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.kickass-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.h33t-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.eztv-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			#addon = 'script.pulsar.torrentz-mc'
			#if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
			'''---------------------------'''
		else: pass #installaddon(admin, addon, "")
		
		addon = 'service.htpt.debug'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, "", update=False)
		
		addon = 'script.htpt.refresh'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, "", update=False)
		
		addon = 'script.htpt.remote'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, "", update=False)
			
		addon = 'script.htpt.smartbuttons'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, "", update=False)
		
		addon = 'service.htpt.fix'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon2(admin, addon, "", update=False)
		
		addon = 'script.htpt.widgets'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			addonsettings2(addon,'plot_enable',"true",'recommended_enable',"true",'randomitems_enable',"true",'randomitems_method',"1",'randomitems_seasonfolders',"false")
			addonsettings2(addon,'randomitems_time',"60",'randomitems_unplayed',"true",'recentitems_enable',"true",'recentitems_homeupdate',"false",'recentitems_unplayed',"true")
			setsetting_custom1(addon, 'recommended_enable', "true")
			'''---------------------------'''
		else: installaddon2(admin, addon, "", update=False)
				
		
		addon = 'metadata.universal'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon):
			printpoint3 = installaddonP(admin, addon)
			if "9" in printpoint3:
				pass
				#notification("Trying to Install addon.", "You may want to reboot if failed!", "", 10000)
				#installaddon(admin, addon, "") ; xbmc.sleep(1000)
				'''---------------------------'''
		
		addon = 'script.favourites'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "", update=False)
		
		if xbmc.getCondVisibility('System.HasAddon(service.openelec.settings)') and not systemplatformwindows:
			addon = 'repository.unofficial.addon.pro'
			if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') and not os.path.exists(os.path.join(addons_path, addon)): installaddon(admin, addon, "", update=False)
		
		
		addon = 'service.subtitles.opensubtitles'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(os.path.join(addons_path, addon)):
			'''------------------------------
			-service.subtitles.opensubtitles-
			------------------------------'''
			#if not id40str: addonsettings2(addon,'OSuser',idstr + "@gmail.com",'OSpass',idpstr,'',"",'',"",'',"")
			path = os.path.join(addondata_path, addon, 'temp', '')
			removefiles(path)
			'''---------------------------'''
		elif not xbmc.getCondVisibility('System.HasAddon('+ addon +')') and not os.path.exists(os.path.join(addons_path, addon)): installaddon(admin, addon, "", update=False)
		
		addon = 'metadata.tvdb.com'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') and not os.path.exists(os.path.join(addons_path, addon)): installaddon(admin, addon, "", update=False)
			
		addon = 'service.subtitles.subscenter'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(os.path.join(addons_path, addon)):
			path = os.path.join(addondata_path, addon, 'temp', '')
			removefiles(path)
			'''---------------------------'''
		elif not xbmc.getCondVisibility('System.HasAddon('+ addon +')') and not os.path.exists(os.path.join(addons_path, addon)):
			if countrystr == "Israel": installaddon(admin, addon, "", update=False)
		
		addon = 'service.subtitles.torec'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(os.path.join(addons_path, addon)):
			path = os.path.join(addondata_path, addon, 'temp', '')
			removefiles(path)
			'''---------------------------'''
		elif not xbmc.getCondVisibility('System.HasAddon('+ addon +')') and not os.path.exists(os.path.join(addons_path, addon)):
			if countrystr == "Israel": installaddon(admin, addon, "", update=False)
		
		addon = 'service.subtitles.subtitle'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(os.path.join(addons_path, addon)):
			'''------------------------------
			---service.subtitles.subtitle----
			------------------------------'''
			#if not id40str and not systemplatformwindows: addonsettings2(addon,'SUBemail',idstr + "@gmail.com",'SUBpassword',idpstr,'',"",'',"",'',"")
			path = os.path.join(addondata_path, addon, 'cookiejar.txt')
			removefiles(path)
			path = os.path.join(addondata_path, addon, 'temp', '')
			removefiles(path)
			'''---------------------------'''
		elif not xbmc.getCondVisibility('System.HasAddon('+ addon +')') and not os.path.exists(os.path.join(addons_path, addon)):
			if countrystr == "Israel": installaddon(admin, addon, "", update=False)
		
		if 1 + 1 == 3:
			addon = 'script.tv.show.next.aired'
			if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				'''------------------------------
				---script.tv.show.next.aired-----
				------------------------------'''
				xbmc.executebuiltin('RunScript(script.tv.show.next.aired,silent=True)')
				xbmc.executebuiltin('RunScript(script.tv.show.next.aired,backend=True)')
				addonsettings2(addon,'',"",'',"",'',"",'',"",'',"")
				'''---------------------------'''
			else:
				pass
				'''---------------------------'''
			
		dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		while dialogtextviewerW and not xbmc.abortRequested:
			xbmc.sleep(1000)
			dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
			'''---------------------------'''
		set_accountdate('REALDEBRID','plugin.video.genesis', 'realdedrid_user', 'realdedrid_password', realdedrid_user, realdedrid_password, 'Account1_Active', 'Account1_Period', 'Account1_EndDate', Account1_Active, Account1_Period, Account1_EndDate, "1")
		set_accountdate('SDAROT TV','plugin.video.sdarot.tv', 'username', 'user_password', sdarottv_user, sdarottv_password, 'Account2_Active', 'Account2_Period', 'Account2_EndDate', Account2_Active, Account2_Period, Account2_EndDate, "1")
		'''---------------------------'''
	
	elif custom == "1":
		pass
	
	elif custom == "3":
		'''------------------------------
		---SETTING-ADDONS-BY-COUNTRY-----
		------------------------------'''
		libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
		if libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
		
		addon = 'metadata.universal'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				if countrystr == "Israel":
					addonsettings2(addon,'imdbsearchlanguage',"he-il",'tmdbplotlanguage',"he",'tmdbsetlanguage',"he",'tmdbtaglinelanguage',"he",'tmdbthumblanguage',"he")
					addonsettings2(addon,'tmdbtitlelanguage',"he",'',"",'imdbakatitles',"Israel",'tmdbgenreslanguage',"he",'',"")
					'''---------------------------'''
				elif countrystr == "": pass
				elif "Foreign" in countrystr:
					addonsettings2(addon,'imdbsearchlanguage',"None",'tmdbplotlanguage',"en",'tmdbsetlanguage',"en",'tmdbtaglinelanguage',"en",'tmdbthumblanguage',"en")
					addonsettings2(addon,'tmdbtitlelanguage',"None",'',"",'imdbakatitles',"Keep Original",'tmdbgenreslanguage',"en",'',"")
					'''---------------------------'''
				addonsettings2(addon,'TrailerQ',"1080p",'countrysource',"themoviedb.org",'creditssource',"themoviedb.org",'fanarttvfanart',"true",'imdbcertcountry',"USA")
				addonsettings2(addon,'imdbthumbs',"true",'plotsource',"themoviedb.org",'studiosource',"themoviedb.org",'taglinesource',"themoviedb.org",'titlesource',"themoviedb.org")
				addonsettings2(addon,'tmdbtags',"themoviedb.org",'trakttvtrailer',"true",'',"",'',"",'tmdbtrailerlanguage',"en")
				
		addon = 'metadata.tvdb.com'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon):
			if addonid2 == "" or addonid2 == addon:
				if countrystr == "Israel": setsetting_custom1(addon, 'language',"he")
				elif countrystr == "": pass
				elif "Foreign" in countrystr: setsetting_custom1(addon, 'language',"en")
				addonsettings2(addon,'RatingS',"IMDb",'absolutenumber',"false",'dvdorder',"false",'fallback',"true",'fanart',"true")
				'''---------------------------'''
			
		addon = 'metadata.themoviedb.org'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon):
			if addonid2 == "" or addonid2 == addon:
				if countrystr == "Israel": setsetting_custom1(addon, 'language',"he")
				elif countrystr == "": pass
				elif "Foreign" in countrystr: setsetting_custom1(addon, 'language',"en")
				addonsettings2(addon,'certprefix',"Rated",'fanart',"true",'keeporiginaltitle',"false",'tmdbcertcountry',"us",'trailer',"true")
				addonsettings2(addon,'RatingS',"IMDb",'TrailerQ',"1080p",'',"",'',"",'',"")
				'''---------------------------'''
		
		addon = 'plugin.video.youtube'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				if countrystr == "Israel": setsetting_custom1(addon, 'youtube.language',"iw-IL")
				elif countrystr == "": pass
				elif "Foreign" in countrystr: setsetting_custom1(addon, 'youtube.language',"en-US")
				addonsettings2(addon,'kodion.view.override',"true",'kodion.video.quality',"4",'kodion.view.default',"50",'kodion.view.episodes',"58",'kodion.search.size',"4")
				addonsettings2(addon,'kodion.setup_wizard',"false",'youtube.folder.disliked_videos.show',"false",'',"",'kodion.fanart.show',"false",'youtube.folder.sign.in.show',"true")
				addonsettings2(addon,'kodion.content.max_per_page',"7",'',"",'',"",'',"",'',"")
				path = os.path.join(addondata_path, addon, 'kodion', 'cache.sqlite')
				removefiles(path)
				'''---------------------------'''
		
		addon = 'plugin.video.sdarot.tv'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				addonsettings2(addon,'DEBUG',"false",'cache',"24",'domain',"http://www.sdarot.wf",'',"",'',"")
				path = os.path.join(addondata_path, 'plugin.video.sdarot.tv', 'sdarot-cookiejar.txt')
				removefiles(path)
				'''---------------------------'''
		
		addon = 'weather.yahoo'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			getsetting_weatheryahoo         = xbmcaddon.Addon(addon).getSetting
			setsetting_weatheryahoo         = xbmcaddon.Addon(addon).setSetting
			'''---------------------------'''
			weatheryahoo_location1 = getsetting_weatheryahoo('Location1')
			weatheryahoo_location1id = getsetting_weatheryahoo('Location1id')
			weatheryahoo_location2 = getsetting_weatheryahoo('Location2')
			weatheryahoo_location2id = getsetting_weatheryahoo('Location2id')
			weatheryahoo_location3 = getsetting_weatheryahoo('Location3')
			weatheryahoo_location3id = getsetting_weatheryahoo('Location3id')
			'''---------------------------'''
			if weatheryahoo_location1 == "" and weatheryahoo_location1id == "":
				setsetting_custom1(addon,'Location1',"Tel Aviv (IL)")
				setsetting_custom1(addon,'Location1id',"1968212")
				'''---------------------------'''
			elif weatheryahoo_location2 == "" and weatheryahoo_location2id == "":
				if countrystr == "Israel":
					setsetting_custom1(addon,'Location2',"Haifa (IL)")
					setsetting_custom1(addon,'Location2id',"2345794")
					'''---------------------------'''
				else: pass
			elif weatheryahoo_location3 == "" and weatheryahoo_location3id == "":
				if countrystr == "Israel":
					setsetting_custom1(addon,'Location3',"")
					setsetting_custom1(addon,'Location3id',"")
					'''---------------------------'''
				else: pass
				
		addon = 'plugin.video.vdubt'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				addonsettings2(addon,'parental',"true",'sort',"false",'auto-view',"true",'default',"50",'movies',"50")
				'''---------------------------'''
		
		addon = 'plugin.video.israelive'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				if sgbpvrmanagerenabled: addonsettings2(addon,'autoIPTV',"0",'useIPTV',"true",'',"",'',"",'',"")
				else: addonsettings2(addon,'autoIPTV',"1",'useIPTV',"false",'',"",'',"",'',"")
				addonsettings2(addon,'',"",'useEPG',"true",'StreramProtocol',"1",'forceRemoteDefaults',"true",'StreramsMethod',"0")
				addonsettings2(addon,'catColor',"chartreuse",'useEPG',"true",'chColor',"yellow",'prColor',"floralwhite",'timesColor',"none")
				#setsetting_custom1(addon,remoteSettingsUrl,"")
				'''---------------------------'''
				
	elif custom == "4":
		'''------------------------------
		---SETTING-GENERAL-ADDONS--------
		------------------------------'''
		
		addon = 'plugin.video.bestofyoutube_com'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				addonsettings2(addon,'filter',"true",'filterRating',"90",'filterThreshold',"40",'forceViewMode',"true",'viewMode',"58")
				'''---------------------------'''
		
		addon = 'screensaver.picture.slideshow'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				'''------------------------------
				--screensaver.picture.slideshow--
				------------------------------'''
				addonsettings2(addon,'cache',"false",'create',"",'date',"",'effect',"2",'iptc',"false")
				addonsettings2(addon,'label',"0",'level',"100",'music',"false",'scale',"false",'random',"true")
				addonsettings2(addon,'type',"0",'path',"",'',"",'',"",'time',"10")
				'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "setAutoSettings" + space + "custom" + space2 + custom + space + "addonid2" + space2 + str(addonid2)
	'''---------------------------'''


def setSubHisotry(admin, DialogSubtitles, DialogSubtitles2):
	dialogsubtitlesna1 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA1)')
	dialogsubtitlesna2 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA2)')
	dialogsubtitlesna3 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA3)')
	dialogsubtitlesna4 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA4)')
	dialogsubtitlesna5 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA5)')
	dialogsubtitlesna6 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA6)')
	dialogsubtitlesna7 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA7)')
	dialogsubtitlesna8 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA8)')
	dialogsubtitlesna9 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA9)')
	dialogsubtitlesna10 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA10)')
	
	if DialogSubtitles2 != "":
		if dialogsubtitlesna1 == "": setSkinSetting("0",'DialogSubtitlesNA1',DialogSubtitles2)
		elif dialogsubtitlesna2 == "": setSkinSetting("0",'DialogSubtitlesNA2',DialogSubtitles2)
		elif dialogsubtitlesna3 == "": setSkinSetting("0",'DialogSubtitlesNA3',DialogSubtitles2)
		elif dialogsubtitlesna4 == "": setSkinSetting("0",'DialogSubtitlesNA4',DialogSubtitles2)
		elif dialogsubtitlesna5 == "": setSkinSetting("0",'DialogSubtitlesNA5',DialogSubtitles2)
		elif dialogsubtitlesna6 == "": setSkinSetting("0",'DialogSubtitlesNA6',DialogSubtitles2)
		elif dialogsubtitlesna7 == "": setSkinSetting("0",'DialogSubtitlesNA7',DialogSubtitles2)
		elif dialogsubtitlesna8 == "": setSkinSetting("0",'DialogSubtitlesNA8',DialogSubtitles2)
		elif dialogsubtitlesna9 == "": setSkinSetting("0",'DialogSubtitlesNA9',DialogSubtitles2)
		elif dialogsubtitlesna10 == "": setSkinSetting("0",'DialogSubtitlesNA10',DialogSubtitles2)
	
	xbmc.sleep(1000)
	setCurrent_Subtitle(admin)
	'''---------------------------'''

def setCurrent_Subtitle(admin):
	dialogsubtitles2 = xbmc.getInfoLabel('Skin.String(DialogSubtitles2)')
	dialogsubtitlesna1 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA1)')
	dialogsubtitlesna2 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA2)')
	dialogsubtitlesna3 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA3)')
	dialogsubtitlesna4 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA4)')
	dialogsubtitlesna5 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA5)')
	dialogsubtitlesna6 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA6)')
	dialogsubtitlesna7 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA7)')
	dialogsubtitlesna8 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA8)')
	dialogsubtitlesna9 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA9)')
	dialogsubtitlesna10 = xbmc.getInfoLabel('Skin.String(DialogSubtitlesNA10)')
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
	addon = 'script.htpt.refresh'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		getsetting_scripthtptrefresh       = xbmcaddon.Addon(addon).getSetting
		'''---------------------------'''
		scripthtptrefresh_Current_Subtitle = getsetting_scripthtptrefresh('Current_Subtitle')
		'''---------------------------'''
	else:
		scripthtptrefresh_Current_Subtitle = ""
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + space + "setCurrent_Subtitle" + space2 + scripthtptrefresh_Current_Subtitle + space + "(" + dialogsubtitles2 + ")"
	'''---------------------------'''
	