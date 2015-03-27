import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon

'''OTHERS'''
xbmc.sleep(10000)
#import datetime
from variables import *
from modules import *

class resetsettings:
	if Addon_Version == "" and Addon_UpdateDate == "":
		'''------------------------------
		---DELETE-ADDON-USERDATA---------
		------------------------------'''
		if not systemplatformwindows: bash('rm -rf /storage/.kodi/userdata/addon_data/service.htpt.fix/settings.xml',"service.htpt.fix - userdata")
		print printfirst + "resetsettings" + space2 + "settings.xml REMOVED!" 
		'''---------------------------'''
	else:
		addonsettings2("service.htpt.fix",'Red_LV1',"false",'Red_LV2',"false",'Red_LV3',"false",'Red_LV4',"false",'Red_LV5',"false")
		addonsettings2("service.htpt.fix",'Red_Alert',"false",'',"",'Addon_ServiceON',"true",'',"",'',"")
		'''---------------------------'''
	xbmc.sleep(4000)
	'''---------------------------'''
	
class set:
	'''------------------------------
	---SET-FIX_----------------------
	------------------------------'''
	'''setFix_("idstr_", "htptfixversion_", Addon_Version, htptfixversion, "Fix_1=false", "Fix_2=false", "Fix_3=false", "Fix_4=false", "Fix_5=false", "Fix_11=false", "Fix_12=false", "Fix_13=false", "Fix_14=false", "Fix_100=false", "Fix_101=false", "Fix_102=false", "Fix_103=false", "Fix_104=false")'''
	setFix_("N/A", "0.0.10", Addon_Version, htptfixversion, "Fix_1=false", "Fix_2=true", "Fix_3=false", "Fix_4=false", "Fix_5=false", "Fix_10=false", "Fix_11=false", "Fix_12=false", "Fix_13=false", "Fix_14=false", "Fix_100=true", "Fix_101=false", "Fix_102=false", "Fix_103=false", "Fix_104=false")
	'''---------------------------'''
	
	'''------------------------------
	---SET-RED_LV--------------------
	------------------------------'''
	'''setRed_LV("idstr_", "htptfixversion_", Addon_Version, htptfixversion, "1=false", "2=false", "3=false", "4=false", "5=false")'''
	#setRed_LV("idstr_", "htptfixversion_", Addon_Version, htptfixversion, "1=true", "2=false", "3=false", "4=false", "5=false")
	'''---------------------------'''
	
	'''------------------------------
	---ID-REWRITE--------------------
	------------------------------'''
	'''idstr = USERNAME EN , id1str = USERNAME HE, id2str = INSTALLATION DATE, id3str = WARRENTY END, id4str = ADDRESS, id5str = TELEPHONE NUMBER, id6str = PAYMENT TERMS,
	id7str = QUESTION, id8str = TECHNICAL NAME, id9str = CODE RED, id10str = HTPT'S MODEL, ID11 = MAC1, ID12 = MAC2'''
	'''ID_Rewrite(idstr_, htptfixversion_, Addon_Version, htptfixversion, "", "", "", "", "", "", "", "", "", "", "", "", "", "")'''
	#ID_Rewrite(idstr_, htptfixversion_, Addon_Version, htptfixversion, "htptuser27", addonString(1001), "", "", addonString(1004), "0542556699", id6v1str, "", "GAL", "", "", "", "", "")
	ID_Rewrite("htptuser27", "0.0.10", Addon_Version, htptfixversion, "", "", "2015-01-13 ", "2016-01-13", "", "", "", "", "", "", "", "", "", "")
	ID_Rewrite("htptuser6", "0.0.10", Addon_Version, htptfixversion, "", addonString(1001), "2015-03-25 ", "2016-03-25", "", "", "", "", "GAL", "", "", "", "", "")
	'''---------------------------'''
	
	'''------------------------------
	---TRIAL-RENEW-------------------
	------------------------------'''
	'''Trial_Renew(idstr_, htptfixversion_, Addon_Version, htptfixversion)'''
	#Trial_Renew("finalmakerr", "0.0.9", Addon_Version, htptfixversion)
	'''---------------------------'''
	xbmc.sleep(2000)
	'''---------------------------'''
class main:
	count = 0
	while 1 and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		#if admin: print printfirst + "DEBUGGING! (0)" + space + "Fix_1/2/3" + space2 + Fix_1 + " / " + Fix_2 + " / " + Fix_3 + space + "Addon_Version" + space2 + Addon_Version + space + "Addon_UpdateLog" + space2 + Addon_UpdateLog
		systeminternetstate = xbmc.getInfoLabel('System.InternetState')
		networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
		connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
		hasinternet = systeminternetstate != "" and networkipaddress != "" and not "169.254." in networkipaddress and (connected or systemplatformwindows)
		'''---------------------------'''
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
		systemidle7 = xbmc.getCondVisibility('System.IdleTime(7)')
		systemidle120 = xbmc.getCondVisibility('System.IdleTime(120)')
		validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')
		validation2 = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION2)')
		home_aW = xbmc.getCondVisibility('Window.IsActive(0)')
		'''---------------------------'''
		#Red_Alert = getsetting('Red_Alert')
		#xbmc.sleep(500)
		#if admin: print printfirst + "DEBUGGING! (0)" + space + "Red_Alert" + space2 + Red_Alert
		'''---------------------------'''
		if (not playerhasvideo and systemidle7 and home_aW and not validation) or (validation or validation2):
			xbmc.executebuiltin('RunScript(service.htpt.fix)')
			'''------------------------------
			---COUNT-------------------------
			------------------------------'''
			if not validation and not validation2:
				count += 1
				countS = str(count)
				if admin: print printfirst + space + "count" + space2 + countS
				'''---------------------------'''
				if admin and not systemidle120: xbmc.sleep(5000)
				else: xbmc.sleep(10000)
				'''---------------------------'''
				
		'''------------------------------
		---SLEEP-------------------------
		------------------------------'''
		if admin and not systemidle120: xbmc.sleep(5000)
		elif playerhasvideo: xbmc.sleep(120000)
		elif not home_aW: xbmc.sleep(20000)
		else: xbmc.sleep(10000)
		'''---------------------------'''
		
		if count >= 10:
			print printfirst + "Clean Exit"
			if admin: notification(printfirst,"Clean Exit","",2000)
			sys.exit()
			'''---------------------------'''
			
	if xbmc.abortRequested:
		print printfirst + "Error 1170: AbortRequested!"
		sys.exit()
		'''---------------------------'''
