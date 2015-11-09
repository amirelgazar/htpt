# -*- coding: utf-8 -*-
#/usr/bin/python
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
	xbmc.executebuiltin('ToggleDebug')
	
	#notification(xbmc.getInfoLabel('$VAR[label77_91]'),"1","",1000)
	
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
	
	#print filtered
	
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
	#label70_90 = xbmc.getInfoLabel('$VAR[label70_90]')
	#ReloadSkin(admin) ; xbmc.sleep(4000)
	if 1 + 1 == 3:
		from variables2 import label77_91, action77_90
		print 'label77_91' + space2 + xbmc.getInfoLabel('$VAR[label77_91]')
		print 'label77_91_' + space2 + label77_91
		
		print 'action77_90' + space2 + xbmc.getInfoLabel('$VAR[action77_90]')
		print 'action77_90_' + space2 + action77_90
	
	#print 'icon77_90' + space2 + str(xbmc.getInfoLabel('$VAR[icon77_90]'))
	#print 'icon77_90_' + space2 + icon77_90
	
	if 1 + 1 == 3:
		from variables2 import *
		xbmc.sleep(1000)
		
		#label84_91 = xbmc.getInfoLabel('$VAR[label84_91]')
		print 'label84_91 ' + label84_91
		print 'label70_90 ' + label70_90
		print 'label70 ' + label70
		
		print 'label_T: ' + str(label_T)
		for x in label_T:
			if x != "" and not 'label' in x: print str(x)
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
	#terminal('adb shell am force-stop org.xbmc.kodi && sleep 1','test')
	#infile = os.path.join('etc','proftpd','proftpd.conf')
	#read_from_file(infile, silent=True, lines=False)
	#output = terminal('ping','test')
	#xbmc.executebuiltin('Action(Quit)')
	#xbmc.executebuiltin('Quit')
	#output = terminal("chmod +x /storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/",'chmod +x')
	#output = terminal('ping en.wikipedia.org -n 1',"Connected")
	#output = call('adb shell am force-stop org.xbmc.kodi', shell=True)
	#print "output: " + str(output)
	
	#copyfiles(os.path.join(htptservicecopy_path,'manual','advancedsettings.xml'), userdata_path)
	#print output
	#killall(admin, custom="1")
	#source = htptservicecopy_path
	#target = userdata_path

	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=15&value='+source+'|'+target+')')
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=15&value=123)')
	#xbmc.executebuiltin('Quit')
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=15&value='+source+'|'+target+')')
	#killall(admin, custom="1")
	#path = os.path.join(htptservicecopy_path,'manual','advancedsettings.xml')
	#removefiles(path)
	#Clean_Library('1')
	#output = terminal('echo 123','')
	#bash_count(packages_path, level=0)
	#write_to_file(guikeepertxt_file, 'killall -9 kodi.bin', append=False, silent=True , utf8=False) ; xbmc.sleep(20000)
	#write_to_file(guikeepertxt_file, '', append=False, silent=True , utf8=False)
	#os.system('sh '+guikeepersh_file+'')
	#installaddonP(admin, 'script.module.requests')
	#killall(admin, custom="f1")
	#terminal('cp -rf /storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/userdata/addon_data/skin.htpt/userdata/Skin_SaveDesign1.txt /storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/userdata/guisettings.xml','')
	#xbmcexe_path = os.path.join(xbmc_path, 'Kodi.exe')
	#if os.path.exists(xbmcexe_path): xbmcexe_path = '"' + xbmcexe_path + '"'
	#print xbmcexe_path
	#removeaddons(['service.subtitles.torec'],"1")
	#from variables2 import *
	notification('test',str(output),'',2000)
	
	guisettings_file_ = read_from_file(guisettings4_file, silent=True)
	x = 'groupmoviesets' #GROUP MOVIES IN SETS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings4_file,old_word,new_word,guisettings_file_)
	else: notification('ohhh','','',2000)
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
	---SubtitleButton_Country--------
	------------------------------'''
	videoplayersubtitleslanguage = xbmc.getInfoLabel('VideoPlayer.SubtitlesLanguage') ; videoplayersubtitleslanguage_ = ""
	if videoplayersubtitleslanguage != "":
		len_ = len(videoplayersubtitleslanguage)
		if str(len_) != '2':
			if str(len_) == '3':
				videoplayersubtitleslanguage_ = videoplayersubtitleslanguage[:-1]
				
		xbmc.executebuiltin('SetProperty(SubtitleButton.Country,'+videoplayersubtitleslanguage_+',home)')
		'''---------------------------'''
	if admin: print printfirst + name + "_LV" + printpoint + space + "videoplayersubtitleslanguage" + space2 + str(videoplayersubtitleslanguage) + space + "videoplayersubtitleslanguage_" + space2 + str(videoplayersubtitleslanguage_)
	
def mode14(admin, name, printpoint):
	'''------------------------------
	---setUser_Name------------------
	------------------------------'''
	returned = dialogkeyboard(scripthtptdebug_User_Name,localize(1014),0,"",'User_Name',"")
	if returned != 'skip':
		setsetting_custom1('service.htpt.debug','User_Name',str(returned))
		'''---------------------------'''
	
def mode15(value, admin, name, printpoint):
	'''------------------------------
	---CopyFiles-Tweak---------------
	------------------------------'''
	source = "" ; target = ""
	if '|' in value:
		source = find_string(value, "", '|')
		source = source.replace('|',"")
		target = find_string(value, '|', "")
		target = target.replace('|',"")

		copyfiles(source, target, chmod="", mount=False)
		
	else: pass
	
	if admin: print printfirst + name + "_LV" + printpoint + newline + 'source' + space2 + str(source) + newline + 'target' + space2 + str(target)
	
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
	pass

def mode38(admin, name, printpoint):
	'''------------------------------
	---TOGGLE-ADULT-BUTTON-----------
	------------------------------'''
	from variables2 import *
	y = idT2.get('89')
	notification('test',str(y),'',2000)
	y_ = xbmc.getCondVisibility('Skin.HasSetting(off'+str(y)+')') #Adult
	if not y_:
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
	else: setSkinSetting("1",'Adult2',"false")
	
	if 1 + 1 == 3:
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
				xbmc.executebuiltin('RunScript(script.htpt.emu,,?mode=7)')
				xbmc.sleep(1000)
				xbmc.executebuiltin('Action(PageDown)')
				'''---------------------------'''

def mode39(admin, name, printpoint):
	'''------------------------------
	---Reset-Network-Settings--------
	------------------------------'''
	'''tweak and reload the network adapters'''
	xbmc.executebuiltin('Notification([COLOR Red] $VAR[CurrentMAC][/COLOR] $LOCALIZE[79061],$LOCALIZE[79062],5000)')
	if systemplatformandroid: pass
	elif systemplatformwindows:
		output = terminal('ipconfig /renew', 'ipconfig /renew')
		dialogok(name, output, "", "")
	else:
		os.system('sh /storage/.kodi/addons/skin.htpt/specials/scripts/resetnetwork.sh')
		xbmc.sleep(1000)
		oewindow("Network")
		'''---------------------------'''
		
def mode40(value, admin, name, printpoint):
	'''------------------------------
	---Reset-Skin-Settings-----------
	------------------------------'''
	extra2 = "" ; TypeError = ""
	if value == '0': printpoint = printpoint + '1'
	elif value == '1':
		returned = dialogyesno(localize(74554) , localize(74556))
		if returned == 'ok': printpoint = printpoint + '1' ; xbmc.executebuiltin('Dialog.Close(1173)')
	
	if printpoint == '1':
		'''------------------------------
		---DELETE-USER-FILES-------------
		------------------------------'''
		pass
		#Clean_Library("10")
		#Clean_Library("11")
		#Clean_Library("12")
		#Clean_Library("13")
	
	if printpoint == '1':
		xbmc.executebuiltin('Skin.ResetSettings') ; xbmc.sleep(500)
		Custom1000(name,1,'This action may take a while.. be patient!',30)
		if playerhasmedia: xbmc.executebuiltin('Action(Stop)')
		
		#ReloadSkin(admin) ; xbmc.sleep(500)
		
		
		'''------------------------------
		---Apply-USER-IDS----------------
		------------------------------'''
		setSkinSetting5("0",'User_ID',idstr,'ID1',id1str,'ID2',id2str,'ID3',id3str,'ID4',id4str)
		setSkinSetting5("0",'ID5',id5str,'ID6',id6str,'ID7',id7str,'ID8',id8str,'ID9',id9str)
		setSkinSetting5("0",'ID10',id10str,'ID11',id11str,'ID12',id12str,'',"",'',"")
		setSkinSetting5("0",'MAC',macstr,'MAC1',mac1str,'MAC2',mac2str,'',"",'',"")
		setSkinSetting5("0",'',"",'',"",'TrialDate',trialdate,'TrialDate2',trialdate2,'Country',countrystr)
		setSkinSetting5("1",'Admin3',admin3,'',"",'',"",'SkinReset',"true",'',"")
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
		setSkinSetting5("1",'off89',"true",'',"",'',"",'',"",'',"") #HOMEBUTTONS
		'''---------------------------'''
		
		'''------------------------------
		---Widgets-----------------------
		------------------------------'''
		
		'''---------------------------'''
		#from variables2 import *
		count = 0

		'''------------------------------
		---performance-------------------
		------------------------------'''
		listL = ["C", "D"]
		#if id10str in listL: setSkinSetting("1",'Performance',"true")
		'''---------------------------'''
		#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=219&value=25)')
		#mode219('25', admin, name, printpoint)
		#xbmc.executebuiltin('Action(Back)')
		
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
	
	if printpoint == '1':
		xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=215&value=RESET)') ; xbmc.sleep(7000)
		xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(500) ; customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
		if not customhomecustomizerW: xbmc.executebuiltin('ActivateWindow(1171)')

	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + extra2
			
def mode41(admin, name, printpoint):
	'''------------------------------
	---Network-Settings--------------
	------------------------------'''
	if systemplatformandroid: terminal('am start -a android.intent.action.MAIN -n com.android.settings/.Settings',name)
	elif systemplatformwindows: terminal('rundll32.exe van.dll,RunVAN',name)
	else: oewindow('Network')
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
	setsetting_custom1('service.htpt.debug','General_ScriptON',"true")
	setsetting_custom1('service.htpt.debug','ModeOn_7',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_7',datenowS + "__" + timenow2S)
	custom = 'f1'
	killall(admin, custom)
	'''---------------------------'''

def mode51(admin, name, printpoint):
	'''------------------------------
	---RESTART-----------------------
	------------------------------'''
	setsetting_custom1('service.htpt.debug','General_ScriptON',"true")
	setsetting_custom1('service.htpt.debug','ModeOn_8',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_8',datenowS + "__" + timenow2S)
	custom = 'r1'
	killall(admin, custom)
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
	setsetting_custom1('service.htpt.debug','ModeOn_10',"true")
	setsetting_custom1('service.htpt.debug','ModeTime_10',datenowS + "__" + timenow2S)
	notification(startupmessage2,id1str,"",5000)
	custom = 's1'
	killall(admin, custom)
	'''---------------------------'''

def mode54(admin, name, printpoint):
	'''------------------------------
	---QUIT--------------------------
	------------------------------'''
	custom = 'q1'
	xbmc.sleep(500)
	killall(admin, custom)
	#notification(startupmessage2,id1str,"",5000)
	'''---------------------------'''


def mode55(value, admin, admin3, name, printpoint, LibraryData_RemoteMoviesFiles, LibraryData_RemoteTvshowsFiles):
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
		if admin:
			print printfirst + "LibraryData" + space + "Afolders_count2" + space2 + Afolders_count2 + space + "Bfolders_count2" + space2 + Bfolders_count2 + newline + \
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
			if not librarydataautoupdate or scripthtptinstall_Skin_FirstBoot == "true" or scripthtptinstall_Skin_Installed == "true" or not libraryhascontentmovies or not libraryhascontenttvshows:
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
			elif librarydataautoupdate: notification(localize(79577), localize(16039), "", 2000)
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
		xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=215&value=RESET)')
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
	mode110(admin, name, printpoint)
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
	
def mode200(value, admin, name, printpoint):
	'''------------------------------
	---DIALOG-SELECT-(10-100)--------
	------------------------------'''
	extra = "" ; TypeError = "" ; value2 = "" ; returned = ""
	list = ['-> (Exit)', 'default', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
	
	if value != "":
		try:
			test = xbmc.getInfoLabel('Skin.String('+value+')')
			if test != None: printpoint = printpoint + "1"
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	else: pass
	
	if "1" in printpoint:
		returned, value2 = dialogselect('$LOCALIZE[74433]',list,0)
	
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
		if "7" in printpoint:
			if value2 == 'default': setSkinSetting('0', str(value), "")
			elif value2 != "": setSkinSetting('0', str(value), value2)
			else: printpoint = printpoint + "8"
			
			if not "8" in printpoint:
				notification(".","","",1000)
				xbmc.sleep(200)
				xbmc.executebuiltin('Action(Back)')
				xbmc.sleep(200)
				ReloadSkin(admin)
	
	if admin: print printfirst + name + "_LV" + printpoint + space + "list" + space2 + str(list) + space + "returned" + space2 + str(returned) + space + "value" + space2 + str(value) + space + "value2" + space2 + str(value2) + extra
	'''---------------------------'''

def Custom1000(title="", progress="", comment="", autoclose=""):
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	if libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
	xbmc.executebuiltin('SetProperty(1000title,'+title+',home)')
	xbmc.executebuiltin('SetProperty(1000progress,'+str(progress)+',home)')
	xbmc.executebuiltin('SetProperty(1000comment,'+comment+',home)')
	custom1000W = xbmc.getCondVisibility('Window.IsVisible(Custom1000.xml)')
	xbmc.executebuiltin('Dialog.Close(all,true)')
	if not custom1000W:
		notification_common("2")
		xbmc.executebuiltin('ActivateWindow(1000)') ; xbmc.sleep(100)
	
	if autoclose != "": xbmc.executebuiltin('AlarmClock(timeout,Action(Back),'+str(autoclose)+',silent)')
	
	
	if admin and not admin2: print printfirst + 'Custom1000' + space + 'title' + space2 + str(title)
	
def getRandomColors(admin):
	#colors_file = os.path.join(skin_path, 'media', 'buttons', 'colors', 'colors.xml')
	#infile_colors_ = read_from_file(colors_file, silent=True)
	
	returned, value1 = getRandom("0", min=0, max=70, percent=50)
	returned, value2 = getRandom("0", min=0, max=70, percent=50)
	returned, value3 = getRandom("0", min=0, max=70, percent=50)
	returned, value4 = getRandom("0", min=0, max=70, percent=50)
	returned, value5 = getRandom("0", min=0, max=70, percent=50)
	listL = [value1, value2, value3, value4, value5]
	count = 0
	for value in listL:
		count += 1
		if value > 0 and value <= 5: value = '' ; value_ = ""
		elif value > 5 and value <= 10: value = 'ff000000' ; value_ = 'black'
		elif value > 10 and value <= 15: value = 'ff00a693' ; value_ = 'persian green'
		elif value > 15 and value <= 20: value = 'ff00cccc' ; value_ = 'robin egg blue'
		elif value > 20 and value <= 25: value = 'ffffc40c' ; value_ = 'mikado yellow'
		elif value > 25 and value <= 30: value = 'ff00ffff' ; value_ = 'aqua'
		elif value > 30 and value <= 35: value = 'ff1e4d2b' ; value_ = 'cal poly pomona green'
		elif value > 35 and value <= 40: value = 'ff2f4f4f' ; value_ = 'dark slate gray'
		elif value > 40 and value <= 45: value = 'ff4cbb17' ; value_ = 'kelly green'
		elif value > 45 and value <= 50: value = 'ff5d8aa8' ; value_ = 'air force blue'
		elif value > 50 and value <= 55: value = 'ff8b4513' ; value_ = 'saddle brown'
		elif value > 55 and value <= 60: value = 'ff89cff0' ; value_ = 'baby blue'
		elif value > 60 and value <= 65: value = 'fff5f5f5' ; value_ = 'white smoke'
		elif value > 65 and value <= 70: value = 'ffffd1dc' ; value_ = 'pastel pink'
		
		if count == 1: value1 = value ; value1_ = value_
		elif count == 2: value2 = value ; value2_ = value_
		elif count == 3: value3 = value ; value3_ = value_
		elif count == 4: value4 = value ; value4_ = value_
		elif count == 5: value5 = value ; value5_ = value_
	
	return value1, value1_, value2, value2_, value3, value3_, value4, value4_, value5, value5_
			
def mode201(value, admin, name, printpoint):
	'''------------------------------
	---RESET-TO-DEFAULT--------------
	------------------------------'''
	#from variables2 import *
	returned = ""
	container50hasfocus390 = xbmc.getCondVisibility('Container(50).HasFocus(390)') #BUTTONS
	
	if container50hasfocus390:
		list = ['-> (Exit)', localize(10035) + space + "(" + localize(593) + ")", localize(590) + space + "(" + localize(593) + ")", \
		localize(74840) + space + "(" + localize(78219) + ")", localize(74840) + space + localize(590) + space + "(" + localize(78219) + ")", \
		localize(74840) + space + "(" + localize(593) + ")", localize(74840) + space + localize(590) + space + "(" + localize(593) + ")", \
		localize(10035) + space + localize(78215) + space + "(" + localize(593) + ")", localize(10035) + space + localize(78215) + space + localize(590) + space + "(" + localize(593) + ")", \
		localize(10035) + space + "(" + localize(74614) + ")"]
	else: list = []
	
	if list != []:
		returned, value_ = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
		
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
		elif returned == 9: printpoint = printpoint + "I" #RESET BUTTONS PROPERTIES
		
		from variables2 import labelT, list1, list0, list0c, list0c2, list0o
		xbmc.executebuiltin('SetProperty(TEMP,'+name+',home)')
		xbmc.executebuiltin('SetProperty(TEMP2,This action may take a while be patient!,home)')
		xbmc.executebuiltin('Dialog.Close(1173)') ; xbmc.sleep(100) ; xbmc.executebuiltin('ActivateWindow(1000)') ; notification_common("2") ; xbmc.sleep(100)
		'''---------------------------'''
		
	if "A" in printpoint:
		Custom1000(name,20,str(list[returned]),20)
		xbmc.executebuiltin('SetProperty(1000title,'+name+',home)')
		xbmc.executebuiltin('SetProperty(1000comment,This action may take a while be patient!,home)')
		for x in list0: setSkinSetting('0',x,"")
		for x in list1: setSkinSetting('1',x,"false")
		'''---------------------------'''
	
	if "B" in printpoint:
		Custom1000(name,30,str(list[returned]),20)
		for x in list1:
			returned1, value1 = getRandom("0", min=0, max=100, percent=50)
			if returned1 == 'ok': value1 = "true"
			else: value1 = "false"
			setSkinSetting('1',x,value1)
		
	if "C" in printpoint:
		Custom1000(name,40,str(list[returned]),20)
		'''RESET-BUTTONS-COLORS'''
		for i in range(70,129):
			setSkinSetting('0','color'+str(i),"")
			setSkinSetting('0','color'+str(i)+'.name',"")
			'''---------------------------'''
	
	if "D" in printpoint:
		Custom1000(name,50,str(list[returned]),20)
		value1, value1_, value2, value2_, value3, value3_, value4, value4_, value5, value5_ = getRandomColors(admin)
		for i in range(70,129):
			x = labelT.get('label'+str(i))
			if x != "":
				returned, count = getRandom("0", min=1, max=5, percent=50)
				if count == 1: value = value1 ; value_ = value1_
				elif count == 2: value = value2 ; value_ = value2_
				elif count == 3: value = value3 ; value_ = value3_
				elif count == 4: value = value4 ; value_ = value4_
				elif count == 5: value = value5 ; value_ = value5_
				setSkinSetting('0','color'+str(i),value)
				setSkinSetting('0','color'+str(i)+'.name',value_)
				'''---------------------------'''
	
	if "E" in printpoint:
		Custom1000(name,60,str(list[returned]),15)
		'''RESET-ALL-COLORS'''
		for x in list0c: setSkinSetting('0',x,"")
		for x in list0c: setSkinSetting('0',x,"")
		'''---------------------------'''
		
	if "F" in printpoint:
		Custom1000(name,70,str(list[returned]),15)
		'''RANDOM-ALL-COLORS'''
		returned, count = getRandom("0", min=1, max=5, percent=50)
		for x in list0c:
			if count == 1: value = value1 ; value_ = value1_
			elif count == 2: value = value2 ; value_ = value2_
			elif count == 3: value = value3 ; value_ = value3_
			elif count == 4: value = value4 ; value_ = value4_
			elif count == 5: value = value5 ; value_ = value5_
			setSkinSetting('0',x,value)
			setSkinSetting('0',x+'.name',value_)
			'''---------------------------'''
		
	if "G" in printpoint:
		Custom1000(name,90,str(list[returned]),10)
		'''RESET-ALL-TRANSPERANCY'''
		for x in list0o: setSkinSetting('0',x,"")
		'''---------------------------'''
		
	if "H" in printpoint:
		Custom1000(name,90,str(list[returned]),10)
		'''RANDOM-ALL-TRANSPERANCY'''
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
		
		for x in list0o:
			returned, count = getRandom("0", min=1, max=5, percent=50)
			if count == 1: y = str(value1)
			elif count == 2: y = str(value2)
			elif count == 3: y = str(value3)
			elif count == 4: y = str(value4)
			elif count == 5: y = str(value5)
			setSkinSetting('0',x,y)
			'''---------------------------'''
	
	if "I" in printpoint:
		Custom1000(name,"",localize(74536),30)
		'''RESET BUTTONS PROPERTIES'''
		count = 0
		for i in range(70,110):
			count += 2
			setSkinSetting('0','id'+str(i),"")
			setSkinSetting('0','label'+str(i),"")
			setSkinSetting('0','action'+str(i),"")
			setSkinSetting('0','color'+str(i),"")
			setSkinSetting('0','icon'+str(i),"")
			setSkinSetting('0','background'+str(i),"")
			setSkinSetting('1','off'+str(i),"")
			setSkinSetting('1','sub'+str(i),"")
			'''---------------------------'''
			for i2 in range(90,110):
				setSkinSetting('0','id'+str(i)+'_'+str(i2),"")
				setSkinSetting('0','label'+str(i)+'_'+str(i2),"")
				setSkinSetting('0','action'+str(i)+'_'+str(i2),"")
				setSkinSetting('1','off'+str(i)+'_'+str(i2),"")
				setSkinSetting('0','icon'+str(i)+'_'+str(i2),"")
				'''---------------------------'''
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		Custom1000(name,100,'',20)
		notification(".","","",1000)
		ReloadSkin(admin)
		xbmc.executebuiltin('ActivateWindow(Home.xml)') ; xbmc.executebuiltin('ActivateWindow(1117)') ; xbmc.executebuiltin('ActivateWindow(1173)')
		
	print printfirst + name + "_LV" + printpoint + space + "list" + space2 + str(list) + space + "returned" + space2 + str(returned)
	'''---------------------------'''

def mode202(value, admin, name, printpoint):
	'''------------------------------
	---CHOOSE-COLORS-2---------------
	------------------------------'''
		
	#x = xbmc.getInfoLabel('Container(9003).ListItem(0).Label')
	#x2 = xbmc.getInfoLabel('Container(9003).ListItemNoWrap(0).Property(colorID)')
	#y = xbmc.getInfoLabel('Container(9003).ListItemNoWrap(0).Property(color)')
	#listitempropertycolor = xbmc.getInfoLabel('ListItem.Property(color)')
	
	if property_temp != "":
		if value == "30110":
			'''DEFAULT COLOR'''
			printpoint = printpoint + "2"
			setSkinSetting('0', property_temp, "")
			setSkinSetting('0', property_temp + '.name', "")
			notification("...","","",1000)
			xbmc.executebuiltin('Dialog.Close(1175)')
			if custom1173W: xbmc.executebuiltin('Dialog.Close(1173)')
			xbmc.executebuiltin('Dialog.Close(1117)')
			xbmc.executebuiltin('Action(Close)')
			xbmc.executebuiltin('ActivateWindow(1117)')
			if custom1173W: xbmc.executebuiltin('ActivateWindow(1173)')
			'''---------------------------'''
		else: printpoint = printpoint + "9"
		
	else: printpoint = printpoint + "9"
	xbmc.executebuiltin('ClearProperty(TEMP,home)')
	print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + newline + \
	'property_temp' + space2 + str(property_temp)
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
		'''---------------------------'''
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		
		if returned == 1 or returned == 2: path = skin_userdata_path
		elif returned == 3 or (returned == "" and value == "Templates"): path = skin_specials_userdata_path
		else: path = ""
		
		if path != "":
			'''read existing files'''
			file1 = os.path.join(path, "Skin_SaveDesign1.txt")
			file2 = os.path.join(path, "Skin_SaveDesign2.txt")
			file3 = os.path.join(path, "Skin_SaveDesign3.txt")
			'''---------------------------'''
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
			Custom1000(name,0,str(list[returned2]),5)
			
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
				from variables2 import *
				Custom1000(name,20,str(list[returned2]),10)
				formula = ""
				formula = "Skin.Theme=2" + skincurrenttheme
				for i in range(70,110):
					x = idT.get('id'+str(i))
					formula = formula + newline + 'id'+str(i)+'=0' + str(x)
					x = labelT.get('label'+str(i))
					formula = formula + newline + 'label'+str(i)+'=0' + str(x)
					x = actionT.get('action'+str(i))
					formula = formula + newline + 'action'+str(i)+'=0' + str(x)
					x = offT.get('off'+str(i))
					formula = formula + newline + 'off'+str(i)+'=1' + str(x)
					x = colorT.get('color'+str(i))
					formula = formula + newline + 'color'+str(i)+'=0' + str(x)
					x = iconT.get('icon'+str(i))
					formula = formula + newline + 'icon'+str(i)+'=0' + str(x)
					x = backgroundT.get('background'+str(i))
					formula = formula + newline + 'background'+str(i)+'=0' + str(x)
					x = subT.get('sub'+str(i))
					formula = formula + newline + 'sub'+str(i)+'=1' + str(x)
					for i2 in range(91,110):
						x = id_T.get('id'+str(i)+'_'+str(i2))
						formula = formula + newline + 'id'+str(i)+'_'+str(i2)+'=0' + str(x)
						x = label_T.get('label'+str(i)+'_'+str(i2))
						formula = formula + newline + 'label'+str(i)+'_'+str(i2)+'=0' + str(x)
						x = action_T.get('action'+str(i)+'_'+str(i2))
						formula = formula + newline + 'action'+str(i)+'_'+str(i2)+'=0' + str(x)
						x = off_T.get('off'+str(i)+'_'+str(i2))
						formula = formula + newline + 'off'+str(i)+'_'+str(i2)+'=1' + str(x)
						x = icon_T.get('icon'+str(i)+'_'+str(i2))
						formula = formula + newline + 'icon'+str(i)+'_'+str(i2)+'=0' + str(x)
						'''---------------------------'''
				
				Custom1000(name,50,str(list[returned2]),5)
				for y in list1:
					x = xbmc.getInfoLabel('Skin.HasSetting('+y+')')
					formula = formula + newline + y+'=1' + str(x)
					'''---------------------------'''
				
				for y in list0:
					x = xbmc.getInfoLabel('Skin.String('+y+')')
					formula = formula + newline + y+'=0' + str(x)
					'''---------------------------'''
					
				for y in list0c:
					x = xbmc.getInfoLabel('Skin.String('+y+')')
					x2 = xbmc.getInfoLabel('Skin.String('+y+'.name)')
					formula = formula + newline + y+'=1' + str(x)
					formula = formula + newline + y+'.name'+'=1' + str(x2)
					'''---------------------------'''
				
				Custom1000(name,70,str(list[returned2]),5)
				for y in list0c2:
					x = xbmc.getInfoLabel('Skin.String('+y+')')
					formula = formula + newline + y+'=0' + str(x)
					'''---------------------------'''
				
				for y in list0o:
					x = xbmc.getInfoLabel('Skin.String('+y+')')
					formula = formula + newline + y+'=0' + str(x)
					'''---------------------------'''
				
				if "1" in printpoint:
					if filename1 == None: filename = ""
					else: filename = filename1
				elif "2" in printpoint:
					if filename2 == None: filename = ""
					else: filename = filename2
				elif "3" in printpoint:
					if filename3 == None: filename = ""
					else: filename = filename3
				
				Custom1000(name,90,str(list[returned2]),5)
				filename = dialogkeyboard(filename, localize(21821), 0, "", "", "") #Description
				filename_ = "&name="+str(filename)+"&"
				formula = filename_ + newline + formula
				
				#formula.decode('utf-8').encode('utf-8')
				try: formula.encode('utf-8')
				except: pass
				
				if "1" in printpoint:
					write_to_file(skin_userdata_path + "Skin_SaveDesign1.txt", str(formula), append=False, silent=True, utf8=False)
					#setsetting('Skin_SaveDesign1', str(formula))
				elif "2" in printpoint:
					write_to_file(skin_userdata_path + "Skin_SaveDesign2.txt", str(formula), append=False, silent=True, utf8=False)
					#setsetting('Skin_SaveDesign2', str(formula))
				elif "3" in printpoint:
					write_to_file(skin_userdata_path + "Skin_SaveDesign3.txt", str(formula), append=False, silent=True, utf8=False)
					#setsetting('Skin_SaveDesign3', str(formula))
				'''---------------------------'''
				Custom1000(name,100,str(list[returned2]),0)
				
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
					Custom1000(name,20,str(list[returned2]),10)
					import fileinput
					count = 0
					for line in fileinput.input([file]):
						count += 1
						if count >= 10:
							count = 0
							property_1000progress = xbmc.getInfoLabel('Window(home).Property(1000progress)')
							Custom1000(name,int(property_1000progress) + 2,str(list[returned2]),10)
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
					
					Custom1000(name,100,str(list[returned2]),5)
			if not "Q" in printpoint and not "A" in printpoint:
				xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(200)
				ReloadSkin(admin)
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
	addon = 'plugin.video.genesis'
	if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
	else:
		if property_buttonid == "77":
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
			
		elif property_buttonid == "78":
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

def mode210(value, admin, name, printpoint):
	'''------------------------------
	---MOVE-ITEM---------------------
	------------------------------'''
	extra = "" ; extra2 = "" ; TypeError = "" ; x = "" ; y = "" ; y2 = ""
	
	xbmc.executebuiltin('Action(Close)')
	
	#dp = xbmcgui.DialogProgress() ; dp.create(name, "Starting", " ")
	'''---------------------------'''

	if not int(property_buttonid) > 0 or not int(property_buttonid_) > 0: printpoint = printpoint + "9A"
	if '0' in value:
		printpoint = printpoint + "0"
		if property_temp == property_buttonid or property_temp2 == property_buttonid_: printpoint = printpoint + "9B"
		if property_temp2 == "": printpoint = printpoint + "9C"
		else:
			try:
				if not int(property_temp2) > 0: printpoint = printpoint + "9D"
			except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9E"
	
	if 1 + 1 == 2: pass
	elif '1' in value or '2' in value:
		if property_subbuttonid == "" or property_subbuttonid_ == "": printpoint = printpoint + "9F"
		elif not property_buttonid in property_subbuttonid and not property_buttonid_ in property_subbuttonid_: printpoint = printpoint + "9G"
		elif '_90' in property_subbuttonid or '_90' in property_subbuttonid_: printpoint = printpoint + "9H"
		'''---------------------------'''
		if '1' in value:
			'''sub menu item up'''
			printpoint = printpoint + "1"
			#dp.update(10,"sub menu item up"," ")
			if property_previoussubbuttonid == "" or property_previoussubbuttonid_ == "": printpoint = printpoint + "9I"
			elif property_subbuttonid in property_previoussubbuttonid or property_subbuttonid_ in property_previoussubbuttonid_: printpoint = printpoint + "9J"
			elif property_subbuttonid == property_previoussubbuttonid or property_buttonid_ == property_previoussubbuttonid_: printpoint = printpoint + "9K"
			elif '_90' in property_previoussubbuttonid or '_90' in property_previoussubbuttonid_: printpoint = printpoint + "9L"
			'''---------------------------'''
		elif '2' in value:
			'''sub menu item down'''
			printpoint = printpoint + "2"
			#dp.update(10,"sub menu item down"," ")
			if property_nextsubbuttonid == "" or property_nextsubbuttonid_ == "": printpoint = printpoint + "9I"
			elif property_subbuttonid in property_nextsubbuttonid or property_subbuttonid_ in property_nextsubbuttonid_: printpoint = printpoint + "9J"
			elif property_subbuttonid == property_nextsubbuttonid or property_buttonid_ == property_nextsubbuttonid_: printpoint = printpoint + "9K"
			elif '_90' in property_nextsubbuttonid or '_90' in property_nextsubbuttonid_: printpoint = printpoint + "9L"
			'''---------------------------'''	
	if not '9' in printpoint:
		notification_common("2")
		from variables2 import *
		if '0' in value:
			for i in range(0,2):
				x = "" ; y = "" ; y2 = ""
				print "i" + space2 + str(i)
				if i == 0:
					'''property_buttonid -> property_temp'''
					#dp.update(20,"property_buttonid -> property_temp"," ")
					x = property_temp2
					x2 = property_temp
					y = property_buttonid_
					y2 = property_buttonid
					'''---------------------------'''
				elif i == 1:
					'''property_temp -> property_buttonid'''
					#dp.update(50,"property_temp -> property_buttonid"," ")
					x = property_buttonid_
					x2 = property_buttonid_
					y = property_temp2
					y2 = property_temp
					'''---------------------------'''
				else: pass	
				if x != "" and y != "":
					'''continue'''
					notification("...", str(labelT.get('label'+x)) + ' -> ' + str(labelT.get('label'+y)), "", 1000)
					setSkinSetting('0','id'+x,str(idT.get('id'+y)))
					setSkinSetting('0','label'+x,str(labelT.get('label'+y)))
					setSkinSetting('0','action'+x,str(actionT.get('action'+y)))
					setSkinSetting('1','off'+x,str(offT.get('off'+y)))
					setSkinSetting('0','color'+x,str(colorT.get('color'+y)))
					setSkinSetting('0','icon'+x,str(iconT.get('icon'+y)))
					#setSkinSetting('0','background'+y,str(backgroundT.get('background'+x)))
					setSkinSetting('1','sub'+x,str(subT.get('sub'+y)))
					'''---------------------------'''
					#setSkinSetting('0','label'+x+'_90',str(label_T.get('label'+y+'_90'))) #_90 label
					#setSkinSetting('0','icon'+x+'_90',str(icon_T.get('icon'+y+'_90'))) #_90 icon
					#setSkinSetting('0','action'+x+'_90',str(action_T.get('action'+y+'_90'))) #_90 icon
					'''---------------------------'''
					if 1 + 1 == 3:
						for i2 in range (90,110):
							setSkinSetting('0','id'+x+'_'+str(i2),str(id_T.get('id'+y+'_'+str(i2))))
							setSkinSetting('1','off'+x+'_'+str(i2),str(off_T.get('off'+y+'_'+str(i2))))
							setSkinSetting('0','label'+x+'_'+str(i2),str(label_T.get('label'+y+'_'+str(i2))))
							setSkinSetting('0','action'+x+'_'+str(i2),str(action_T.get('action'+y+'_'+str(i2))))
							setSkinSetting('0','icon'+x+'_'+str(i2),str(icon_T.get('icon'+y+'_'+str(i2))))
							'''---------------------------'''
				else: notification("Error","","",2000) ; printpoint = printpoint + "8"
		elif '1' in value or '2' in value:
			for i in range(0,2):
				x = "" ; y = ""
				if i == 0:
					if '1' in value:
						'''property_subbuttonid_ -> property_previoussubbuttonid_'''
						#dp.update(20,"property_subbuttonid_ -> property_previoussubbuttonid_"," ")
						x = property_previoussubbuttonid_
						y = property_subbuttonid_
						'''---------------------------'''
					elif '2' in value:
						'''property_subbuttonid_ -> property_nextsubbuttonid_'''
						#dp.update(20,"property_subbuttonid_ -> property_nextsubbuttonid_"," ")
						x = property_nextsubbuttonid_
						y = property_subbuttonid_
						'''---------------------------'''
					
				elif i == 1:
					'''property_previoussubbuttonid_ -> property_subbuttonid_'''
					if '1' in value:
						'''property_previoussubbuttonid_ -> property_subbuttonid_'''
						#dp.update(50,"property_previoussubbuttonid_ -> property_subbuttonid_"," ")
						x = property_subbuttonid_
						y = property_previoussubbuttonid_
						'''---------------------------'''
					elif '2' in value:
						'''property_nextsubbuttonid_ -> property_subbuttonid_'''
						#dp.update(50,"property_nextsubbuttonid_ -> property_subbuttonid_"," ")
						x = property_subbuttonid_
						y = property_nextsubbuttonid_
						'''---------------------------'''
					
				else: pass
				
				if x != "" and y != "":
					'''continue'''
					#label_ = xbmc.getInfoLabel('$VAR[label'+y+']')
					label_ = xbmc.getInfoLabel('$VAR['+label_T.get('label'+y)+']')
					#label_ = xbmc.getInfoLabel('$VAR[label78_91]')
					
					#elif i == 1: label_ = xbmc.getInfoLabel('$VAR[label'+x+']')
					#y2 = xbmc.getInfoLabel('$VAR[action'+x+']')
					#from variables2 import label_T
					notification("...", "", "", 1000)
					setSkinSetting('0','id'+x,str(id_T.get('id'+y)))
					setSkinSetting('1','off'+x,str(off_T.get('off'+y)))
					#xbmc.executebuiltin('Skin.SetString(label'+x+','+str(label_T.get('label'+y))+')')
					setSkinSetting('0','label'+x,label_T.get('label'+y))
					#setSkinSetting('0','label'+x,str(label_))
					setSkinSetting('0','action'+x,str(action_T.get('action'+y)))
					setSkinSetting('0','icon'+x,str(icon_T.get('icon'+y)))
					
					print id_T.get('id'+y)
					print label_T.get('label'+y)
					print 'label_' + space2 + label_
					print action_T.get('action'+y)
					print icon_T.get('icon'+y)
					print 'label_T:'
					if 1 + 1 == 3:
						for xx in label_T:
							if xx != "":
								print xx
								'''---------------------------'''
				else: printpoint = printpoint + "9" ; break
				
				extra2 = extra2 + newline + "i" + space2 + str(i) + space + "x" + space2 + str(x) + space + "y" + space2 + str(y) + space + "y2" + space2 + str(y2) + space
	#dp.close
	if "9" in printpoint: notification("Error Occured!", '', '', 2000)
	else:
		pass#ReloadSkin(admin)
		xbmc.sleep(500) ; xbmc.executebuiltin('Action(Down)') ; xbmc.sleep(500) ; xbmc.executebuiltin('Action(Up)')
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + newline + \
		"property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonid_" + space2 + str(property_buttonid_) + newline + \
		"property_temp" + space2 + str(property_temp) + space + "property_temp2" + space2 + str(property_temp2) + newline + \
		"property_subbuttonid" + space2 + str(property_subbuttonid) + space + "property_subbuttonid_" + space2 + str(property_subbuttonid_) + newline + \
		"property_previoussubbuttonid" + space2 + str(property_previoussubbuttonid) + space + "property_previoussubbuttonid_" + space2 + str(property_previoussubbuttonid_) + newline + \
		"property_nextsubbuttonid" + space2 + str(property_nextsubbuttonid) + space + "property_nextsubbuttonid_" + space2 + str(property_nextsubbuttonid_) + newline + \
		extra + extra2
		'''---------------------------'''

def mode211(value, admin, name, printpoint):
	'''------------------------------
	---Create-New-Item---------------
	------------------------------'''
	from variables2 import *
	extra = "" ; TypeError = "" ; x = "" ; y = ""
	
	#xbmc.executebuiltin('Action(Close)')
	if not int(property_buttonid_) > 0: printpoint = printpoint + "1" ; notification("Error No.1", "", "", 1000)
	else:
		'''Get new control ID'''
		if '0' in value:
			'''main menu item'''
			xbmc.executebuiltin('Dialog.Close(1175)')
			for i in range(100,109):
				x = xbmc.getInfoLabel('Skin.String(label'+str(i)+')')
				if x == "":
					y = str(i)
					setSkinSetting('0','label'+y,"...")
					setSkinSetting('1','off'+y,"false")
					break
				else: pass
		
		elif '1' in value:
			'''sub menu item'''
			#xbmc.executebuiltin('Dialog.Close(1138)')
			for i in range(100,109):
				x = xbmc.getInfoLabel('Skin.String(label'+property_buttonid+'_'+str(i)+')')
				print x
				if x == "":
					y = property_buttonid+'_'+str(i)
					setSkinSetting('0','label'+y,"...")
					setSkinSetting('1','off'+y,"false")
					break
				else: pass

					
		if y == "": printpoint = printpoint + "9" ; notification("Cannot create new buttons","Delete some first","",2000)
		else:
			notification("...", "", "", 1000)
			mode232(y, admin, 'ACTION-BUTTON', printpoint)
			'''---------------------------'''
			#xbmc.executebuiltin('SetProperty(TEMP2,'+str(idT.get('id'+y))+',home)') #STATIC
			#xbmc.executebuiltin('SetProperty(TEMP,'+str(idT.get('id'+y))+',home)') #DYNAMIC
			
			#xbmc.executebuiltin('RunScript('+addonID+',,?mode=210&value=0)') ; xbmc.sleep(1000)
			#mode210(y, admin, name, printpoint)
				
	
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + newline + \
		"property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonid_" + space2 + str(property_buttonid_) + newline + \
		"property_temp" + space2 + str(property_temp) + space + "property_temp2" + space2 + str(property_temp2) + newline + \
		"x" + space2 + str(x) + newline + \
		"y" + space2 + str(y) + newline + \
		extra
		'''---------------------------'''

def mode212(value, admin, name, printpoint):
	'''------------------------------
	---REMOVE-ITEM-------------------
	------------------------------'''
	extra = "" ; extra2 = "" ; TypeError = "" ; x = "" ; two = 1 ; property_buttonname2 = ""

	try:
		if property_buttonid == "": printpoint = printpoint + "9A"
		else: test = int(property_buttonid_) + 1
		if '0' in value:
			if int(property_buttonid) < 100 and not 'B' in value: printpoint = printpoint + "9B"
		if '1' in value:
			if not "_" in property_subbuttonid or not "_" in property_subbuttonid_: printpoint = printpoint + "9C"
			if not "_" in property_subbuttonid or not "_" in property_subbuttonid_: printpoint = printpoint + "9D"
			if not property_buttonid in property_subbuttonid and not property_buttonid_ in property_subbuttonid_: printpoint = printpoint + "9E"
		if 'B' in value and property_buttonid != property_buttonid_:
			from variables2 import idT, labelT
			two = 2
			y = 'Reset item'
			x = property_buttonid_
			property_buttonname2 = labelT.get('label'+property_buttonid)
			extra2 = extra2 + newline + "This action will also reset" + space2 + str(property_buttonname2) + space + "(" + str(property_buttonid) + ")"
		
		else:
			y = 'Remove item'
			x = property_buttonid_
			two = 1
			
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9F"
	
	if not '9' in printpoint:
		if '0' in value:
			'''main menu item'''
			printpoint = printpoint + "0"
			xbmc.sleep(100) ; returned = dialogyesno(y + space2 + str(property_buttonname), "Choose YES to proceed!" + extra2)
			if returned == 'skip': printpoint = printpoint + "8"
			else:
				for i in range(0,two):
					if i == 1: x = str(property_buttonid)
					setSkinSetting('1','off' + x,"false")
					if int(property_buttonid) > 99 and not 'B' in value: setSkinSetting('0','label' + x,"")
					else: setSkinSetting('0','label' + x,"...")
					setSkinSetting('1','sub' + x,"false")
					setSkinSetting('0','id' + x,"")
					setSkinSetting('0','color' + x,"")
					setSkinSetting('0','icon' + x,"")
					setSkinSetting('0','action' + x,"")

					if '2' in value:
						'''sub menu items'''
						printpoint = printpoint + "2"
						if x == "": printpoint = printpoint + "9L"
						else:
							for i in range(90,109):
								if i > 99 : setSkinSetting('0','label'+x+'_'+str(i),"")
								else: setSkinSetting('0','label'+x+'_'+str(i),"")
								setSkinSetting('1','off'+x+'_'+str(i),"false")
								setSkinSetting('0','id'+x+'_'+str(i),"")
								setSkinSetting('0','action'+x+'_'+str(i),"")
								setSkinSetting('0','icon'+x+'_'+str(i),"")
								'''---------------------------'''			
				printpoint = printpoint + "7"
					
		if '1' in value:
			'''sub menu item'''
			printpoint = printpoint + "1"
			if 'B' in value:
				y = 'Reset item'
				x = property_subbuttonid_
			else:
				y = 'Remove item'
				x = property_subbuttonid_
				
			xbmc.sleep(100) ; returned = dialogyesno(y + space2 + str(property_subbuttonname), "Choose YES to proceed!")
			if returned == 'skip': printpoint = printpoint + "8"
			else:
				setSkinSetting('1','off' + x,"false")
				if not '_90' in property_subbuttonid_ and not 'B' in value: setSkinSetting('0','label' + x,"")
				else: setSkinSetting('0','label' + x,"...")
				setSkinSetting('0','id' + x,"")
				setSkinSetting('0','icon' + x,"")
				setSkinSetting('0','action' + x,"")
				printpoint = printpoint + "7"
		
	
	if not "7" in printpoint and not "8" in printpoint:
		'''Error'''
		notification("Error...","","",1000)
	else:
		xbmc.executebuiltin('Action(Close)') ; xbmc.sleep(500)
		xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=215&value='+property_buttonid_+')')
		if two == 2: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=215&value='+property_buttonid+')')
	
	
	
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + newline + \
		"property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonid_" + space2 + str(property_buttonid_) + space + "property_buttonname" + space2 + str(property_buttonname) + newline + \
		"property_buttonname2" + space2 + str(property_buttonname2) + newline + \
		"property_subbuttonid" + space2 + str(property_subbuttonid) + space + "property_subbuttonid_" + space2 + str(property_subbuttonid_) + space + "property_subbuttonname" + space2 + str(property_subbuttonname) + newline + \
		extra
		'''---------------------------'''

def mode213(value, admin, name, printpoint):
	'''------------------------------
	---Includes_HomeContent----------
	------------------------------'''
	list = [] ; i = 0 ; x = 0
	
	returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
	if returned_Dialog != "": printpoint = printpoint + "9"
	
	elif value == '1' or value == '2':
		'''homeW/customhomecustomizerW'''
		if custom1138W or custom1139W or custom1175W or custom1173W or HomeW: printpoint = printpoint + "9"
		x = xbmc.getInfoLabel('Container(9000).ListItem('+str(i)+').Label')
		y = xbmc.getInfoLabel('Container(9000).NumItems')

	elif value == '3':
		'''customhomecustomizer2W'''
		if custom1138W or custom1139W or custom1175W or custom1173W: printpoint = printpoint + "9"
		x = xbmc.getInfoLabel('Container(51).ListItem('+str(i)+').Label')
		y = xbmc.getInfoLabel('Container(51).NumItems')
	
	elif value == '4':
		'''Home'''
		x = 'N/A'
		y = 'N/A'
		
	try: test = int(y)
	except: y = 0
	
	if value == '1':
		if int(y) < 2:
			'''set default buttons'''
			printpoint = printpoint + "5"
			mode215('_', admin, name, "")
			
			if 1 + 1 == 3:
				if not os.path.exists(includes_homecontent_file): printpoint = printpoint + "5"
				else:
					filesize = getFileAttribute(2, includes_homecontent_file)
					if filesize == 0: printpoint = printpoint + "5"
					else:
						homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
						container9000numitems = xbmc.getInfoLabel('Container(9000).NumItems')
						if homeW and container9000numitems == "0": printpoint = printpoint + "5"
						'''---------------------------'''
					
				if "5" in printpoint:
					if os.path.exists(includes_homecontent2_file):
						printpoint = printpoint + "1"
						notification("Restoring AutoSaved Buttons", "...", "", 4000)
						returned = copyfiles(includes_homecontent2_file, includes_homecontent_file, chmod="", mount=False)
						if returned != 'ok': notification("Error restoring AutoSaved Buttons", "...", "", 3000)
						xbmc.sleep(1000)
						replace_word(includes_homecontent_file,'','', LineR=True, LineClean=True)
						ReloadSkin(admin) ; xbmc.sleep(4000)
					
					homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
					container9000numitems = xbmc.getInfoLabel('Container(9000).NumItems')
					if homeW and container9000numitems == "0":
						printpoint = printpoint + "3"
						if os.path.exists(includes_homecontent3_file):
							printpoint = printpoint + "7"
							notification("Restoring Default Home Buttons!", "...", "", 4000)
							returned = copyfiles(includes_homecontent3_file, includes_homecontent_file, chmod="", mount=False) ; xbmc.sleep(1000)
							if returned != 'ok': notification("Error restoring Default Home Buttons", "Contact HTPT Team", "", 3000)
							xbmc.sleep(1000)
							replace_word(includes_homecontent_file,'','', LineR=True, LineClean=True)
							ReloadSkin(admin) ; xbmc.sleep(4000)
	
	if "9" in printpoint: pass
	elif (value == '1' or value == '2' or value == '3') and xbmc.getInfoLabel('$VAR[background]') == "" and reloadskin_check == "": printpoint = printpoint + "7A"
	elif value == '4' and xbmc.getCondVisibility('IsEmpty(Control.GetLabel(111))') and xbmc.getCondVisibility('!Control.IsVisible(7021)') and reloadskin_check == "": printpoint = printpoint + "7B"
	elif (x == "" or y == ""):
		'''ReloadSkin - Fix Bug'''
		count = 0
		for i in range(-5,5):
			count += 1
			x = xbmc.getInfoLabel('Container(9000).ListItem('+str(i)+').Label') + xbmc.getInfoLabel('Container(51).ListItem('+str(i)+').Label') + xbmc.getInfoLabel('Container(50).ListItem('+str(i)+').Label')
			list.append(x)
			if x != '' and x != 'Test': break
	
		if count > 7:
			printpoint = printpoint + "7D"
	
	else:
		pass
	
	if "7" in printpoint and not playerhasvideo: ReloadSkin(admin)
	
	print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + newline + \
	"x" + space2 + str(x) + space + "y" + space2 + str(y) + space + newline + \
	"list" + space2 + str(list) + newline + \
	"$VAR[background]" + space2 + str(xbmc.getInfoLabel('$VAR[background]')) + space + "$VAR[MainBackgroundTexture]" + space2 + str(xbmc.getInfoLabel('$VAR[MainBackgroundTexture]')) + newline + \
	"$VAR[Button9093]" + space2 + str(xbmc.getInfoLabel('$VAR[Button9093]')) + space + "reloadskin_check" + space2 + str(reloadskin_check)

def mode214(value, admin, name, printpoint):
	if value == '0':
		returned = dialogkeyboard(property_buttonname,'Button Name',0,"",'label'+property_buttonid_,"")
		if returned != 'skip':
			if returned == "": setSkinSetting('0','label'+property_buttonid_, '...') ; xbmc.sleep(500) ; mode215(property_buttonid_, admin, name, "")
	
	if value == '1':
		returned = dialogkeyboard(property_subbuttonname,'Sub Button Name',0,"",'label'+property_subbuttonid_,"")
		if returned != 'skip':
			if returned == "": setSkinSetting('0','label'+property_subbuttonid_, '...') ; xbmc.sleep(500) ; mode215(property_subbuttonid, admin, name, "")
		
def mode215(value, admin, name, printpoint):
	extra2 = ""
	from variables2 import *
	
	if value == '_' or value == 'MAIN':
		for i in range(70,110):				
			if 1 + 1 == 3:
				x = 'id'+str(i)
				y = xbmc.getInfoLabel('Skin.String('+x+')')
				if y == "":
					setSkinSetting('0',str(x),str(x).replace('id',""))
					if admin: extra2 = extra2 + space + "id" + space + "x" + space2 + str(x) + space + "y" + space2 + str(y) + '|'
					
			for i2 in range(90,110):
				x = 'id'+str(i)+'_'+str(i2)
				y = xbmc.getInfoLabel('Skin.String('+x+')')
				if y == "":
					setSkinSetting('0',str(x),str(x).replace('id',""))
					if admin: extra2 = extra2 + space + "id_" + space + "x" + space2 + str(x) + space + "y" + space2 + str(y) + '|'
					
	if 1 + 1 == 3:			
		for x in id_T:
			y = id_T.get(x)
			print "y" + space2 + str(y)
			if y == "" or y == None:
				setSkinSetting('0','id' + str(x), str(x))
				extra2 = extra2 + space + str(x) + space2 + str(y) + '|'
			else:
				pass
				
	
	if value != "": notification_common("2")
	
	if value == 'MAIN' or value == '_':
		if 1 + 1 == 3:
			for i in range(70,110):
				
				x = 'id'+str(i)
				y = xbmc.getInfoLabel('Skin.String('+x+')')
				if y == "":
					setSkinSetting('0',str(x),str(x).replace('id',""))
					extra2 = extra2 + newline + "id" + space + "x" + space2 + str(x) + space + "y" + space2 + str(y) + space
						
				for i2 in range(90,110):
					x = 'id'+str(i)+'_'+str(i2)
					y = xbmc.getInfoLabel('Skin.String('+x+')')
					if y == "":
						setSkinSetting('0',str(x),str(x).replace('id',""))
						extra2 = extra2 + newline + "id_" + space + "x" + space2 + str(x) + space + "y" + space2 + str(y) + space
	
	'''סרטים'''
	if value != "":
		'''ראשי'''
		x = '70' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(342))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=501&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/movies.png')		
			'''---------------------------'''
		if value in '70_93' or value == 'RESET':
			'''קדימונים'''
			x = '70_93' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'קדימונים')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=501&value=3)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/trailers.png')
				'''---------------------------'''
		if value in '70_94' or value == 'RESET':
			'''חידון'''
			x = '70_94' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'חידון') #localize(75090)
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=501&value=4)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
				'''---------------------------'''
	
	'''סדרות'''
	if value != "":
		'''ראשי'''
		x = '71' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(20343))
			
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=502&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/tvshows.png')
			'''---------------------------'''
	
	''''''
	if value != "" and 1 + 1 == 3:
		'''ראשי'''
		x = '72' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''
	
	''''''
	if value != "" and 1 + 1 == 3:
		'''ראשי'''
		x = '73' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	
		
	'''סדרות ישראליות'''
	if value != "":
		'''ראשי'''
		x = '74' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(73420))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/israeltv.png')
			'''---------------------------'''
		print str(id)
		if value in '74_91' or value == 'RESET':
			'''מאקו'''
			x = '74_91' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79002))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=1)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/makoTV.png')
				'''---------------------------'''
		if value in '74_92' or value == 'RESET':
			'''רשת'''
			x = '74_92' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79003))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=2)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/reshet.png')
				'''---------------------------'''
		if value in '74_93' or value == 'RESET':
			'''סרטים ישראלים'''
			x = '74_93' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(78958))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=3)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/israelmovies.png')
				'''---------------------------'''
		if value in '74_94' or value == 'RESET':
			'''טלנובלה'''
			x = '74_94' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(78943))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=4)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/soapopera.png')
				'''---------------------------'''
		if value in '74_96' or value == 'RESET':
			'''VOD הוט'''
			x = '74_96' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79000))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=6)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/hotvod.png')
				'''---------------------------'''
		if value in '74_97' or value == 'RESET':
			'''VOD ערוץ 10'''
			x = '74_97' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79005) + ' VOD')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=7)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/c10.png')
				'''---------------------------'''
		if value in '74_98' or value == 'RESET':
			'''VOD ערוץ 11'''
			x = '74_98' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79006) + ' VOD')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=503&value=8)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/c11.png')
				'''---------------------------'''
	
	'''יו-טיוב'''
	if value != "":
		'''ראשי'''
		x = '75' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(73430))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,mode=504&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/youtube.png')
			'''---------------------------'''	
		if value in '75_91' or value == 'RESET':
			'''HTPT-צחוקים'''
			x = '75_91' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'HTPT ROFL')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=504&value=1)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/rofl.png')
				'''---------------------------'''
		if value in '75_92' or value == 'RESET':
			'''המיטב של יו-טיוב'''
			x = '75_92' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79010))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=504&value=2)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/bestofyoutube.png')
				'''---------------------------'''
		if value in '75_95' or value == 'RESET':
			'''פוקר'''
			x = '75_95' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'POKER')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=504&value=5)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icon/wsop.png')	
				'''---------------------------'''
	
	'''מוזיקה'''
	if value != "":
		'''ראשי'''
		x = '76' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(2))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=514&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/music.png')
			'''---------------------------'''	
		if value in '76_92' or value == 'RESET':
			'''ספריית מוזיקה'''
			x = '76_92' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79491))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=514&value=3)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')	
			
		if value in '76_93' or value == 'RESET':
			'''רדיו'''
			x = '76_93' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(19021))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=514&value=4)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/radio.png')	
			
		if value in '76_95' or value == 'RESET':
			'''שיעורי גיטרה'''
			x = '76_95' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79027))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=514&value=6)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/guitar.png')	
				
	'''חפש/הוסף סרטים'''
	if value != "":
		'''ראשי'''
		x = '77' ; id = idT2.get(x)
		if id != "" and int(id) <100:			
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(73200))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=506&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/moviese.png')
			'''---------------------------'''	
		if value in '77_91' or value == 'RESET':
			'''פולסר'''
			x = '77_91' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(77474))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=506&value=1)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')

	'''חפש/הוסף סדרות'''
	if value != "":
		'''ראשי'''
		x = '78' ; id = idT2.get(x)
		if id != "" and int(id) <100:			
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(73210))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=507&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/tvshowse.png')
			'''---------------------------'''	
		if value in '78_91' or value == 'RESET':
			'''פולסר'''
			x = '78_91' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(77474))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=507&value=1)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')	
	
	'''ערוצי טלוויזיה'''
	if value != "":
		'''ראשי'''
		x = '79' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(19023))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=517&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/LiveTV.png')
			'''---------------------------'''
		if value in '79_91' or value == 'RESET':
			'''ספורט 1'''
			x = '79_91' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31621) + ' 1 ' + '('+localize(19664)+')')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=310)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/football.png')
			
			
		if value in '79_92' or value == 'RESET':
			'''ספורט 2'''
			x = '79_92' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31621) + ' 2 ' + '('+localize(19664)+')')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=311)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/football.png')
		
		if value in '79_93' or value == 'RESET':
			'''ספורט 3'''
			x = '79_93' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31621) + ' 3 ' + '('+localize(19664)+')')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=312)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/football.png')
			
		if value in '79_96' or value == 'RESET':
			'''ערוץ הטיולים'''
			x = '79_96' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(74603))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=517&value=6)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/travel.png')
	
	'''מדע וטבע'''
	if value != "":
		'''ראשי'''
		x = '80' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(78942))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=519&value=1)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/animals.png')
			'''---------------------------'''
		
		x = '80_94'
		if value in x or value == 'RESET':
			'''היסטוריה (סרטים)'''
			id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31612) + space + '(' + localize(20342) + ')')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=519&value=4)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
				'''---------------------------'''
				
		x = '80_95'
		if value in x or value == 'RESET':
			'''היסטוריה (סדרות)'''
			id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31612) + space + '(' + localize(20343) + ')')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=519&value=5)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
				'''---------------------------'''
				
		x = '80_95'
		if value in x or value == 'RESET':
			'''היסטוריה (סדרות)'''
			id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31612) + space + '(' + localize(20343) + ')')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=504&value=5)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
				'''---------------------------'''
				print "label" + space + str(label) + space + str(icon)
			print "Walla" + space + str(x) + space + str(id)
				
		if value in '80_96' or value == 'RESET':
			'''TED הרצאות'''
			x = '80_96' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79014))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=504&value=6)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/ted.png')
			
	'''ילדים'''
	if value != "":
		'''ראשי'''
		x = '81' ; id = idT2.get(x) ; background = backgroundT.get('icon'+x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(73220))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=515&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/kids.png')
			'''---------------------------'''	
	
	'''תמונות'''
	if value != "":
		'''ראשי'''
		x = '82' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(1))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=509&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/pictures.png')
			'''---------------------------'''
	
	'''וידאו'''
	if value != "":
		'''ראשי'''
		x = '83' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(157))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=513&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/videos.png')
			'''---------------------------'''	
	
	'''מזג אוויר'''
	if value != "":
		'''ראשי'''
		x = '84' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(400))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,mode=508&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/weather.png')
			'''---------------------------'''
		
	'''גו-פרו'''
	if value != "":
		'''ראשי'''
		x = '85' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(73440))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/gopro.png')
			'''---------------------------'''	
		if value in '85_93' or value == 'RESET':
			'''ספורט 5 VOD'''
			x = '85_93' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(31621) + ' 5 VOD')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=3)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/israelsport5.png')
			
			
		if value in '85_94' or value == 'RESET':
			'''WWE'''
			x = '85_94' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'WWE')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=4)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/wwe.png')	
			
		if value in '85_95' or value == 'RESET':
			'''NHL'''
			x = '85_95' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'NHL')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=5)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/nhl.png')	
			
		if value in '85_96' or value == 'RESET':
			'''כדורגל'''
			x = '85_96' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(19551))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=6)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/footballtoday.png')
			
			
		if value in '85_97' or value == 'RESET':
			'''כדורסל'''
			x = '85_97' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(79017))
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=7)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/nba.png')
			
			
		if value in '85_98' or value == 'RESET':
			'''אופנועים'''
			x = '85_98' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'אופנועים')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=505&value=8)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/motors.png')
				setSkinSetting('0','del'+id,'true')
		
	'''משחקים'''
	if value != "":
		'''ראשי'''
		x = '86' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(15016))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=510&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/games.png')
			'''---------------------------'''	
		if value in '86_91' or value == 'RESET':
			'''גיימר TV'''
			x = '86_91' ; id = id_T2.get(x)
			
			if id != "" and id != None:
				id = id.replace('id',"")
				label = label_T.get('label'+str(id)) ; icon = icon_T.get('icon'+str(id))
				if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'גיימר TV')
				setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=510&value=1)')
				if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/gametrailers.png')		
	
	'''אינטרנט'''
	if value != "":
		'''ראשי'''
		x = '87' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(443))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=512&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/internet.png')
			'''---------------------------'''
		
	'''מעודפים'''
	if value != "":
		'''ראשי'''
		x = '88' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(1036))
			setSkinSetting('0','action'+id,'ActivateWindow(134)') #RunScript(script.htpt.smartbuttons,,?mode=516&value=0)
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/star.png')
			'''---------------------------'''	
		
	'''מבוגרים'''
	if value != "":
		'''ראשי'''
		x = '89' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(75003))
			setSkinSetting('0','action'+id,'RunScript(script.htpt.smartbuttons,,?mode=520&value=0)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/adult.png')
			'''---------------------------'''
			
	''''''
	if value != "":
		'''ראשי'''
		x = '90' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	

	''''''
	if value != "":
		'''ראשי'''
		x = '91' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	
	
	''''''
	if value != "":
		'''ראשי'''
		x = '92' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	

	''''''
	if value != "":
		'''ראשי'''
		x = '93' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''			
		
	''''''
	if value != "":
		'''ראשי'''
		x = '94' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	
	
	''''''
	if value != "":
		'''ראשי'''
		x = '95' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	
	
	''''''
	if value != "":
		'''ראשי'''
		x = '96' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,'')
			setSkinSetting('0','action'+id,'')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	
	
	'''עזרה'''
	if value != "":
		'''ראשי'''
		x = '97' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(10043))
			setSkinSetting('0','action'+id,'ActivateWindow(1170)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/help.png')
			'''---------------------------'''	
		
	'''הגדרות'''
	if value != "":
		'''ראשי'''
		x = '98' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(5))
			setSkinSetting('0','action'+id,'ActivateWindow(Settings.xml)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/settings.png')
			'''---------------------------'''
		
	'''כיבוי'''
	if value != "":
		'''ראשי'''
		x = '99' ; id = idT2.get(x)
		if id != "" and 1 + 1 == 2:		
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id))
			if label == "" or label == "..." or value == 'RESET': setSkinSetting('0','label'+id,localize(13005))
			setSkinSetting('0','action'+id,'ActivateWindow(1191)')
			if icon == "" or value == 'RESET': setSkinSetting('0','icon'+id,'icons/power.png')
			'''---------------------------'''
	
	if admin:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "id" + space2 + str(id) + newline + \
		"idT" + space2 + str(idT) + newline + \
		"idT2" + space2 + str(idT2) + newline + \
		"id_T" + space2 + str(id_T) + newline + \
		"id_T2" + space2 + str(id_T2) + newline + \
		extra2

def mode218(value, admin, name, printpoint):
	'''------------------------------
	---editButtonProprties-----------
	------------------------------'''	
	if "view" in value:
		message = ""
		message = message + newline + "Current XML" + space2 + xbmc.getInfoLabel('Window.Property(xmlfile)')
		message = message + newline + "TEMP" + space2 + property_temp
		message = message + newline + "TEMP2" + space2 + property_temp2
		message = message + newline + '---------------------------'
		message = message + newline + "Button.ID" + space2 + property_buttonid
		message = message + newline + "Button.ID_" + space2 + property_buttonid_
		message = message + newline + "Button.Name" + space2 + property_buttonname
		message = message + newline + '---------------------------'
		message = message + newline + "SubButton.ID" + space2 + property_subbuttonid
		message = message + newline + "SubButton.ID_" + space2 + property_subbuttonid_
		message = message + newline + "SubButton.Name" + space2 + property_subbuttonname
		message = message + newline + '---------------------------'
		message = message + newline + "Previous_SubButton.ID" + space2 + property_previoussubbuttonid
		message = message + newline + "Previous_SubButton.ID_" + space2 + property_previoussubbuttonid_
		message = message + newline + "Next_SubButton.ID" + space2 + property_nextsubbuttonid
		message = message + newline + "Next_SubButton.ID_" + space2 + property_nextsubbuttonid_
		message = message + newline + '---------------------------'
		message = message + newline + "ReloadSkin" + space2 + property_reloadskin
		message = message + newline + '---------------------------'
		message = message + newline + "SubMenuTip" + space2 + property_submenutip
		message = message + newline + '---------------------------'
		message = message + newline + "1000progress" + space2 + property_1000progress
		message = message + newline + "1000title" + space2 + property_1000title
		message = message + newline + "1000comment" + space2 + property_1000comment
		

		header = name
		diaogtextviewer(header,message)

							
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

def mode230(value, admin, name, printpoint):
	'''------------------------------
	---COLOR-PICKER------------------
	------------------------------'''
	#xbmc.executebuiltin('ActivateWindow(1178)')
	
	if 1 + 1 == 2:
		import xbmcgui
		from Utils import *
		from MainModule import *
		from ColorPicker import ColorPicker, getParams
		params = self.getParams()
		colorPicker = ColorPicker("script-skin_helper_service-ColorPicker.xml", ADDON_PATH, "Default", "1080i")
		colorPicker.skinString = params.get("SKINSTRING",None)
		colorPicker.winProperty = params.get("WINPROPERTY",None)
		colorPicker.shortcutProperty = params.get("SHORTCUTPROPERTY",None)
		colorPicker.doModal()
		propname = params.get("SHORTCUTPROPERTY",None)
		if propname:
			wid = xbmcgui.getCurrentWindowDialogId()
			currentWindow = xbmcgui.Window( xbmcgui.getCurrentWindowDialogId() )
			currentWindow.setProperty("customProperty",propname)
			currentWindow.setProperty("customValue",colorPicker.result[0])
			xbmc.executebuiltin("SendClick(404)")
			xbmc.sleep(250)
			currentWindow.setProperty("customProperty",propname+".name")
			currentWindow.setProperty("customValue",colorPicker.result[1])
			xbmc.executebuiltin("SendClick(404)")
		del colorPicker
		'''---------------------------'''
	
def mode231(value, admin, name, printpoint):
	'''------------------------------
	---INSTALL-ADDON-----------------
	------------------------------'''
	notification_common("24")
	installaddonP(admin, value, update=True)
	'''---------------------------'''

def mode232(value, admin, name, printpoint):
	'''------------------------------
	---ACTION-BUTTON-----------------
	------------------------------'''
	id1 = "" ; id2 = "" ; extra = "" ; TypeError = ""
	if printpoint != "": printpoint = printpoint + "_"
	addon = 'script.skinshortcuts'
	if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddonP(admin, addon)
	else:
		printpoint = printpoint + "0"
		try:
			if value != "":
				if '_' in value: pass
				else: test = int(value) + 1
				id1 = value
			elif custom1175W and not custom1138W:
				if property_buttonid_ == "": printpoint = printpoint + "9B"
				else: test = int(property_buttonid) + 1 ; id1 = property_buttonid_
			elif custom1138W:
				if property_subbuttonid == "" or property_subbuttonid_ == "" or (not property_buttonid in property_subbuttonid and not property_buttonid_ in property_subbuttonid_): printpoint = printpoint + "9C"
				else: id1 = property_subbuttonid_
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9D"
		
		if id1 != "":			
			if custom1175W and not custom1138W:
				'''Main Action'''
				printpoint = printpoint + "x1"
				xbmc.executebuiltin('RunScript(script.skinshortcuts,type=shortcuts&custom=False&showNone=True&skinLabel=label'+id1+'&skinAction=action'+id1+'&skinList=[skinList]&skinType=[skinType]&skinThumbnail=icon'+id1+')')
			elif custom1138W:	
				'''Sub Action'''
				printpoint = printpoint + "x2"
				xbmc.executebuiltin('RunScript(script.skinshortcuts,type=shortcuts&custom=False&showNone=True&skinLabel=label'+id1+'&skinAction=action'+id1+'&skinList=[skinList]&skinType=[skinType]&skinThumbnail=icon'+id1+')')
				'''---------------------------'''
			else: printpoint = printpoint + "8"	
			
			if "x" in printpoint:
				'''wait'''
				xbmc.sleep(4000)
				dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
				while dialogselectW and not xbmc.abortRequested:
					xbmc.sleep(1000)
					dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
					'''---------------------------'''
				xbmc.sleep(500) ; xlabel = xbmc.getInfoLabel('Skin.String(label'+id1+')')
				if xlabel == "":
					setSkinSetting('0','label'+id1,'...')
					if 'x1' in printpoint and not '_' in id1: setSkinSetting('0','label'+id1+'_90','...')
				else:
					if 'x1' in printpoint and not '_' in id1: setSkinSetting('0','label'+id1+'_90',str(xlabel))
					
	if admin and not admin2 and admin3:
		print printpoint + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + space + "property_subbuttonid" + space2 + str(property_subbuttonid) + newline + \
		"id1" + space2 + str(id1) + space + "id2" + space2 + str(id2) + newline + \
		extra
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
	elif (HomeW and myvideopath):
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
			if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ pathwin +'videos/,return)')
			if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ pathwin +'pictures/,return)')
		if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ pathwin +')'):
			if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'videos/,return)')
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
		if "ok" in returned and 1 + 1 == 3:
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
		installaddonP(admin, 'repository.natko1412', update=True)
		installaddonP(admin, 'program.plexus', update=True)
		addon = 'plugin.video.p2psport'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			'''------------------------------
			---plugin.video.p2p-streams------
			------------------------------'''
			printpoint = printpoint + "1"
			countrystr = xbmc.getInfoLabel('Skin.String(Country)')
			if countrystr == "Israel": setsetting_custom1('plugin.video.p2psport','timezone_new','Israel')
			
			if systemplatformwindows:
				programplexus_path = os.path.join(addondata_path, 'program.plexus', '')
				ace_engine = os.path.join(programplexus_path, 'acestream', 'ace_engine.exe')
				ace_player = os.path.join(programplexus_path, 'player', 'ace_player.exe')
				if not os.path.exists(ace_engine) or not os.path.exists(ace_player):
					notification("downloading AceEngine...", "Please wait", "", 7000)
					file = "AceEngine.zip"
					fileID = getfileID(file)
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/AceEngine.zip?dl=1", file, temp_path, programplexus_path, silent=True)
				else: printpoint = printpoint + "A"
			
			returned = ActivateWindow("0", addon, '', 0, wait=True)
			
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
	---SPORT-LIVE-3------------------
	------------------------------'''
	addon = 'plugin.video.bbts'
	installaddonP(admin, addon, update=True)
	url = 'plugin://plugin.video.bbts/?folder=%2fSPORTS'
	returned = ActivateWindow("1", addon, url, 0, wait=True)
	'''---------------------------'''

