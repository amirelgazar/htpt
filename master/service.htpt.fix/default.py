import xbmc, os, subprocess, sys
import xbmcgui, xbmcaddon

from variables import *
from modules import *
from shared_modules3 import get_params

printpoint = ""
'''---------------------------'''
try: params=get_params()
except Exception, TypeError: notification_common("18")
mode=None
'''---------------------------'''
try: mode=int(params["mode"])
except: pass
'''---------------------------'''

#if mode == None and General_ScriptON == "true": sys.exit()
if mode != 11 and mode != 13 and mode != 14 and mode != 20: setGeneral_ScriptON("0", General_ScriptON, "")

if mode != 20 and xbmc.getSkinDir() != 'skin.htpt' and not systemplatformwindows:
	printpoint = printpoint + "9"
	setSkinSetting("1", 'Admin', "false")
	setSkinSetting("1", 'Admin2', "false")
	'''---------------------------'''

elif mode == None:	
	'''------------------------------
	---Execute_Fix-------------------
	------------------------------'''
	if "true" in Fix_L and systemidle7 and Fix_ScriptON != "true" and scripthtptinstall_Skin_Installed != "true": xbmc.executebuiltin('RunScript('+ addonID +',,?mode=3)')
		
	elif homeW and not dialogprogressW and not dialogokW and not dialogbusyW and not dialogtextviewerW and not dialogyesnoW and not startupW and not custom1191W:
		if Addon_Version == addonVersion and Addon_UpdateLog == "true" and Addon_UpdateDate != "":
			'''------------------------------
			---?-----------------------------
			------------------------------'''
			pass
				
elif mode == 1:
	'''------------------------------
	---Addon_Update-&-SET------------
	------------------------------'''
	if Addon_Update != "true" or (Addon_Update == "true" and Addon_Version == htptfixversion): Addon_Update = setAddon_Update(admin, addonVersion, Addon_Version, Addon_Update)
	'''---------------------------'''
	if Addon_Update == "true" or Addon_UpdateDate == "": Addon_UpdateDate = setAddon_UpdateDate(admin, Addon_Version, htptfixversion, Addon_Update, Addon_UpdateDate)
	'''---------------------------'''
	if Addon_Update == "true":
		'''------------------------------
		---SET-FIX_----------------------
		------------------------------'''
		'''setFix_("idstr_", "htptfixversion_", noidstr_, Addon_Version, htptfixversion, "Fix_1=false", "Fix_2=false", "Fix_3=false", "Fix_4=false", "Fix_5=false", "Fix_6=false", "Fix_7=false", "Fix_8=false", "Fix_9=false", "Fix_11=false", "Fix_12=false", "Fix_13=false", "Fix_14=false", "Fix_100=false", "Fix_101=false", "Fix_102=false", "Fix_103=false", "Fix_104=false")'''
		setFix_("N/A", "0.1.54", '', Addon_Version, htptfixversion, "Fix_1=false", "Fix_2=false", "Fix_3=false", "Fix_4=false", "Fix_5=true", "Fix_6=false", "Fix_7=false", "Fix_8=false", "Fix_9=false", "Fix_10=false", "Fix_11=false", "Fix_12=false", "Fix_13=false", "Fix_14=false", "Fix_100=false", "Fix_101=false", "Fix_102=false", "Fix_103=false", "Fix_104=false")
		'''---------------------------'''
		
		'''------------------------------
		---SET-RED_LV--------------------
		------------------------------'''
		'''setRed_LV("idstr_", "htptfixversion_", Addon_Version, htptfixversion, "1=false", "2=false", "3=false", "4=false", "5=false")'''
		#setRed_LV("idstr_", "htptfixversion_", Addon_Version, htptfixversion, "1=true", "2=false", "3=false", "4=false", "5=false")
		setRed_LV("htpt3155919", "0.1.40", Addon_Version, htptfixversion, "1=false", "2=false", "3=false", "4=true", "5=false")
		setRed_LV("htpt1284906", "0.1.40", Addon_Version, htptfixversion, "1=false", "2=false", "3=false", "4=true", "5=false")
		setRed_LV("htpt2066520", "0.1.40", Addon_Version, htptfixversion, "1=false", "2=false", "3=false", "4=true", "5=false")
		
		'''---------------------------'''
		
		'''------------------------------
		---ID-REWRITE--------------------
		------------------------------'''
		'''idstr = USERNAME EN , id1str = USERNAME HE, id2str = INSTALLATION DATE, id3str = WARRENTY END, id4str = ADDRESS, id5str = TELEPHONE NUMBER, id6str = PAYMENT TERMS,
		id7str = QUESTION, id8str = TECHNICAL NAME, id9str = CODE RED, id10str = HTPT'S MODEL, ID11 = MAC1, ID12 = MAC2, ID40=, ID60 = '''
		'''ID_Rewrite(idstr_, htptfixversion_, Addon_Version, htptfixversion, "", "", "", "", "", "", "", "", "", "", "", "", "", "")'''
		ID_Rewrite("htpt3313341", "0.1.47", Addon_Version, htptfixversion, "idstr=htptuser9", "id1str=", "id2str=", "id3str=", "id4str=", "id5str=", "id6str=", "id7str=", "id8str=", "id9str=TULU", "id10str=", "id11str=", "id12str=", "id40str=false", "id60str=")
		'''---------------------------'''
		
		'''------------------------------
		---Activate_Account--------------
		------------------------------'''
		'''Activate_Account(idstr_, htptfixversion_, Addon_Version, htptfixversion, id2set)'''
		#Activate_Account("htpt1296816", "0.1.31", Addon_Version, htptfixversion, "")
		'''---------------------------'''
		
		'''------------------------------
		---setAddon_Version---------------
		------------------------------'''
		Addon_Version = setAddon_Version(admin, addonVersion, Addon_Version)
		'''---------------------------'''

	#if Addon_Version == htptfixversion and Addon_UpdateLog == "true" and Addon_UpdateDate != "" and Fix_Done != "" and systemidle7 and not playerhasvideo and home_aW:
	
	if Addon_Update == "false":
		if (startupW or loginscreenW) and not systemidle40: setMessagesCustom_All(admin)
		
		'''------------------------------
		---Red_Alert---------------------
		------------------------------'''
		if "true" in Red_L and Red_ScriptON != "true" and Red_Alert == 'true': xbmc.executebuiltin('RunScript('+ addonID +',,?mode=2)')
		'''---------------------------'''
		
