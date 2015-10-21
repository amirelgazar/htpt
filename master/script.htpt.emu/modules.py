import xbmc, xbmcgui, xbmcaddon
import os, subprocess

from variables import *
from shared_modules import *

def downloads(admin, printpoint, name, connected, multi=True):

	
	if connected:
		printpoint = printpoint + "1"
		#from commondownloader import * #GAL TEST THIS!
		file = ""
		
		if not systemplatformwindows or admin3:
			printpoint = printpoint + "2"
			if "A" in id10str or "B" in id10str:
				printpoint = printpoint + "3"
				if addonVersion != "0.0.7":
					printpoint = printpoint + "4"
					if servicehtptfix_General_DownloadON != "true":
						printpoint = printpoint + "5"
						if multi == True:
							if not os.path.exists(os.path.join(rom_path,'Sega Master System')):
								file = "Sega Master System.zip"
								fileID = getfileID(file)
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sega%20Master%20System.zip?dl=1", file, temp_path, rom_path)
							elif not os.path.exists(os.path.join(rom_path,'TurboGrafx 16')):
								file = "TurboGrafx 16.zip"
								fileID = getfileID(file)
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/TurboGrafx%2016.zip?dl=1", file, temp_path, rom_path)
							elif addonVersion != "0.0.8" or addonVersion != "0.0.9": notification("No more games available atm..", "Wait for next update", "", 4000)
							elif not os.path.exists(os.path.join(rom_path,'Sega Genesis')):
								file = "Sega Genesis.zip"
								fileID = getfileID(file)
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sega%20Genesis.zip?dl=1", file, temp_path, rom_path)
							elif not os.path.exists(os.path.join(rom_path,'Nintendo')):
								file = "Nintendo.zip"
								fileID = getfileID(file)
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/Nintendo.zip?dl=1", file, temp_path, rom_path)
							elif not os.path.exists(os.path.join(rom_path,'Super Nintendo')):
								file = "Super Nintendo.zip"
								fileID = getfileID(file)
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/Super%20Nintendo.zip?dl=1", file, temp_path, rom_path)
							elif not os.path.exists(os.path.join(rom_path,'Nintendo 64')):
								file = "Nintendo 64.zip"
								fileID = getfileID(file)
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/Nintendo%2064.zip?dl=1", file, temp_path, rom_path)
						else: downloads2(admin, listitemlabel)
							
	else:
		printpoint = printpoint + "9"
		notification_common("5")
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + name + "_LV" + printpoint + space + "file" + space2 + file
	'''---------------------------'''

def downloads2(admin, listitemlabel):
	name = 'downloads2' ; printpoint2 = "" ; sub = "" ; file = "" ; file_ = ""
	
	if listitemlabel != "":
		'''Sony Playstation'''
		if listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Crash Bandicoot': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		elif listitemlabel == 'Arcade 1P': printpoint2 = printpoint2 + "1"
		else: notification_common("17") #Error, Unknown
		
	if printpoint2 != "":
		if "1" in printpoint2: sub = '1P' 
		elif "2" in printpoint2: sub = '2P'
		elif "3" in printpoint2: sub = '3P'
		elif "4" in printpoint2: sub = '4P'
		else: notification_common("17") #Error, Unknown
	
		if sub != "":
			path = os.path.join(rom_path, 'Sony Playstation', sub, listitemlabel, '')
			if os.path.exists(path):
				returned = dialogyesno("Game exist!", "Would you like to redownload?")
				if returned == 'ok': printpoint2 = printpoint2 + "d"
				else: notification_common("9") #HAPEULA BUTLA, LO BUTZHU SINUHIM
			else: printpoint2 = printpoint2 + "d"
			
			if "d" in printpoint2:
				'''------------------------------
				---DOWNLOAD-GAME-----------------
				------------------------------'''
				file = "Sony Playstation" + space3 + sub + space3 + listitemlabel + ".zip"
				file_ = file.replace(" ", "%20")
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sega%20Master%20System.zip?dl=1", file, temp_path, rom_path)
				'''---------------------------'''
	
	print printfirst + name + "_LV" + printpoint2 + space + "listitemlabel" + space2 + listitemlabel + space + "sub" + space2 + sub + newline + \
	"file" + space2 + file + newline + \
	"file_" + space2 + file_ + newline