def mode313(admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	pass
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
			systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1259),40,'Action(Right)','Action(Down)')
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
		systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1273),40,'Action(Right)','Action(Down)')
		count = 0
		while count < 5 and systemcurrentcontrol != localize(1273) and not xbmc.abortRequested:
			'''AirPlay'''
			if count == 0: printpoint = printpoint + "5"
			systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(1273),40,'Action(Right)','Action(Down)')
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

def mode501(value, admin, name, printpoint):
	'''------------------------------
	---MOVIES-BUTTON-----------------
	------------------------------'''
	if value == '0':
		libraryhascontentmovies = xbmc.getCondVisibility('Library.HasContent(Movies)')
		if libraryhascontentmovies:
			if admin: xbmc.executebuiltin('Notification(Admin,moviesbutton,1000)')
			xbmc.executebuiltin('ActivateWindow(Videos,MovieTitles,return)')
			if autoview:
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
	elif value == "3":
		'''------------------------------
		---TRAILERS----------------------
		------------------------------'''
		addon = 'screensaver.randomtrailers'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon(screensaver.randomtrailers)')
		else:
			installaddon(admin, addon, "") ; xbmc.sleep(500)
			
	elif value == '4':
		'''------------------------------
		---QUIZ--------------------------
		------------------------------'''
		addon = 'script.moviequiz'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +')')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		
