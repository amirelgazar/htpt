# -*- coding: utf-8 -*-
#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys
import xbmcplugin
import urllib
import urllib2
import re

from variables import *
from shared_modules import *
from shared_modules3 import addDir
from shared_modules4 import guikeeper

def mode0(admin, name, printpoint):
	TypeError = "" ; extra = ""
	try:
		systemmemorytotal2 = systemmemorytotal.replace("MB","")
		if systemmemorytotal2 >= 384: pass
		else:
			printpoint = printpoint + "9"
			dialogok("Memory Warning!", "Your hardware don't have enough memory ram" + "(" + str(systemmemorytotal2) + ")", "Make sure you have atleast 384MB of free memory ram.","")
		extra = extra + newline + "systemmemorytotal2" + space2 + str(systemmemorytotal2)
	except Exception, TypeError: 
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		dialogok("Memory Warning!", "Unable to obtain required hardware information.", "Make sure you have atleast a total of 1GB of memory ram.","")
	
	printpoint = printpoint + installaddon2(admin, 'repository.htpt', update=True)
	if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'service.htpt', update=True)
	if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'service.htpt.debug', update=True)
	'''---------------------------'''
	
	if not "8" in printpoint and not "9" in printpoint:
		if "5" in printpoint:
			notification("PROCEEDING PLEASE WAIT...","","",2000)
			xbmc.sleep(1000)
			printpoint = printpoint + "7"
			'''---------------------------'''
	
		CATEGORIES()
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
		'''---------------------------'''
	
	print printfirst + name + "_LV" + printpoint + space + extra
	return printpoint
	
def CATEGORIES():

	addon = 'skin.htpt'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon):
		if xbmc.getSkinDir() == addon:
			addDir(addonString(11).encode('utf-8'),'',21,htptservicemedia_path + 'bin.png',addonString(101).encode('utf-8'),'1',500) #הסרת מערכת
			#addDir(addonString(12).encode('utf-8'),'',22,htptservicemedia_path + 'linkbroken.png',addonString(102).encode('utf-8'),'1',500) #החלפת סקין
			'''---------------------------'''
			if admin and not admin2:
				addDir("Test7",'',7,htptservicemedia_path + 'caa2.png','','1',500) #Test
		else:
			try: addDir(addonString(13).encode('utf-8'),'',23,htptservicemedia_path + 'htpt.png',addonString(103).encode('utf-8'),'1',500) #כניסה ל-HTPT
			except: pass
			'''---------------------------'''
	else:
		addDir(addonString(10).encode('utf-8'),'',20,htptservicemedia_path + 'software.png',addonString(100).encode('utf-8'),'1',500) #התקנת מערכת
		'''---------------------------'''
		
	addon = 'service.htpt.debug'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon):
		addDir(addonString(14).encode('utf-8'),'',14,htptservicemedia_path + 'help.png',addonString(104).encode('utf-8'),'1',500) #עזרה
	
	#xbmc.executebuiltin('Container.Refresh')

def setUserID(admin, addonID, User_ID, User_ID2, htpt_a1, htpt_a2):
	'''------------------------------
	---APPLY-USER-ID-----------------
	------------------------------'''
	#from shared_variables import htpt_a1, htpt_a2
	name = 'APPLY-USER-ID' ; printpoint = "" ; returned = ""
	User_ID_len = len(User_ID)
	User_ID2_len = len(User_ID2)

	if 'finalmakerr' in User_ID or admin3: pass
	elif 'htpt' in User_ID and User_ID_len == 11:
		setsetting_custom1('service.htpt.debug','User_ID',User_ID)
		setSkinSetting('0','User_ID',User_ID)
	elif 'htpt' in User_ID2 and User_ID2_len == 11:
		if addonID == 'script.htpt.install': setsetting('User_ID',User_ID2)
		else: setsetting_custom1(addonID,'User_ID',User_ID2)
		setSkinSetting('0','User_ID',User_ID2)
	else:
		printpoint = printpoint + "4"
		returned, value = getRandom("0", min=1000000, max=7000000, percent=50)
		setsetting_custom1('service.htpt.debug','User_ID',htpt_a1 + str(value))
		if addonID == 'script.htpt.install':
			setsetting('User_ID',htpt_a1 + str(value))
			setsetting('Skin_Installed','true')
			'''---------------------------'''
		else:
			setsetting_custom1(addonID,'User_ID',htpt_a1 + str(value))
			setsetting_custom1(addonID,'Skin_Installed',htpt_a1 + 'true')
			'''---------------------------'''
		setSkinSetting('0','User_ID',htpt_a1 + str(value))
		xbmc.sleep(100)
	
	
		
	print printfirst + name + "_LV" + printpoint + space + "addonID" + space2 + str(addonID) + space + "User_ID" + space2 + str(User_ID) + space + "User_ID2" + space2 + str(User_ID2) + newline + \
		"User_ID_len" + space2 + str(User_ID_len) + space + "User_ID2_len" + space2 + str(User_ID2_len) + newline + \
		"htpt_a1" + space2 + str(htpt_a1) + space + "htpt_a2" + space2 + str(htpt_a2)
		