def createfolders(admin):
	if not os.path.exists(advancedlauncher_addondata_path):
		try: os.mkdir(advancedlauncher_addondata_path)
		except Exception, TypeError: pass
	
	if not os.path.exists(htptemu_addondata_path):
		try: os.mkdir(htptemu_addondata_path)
		except Exception, TypeError: pass
		
	if not os.path.exists(emulators_path):
		try: os.mkdir(emulators_path)
		except Exception, TypeError: pass
		
	if not os.path.exists(configpath):
		try: os.mkdir(configpath)
		except Exception, TypeError: pass
		
def copylaunchers(admin):
			
	if systemplatformlinux:
		adult = xbmc.getInfoLabel('Skin.HasSetting(Adult)')
		copyfiles(htptemu_copyonce_path, emulators_path, chmod="+x", mount=False) #Copy Once Folders
		
		file_name = launcherfilename
		if id10str == "B": file_name = file_name + "_B"
		else: file_name = file_name + "_A"
		if adult: file_name = file_name + "A"
		file_name = file_name + ".xml"
		file_path = os.path.join(htptemu_copyrepeatlaunchers_path, file_name)
		
		copyfiles(file_path, htptemu_addondata_path + launcherfilename + ".xml", chmod="+x", mount=False) #Copy launchers
		copyfiles(file_path, advancedlauncher_addondata_path + launcherfilename + ".xml", chmod="+x", mount=False) #Copy launchers
		
def mode4(admin, name):
	'''------------------------------
	---OPEN-SETTINGS-----------------
	------------------------------'''
	returned = dialogyesno(addonString(16).encode('utf-8'), addonString(17).encode('utf-8'))
	if returned == "ok":
		xbmc.executebuiltin('Addon.OpenSettings(script.htpt.emu)')
		xbmc.sleep(2000)
		dialogaddonsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogAddonSettings.xml)')
		while dialogaddonsettingsW and not xbmc.abortRequested:
			xbmc.sleep(1000)
			dialogaddonsettingsW = xbmc.getCondVisibility('Window.IsVisible(DialogAddonSettings.xml)')
			'''---------------------------'''
	if admin:
		print printfirst + name + space + "file1_fix" + space2 + file1_fix + newline + "file1_fix2" + space2 + file1_fix2 + newline + "configpath" + space2 + configpath + newline + "file1_fix" + space2 + file1_fix

def mode5(admin, name):
	'''------------------------------
	---MUSIC-DEBUG-------------------
	------------------------------'''
	if not systemplatformwindows:
		returned = dialogyesno(addonString(79), localize(79603))
		if returned == 'ok':					
			output = terminal('aplay -l | grep -e "card" | grep -n ""','aplay -l')
			output = output.split('\n')
			CARD_DEVICE = ""
			i = 0
			for line in output:
				if line != "":
					i += 1
					CARD_ = find_string(line, "card ", ": ")
					CARD_ = CARD_.replace("card ","")
					CARD_ = CARD_.replace(": ",",")
					DEVICE_ = find_string(line, "device ", ": ")
					DEVICE_ = DEVICE_.replace("device ","")
					DEVICE_ = DEVICE_.replace(": ","")
					CARD_DEVICE = CARD_DEVICE + newline + "OPTION" + str(i) + space2 + "hw:" + CARD_ + DEVICE_
					
			print CARD_ + space + DEVICE_ + newline + str(output) + "CARD_DEVICE" + space2 + CARD_DEVICE
			header = addonString(79).encode('utf-8')
			message2 = "[CR]---------------------------[CR]" + CARD_DEVICE + "[CR]---------------------------[CR][CR]" + addonString(77).encode('utf-8')
			w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
			w.doModal()
			'''---------------------------'''

def mode6(value, admin, name):
	'''------------------------------
	---Copy Config & Save Folders----
	------------------------------'''
	if value == '0': returned = "ok"
	else: returned = dialogyesno(addonString(18).encode('utf-8'), addonString(19).encode('utf-8') + '[CR]' + addonString(15).encode('utf-8'))
	if returned == "ok" and not systemplatformwindows:
		#path = os.path.join(addondata_path, 'script.htpt.emu', 'launchers.xml')
		#removefiles(path)
		path = os.path.join(htptemu_copyrepeat_path, 'emulators', '')
		ExtractAll(path + "retroarch.zip", emulators_path)
		terminal('chmod +x '+emulators_path+'','chmod' + space2 + emulators_path)
		
	else: notification_common("9")
	
	