def mode502(value, admin, name, printpoint):
	'''------------------------------
	---TVSHOWS-BUTTON----------------
	------------------------------'''
	if value == '0':
		libraryhascontenttvshows = xbmc.getCondVisibility('Library.HasContent(TVShows)')
		if libraryhascontenttvshows:
			if admin: xbmc.executebuiltin('Notification(Admin,tvshowsbutton,1000)')
			xbmc.executebuiltin('ActivateWindow(VideoLibrary,TVShowTitles,return)')
			if autoview:
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
	elif value == '1':
		pass
		
def mode503(value, admin, name, printpoint):
	'''------------------------------
	---ISRAEL-TV-BUTTON--------------
	------------------------------'''
	if value == '0':
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
	elif value == '1':
		addon = 'plugin.video.makoTV.video'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '2':
		addon = 'plugin.video.reshet.video'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '3':
		xbmc.executebuiltin('SetProperty(Button.ID,N/A,home)')
		xbmc.executebuiltin('SetProperty(SubButton.ID,74_93,home)')
		xbmc.executebuiltin('ActivateWindow(1138)')
		xbmc.executebuiltin('SetProperty(Button.ID,'+property_buttonid+',home)')
		xbmc.executebuiltin('SetProperty(SubButton.ID,'+property_subbuttonid+',home)')
		'''---------------------------'''
	elif value == '4':
		xbmc.executebuiltin('SetProperty(Button.ID,N/A,home)')
		xbmc.executebuiltin('SetProperty(SubButton.ID,74_94,home)')
		xbmc.executebuiltin('ActivateWindow(1138)')
		xbmc.executebuiltin('SetProperty(Button.ID,'+property_buttonid+',home)')
		xbmc.executebuiltin('SetProperty(SubButton.ID,'+property_subbuttonid+',home)')
		'''---------------------------'''
	elif value == '5':
		pass
		'''---------------------------'''
	elif value == '6':
		addon = 'plugin.video.hotVOD.video'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '7':
		addon = 'plugin.video.ilten'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '8':
		addon = 'plugin.video.IBA'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '9':
		pass
		'''---------------------------'''
	SubMenuTip(admin)
	