def setUserID2(admin, addonID, Skin_DateInstalled, id2str):
	printpoint = ""
	try:
		'''------------------------------
		---APPLY-USER-ID2----------------
		------------------------------'''
		name = 'APPLY-USER-ID2'

		if Skin_DateInstalled == "" and id2str == "":
			printpoint = printpoint + "2"
			setSkinSetting("0",'ID2', datenowS)
			if addonID == 'script.htpt.install': setsetting('Skin_DateInstalled', datenowS)
			else: setsetting_custom1(addonID, 'Skin_DateInstalled', datenowS)
				
		elif Skin_DateInstalled == "":
			printpoint = printpoint + "3"
			if addonID == 'script.htpt.install': setsetting('Skin_DateInstalled', id2str)
			else: setsetting_custom1(addonID, 'Skin_DateInstalled', id2str)
		elif id2str == "": setSkinSetting("0",'ID2', Skin_DateInstalled)
		else:
			Skin_DateInstalled_ = Skin_DateInstalled.replace("-", "")
			id2str_ = id2str.replace("-", "")
			if int(Skin_DateInstalled_) > int(id2str_):
				printpoint = printpoint + "5"
				if addonID == 'script.htpt.install': setsetting('Skin_DateInstalled', id2str)
				else: setsetting_custom1(addonID, 'Skin_DateInstalled', id2str)
			elif int(Skin_DateInstalled_) < int(id2str_): setSkinSetting("0",'ID2', Skin_DateInstalled)
			else: printpoint = printpoint + "6"
			'''---------------------------'''
			
	except Exception, TypeError: print printfirst + name + space + "TypeError" + space2 + str(TypeError)
	
