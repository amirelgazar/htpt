import xbmc, os, subprocess, sys
import xbmcgui, xbmcaddon

from variables import *
from modules import *

RefreshSettings()
if admin: notification("script.htpt.refresh","","",2000)
class AutoPlay_PauseButton:
	'''------------------------------
	---AutoPlay-Pause----------------
	------------------------------'''
	if autoplaypausebutton:
		#from variables import autoplaypause
		#from variables import autoplaypause, homeW, myvideonavW
		#from variables import AutoPlay_Pause, AutoPlay_HD, AutoPlay_SD
		'''---------------------------'''
		if AutoPlay_Pause == "false" and not autoplaypause:
			'''------------------------------
			---AutoPlay-PAUSE-ON-------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','AutoPlay_Pause',"true")
			setSkinSetting("1",'AutoPlay_Pause',"true")
			addonsettings2('plugin.video.genesis','autoplay',"false",'',"",'autoplay_library',"false",'playback_info',"true",'',"")
			if AutoPlay_HD == "true": notification(addonString(202) + " (HD) ","","",2000)
			elif AutoPlay_SD == "true": notification(addonString(202) + " (SD) ","","",2000)
			'''---------------------------'''
		elif AutoPlay_Pause == "true" and autoplaypause:
			'''------------------------------
			---AutoPlay-PAUSE-OFF------------
			------------------------------'''
			setsetting_custom1('script.htpt.refresh','AutoPlay_Pause',"false")
			setSkinSetting("1",'AutoPlay_Pause',"false")
			addonsettings2('plugin.video.genesis','autoplay',"true",'',"",'autoplay_library',"true",'playback_info',"false",'',"")
			if AutoPlay_HD == "true": notification(addonString(200) + " (HD) ","","",1000)
			elif AutoPlay_SD == "true": notification(addonString(200) + " (SD) ","","",1000)
			else:
				notification(addonString(200) + " (HD) ","","",1000)
				addonsettings2('plugin.video.genesis','autoplay_hd',"true",'',"",'',"",'',"",'',"")
			'''---------------------------'''
		else:
			if admin: notification("AutoPlayPause-Bugged...","","",2000)
			if not autoplaypause:
				'''------------------------------
				---AutoPlay-PAUSE-ON-------------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','AutoPlay_Pause',"true")
				setSkinSetting("1",'AutoPlay_Pause',"true")
				addonsettings2('plugin.video.genesis','autoplay',"false",'',"",'autoplay_library',"false",'playback_info',"false",'',"")
				if AutoPlay_HD == "true": notification(addonString(202) + " (HD) ","","",2000)
				elif AutoPlay_SD == "true": notification(addonString(202) + " (SD) ","","",2000)
				'''---------------------------'''
			elif autoplaypause:
				'''------------------------------
				---AutoPlay-PAUSE-OFF------------
				------------------------------'''
				setsetting_custom1('script.htpt.refresh','AutoPlay_Pause',"false")
				setSkinSetting("1",'AutoPlay_Pause',"false")
				addonsettings2('plugin.video.genesis','autoplay',"true",'',"",'autoplay_library',"true",'playback_info',"true",'',"")
				if AutoPlay_HD == "true": notification(addonString(200) + " (HD) ","","",1000)
				elif AutoPlay_SD == "true": notification(addonString(200) + " (SD) ","","",1000)
				else:
					notification(addonString(200) + " (HD) ","","",1000)
					addonsettings2('plugin.video.genesis','autoplay_hd',"true",'',"",'',"",'',"",'',"")
				'''---------------------------'''
			
		if homeW: xbmc.executebuiltin('Action(Down)')
		elif myvideonavW: xbmc.executebuiltin('Action(Right)')
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		AutoPlay_Pause2 = getsetting('AutoPlay_Pause')
		print printfirst + "AutoPlay_PauseButton" + space2 + "AutoPlay_Pause" + space2 + AutoPlay_Pause + " - " + AutoPlay_Pause2 + space3
		'''---------------------------'''