def mode504(value, admin, name, printpoint):
	'''------------------------------
	---YOUTUBE-BUTTON----------------
	------------------------------'''
	if value == '0':
		addon = 'plugin.video.youtube'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	if value == '1':
		addon = 'plugin.video.htptrofl'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '2':
		addon = 'plugin.video.bestofyoutube_com'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '5':
		addon = 'plugin.video.thaakillah'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	SubMenuTip(admin)
		
def mode505(value, admin, name, printpoint):
	'''------------------------------
	---GOPRO-BUTTON------------------
	------------------------------'''
	if value == '0':
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
		'''---------------------------'''
	elif value == '3':
		addon = 'plugin.video.israelsports'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '4':
		addon = 'plugin.video.wweonline'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '5':
		addon = 'plugin.video.nflreplays'
		installaddonP(admin, 'repository.natko1412', update=True)
		installaddon(admin, addon, "")
		xbmc.executebuiltin('RunAddon('+ addon +')')
		'''---------------------------'''
	elif value == '6':
		addon = 'plugin.video.football.today'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	elif value == '7':
		addon = 'plugin.video.nbafullgames'
		installaddonP(admin, 'repository.natko1412', update=True)
		installaddon(admin, addon, "")
		xbmc.executebuiltin('RunAddon('+ addon +')')
		'''---------------------------'''
	elif value == '8':
		addon = 'plugin.video.the666sicco'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
		
	SubMenuTip(admin)

