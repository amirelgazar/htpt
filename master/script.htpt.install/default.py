
import xbmc
import os, sys
#import subprocess
#import xbmcgui, xbmcaddon
	
from variables import *
from modules import *
from shared_modules3 import get_params, urlcheck
#url, name, mode, iconimage, desc, num, viewtype = pluginend(admin)

'''---------------------------'''
try: params=get_params()
except Exception, TypeError: pass
mode=None
'''---------------------------'''
try: mode=int(params["mode"])
except: pass
'''---------------------------'''

setGeneral_ScriptON("0", General_ScriptON, str(mode))
if xbmc.getSkinDir() != "skin.htpt":
	setSkinSetting("1",'Admin',"false")
	setSkinSetting("1",'Admin2',"false")
	'''---------------------------'''

if mode == None:
	'''------------------------------
	---MAIN-MENU---------------------
	------------------------------'''
	name = 'MAIN-MENU' ; printpoint = ""
	if General_ScriptON == "true": xbmc.sleep(1000)
	else: printpoint = printpoint + mode0(admin, name, printpoint)

elif mode == 7:
	pass
	'''------------------------------
	---TEST-BUTTON-------------------
	------------------------------'''
	if 1 + 1 == 2:
		returned = dialogkeyboard(scripthtptdebug_User_Name, localize(1014) + space + "(" + addonString_servicehtpt(22) + ")", 0, '1', 'User_Name', 'service.htpt.debug')
	
	if 1 + 1 == 3:
		if os.path.exists(backuppath + backupname + ".zip"):
			notification("Using Restore point", "From Last Backup", "", 4000)
			ExtractAll(backuppath + backupname + ".zip", restorepath)
		
		if os.path.exists(backuppath + backupname2 + ".zip"):
			returned = dialogyesno(addonString(87) % ('guisettings.xml'), addonString(86))
			if returned == 'ok':
				notification("Using Restore point", "From Last Backup", "", 4000)
				printpoint = printpoint + "3"
				ExtractAll(backuppath + backupname2 + ".zip", restorepath)
			else: pass
	if 1 + 1 == 3:
		CreateZip(userdata_path.encode('utf-8'), backuppath + backupname, filteron=['advancedsettings.xml', 'sources.xml', 'keymaps'], filteroff=[], level=0, append=False, ZipFullPath=True, temp=True)
		CreateZip(addondata_path.encode('utf-8'), backuppath + backupname, filteron=['metadata.tvdb.com', 'plugin.video.israelive', 'plugin.video.youtube'], filteroff=[], append="End", ZipFullPath=True, temp=True)
		print backuppath + backupname + ".zip"
		if os.path.exists(backuppath + backupname + ".zip"):
			backupdate = getFileAttribute(1, backuppath + backupname + ".zip")
			returned = dialogyesno("Backup file present!", "There is already backup file made on" + space2 + '[CR]' + '[B]' + str(backupdate) + '[/B]' + ".[CR]" + "Would you like to continue with the previous backup?")
			if returned == 'ok': printpoint = printpoint + "2"
	
elif mode == 14:
	'''------------------------------
	---HELP-BUTTON-------------------
	------------------------------'''
	xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=1)')
	'''---------------------------'''
	
elif mode == 20:
	'''------------------------------
	---INSTALL-BUTTON----------------
	------------------------------'''
	name = 'INSTALL-BUTTON'
	mode20(name, printpoint, backupname, backuppath)
	'''---------------------------'''

elif mode == 21:
	'''------------------------------
	---UNINSTALL-BUTTON--------------
	------------------------------'''
	name = 'UNINSTALL-BUTTON'
	mode21(name, printpoint, backupname, backupname2, backuppath)
	'''---------------------------'''

elif mode == 22:
	'''------------------------------
	---CHANGE-SKIN-BUTTON------------
	------------------------------'''
	name = 'CHANGE-SKIN-BUTTON'
	mode22(name, printpoint)
	'''---------------------------'''

elif mode == 23:
	'''------------------------------
	---ENTER-HTPT-BUTTON-------------
	------------------------------'''
	name = 'ENTER-HTPT-BUTTON'
	mode23(name, printpoint)
	'''---------------------------'''

elif mode == 24:
	'''------------------------------
	---MAIN-SKIN---------------------
	------------------------------'''
	name = 'MAIN-SKIN'
	mode24(name, printpoint)
	'''---------------------------'''
	
