import xbmc, xbmcgui, xbmcaddon
import os, subprocess, sys

from variables import *
from shared_modules import *
#from shared_modules2 import *
'''------------------------------
---service.htpt.fix--------------
------------------------------'''
			
def setSkinSetting_startup(admin):
	if systemplatformwindows and ((scripthtptdebug_Info_SystemName == 'GAL-PC' or scripthtptdebug_Info_Model == "Intel(R) Core(TM) i7-4700HQ CPU @ 2.40GHz") or scripthtptinstall_User_ID == 'finalmakerr'):
		setSkinSetting("1",'Admin3',"true")
	else:
		setSkinSetting("1",'Admin',"false")
		setSkinSetting("1",'Admin3',"false")
	
	if xbmc.getSkinDir() == 'skin.htpt':
		'''------------------------------
		---skin.htpt---------------------
		------------------------------'''
		
		setSkinSetting5("0",'VarCurrentPicVidPath',"", 'VarCurrentPicVid', "", 'MessagesCustom', "", 'DialogSelectSources7', "", '', "")
		'''---------------------------'''
		setSkinSetting5("1",'',"", '',"", 'MoviesShelfWL',"true", '', "", 'trailers', "false")
		'''---------------------------'''
		if scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true":
			if countrystr == "": setSkinSetting("0", 'Country', "Israel")
			'''---------------------------'''
		if not adult2: setSkinSetting("1",'adult',"false")
		if not moviesestartup: setSkinSetting("0",'moviesestartup',"1")
		if not tvshowsestartup: setSkinSetting("0",'tvshowsestartup',"1")
		
		setSkinSetting("1",'musicseptip',"true")
		setSkinSetting("1",'kidseptip',"true")
		setSkinSetting("1",'ShowDialog',"false")
		if macaddress and macaddress != localize(503):
			setSkinSetting("0",'MAC', macaddress)
		setSkinSetting("0",'musicseptip',"true")
		'''---------------------------'''
	
def Mode_20(admin, name, printpoint, scripthtptdebug_Info_TotalSpace, scripthtptdebug_Info_TotalMemory, scripthtptdebug_Info_Model, scripthtptdebug_Info_Intel):
	'''------------------------------
	---setAdvancedSettings-----------
	------------------------------'''
	if not customas:
		copyfiles(os.path.join(htptservicecopy_path,'manual','advancedsettings.xml'), userdata_path)

		xbmc.sleep(1000)
		if os.path.exists(userdata_path + "advancedsettings.xml"):
			printpoint = printpoint + "7"
			try: scripthtptdebug_Info_TotalSpaceN = int(scripthtptdebug_Info_TotalSpace)
			except: scripthtptdebug_Info_TotalSpaceN = 0
			
			try: scripthtptdebug_Info_TotalMemoryN = int(scripthtptdebug_Info_TotalMemory)
			except: scripthtptdebug_Info_TotalMemoryN = 0
			
			infile = os.path.join(userdata_path,'advancedsettings.xml')
			infile_ = read_from_file(infile, silent=False)
			
			'''---------------------------'''
			x = 'enablerssfeeds' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			if xbmc.getSkinDir() != 'skin.htpt': new_word = '<'+x+'>true</'+x+'>'
			else: new_word = '<'+x+'>false</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'loglevel'
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			if scripthtptdebug_Info_TotalMemoryN < 2000 and performance and scripthtptdebug_General_AllowDebug != "true": new_word = '<'+x+'>-1</'+x+'>'
			elif admin3 and admin and admin2: new_word = '<'+x+'>1</'+x+'>'
			else: new_word = '<'+x+'>0</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'cachemembuffersize' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			new_word = '<'+x+'>0</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'readbufferfactor' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			new_word = '<'+x+'>4.0</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'fanartres' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			if scripthtptdebug_Info_TotalSpaceN > 250: new_word = '<'+x+'>1080</'+x+'>'
			else: new_word = '<'+x+'>720</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'imageres' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			if scripthtptdebug_Info_TotalSpaceN > 250: new_word = '<'+x+'>1080</'+x+'>'
			else: new_word = '<'+x+'>480</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'packagefoldersize' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			if scripthtptdebug_Info_TotalSpaceN > 250: new_word = '<'+x+'>250</'+x+'>'
			else: new_word = '<'+x+'>40</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
			
			'''---------------------------'''
			x = 'skiploopfilter' 
			old_word = regex_from_to(infile_, '<'+x+'>', '</'+x+'>', excluding=False)
			if ('i3' in scripthtptdebug_Info_Model or 'i5' in scripthtptdebug_Info_Model or 'i7' in scripthtptdebug_Info_Model) and scripthtptdebug_Info_TotalMemoryN > 2000: new_word = '<'+x+'>0</'+x+'>'
			else: new_word = '<'+x+'>8</'+x+'>'
			replace_word(infile,old_word,new_word)
			'''---------------------------'''
		else: printpoint = printpoint + "8"
	else: printpoint = printpoint + "9"
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + "_LV" + printpoint + space
	'''---------------------------'''
	Mode_20plus(admin)
	
def Mode_20plus(admin):
	name = 'Mode_20plus' ; printpoint = ""
	if not customasources: copyfiles(os.path.join(htptservicecopy_path, 'manual', 'sources.xml'), userdata_path)
	if not customkeymaps: copyfiles(os.path.join(htptservicecopy_path, 'manual', 'keymaps', '', '*'), keymaps_path)
	'''---------------------------'''
	addon = 'service.openelec.settings'
	if not systemplatformwindows and xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		if not customgui and scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true":
			copyfiles(os.path.join(htptservicecopy_path, 'manual', 'config', '*'), config_path, chmod='+x')
			#if not os.path.exists(flash_path + '/oemsplash.png'): copyfiles(os.path.join(htptservicecopy_path, 'manual', 'flash', '*'), flash_path, mount=True) ; printpoint = printpoint + "4"
			copyfiles(os.path.join(htptservicecopy_path, 'manual', 'addon_data', 'service.openelec.settings', '*'), os.path.join(addondata_path,'service.openelec.settings'))
			'''---------------------------'''
	copyfiles(os.path.join(htptservicecopy_path, 'manual', 'addon_data', 'screensaver.randomtrailers', '*'), os.path.join(addondata_path, 'screensaver.randomtrailers'))
				
	if os.path.exists(os.path.join(htptservicecopy_path, 'once', '')):
		printpoint = printpoint + "3"
		copyfiles(os.path.join(htptservicecopy_path,'once', '*'), home_path)
		if scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true": removefiles(os.path.join(htptservicecopy_path, 'once', '*'))
		'''---------------------------'''
	
	print printfirst + name + "_LV" + printpoint + space
	