def mode506(value, admin, name, printpoint):
	'''------------------------------
	---MOVIESE-BUTTON----------------
	------------------------------'''
	if value == "0":
		printpoint = printpoint + "5"
		url = 'plugin://plugin.video.genesis/?action=movieNavigator'
		returned = ActivateWindow("1", 'plugin.video.genesis', url, 0, wait=True)
		printpoint = printpoint + moviese_tvshowse(admin, name, printpoint, returned)
		'''---------------------------'''
	elif value == "1":
		'''------------------------------
		---PULSAR------------------------
		------------------------------'''
		addon = 'plugin.video.pulsar'
		installaddon(admin, addon, "")
		installaddonP(admin, addon, "")
		xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.pulsar/movies/,return)')
				
	elif value == "4":
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
	if value == "0":
		printpoint = printpoint + "5"
		url = 'plugin://plugin.video.genesis/?action=tvNavigator'
		returned = ActivateWindow("1", 'plugin.video.genesis', url, 0, wait=True)
		printpoint = printpoint + moviese_tvshowse(admin, name, printpoint, returned)
		'''---------------------------'''
	elif value == "1":
		'''------------------------------
		---PULSAR------------------------
		------------------------------'''
		addon = 'plugin.video.pulsar'
		installaddon(admin, addon, "")
		installaddonP(admin, addon, "")
		xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.pulsar/shows/,return)')
		
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
				if moviesestartup == "0": value = "" #root
				elif moviesestartup == "1": value = addonString_genesis(30027).encode('utf-8') #Most Popular
				elif moviesestartup == "2": value = addonString_genesis(30544).encode('utf-8') #Returning TV Shows
				elif moviesestartup == "3": value = addonString_genesis(30009).encode('utf-8') #Search
				elif moviesestartup == "4": value = addonString_genesis(30021).encode('utf-8') #Genres
				else: value = ""
				if value != "": value = "[" + value + "]"
				'''---------------------------'''
				count = 0
				while count < 17 and containerfolderpath == roottv and value != "" and not xbmc.abortRequested:
					if moviesestartup == "3" and not xbmc.Player().isPlayingVideo(): systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Up)','')
					elif moviesestartup == "3": systemcurrentcontrol = findin_systemcurrentcontrol("0",value,40,'Action(Down)','')
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
					if moviesestartup != "3" and moviesestartup != "3": notification('[COLOR=Yellow]' + value + '[/COLOR]' + localize(512) + space2, localize(75782), "", 4000)
				elif moviesestartup == "3" or moviesestartup == "3": notification('[COLOR=Yellow]' + value + '[/COLOR]' + localize(512) + space2, localize(75782), "", 4000)
		elif admin: notification("containerfolderpath_Error","","",1000)
	
	SubMenuTip(admin)
	return printpoint
	