def mode20(name, printpoint, backupname, backuppath):
	'''------------------------------
	---INSTALL-BUTTON----------------
	------------------------------'''
	if not systemplatformwindows and not systemplatformlinux and not systemplatformlinuxraspberrypi: dialogok(addonString(97),addonString(96) + space2, "1. OpenELEC[CR]2. Windows","")
	else:
		
		if xbmc.getSkinDir() != 'skin.htpt':
			try:
				printpoint = printpoint + mode0(admin, name, printpoint)
				returned = dialogkeyboard(scripthtptdebug_User_Name, localize(1014) + space + "(" + addonString_servicehtpt(22).encode('utf-8') + ")", 0, '1', 'User_Name', 'service.htpt.debug') #ID1
			except: returned = 'ok'
		else: returned = 'ok'
		
		if returned == 'skip':
			notification_common("8")
			printpoint = printpoint + "8"
		else:
			'''---------------------------'''
			
			if xbmc.getSkinDir() != 'skin.htpt':
				dialogok(addonString(93), addonString(94), "", "") #Backup Current System
				CreateZip(userdata_path.encode('utf-8'), backuppath + backupname2, filteron=['guisettings.xml'], filteroff=[], level=0, append=False, ZipFullPath=True, temp=False)
			
				if os.path.exists(backuppath + backupname + ".zip"):
					backupdate = getFileAttribute(1, backuppath + backupname + ".zip")
					returned = dialogyesno("Backup file present!", "There is already backup file made on" + space2 + '[CR]' + '[B]' + str(backupdate) + '[/B]' + ".[CR]" + "Would you like to continue with the previous backup?")
					if returned == 'ok': printpoint = printpoint + "2"
			else: printpoint = printpoint + "2"
			
			if not "2" in printpoint:
				notification(addonString(93), ".", "", 1000)
				
				setSkinSetting("1",'ShowDialog',"true")
				dp = xbmcgui.DialogProgress()
				dp.create("HTPT Backup", "Starting", " ")
				dp.update(0,"Starting"," ")
				'''---------------------------'''
				if not dp.iscanceled(): CreateZip(userdata_path.encode('utf-8'), backuppath + backupname, filteron=['advancedsettings.xml', 'sources.xml', 'keymaps'], filteroff=[], level=0, append=False, ZipFullPath=True, temp=True)
				dp.update(10,"Starting."," ")
				if not dp.iscanceled() and not systemplatformwindows: CreateZip(emulators_path, backuppath + backupname, filteroff=['retroarch'], append=True, ZipFullPath=True, temp=True)
				dp.update(20,"Starting.."," ")
				
				if not dp.iscanceled() and not systemplatformwindows: CreateZip(config_path, backuppath + backupname, filteron=['samba.conf', 'autostart.sh'], level=0, append=False, ZipFullPath=True, temp=True)
				dp.update(30,"Starting..."," ")
				'''ADDONS ONLY'''
				dp.update(40,"Addons"," ")
				if not dp.iscanceled(): CreateZip(addons_path.encode('utf-8'), backuppath + backupname, filteron=['repository.lambda', 'repository.xbmc-israel', 'repository.unofficial.addon.pro', 'repository.xbmcadult', 'repository.xunitytalk', 'repository.superrepo.org.helix.all'], filteroff=[], append=True, ZipFullPath=True, temp=True)
				'''ADDONS'''
				dp.update(60,"Addons."," ")
				if not dp.iscanceled(): CreateZip(addons_path.encode('utf-8'), backuppath + backupname, filteron=['script.openelec.rpi.config', 'plugin.video.p2p-streams', 'plugin.video.vdubt', 'plugin.program.advanced.launcher', 'weather.yahoo', 'metadata.universal', 'metadata.common.impa.com', 'metadata.common.movieposterdb.com', 'metadata.common.ofdb.de', 'metadata.common.port.hu', 'metadata.common.rt.com', 'plugin.video.genesis', 'plugin.video.bestofyoutube_com', 'service.skin.widgets'], filteroff=[], append=True, ZipFullPath=True, temp=True)
				'''USERDATA ADDONS'''
				dp.update(80,"Addons.."," ")
				if not dp.iscanceled(): returned = CreateZip(addondata_path.encode('utf-8'), backuppath + backupname, filteron=['script.openelec.rpi.config', 'plugin.video.p2p-streams', 'plugin.video.vdubt', 'plugin.program.advanced.launcher', 'weather.yahoo', 'metadata.universal', 'plugin.video.genesis', 'plugin.video.bestofyoutube_com', 'service.skin.widgets'], filteroff=[], append=True, ZipFullPath=True, temp=True)
				'''USERDATA ONLY ADDONS'''
				dp.update(90,"Addons..."," ")
				if not dp.iscanceled(): returned = CreateZip(addondata_path.encode('utf-8'), backuppath + backupname, filteron=['metadata.tvdb.com', 'plugin.video.israelive', 'plugin.video.youtube'], filteroff=[], append="End", ZipFullPath=True, temp=True)
				
				
				if dp.iscanceled(): printpoint = printpoint + "8"
				setSkinSetting("1",'ShowDialog',"false")
				dp.close
			
			if "8" in printpoint: dialogok('$LOCALIZE[16200]', '$LOCALIZE[114]!', "", "") #Operation was aborted, Installation failed
			else:
				if returned != 'ok' and xbmc.getSkinDir() != 'skin.htpt':
					returned = dialogyesno("Backup Failed", "Proceed without backup? + '[CR]' + 'You should choose no :)')")
					if returned == 'ok': printpoint = printpoint + "4"
					else: notification_common("9")
					'''---------------------------'''
				else: printpoint = printpoint + "4"
				'''---------------------------'''
					
				if "4" in printpoint:
					dp = xbmcgui.DialogProgress()
					dp.create("HTPT Install", "1/10", " ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'service.htpt.debug', update=False) ; dp.update(10,"2/10"," ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'service.htpt.fix', update=False) ; dp.update(20,"3/10"," ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'script.htpt.smartbuttons', update=False) ; dp.update(30,"4/10"," ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'script.htpt.remote', update=False) ; dp.update(40,"5/10"," ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'script.htpt.refresh', update=False) ; dp.update(50,"6/10"," ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'script.htpt.widgets', update=False) ; dp.update(60,"7/10"," ")
					#if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddonP(admin, 'metadata.universal') ; dp.update(70,"8/10"," ")
					#if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'metadata.common.imdb.com', update=False) ; dp.update(80,"9/10"," ")
					if not "8" in printpoint and not "9" in printpoint and not dp.iscanceled(): printpoint = printpoint + installaddon2(admin, 'skin.htpt', update=True) ; dp.update(90,"10/10"," ")
					'''---------------------------'''
				try: dp.close
				except: pass
				
				if "5" in printpoint:
					xbmc.executebuiltin("UpdateLocalAddons")
					xbmc.sleep(2000)
					'''---------------------------'''
				
				if (not "8" in printpoint and not "9" in printpoint) or (xbmc.getSkinDir() == 'skin.htpt' and skinnamestr != 'skin.htpt'):
					'''------------------------------
					---INSTALLATION-SUCCESSFULLY-----
					------------------------------'''
					htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)')
					printpoint = printpoint + "7"
					'''---------------------------'''
					setsetting('Skin_DateInstalled', datenowS)
					setsetting('Skin_Installed', "true")
					if os.path.exists(skininstalledtxt): copyfiles(skininstalledtxt, home_path) #GAL TEST THIS!
					setsetting_custom1('service.htpt.debug','ModeOn_20',"true")
					setsetting_custom1('service.htpt.fix','Fix_5',"true")
					setsetting_custom1('service.htpt.fix','Fix_6',"true")
					setsetting_custom1('service.htpt.fix','Fix_100',"true")
					setsetting_custom1('service.htpt.fix','Fix_101',"true")
					#setsetting_custom1('service.htpt','Skin_Name',"skin.htpt")
					'''---------------------------'''
					if xbmc.getSkinDir() != 'skin.htpt':
						xbmc.executebuiltin('ReplaceWindow(0)')
						xbmc.sleep(1000)
						dialogok(addonString(91), addonString(92) % (htptversion), "", "")
						#xbmc.sleep(1000)
						guikeeper(admin, guicheck="", guiread="") #GAL TEST THIS
						#xbmc.sleep(1000)
						#killall(admin, custom="1")
					#os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copyskin.sh')
					'''---------------------------'''
					#xbmc.sleep(1000)
					#terminal('pgrep kodi.bin | xargs kill -SIGSTOP && killall -9 kodi.bin && sleep 1 && pgrep kodi.bin | xargs kill -SIGCONT',"SOFT-RESTART")
					#xbmc.executebuiltin('XBMC.Reset()')
					'''---------------------------'''
				
				else:
					if "55" in printpoint: extra = addonString(85) + '[CR]' + addonString(84)
					else: extra = ""
					if not "8" in printpoint: dialogok('$LOCALIZE[113]', localize(257) + space + printpoint, extra, "")
			
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + name + "_LV" + printpoint + space + "idstr" + space2 + idstr + space + "MAC" + space2 + macstr
		'''---------------------------'''