elif mode == 27:
	'''------------------------------
	---STARTUP-APPLY-----------------
	------------------------------'''
	name = 'STARTUP-APPLY'
	printpoint = ""
	startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
	while startupW and not xbmc.abortRequested:
		startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
		xbmc.sleep(10000)
		
	idstr_len = len(idstr)
	if xbmc.getSkinDir() == "skin.htpt":
		if (User_ID == "" or User_ID == 'new' or User_ID == 'old') and Skin_Installed != "true" and not os.path.exists(skininstalledtxt2):
			print printfirst + name + space + "mode20" + space + "User_ID" + space2 + str(User_ID)
			#mode20(name, printpoint, backupname, backuppath) #xbmc.executebuiltin('RunScript(script.htpt.install,,?mode=20)')
			Skin_Installed = "true"
	
	else: printpoint = printpoint + "q"
		
	if xbmc.getSkinDir() == "skin.htpt":
		
		setUserID(admin, addonID, User_ID, scripthtptdebug_User_ID, htpt_a1, htpt_a2)
		
		setUserID2(admin, addonID, Skin_DateInstalled, id2str)
		
		setSkinSetting("0",'Skin_Default', Skin_Default)
		
		if Skin_Installed != "true" and not os.path.exists(skininstalledtxt2):
			if skinnamestr != "skin.htpt":
				returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
				count = 0
				while count < 20 and returned_Dialog != "" and not xbmc.abortRequested:
					count += 1
					xbmc.sleep(10000)
					returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
				if count < 20:
					returned = dialogyesno("HTPT Installation 90%","Would you like to finish the installation now?")
					if returned == "ok":
						setsetting('Skin_Installed', "true")
						Skin_Installed = "true"
						setSkinSetting("0",'Skin_Name', "skin.htpt")
						'''---------------------------'''
					else: pass #setSkinSetting("0",'Skin_Name', "skin.htpt")
					
		if Skin_Installed == "true" or os.path.exists(skininstalledtxt2):
			setsetting('Skin_FirstBoot', "true")
			if Skin_Installed != "true":
				setsetting('Skin_Installed', "true")
				setsetting('Skin_DateInstalled', datenowS)
				'''---------------------------'''
			addons = ['service.htpt.fix', 'script.htpt.smartbuttons']
			for addon in addons:
				if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon): printpoint = printpoint + "6"
				else: printpoint = printpoint + "9"
				'''---------------------------'''
			
			if not "9" in printpoint:
				printpoint = printpoint + "7"
				if scripthtptdebug_User_Name != id1str and scripthtptdebug_User_Name != "": setSkinSetting("0", 'ID1', scripthtptdebug_User_Name)
				setsetting_custom1('service.htpt.fix','Fix_5',"true")
				setsetting_custom1('service.htpt.fix','Fix_6',"true")
				setsetting_custom1('service.htpt.fix','Fix_100',"true")
				setsetting_custom1('service.htpt.fix','Fix_101',"true")
				'''---------------------------'''
				xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=59)') ; xbmc.sleep(1000)
				dialogok("Choose your country", "This option will effect the whole system!", localize(75775), "") ; xbmc.sleep(1000)
				
				dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
				dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
				dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
				while dialogokW or dialogyesnoW or dialogselectW and not xbmc.abortRequested:
					dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
					dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
					dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
					xbmc.sleep(1000)
					'''---------------------------'''
				returned = dialogyesno(localize(76177), localize(76178) + localize(75775), yes=True) #Allow sending reports from this device
				if returned == 'ok': setsetting_custom1('service.htpt.debug','General_AllowDebug',"true")
				else: setsetting_custom1('service.htpt.debug','General_AllowDebug',"false")
				'''---------------------------'''
				returned = dialogyesno(localize(79516), localize(79608) + localize(75775)) #User settings
				if returned == 'ok': setSkinSetting("1",'CustomGUI',"true")
				else: setSkinSetting("1",'CustomGUI',"false")
				'''---------------------------'''
				xbmc.executebuiltin('RunScript(script.htpt.install,,?mode=24)')
				dialogok("Choose your default Skin", "The system will force default skin on startup", localize(75775), "") ; xbmc.sleep(500)
				'''---------------------------'''
				dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
				dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
				dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
				while dialogokW or dialogyesnoW or dialogselectW and not xbmc.abortRequested:
					dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
					dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
					dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
					xbmc.sleep(1000)
					'''---------------------------'''
				addon = 'service.htpt.debug'
				if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon): xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=20)')
				dialogok(addonString(89), addonString(82), addonString(88), "") #Installation almost done!
				#xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=3)')
				xbmc.sleep(200) ; startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
				if xbmc.getCondVisibility('Control.HasFocus(8)') + startupW: xbmc.executebuiltin('Action(Select)')
				'''---------------------------'''
				xbmc.sleep(4000)
				xbmc.executebuiltin('Action(reloadkeymaps)')
				setsetting('Skin_Installed', "false")
				if os.path.exists(skininstalledtxt2):
					if systemplatformwindows: terminal('DEL "'+skininstalledtxt2+'" /F /Q >NUL', 'Skin_Installed.txt')
					else: terminal('rm -rf '+skininstalledtxt2+'', 'Skin_Installed.txt')
					'''---------------------------'''
				xbmc.sleep(1000)
				setsetting('Skin_DateInstalled', datenowS)
				setsetting_custom1('service.htpt.debug','ModeOn_20',"true")
				setsetting_custom1('service.htpt.fix','Fix_5',"true")
				setsetting_custom1('service.htpt.fix','Fix_6',"true")
				setsetting_custom1('service.htpt.fix','Fix_100',"true")
				setsetting_custom1('service.htpt.fix','Fix_101',"true")

		elif Skin_FirstBoot != "false":
			setsetting_custom1('service.htpt.debug','ModeOn_20',"true")
			setsetting('Skin_FirstBoot', "false")
			'''---------------------------'''
		else: pass
			
			
		'''---------------------------'''
		'''idstr = USERNAME EN , id1str = USERNAME HE, id2str = INSTALLATION DATE, id3str = WARRENTY END, id4str = ADDRESS, id5str = TELEPHONE NUMBER, id6str = PAYMENT TERMS,
		id7str = QUESTION, id8str = TECHNICAL NAME, id9str = CODE RED, id10str = HTPT'S MODEL, ID11 = MAC1, ID12 = MAC2'''
		if id1str == "":
			 if scripthtptdebug_User_Name != "":
				setSkinSetting("0",'ID1',scripthtptdebug_User_Name)
			 else:
				returned = dialogkeyboard(id1str, localize(1014) + space + "(" + addonString_servicehtpt(22).encode('utf-8') + ")", 0, '1', '', '') #ID1
				if returned != "skip" and returned != "":
					setsetting_custom1('service.htpt.debug','User_Name',returned)
					setSkinSetting("0",'ID1',returned)
				
		if id3str == "": setSkinSetting("0",'ID3',"None") #ID3
		if id6str == "": setSkinSetting("0",'ID6',"None") #ID6
		if id7str != "": setSkinSetting("0",'ID7',"") #ID7
		if id8str == "": setSkinSetting("0",'ID8',"None") #ID8
		if id9str == "": setSkinSetting("0",'ID9',"") #ID9
		#if id10str == "": setSkinSetting("0",'ID10','UNKNOWN') #ID10
		'''---------------------------'''
		if mac1str == "" or admin and not systemplatformwindows:
			MAC1_ = terminal("ifconfig -a | grep -e 'eth' | awk {'print $5'}","LAN MAC")
			if MAC1_ != "" and MAC1_ != None:
				MAC1_ = MAC1_.replace("\n","")
				setSkinSetting("0",'MAC1',MAC1_)
				'''---------------------------'''
		if mac2str == "":
			MAC2_ = terminal("ifconfig -a | grep -e 'wlan' | awk {'print $5'}","WLAN MAC")
			if MAC2_ != "" and MAC2_ != None:
				MAC2_ = MAC2_.replace("\n","")
				setSkinSetting("0",'MAC2',MAC2_)
				'''---------------------------'''
	else: printpoint = printpoint + "9"
	'''---------------------------'''
	
#xbmc.executebuiltin('Container.Refresh')
#xbmc.executebuiltin('Container.Update')
if TypeError != "": extra = space + "TypeError" + space2 + str(TypeError)
print printfirst + "default.py_LV" + printpoint + space + "mode" + space2 + str(mode) + space + "name" + space2 + str(name) + extra
setGeneral_ScriptON("1", General_ScriptON, str(mode))


#pluginend2(admin, containerfolderpath, viewtype)