class Refresh_Button:
	if refreshbutton or General_Refresh != "":
		'''------------------------------
		---Refresh-----------------------
		------------------------------'''
		#from variables import myvideonavW
		setsetting_custom1('script.htpt.refresh','General_Refresh',"")
		setsetting_custom1('script.htpt.refresh','General_StartWindow',"")
		setsetting_custom1('script.htpt.refresh','AutoPlay_Pause',"false")
		setSkinSetting("1",'AutoPlay_Pause',"false")
		xbmc.sleep(500)
		GenesisSettings("0")
		GenesisSettings("2")
		GenesisSettings("4")
		'''---------------------------'''
		
		if General_Refresh == "0":
			'''------------------------------
			---ismovie-----------------------
			------------------------------'''
			if not myvideonavW: xbmc.executebuiltin('ActivateWindow(Videos,MovieTitles)')
			setsetting_custom1('script.htpt.refresh','General_CustomVAR',"1")
			
			xbmc.executebuiltin('Notification($LOCALIZE[79067] $LOCALIZE[71030],$LOCALIZE[31407],4000)')
			'''---------------------------'''
			
		elif refreshbutton or General_Refresh == "1":
			'''------------------------------
			---istv--------------------------
			------------------------------'''
			if not myvideonavW: xbmc.executebuiltin('ActivateWindow(VideoLibrary,TVShowTitles)')
			xbmc.executebuiltin('Notification($LOCALIZE[79067] $LOCALIZE[73120],$LOCALIZE[31407],4000)')
			'''---------------------------'''
			
		'''------------------------------
		---MYVIDEO-NAV-------------------
		------------------------------'''
		xbmc.sleep(1500)
		xbmc.executebuiltin('Container.Refresh')
		xbmc.executebuiltin('RunScript(service.skin.widgets)')
		xbmc.sleep(500)
		'''---------------------------'''
		if General_StartWindow == "1" or refreshbutton:
			'''------------------------------
			---HOME--------------------------
			------------------------------'''
			xbmc.sleep(1200)
			xbmc.executebuiltin('ReplaceWindow(0)')
			xbmc.sleep(700)
			'''---------------------------'''
			if refreshbutton or General_Refresh == "1":
				'''------------------------------
				---HOME--------------------------
				------------------------------'''
				xbmc.executebuiltin('Control.SetFocus(2)')
				xbmc.executebuiltin('Action(Up)')
				xbmc.executebuiltin('Action(Up)')
			elif General_Refresh == "0":
				'''------------------------------
				---ismovie-----------------------
				------------------------------'''
				xbmc.executebuiltin('Control.SetFocus(1)')
				xbmc.executebuiltin('Action(Up)')
				xbmc.executebuiltin('Action(Up)')
				'''---------------------------'''
		if General_StartWindow == "1":
			'''------------------------------
			---HOME--------------------------
			------------------------------'''
			from variables import dialogselectsources3, dialogselectsources5
			'''---------------------------'''
			if dialogselectsources3 == dialogselectsources5:
				'''------------------------------
				---TRIGGER-REFRESH2--------------
				------------------------------'''
				xbmc.executebuiltin('Control.SetFocus(9092)')
				xbmc.executebuiltin('Action(Select)')
				print printfirst + "refresh2" + space3
		
		#RefreshSettings()
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "Refresh_Button"
		'''---------------------------'''

class Cancel_Button:
	if cancelbutton and customvar == "1":
		count = 0
		while count < 5 and not xbmc.abortRequested:
			General_CustomVAR = getsetting('General_CustomVAR')
			if General_CustomVAR != "1" and General_CustomVAR != "3" and General_CustomVAR != "20": setsetting_custom1('script.htpt.refresh','General_CustomVAR',"1")
			count += 1
			xbmc.sleep(200)

		General_CustomVAR2 = getsetting('General_CustomVAR')
		setSkinSetting("0",'General_CustomVAR',General_CustomVAR2)
		print printfirst + "Cancel_Button" + space2 + "General_CustomVAR/2" + space2 + General_CustomVAR + " - " + General_CustomVAR2

class main:
	xbmc.sleep(500)
	#RefreshSettings()
	#notification(controlisvisible311S,controlisvisible312S,"",5000)
	#GenesisSettings("4")
	#topvideoinformation('run')
	#setsetting_custom1('script.htpt.refresh','General_Refresh',"false")
	