def mode21(name, printpoint, backupname, backupname2, backuppath):
	'''------------------------------
	---UNINSTALL-BUTTON--------------
	------------------------------'''
	
	returned = dialogyesno(addonString(11),addonString(98))
	if returned == 'ok':
		'''------------------------------
		---REMOVE------------------------
		------------------------------'''
		if not systemplatformwindows and not systemplatformlinux and not systemplatformlinuxraspberrypi: dialogok("Uninstall isn't available for your OS!","", addonString(80),"")
		else:
			if os.path.exists(backuppath + backupname + ".zip"):
				backupsize = getFileAttribute(2, backuppath + backupname + ".zip")
				try:
					if int(backupsize) > 24000: pass
					else: printpoint = printpoint + "b"
				except Exception, TypeError:
					printpoint = printpoint + "b"
			else:
				printpoint = printpoint + "b"
				
			notification("Removing",'Please Wait',"",10000)
			setSkinSetting("1",'ShowDialog',"true")
			dp = xbmcgui.DialogProgress()
			dp.create("HTPT Uninstaller", "Removing Scripts", " ")
			'''---------------------------'''
			
			if not admin: removefiles(os.path.join(config_path, 'samba.conf'))
			removefiles(os.path.join(config_path, 'autostart.sh'))
			'''---------------------------'''
			removefiles('/storage/*.log')
			#removefiles(skin_userdata_path)
			removefiles(os.path.join(config_path, 'sources.xml'))
			'''---------------------------'''
			dp.update(10,"Removing Scripts."," ")
			removefiles(os.path.join(userdata_path, 'advancedsettings.xml'))
			removefiles(os.path.join(userdata_path, 'sources.xml'))
			'''---------------------------'''
			removefiles(keymaps_path)
			'''---------------------------'''
			if not systemplatformwindows: 
				try:
					terminal('mount -o remount,rw /flash','mount flash')
					removefiles('/flash/oemsplash.png')
					'''---------------------------'''
				except: pass
				
			dp.update(20,"Removing Scripts.."," ")
			removefiles(emulators_path)
			dp.update(30,"Removing Scripts..."," ")
			'''------------------------------
			---USERDATA+PACKAGE--------------
			------------------------------'''
			addonsL = []
			
			addonsL.append('plugin.video.israelive')
			addonsL.append('plugin.video.genesis')
			addonsL.append('plugin.video.youtube')
			addonsL.append('plugin.video.p2p-streams')
			addonsL.append('metadata.tvdb.com')
			'''---------------------------'''
			dp.update(50,"Removing HTPT Addons"," ")
			removeaddons(addonsL,"23")
			'''---------------------------'''
			
			'''------------------------------
			---ALL---------------------------
			------------------------------'''
			addonsL = []
			
			addonsL.append('repository.xunitytalk')
			#addonsL.append('repository.xbmc-israel')
			#addonsL.append('script.favourites')
			addonsL.append('repository.unofficial.addon.pro')
			addonsL.append('repository.xbmcadult')
			addonsL.append('repository.superrepo.org.helix.all')
			addonsL.append('plugin.program.advanced.launcher')
			addonsL.append('metadata.universal') ; addonsL.append('metadata.common.port.hu') ; addonsL.append('metadata.common.ofdb.de') ; addonsL.append('metadata.common.movieposterdb.com') ; addonsL.append('metadata.common.impa.com') ; addonsL.append('metadata.common.rt.com')
			addonsL.append('browser.chromium-browser')
			addonsL.append('plugin.video.bestofyoutube_com')
			addonsL.append('screensaver.randomtrailers')
			addonsL.append('screensaver.picture.slideshow')
			addonsL.append('script.moviequiz')
			addonsL.append('emulator.retroarch')
			addonsL.append('service.htpt.fix')
			addonsL.append('script.openelec.rpi.config')
			#addonsL.append('plugin.video.vdubt')
			#addonsL.append('repository.lambda')
			#addonsL.append('repository.htpt')
			addonsL.append('plugin.video.htpt.gopro')
			#addonsL.append('plugin.video.htpt.kids')
			addonsL.append('plugin.video.htpt.music')
			'''---------------------------'''
			dp.update(60,"Removing HTPT Addons."," ")
			removeaddons(addonsL,"123")
			'''---------------------------'''
			addonsL = []
			addonsL.append('service.htpt.debug')
			addonsL.append('script.htpt.emu')
			addonsL.append('script.htpt.homebuttons')
			addonsL.append('script.htpt.smartbuttons')
			addonsL.append('script.htpt.refresh')
			addonsL.append('script.htpt.remote')
			addonsL.append('script.htpt.widgets')
			
			dp.update(70,"Removing HTPT Addons.."," ")
			removeaddons(addonsL,"123")
			'''---------------------------'''
			setsetting('User_ID', 'old')
			setSkinSetting('0', 'Skin_Name', "")
			'''---------------------------'''
			addonsL = []
			addonsL.append('skin.htpt')
			#addonsL.append('service.htpt')
			
			dp.update(80,"Removing HTPT Addons..."," ")
			try: removeaddons(addonsL,"123")
			except Exception, TypeError:
				print "Uninstall htpt.service/skin - TypeError(1): " + str(TypeError)
				try: removeaddons(addonsL,"123")
				except Exception, TypeError: print "Uninstall htpt.service/skin - TypeError(2): " + str(TypeError)
				'''---------------------------'''
			#from variables import *
			if systemhasaddon_htptdebug: xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=21)')
			dp.update(90,"Almost Done!","Please Wait")
			
			if os.path.exists(backuppath + backupname + ".zip"):
				notification("Using Restore point", "From Last Backup", "", 4000)
				ExtractAll(backuppath + backupname + ".zip", restorepath)
			
			if os.path.exists(backuppath + backupname2 + ".zip"):
				returned = dialogyesno(addonString(87) % ('guisettings.xml'), addonString(86))
				if returned == 'ok':
					notification("Using Restore point", "From Last Backup", "", 4000)
					printpoint = printpoint + "3"
				else: pass
			
			if not "3" in printpoint: xbmc.executebuiltin('SetGUILanguage(English)')
			

			dp.close
			
			dialogok(addonString(83),"","","")
			
				
			
			xbmc.executebuiltin("UpdateLocalAddons")
			xbmc.executebuiltin('ReplaceWindow(0)')
			
			xbmc.sleep(1000)
			if "3" in printpoint: ExtractAll(backuppath + backupname2 + ".zip", restorepath)
			killall(admin, custom="")
			#terminal('pgrep kodi.bin | xargs kill -SIGSTOP && killall -9 kodi.bin && sleep 1 && pgrep kodi.bin | xargs kill -SIGCONT',"SOFT-RESTART")
			'''---------------------------'''
	else:
		notification_common("9")
		'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + "_LV" + printpoint
	'''---------------------------'''
	
