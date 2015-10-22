import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon

'''OTHERS'''
xbmc.sleep(4000)
from variables import *
from modules import *

class resetsettings:
	if Addon_Version == "" and Addon_UpdateDate == "":
		'''------------------------------
		---DELETE-ADDON-USERDATA---------
		------------------------------'''
		pass
		#if not systemplatformwindows: terminal('rm -rf /storage/.kodi/userdata/addon_data/service.htpt.fix/settings.xml',"service.htpt.fix - userdata")
		#print printfirst + "resetsettings" + space2 + "settings.xml REMOVED!" 
		'''---------------------------'''
	else:
		addonsettings2("service.htpt.fix",'Red_LV1',"false",'Red_LV2',"false",'Red_LV3',"false",'Red_LV4',"false",'Red_LV5',"false")
		addonsettings2("service.htpt.fix",'Red_Alert',"false",'Fix_ScriptON',"false",'Addon_ServiceON',"true",'Addon_UpdateLog',"true",'Red_ScriptON',"false")
		addonsettings2("service.htpt.fix",'General_ScriptON',"false",'General_DownloadON',"false",'',"true",'',"",'',"")
		'''---------------------------'''

while (xbmc.getSkinDir() != 'skin.htpt') and not xbmc.abortRequested:
	xbmc.sleep(60000)
	
class clean:
	Clean_Library("1")
	Clean_Library("2")
	Clean_Library("3")
	removefiles(addons_path + '#')
	removefiles(userdata_path + '#')
	removefiles(addondata_path + '#')
	removeaddons(['script.htpt.homebuttons', 'service.htpt.fix', 'service.htpt', 'script.htpt.smartbuttons', 'service.htpt.debug', 'script.htpt.emu', 'script.htpt.install', 'script.htpt.refresh', 'script.htpt.widgets', 'plugin.video.htpt.kids', 'plugin.video.htpt.gopro', 'plugin.video.htpt.music', 'skin.htpt'], "3")
	path1 = os.path.join(addons_path,'script.htpt.widgets','')
	if not os.path.exists(temp_path): os.mkdir(temp_path)
	if not os.path.exists(downloads_path): os.mkdir(downloads_path)
	if not os.path.exists(music_path): os.mkdir(music_path)
	if not os.path.exists(pictures_path): os.mkdir(pictures_path)
	'''---------------------------'''

class startup:
	xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=12)') #downloads
	xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=20)') #setAdvancedSettings
	
	

	setSkinSetting_startup(admin)
	'''---------------------------'''
	
class modifyaddons:
	addon = 'plugin.video.sdarot.tv'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		'''------------------------------
		---plugin.video.sdarot.tv--------
		------------------------------'''
		infile = os.path.join(addons_path, 'plugin.video.sdarot.tv', 'sdarottv.py')
		old_word = "finalVideoUrl,VID = getFinalVideoUrl(series_id,season_id,epis,silent=True)"
		new_word = "finalVideoUrl,VID = getFinalVideoUrl(series_id,season_id,epis,silent=False)"
		replace_word(infile,old_word,new_word)
		'''---------------------------'''
		infile = os.path.join(addons_path, 'plugin.video.sdarot.tv', 'resources', 'lib', 'sdarotcommon.py')
		old_word = "time.sleep(5)"
		new_word = "time.sleep(2)"
		replace_word(infile,old_word,new_word)
		'''---------------------------'''

	addon = 'plugin.video.israelsports'
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		'''------------------------------
		---plugin.video.israelsports-----
		------------------------------'''
		infile = os.path.join(addons_path,addon,'default.py')
		old_word = "addDir('PTP STREAMS *LIVE*'"	
		new_word = "#a#ddDir('PTP STREAMS *LIVE*'"
		replace_word(infile,old_word,new_word)
		'''---------------------------'''
		old_word = "addDir('SPORTS DEVIL  *LIVE*'"	
		new_word = "#a#ddDir('SPORTS DEVIL  *LIVE*'"
		replace_word(infile,old_word,new_word)
		'''---------------------------'''
	
class main:
	scriptcount = 0 #EXECUTE
	scriptcount2 = 0 #SUSPEND > 0
	xbmc.executebuiltin('RunScript('+ addonID +',,?mode=1)')
	while 1 and not xbmc.abortRequested:
		if xbmc.getSkinDir() != "skin.htpt":
			xbmc.sleep(60000)
		else:
			custom1000W = xbmc.getCondVisibility('Window.IsVisible(Custom1000.xml)')
			if custom1000W:
				xbmc.sleep(10000)
			else:
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
				performance = xbmc.getInfoLabel('Skin.HasSetting(Performance)')
				home_aW = xbmc.getCondVisibility('Window.IsActive(0)')
				containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
				'''---------------------------'''
				dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
				dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
				dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
				dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
				dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
				dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
				startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
				custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
				'''---------------------------'''
				if scriptcount2 == 0:
					if (not playerhasvideo and systemidle7 and home_aW) or startupW:
						x = 0
						if startupW and not systemidle7: xbmc.executebuiltin('RunScript('+ addonID +',,?mode=1)') #Addon_Update-&-SET
						else: x += 1
						if home_aW and not dialogprogressW and not dialogokW and not dialogbusyW and not dialogtextviewerW and not dialogyesnoW and not dialogselectW and not custom1191W and not startupW: xbmc.executebuiltin('RunScript(service.htpt.fix,,)')
						else: x += 1
						if x > 0: scriptcount += 1
						if admin: print printfirst + space + "count" + space2 + str(scriptcount)
						'''---------------------------'''
							
					'''------------------------------
					---scriptcount2------------------
					------------------------------'''
					if admin and not systemidle120: scriptcount2 += 2 #xbmc.sleep(10000)
					elif playerhasvideo: scriptcount2 += 24 #xbmc.sleep(120000)
					elif not home_aW: scriptcount2 += 4 #xbmc.sleep(20000)
					else: scriptcount2 += 2 #xbmc.sleep(10000)
					'''---------------------------'''
							
				'''---------------------------'''
				if scriptcount2 > 0: scriptcount2 += -1
				'''---------------------------'''
				if scriptcount >= 10:
					if admin and not admin2:
						pass
						#notification(printfirst,"Clean Exit = NO","scriptcount = 0",2000)
						#scriptcount = 0
						#setsetting_custom1("service.htpt.fix",'Addon_ServiceON',"true")
					else:
						pass
						setsetting_custom1("service.htpt.fix",'Addon_ServiceON',"false")
						print printfirst + "Clean Exit" + space + "Addon_ServiceON" + space2 + Addon_ServiceON
						sys.exit()
						'''---------------------------'''

				'''---------------------------'''
				
				'''------------------------------
				---SLEEP-------------------------
				------------------------------'''
				if admin and not systemidle7: xbmc.sleep(5000)
				elif playerhasvideo: xbmc.sleep(60000)
				else: xbmc.sleep(10000)
				if performance: xbmc.sleep(10000)
				'''---------------------------'''
				
				'''------------------------------
				---PRINT-END---------------------
				------------------------------'''
				if admin and not admin2 and admin3 and not systemidle7: print printfirst + "service.py" + space + "scriptcount" + space2 + str(scriptcount) + " (" + str(scriptcount2) + ") " + space + "General_ScriptON" + space2 + General_ScriptON + space + "Addon_ServiceON" + space2 + Addon_ServiceON
				'''---------------------------'''
			
	if xbmc.abortRequested:
		print printfirst + "Error 1170: AbortRequested!"
		sys.exit()
		'''---------------------------'''