def ID_Rewrite(idstr_, htptfixversion_, Addon_Version, htptfixversion, idstr2, id1str2, id2str2, id3str2, id4str2, id5str2, id6str2, id7str2, id8str2, id9str2, id10str2, id11str2, id12str2):
	'''------------------------------
	---***---------------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	
	if (Addon_Version != htptfixversion and htptfixversion == htptfixversion_) and idstr_ == idstr:
		idstr2 = idstr2.replace("idstr=", "").encode('utf-8')
		id1str2 = id1str2.replace("id1str=", "").encode('utf-8')
		id2str2 = id2str2.replace("id2str=", "").encode('utf-8')
		id3str2 = id3str2.replace("id3str=", "").encode('utf-8')
		id4str2 = id4str2.replace("id4str=", "").encode('utf-8')
		id5str2 = id5str2.replace("id5str=", "").encode('utf-8')
		id6str2 = id6str2.replace("id6str=", "").encode('utf-8')
		id7str2 = id7str2.replace("id7str=", "").encode('utf-8')
		id8str2 = id8str2.replace("id8str=", "").encode('utf-8')
		id9str2 = id9str2.replace("id9str=", "").encode('utf-8')
		id10str2 = id10str2.replace("id10str=", "").encode('utf-8')
		id11str2 = id11str2.replace("id11str=", "").encode('utf-8')
		id12str2 = id12str2.replace("id12str=", "").encode('utf-8')
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
		'''---------------------------'''
		print printfirst + "ID_Rewrite: " + datenowS + space
		'''---------------------------'''
		
def setFix_(idstr_, htptfixversion_, noidstr_, Addon_Version, htptfixversion, Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_6, _Fix_7, Fix_8, Fix_9, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104):
	'''------------------------------
	---APPLY-FIXS--------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	printpoint = ""
	if Addon_Version != htptfixversion:
		printpoint = printpoint + "1"
		if htptfixversion == htptfixversion_:
			printpoint = printpoint + "2"
			if (idstr_ == scripthtptinstall_User_ID or idstr_ == "N/A"):
				printpoint = printpoint + "3"
				if not scripthtptinstall_User_ID in noidstr_:
					printpoint = printpoint + "7"
					'''CHOOSEN FIXS TO APPLY'''
					if "true" in Fix_1: setsetting('Fix_1',"true")
					if "true" in Fix_2: setsetting('Fix_2',"true")
					if "true" in Fix_3: setsetting('Fix_3',"true")
					if "true" in Fix_4: setsetting('Fix_4',"true")
					if "true" in Fix_5: setsetting('Fix_5',"true")
					if "true" in Fix_6: setsetting('Fix_6',"true")
					if "true" in Fix_7: setsetting('Fix_7',"true")
					if "true" in Fix_8: setsetting('Fix_8',"true")
					if "true" in Fix_9: setsetting('Fix_9',"true")
					'''---------------------------'''
					if "true" in Fix_10: setsetting('Fix_10',"true")
					if "true" in Fix_11: setsetting('Fix_11',"true")
					if "true" in Fix_12: setsetting('Fix_12',"true")
					if "true" in Fix_13: setsetting('Fix_13',"true")
					if "true" in Fix_14: setsetting('Fix_14',"true")
					'''---------------------------'''
					if "true" in Fix_100:
						setsetting('Fix_100',"true")
						doFix_100_0("remove", "100")
					if "true" in Fix_101:
						setsetting('Fix_101',"true")
						doFix_100_0("remove", "101")
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
	elif printpoint == "1": print printfirst + "setFix_LV" + printpoint + space + "htptfixversion" + space2 + htptfixversion + space +  "htptfixversion_" + space2 + htptfixversion_
	elif printpoint == "12": print printfirst + "setFix_LV" + printpoint + space + "idstr_" + space2 + idstr_ + space +  "scripthtptinstall_User_ID" + space2 + str(scripthtptinstall_User_ID)
	elif printpoint == "123": print printfirst + "setFix_LV" + printpoint + space + "noidstr_" + space2 + noidstr_ + space +  "scripthtptinstall_User_ID" + space2 + str(scripthtptinstall_User_ID)
	elif "7" in printpoint:
		print printfirst + "setFix_1/2/3/4/5/6/7/8/9" + space2 + Fix_1 + " / " + Fix_2 + " / " + Fix_3 + " / " + Fix_4 + " / " + Fix_5 + " / " + Fix_6 + " / " + Fix_7 + " / " + Fix_8 + " / " + Fix_9
		print printfirst + "setFix_100/101/102/103/104" + space2 + Fix_100 + " / " + Fix_101 + " / " + Fix_102 + " / " + Fix_103 + " / " + Fix_104
		'''---------------------------'''

def downloads(admin, printpoint, name, connected):
	count = 0 ; file = "" ; returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
	while count < 10 and count > -5 and not xbmc.abortRequested:
		if not connected: count += 1
		elif returned_Dialog == "": count += -1
		else: count += 1
		xbmc.sleep(500)
		connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
		if connected: returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
		xbmc.sleep(500)
		if count == 1: printpoint = printpoint + "1"
		'''---------------------------'''
	if count < 10:
		printpoint = printpoint + "2"
		from commondownloader import *
		
		
		printpoint2 = installaddon2(admin, 'repository.htpt', update=True)
		printpoint2 = printpoint2 + installaddon2(admin, 'script.htpt.smartbuttons', update=False)
		printpoint2 = printpoint2 + installaddon2(admin, 'script.htpt.remote', update=False)
		printpoint2 = printpoint2 + installaddon2(admin, 'service.htpt.debug', update=False)
		printpoint2 = printpoint2 + installaddon2(admin, 'script.htpt.widgets', update=False)
		
		printpoint2 = printpoint2 + installaddon2(admin, 'repository.xbmc-israel')
		printpoint2 = printpoint2 + installaddonP(admin, 'repository.lambda')
		
		#printpoint2 = printpoint2 + installaddon2(admin, 'metadata.common.imdb.com', update=False)
		printpoint2 = printpoint2 + installaddonP(admin, 'metadata.universal')
		
		if "5" in printpoint2: xbmc.executebuiltin("UpdateLocalAddons")
		
		if scripthtptinstall_Skin_FirstBoot != "true" and systemidle300:
			printpoint = printpoint + "7"
			if not os.path.exists(addondata_path + "skin.htpt") or not os.path.exists(os.path.join(addondata_path,'skin.htpt','video')) or not os.path.exists(os.path.join(addondata_path,'skin.htpt','music')):
				file = "Media.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/Media.zip?dl=1", file, temp_path, addondata_path, silent=True)
			else: printpoint = printpoint + "8"
			
	else: printpoint = printpoint + "9"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + name + "_LV" + printpoint + space + "file" + space2 + file + space + "count" + space2 + str(count)
	'''---------------------------'''
	