def mode22(name, printpoint):
	'''------------------------------
	---CHANGE-SKIN-BUTTON------------
	------------------------------'''
	
	xbmc.executebuiltin('ActivateWindow(AppearanceSettings)')
	xbmc.sleep(1000)
	if xbmc.getCondVisibility('System.IdleTime(1)') and xbmc.getInfoLabel('System.CurrentControl') == localize(166):
		xbmc.executebuiltin('Action(Select)') ; xbmc.sleep(40) ; xbmc.executebuiltin('Action(Down)') ; xbmc.sleep(40) ; xbmc.executebuiltin('Action(Select)') ; xbmc.sleep(200) ; xbmc.executebuiltin('Action(Down)')
	#dialogok('[COLOR=Yellow]'+'$LOCALIZE[78955]'+'[/COLOR]','$LOCALIZE[78954]','$LOCALIZE[78953]',"")
	'''---------------------------'''
	
def mode23(name, printpoint):
	'''------------------------------
	---ENTER-HTPT-BUTTON-------------
	------------------------------'''
	printpoint = printpoint + installaddon2(admin, 'script.htpt.smartbuttons', update=True)
	#xbmc.executebuiltin('ReloadSkin()')
	#killall(admin, custom="1")
	guikeeper(admin, guicheck="", guiread="") #GAL TEST THIS
	#if not systemplatformwindows: os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copyskin.sh')
	#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=50)')
	#UnloadSkin()
	'''---------------------------'''

def mode24(name, printpoint):
	'''------------------------------
	---MAIN-SKIN---------------------
	------------------------------'''
	list = ['-> (Exit)', 'HTPT', 'OTHER']
	if Skin_Default != "0" and Skin_Default != "1" and Skin_Default != "2":
		list.remove(list[0])
	
	returned, value = dialogselect('$LOCALIZE[74433]',list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
		
	if "7" in printpoint or value == 'HTPT':
		if value != "":
			setSkinSetting('0', 'Skin_Default', value)
			setsetting_custom1('script.htpt.install','Skin_Default', value)
			notification("Your default skin is:", str(value), "", 2000)	
	
	print printfirst + name + "_LV" + printpoint + space + "list" + space2 + str(list) + space + "returned" + space2 + str(returned)
	'''---------------------------'''
	