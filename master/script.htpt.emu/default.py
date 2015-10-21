#!/usr/bin/python
#import xbmc, sys, xbmcaddon
import xbmc, os, subprocess, sys
import xbmcgui, xbmcaddon

from variables import *
from modules import *
from shared_modules3 import get_params

'''---------------------------'''
try: params=get_params()
except: pass

mode=None
'''---------------------------'''
try: mode=int(params["mode"])
except: pass
'''---------------------------'''

if mode == None:
	
	if emubutton or emubutton2:
		name = 'OPEN-SETTINGS'
		mode4(admin, name)
			
	if emubutton:
		name = 'RELOAD-CFG'
		mode6('1', admin, name)
			
	if not systemplatformwindows:
		copyfiles(os.path.join(emulators_path, 'retroarch', 'config', 'retroarch.cfg'), os.path.join(addondata_path, 'addonID', 'emusettings.py')) #GAL TEST THIS!
		xbmc.sleep(1000)
		
	from emusettings import *

	class emusettings2:
		'''------------------------------
		---CHANGE-RETROARCH-SETTINGS-----
		------------------------------'''
		setsetting('General_LastModified',datenowS)
		if not systemplatformwindows or systemplatformwindows:
			'''------------------------------
			---video_black_frame_insertion---
			------------------------------'''
			if video_black_frame_insertion2 != video_black_frame_insertion and video_black_frame_insertion2 != "":
				replace_word(file1,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file2,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file3,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file4,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file5,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file6,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file7,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file8,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				replace_word(file9,'video_black_frame_insertion = "' + video_black_frame_insertion + '"','video_black_frame_insertion = "' + video_black_frame_insertion2 + '"')
				print printfirst + space + "video_black_frame_insertion" + space2 + video_black_frame_insertion + " - " + video_black_frame_insertion2
				'''---------------------------'''
			
			'''------------------------------
			---video_refresh_rate------------
			------------------------------'''
			if video_refresh_rate2 != video_refresh_rate and video_refresh_rate2 != "":
				replace_word(file1,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file2,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file3,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file4,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file5,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file6,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file7,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file8,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				replace_word(file9,'video_refresh_rate = "' + video_refresh_rate + '"','video_refresh_rate = "' + video_refresh_rate2 + '"')
				print printfirst + space + "video_refresh_rate" + space2 + video_refresh_rate + " - " + video_refresh_rate2
				'''---------------------------'''
			
			'''------------------------------
			---video_smooth------------
			------------------------------'''
			if video_smooth2 != video_smooth and video_smooth2 != "":
				replace_word(file1,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file2,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file3,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file4,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file5,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file6,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file7,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file8,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				replace_word(file9,'video_smooth = "' + video_smooth + '"','video_smooth = "' + video_smooth2 + '"')
				print printfirst + space + "video_smooth" + space2 + video_smooth + " - " + video_smooth2
				'''---------------------------'''
				
			'''------------------------------
			---audio_device2-----------------
			------------------------------'''
			if audio_device2 != audio_device and audio_device2 != "":
				replace_word(file1,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file2,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file3,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file4,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file5,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file6,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file7,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file8,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				replace_word(file9,'audio_device = "' + audio_device + '"','audio_device = "' + audio_device2 + '"')
				print printfirst + space + "audio_device" + space2 + audio_device + " - " + audio_device2
				'''---------------------------'''
			
			'''------------------------------
			---audio_out_rate----------------
			------------------------------'''
			if audio_out_rate2 != audio_out_rate and audio_out_rate2 != "":
				replace_word(file1,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file2,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file3,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file4,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file5,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file6,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file7,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file8,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				replace_word(file9,'audio_out_rate = "' + audio_out_rate + '"','audio_out_rate = "' + audio_out_rate2 + '"')
				print printfirst + space + "audio_out_rate" + space2 + audio_out_rate + " - " + audio_out_rate2
				'''---------------------------'''
			
			'''------------------------------
			---audio_sync--------------------
			------------------------------'''
			if audio_sync2 != audio_sync and audio_sync2 != "":
				replace_word(file1,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file2,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file3,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file4,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file5,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file6,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file7,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file8,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				replace_word(file9,'audio_sync = "' + audio_sync + '"','audio_sync = "' + audio_sync + '"')
				print printfirst + space + "audio_sync" + space2 + audio_sync + " - " + audio_sync2
				'''---------------------------'''
				
			'''------------------------------
			---audio_latency-----------------
			------------------------------'''
			if audio_latency2 != audio_latency and audio_latency2 != "":
				replace_word(file1,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file2,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file3,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file4,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file5,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file6,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file7,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file8,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				replace_word(file9,'audio_latency = "' + audio_latency + '"','audio_latency = "' + audio_latency2 + '"')
				print printfirst + space + "audio_latency" + space2 + audio_latency + " - " + audio_latency2
				
			'''------------------------------
			---audio_volume------------------
			------------------------------'''
			if audio_volume2 != audio_volume and audio_volume2 != "":
				replace_word(file1,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file2,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file3,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file4,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file5,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file6,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file7,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file8,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				replace_word(file9,'audio_volume = "' + audio_volume + '"','audio_volume = "' + audio_volume2 + '"')
				print printfirst + space + "audio_volume" + space2 + audio_volume + " - " + audio_volume2
			
	if emubutton: output = terminal('retroarch --menu -v -c /storage/emulators/retroarch/config/retroarch.cfg',"retroarch menu")

if mode == 1:
	'''------------------------------
	---ALLOW-JOYSTICK----------------
	------------------------------'''
	settingschange('SystemSettings','input.enablejoystick','1','yes',xbmc.getInfoLabel('$LOCALIZE[14094]'),xbmc.getInfoLabel('$LOCALIZE[35100]'))
	'''---------------------------'''
	
elif mode == 2:
	'''------------------------------
	---JOYSTICK-STATUS---------------
	------------------------------'''
	oewindow("Bluetooth")
	'''---------------------------'''
	
elif mode == 3:
	'''------------------------------
	---DOWNLOAD----------------------
	------------------------------'''
	name = 'DOWNLOAD'
	if dialogaddonsettingsW: xbmc.executebuiltin('Action(Back)')
	notification("Looking for games..","Please Wait","",1000)
	if dialogaddonsettingsW: downloads(admin, printpoint, name, connected, multi=True)
	elif myprogramsW: downloads(admin, printpoint, name, connected, multi=False)
	else: notification_common("17")
	'''---------------------------'''

elif mode == 4:
	'''------------------------------
	---OPEN-SETTINGS-----------------
	------------------------------'''
	name = 'OPEN-SETTINGS'
	mode4(admin, name)
	'''---------------------------'''
elif mode == 5:
	'''------------------------------
	---MUSIC-DEBUG-------------------
	------------------------------'''
	name = 'MUSIC-DEBUG'
	mode5(admin, name)
	'''---------------------------'''
elif mode == 6:
	'''------------------------------
	---RELOAD-CFG--------------------
	------------------------------'''
	name = 'RELOAD-CFG'
	mode6('1', admin, name)
	'''---------------------------'''
elif mode == 7:
	'''------------------------------
	---AdvancedLauncher--------------
	------------------------------'''
	name = 'AdvancedLauncher'
	createfolders(admin)
	
	if os.path.exists(launcher_file) and os.path.exists(launcher2_file):
		launcher_size = getFileAttribute(2, launcher_file)
		launcher2_size = getFileAttribute(2, launcher2_file)
		if launcher_size != launcher2_size: copylauncher = "true"
	else: copylauncher = "true"
	
	if copylauncher == "true":
		copyfiles(launcher2_file, launcher_file, chmod="+x", mount=False)
	
	returned = ActivateWindow("0", 'plugin.program.advanced.launcher', '', 0, wait=True)
	
	if "ok" in returned:
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		containernumitems = xbmc.getInfoLabel('Container.NumItems')
		if (systemcurrentcontrol == "[..]" or systemcurrentcontrol == "[Default]") and (containernumitems == "0" or containernumitems == "1"):
			'''------------------------------
			---FIX-CONFIGURATION-FILE--------
			------------------------------'''
			print printfirst + space + "gamesbutton" + space + "Possible Error in file: launcher.xml"
			dialogok(localize(75795), localize(75796),"","")
			copylaunchers(admin) #os.system('sh /storage/.kodi/addons/script.htpt.emu/specials/scripts/copyemu.sh')
			xbmc.executebuiltin('ActivateWindow(Home.xml)') ; xbmc.sleep(1000) ; xbmc.executebuiltin('RunAddon(plugin.program.advanced.launcher)')
			'''---------------------------'''
		else:
			mode6('1', admin, name)
			if not os.path.exists(os.path.join(rom_path,'Sega Master System')) and not os.path.exists(os.path.join(rom_path,'TurboGrafx 16')) and not os.path.exists(os.path.join(rom_path,'Sega Genesis')):
				dialogok("You currently have no games!", "Choose the Advanced Options button (Left Menu), then Choose YES.", "Click once on the Downloading Games button, then Choose Confirm to dow", "")
			elif scripthtptdebug_Info_Bluetooth == "":
				returned = dialogyesno("Bluetooth support", "Click YES in order to learn how to sync your PS3 controller")
				if returned == 'ok':
					diaogtextviewer("How to sync your PS3 controller", "This guide assume your hardware have a supported bluetooth adapter.[CR]If it's not then note that you maybe able to play with your PS3 cable attached![CR][CR]1. Enable your bluetooth by Choosing the Joystick Status button (left menu) then go up + right into service tab.[CR]Select the Enable Bluetooth option.[CR]2. Plug in your PS3 cable (Use 2.0 usb slot), connect it to the PS3 controller.[CR]Note: If the lights are blinking then your controller is charging.[CR]3. Click the PS button once.[CR]Note: The blinked lights are now off and your 1 player slot should light up.[CR]4. Unplug the PS3 cable.[CR]Note: The lights will blink and the controller should be auto sync in a few seconds.[CR]If that's not occur it's recommend to reboot your device.[CR]5. If the 1P light isn't on but 2-4P, you should unplug your others bluetooth device (one time), disconnect your PS3 controller by using the Josytick Status button, then turn on the PS3 controller by using the PS3 button.[CR][CR]- You can enable up to 4 PS3 controllers at once, they are all able to control your interface and in-game (ofcourse).")
	
	print printfirst + "mode7_LV" + printpoint + space + "containernumitems" + space2 + str(containernumitems)
		
elif mode == 8:
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	pass
	'''---------------------------'''
elif mode == 9:
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	pass
	'''---------------------------'''	
elif mode == 10:
	'''------------------------------
	---?-----------------------------
	------------------------------'''
	pass
	'''---------------------------'''
	
if admin: print printfirst + "mode" + space2 + str(mode)