def setRed_LV(idstr_, htptfixversion_, Addon_Version, htptfixversion, Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5):
	'''------------------------------
	---APPLY-CODE-RED----------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	printpoint = ""
	if Addon_Version != htptfixversion and htptfixversion == htptfixversion_ and idstr_ == scripthtptinstall_User_ID:
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
	
def doFix_100(admin, custom):
	'''---------------------------'''
	if custom == "100": dialogok(str78971.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (localize(342)) + '[/COLOR]', '$LOCALIZE[78972]', '$LOCALIZE[78973]', '$LOCALIZE[78980]')
	elif custom == "101": dialogok(str78971.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (str36903.encode('utf-8')) + '[/COLOR]', '$LOCALIZE[78972]', '$LOCALIZE[78973]', '$LOCALIZE[78980]')
	libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
	if libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
	#if not systemplatformwindows: UserBlock("ON")
	setSkinSetting("1",'Admin',"true")
	printpoint = "" ; extra = ""
	'''---------------------------'''
	xbmc.executebuiltin('ActivateWindow(10025,special://userdata/library/,return)')
	xbmc.sleep(500)
	xbmc.executebuiltin('Container.SetViewMode(50)')
	notification_common(custom)
	printpoint = doFix_100A(printpoint, custom)
	'''---------------------------'''
	if not "9" in printpoint: printpoint = doFix_100I(printpoint, custom)
	'''---------------------------'''	
	if not "9" in printpoint: printpoint = doFix_100M(printpoint, custom)
	'''---------------------------'''
	if not "9" in printpoint and "C" in printpoint: printpoint = doFix_100A(printpoint, custom)
	'''---------------------------'''
	if not "9" in printpoint and "C" in printpoint: printpoint = doFix_100I(printpoint, custom)
	'''---------------------------'''	
	if not "9" in printpoint and "C" in printpoint: printpoint = doFix_100M(printpoint, custom)
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
	#extra = newline + "localize(107)" + space2 + localize(107) + space + "localize107" + space2 + localize(107) + space + "xbmc.getInfoLabel('$LOCALIZE[107]')" + space2 + xbmc.getInfoLabel('$LOCALIZE[107]')
	print printfirst + space + "doFix_100_LV" + printpoint + space + "systemcurrentcontrol" + space2 + systemcurrentcontrol + space + "custom" + space2 + str(custom) + extra
	#if admin: print printfirst + space + "str20442" + space2 + str20442
	'''---------------------------'''
	return printpoint

def doFix_100_0(printpoint, custom):
	'''---------------------------'''
	xbmc.executebuiltin("UpdateLocalAddons") ; xbmc.sleep(2000)
	if custom == "100": x = xbmc.getCondVisibility('System.HasAddon(metadata.universal)')
	elif custom == "101": x = xbmc.getCondVisibility('System.HasAddon(metadata.tvdb.com)')
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	xbmc.sleep(500)
	'''---------------------------'''
	if custom == "100": list = [os.path.exists(addons_path + 'metadata.universal'), os.path.exists(addons_path + 'metadata.common.impa.com'), os.path.exists(addons_path + 'metadata.common.port.hu'), os.path.exists(addons_path + 'metadata.common.movieposterdb.com'), os.path.exists(addons_path + 'metadata.common.rt.com'), os.path.exists(addons_path + 'metadata.common.trakt.tv')]
	elif custom == "101": list = [os.path.exists(addons_path + 'metadata.common.imdb.com')]
	listS = str(list)
	'''---------------------------'''
	if printpoint == "remove" or (("False" in listS and "True" in listS) and scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true"):
		'''------------------------------
		---metadata.universal------------
		------------------------------'''
		printpoint = printpoint + "9"
		if admin: notification_common(custom)
		addonsL = []
		if custom == "100":
			addonsL.append('metadata.common.impa.com')
			addonsL.append('metadata.common.movieposterdb.com')
			addonsL.append('metadata.common.ofdb.de')
			addonsL.append('metadata.common.port.hu')
			addonsL.append('metadata.common.rt.com')
			addonsL.append('metadata.common.trakt.tv')
			addonsL.append('metadata.universal')
			'''---------------------------'''
		elif custom == "101":
			#addonsL.append('metadata.tvdb.com')
			addonsL.append('metadata.common.imdb.com')
			'''---------------------------'''
		removeaddons(addonsL,"13")
		#xbmc.executebuiltin("UpdateLocalAddons")
		#xbmc.executebuiltin("UpdateAddonRepos")
		xbmc.sleep(4000)
		
	elif connected and not "False" in listS and x:
		printpoint = printpoint + "0"
		'''---------------------------'''
	print printfirst + "doFix_100_0_LV" + printpoint + space + "listS" + space2 + listS	 + space + "custom" + space2 + str(custom) + space
	'''---------------------------'''
	return printpoint

def doFix_100A(printpoint, custom):
	xbmc.sleep(200)
	containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
	count = 0
	while count < 10 and containerfolderpath != "special://userdata/library/" and not "9" in printpoint and not xbmc.abortRequested:
		'''------------------------------
		---containerfolderpath-----------
		------------------------------'''
		xbmc.sleep(100)
		count += 1
		if count > 5 and "special://userdata/library/" in containerfolderpath: xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(200)
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		xbmc.sleep(100)
		if count == 1: printpoint = printpoint + "A"
		if count == 10: printpoint = printpoint + "9"
		'''---------------------------'''
		
	if not "9" in printpoint:
		'''------------------------------
		---ContextMenu-------------------
		------------------------------'''
		xbmc.executebuiltin('Action(PageUp)')
		xbmc.sleep(200)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		if custom == "100": x = "[movies]"
		elif custom == "101": x = "[tvshows]"
		else:
			x = "" ; printpoint = printpoint + "9"
		
		count = 0
		while count < 10 and systemcurrentcontrol != x and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("0",x,100,'Action(Down)','Action(ContextMenu)')
			if count == 1: printpoint = printpoint + "B"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		if not "9" in printpoint:
			count = 0
			while count < 10 and not xbmc.abortRequested: 
				count += 1
				xbmc.sleep(40)
				if count <= 7: xbmc.executebuiltin('Action(Up)')
				else:
					if count == 8: printpoint = printpoint + "8"
					xbmc.executebuiltin('Action(Down)')
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
				
	'''---------------------------'''
	return printpoint

def doFix_100I(printpoint, custom):
	xbmc.sleep(500)
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	if "C" in printpoint and not "M" in printpoint:
		'''------------------------------
		---Change-content----------------
		------------------------------'''
		count = 0
		while count < 10 and (not localize(231) in systemcurrentcontrol or not localize(16018) in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			if count < 5: systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(231),100,'Action(Select)','Action(Down)')
			elif count >=5: systemcurrentcontrol = findin_systemcurrentcontrol("1",localize(16018),100,'Action(Select)','Action(Down)')
			if count == 1: printpoint = printpoint + "I"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		
	elif "D" in printpoint or "M" in printpoint:
		'''------------------------------
		---Set-content-------------------
		------------------------------'''
		count = 0
		if custom == "100": x = localize(342) ; y = str36901.encode('utf-8') ; z = "Universal Movie Scraper"
		elif custom == "101": x = str36903.encode('utf-8') ; y = str36903.encode('utf-8') ; z = "The TVDB"
		else: x = "" ; y = "" ; z = ""
		while count < 10 and (not x in systemcurrentcontrol and not y in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			if count < 5: systemcurrentcontrol = findin_systemcurrentcontrol("1",x,100,'Action(Select)','Action(Down)')
			elif count >=5: systemcurrentcontrol = findin_systemcurrentcontrol("1",y,100,'Action(Select)','Action(Down)')
			if count == 1: printpoint = printpoint + "Q"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''

		'''---------------------------'''
		xbmc.executebuiltin('Control.SetFocus(20)')
		xbmc.sleep(200)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		count = 0
		while count < 10 and not z in systemcurrentcontrol and not "9" in printpoint and not xbmc.abortRequested:
			'''------------------------------
			---SCRAPER-NAME------------------
			------------------------------'''
			count += 1
			systemcurrentcontrol = findin_systemcurrentcontrol("1",z,300,'Action(Down)','Action(Select)')
			if z in systemcurrentcontrol: xbmc.executebuiltin('Action(Select)')
			if count == 5: xbmc.executebuiltin('Control.SetFocus(20)')
			if count == 1: printpoint = printpoint + "R"
			if count == 10: printpoint = printpoint + "9"
			'''---------------------------'''
		
		if custom == "100":
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
			while count < 10 and (not str20346.encode('utf-8') in systemcurrentcontrol or "(*)" in systemcurrentcontrol) and not "9" in printpoint and not xbmc.abortRequested:
				'''------------------------------
				---Scan recursively - OFF--------
				------------------------------'''
				count += 1
				systemcurrentcontrol = findin_systemcurrentcontrol("1",str20346.encode('utf-8'),400,'Action(Down)','')
				if count == 1: printpoint = printpoint + "T"
				if count == 10: printpoint = printpoint + "9"
				if str20346.encode('utf-8') in systemcurrentcontrol: systemcurrentcontrol = findin_systemcurrentcontrol("1","( )",400,'Action(Select)','')
				'''---------------------------'''
				
			'''count = 0
			while count < 10 and (systemcurrentcontrol != localize(186) or systemcurrentcontrol != localize(12321)) and not "9" in printpoint and not xbmc.abortRequested:
				count += 1
				if count < 4: xbmc.executebuiltin('Action(Down)')
				if count < 5: systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(186),100,'Action(Left)','Action(Select)')
				elif count >=5: systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(12321),100,'Action(Left)','Action(Select)')
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
	