elif mode == 2:
	'''------------------------------
	---Red_Alert---------------------
	------------------------------'''
	setsetting_custom1('service.htpt.fix','Red_ScriptON',"true")
	'''---------------------------'''
	
	Red_Done = Execute_Red(admin, Red_Done, Red_L, Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5)
	if systemhasaddon_scripthtptdebug and Red_Done != "" and Red_LastDate != "":
		setsetting_custom1('service.htpt.debug','ModeOn_5',"true")
		#if scripthtptdebug_General_ScriptON != "true": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=5)')
		'''---------------------------'''

	'''---------------------------'''
	setsetting_custom1('service.htpt.fix','Red_ScriptON',"false")
	'''---------------------------'''

elif mode == 3:
	'''------------------------------
	---Fix_Execute-------------------
	------------------------------'''
	setsetting_custom1('service.htpt.fix','Fix_ScriptON',"true")
	'''---------------------------'''
	
	if libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
	Fix_Done = Execute_Fix(admin, Fix_Done, Fix_L, Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_6, Fix_7, Fix_8, Fix_9, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104)
	
	if Fix_Done != "": setsetting('Fix_LastDate',datenowS)
	
	if systemhasaddon_scripthtptdebug and Fix_Done != "":
		setsetting_custom1('service.htpt.debug','ModeOn_6',"true")
		#if scripthtptdebug_General_ScriptON != "true": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=6)')
		'''---------------------------'''
	
	'''---------------------------'''
	setsetting_custom1('service.htpt.fix','Fix_ScriptON',"false")
	'''---------------------------'''
	