def mode508(value, admin, name, printpoint):
	'''------------------------------
	---WEATHER-BUTTON----------------
	------------------------------'''
	if value == '0':
		addon = 'weather.yahoo'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('ActivateWindow(MyWeather)')
			xbmc.executebuiltin('Action(Weather.Refresh)')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		'''---------------------------'''

def mode509(value, admin, name, printpoint):
	'''------------------------------
	---PICTURES-BUTTON---------------
	------------------------------'''
	if value == '0':
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
	picturesbutton = xbmc.getCondVisibility('Container(9000).HasFocus(80)')
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
			#HomeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
			#mypicsW = xbmc.getCondVisibility('Window.IsVisible(MyPics.xml)')
			containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
			
			if (HomeW or mypicsW) and mode == 304:
				printpoint = printpoint + "5"
				#xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,)')
				#xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,)')
				if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path0 +')') and rowscountN > 0:
					if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,1)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path1 +')')
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path1 +')') and rowscountN > 1:
					if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path2 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path2 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,2)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path2 +')')
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path2 +')') and rowscountN > 2:
					if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path3 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path3 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,3)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path3 +')')
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path3 +')') and rowscountN > 3:
					if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path4 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path4 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,4)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path4 +')')
					'''---------------------------'''
				elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path4 +')') and rowscountN > 4:
					if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path5 +'/videos/,return)')
					if mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path5 +'/pictures/,return)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVid,5)')
					xbmc.executebuiltin('Skin.SetString(VarCurrentPicVidPath,'+ path5 +')')
					'''---------------------------'''
					
				else:
					#if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path1 +')') and rowscountN == 1 and 1 + 1 == 3:
					printpoint = printpoint + "A"
					if device == "1":
						notification('$LOCALIZE[74546]', '$LOCALIZE[74547]', '', 2000)
						if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
						'''---------------------------'''
					elif HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
					elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
				if 1 + 1 == 3:
					if xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path2 +')') and rowscountN == 2:
						if device == "1":
							if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
					elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path3 +')') and rowscountN == 3:
						if device == "1":
							if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
					elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path4 +')') and rowscountN == 4:
						if device == "1":
							if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
						elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path0 +'/pictures/,return)')
					elif xbmc.getCondVisibility('SubString(Container.FolderPath,'+ path5 +')') and rowscountN == 5:
						if device == "1":
							if HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path1 +'/videos/,return)')
							elif mypicsW: xbmc.executebuiltin('ActivateWindow(Pictures,'+ path1 +'/pictures/,return)')
							'''---------------------------'''
						elif HomeW: xbmc.executebuiltin('ActivateWindow(Video,'+ path0 +'/videos/,return)')
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
			
			if admin: print printfirst + name + "_LV" + printpoint + space + "mypicsW" + space2 + str(mypicsW) + space + "HomeW" + space2 + str(HomeW) + space + "containerfolderpath" + space2 + str(containerfolderpath) + space + "device" + space2 + str(device) + newline + "path1" + space2 + path1 + space + "rowscountN" + space2 + str(rowscountN) + newline + space
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
				