def doFix_100M(printpoint, custom):
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	xbmc.sleep(1000)
	dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
	if dialogyesnoW:
		controlhasfocus11 = xbmc.getCondVisibility('Control.HasFocus(11)')
		count = 0
		while count < 10 and (count == 0 or not controlhasfocus11) and not "9" in printpoint and not xbmc.abortRequested:
			count += 1
			#systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(107),100,'Action(Down)','Action(Select)')
			controlhasfocus11 = findin_controlhasfocus("0",11,100,'Action(Down)','Action(Select)')
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
				notification_common(custom)
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
	addonsL = []
	'''------------------------------
	---REMOVE-REPOSITORIES-----------
	------------------------------'''
	addonsL.append('repository.divingmule.addons')
	addonsL.append('repository.tknorris.release')
	addonsL.append('repository.addonscriptorde-beta')
	addonsL.append('repository.superrepo.org.helix.others.adult')
	addonsL.append('repository.superrepo.org.helix.all')
	addonsL.append('repository.ninbora')
	'''---------------------------'''
	
	'''------------------------------
	---REMOVE-ADDONS-----------------
	------------------------------'''
	#addonsL.append('metadata.thexem.de')
	addonsL.append('plugin.video.aob')
	addonsL.append('plugin.video.discovery_com')
	addonsL.append('plugin.video.howstuffworks_com')
	addonsL.append('plugin.video.howstuffworks_com-2.0.4')
	addonsL.append('plugin.video.GoProCamera')
	addonsL.append('plugin.video.MikeysKaraoke')
	#addonsL.append('plugin.video.p2p-streams')
	addonsL.append('plugin.video.testtube')
	addonsL.append('plugin.video.the666sicco')
	addonsL.append('repository.pulsarunofficial')
	addonsL.append('script.htpt.homebuttons')
	addonsL.append('script.htpt.debug')
	'''---------------------------'''
	#addonsL.append('script.extendedinfo')
	#addonsL.append('script.module.addon.common')
	#addonsL.append('script.module.myconnpy')
	#addonsL.append('script.module.pil')
	#addonsL.append('script.module.simple.downloader')
	#addonsL.append('script.module.TheYid.common')
	#addonsL.append('script.module.youtube.dl')
	#addonsL.append('script.toolbox')
	'''---------------------------'''
	
	if (id10str == "C" or id10str == "D"):
		pass
		#addonsL.append('plugin.program.advanced.launcher')
		#addonsL.append('script.htpt.emu')
		'''---------------------------'''
		
	'''---------------------------'''
	removeaddons(addonsL,"12")
	'''---------------------------'''
	movefiles(os.path.join(addons_path, 'script.skin.helper.service-master'), os.path.join(addons_path, 'script.skin.helper.service'))
	movefiles(os.path.join(addons_path, 'script.skinshortcuts-master'), os.path.join(addons_path, 'script.skinshortcuts'))
	
	#setSkinSetting("1",'YouTube.23',"true")
	'''---------------------------'''
		