elif mode == 10:
	returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
	if returned_Dialog == "":
		xbmc.sleep(3000)
		returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
	if returned_Dialog == "dialogselectW":
		'''------------------------------
		---dialogselectW-----------------
		------------------------------'''
		printpoint = printpoint + "1"
		if "IPTVSimple?" in returned_Header:
			printpoint = printpoint + "2"
			if returned_Message == "":
				systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
				count = 0
				while count < 10 and (systemcurrentcontrol != localize(107) or count == 0) and not xbmc.abortRequested:
					count += 1
					systemcurrentcontrol = findin_systemcurrentcontrol("0",localize(107),100,'Action(Down)','Action(Select)')
					'''---------------------------'''
				if count < 10: printpoint = printpoint + "7"
				'''---------------------------'''
		elif localize(166) in returned_Header:
			if 1 + 1 == 3:
				if systemhasaddon_htptinstall and id40str:
					 if scripthtptinstall_General_ScriptON != "true": pass #xbmc.executebuiltin('RunScript(script.htpt.install,,?mode=22)')
					 else: setsetting_custom1('script.htpt.install', 'General_ScriptON', "false")
				else: xbmc.executebuiltin('dialog.close(selectdialog)')
				'''---------------------------'''
			
		'''---------------------------'''
	elif returned_Dialog == "dialogyesnoW":
		'''------------------------------
		---dialogyesnoW------------------
		------------------------------'''
		printpoint = printpoint + "1"
		if returned_Header == "P2P-STREAMS":
			printpoint = printpoint + "2"
			if returned_Message == "Are you using OpenELEC x86_x64?":
				printpoint = printpoint + "7"
				#xbmc.executebuiltin('Control.SetFocus(11)')
				xbmc.executebuiltin('Action(Down)')
				xbmc.sleep(200)
				xbmc.executebuiltin('Action(Select)')
				'''---------------------------'''
		elif returned_Header == "OpenELEC Bluetooth":
			printpoint = printpoint + "2"
			if returned_Message == "AuthorizeService":
				printpoint = printpoint + "7"
				#xbmc.executebuiltin('Control.SetFocus(11)')
				xbmc.executebuiltin('Action(Down)')
				xbmc.sleep(200)
				xbmc.executebuiltin('Action(Select)')
				'''---------------------------'''
		elif returned_Header == "YouTube":
			'''untested!'''
			printpoint = printpoint + "2"
			if returned_Message == "Execute setup-wizard?":
				printpoint = printpoint + "7"
				#xbmc.executebuiltin('Control.SetFocus(11)')
				xbmc.executebuiltin('Action(Select)')
				'''---------------------------'''
		elif returned_Header == "Genesis":
			'''untested!'''
			notification("QWE","","",5000)
			printpoint = printpoint + "2"
			#if returned_Message == genesis30341str:
			printpoint = printpoint + "7"
			#xbmc.executebuiltin('Control.SetFocus(11)')
			xbmc.executebuiltin('Action(Down)')
			xbmc.executebuiltin('Action(Select)')
			'''---------------------------'''
		else: printpoint = printpoint + "9"
			
	elif returned_Dialog == "dialogkeyboardW":
		'''------------------------------
		---dialogkeyboardW---------------
		------------------------------'''
		pass
		'''---------------------------'''
	elif returned_Dialog == "dialogprogressW":
		'''------------------------------
		---dialogprogressW---------------
		------------------------------'''
		pass
		'''---------------------------'''
	elif returned_Dialog == "dialogbusyW":
		'''------------------------------
		---dialogbusyW-------------------
		------------------------------'''
		if returned_Header == addonString_servicehtpt(10):
			if returned_Message == "":
				dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
				count = 0
				while count < 10 and dialogbusyW and not xbmc.abortRequested:
					count += 1
					xbmc.sleep(2000)
					if xbmc.Player().isPlayingVideo(): xbmc.sleep(500)
					if "C" in id10str or "D" in id10str: xbmc.sleep(1000)
					if int(pingrate) < 3: xbmc.sleep(500)
					dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
					if count == 9: notification_common("21")
					'''---------------------------'''
				if count == 10:
					xbmc.executebuiltin('Dialog.Close(busydialog)')
					notification_common("20")
					'''---------------------------'''
					
	elif returned_Dialog == "dialogokW":
		'''------------------------------
		---dialogokW---------------
		------------------------------'''
		printpoint = printpoint + "1"
		if returned_Header == localize(19240):
			'''------------------------------
			---No PVR Add-on enabled---------
			------------------------------'''
			printpoint = printpoint + "2"
			xbmc.executebuiltin('Action(Select)')
			addonbrowserW = xbmc.getCondVisibility('Window.IsVisible(AddonBrowser.xml)')
			count = 0
			while count < 10 and not addonbrowserW and not xbmc.abortRequested:
				if count == 0: printpoint = printpoint + "3"
				count += 1
				xbmc.sleep(100)
				addonbrowserW = xbmc.getCondVisibility('Window.IsVisible(AddonBrowser.xml)')
				'''---------------------------'''
			xbmc.executebuiltin('Control.SetFocus(50)')
			xbmc.executebuiltin('Acion(PageUp)')
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			count = 0
			while count < 10 and addonbrowserW and systemcurrentcontrol != "PVR IPTV Simple Client" and not xbmc.abortRequested:
				if count == 0: printpoint = printpoint + "4"
				count += 1
				systemcurrentcontrol = findin_systemcurrentcontrol("0","PVR IPTV Simple Client",100,'Action(Down)','')
				addonbrowserW = xbmc.getCondVisibility('Window.IsVisible(AddonBrowser.xml)')
				'''---------------------------'''
			if count < 10:
				xbmc.executebuiltin('Action(Select)')
				dialogaddoninfoW = xbmc.getCondVisibility('Window.IsVisible(DialogAddonInfo.xml)')
				count = 0
				while count < 10 and not dialogaddoninfoW and not xbmc.abortRequested:
					count += 1
					dialogaddoninfoW = xbmc.getCondVisibility('Window.IsVisible(DialogAddonInfo.xml)')
					xbmc.sleep(100)
					'''---------------------------'''
				if count < 10:
					count = 0
					while count < 10 and addonbrowserW and systemcurrentcontrol != str24022.encode('utf-8') and not xbmc.abortRequested:
						if count == 0: printpoint = printpoint + "5"
						count += 1
						systemcurrentcontrol = findin_systemcurrentcontrol("0",str24022.encode('utf-8'),100,'Action(Down)','Action(Select)')
						addonbrowserW = xbmc.getCondVisibility('Window.IsVisible(AddonBrowser.xml)')
						'''---------------------------'''
					if count < 10:
						xbmc.sleep(500)
						systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
						systemcurrentcontrol = findin_systemcurrentcontrol("0",str24022.encode('utf-8'),100,'','Action(Select)')
						xbmc.sleep(100)
						systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
						if systemcurrentcontrol == str24021.encode('utf-8'):
							printpoint = printpoint + "7"
							xbmc.executebuiltin('Action(PreviousMenu)')
							xbmc.executebuiltin('Action(PreviousMenu)')
							'''---------------------------'''
			
		elif "ISRAELIVE" in returned_Header:
			'''------------------------------
			---plugin.video.israelive--------
			------------------------------'''
			#xbmc.executebuiltin('SendClick(10)')
			#xbmc.executebuiltin('SetFocus(10)')
			xbmc.executebuiltin('Action(Select)')
			#notification("k","","",1000)
			'''---------------------------'''
						
	elif returned_Dialog == "dialogsubtitlesW":
		'''------------------------------
		---dialogsubtitlesW---------------
		------------------------------'''
		pass
		'''---------------------------'''
	elif returned_Dialog == "videofullscreenW":
		'''------------------------------
		---videofullscreenW---------------
		------------------------------'''
		pass
		'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if "7" in printpoint: notification_common("14") #***Automatic Action***
	if admin: print printfirst + "default.py_LV" + printpoint + space + "mode" + space2 + str(mode) + space + "returned_Dialog" + space2 + returned_Dialog + space + "returned_Header" + space2 + returned_Header + space + "returned_Message" + space2 + returned_Message
	'''---------------------------'''