def mode510(value, admin, name, printpoint):
	'''------------------------------
	---GAMES-BUTTON------------------
	------------------------------'''
	if value == '0':
		name2 = localize(15016)

		returned = supportcheck(name2, ["A","A?","B","B?"], 200, platform="13456")
		if returned == "ok":
			addon = 'plugin.program.advanced.launcher'
			if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
				printpoint = printpoint + "7"
				'''---------------------------'''
			else:
				installaddonP(admin, addon)
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
				else: xbmc.executebuiltin('RunScript(script.htpt.emu,,?mode=7)')
				'''---------------------------'''
	elif value == '1':
		'''------------------------------
		---GAMER-TV----------------------
		------------------------------'''
		addon = 'plugin.video.g4tv'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +')')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		
def mode511(admin, name, printpoint):
	'''------------------------------
	---TRAILERS-BUTTON---------------
	------------------------------'''
	pass
	'''---------------------------'''

def mode512(value, admin, name, printpoint):
	'''------------------------------
	---INTERNET-BUTTON---------------
	------------------------------'''
	if value == '0':
		name = localize(443)
		if systemplatformwindows: terminal('start /max www.google.co.il','')
		elif systemplatformandroid: terminal('adb shell am start -a android.intent.action.VIEW -d http://www.google.co.il','')
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