def doFix_3(printpoint):
	'''------------------------------
	---SET-FILES-AND-FOLDERS---------
	------------------------------'''
	path = os.path.join(userdata_path, 'userdata', '')
	removefiles(path)
	'''---------------------------'''
	
	'''------------------------------
	---USERDATA-ONLY!----------------
	------------------------------'''
	terminal('rm -rf /storage/.kodi/userdata/plugin.video.youtube/settings.xml',"plugin.video.youtube-settings.xml")
	'''---------------------------'''
	terminal('rm -rf /storage/.kodi/userdata/plugin.video.genesis',"plugin.video.youtube-userdata folder")
	xbmc.executebuiltin('AlarmClock(mode11,RunScript(script.htpt.refresh,,?mode=11),00:07,silent)') #GAL TEST THIS
	'''---------------------------'''
	
def Execute_Fix(admin, Fix_Done, Fix_L, Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_6, Fix_7, Fix_8, Fix_9, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104):
	'''------------------------------
	---EXECUTE-AUTO-FIX--------------
	------------------------------'''
	systeminternetstate = xbmc.getInfoLabel('System.InternetState')
	networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	'''---------------------------'''
	printpoint = ""
	printpoint2 = ""
	if "true" in Fix_L and xbmc.getSkinDir() == 'skin.htpt':
		printpoint = printpoint + "1"
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
		dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
		custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
		home_aW = xbmc.getCondVisibility('Window.IsActive(0)')
		startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
		'''---------------------------'''
				
		printpoint = printpoint + "3"
		'''---------------------------'''
		if Fix_10 == 'true':
			'''------------------------------
			---?-----------------------------
			------------------------------'''
			setsetting_custom1('service.htpt.fix','Fix_10',"false")
			pass
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
			dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74553.encode('utf-8') + '[/COLOR]', '$LOCALIZE[78979]', "", '$LOCALIZE[78984]')
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
				
		if (home_aW or startupW) and not dialogbusyW and not dialogokW and not dialogprogressW and not dialogselectW and not dialogtextviewerW and not dialogyesnoW and not custom1191W:
			printpoint = printpoint + "2"
			'''---------------------------'''
			if Fix_1 == 'true':
				'''------------------------------
				---LIVE-TV-----------------------
				------------------------------'''
				removeaddons('plugin.video.israelive', "23")
				dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + localize(19023) + '[/COLOR]', '$LOCALIZE[78988]', "", '$LOCALIZE[78984]')
				Fix_Done = Fix_Done + space4 + 'Fix_1'
				setsetting_custom1('service.htpt.fix','Fix_1',"false")
				#setsetting('Fix_1',"false")
				'''---------------------------'''
			if Fix_2 == 'true':
				'''------------------------------
				---REMOVE-ADDONS-----------------
				------------------------------'''
				doFix_2(printpoint2)
				dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + localize(74555) + '[/COLOR]', '$LOCALIZE[78989]', "", '$LOCALIZE[78984]')
				Fix_Done = Fix_Done + space4 + 'Fix_2'
				setsetting_custom1('service.htpt.fix','Fix_2',"false")
				#setsetting('Fix_2',"false")
				'''---------------------------'''
			if Fix_3 == 'true':
				'''------------------------------
				---SET-FILES-AND-FOLDERS---------
				------------------------------'''
				doFix_3(printpoint2)
				dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + localize(74552) + '[/COLOR]', '$LOCALIZE[78989]', "", '$LOCALIZE[78984]')
				Fix_Done = Fix_Done + space4 + 'Fix_3'
				setsetting_custom1('service.htpt.fix','Fix_3',"false")
				'''---------------------------'''
			if Fix_4 == 'true':
				'''------------------------------
				---USERDATA-CLEAR----------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_4',"false")
				'''---------------------------'''
			if Fix_5 == 'true':
				'''------------------------------
				---RESET-GUI---------------------
				------------------------------'''
				xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=40&amp;value=0)')
				xbmc.sleep(4000)
				dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74554.encode('utf-8') + '[/COLOR]', '$LOCALIZE[74795]', "", '$LOCALIZE[78984]')
				Fix_Done = Fix_Done + space4 + 'Fix_5'
				setsetting_custom1('service.htpt.fix','Fix_5',"false")
				xbmc.sleep(2000)
				'''---------------------------'''
			if Fix_6 == 'true':
				'''------------------------------
				---CustomHomeCustomizer----------
				------------------------------'''
				printpoint2 = ""
				returned = dialogyesno(localize(76196), localize(78022) + space + localize(76197)) #Skin Design
				if returned == 'ok':
					'''------------------------------
					---CustomHomeCustomizer-Window---
					------------------------------'''
					printpoint2 = printpoint2 + "1"
					xbmc.executebuiltin('ActivateWindow(1117)'); xbmc.sleep(500)
					customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
					count = 0
					while count < 10 and not customhomecustomizerW and not xbmc.abortRequested:
						count += 1
						xbmc.sleep(500)
						customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
						if count == 5: xbmc.executebuiltin('ActivateWindow(1117)'); xbmc.sleep(500)
						'''---------------------------'''
					if count < 10:
						xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=203&value=Templates)') #xbmc.executebuiltin('Dialog.Close(1173)')
						dialogok(localize(76196), localize(76198), localize(74444), localize(74448)) ; xbmc.sleep(5000) #Skin Design Save and Load your skin design.
						dialogok(localize(74444), localize(76180) + space + localize(480) + space + localize(636) + " + " + localize(74449), "", "")
						
						if 1 + 1 == 3:
							returned = dialogyesno(localize(74460), localize(78022) + space + localize(74460))  #Themes
							if returned == 'ok':
								'''------------------------------
								---Skin-Theme--------------------
								------------------------------'''
								printpoint2 = printpoint2 + "3"
								while returned == 'ok' and not xbmc.abortRequested:
									skincurrenttheme = xbmc.getInfoLabel('Skin.CurrentTheme')
									notification(localize(21895) + space2 + skincurrenttheme, localize(31407), "", 1000) ; xbmc.sleep(1000)
									xbmc.executebuiltin('Skin.Theme(-1)') ; xbmc.sleep(4000)
									skincurrenttheme = xbmc.getInfoLabel('Skin.CurrentTheme')
									notification(localize(21895) + space2 + skincurrenttheme, ".", "", 1000) ; xbmc.sleep(1000)
									notification(localize(21895) + space2 + skincurrenttheme, "..", "", 1000) ; xbmc.sleep(1000)
									notification(localize(21895) + space2 + skincurrenttheme, "...", "", 1000) ; xbmc.sleep(1000)
									returned = dialogyesno(localize(74460), localize(78022) + space + localize(74460))  #Themes
									'''---------------------------'''
						
						returned = dialogyesno(localize(10035) + space + localize(10507), localize(78022) + space + localize(76196) + space + localize(409))  #Themes
						if returned == 'ok':
							'''------------------------------
							---Reset-Settings----------------
							------------------------------'''
							printpoint2 = printpoint2 + "5"
							xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=201&value=1)') ; xbmc.sleep(500)
							'''---------------------------'''
						
						
				if printpoint2 != "":
					printpoint2 = printpoint2 + "7"
					setsetting_custom1('service.htpt.fix','Fix_6',"false")	
					Fix_Done = Fix_Done + space4 + 'Fix_6'
					'''---------------------------'''
					
			if Fix_7 == 'true':
				'''------------------------------
				---?-----------------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_7',"false")
				Fix_Done = Fix_Done + space4 + 'Fix_7'
				'''---------------------------'''
			if Fix_8 == 'true':
				'''------------------------------
				---?-----------------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_8',"false")
				Fix_Done = Fix_Done + space4 + 'Fix_8'
				'''---------------------------'''
			if Fix_9 == 'true':
				'''------------------------------
				---?-----------------------------
				------------------------------'''
				setsetting_custom1('service.htpt.fix','Fix_9',"false")
				Fix_Done = Fix_Done + space4 + 'Fix_9'
				'''---------------------------'''
			'''---------------------------'''
			if Fix_100 == 'true' and scripthtptinstall_Skin_FirstBoot != "true" and servicehtpt_Skin_UpdateLog != "true":
				'''------------------------------
				---SCRAPER-MOVIE-LIBRARY---------
				------------------------------'''
				#printpoint2 = "" ; printpoint2 = doFix_100_0(printpoint2, "100")
				printpoint2 = "" ; printpoint2 = doFix_100_0(printpoint2, "100")
				
				if not "9" in printpoint2 and "0" in printpoint2:
					dialogok(str78985.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (localize(342)) + '[/COLOR]', '$LOCALIZE[78983]', '$LOCALIZE[78982]',"")
					returned = dialogyesno(str78985.encode('utf-8'), '[COLOR=Yellow]' + str74550.encode('utf-8') % (localize(342)) + '[/COLOR]' + '[CR]' + str78981.encode('utf-8')) #Manual fix is available ,
					if returned == 'ok': printpoint2 = doFix_100(admin, "100")
					else: printpoint2 = printpoint2 + "8"
					'''---------------------------'''
					if "7" in printpoint2:
						dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (localize(342)) + '[/COLOR]',str75209.encode('utf-8') % (localize(342)), '$LOCALIZE[75208]', "")
						#setsetting_custom1('service.htpt.fix','Fix_100',"false")
						setsetting('Fix_100',"false")
						Fix_Done = Fix_Done + space4 + 'Fix_100'
						'''---------------------------'''
					elif "9" in printpoint2: dialogok(str78974.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (localize(342)) + '[/COLOR]',"", '$LOCALIZE[75210]', "") #Fix failed, Add movies to library
					'''---------------------------'''

			elif Fix_101 == 'true' and connected and scripthtptinstall_Skin_FirstBoot != "true" and servicehtpt_Skin_UpdateLog != "true":
				'''------------------------------
				---SCRAPER-TV-LIBRARY------------
				------------------------------'''
				printpoint2 = "" ; printpoint2 = doFix_100_0(printpoint2, "101")
				addon = 'metadata.tvdb.com'
				if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'): installaddon(admin, addon, "")
				printpoint2 = "" ; printpoint2 = doFix_100_0(printpoint2, "101")
				'''---------------------------'''
				if not "9" in printpoint2 and "0" in printpoint2:
					dialogok(str78985.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (str20343.encode('utf-8')) + '[/COLOR]', '$LOCALIZE[78983]', '$LOCALIZE[78982]',"")
					returned = dialogyesno(str78985.encode('utf-8'), '[COLOR=Yellow]' + str74550.encode('utf-8') % (str20343.encode('utf-8')) + '[/COLOR]' + '[CR]' + str78981.encode('utf-8')) #Manual fix is available ,
					if returned == 'ok': printpoint2 = doFix_100(admin, "101")
					else: printpoint2 = printpoint2 + "8"
					'''---------------------------'''
					if "7" in printpoint2:
						dialogok(str78986.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (str20343.encode('utf-8')) + '[/COLOR]',str75209.encode('utf-8') % (str20343.encode('utf-8')), '$LOCALIZE[75208]', "")
						#setsetting_custom1('service.htpt.fix','Fix_101',"false")
						setsetting('Fix_101',"false")
						Fix_Done = Fix_Done + space4 + 'Fix_101'
						'''---------------------------'''
					elif "9" in printpoint2: dialogok(str78974.encode('utf-8') + '[CR]' + '[COLOR=Yellow]' + str74550.encode('utf-8') % (str20343.encode('utf-8')) + '[/COLOR]',"", '$LOCALIZE[75210]', "") #Fix failed, Add movies to library
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
			#if not systemplatformwindows: os.system('sh /storage/.kodi/addons/service.htpt.fix/specials/scripts/Red_LV4.sh')
			removefiles(emulators_path)
			removeaddons(['script.htpt.emu', 'plugin.program.advanced.launcher'],"123")
			Red_Done = Red_Done + space4 + 'Red_LV4'
			#setsetting_custom1('service.htpt.fix','Red_LV4',"false")
			setsetting('Red_LV4',"false")
			printpoint == printpoint + "4"
			'''---------------------------'''
		
		if Red_LV5 == "true":
			'''------------------------------
			---TOTAL-------------------------
			------------------------------'''
			path = '/storage/'
			removefiles(path)
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
		dialogok('$LOCALIZE[78975]', '$LOCALIZE[78976]', '', '$LOCALIZE[78984]', line2c="Red")
		setsetting('Red_Alert',"false")
		'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	Red_L = str(Red_L)
	if admin and printpoint == "": print printfirst + space + "Execute_RedLV" + printpoint + space + "Red_L" + space2 + Red_L + space + "Red_LV1" + space2 + Red_LV1
	else:
		print printfirst + space + "Execute_RedLV" + printpoint + space + "Red_Done" + space2 + Red_Done
		dialogok('$LOCALIZE[78975]', str78978.encode('utf-8') + space2 + printpoint, '$LOCALIZE[78977]', '$LOCALIZE[78984]', line2c="Red")
		'''---------------------------'''
	'''---------------------------'''
	return Red_Done

def setMessagesCustom_All(admin):
	from shared_variables import htpt_a1, htpt_a2
	returned = ""
	count = 0
	while count == 0 and returned != "ok" and datenowS != "" and not xbmc.abortRequested:
		
		if (id9str == htpt_a2 or (admin and not admin2)) and yomshabat != "true":
			
			if scripthtptinstall_Skin_DateInstalled != "":
				'''------------------------------
				---DOWNLOADED--------------------
				------------------------------'''
				returned = setMessagesCustom(admin, returned, scripthtptinstall_Skin_DateInstalled, "+1", "", "", '[COLOR=Yellow]' + str79538.encode('utf-8') % (id1str) + '[/COLOR]' + '[CR][CR]' + xbmc.getInfoLabel('$LOCALIZE[74537]') + '[CR][CR]' + xbmc.getInfoLabel('$LOCALIZE[74542]') + '[CR][CR]' + xbmc.getInfoLabel('$LOCALIZE[79084]'))
				'''---------------------------'''
			
			if returned == "skip":
				pass
				'''------------------------------
				---NEW-MOVIES--------------------
				------------------------------'''
				#returned = setMessagesCustom(admin, returned, '2015-05-11', "2015-05-12", 19, 07, addonString(128).encode('utf-8') % ('[COLOR=Blue]- Furious Seven (2015)[CR]- Kingsman The Secret Service (2014)[/COLOR][CR]- Focus (2015)[CR]- Selma (2014)[CR]- Run All Night (2015)'))
				#returned = setMessagesCustom(admin, returned, '2015-05-12', "2015-05-13", 19, 07, addonString(128).encode('utf-8') % ('[COLOR=Blue]- Furious Seven (2015)[CR]- Kingsman The Secret Service (2014)[/COLOR][CR]- Focus (2015)[CR]- Selma (2014)[CR]- Run All Night (2015)'))
				#returned = setMessagesCustom(admin, returned, '2015-05-13', "2015-05-14", 19, 07, addonString(128).encode('utf-8') % ('[COLOR=Blue]- Furious Seven (2015)[CR]- Kingsman The Secret Service (2014)[/COLOR][CR]- Focus (2015)[CR]- Selma (2014)[CR]- Run All Night (2015)'))
				#returned = setMessagesCustom(admin, returned, '2015-05-14', "2015-05-15", 19, 07, addonString(128).encode('utf-8') % ('[COLOR=Blue]- Furious Seven (2015)[CR]- Kingsman The Secret Service (2014)[/COLOR][CR]- Focus (2015)[CR]- Selma (2014)[CR]- Run All Night (2015)'))
				'''---------------------------'''
				
				'''------------------------------
				---BIG-BRO-----------------------
				------------------------------'''
				#returned = setMessagesCustom(admin, returned, '2015-05-11', '2015-05-15', "", "", addonString(127).encode('utf-8'))
				'''---------------------------'''
				
				'''------------------------------
				---BIRTHDAY----------------------
				------------------------------'''
				if scripthtptinstall_User_ID == 'htptuser2' or scripthtptinstall_User_ID == 'htptuser4' or scripthtptinstall_User_ID == 'htptuser5' or 'finalmakerr' in scripthtptinstall_User_ID:
					pass
					#returned = setMessagesCustom(admin, returned, '2015-07-12', '2015-07-14', "", "", addonString(126).encode('utf-8') % (addonString(1100)))
					'''---------------------------'''
		
		elif returned == "skip" and scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true":
			'''------------------------------
			---PESAH-HOLIDAY-----------------
			------------------------------'''
			#returned = setMessagesCustom(admin, returned, '2015-04-03', '2015-04-09', "", "", addonString(130).encode('utf-8'))
			returned = setMessagesCustom(admin, returned, '2016-04-22', '2016-04-28', "", "", addonString(130).encode('utf-8'))
			returned = setMessagesCustom(admin, returned, '2017-04-10', '2017-04-16', "", "", addonString(130).encode('utf-8'))
			'''---------------------------'''
			
			'''------------------------------
			---Yom-HaShoah-------------------
			------------------------------'''
			#returned = setMessagesCustom(admin, returned, '2015-04-15', '2015-04-16', 19, 21, addonString(150).encode('utf-8'))
			returned = setMessagesCustom(admin, returned, '2016-05-04', '2016-05-05', 19, 21, addonString(150).encode('utf-8'))
			returned = setMessagesCustom(admin, returned, '2017-04-23', '2017-04-24', 19, 21, addonString(150).encode('utf-8'))
			'''---------------------------'''
			
			'''------------------------------
			---Yom-Hazikaron-----------------
			------------------------------'''
			#returned = setMessagesCustom(admin, returned, '2015-04-21', '2015-04-22', 19, 18, addonString(131).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-05-10', '2016-05-11', 19, 18, addonString(131).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-04-30', '2017-05-01', 19, 18, addonString(131).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Yom-Ha'atzmaut----------------
			------------------------------'''
			#returned = setMessagesCustom(admin, returned, '2015-04-22', '2015-04-23', 19, 20, addonString(132).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-05-11', '2016-05-12', 19, 20, addonString(132).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-05-01', '2017-05-02', 19, 20, addonString(132).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Lag_BaOmer--------------------
			------------------------------'''
			#returned = setMessagesCustom(admin, returned, '2015-05-06', '2015-05-07', 19, 20, addonString(133).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-05-25', '2016-05-26', 19, 20, addonString(133).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-05-13', '2017-05-14', 19, 20, addonString(133).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Shavuot-----------------------
			------------------------------'''
			#returned = setMessagesCustom(admin, returned, '2015-05-23', '2015-05-24', 19, 20, addonString(134).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-06-11', '2016-06-12', 19, 20, addonString(134).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-05-30', '2017-05-31', 19, 20, addonString(134).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Rosh-Hashanah-----------------
			------------------------------'''
			returned = setMessagesCustom(admin, returned, '2015-09-13', '2015-09-15', 19, 20, addonString(137).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-10-02', '2016-10-04', 19, 20, addonString(137).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-09-20', '2017-09-22', 19, 20, addonString(137).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Yom-Kippur--------------------
			------------------------------'''
			returned = setMessagesCustom(admin, returned, '2015-09-22', '2015-09-23', 19, 20, addonString(139).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-10-11', '2016-10-12', 19, 20, addonString(139).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-09-29', '2017-09-30', 19, 20, addonString(139).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Sukkot------------------------
			------------------------------'''
			returned = setMessagesCustom(admin, returned, '2015-09-27', '2015-10-05', 19, 20, addonString(141).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-10-16', '2016-10-24', 19, 20, addonString(141).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-10-04', '2017-10-12', 19, 20, addonString(141).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Hanukkah----------------------
			------------------------------'''
			returned = setMessagesCustom(admin, returned, '2015-12-06', '2015-12-14', 19, 20, addonString(143).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-12-24', '2017-01-01', 19, 20, addonString(143).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-12-12', '2017-12-20', 19, 20, addonString(143).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''------------------------------
			---Purim-------------------------
			------------------------------'''
			returned = setMessagesCustom(admin, returned, '2015-03-05', '2015-03-06', 19, 20, addonString(146).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2016-03-24', '2016-03-25', 19, 20, addonString(146).encode('utf-8') + '[CR]')
			returned = setMessagesCustom(admin, returned, '2017-03-12', '2017-03-13', 19, 20, addonString(146).encode('utf-8') + '[CR]')
			'''---------------------------'''
			
			'''---------------------------'''
			xbmc.sleep(1000)
			count += 1
			'''---------------------------'''
		
		if returned == "skip":
			count += 1
			returned = "skip"
			
	if returned == "skip": setSkinSetting("0",'MessagesCustom', "")
	
	xbmc.sleep(2000)
	'''---------------------------'''
	
def setMessagesCustom(admin, returned, date1, date2, time1, time2, message):
	#import datetime as dt #Can cause a bug with stringtodate!
	printpoint = "" ; TypeError = "" ; extra = ""
	if date1 == "" or date2 == "": printpoint = printpoint + "9"
	elif returned != "ok" and returned != "ok2":
		date1D = stringtodate(date1,'%Y-%m-%d')
		if admin: print "date1D" + space2 + str(date1D)
		if str(date1D) != "error":
			try:
				datenowD = stringtodate(datenowS,'%Y-%m-%d')
				if "+7" in date2: date2D = date1D + dt.timedelta(days=7)
				elif "+1" in date2: date2D = date1D + dt.timedelta(days=1)
				else: date2D = stringtodate(date2,'%Y-%m-%d')
			except Exception, TypeError:
				extra = extra + newline + "TypeError" + space2 + str(TypeError)
				printpoint = printpoint + "8"
			
			if not "8" in printpoint:
				date1 = str(date1D)
				date2 = str(date2D)
				message = str(message)
				message = '"' + message + '"'
				'''---------------------------'''
				if (str(datenowD) or str(date1D) or str(date2D)) == "error": printpoint + "9"
				elif (datenowD >= date1D and datenowD <= date2D):
					printpoint = printpoint + "2"
					if datenowD == date1D and time1 != "" and timenow3S != "":
						printpoint = printpoint + "3"
						if time1 > timenow3N:
							printpoint = printpoint + "4"
							returned = "skip"
							'''---------------------------'''
						else: returned = 'ok'
					elif datenowD == date2D and time2 != "" and timenow3S != "":
						printpoint = printpoint + "5"
						if time2 < timenow3N:
							printpoint = printpoint + "6"
							returned = "skip"
							'''---------------------------'''
						else: returned = 'ok'
					else: returned = 'ok'	
					if returned == 'ok':
						printpoint = printpoint + "7"
						setSkinSetting("0",'MessagesCustom', message)
						returned = 'ok'
						xbmc.sleep(500)
						'''---------------------------'''
				elif returned != 'ok': printpoint = printpoint + "8"
				else: printpoint = printpoint + "9"
		else: printpoint = printpoint + "9"
		
	if ("9" in printpoint or "8" in printpoint) and returned != "ok" and returned != "ok2": returned = "skip"
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and not admin2 or extra != "": print printfirst + "setMessagesCustom_LV" + printpoint + space + "(" + returned + ")" + space + "date1" + space2 + date1 + space + "date2" + space2 + date2 + space + "datenowS" + space2 + datenowS + space + "timenow3S" + space2 + timenow3S
	'''---------------------------'''
	return returned
	'''---------------------------'''
		