elif mode == 11:
	'''------------------------------
	---autoshutdown------------------
	------------------------------'''
	dialogok(localize(79532), localize(79533), localize(79534), "")
	'''---------------------------'''
	
elif mode == 12:
	'''------------------------------
	---downloads---------------------
	------------------------------'''
	name = 'downloads'
	downloads(admin, printpoint, name, connected)
	'''---------------------------'''

elif mode == 14:
	'''------------------------------
	---dialogok----------------------
	------------------------------'''
	if scripthtptrefresh_General_CustomVAR == "53": dialogok('$ADDON[script.htpt.refresh 204]', '$ADDON[script.htpt.refresh 256]', "", "")
	else: dialogok('$ADDON[script.htpt.refresh 224]', '$ADDON[script.htpt.refresh 256]', "", "")
	'''---------------------------'''
	
elif mode == 20:
	'''------------------------------
	---setAdvancedSettings-----------
	------------------------------'''
	name = 'setAdvancedSettings'
	Mode_20(admin, name, printpoint, scripthtptdebug_Info_TotalSpace, scripthtptdebug_Info_TotalMemory, scripthtptdebug_Info_Model, scripthtptdebug_Info_Intel)
	'''---------------------------'''
	
elif mode == 40:
	'''------------------------------
	---setInstalled------------------
	------------------------------'''
	pass
	'''---------------------------'''	
	
setGeneral_ScriptON("1", General_ScriptON, "")
if admin: print printfirst + "default.py" + space + "mode" + space2 + str(mode)