def mode513(value, admin, name, printpoint):
	'''------------------------------
	---VIDEOS-BUTTON-----------------
	------------------------------'''
	if value == '0':
		name2 = str3
		path2 = "videos" 
		pictures_videos(admin, name, printpoint, 513, name2, path2)
		'''---------------------------'''

def mode514(value, admin, name, printpoint):
	'''------------------------------
	---MUSIC-BUTTON------------------
	------------------------------'''
	if value == "0":
		'''------------------------------
		---HTPT-MUSIC--------------------
		------------------------------'''
		addon = 'plugin.video.htpt.music'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +',,)')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		SubMenuTip(admin)
				
	elif value == "1":
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
			
	elif value == "3":
		'''------------------------------
		---LOCAL-MUSIC-------------------
		------------------------------'''

		if libraryhascontentmusic:
			if musiclinkstr == "": xbmc.executebuiltin('ActivateWindow(502,return)')
			else: xbmc.executebuiltin('ActivateWindow(502,'+ musiclinkstr +',return)')
		else:
			xbmc.executebuiltin('ActivateWindow(501,root),return)')
			#xbmc.executebuiltin('ActivateWindow(501),return)')
			xbmc.sleep(1000)
			dialogok('[COLOR=Yellow]' + addonString(120) % (localize(36914).decode('utf-8')) + '[/COLOR]', addonString(147) % (localize(75004).decode('utf-8')), localize(75783), '')
			'''---------------------------'''
			returned = supportcheck(localize(75004), ["A", "B", "A?", "B?"], totalspace=40, Intel=False, silence=False)
			if returned != 'ok': pass
			
	elif value == "4":
		'''------------------------------
		---RADIO-------------------------
		------------------------------'''
		addon = 'plugin.video.israelive'
		if xbmc.getCondVisibility('System.HasAddon(PVR.HasRadioChannels)'):
			xbmc.executebuiltin('ActivateWindow(RadioGuide)')
			
		elif xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			#xbmc.executebuiltin('RunAddon('+ addon +',,)')
			
			if not sgbpvrmanagerenabled: xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.israelive/?categoryid=9999&description&displayname=10000&iconimage=http%3a%2f%2fmdmorrope.gob.pe%2fportalweb%2fimagenes%2fradioss.png&mode=2&name=%5bCOLOR%20chartreuse%5d%5bB%5d%5b%d7%a8%d7%93%d7%99%d7%95%5d%5b%2fB%5d%5b%2fCOLOR%5d&url,return)')
			else: xbmc.executebuiltin('ActivateWindow(MyPVRChannels.xml)') ; notification("Test","","",2000)
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		
	elif value == "6":
		'''------------------------------
		---GUITAR------------------------
		------------------------------'''
		addon = 'plugin.video.ultimateguitar'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
		
def mode515(value, admin, name, printpoint):
	'''------------------------------
	---KIDS-BUTTON-------------------
	------------------------------'''
	if value == "0":
		'''------------------------------
		---HTPT-KIDS---------------------
		------------------------------'''
		addon = 'plugin.video.htpt.kids'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			xbmc.executebuiltin('RunAddon('+ addon +',,)')
			'''---------------------------'''
		else: installaddon(admin, addon, "")
		SubMenuTip(admin)

def mode516(value, admin, name, printpoint):
	'''------------------------------
	---FAVOURITES-BUTTON-------------
	------------------------------'''
	if value == '0':
		xbmc.executebuiltin('ActivateWindow(134)')
		'''---------------------------'''

def mode517(value, admin, name, printpoint):
	'''------------------------------
	---LIVE-TV-BUTTON----------------
	------------------------------'''
	if '0' in value:
		extra = "" ; TypeError = ""
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		if xbmc.getCondVisibility('System.GetBool(pvrmanager.enabled)'):
			printoint = printpoint + "1"
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
					xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=12)')		
		else:
			printpoint = printpoint + "2"
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
	elif '6' in value:
		'''ערוץ הטיולים'''
		addon = 'plugin.video.travel'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	SubMenuTip(admin)
	
def mode518(value, admin, name, printpoint):
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	name = "?"
	mode518(admin, name, printpoint)
	'''---------------------------'''

def mode519(value, admin, name, printpoint):
	'''------------------------------
	---NATURE/SCIENCE-BUTTON---------
	------------------------------'''
	if value == '1':
		addon = 'plugin.video.movixws'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, name, update=True)
		else:
			url = 'plugin://plugin.video.movixws/?iconimage=http%3a%2f%2ficons.iconarchive.com%2ficons%2faaron-sinuhe%2ftv-movie-folder%2f512%2fDocumentaries-National-Geographic-icon.png&mode=2&name=Documentary%20-%20%d7%93%d7%95%d7%a7%d7%95%d7%9e%d7%a0%d7%98%d7%a8%d7%99&url=http%3a%2f%2fwww.movix.me%2fgenres%2fDocumentary'
			returned = ActivateWindow("1", addon, url, 0, wait=True)
			if not 'ok' in returned:
				returned = ActivateWindow("0", addon, url, 0, wait=True)
				'''---------------------------'''
				
	if value == '5':
		addon = 'plugin.video.sdarot.tv'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, name, update=True)
		else:
			url = 'plugin://plugin.video.sdarot.tv/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f11%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&name=%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&summary&url=all-heb'
			returned = ActivateWindow("1", addon, url, 0, wait=True)
			if not 'ok' in returned:
				returned = ActivateWindow("0", addon, url, 0, wait=True)
				'''---------------------------'''
				
	elif value == '6':
		addon = 'plugin.video.ted.talks'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('RunAddon('+ addon +')')
		else: installaddon(admin, addon, "")
		'''---------------------------'''
	

def mode520(value, admin, name, printpoint):
	'''------------------------------
	---ADULT-MOVIE-BUTTON------------
	------------------------------'''
	if value == '0':
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
	pass

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
	
	if "1" in custom:
		adult2 = xbmc.getInfoLabel('Skin.HasSetting(Adult2)')
		if not adult2:
			'''hide adult contents'''
			from variables2 import idT2
			y = idT2.get('89')
			setSkinSetting('1','off'+str(y),"true")
			print "y" + space2 + str(y) + space + "Turned Off"
			#setSkinSetting('0','label'+x,str(labelT.get('label'+y)))
			
	if "0" in custom:
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
		
		addon = 'script.module.unidecode'
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddonP(admin, addon, update=False)
		
		addon = 'service.subtitles.opensubtitles'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(os.path.join(addons_path, addon)):
			'''------------------------------
			-service.subtitles.opensubtitles-
			------------------------------'''
			#addonsettings2(addon,'OSuser',idstr + "@gmail.com",'OSpass',idpstr,'',"",'',"",'',"")
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
			#addonsettings2(addon,'SUBemail',idstr + "@gmail.com",'SUBpassword',idpstr,'',"",'',"",'',"")
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
	
	if "3" in custom:
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
		
		addon = 'plugin.video.dailymotion_com'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			if addonid2 == "" or addonid2 == addon:
				if countrystr == "Israel": pass #setsetting_custom1(addon, 'language',"0")
				elif countrystr == "": pass
				elif "Foreign" in countrystr: setsetting_custom1(addon, 'language',"0")
				addonsettings2(addon,'itemsPerPage',"0",'maxVideoQuality',"2",'downloadDir',"special://userdata/library/downloads/",'forceViewModeNew',"true",'viewModeNew',"50")
				#path = os.path.join(addondata_path, addon, 'kodion', 'cache.sqlite')
				#removefiles(path)
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
				
	if "4" in custom:
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
	
def SubMenuTip(admin):
	if not property_submenutip:
		if scripthtptinstall_Skin_FirstBoot != "true":
			notification_common("25")
			xbmc.executebuiltin('SetProperty(SubMenuTip,true,home)')
			'''---------------------------'''
	