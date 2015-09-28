import xbmc, xbmcgui, xbmcaddon
import os, sys

from shared_modules import *

def guicheck(admin):
	name = 'guicheck' ; printpoint = "" ; TypeError = "" ; extra = ""
	guisettings_file_ = read_from_file(guisettings_file, silent=True)
	guisettings2_file_ = read_from_file(guisettings2_file, silent=True)
	guisettings3_file_ = read_from_file(guisettings3_file, silent=True)
	guisettings4_file_ = read_from_file(guisettings4_file, silent=True)
	
	x = 'skin'
	guisettings_file_SKIN = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	guisettings2_file_SKIN = regex_from_to(guisettings2_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	guisettings3_file_SKIN = regex_from_to(guisettings3_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	guisettings4_file_SKIN = regex_from_to(guisettings4_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	
	x = '"skin.htpt.ID"'
	guisettings_file_ID = regex_from_to(guisettings_file_, ''+x+'>', '</setting>', excluding=True)
	guisettings2_file_ID = regex_from_to(guisettings2_file_, ''+x+'>', '</setting>', excluding=True)
	guisettings3_file_ID = regex_from_to(guisettings3_file_, ''+x+'>', '</setting>', excluding=True)
	guisettings4_file_ID = regex_from_to(guisettings4_file_, ''+x+'>', '</setting>', excluding=True)
	
	x = '"skin.htpt.VALIDATION2"'
	guisettings4_file_VALIDATION2 = regex_from_to(guisettings4_file_, ''+x+'>', '</setting>', excluding=True)
	guisettings2_file_VALIDATION2 = regex_from_to(guisettings2_file_, ''+x+'>', '</setting>', excluding=True)
	guisettings3_file_VALIDATION2 = regex_from_to(guisettings3_file_, ''+x+'>', '</setting>', excluding=True)
	
	x = 'systemtotaluptime'
	guisettings_file_UPTIME = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	guisettings2_file_UPTIME = regex_from_to(guisettings2_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	guisettings3_file_UPTIME = regex_from_to(guisettings3_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	guisettings4_file_UPTIME = regex_from_to(guisettings4_file_, '<'+x+'>', '</'+x+'>', excluding=True)
	try: guisettings_file_UPTIME = int(guisettings_file_UPTIME)
	except Exception, TypeError: guisettings_file_UPTIME = 0 ; extra = extra + newline + "TypeError" + space2 + str(TypeError)
	try: guisettings2_file_UPTIME = int(guisettings2_file_UPTIME)
	except Exception, TypeError: guisettings2_file_UPTIME = 0 ; extra = extra + newline + "TypeError" + space2 + str(TypeError)
	try: guisettings3_file_UPTIME = int(guisettings3_file_UPTIME)
	except Exception, TypeError: guisettings3_file_UPTIME = 0 ; extra = extra + newline + "TypeError" + space2 + str(TypeError)
	try: guisettings4_file_UPTIME = int(guisettings4_file_UPTIME)
	except Exception, TypeError: guisettings4_file_UPTIME = 0 ; extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if guisettings_file_SKIN != 'skin.htpt': printpoint = printpoint + "1"
	if guisettings_file_ID == "" or (guisettings_file_UPTIME > 1 and guisettings_file_UPTIME < guisettings2_file_UPTIME): printpoint = printpoint + "2"
	if guisettings4_file_VALIDATION2 == "true": printpoint = printpoint + "3"
	
	if guisettings2_file_SKIN != 'skin.htpt': printpoint = printpoint + "4"
	if guisettings2_file_ID == "": printpoint = printpoint + "5"
	if guisettings2_file_VALIDATION2 == "true": printpoint = printpoint + "6"
	
	if guisettings3_file_SKIN != 'skin.htpt': printpoint = printpoint + "7"
	if guisettings3_file_ID == "": printpoint = printpoint + "8"
	if guisettings3_file_VALIDATION2 == "true": printpoint = printpoint + "9"
	
	if (not "4" in printpoint and not "5" in printpoint and not "6" in printpoint) or (not "7" in printpoint and not "8" in printpoint and not "9" in printpoint):
		if guisettings_file_ID != guisettings2_file_ID and guisettings_file_ID != guisettings3_file_ID or (guisettings_file_UPTIME < guisettings2_file_UPTIME and guisettings_file_UPTIME < guisettings3_file_UPTIME):
			guisettings2_file_ID_len = len(guisettings2_file_ID)
			guisettings3_file_ID_len = len(guisettings3_file_ID)
			if (guisettings2_file_ID_len == 11 or guisettings3_file_ID_len == 11):
				printpoint = printpoint + "A"
	
	if printpoint == "": printpoint = printpoint + "_"
	
	print printfirst + name + "_LV" + printpoint + space + "guisettings_file_SKIN/2/3" + space2 + str(guisettings_file_SKIN) + space4 + str(guisettings2_file_SKIN) + space4 + str(guisettings3_file_SKIN) + newline + \
	"guisettings_file_ID" + space2 + str(guisettings_file_ID) + space + "guisettings2_file_ID" + space2 + str(guisettings2_file_ID) + space + "guisettings3_file_ID" + space2 + str(guisettings3_file_ID) + newline + \
	"guisettings_file_UPTIME" + space2 + str(guisettings_file_UPTIME) + space + "guisettings2_file_UPTIME" + space2 + str(guisettings2_file_UPTIME) + space + "guisettings3_file_UPTIME" + space2 + str(guisettings3_file_UPTIME)
	return printpoint, guisettings_file_

def guikeeper(admin, guicheck="", guiread=""):
	name = 'guikeeper' ; printpoint = "" ; TypeError = "" ; extra = ""
	if guiread == "": guiread_ = ""
	else: guiread_ = "V"
	
	if guicheck != "":
		printpoint = printpoint + "Q"
		if "A" in guicheck:
			printpoint = printpoint + "A"
			'''------------------------------
			---GUI-RESTORE-------------------
			------------------------------'''
			if not "4" in guicheck and not "5" in guicheck: printpoint = printpoint + "B"
			elif not "7" in guicheck and not "8" in guicheck: printpoint = printpoint + "C"
			elif not "4" in guicheck or not "5" in guicheck: printpoint = printpoint + "B"
			else: printpoint = printpoint + "D"
			'''---------------------------'''
		elif not "1" in guicheck and not "2" in guicheck:
			printpoint = printpoint + "W"
			if not "3" in guicheck:
				'''------------------------------
				---GUI-BACKUP--------------------
				------------------------------'''
				notification("guisettings backup", "", "", 1000)
				printpoint = printpoint + "E"
				if not "4" in guicheck and not "5" in guicheck and not "6" in guicheck: copyfiles(guisettings2_file, guisettings3_file, chmod="", mount=False)
				copyfiles(guisettings4_file, guisettings2_file, chmod="", mount=False)
				guiset(admin, guiread)
				'''---------------------------'''
		else: printpoint = printpoint + "9"
	
	
	print printfirst + name + "1_LV" + printpoint + space + "guicheck" + space2 + str(guicheck) + space + "guiread_" + space2 + str(guiread_) 
	
	if "A" in guicheck:
		'''------------------------------
		---GUI-RESTORE-------------------
		------------------------------'''
		if os.path.exists(skin_path) and xbmc.getCondVisibility('System.HasAddon(skin.htpt)'):
			returned = dialogyesno("guisettings.xml recover", "It's seem like your file has been corrupted!" + "[CR]Choose YES in order to recover it!", yes=True)
			if returned == "ok":
				target = guisettings_file
				if "B" in printpoint: killall(admin, custom="2")
				elif "C" in printpoint: killall(admin, custom="3")
				elif "D" in printpoint: pass
				'''---------------------------'''
			else:
				returned = dialogyesno("Use current guisettings.xml", "I know what i am doing! Do not show this message again!")
				if returned == "ok":
					notification("guisettings backup", "", "", 1000)
					printpoint = printpoint + "E"
					copyfiles(guisettings2_file, guisettings3_file, chmod="", mount=False)
					copyfiles(guisettings4_file, guisettings2_file, chmod="", mount=False)
					'''---------------------------'''
				else: pass
	elif xbmc.getSkinDir() != 'skin.htpt':
		printpoint = printpoint + "1"
		if os.path.exists(skin_path) and xbmc.getCondVisibility('System.HasAddon(skin.htpt)'):
			printpoint = printpoint + "2"
			if scripthtptinstall_Skin_Installed == "true" or scripthtptinstall_Skin_FirstBoot == "true" or os.path.exists(skininstalledtxt2):
				printpoint = printpoint + "3"
				setsetting_custom1('script.htpt.install','Skin_Default', "")
			else: printpoint = printpoint + "4"
			
			if scripthtptinstall_Skin_Default != 'HTPT':
				printpoint = printpoint + "5"
				returned = dialogyesno(addonString_servicehtpt(3), addonString_servicehtpt(4))
				if returned == "ok": printpoint = printpoint + "x"
				else:
					pass
			else:
				printpoint = printpoint + "x"
				notification("Skin Default is HTPT", "Entering HTPT now", "", 2000)

	else: printpoint = printpoint + "9"
	#replace_word(guisettings_file,old_word,new_word) ; terminal('TASKKILL /im Kodi.exe /f && "C:\Program Files (x86)\Kodi\Kodi.exe"',"GUI-ENTER")
			
	
	print printfirst + name + "2_LV" + printpoint + space + "xbmc.getSkinDir()" + space2 + xbmc.getSkinDir()
	
	if "x" in printpoint:
		if guiread == "": guisettings_file_ = read_from_file(guisettings_file, silent=True)
		else: guisettings_file_ = guiread
		
		x = 'skin' 
		old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
		if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
		new_word = '<'+x+'>skin.htpt</'+x+'>'
		if new_word != "N/A" and new_word != old_word:
			printpoint = printpoint + "7"
			notification(addonString(41), localize(31407), "", 2000)
			replace_word(guisettings_file,old_word,new_word) ; killall(admin, custom="1")
	#if "x" in printpoint: killall(admin)
	
def guiset(admin, guiread=""):
	name = 'guiset' ; printpoint = "" ; TypeError = "" ; extra = ""
	
	skinnamestr = xbmc.getInfoLabel('Skin.String(Skin_Name)')
	if guiread == "":
		guisettings_file_ = read_from_file(guisettings4_file, silent=True)
		if admin and not admin2: xbmc.sleep(2000)
	else: guisettings_file_ = guiread
	
	guisettings_file = guisettings4_file
	
	if not customgui and xbmc.getSkinDir() == 'skin.htpt':
		printpoint = printpoint + "1"
		if (scripthtptinstall_Skin_Installed != "true" and scripthtptinstall_Skin_FirstBoot != "true" and scripthtptinstall_User_ID != "" and scripthtptinstall_User_ID != "New"):
			printpoint = printpoint + "2"
			guiset_appearance(admin, guisettings_file, guisettings_file_)
			guiset_videos(admin, guisettings_file, guisettings_file_)
			guiset_music(admin, guisettings_file, guisettings_file_)
			guiset_livetv(admin, guisettings_file, guisettings_file_)
			guiset_pictures(admin, guisettings_file, guisettings_file_)
			guiset_weather(admin, guisettings_file, guisettings_file_)
			guiset_services(admin, guisettings_file, guisettings_file_)
			guiset_system(admin, guisettings_file, guisettings_file_)
	
	elif not customgui: extra = newline + "xbmc.getSkinDir()" + space2 + xbmc.getSkinDir()
	'''---------------------------'''
	x = 'addonnotifications' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'addonupdates' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'addonforeignfilter' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	
	print printfirst + name + "_LV" + printpoint + space + extra

def guiset_appearance(admin, guisettings_file, guisettings_file_):
	'''------------------------------
	---SKIN--------------------------
	------------------------------'''
	x = 'skin' #SKIN
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>skin.htpt</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'skintheme' #THEME
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'skintheme' #COLOURS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'font' #FONTS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if countrystr == "Israel": new_word = '<'+x+'>Arial</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'skinzoom' #ZOOM
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>0</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'startupwindow' #STARTUP WINDOW
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'soundskin' #NAVIGATION SOUNDS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>SKINDEFAULT</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---INTERNATIONAL-----------------
	------------------------------'''
	x = '' #LANGUAGE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'country' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or (countrystr == "Israel" and scripthtptinstall_Skin_FirstBoot == "true"): new_word = '<'+x+'>ISRAEL (24h)</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'charset'  #(DUPLICATED! CANT USE THAT!)
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>DEFAULT</'+x+'>'
	print "ahh" + space + new_word
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'keyboardlayouts' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if countrystr == "Israel": new_word = '<'+x+'>English ABC|Hebrew ABC</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	print "ahh" + space + new_word
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---FILE LISTS--------------------
	------------------------------'''
	x = 'showparentdiritems' #SHOW PARENT FOLDER ITEMS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'showextensions' #SHOW FILE EXTENSIONS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'ignorethewhensorting' #IGNORE ARTICALES WHEN SORTING
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'allowfiledeletion' #ALLOW FILE RENAMING AND DELETION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'showaddsourcebuttons' #SHOW ADD SOURCE BUTTON IN FILE LISTS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'showhidden' #SHOW HIDDEN FILES AND DIRECTORIES
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>false</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---SCREENSAVER-------------------
	------------------------------'''
	x = 'mode' #SCRENSAVER MODE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'></'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'time' #SCRENSAVER TIME
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>60</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usedimonpause' #USE DIM IF PAUSED DURING VIDEO PLAYBACK
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usemusicvisinstead' #USE DIM IF PAUSED DURING VIDEO PLAYBACK
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
		
def guiset_videos(admin, guisettings_file, guisettings_file_):
	'''------------------------------
	---LIBRARY-----------------------
	------------------------------'''
	x = 'showunwatchedplots' #SHOW PLOT FOR UNWATCHED ITEMS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'actorthumbs' #DOWNLOAD ACTOR THUMBNAILS WHEN ADDING TO LIBRARY
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if scripthtptdebug_Info_TotalSpace > 10: new_word = '<'+x+'>true</'+x+'>'
	else: new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'flatten' #FLATTEN LIBRARY HIERARCHY
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'flattentvshows' #FLATTEN TVSHOW SEASONS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>1</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'groupmoviesets' #GROUP MOVIES IN SETS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #UPDATELIBRARY ON STARTUP
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'backgroundupdate' #HIDE PROGRESS OF LIBRARY UPDATES
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---PLAYBACK----------------------
	------------------------------'''
	x = 'audiolanguage' #PREFERED AUDIO LANGUAGE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str: new_word = '<'+x+'>original</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'autoplaynextitem' #PLAY THE NEXT VIDEO AUTOMATICALLY
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'adjustrefreshrate' #ADJUST DISPLAY REFRESH RATE TO MATCH VIDEO
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'pauseafterrefreshchange' #PAUSE DURING REFRESH RATE CHANGE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usedisplayasclock' #SYNC PLAYBACK TO DISPLAY
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'synctype' #A/V SYNC METHOD
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>1</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'errorinaspect' #ALLOWD ERROR IN ASPECT RATIO TO MINIMISE BLACK BARS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'stretch43' #DISPLAY 4:3 VIDEOS AS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>3</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #ACTIVATE TELETEXT
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #SCALE TELETEXT TO 4:3
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #PLAYBACK MODE OF STEREOSCOPIC 3D VIDEOS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'quitstereomodeonstop' #DISABLE STEREOSCOPIC 3D MODE WHEN PLAYBACK ENDED
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---ACCELERATION------------------
	------------------------------'''
	x = 'rendermethod' #RENDER METHOD
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'hqscalers' #ENABLE HQ SCALERS FOR SCALINGS ABOVE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'decodingmethod' #DECODING METHOD
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>1</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	
	'''---------------------------'''
	x = 'limitgui' #
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>' #GAL TEST THIS!
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usevdpau' #ALLOW HARDWARE ACCELERATION (VDPAU) -NVIDIA/AMD*
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usevdpaumixer' #PREFER VDPAU VIDEO MIXER
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usevaapi' #ALLOW HARDWARE ACCELERATION (VAAPI) -INTEL
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>true</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usevaapimpeg2' #USE MPEG-2 VAAPI
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>false</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usevaapimpeg4' #USE MPEG-4 VAAPI
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>true</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'usevaapivc1' #USE VC-1 VAAPI
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str: new_word = '<'+x+'>false</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #PREFER VAAPI RENDER METHOD
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str: new_word = '<'+x+'>false</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	
	
	
	'''---------------------------'''
	x = 'usedxva2' #DXVA2 (WINDOWS?)
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---FILES-LIST--------------------
	------------------------------'''
	x = 'selectaction' #DEFAULT SELECT ACTION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>1</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'extractthumb' #EXTRACT THUMBNAILS AND VIDEO INFORMATION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if scripthtptdebug_Info_TotalSpace > 10: new_word = '<'+x+'>true</'+x+'>'
	else: new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'replacelabels' #REPLACE FILE NAMES WITH LIBRARY TITLES
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'stackvideos' #COMBINE SPLIT VIDEO ITEMS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---SUBTITLES---------------------
	------------------------------'''
	x = 'subtitlelanguage' #PREFERRED SUBTITLE LANGUAGE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>original</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'align' #SUBTITLE POSITION ON SCREEN
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'stereoscopicdepth' #STEREOSCOPIC 3D DEPTH OF SUBTITLES
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'font' #FONT TO USE FOR TEXT SUBTITLES
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	#new_word = '<'+x+'>arial.ttf</'+x+'>'
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'height' #SIZE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>32</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'style' #STYLE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>1</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'color' #COLOUR
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>1</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'charset' #CHARACTER SET (DUPLICATED! CANT USE THAT!)
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'languages' #LANGUAGES TO DOWNLOAD SUBTITLES FOR
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if countrystr == "Israel" or not id40str: new_word = '<'+x+'>English,Hebrew</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'pauseonsearch' #PAUSE WHEN SEARCHING FOR SUBTITLES
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>true</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'downloadfirst' #AUTO DOWNLOAD FIRST SUBTITLE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''	
	x = 'tv' #DEFAULT TV SERVICE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if countrystr == "Israel": new_word = '<'+x+'>service.subtitles.subscenter</'+x+'>'
	elif "Foreign" in countrystr: new_word = '<'+x+'>service.subtitles.opensubtitles</'+x+'>'
	else: new_word = '<'+x+'>service.subtitles.opensubtitles</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'movie' #DEFAULT MOVIE SERVICE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if countrystr == "Israel": new_word = '<'+x+'>service.subtitles.subscenter</'+x+'>'
	elif "Foreign" in countrystr: new_word = '<'+x+'>service.subtitles.opensubtitles</'+x+'>'
	else: new_word = '<'+x+'>service.subtitles.opensubtitles</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''

	'''------------------------------
	---DISCS-------------------------
	------------------------------'''
	x = '' #LANGUAGES TO DOWNLOAD SUBTITLES FOR
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''

def guiset_music(admin, guisettings_file, guisettings_file_):
	'''------------------------------
	---LIBRARY-----------------------
	------------------------------'''
	x = '' #INCLUDE ARTISTS WHO APPEAR ONLY ON COMPLIATIONS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---PLAYBACK----------------------
	------------------------------'''
	'''Conflict with videoplayer'''
	x = 'autoplaynextitem' #PLAY THE NEXT SONG AUTOMATICALLY
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'queuebydefault' #QUEUE SONGS ON SELECTION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'visualisation' #VISUALISATION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'></'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---FILE-LISTS--------------------
	------------------------------'''
	x = '' #ENABLE TAG READING
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---AUDIO-CD----------------------
	------------------------------'''
	x = '' #AUDIO CD INSERT ACTION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---KARAYOKE----------------------
	------------------------------'''
	x = '' #ENABLE KARAOKE SUPPORT
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''

	
def guiset_livetv(admin, guisettings_file, guisettings_file_):
	'''------------------------------
	---GENERAL-----------------------
	------------------------------'''
	x = '' #ENABLED
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #DO NOT SHOW CONNECTION LOST WARNINGS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #SYNCHRONISE CHANNEL GROUPS WITH BACKEND(S)
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #ALWAYS USE THE CHANNEL ORDER FROM BACKEND(S)
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = '' #USE BACKEND CHANNELS NUMBERS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---MENU/OS-----------------------
	------------------------------'''
	x = '' #SHOW CHANNEL INFORMATION WHEN SWITCHING CHANNELS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---EPG---------------------------
	------------------------------'''
	x = '' #DAYS TO DISPLAY IN THE EPG
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---PLAYBACK----------------------
	------------------------------'''
	x = '' #START PLAYBACK MINIMISED
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---RECORDING----------------------
	------------------------------'''
	x = '' #INSTANT RECORDING DURATION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---POWER-SAVING------------------
	------------------------------'''
	x = '' #ENABLED
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---PARENTAL-CONTROL--------------
	------------------------------'''
	x = '' #ENABLED
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
def guiset_pictures(admin, guisettings_file, guisettings_file_):
	x = 'usetags' #SHOW EXIF PICTURE INFORMATION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'generatethumbs' #AUTOMATICALLY GENERATE THUMBNAILS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'useexifrotation' #ROTATE PICTURES USING EXIF INFORMATION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'showvideos' #SHOW VIDEO FILES IN LISTINGS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
def guiset_weather(admin, guisettings_file, guisettings_file_):
	x = 'addon' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>weather.yahoo</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
def guiset_services(admin, guisettings_file, guisettings_file_):
	'''------------------------------
	---GENERAL-----------------------
	------------------------------'''
	x = 'devicename' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>HTPT</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---UPnP--------------------------
	------------------------------'''
	x = 'upnprenderer' #ALLOW CONTROL ON KODI
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---INTERNET-SERVER---------------
	------------------------------'''
	x = 'webserver' #ALLOW CONTROL ON KODI
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'webserverport' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>8080</'+x+'>'
	else: new_word = "N/A"
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'webserverusername' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>HTPT</'+x+'>'
	else: new_word = "N/A"
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'webserverpassword' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'></'+x+'>'
	else: new_word = "N/A"
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---REMOTE-CONTROL----------------
	------------------------------'''
	x = 'esenabled' #ALLOW CONTROL FROM PROGRAMS IN THIS SYSTEM
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'esallinterfaces' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---ZEROCONF----------------------
	------------------------------'''
	x = 'zeroconf' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---AIRPLAY-----------------------
	------------------------------'''
	x = 'airplay' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if performance and ("C" in id10str or "D" in id10str): new_word = '<'+x+'>false</'+x+'>'
	elif not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>true</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'airplaypassword' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str: new_word = '<'+x+'></'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'airplayvolumecontrol' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>true</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'useairplaypassword' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>false</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---SMB---------------------------
	------------------------------'''
	x = 'workgroup' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>MSHTPT</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
def guiset_system(admin, guisettings_file, guisettings_file_):
	'''------------------------------
	---VIDEO-------------------------
	------------------------------'''
	x = 'screenmode' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str and systemplatformlinux: new_word = '<'+x+'>00192001080060.00000pstd</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'resolution' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str and systemplatformlinux: new_word = '<'+x+'>18</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'vsync' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>2</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---AUDIO-------------------------
	------------------------------'''
	x = 'streamsilence' #KEEP AUDIO DEVICE ALIVE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or xbmc.getCondVisibility('System.HasAddon(script.htpt.emu)'): new_word = '<'+x+'>0</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'guisoundmode' #PLAY GUI SOUNDS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or xbmc.getCondVisibility('System.HasAddon(script.htpt.emu)'): new_word = '<'+x+'>0</'+x+'>'
	elif scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>1</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'processquality' #PLAY GUI SOUNDS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if performance and not "A" in id10str and not "B" in id10str: new_word = '<'+x+'>20</'+x+'>'
	elif not "A" in id10str and not "B" in id10str: new_word = '<'+x+'>30</'+x+'>'
	else: new_word = '<'+x+'>50</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	
	'''------------------------------
	---INPUT-DEVICES-----------------
	------------------------------'''
	x = 'enablemouse' #ENABLE MOUSE AND TOUCH SCREEN SUPPORT
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'enablejoystick' #ENABLE JOYSTICK AND GAMEPAD SUPPORT
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	if not id40str or xbmc.getCondVisibility('System.HasAddon(script.htpt.emu)'): new_word = '<'+x+'>true</'+x+'>'
	elif scripthtptinstall_Skin_FirstBoot == "true": new_word = '<'+x+'>false</'+x+'>'
	else: new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---INTERNET-ACCESS---------------
	------------------------------'''
	pass
	'''---------------------------'''
	
	'''------------------------------
	---POWER-SAVING------------------
	------------------------------'''
	x = 'displaysoff' #PUT DISPLAY TO SLEEP WHEN IDLE
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'shutdownstate' #SHUTDOWN FUNCTION TIMER
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'shutdowntime' #SHUTDOWN FUNCTION
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>0</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'wakeonaccess' #TRY TO WAKE REMOTE SERVERS ON ACCESS
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---DEBUGGING---------------------
	------------------------------'''
	x = 'extralogging' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'screenshotpath' 
	screenshot_path = os.path.join(pictures_path, 'screenshots', '')
	if not os.path.exists(screenshot_path): os.mkdir(screenshot_path)
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>'+screenshot_path.encode('utf-8')+'</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'setextraloglevel' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'showloginfo' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
	'''------------------------------
	---MASTER-LOCK-------------------
	------------------------------'''
	x = 'maxretries' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	x = 'startuplock' 
	old_word = regex_from_to(guisettings_file_, '<'+x+'>', '</'+x+'>', excluding=False)
	if old_word == '<'+x+'></'+x+'>': old_word = regex_from_to(guisettings_file_, '<'+x+' default="true">', '</'+x+'>', excluding=False)
	new_word = '<'+x+'>N/A</'+x+'>'
	if not "N/A" in new_word and new_word != old_word: replace_word(guisettings_file,old_word,new_word)
	'''---------------------------'''
	
