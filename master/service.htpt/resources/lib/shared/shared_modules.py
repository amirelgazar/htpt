import xbmc, xbmcgui, xbmcaddon
import os, sys

try: from variables import *
except:
	try: from shared_variables import *
	except: pass

#if admin: from shared_modules2 import *
xbmc.sleep(100)

def CreateZip(src, dst, filteron=[], filteroff=[], level=10000, append=False, ZipFullPath=False, temp=False):

	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	name = 'CreateZip'
	TypeError = "" ; extra = "" ; arcname = "" ; absname = "" ; dirname = "" ; files = "" ; printpoint = "" ; file = "" ; subdirs = "" ; subdir = "" ; temp__ = ".zip" ; returned = ""
	if append == False: append_ = "w"
	else: append_ = "a"
	
	if temp == False: temp_ = temp__
	else: temp_ = "_temp.zip"
	
	import zipfile
	zf = zipfile.ZipFile("%s%s" % (dst, temp_), append_, zipfile.ZIP_DEFLATED)
	abs_src = os.path.abspath(src)
	
	for dirname, subdirs, files in os.walk(src):

		printpoint = "" ; extra2 = ""
		
		subdir = dirname.replace(src, "")
		
		
		if systemplatformwindows:
			try: subdir2 = find_string(subdir, subdir[:1], "\\") ; subdir2 = subdir2.replace("\\","")
			except: subdir2 = "?"
			subdir_level = subdir.count("\\")
		else:
			try: subdir2 = find_string(subdir, subdir[:1], "/") ; subdir2 = subdir2.replace("/","")
			except: subdir2 = "?"
			subdir_level = subdir.count("/")
		
		if not os.path.exists(dst+temp_):
			zf.close()
			dialogok("Error Abort","","","")
			sys.exit()
		
		if subdir_level <= level:
			printpoint = printpoint + "1"
			if filteron == [] or subdir in filteron or subdir == "" or subdir2 in filteron:
				printpoint = printpoint + "2"
				if filteroff == [] or (not subdir in filteroff and not subdir2 in filteroff):
					printpoint = printpoint + "3"
					for filename in files:
						printpoint = printpoint + "4" ; extra2 = extra2 + space + "filename" + space2 + filename
						if filteron == [] or filename in filteron or subdir in filteron or subdir2 in filteron:
							printpoint = printpoint + "5"
							if filteroff == [] or not filename in filteroff:
								printpoint = printpoint + "6"
								absname = os.path.abspath(os.path.join(dirname, filename))
								arcname = absname[len(abs_src) + 1:]
								arcname1dir = find_string(arcname, arcname[:2], "/")
								print 'zipping %s as %s' % (os.path.join(dirname, filename),arcname)
								#if filteron == [] or arcname in filteron:
								#if filteroff == [] or not arcname in filteroff:
								try:
									if ZipFullPath == False: zf.write(absname, arcname)
									else:
										if systemplatformwindows:
											absname2 = absname
											if "\\Kodi\\" in absname2:
												split = absname2.split("Kodi")
												absname2 = absname2.replace(split[0]+'Kodi\\',"")
											elif "\\XBMC\\" in absname2:
												split = absname2.split("XBMC")
												absname2 = absname2.replace(split[0]+'XBMC\\',"")
											
											
											#if len(split[0]) == 2: absname2 = split[0] + "\\" + absname
											if admin: print printfirst + name + space + "absname2_test" + space2 + "split[0]" + space2 + str(split[0]) + space + "split[1]" + space2 + str(split[1]) + space
											#if "C:\\" in absname2: absname2 = absname2.replace("C:\\","C:\\\\")
											zf.write(absname, absname2)
										else:
											absname2 = absname.replace('/storage/','/')
											zf.write(absname, absname2)
											'''---------------------------'''

									printpoint = printpoint + "7"
									'''---------------------------'''
								except Exception, TypeError:
									printpoint = printpoint + "8"
									TypeError = str(TypeError) + space + "absname" + space2 + str(absname) + space + "arcname" + space2 + str(arcname)
									'''---------------------------'''
									
		else: printpoint = printpoint + "9"				
		if admin: print "Admin-Test_LV" + printpoint + space + "dirname" + space2 + str(dirname) + space + "subdir" + space2 + str(subdir) + space + "subdir_level" + space2 + str(subdir_level) + space + "subdir2" + space2 + str(subdir2) + space + "files" + space2 + str(files) + space + "file" + space2 + str(file) + space + "level" + space2 + str(level) + space + extra2
	
	#except Exception, TypeError:
	#TypeError = str(TypeError) + space + "os.walk(src)" + space2 + str(os.walk(src)) + space + "src" + space2 + str(src) + space + "dirname" + space2 + dirname + space + "files" + space2 + str(files)
	#notification("Error 1050","","",1000)
	#continue

	zf.close()
	
	if append == "End" and temp == True:
		xbmc.sleep(500)
		removefiles(dst + temp__)
		try:
			os.rename(dst + temp_, dst + temp__)
			#else: terminal('mv -f '+dst+''+temp_+' '+dst+''+temp__+'',"End Zip")
			notification("Zip File Ready!", dst + temp__, "", 2000)
		except Exception, TypeError:
			notification("Zip File Error!", dst + temp__, "", 2000)
		
		
		'''---------------------------'''
		returned = 'ok'
	elif temp != True and append == False: returned = 'ok'
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if TypeError != "": extra = newline + "TypeError:" + space2 + str(TypeError)
	print printfirst + name + "_LV" + printpoint + space + "src" + space2 + str(src) + space + "dst" + space2 + str(dst) + space + "filteron" + space2 + str(filteron) + space + "filteroff" + space2 + str(filteroff) + space + "level" + space2 + str(level) + space + newline + "arcname" + space2 + str(arcname) + space + "absname" + space2 + str(absname) + space + "abs_src" + space2 + str(abs_src) + space + "dirname" + space2 + str(dirname) + space + "files" + space2 + str(files) + space + "subdirs" + space2 + str(subdirs) + space + "subdir" + space2 + str(subdir) + space + extra
	'''---------------------------'''
	return returned	
	
			
def ExtractAll(source, output):
	name = 'ExtractAll' ; printpoint = "" ; TypeError = "" ; extra = ""
	if not admin3 or 1 + 1 == 2:
		if ".zip" in source:
			import zipfile
			#import zlib
			try:
				zin = zipfile.ZipFile(source, 'r')
				#zin = zipfile.ZipFile(source, 'r',allowZip64=True)
				zin.extractall(output)
				zin.close()
				printpoint = printpoint + "7"
			
			except Exception, TypeError:
				
				#if "compression type 9 (deflate64)" in TypeError:
				printpoint = printpoint + "9"
				
		
		elif ".tar" in source:
			import tarfile
			try:
				tar = tarfile.open(source)
				#terminal('mv -f '+ source +' '+ output +'',"move tar") #UNTESTED
				tar.extractall(output)
				tar.close()
				printpoint = printpoint + "7"
			except Exception, TypeError:
				printpoint = printpoint + "9"
		
		elif ".7z" in source:
			#NOT WORKING!
			import gzip
			f_in = open(source, 'rb')
			f_out = gzip.open(output, 'wb')
			f_out.writelines(f_in)
			f_out.close()
			f_in.close()
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if TypeError != "": extra = newline + "TypeError:" + space2 + str(TypeError)
	print printfirst + name + "_LV" + printpoint + space + "source" + space2 + source + space + "output" + space2 + output + space + extra
	
	'''---------------------------'''
	if "7" in printpoint: return True
	else: return False

def getFileAttribute(custom, file):
	name = 'getFileAttribute' ; printpoint = "" ; extra = "" ; returned = ""
	
	if not os.path.exists(file): printpoint = printpoint + "8"
	elif custom == 1: #last modified
		import time
		returned = time.ctime(os.path.getmtime(file))
		extra = extra + newline + "timenow5" + space2 + str(timenow5)
		
	elif custom == 2: #size
		returned = os.path.getsize(file)
	
	if admin and not admin2 and admin3: print printfirst + name + "_LV" + printpoint + space + "custom" + space2 + str(custom) + space + "file" + space2 + str(file) + newline + \
	"returned" + space2 + str(returned) + extra
	return returned

def localize(value, s=None):
	name = 'localize'
	admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	TypeError = "" ; extra = "" ; returned = "" ; value = str(value)
	try: returned = xbmc.getInfoLabel('$LOCALIZE['+value+']')
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	try: returned = returned.decode('utf-8') #GAL TEST THIS!
	except: pass
	
	try: value = value.encode('utf-8')
	except: pass
	
	if s != None:
		'''not working!'''
		s2 = str(s)
		s2 = s2.split(",")
		s2 = str(s2)
		s2 = s2.replace('["',"")
		s2 = s2.replace("['","")
		s2 = s2.replace('"]',"")
		s2 = s2.replace("']","")
		print str(s2) + newline + str(s)
		returned = xbmc.getInfoLabel('$LOCALIZE['+value+']') % (s2)
	
	try: returned = returned.encode('utf-8')
	except: pass
	
	if (admin and not admin2 and admin3 and 1 + 1 == 3) or extra != "":
		print printfirst + name + space + "value" + space2 + str(value) + space + "returned" + space2 + str(returned) + space + extra
	return returned
	
def DownloadFile(url, filename, downloadpath, extractpath, silent=False):
	name = 'DownloadFile' ; TypeError = "" ; extra = ""
	downloadpath2 = os.path.join(downloadpath, filename)
	
	from commondownloader import *
	if servicehtptfix_General_DownloadON == "true":
		returned = "skip"
		notification_common("23")
	else:
		try: setsetting_custom1('service.htpt.fix','General_DownloadON',"true")
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
		try: returned = doDownload(url, downloadpath2, filename, "", "", "", silent)
		except exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			returned = str(TypeError)
		try: setsetting_custom1('service.htpt.fix','General_DownloadON',"false") ; xbmc.sleep(40)
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if returned == "ok":
		#dialogok("download done","","","")
		#urllib.urlretrieve(url, downloadpath2) #, reporthook=dlProgress
		ExtractAll(downloadpath2, extractpath)
	
	try:
		if downloadpath2 != downloadpath: os.remove(downloadpath2)
	except:
		pass
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin3 or extra != "" or 1 + 1 == 2: print printfirst + name + space + "url" + space2 + url + space + "returned" + space2 + str(returned) + extra
	'''---------------------------'''
	
def addonsettings2(addon,set1,set1v,set2,set2v,set3,set3v,set4,set4v,set5,set5v):
	'''------------------------------
	---SET-ADDON-SETTING-5-----------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
		getsetting_custom          = xbmcaddon.Addon(addon).getSetting
		setsetting_custom          = xbmcaddon.Addon(addon).setSetting

		setting1 = getsetting_custom(set1)
		setting2 = getsetting_custom(set2)
		setting3 = getsetting_custom(set3)
		setting4 = getsetting_custom(set4)
		setting5 = getsetting_custom(set5)
		
		checkChange = "false"
		'''---------------------------'''
		if set1 != "" and set1v != setting1:
			setsetting_custom(set1,set1v)
			if checkChange != "true": checkChange = "true"
		if set2 != "" and set2v != setting2:
			setsetting_custom(set2,set2v)
			if checkChange != "true": checkChange = "true"
		if set3 != "" and set3v != setting3:
			setsetting_custom(set3,set3v)
			if checkChange != "true": checkChange = "true"
		if set4 != "" and set4v != setting4:
			setsetting_custom(set4,set4v)
			if checkChange != "true": checkChange = "true"
		if set5 != "" and set5v != setting5:
			setsetting_custom(set5,set5v)
			if checkChange != "true": checkChange = "true"
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if checkChange == "true" and (admin3 or scripthtptinstall_Skin_Installed == "true"): print printfirst + "addonsettings2 " + addon + space + set1 + space2 + set1v + space + set2 + space2 + set2v + space + set3 + space2 + set3v + space + set4 + space2 + set4v + space + set5 + space2 + set5v + space
		'''---------------------------'''

def checkAddon_Update(admin, Addon_Update, Addon_Version, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2):
	from variables import addonVersion
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	#addonVersion          = xbmcaddon.Addon().getAddonInfo("version")
	#reload(addonVersion)
	#notification(addonVersion,"","",5000)
	
	if Addon_Update != "true" or (Addon_Update == "true" and Addon_Version == addonVersion):
		'''------------------------------
		---Addon_Update-(NEW-ONLY)--------
		------------------------------'''
		Addon_Update = setAddon_Update(admin, addonVersion, Addon_Version, Addon_Update)
		'''---------------------------'''
	
	if Addon_Update == "true":
		'''------------------------------
		---setAddon_Version---------------
		------------------------------'''
		Addon_Version = setAddon_Version(admin, addonVersion, Addon_Version)
		'''---------------------------'''
		
	if Addon_Update == "true" or Addon_UpdateDate == "":
		'''------------------------------
		---setAddon_UpdateDate-(NEW-ONLY)-
		------------------------------'''
		Addon_UpdateDate = setAddon_UpdateDate(admin, addonVersion, Addon_Version, Addon_Update, Addon_UpdateDate)
		'''---------------------------'''
	
	if Addon_Version == addonVersion and Addon_UpdateLog == "true" and Addon_UpdateDate != "":
		'''------------------------------
		---Addon_UpdateLog----------------
		------------------------------'''
		dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
		dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
		custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
		if not dialogokW and not dialogselectW and not dialogprogressW and not dialogbusyW and not startupW and not dialogtextviewerW and not custom1191W:
			from variables import datenowS
			if datenowS != "": #PREVENT RANDOM BUG WITH datetime
				setAddon_UpdateLog(admin, Addon_Version, Addon_UpdateDate, Addon_ShowLog, Addon_ShowLog2, datenowS)
				'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and not admin2 and admin3: print printfirst + "checkAddon_Update" + space2 + "Addon_Update" + space2 + Addon_Update + space + "Addon_Version" + space2 + Addon_Version + space + "addonVersion" + space2 + addonVersion + space + "Addon_UpdateDate" + space2 + Addon_UpdateDate + space + "Addon_UpdateLog" + space2 + Addon_UpdateLog
	'''---------------------------'''
				
def setAddon_Update(admin, addonVersion, Addon_Version, Addon_Update):
	'''------------------------------
	---CHECK-FOR-FIX-UPDATE----------
	------------------------------'''
	Addon_Update2 = Addon_Update
	if Addon_Version != addonVersion and Addon_Update == "false":
		Addon_Update2 = "true"
		setsetting('Addon_UpdateLog',"true")
		'''---------------------------'''
	else:
		Addon_Update2 = "false"
		'''---------------------------'''
		
	if Addon_Update != Addon_Update2: setsetting('Addon_Update',Addon_Update2)
	'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and Addon_Update != Addon_Update2 and admin3 and not admin2: print printfirst + "setAddon_Update" + space2 + Addon_Update + " - " + Addon_Update2
	'''---------------------------'''	
	return Addon_Update2

def setAddon_Version(admin, addonVersion, Addon_Version):
	'''------------------------------
	---CHECK-FOR-ADDON-UPDATE-2------
	------------------------------'''
	Addon_Version2 = Addon_Version
	'''---------------------------'''
	if Addon_Version != addonVersion:
		Addon_Version2 = addonVersion
		setsetting('Addon_Version',Addon_Version2)
		'''---------------------------'''	
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if Addon_Version != addonVersion or admin and not admin2 and admin3: print printfirst + "setAddon_Version" + space2 + Addon_Version + " - " + Addon_Version2
	'''---------------------------'''
	return Addon_Version2
		
def setAddon_UpdateDate(admin, addonVersion, Addon_Version, Addon_Update, Addon_UpdateDate):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	from variables import datenowS
	Addon_UpdateDate2 = Addon_UpdateDate
	'''---------------------------'''
	if Addon_UpdateDate != datenowS:
		Addon_UpdateDate2 = datenowS
		setsetting('Addon_UpdateDate',Addon_UpdateDate2)
		'''---------------------------'''

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if Addon_Version != addonVersion or admin and not admin2 and admin3: print printfirst + "setAddon_UpdateDate" + space2 + Addon_UpdateDate + " - " + Addon_UpdateDate2
	'''---------------------------'''
	return Addon_UpdateDate2
	
def setAddon_UpdateLog(admin, Addon_Version, Addon_UpdateDate, Addon_ShowLog, Addon_ShowLog2, datenowS):	
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	if Addon_ShowLog == "true":
		from variables import addonID, addonName2
		printpoint = "" ; TypeError = "" ; extra = ""
		number2S = ""
		datenowD = stringtodate(datenowS,'%Y-%m-%d')
		datedifferenceD = stringtodate(Addon_UpdateDate,'%Y-%m-%d')
		datedifferenceS = str(datedifferenceD)
		if "error" in [datenowD, datedifferenceD]: printpoint = printpoint + "9"
		try:
			number2 = datenowD - datedifferenceD
			number2S = str(number2)
			printpoint = printpoint + "2"
			'''---------------------------'''
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			printpoint = printpoint + "9"
			'''---------------------------'''
		try:
			Addon_ShowLog2 = int(Addon_ShowLog2)
			Addon_ShowLog2 = str(Addon_ShowLog2)
			printpoint = printpoint + "3"
			'''---------------------------'''
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			Addon_ShowLog2 = "1"
			printpoint = printpoint + "4"
			'''---------------------------'''
		if not "9" in printpoint:
			printpoint = printpoint + "5"
			if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
			elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
			else: number2S = "0"
			if admin: notification("number2S:" + number2S,"","",2000)
			number2N = int(number2S)
			'''---------------------------'''
			#header = '[COLOR=Yellow]' + addonString(304).encode('utf-8') + " - " + addonVersion + '[/COLOR]'
			if number2N == 0: header = '[COLOR=Yellow]' + localize(24065) + space + localize(33006) + space5 + Addon_Version + '[/COLOR]'
			elif number2N == 1: header = '[COLOR=Green]' + localize(24065) + space + addonString_servicehtpt(5).encode('utf-8') + space5 + Addon_Version + '[/COLOR]'
			elif number2N <= 7: header = '[COLOR=Purple]' + localize(24065) + space + addonString_servicehtpt(6).encode('utf-8') + space5 + Addon_Version + '[/COLOR]'
			else: header = ""
			'''---------------------------'''
			if number2N <= int(Addon_ShowLog2):
				printpoint = printpoint + "7"
				log = open(addonPath + "/" + 'changelog.txt', 'rb')
				message2 = log.read()
				log.close()
				message2S = str(message2)
				message3 = message2[0:8000]
				message3 = '"' + message3 + '"'
				message3S = str(message3)
				if header != "":
					w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
					w.doModal()
					'''---------------------------'''
			else: printpoint = printpoint + "8"
	#setsetting('Addon_UpdateLog',"false")
	setsetting_custom1(addonID, 'Addon_UpdateLog', "false")
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "setAddon_UpdateLog_LV" + printpoint + space2 + "Addon_UpdateDate" + space2 + Addon_UpdateDate + " - " + datenowS + "(" + number2S + ")" + space + newline + \
	"Addon_UpdateLog" + space2 + Addon_UpdateLog + space + "Addon_ShowLog" + space2 + str(Addon_ShowLog) + space + "Addon_ShowLog2" + space2 + str(Addon_ShowLog2) + extra
	'''---------------------------'''


def terminal(command,desc):
	import subprocess
	customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)') ; admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)') ; printpoint = "" ; TypeError = "" ; extra = "" ; output = ""
	#print command
	try:
		if systemplatformandroid:
			#process = subprocess.Popen(x, stdout=subprocess.PIPE)
			#process = subprocess.Popen(x, stderr=subprocess.STDOUT)
			
			process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=False)
			#process = subprocess.Popen(command,stderr=subprocess.STDOUT,shell=False)
			output = process.communicate()[0]
			'''---------------------------'''
		else:
			process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
			output = process.communicate()[0]
			'''---------------------------'''
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if 'Permission denied' in TypeError:
		printpoint = printpoint + '9'
		if scripthtptsmartbuttons_General_Terminal == 'true':
			setsetting_custom1('script.htpt.smartbuttons','General_Terminal',"false")
			if xbmc.getSkinDir() == 'skin.htpt':
				xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=60&value=2)')
				'''---------------------------'''
				if systemplatformandroid:
					write_to_file(guikeepertxt_file, 'adb kill-server', append=False, silent=True , utf8=False) ; xbmc.sleep(10) ; os.system('sh '+guikeepersh_file+'')
					write_to_file(guikeepertxt_file, 'adb start-server', append=False, silent=True , utf8=False) ; xbmc.sleep(10) ; os.system('sh '+guikeepersh_file+'')
					write_to_file(guikeepertxt_file, 'adb devices', append=False, silent=True , utf8=False) ; xbmc.sleep(10) ; os.system('sh '+guikeepersh_file+'')
					write_to_file(guikeepertxt_file, "", append=False, silent=True , utf8=False)
					'''---------------------------'''
			
	if output == "":
		printpoint = printpoint + '5'
		if systemplatformandroid:
			write_to_file(guikeepertxt_file, command, append=False, silent=True , utf8=False) ; xbmc.sleep(10) ; os.system('sh '+guikeepersh_file+'')
			write_to_file(guikeepertxt_file, "", append=False, silent=True , utf8=False)
			'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if ((admin and admin2 and admin3 or extra != "") or TypeError != "") and not customhomecustomizerW and scripthtptsmartbuttons_General_Terminal == 'true' or 'killall' in command or 'TASKKILL' in command:
		try: print printfirst + "terminal_LV" + printpoint + space + desc + space2 + str(output) + extra
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			print printfirst + "terminal_LV" + printpoint + space + "desc" + space2 + str(desc) + extra
		'''---------------------------'''
	return output

def bash(bashCommand,bashname): #TEMP
	import subprocess
	if not systemplatformwindows:
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)') ; TypeError = "" ; output = ""
		
		try:
			#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			process = subprocess.Popen(bashCommand,stdout=subprocess.PIPE,shell=True)
			output = process.communicate()[0]
			'''---------------------------'''
		except Exception, TypeError: pass
	
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if admin and admin2 or str(TypeError) != "": print printfirst + bashname + space2 + output + newline + "TypeError" + space2 + str(TypeError)
		'''---------------------------'''
		return output

def cmd(cmdCommand,cmdname): #TEMP
	import subprocess
	if systemplatformwindows:
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
		
		process = subprocess.Popen(cmdCommand,stdout=subprocess.PIPE,shell=True)
		output = process.communicate()[0]
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		try: output = output.encode('utf-8')
		except: output = "?"
		
		if admin and admin2 and admin3: print printfirst + "cmd" + space2 + cmdname + space + cmdCommand + space + "output" + space2 + str(output)
		'''---------------------------'''
		return output
		
def find_string(findin, findwhat, findwhat2):
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	
	findin = str(findin)
	findinL = len(findin)
	findinLS = str(findinL)
	findinLN = int(findinLS)
	findwhat = str(findwhat)
	findwhatL = len(findwhat)
	findwhatLS = str(findwhatL)
	findwhatLN = int(findwhatLS)
	findwhat2 = str(findwhat2)
	findwhat2L = len(findwhat2)
	findwhat2LS = str(findwhat2L)
	findwhat2LN = int(findwhat2LS)
	'''---------------------------'''
	
	findin_start = findin.find(findwhat, 0, findinL)
	findin_startS = str(findin_start)
	findin_startN = int(findin_startS) + findwhatLN
	findin_startS = str(findin_start)
	'''---------------------------'''
	if findwhat2 == "": findin_end = findin.find(findwhat2, findin_startN, findinL)
	else:
		findin_end = findin.find(findwhat2, findin_startN, findin_startN + findwhatLN)
		if findin_end == -1: findin_end = findin.find(findwhat2, findin_startN, findinL)
	findin_endS = str(findin_end)
	findin_endN = int(findin_endS) + findwhat2LN
	'''---------------------------'''
	findin_startN = int(findin_startS) #SOME KIND OF BUG? BUT WORKING THIS WAY!
	if findwhat == "": findin_startN = 0
	if findwhat2 == "": findin_endN = findinLN
	found = findin[findin_startN:findin_endN]
	foundS = str(found)
	'''---------------------------'''
	try:
		foundF = float(foundS)
		found2 = round(foundF)
		found2S = str(found2)
		if ".0" in found2S: found2S = found2S.replace(".0","",1)
	except: pass
	
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and admin2 and admin3:
		print printfirst + "find_string" + space + "findin" + space2 + findin + newline + \
		"(" + findinLS + ")" + space + "findwhat" + space2 + findwhat + newline + \
		"(" + findwhatLS + ")" + space +  "findin_startS" + space2 + findin_startS + space + "findin_endS" + space2 + findin_endS + newline + \
		"findin_start" + space2 + str(findin_start) + space + "findin_startN" + space2 + str(findin_startN) + newline + \
		"foundS" + space2 + foundS
		'''---------------------------'''
	return foundS
	
def calculate(addon, set1, custom, opt):
	'''------------------------------
	---RETURN-CALCULATE-NUMBER-------
	------------------------------'''
	printpoint = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	setsetting_custom          = xbmcaddon.Addon(addon).setSetting
		
	set1v = getsetting_custom(set1)
	try: set1v = int(set1v)
	except: printpoint = printpoint + "1"
	
	try:
		if custom > 1 or custom < -1: printpoint = printpoint + "3"
	except: pass
	
	if opt != "": set2v = int(opt)
	else: set2v = ""
	'''---------------------------'''
	if custom == '1':
		if not "1" in printpoint: set1v += 1
		if opt != "": set2v += 1
		'''---------------------------'''
	elif custom == '2':
		if not "1" in printpoint: set1v += -1
		if opt != "": set2v += -1
		'''---------------------------'''
	elif "3" in printpoint:
		if not "1" in printpoint: set1v += custom
		if opt != "": set2v += custom
		custom = str(custom) + "*"
		'''---------------------------'''
		
				
	set1v = str(set1v)
	if opt != "": set2v = str(set2v)
	'''---------------------------'''
	if opt != "": setsetting_custom(set1, set2v) #setsetting(set1, set2v) #setsetting_custom1(addon,set1,set2v) #setsetting_custom(set1, set2v)
	else: setsetting_custom(set1, set1v) #setsetting(set1, set1v) #setsetting_custom1(addon,set1,set1v) #setsetting_custom(set1, set1v)
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''	
	if admin and admin2 and admin3: print printfirst + "calculate_LV" + printpoint + space + addon + space + set1 + space + "set1v" + space + set1v + space + "set2v" + space + set2v + space + "custom" + space2 + str(custom)
	if opt != "": return set2v
	else: return set1v
	'''---------------------------'''

def bash_count(path_, level=0):
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; folders_count = 0 ; subdir_count = 0 ; files_count = 0 ; list_count = [[],'']
	printpoint = ""
	if systemplatformandroid:
		import os
		if '*' in path_:
			printpoint = printpoint + '0'
			path_ = path_.replace('*',"")
				
		for dirname, subdirs, files in os.walk(path_):
			subdir = dirname.replace(path_, "")
			
			if systemplatformwindows:
				try: subdir2 = find_string(subdir, subdir[:1], "\\") ; subdir2 = subdir2.replace("\\","")
				except: subdir2 = "?"
				subdir_level = subdir.count("\\")
				'''---------------------------'''
			else:
				try: subdir2 = find_string(subdir, subdir[:1], "/") ; subdir2 = subdir2.replace("/","")
				except: subdir2 = "?"
				subdir_level = subdir.count("/")
				'''---------------------------'''
				
			if subdir_level <= level:
				if not dirname in list_count: list_count.append(dirname) ; folders_count += 1
				if not subdir in list_count: list_count.append(subdir) ; subdir_count += 1
				if not files in list_count: list_count.append(files) ; files_count += 1
				
		
		#folders_count = terminal('find '+ path_ +' -type d | wc -l', "folders_count")
		#subdir_count = terminal('find '+ path_ +' -type d -prune | wc -l', "folders_count")
		#files_count = terminal('find '+ path_ +' -type f | wc -l', "files_count")
	elif systemplatformlinux or systemplatformlinuxraspberrypi:
		folders_count = terminal('find '+ path_ +' -type d | wc -l', "folders_count")
		subdir_count = terminal('find '+ path_ +' -type d -prune | wc -l', "folders_count")
		files_count = terminal('find '+ path_ +' -type f | wc -l', "files_count")
		'''---------------------------'''
	elif systemplatformwindows:
		#folders_count = terminal('dir /AD /B '+ path_ +' | find /C /V "<DIR>"', "folders_count") #GAL CHECK THIS!
		subdir_count = terminal('dir /AD /B "'+ path_ +'" | find /C /V "<DIR>"', "folders_count") 
		files_count = terminal('dir /A-D /B /S "'+ path_ +'" | find /C /V "File(s)"', "folders_count")
		#files_count = int(files_count)
		#if files_count > 0: files_count = int(files_count) - 1
		'''---------------------------'''
		
	#print "path_" + space2 + path_ + newline + "folders_count" + space2 + str(folders_count)
	try: folders_count = int(folders_count) ; folders_count = str(folders_count)
	except: folders_count = "0"
	try: subdir_count = int(subdir_count) ; subdir_count = str(subdir_count)
	except: subdir_count = "0"
	try: files_count = int(files_count) ; files_count = str(files_count)
	except: files_count = "0"
	
	
	
	
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''	
	if admin and not admin2 and admin3 or (folders_count == "0" and subdir_count == "0" and files_count == "0"):
		print printfirst + "bash_count_LV" + printpoint + space + "path_" + space2 + path_ + newline + \
		"folders_count" + space2 + folders_count + space + "subdir_count" + space2 + subdir_count + space + "files_count" + space2 + files_count + newline + \
		'list_count' + space2 + str(list_count)
		'''---------------------------'''
	
	'''---------------------------'''
	return folders_count, subdir_count, files_count
	
def Clean_Library(type):
	'''---------------------------'''
	manualL = ["9","10","11","12","13"]
	manualL2 = ["downloads", "music", "pictures", "videos", "movies", "tvshows"]
	'''---------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	name = 'Clean_Library' ; printpoint = "" ; dirs = "" ; dirsN = 0 ; emptydirs = "" ; path = "" ; emptydirsN = 0 ; files_count = 0 ; folders_count = 0 ; pathdir = "" ; TypeError = "" ; extra = ""
	'''---------------------------'''

	if type == "1": foldername = 'movies'
	elif type == "2": foldername = 'tvshows'
	elif type == "3": foldername = 'storage'
	elif type == "4": foldername = 'temp'
	elif type == "9": foldername = 'library'
	elif type == "10": foldername = 'downloads'
	elif type == "11": foldername = 'music'
	elif type == "12": foldername = 'pictures'
	elif type == "13": foldername = 'videos'
	else: foldername = ""
	'''---------------------------'''
	
	if foldername == "": path = ""
	elif type == "9": path = library_path #"/" + foldername + "/"
	elif type == "3" and (systemplatformlinux or systemplatformlinuxraspberrypi) and not systemplatformandroid: path = os.path.join(foldername, '')
	elif type == "4": path = temp_path
	elif type != "3": path = os.path.join(library_path, foldername, '')
	else: printpoint = printpoint + "9"
	'''---------------------------'''
	
	if path != "":
		printpoint = printpoint + "1"
		if not os.path.exists(path):
			printpoint = printpoint + "3"
			try: os.mkdir(path)
			except Exception, TypeError:
				extra = extra + newline + str(TypeError)
				notification("Critical Error!", "Verify your OS is supported!", "", 2000)
				
		elif os.listdir(path) == []: printpoint = printpoint + "4"
		else:
			printpoint = printpoint + "5"
			folders_count, folders_count2, files_count = bash_count(path)
			try:
				files_count = int(files_count)
				folders_count = int(folders_count)
				folders_count2 = int(folders_count2)
			except Exception, TypeError:
				files_count = 0
				folders_count = 0
				folders_count2 = 0
				extra = extra + newline + str(TypeError)
			subdirectories = os.listdir(path)
			for dir in subdirectories:
				#dirsN += 1
				try: pathdir = os.path.join(path, dir)
				except Exception, TypeError:
					try: pathdir = os.path.join(path, dir.encode('utf-8'))
					except: 
						pathdir_ = pathdir
						pathdir = ""
						extra = extra + newline + "TypeError" + space2 + str(TypeError) + space + "pathdir_" + space2 + str(pathdir_)
						
				if os.path.isdir(pathdir) == True:
					if dir[:1] != ".":
						if os.listdir(pathdir) == []:
							emptydirs = emptydirs + space + dir
							emptydirsN += 1
							removefiles(pathdir)
							#terminal('rmdir ' + "'" + pathdir + "'",pathdir)
							'''---------------------------'''
						else:
							pass
							'''---------------------------'''
					else:
						pass
						'''---------------------------'''
				else:
					pass
					'''---------------------------'''
	else: printpoint = printpoint + "9"
	
	if emptydirsN > 0:
		try: notification(str79542.encode('utf-8'),str79543.encode('utf-8') % (str(type), str(emptydirsN)),"",4000) #GAL CHECK THIS ERROR (ENGLISH)
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if "5" in printpoint and files_count > 0 and foldername != "" and type in manualL:
		'''------------------------------
		---MANUAL-PROMPT-----------------
		------------------------------'''
		pass
		returned = dialogyesno(localize(117) + space + localize(19076) + space + '[COLOR=Yellow]' + str(foldername) + '[/COLOR]', localize(79541) + '[CR]' + str(files_count) + space + localize(744))
		#returned = dialogyesno('[COLOR=Yellow]' + localize(117) + space + str(files_count) + localize(744) + space + localize(19107) + "-" + foldername, localize(79541))
		if returned == 'ok': removefiles(path+'*')
		else: notification_common("9")
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "Clean_Library_" + printpoint + space + "type" + space2 + type + space + "foldername" + space2 + foldername + space + "totalfiles" + space2 + str(files_count) + space + "addonID" + space2 + addonID + space + extra
	if admin:
		print '---------------------------'
		print printfirst + "path" + space2 + path
		print printfirst + "dirs" + space2 + "(" + str(dirsN) + ")" + space + "folders_count" + space2 + str(folders_count) + space + "folders_count" + space2 + str(folders_count) + space + dirs
		print printfirst + "pathdir" + space2 + str(pathdir.encode('utf-8')) + space
		print printfirst + "emptydirs" + space2 + "(" + str(emptydirsN) + ")" + space + emptydirs
		print '---------------------------'
		'''---------------------------'''

def CleanString(output, filter=[]):
	name = 'CleanString' ; output0 = str(output) ; output1 = "" ; output2 = "" ; output3 = ""
	
	if filter != []:
		
		for x in filter:
			output0 = output0.replace(x, "")
			output0 = output0.replace(x.upper(), "")
			
		
	output1 = output0.split('\n')
		
	
	for x in output1:
		x2 = x.replace('   ','#')
		x2 = x2.replace('  \n','#')
		x2 = x2.replace(' \n','#')
		x2 = x2.replace('\n','#')
		x2 = x2.replace('  \r','#')
		x2 = x2.replace(' \r','#')
		x2 = x2.replace('\r','#')
		x2 = x2.replace("'",'')
		x2 = x2.replace("[",'')
		x2 = x2.replace("]",'')
		#x2 = x2.replace(' \xd7','#')
		#x2 = x2.replace('\xd7','#')
		#x2 = x2.replace('\xa1','#')
		#x2 = x2.replace('\x94"','#')
		#x2 = x2.replace('\x94','#')
		#x2 = x2.replace('\x9b','#')
		'''---------------------------'''
		output2 = output2 + x2
		'''---------------------------'''
		
	output3 = output2.split('#') ; x2 = ""
	
	for x in output3:
		
		if x != "" and x != " " and not "    " in x:
			x2 = x2 + x
			'''---------------------------'''
			
	output4 = x2
	output1 = str(output1) ; output2 = str(output2) ; output3 = str(output3) ; output4 = str(output4)
	
	if admin and admin2 and admin3: print printfirst + name + newline + "output" + space2 + str(output) + newline + "output0" + space2 + str(output0) + newline + "output1" + space2 + str(output1) + newline + "output2" + space2 + str(output2) + newline + "output3" + space2 + str(output3) + newline + "output4" + space2 + str(output4)		
	'''---------------------------'''
	return output4
	


def checkDialog(admin):
	'''------------------------------
	---checkDialog-------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
	dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
	dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
	dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
	dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
	dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
	dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
	dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
	videofullscreenW = xbmc.getCondVisibility('Window.IsVisible(VideoFullScreen.xml)')
	'''---------------------------'''
	dialogHeader = ""
	dialogHeaderCustom = ""
	dialogMessage = ""
	dialogMessageCustom = ""
	'''---------------------------'''
	if dialogselectW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)') ### Skin.HasSetting(Admin) | !StringCompare(Control.GetLabel(1),Genesis)
		dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(100)') ###CUSTOM
		dialogMessage = ""
		dialogMessageCustom = ""
		returned_Dialog = "dialogselectW"
		'''---------------------------'''
	elif dialogyesnoW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)') ###
		dialogHeaderCustom = ""
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(9)') ###TEXTBOX
		if xbmc.getCondVisibility('!IsEmpty(Control.GetLabel(90))'): dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		else: dialogMessageCustom = ""
		returned_Dialog = "dialogyesnoW"
		'''---------------------------'''
	elif dialogkeyboardW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(311)')
		dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(317)')
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(312)') ###EDIT
		dialogMessageCustom = "" ###NONE
		returned_Dialog = "dialogkeyboardW"
		'''---------------------------'''
	elif dialogprogressW:
		dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)')
		dialogHeaderCustom = ""
		dialogMessage = xbmc.getInfoLabel('Control.GetLabel(9)') ###TEXTBOX
		if xbmc.getCondVisibility('Control.IsVisible(90)'): dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		else: dialogMessageCustom = ""
		returned_Dialog = "dialogprogressW"
		'''---------------------------'''
	elif dialogbusyW:
		if xbmc.getCondVisibility('Control.IsVisible(9)'): dialogHeader = xbmc.getInfoLabel('Control.GetLabel(9)') ###NONE
		elif xbmc.getCondVisibility('Control.IsVisible(100)'): dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(100)') ###CUSTOM
		elif xbmc.getCondVisibility('Control.IsVisible(101)'): dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(101)') ###CUSTOM
		dialogMessage = "" ###NONE
		if xbmc.getCondVisibility('!IsEmpty(Control.GetLabel(90))'): dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		returned_Dialog = "dialogbusyW"
		'''---------------------------'''
	elif dialogokW:
		if xbmc.getCondVisibility('Control.IsVisible(1)'): dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)') ### Skin.HasSetting(Admin) | StringCompare(Control.GetLabel(100),) | StringCompare(Control.GetLabel(1),$LOCALIZE[19240])
		elif xbmc.getCondVisibility('Control.IsVisible(100)'): dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(100)') ###CUSTOM
		if xbmc.getCondVisibility('Control.IsVisible(9)'): dialogMessage = xbmc.getInfoLabel('Control.GetLabel(9)') ###TEXTBOX
		elif xbmc.getCondVisibility('!Control.IsVisible(9)'): dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(90)') ###CUSTOM
		returned_Dialog = "dialogokW"
		'''---------------------------'''
	elif dialogsubtitlesW:
		dialogHeader = ""
		dialogHeaderCustom = ""
		dialogMessage = xbmc.getInfoLabel('Container(120).ListItem.Label2') ###FILE NAME
		dialogMessageCustom = xbmc.getInfoLabel('Container(120).ListItem.Label') ###FILE LANGUAGE
		returned_Dialog = "dialogsubtitlesW"
		'''---------------------------'''
	elif videofullscreenW:
		dialogHeader = ""
		dialogHeaderCustom = ""
		dialogMessage = ""
		dialogMessageCustom = ""
		returned_Dialog = "videofullscreenW"
		'''---------------------------'''
	else:
		'''------------------------------
		---NOTHING-SPECIFIC--------------
		------------------------------'''
		dialogHeader = ""
		dialogHeaderCustom = ""
		dialogMessage = ""
		dialogMessageCustom = ""
		returned_Dialog = ""
		'''---------------------------'''
	#elif dialogkaitoastW:
		#if xbmc.getCondVisibility('Control.IsVisible(401)'): dialogHeader = xbmc.getInfoLabel('Control.GetLabel(401)')
		#elif xbmc.getCondVisibility('!Control.IsVisible(401)'): dialogHeaderCustom = xbmc.getInfoLabel('Control.GetLabel(410)')
		#if xbmc.getCondVisibility('Control.IsVisible(402)'): dialogMessage = xbmc.getInfoLabel('Control.GetLabel(402)')
		#elif xbmc.getCondVisibility('Control.IsVisible(420)'): dialogMessageCustom = xbmc.getInfoLabel('Control.GetLabel(420)')
		#returned_Dialog = "dialogkaitoastW"
		#'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if returned_Dialog != "" and admin: print printfirst + "checkDialog" + space + "returned_Dialog" + space2 + "returned_Dialog" + space2 + returned_Dialog + space + "dialogHeader" + space2 + dialogHeader + space3 + "dialogHeaderCustom" + space2 + dialogHeaderCustom + space3 + "dialogMessage" + space2 + dialogMessage + space3 + "dialogMessageCustom" + space2 + dialogMessageCustom + space3
	'''---------------------------'''
	
	'''------------------------------
	---RETURN-END--------------------
	------------------------------'''
	returned_Header = dialogHeader
	returned_Message = dialogMessage
	if returned_Header == "Error occurred": returned_Header = "Sdarot.tv Video"
	'''---------------------------'''
	return returned_Dialog, returned_Header, returned_Message
	'''---------------------------'''
	
def dialogkeyboard(input, heading, option, custom, set1, addon):
	'''option:
    - xbmcgui.INPUT_ALPHANUM (standard keyboard)
    - xbmcgui.INPUT_NUMERIC (format: #)
    - xbmcgui.INPUT_DATE (format: DD/MM/YYYY)
    - xbmcgui.INPUT_TIME (format: HH:MM)
    - xbmcgui.INPUT_IPADDRESS (format: #.#.#.#)
    - xbmcgui.INPUT_PASSWORD (return md5 hash of input, input is masked)
	'''
	name = 'dialogkeyboard' ; printpoint = "" ; returned = 'skip' ; set1v = ""
	if '$LOCALIZE' in heading: heading = xbmc.getInfoLabel(heading)
	try: heading = heading.encode('utf-8')
	except: pass
	dialog = xbmcgui.Dialog()
	keyboard = xbmc.Keyboard(input,heading,option)
	keyboard.doModal()
	
	'''---------------------------'''
	if (keyboard.isConfirmed()):
		printpoint = printpoint + "0"
		set1v = keyboard.getText()
		if custom == '1':
			'''not empty'''
			printpoint = printpoint + "1"
			if set1v != "": returned = 'ok'
			else: notification_common("3")
		elif custom == '2' and set1v == input:
			printpoint = printpoint + "2"
			returned = 'ok'
		elif custom == '3':
			printpoint = printpoint + "3"
			if set1v != input and set1v != "" and option == 0: xbmc.executebuiltin('Notification('+ heading +': '+ set1v +',,4000)')
			if set1v != "": returned = 'ok'
			'''---------------------------'''
		elif custom == '5':
			'''Custom Playlist'''
			printpoint = printpoint + "5"
			if ("&list=PL" in set1v or "watch?v=" in set1v or "/user/" in set1v or "/channel/" in set1v):
				from shared_modules3 import urlcheck
				check = urlcheck(set1v, ping=False)
				if check == "ok":
					xbmc.executebuiltin('Notification('+ heading +': '+ set1v +',,4000)')
					returned = 'ok'
					'''---------------------------'''
				else: notification("URL is not valid!", "Try again..", "", 2000)
			elif set1v == "":
				check = dialogyesno(addonString_servicehtpt(60).encode('utf-8'), localize(19194)) #Your input is empty!, Continue?
				if check == "ok":
					returned = "ok"
					set1v = "None"
			else: notification("URL is not valid!", "Try again..", "", 2000)
			
		elif custom == "":
			printpoint = printpoint + "_"
			returned = 'ok'
		
	if returned == 'ok':
		returned = set1v
		if set1 != "" and addon != "":
			if addon == "0": setsetting(set1, set1v)
			elif addon != "": setsetting_custom1(addon,set1,set1v)
			'''---------------------------'''
		elif set1 != "" and addon == "": setSkinSetting("0",set1,set1v)
	
	if option != 0: set1v = "******"
	print printfirst + name + "_LV" + printpoint + space + "returned" + space2 + str(returned) + space + "heading" + space2 + str(heading) + space + "set1v" + space2 + str(set1v)
	'''---------------------------'''
	return returned

def dialognumeric(type,heading,input,custom,set1,addon):
	'''type: 0 = #, 1 = DD/MM/YYYY, 2 = HH:MM, 3 = #.#.#.#, message2 = heading, message1 = content'''
	name = 'dialognumeric' ; printpoint = "" ; returned = "skip" ; TypeError = ""
	if '$LOCALIZE' in heading: heading = xbmc.getInfoLabel(heading)
	try: heading = heading.encode('utf-8')
	except: pass
	
	if custom == 0:
		try:
			if int(input) > 001000000 and int(input) < 9999999999 and input != "": pass
			else: input = 0
			'''---------------------------'''
		except Exception, TypeError: input = 0 ; printpoint = printpoint + "8"

	set1v = xbmcgui.Dialog().numeric(type, heading, str(input))
	
	if set1v == "":
		notification_common("3")
		sys.exit()
		'''---------------------------'''
		
	if custom == '0':
		try:
			if int(set1v) > 001000000 and int(set1v) < 9999999999: returned = 'ok'
			elif int(set1v) < 001000000 or int(set1v) > 9999999999: returned = 'skip0'
			'''---------------------------'''
		except Exception, TypeError:
			returned = 'skip'
			printpoint = printpoint + "6"
			'''---------------------------'''
			
	if custom == '1':
		if set1v != "": returned = 'ok'
		'''---------------------------'''
	if custom == '2':
		if set1v == "": set1v = 0
		elif set1v != 0: returned = 'ok'
		'''---------------------------'''
	
	if returned == 'ok':
		if set1 != "" and addon != "":
			if addonID == addon: setsetting(set1, set1v) ; printpoint = printpoint + "A"
			else: setsetting_custom1(addon,set1,set1v) ; printpoint = printpoint + "B"
			'''---------------------------'''
		elif set1 != "" and addon == "":
			setSkinSetting("0", set1, set1v)
			printpoint = printpoint + "C"
			'''---------------------------'''
		else: printpoint = printpoint + "9"
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + "_LV" + printpoint + space + "heading" + space2 + str(heading) + space + "input" + space2 + str(input) + space5 + str(set1v) + space +  "( " + returned + " )"	
	'''---------------------------'''
	
	'''---------------------------'''
	return returned, set1v

def dialogok(heading,line1,line2,line3, line1c="", line2c="", line3c="", line4c=""):
	'''------------------------------
	---DIALOG-OK---------------------
	------------------------------'''
	dialog = xbmcgui.Dialog() ; TypeError = "" ; extra = ""
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	if '$LOCALIZE' in line2 or '$ADDON' in line2: line2 = xbmc.getInfoLabel(line2)
	if '$LOCALIZE' in line3 or '$ADDON' in line3: line3 = xbmc.getInfoLabel(line3)
	try: heading = str(heading.encode('utf-8'))
	except: heading = str(heading)
	try: line1 = str(line1.encode('utf-8'))
	except: line1= str(line1)
	try: line2 = str(line2.encode('utf-8'))
	except: line2 = str(line2)
	try: line3 = str(line3.encode('utf-8'))
	except: line3 = str(line3)
	
	if line1c != "":
		try: line1 = '[COLOR='+ line1c + ']' + line1 + '[/COLOR]'
		except Exception, TypeError: pass
	if line2c != "":
		try: line1 = '[COLOR='+ line2c + ']' + line1 + '[/COLOR]'
		except Exception, TypeError: pass
	if line3c != "":
		try: line1 = '[COLOR='+ line3c + ']' + line1 + '[/COLOR]'
		except Exception, TypeError: pass
	if line4c != "":
		try: line1 = '[COLOR='+ line4c + ']' + line1 + '[/COLOR]'
		except Exception, TypeError: pass
		
	dialog.ok(heading,line1,line2,line3)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if TypeError != "": extra = newline + "TypeError" + space2 + str(TypeError)
	print printfirst + heading + space2 + line1 + space2 + line2 + space2 + line3 + extra
	'''---------------------------'''
	
def dialogselect(heading, list, autoclose):
	'''------------------------------
	---DIALOG-SELECT-----------------
	------------------------------'''
	'''autoclose = [opt] integer - milliseconds to autoclose dialog. (default=do not autoclose)'''
	printpoint = "" ; TypeError = "" ; extra = ""
	dialog = xbmcgui.Dialog()
	if '$LOCALIZE' in heading or '$ADDON' in heading:
		printpoint = printpoint + "1"
		heading = xbmc.getInfoLabel(heading)
	#heading = str(heading).decode('utf-8').encode('utf-8')
	try: heading = heading.encode('utf-8')
	except Exception, TypeError: printpoint = printpoint + "2" ; extra = extra + newline + "TypeError_LV" + printpoint + space2 + str(TypeError)
	try: heading = str(heading)
	except Exception, TypeError: printpoint = printpoint + "3" ; extra = extra + newline + "TypeError_LV" + printpoint + space2 + str(TypeError)
			
	returned = dialog.select(heading,list,autoclose)
	returned = int(returned)
	
	
	
	#value = value.replace(" ","",1)
	#value = value.decode('utf-8').encode('utf-8')
	#value = str(value).decode('utf-8')
	#value = str(value).decode('utf-8').encode('utf-8')
	#value = value.decode('utf-8').encode('utf-8')
	if returned == -1:
		notification_common("9")
		value = ""
	else:
		value = list[returned]
		try: value = value.encode('utf-8')
		except Exception, TypeError: printpoint = printpoint + "5" ; extra = extra + newline + "TypeError_LV" + printpoint + space2 + str(TypeError)
		try: value = str(value)
		except Exception, TypeError: printpoint = printpoint + "6" ; extra = extra + newline + "TypeError_LV" + printpoint + space2 + str(TypeError)

	if admin and not admin2 and admin3 or extra != "":
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "dialogselect_LV" + printpoint + space2 + heading + "( " + str(returned) + " )" + space + "value" + space2 + value + extra
		'''---------------------------'''
	return returned, value
	'''---------------------------'''

def diaogtextviewer(header,message):
	if '$LOCALIZE' in header or '$ADDON' in header: header = xbmc.getInfoLabel(header)
	if '$LOCALIZE' in message or '$ADDON' in message: message = xbmc.getInfoLabel(message)
	
	try: header = str(header.encode('utf-8'))
	except: pass
	try: message = str(message.encode('utf-8'))
	except: pass
	
	w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message)
	w.doModal()
	
def dialogyesno(heading,line1,yes=False, nolabel="", yeslabel="", autoclose=0):
	'''------------------------------
	---DIALOG-YESNO------------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	returned = 'skip'
	
	if yes != False: xbmc.executebuiltin('AlarmClock(yes,Action(Down),0,silent)')
	if dialog.yesno(heading,line1, nolabel=nolabel, yeslabel=yeslabel, autoclose=autoclose): returned = 'ok'
	
	try: heading = str(heading.encode('utf-8'))
	except: pass
	try: line1 = str(line1.encode('utf-8'))
	except: pass
	
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "dialogyesno" + space2 + heading + space3 + line1 + "( " + returned + " )"
	'''---------------------------'''
	return returned
	'''---------------------------'''

def findin_controlhasfocus(custom,what,sleep,action,action2):
	'''action = not found | action2 = when found'''
	'''---------------------------'''
	what = str(what)
	custom = str(custom)
	if custom == "0": controlhasfocus = xbmc.getCondVisibility('Control.HasFocus('+ what +')')
	else: controlhasfocus = xbmc.getCondVisibility('ControlGroup('+ custom +').HasFocus('+ what +')')
	
	if (what != "" and not controlhasfocus and action != ""): xbmc.executebuiltin(''+ action +'')
	'''---------------------------'''
	xbmc.sleep(sleep)
	if custom == "0": controlhasfocus = xbmc.getCondVisibility('Control.HasFocus('+ what +')')
	else: controlhasfocus = xbmc.getCondVisibility('ControlGroup('+ custom +').HasFocus('+ what +')')
	#systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	xbmc.sleep(sleep)
	'''---------------------------'''
	if (what != "" and controlhasfocus and action2 != ""): xbmc.executebuiltin(''+ action2 +'')
	'''---------------------------'''
	return controlhasfocus
	
def findin_systemcurrentcontrol(custom,what,sleep,action,action2):
	'''action = not found | action2 = when found'''
	'''---------------------------'''
	if '$LOCALIZE' in what or '$ADDON' in what: what = xbmc.getInfoLabel(what)
	try: what = what.encode('utf-8')
	except: pass
	
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	if custom == "0" and (what != "" and systemcurrentcontrol != what and action != ""): xbmc.executebuiltin(''+ action +'')
	elif custom == "1" and (what != "" and not what in systemcurrentcontrol and action != ""): xbmc.executebuiltin(''+ action +'')
	elif custom == "2" and (what != "" and systemcurrentcontrol not in what and action != ""): xbmc.executebuiltin(''+ action +'')
	'''---------------------------'''
	xbmc.sleep(sleep)
	systemcurrentcontrol2 = xbmc.getInfoLabel('System.CurrentControl')
	xbmc.sleep(sleep)
	'''---------------------------'''
	if custom == "0" and (what != "" and systemcurrentcontrol2 == what and action2 != ""): xbmc.executebuiltin(''+ action2 +'')
	elif custom == "1" and (what != "" and what in systemcurrentcontrol2 and action2 != ""): xbmc.executebuiltin(''+ action2 +'')
	elif custom == "2" and (what != "" and systemcurrentcontrol2 in what and action2 != ""): xbmc.executebuiltin(''+ action2 +'')
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and not admin2 and admin3: print printfirst + "findin_systemcurrentcontrol" + space + "custom" + space2 + custom + space + "what" + space2 + str(what) + space + "systemcurrentcontrol/2" + space2 + str(systemcurrentcontrol) + space5 + str(systemcurrentcontrol2)
	'''---------------------------'''
	return systemcurrentcontrol2
	
def get_types(value):
	import types
	returned = str(type(value))
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "get_types" + space + "value" + space2 + str(value) + space + "type" + space2 + returned
	'''---------------------------'''
	
	return returned
	'''---------------------------'''
	
def get_daynow(custom):
	daynow = datenow.strftime("%a")
	daynowS = str(daynow)
	return daynowS
	'''---------------------------'''
	
def refresh_datetime(admin, datenowS_, timenowS_):
	import datetime as dt
	import time
	
	name = 'refresh_datetime'
	
	datenow = dt.date.today()
	datenowS = str(datenow)
	'''---------------------------'''
	dateafter = datenow + dt.timedelta(days=7)
	dateafterS = str(dateafter)
	'''---------------------------'''
	yearnow = datenow.strftime("%Y")
	yearnowS = str(yearnow)
	'''---------------------------'''
	daynow = datenow.strftime("%a")
	daynowS = str(daynow)
	timenow = dt.datetime.now()
	timenowS = str(timenow)
	timenow2 = timenow.strftime("%H:%M")
	timenow2S = str(timenow2)
	timenow2N = int(timenow2S.replace(":","",1)) #GAL CHECK # PAREMTERS WHY?
	timenow3 = timenow.strftime("%H")
	timenow3S = str(timenow3)
	timenow3N = int(timenow3S)
	timenow4 = timenow.strftime("%S")
	timenow4S = str(timenow4)
	'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + name + space + "datenowS/2" + space2 + datenowS_ + space4 + datenowS + space + "timenowS" + space2 + timenowS_ + space4 + timenowS
	'''---------------------------'''
	return datenow, datenowS, dateafter, dateafterS, yearnow, yearnowS, daynow, daynowS, timenowS, timeow2S, timenow3S, timenow4S

def getRandom(custom, min=0, max=100, percent=50):
	'''------------------------------
	---RANDOM------------------------
	------------------------------'''
	import random
	value = ""
	returned = ""
	printpoint = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	try:
		min = int(min)
		max = int(max)
		percent = int(percent)
	except Exception, TypeError: printpoint = printpoint + "9"
	'''---------------------------
	random.random()
	This prints a random floating point number in the range [0, 1) (that is, between 0 and 1, including 0.0 but always smaller than 1.0).
	randrange(a, b) chooses an integer in the range [a, b).
	uniform(a, b) chooses a floating point number in the range [a, b).
	normalvariate(mean, sdev) samples the normal (Gaussian) distribution.
	------------------------------'''
	
	if not "9" in printpoint:
		'''---------------------------'''
		if custom == "0": value = random.randrange(min,max)
		'''---------------------------'''
		if value <= percent: returned = "ok"
		else: returned = "skip"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print "getRandom_LV" + printpoint + space + "min" + space2 + str(min) + space + "max" + space2 + str(max) + space + "percent" + space2 + str(percent) + newline + "returned" + space2 + str(returned) + space + "value" + space2 + str(value)
	if "9" in printpoint: print "getRandom_LV" + printpoint + space + "TypeError" + space2 + str(TypeError) 
	'''---------------------------'''
	
	return returned, value
				
def get_timenow(custom):
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	import datetime as dt
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	customS = str(custom)
	timenow = dt.datetime.now()
	timenow3 = timenow.strftime("%H")
	timenow3S = str(timenow3)
	timenow3N = int(timenow3)
	timezone = ""
	'''---------------------------'''
	if timenow3N > 03 and timenow3N < 12: timezone = "A"
	elif timenow3N > 11 and timenow3N < 20: timezone = "B"
	elif timenow3N > 19 or timenow3N < 04: timezone = "C"
	
	if custom == 1: returned = timezone
	else: returned = ""
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "get_timenow_" + customS + space + "timenow3S" + space2 + timenow3S + space + "timezone" + space2 + timezone + space
	'''---------------------------'''
	return returned

def installaddon(admin, addonid2, name, update=True):
	returned = "" ; printpoint = ""
	
	if not xbmc.getCondVisibility('System.HasAddon('+ addonid2 +')') or not os.path.exists(addons_path + addonid2):
		printpoint = printpoint + "1"
		setSkinSetting("1",'ShowDialog',"true")
		if update == True: notification_common("24")
		#xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addonid2 +'),returned')
		#xbmc.executebuiltin('Action(Down)')
		#xbmc.executebuiltin('Action(Select)')
		
		if 1 + 1 == 2:
			#dp = xbmcgui.DialogProgress()
			#dp.create("HTPT Looking for addon", "Starting..", " ")
			#dp.update(0, addonid2, " ")
			if update != True: xbmc.executebuiltin('ActivateWindow(10025,special://userdata/library/,return)') ; xbmc.sleep(2000) #; dp.update(10, addonid2, " ") ; xbmc.sleep(1000) ; dp.update(20, addonid2, " ")
			xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addonid2 +'),returned') #; dp.update(40, addonid2, " ")
			if update != True:
				xbmc.executebuiltin('Action(Down)')
				xbmc.executebuiltin('Action(Select)')
			#dp.update(50, addonid2, " ")
			#xbmc.sleep(1000) #; dp.update(60, addonid2, " ")
			#dp.update(100, addonid2, " ")
			#dp.close
			dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
			if not dialogyesnoW:
				xbmc.executebuiltin('Action(Close)') ; xbmc.sleep(500) ; xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addonid2 +'),returned')
		#xbmc.sleep(1000)
		setSkinSetting("1",'ShowDialog',"false")
		if xbmc.getCondVisibility('System.HasAddon('+ addonid2 +')') and os.path.exists(addons_path + addonid2):
			printpoint = printpoint + "7" ; returned = "ok"
		elif os.path.exists(addons_path + addonid2) and update == True:
			xbmc.executebuiltin("UpdateLocalAddons")
			if 'repo' in addonid2: xbmc.executebuiltin("UpdateAddonRepos")
			returned = "error?"
		else: printpoint = printpoint + "9" ; returned = "error"
		#elif dp.iscanceled(): printpoint = printpoint + "8" ; returned = "skip"
		homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
		if not homeW and not startupW: xbmc.executebuiltin('ActivateWindow(0)') ; xbmc.sleep(1000)
	if admin and not admin2 and admin3: print printfirst + "installaddon_LV" + printpoint + space + str(addonid2) + space + "(" + returned + ")"
	'''---------------------------'''
	return returned

def installaddonP(admin, addon, update=True):
	printpoint = "" ; name = 'installaddonP'
	if addon == 'metadata.universal':
		
		file = "metadata.common.imdb.com"
		if not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
		
		if 1 + 1 == 3:
			file = "metadata.tvdb.com"
			if not os.path.exists(addons_path + file) and not "9" in printpoint:
				fileID = getfileID(file+".zip")
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
				if os.path.exists(addons_path + file): printpoint = printpoint + "5"
				else: printpoint = printpoint + "9"
			elif "9" in printpoint: pass
			else: printpoint = printpoint + "7"
		
		file = "metadata.common.impa.com"
		if not xbmc.getCondVisibility('System.HasAddon('+ file +')') or not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
		
		file = "metadata.common.movieposterdb.com"
		if not xbmc.getCondVisibility('System.HasAddon('+ file +')') or not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
		
		file = "metadata.common.port.hu"
		if not xbmc.getCondVisibility('System.HasAddon('+ file +')') or not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		else: printpoint = printpoint + "7"
		
		file = "metadata.common.rt.com"
		if not xbmc.getCondVisibility('System.HasAddon('+ file +')') or not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
		
		file = "metadata.common.trakt.tv"
		if not xbmc.getCondVisibility('System.HasAddon('+ file +')') or not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
		
		file = "metadata.universal"
		if not xbmc.getCondVisibility('System.HasAddon('+ file +')') or not os.path.exists(addons_path + file) and not "9" in printpoint:
			fileID = getfileID(file+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+".zip?dl=1", file + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + file): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
		
		if 3 + 3 == 2:
			printpoint = printpoint + installaddon2(admin, 'metadata.common.impa.com', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.common.imdb.com', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.common.movieposterdb.com', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.common.ofdb.de', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.common.port.hu', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.common.rt.com', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.common.trakt.tv', update=False)
			if not "8" in printpoint and not "9" in printpoint: printpoint = printpoint + installaddon2(admin, 'metadata.universal', update=True)
	
	elif addon == 'script.openelec.rpi.config':
		
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+addon+".zip?dl=1", addon + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'plugin.program.advanced.launcher':
		
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+addon+".zip?dl=1", addon + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'repository.lambda':
		
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+addon+".zip?dl=1", addon + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'script.skin.helper.service': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://github.com/marcelveldt/script.skin.helper.service/archive/master.zip", addon + "-master.zip", packages_path, addons_path, silent=True)
			movefiles(os.path.join(addons_path, 'script.skin.helper.service-master'), os.path.join(addons_path, addon))
			if os.path.exists(addons_path + addon + "-master") or os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'script.skinshortcuts': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://github.com/BigNoid/script.skinshortcuts/archive/master.zip", addon + "-master.zip", packages_path, addons_path, silent=True)
			movefiles(os.path.join(addons_path, 'script.skinshortcuts-master'), os.path.join(addons_path, addon))
			if os.path.exists(addons_path + addon + "-master") or os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'script.module.unidecode':
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+addon+".zip?dl=1", addon + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'plugin.video.dailymotion_com':
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			fileID = getfileID(addon+".zip")
			DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+addon+".zip?dl=1", addon + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'script.module.requests': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			DownloadFile("https://github.com/beenje/script.module.requests/archive/gotham.zip", addon + ".zip", packages_path, addons_path, silent=True)
			#os.rename(os.path.join(addons_path, 'script.module.requests-gotham'), 'script.module.requests')
			movefiles(os.path.join(addons_path, 'script.module.requests-gotham'), os.path.join(addons_path, addon))
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'repository.natko1412': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon(repo.natko1412)') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			DownloadFile("https://offshoregit.com/natko1412/zips/repo.natko1412/repo.natko1412-2.0.0.zip", addon + ".zip", packages_path, addons_path, silent=True)
			#movefiles(os.path.join(addons_path, 'repository.natko1412'), os.path.join(addons_path, addon))
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'plugin.video.bbts': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			DownloadFile("https://raw.githubusercontent.com/kodil/kodil/master/repo/plugin.video.bbts/plugin.video.bbts-0.1.4.zip", addon + ".zip", packages_path, addons_path, silent=True)
			movefiles(os.path.join(addons_path, 'repository.natko1412'), os.path.join(addons_path, addon))
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'plugin.video.pulsar': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			DownloadFile("https://github.com/steeve/plugin.video.pulsar/releases/download/v0.6.1/plugin.video.pulsar-0.6.1.zip", addon + ".zip", packages_path, addons_path, silent=True)
			if os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
	
	elif addon == 'program.plexus': #FIXED PATH
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon) and not "9" in printpoint:
			DownloadFile("https://github.com/enen92/program.plexus/archive/master.zip", addon + ".zip", packages_path, addons_path, silent=True)
			movefiles(os.path.join(addons_path, 'program.plexus-master'), os.path.join(addons_path, addon))
			if os.path.exists(addons_path + addon + "-master") or os.path.exists(addons_path + addon): printpoint = printpoint + "5"
			else: printpoint = printpoint + "9"
		elif "9" in printpoint: pass
		else: printpoint = printpoint + "7"
		
	if "5" in printpoint:
		if update == True:
			xbmc.executebuiltin("UpdateLocalAddons")
			xbmc.sleep(1000)
		if "repository" in addon: xbmc.executebuiltin("UpdateAddonRepos")
		'''---------------------------'''
		
	print printfirst + name + "_LV" + printpoint
	return printpoint
	
def installaddon2(admin, addon, version="0.0.0", update=True, silent=True):
	returned = "" ; printpoint = "" ; printpoint2 = "" ; name = 'installaddon2'
	
	'''---------------------------'''
	if addon == 'repository.htpt': version = "1.1.0"
	elif addon == 'service.htpt': version = "0.1.72"
	elif addon == 'service.htpt.debug': version = "0.1.41"
	elif addon == 'service.htpt.fix': version = "0.1.60"
	elif addon == 'script.htpt.install': version = "0.0.27"
	elif addon == 'script.htpt.smartbuttons': version = "0.0.32"
	elif addon == 'script.htpt.remote': version = "0.1.12"
	elif addon == 'script.htpt.refresh': version = "0.1.32"
	elif addon == 'script.htpt.widgets': version = "0.1.3"
	elif addon == 'skin.htpt': version = "0.1.41"
	
	elif addon == 'metadata.common.impa.com': version = "1.1.3"
	elif addon == 'metadata.common.movieposterdb.com': version = "1.1.2"
	elif addon == 'metadata.common.ofdb.de': version = "1.0.4"
	elif addon == 'metadata.common.port.hu': version = "1.1.4"
	elif addon == 'metadata.common.rt.com': version = "1.5.0"
	elif addon == 'metadata.common.trakt.tv': version = "1.1.3"
	elif addon == 'metadata.universal': version = "2.6.3"
	
	elif addon == 'metadata.common.imdb.com': version = "2.7.6"
	elif addon == 'repository.xbmcadult': version = "1.0.6"
	elif addon == 'repository.xbmc-israel': version = "1.0.4"
	elif addon == 'program.plexus': version = "0.1.4"
	'''---------------------------'''
	
	'''---------------------------'''
	if addon == "": printpont = printpoint + "0"
	elif not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(addons_path + addon):
		if os.path.exists(addons_path + addon): removeaddons(addon, "123")
		if addon == 'repository.xbmcadult': url, printpoint2 = findVersion(gh1+gh3+addon+'/'+addon+'-', Ver=version)
		elif addon == 'repository.xbmc-israel': url, printpoint2 = findVersion(gh1+gh4+addon+'/'+addon+'-', Ver=version)
		elif addon == 'program.plexus': url, printpoint2 = findVersion(gh10+gh11+addon+'/'+addon+'-', Ver=version)
		else: url, printpoint2 = findVersion(gh1+gh2+addon+'/'+addon+'-', Ver=version)
		'''---------------------------'''
		if url != "" and "7" in printpoint2:
			DownloadFile(url, addon+".zip", packages_path, addons_path, silent=silent)
			if os.path.exists(addons_path + addon):
				printpoint = printpoint + "5"
			else: printpoint = printpoint + "9" ; notification_common("9")
			'''---------------------------'''
		elif not "8" in printpoint2: printpoint = printpoint + "9" #Error
		else: printpoint = printpoint + "8" #Abort
		
	else: printpoint = printpoint + "7"
	
	if not "7" in printpoint and not "0" in printpoint:
		if update == True:
			xbmc.executebuiltin("UpdateLocalAddons")
			xbmc.sleep(1000)
		if "repository" in addon: xbmc.executebuiltin("UpdateAddonRepos")
		'''---------------------------'''
	
	
	if "8" in printpoint2: dialogok(localize(16200), '$LOCALIZE[114]!', "", "") #Operation was aborted, Installation failed
	elif "9" in printpoint2: dialogok(localize(257) + space + "1070", '$LOCALIZE[114]!', "", addonString(80)) #Error 1070, Installation failed
	
	if admin or (addonID == 'script.htpt.install' or addonID == 'service.htpt.fix'): print printfirst + name + "_LV" + printpoint + "(_LV" + printpoint2 + ")" + space + "addon" + space2 + str(addon)
	'''---------------------------'''
	return printpoint
	
def findVersion(url, Ver='0.1.x', silent=False):
	from shared_modules3 import urlcheck
	name = 'findVersion'
	printpoint = ""
	Version = Ver.split('.')
	Version1 = Version[0]
	Version2 = Version[1]
	try: Version3 = Version[2]
	except: Version3 = ""
	x_nums = Version.count('x') ; x_nums = int(x_nums) ; num = 1 ; num3 = 40
	if 'x' in Version1: num += 10
	if 'x' in Version2: num += 10
	
	setSkinSetting("1",'ShowDialog',"true")
	dp = xbmcgui.DialogProgress()
	dp.create("HTPT Version Find", "Starting..", " ")
	dp.update(0,"Starting..."," ")
	count = 0 ; count1 = 0 ; count2 = 0 ; count3 = 0 ; countout = 0 ; returned = ""
	while count < num and returned != 'ok' and not dp.iscanceled() and not xbmc.abortRequested:
		
		if Version1 == 'x' or count1 > 0:
			if Version1 == 'x': Version1 = Version1.replace('x','0')
			elif count1 > 0:
				Version1 = int(Version1)
				Version1 += 1
				'''---------------------------'''
			count1 += 1
		
		if Version2 == 'x' or count2 > 0:
			if Version2 == 'x': Version2 = Version2.replace('x','0')
			elif count2 > 0:
				Version2 = int(Version2)
				Version2 += 1
				'''---------------------------'''
			count2 += 1
				
		if Version3 == 'x': Version3 = Version3.replace('x','0')
		while countout < 10 and count3 < num3 and returned != 'ok' and not dp.iscanceled() and not xbmc.abortRequested:
			try: returned = urlcheck(url+str(Version1)+"."+str(Version2)+"."+str(Version3)+".zip")
			except Exception, TypeError:
				if "The read operation timed out" in TypeError: returned = 'timeout'
				else: returned = 'error'
				print printfirst + name + "_LV" + printpoint + space + "TypeError" + space2 + str(TypeError)
			if returned != 'ok':
				Version3 = int(Version3)
				if returned != "timeout": Version3 += 1 ; countout = 0
				else: countout += 1
				xbmc.sleep(40)
				'''---------------------------'''
			else:
				dp.update(100,"FOUND!!!:" + space + str(Version1)+"."+str(Version2)+"."+str(Version3)," ")
				xbmc.sleep(1000)
				dp.close
				'''---------------------------'''
			progress = (((1+count)*(1+count3))*100/(num*num3))
			
			try:
				#progress = str(progress)
				#progress = float(progress)
				#progress = round(progress)
				#progress = str(progress)
				if ".0" in progress: progress = progress.replace(".0","",1)
				progress = int(progress)
			except: pass
			
			if count == 0 and count3 == 0: pass
			elif count == 0: dp.update(progress,"Looking for Version:" + space + str(Version1)+"."+str(Version2)+"."+str(Version3)," ")
			count3 += 1
			'''---------------------------'''
		if count3 >= num3: Version3 = 'x' ; count3 = 0
		
		
		count += 1
		
		
	
	setSkinSetting("1",'ShowDialog',"false")
	
	if returned == 'ok':
		url2 = url+str(Version1)+"."+str(Version2)+"."+str(Version3)+".zip"
		printpoint = printpoint + "7"
	else:
		url2 = ""
		if dp.iscanceled():
			dp.close
			printpoint = printpoint + "8"
		else: printpoint = printpoint + "9"
		
	print printfirst + name + "_LV" + printpoint + space + "["+str(count)+"]" + space + "Version" + space2 + str(Version) + space + "Version1/2/3" + space2 + str(Version1) + space4 + str(Version2) + space4 + str(Version3) + space + "returned" + space2 + str(returned) + space + "url2" + space2 + str(url2)
	
	'''---------------------------'''
	return url2, printpoint
	
def oewindow(name):
	'''------------------------------
	---OpenELEC-Window---------------
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	xbmc.executebuiltin('RunScript(service.openelec.settings)')
	xbmc.sleep(500)
	mainwindowW = xbmc.getCondVisibility('Window.IsVisible(mainwindow.xml)')
	count = 0
	countbusy = 0
	while count < 20 and not mainwindowW and not xbmc.abortRequested:
		xbmc.sleep(100)
		count += 1
		mainwindowW = xbmc.getCondVisibility('Window.IsVisible(mainwindow.xml)')
		xbmc.sleep(100)
		'''---------------------------'''
	if count < 20:
		
		while mainwindowW and not xbmc.abortRequested:
			xbmc.sleep(100)
			mainwindowW = xbmc.getCondVisibility('Window.IsVisible(mainwindow.xml)')
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
			count = 0
			while count < 5 and not dialogbusyW and not xbmc.abortRequested:
				count += 1
				xbmc.sleep(40)
				dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
				if count == 5:
					mainwindowW = xbmc.getCondVisibility('Window.IsVisible(mainwindow.xml)')
					if name == "Bluetooth":
						list1 = [openelec1, openelec2, openelec6] #UP
						list2 = [openelec3, openelec4] #DOWN
						systemcurrentcontrol = findin_systemcurrentcontrol("2",list1,40,'','Action(Up)')
						systemcurrentcontrol = findin_systemcurrentcontrol("2",list2,40,'','Action(Down)')
						systemcurrentcontrol = findin_systemcurrentcontrol("0",openelec5,100,'','Action(Right)')
						'''---------------------------'''
					elif name == "Network":
						systemcurrentcontrol = findin_systemcurrentcontrol("0",openelec1,100,'','Action(Down)')
						systemcurrentcontrol = findin_systemcurrentcontrol("0",openelec4,100,'','Action(Up)')
						systemcurrentcontrol = findin_systemcurrentcontrol("0",openelec5,100,'','Action(Up)')
						systemcurrentcontrol = findin_systemcurrentcontrol("0",openelec6,100,'','Action(Down)')
						'''---------------------------'''
					if countbusy > 0: countbusy += -1
			if dialogbusyW: countbusy += 1
			xbmc.sleep(100)
			systemidle40 = xbmc.getCondVisibility('System.IdleTime(40)')
			if systemidle40 or countbusy >= 15:
				xbmc.executebuiltin('Action(Close)')
				notification("Trying to close...", "", "", 4000)
				xbmc.sleep(5000)
				mainwindowW = xbmc.getCondVisibility('Window.IsVisible(mainwindow.xml)')
				dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
				if mainwindowW and dialogbusyW: xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=50)') #NEW GAL CHECK!
				'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "oewindow" + space + name + space2 + "countbusy" + space2 + str(countbusy)
	'''---------------------------'''
	
def notification(heading, message, icon, time):
	'''------------------------------
	---Show a Notification alert.----
	------------------------------'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	'''heading : string - dialog heading | message : string - dialog message. | icon : [opt] string - icon to use. (default xbmcgui.NOTIFICATION_INFO/NOTIFICATION_WARNING/NOTIFICATION_ERROR) | time : [opt] integer - time in milliseconds (default 5000) | sound : [opt] bool - play notification sound (default True)'''
	
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in message or '$ADDON' in message: message = xbmc.getInfoLabel(message)
	
	icon = ""
	
	dialog.notification(heading, message, icon, time)
	
	#if "addonString" in heading and not "+" in heading: heading = str(heading.encode('utf-8'))
	if "addonString" in heading:
		try: heading = str(heading.encode('utf-8'))
		except: heading = str(heading)
	elif '$LOCALIZE' in heading or '$ADDON' in heading: heading = str(heading)
	if "addonString" in message:
		try: message = str(message.encode('utf-8'))
		except: message = str(message)
	elif '$LOCALIZE' in message or '$ADDON' in message: message = str(message)
	
	time = str(time)
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin:
		try: print printfirst + "notification" + space2 + heading + space3 + message + space + time
		except: print printfirst + "notification" + "..."
		'''---------------------------'''
		
def removeaddons(addons, custom):
	Afolders_count = 0 ; Afiles_count = 0 ; Bfolders_count = 0 ; Bfiles_count = 0 ; Cfolders_count = 0 ; Cfiles_count = 0 ; printpoint = ""
	forceL = ['plugin.video.p2p-streams', 'program.plexus', 'script.htpt.smartbuttons', 'script.htpt.emu', 'skin.htpt']
	output = ""
	output2 = ""
	i = 0
	returned = get_types(addons)
	
	if custom == "": printpoint = printpoint + '9'
	else:
		if not "list" in returned: addons = [addons] #addons.append(addons)
		
		for addon in addons:
			i += 1
			path = "" ; path2 = "" ; path3 = ""
			if "1" in custom:
				for file in os.listdir(addons_path):
					if addon in file:
						path = os.path.join(addons_path, file)
						Afiles_count += 1
						break
						'''---------------------------'''
						
			if "2" in custom:
				for file in os.listdir(addondata_path):
					if addon in file:
						path2 = os.path.join(addondata_path, file)
						Bfiles_count += 1
						break
						'''---------------------------'''
						
			if "3" in custom:					
				for file in os.listdir(packages_path):
					if addon in file and file.endswith(".zip"):
						path3 = os.path.join(packages_path, file)
						Cfiles_count += 1
						break
						'''---------------------------'''
			
			if path != addons_path and path != addondata_path and path2 != addons_path and path2 != addondata_path and path3 != addons_path and path3 != addondata_path and (int(Afiles_count) < 1000 and int(Bfiles_count) < 1000 and int(Cfiles_count) < 100 or addon in forceL):
				if int(Afiles_count) > 0:
					output = output + newline + str(i) + space2 + str(Afiles_count) + space + "DELETED FROM" + space + path
					removefiles(path)
					'''---------------------------'''
				if int(Bfiles_count) > 0:
					output = output + newline + str(i) + space2 + str(Bfiles_count) + space + "DELETED FROM" + space + path2
					removefiles(path2)
					'''---------------------------'''
				if int(Cfiles_count) > 0:
					output = output + newline + str(i) + space2 + str(Cfiles_count) + space + "DELETED FROM" + space + path3
					removefiles(path3)
					'''---------------------------'''
			else:
				output2 = output2 + newline + str(i) + space2 + "addon" + space2 + addon + space + "IGNORE"
		
		xbmc.sleep(500)
		xbmc.executebuiltin("UpdateLocalAddons")
		xbmc.sleep(500)
	'''---------------------------'''
	print printfirst + "removeaddons" + space + "addons" + space2 + str(addons) + space + "custom" + space2 + custom + space + "output" + space2 + output + newline + output2
	'''---------------------------'''

def removefiles(path):
	name = 'removefiles' ; printpoint = "" ; path1 = path[-1:] ; TypeError = "" ; extra = ""
	if 1 + 1 == 2:
		if "*" in path: path = path.replace("*","")
		if os.path.exists(path):
			import shutil
			if os.path.isdir(path) == True or "\*" in path:
				try:
					shutil.rmtree(path)
					printpoint = printpoint + "7"
				except Exception, TypeError:
					printpoint = printpoint + "5"
					if 'The process cannot access the file because it is being used by another process' in TypeError:
						for file in os.listdir(path):
							x = os.path.join(path, file)
							try: removefiles(x)
							except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
					else: extra = extra + newline + "TypeError" + space2 + str(TypeError)
			else:
				os.remove(path)
				printpoint = printpoint + "7"
		elif os.path.isfile(path) == True:
			printpoint = printpoint + "4"
			os.remove(path)
		else: printpoint = printpoint + "8"
	else:
		if not os.path.exists(path) and not systemplatformwindows and "*" in path: path = path.replace("*","")
		if os.path.exists(path):
			printpoint = printpoint + "0"
			if systemplatformandroid:
				import shutil
				if os.path.isdir(path) == True or "\*" in path:
					shutil.rmtree(path)
				else:
					os.remove(path)
			elif (systemplatformlinux or systemplatformlinuxraspberrypi): terminal('rm -rf '+path+'',name + space2 + path) ; printpoint = printpoint + "1"
			elif systemplatformwindows and (not admin3 or scripthtptdebug_Info_SystemName != 'GAL-PC' or path == guisettings_file or "settings.xml" in path):
				if os.path.isdir(path) == True or "\*" in path:
					if "*" in path and path1 == "*": path = path[:-1] ; printpoint = printpoint + "3"
					terminal('RD "'+path+'" /S /Q',name + space2 + path) ; printpoint = printpoint + "4"
				else: terminal('DEL "'+path+'" /Q /F',name + space2 + path) ; printpoint = printpoint + "5"
			else: pass ; printpoint = printpoint + "9"
		
		else: printpoint = printpoint + "8"
	
	if "0" in printpoint or admin3 or TypeError != "": print printfirst + name + "_LV" + printpoint + space + "path" + space2 + str(path) + extra

		
def copytree(source, target, symlinks=False, ignore=None):
	import shutil
	for item in os.listdir(source):
		s = os.path.join(source, item)
		t = os.path.join(target, item)
		
		if os.path.isdir(s):
			if os.path.exists(t):
				copytree(s, t, symlinks, ignore)
			else: shutil.copytree(s,t, symlinks, ignore)
		else:
			shutil.copy(s,t)
		
		#print "item" + space2 + str(item)

def movefiles(source, target):
	import shutil
	if os.path.exists(target):
		copyfiles(source, target, chmod="", mount=False)
		removefiles(source)
	else:
		shutil.move(source, target)
def copyfiles(source, target, chmod="", mount=False):
	name = 'copyfiles' ; printpoint = "" ; source1 = source[-1:] ; TypeError = "" ; extra = ""
	
	if systemplatformandroid: pass
	elif (systemplatformlinux or systemplatformlinuxraspberrypi) and mount == True: #GAL TEST THIS!
		printpoint = printpoint + "1"
		if target[:1] == '/':
			printpoint = printpoint + "2"
			target2 = target[:-1]
			terminal('mount -o remount,rw '+target2+'','mount' + space2 + target2)
	
	if systemplatformandroid:
		import shutil
		try:
			if '*' in source: source = source.replace('*',"") ; printpoint = printpoint + "0"
			if os.path.isdir(source) == True:
				printpoint = printpoint + "1"
				copytree(source, target, symlinks=False, ignore=None)
			elif os.path.isfile(source) == True:
				printpoint = printpoint + "2"
				shutil.copy(source, target)
				#shutil.copyfile(source, target)
			else:
				printpoint = printpoint + "3"
				shutil.copy(source, target)
				#terminal('cp -rf '+source+' '+target+'',name + space2 + source + space5 + target) ; printpoint = printpoint + "3"
				
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
		
	elif (systemplatformlinux or systemplatformlinuxraspberrypi):
		terminal('cp -rf '+source+' '+target+'',name + space2 + source + space5 + target) ; printpoint = printpoint + "3"
	elif systemplatformwindows and 1 + 1 == 2:
		if os.path.isdir(source) == True or "\*" in source:
			#if not "\\*" in source and source1 == "\\": source = source + '*' ; printpoint = printpoint + "4"
			if not admin3: terminal('xcopy "'+source+'" "'+target+'" /s /i /y >NUL',name + space2 + source + space5 + target) ; printpoint = printpoint + "5"
		else: terminal('copy "'+source+'" "'+target+'" /V /Y >NUL',name + space2 + source + space5 + target) ; printpoint = printpoint + "6"
	else:
		import shutil
		shutil.copy(source, target)
	
	if not systemplatformwindows and chmod != "": terminal('chmod '+chmod+' '+target+'','chmod' + space2 + target) ; printpoint = printpoint + "C" #GAL TEST THIS! 
	
	if os.path.isdir(source) == True or "\*" in source or os.path.isdir(target) == True or "\*" in target: returned = "ok"
	else:
		#sourcefile_date = getFileAttribute(1, source)
		sourcefile_size = getFileAttribute(2, source)
		#targetfile_date = getFileAttribute(1, target)
		targetfile_size = getFileAttribute(2, target)
		if sourcefile_size == targetfile_size:
			#if targetfile_date == str(timenow5)
			printpoint = printpoint + "7"
			returned = "ok"
		else:
			returned = "skip"
	
	if admin and not admin2 and admin3 or TypeError != "":
		print printfirst + name + "_LV" + printpoint + space + "source" + space2 + str(source) + space + "target" + space2 + str(target) + space + "source1" + space2 + str(source1) + extra
	
	return returned
	
def catfile(path):
	name = 'catfile'
	if not systemplatformwindows: returned = terminal('cat '+path+'', name + space2 + path)
	elif systemplatformwindows: returned = terminal('find /V "" "'+path+'"', name + space2 + path)
	
	'''---------------------------'''
	return returned
	
def notification_common(custom):
	if custom == "2": notification(addonString_servicehtpt(11).encode('utf-8'),addonString_servicehtpt(10).encode('utf-8'),"",4000) #processing, please wait
	elif custom == "3": notification(localize(257),localize(106) + space + localize(504),"",2000) #Error, Not Empty!
	elif custom == "4": notification('$LOCALIZE[79508]','$LOCALIZE[79376]',"",2000) #Check network connection!...
	elif custom == "5": notification('$LOCALIZE[79512]','$LOCALIZE[21451]',"",2000) #Check internet connection!...
	elif custom == "6": pass
	elif custom == "7": notification('$LOCALIZE[79494]',addonString_servicehtpt(10).encode('utf-8'),"",2000) #HODAH NIHNESHET
	elif custom == "8": notification('$LOCALIZE[16200]',"","",2000) #HAPEULA BUTLA
	elif custom == "9": notification('$LOCALIZE[16200]',addonString_servicehtpt(19).encode('utf-8'),"",2000) #HAPEULA BUTLA, LO BUTZHU SINUHIM
	elif custom == "10": notification('$LOCALIZE[79496]','$LOCALIZE[79497]' + "   -   " + '$LOCALIZE[79081]',"",4000) #AFSARUT ZOT NIMZET BEPITHU...
	elif custom == "11": notification(localize(257), '$LOCALIZE[79078]', "", 1000)   #ERROR | NASE SHENIT KAHET
	elif custom == "12": notification('$LOCALIZE[78959]',addonString_servicehtpt(10).encode('utf-8'),"",7000) #MATKIN HARHAVOT
	elif custom == "13": notification('$LOCALIZE[79072]',"...","",2000) #HAPEULA ISTAIMA BEHATZLAHA!
	elif custom == "14": notification('$LOCALIZE[74999]',"","",2000) #***Automatic Action***
	elif custom == "15":
		playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
		playlistposition = xbmc.getInfoLabel('Playlist.Position(video)')
		notification('$LOCALIZE[74998]','[COLOR=Yellow]' + playlistposition + space4 + playlistlength + '[/COLOR]',"",2000) #Playlist Done,
	
	elif custom == "16": notification("Downloading Files...","","",4000) #
	
	elif custom == "17": notification(localize(257),'$LOCALIZE[1446]',"",2000) #Error, Unknown
	elif custom == "18": notification('$LOCALIZE[79594]', '', "", 1000)   #
	elif custom == "19": notification('$LOCALIZE[16200]','$LOCALIZE[77877]',"",2000) #HAPEULA BUTLA, HAMISTAMES ITAREV BEAMZA APEHULA
	elif custom == "20": notification('$LOCALIZE[79531]',"","",2000) #The system issued an automatic abort
	elif custom == "21": notification('$LOCALIZE[79505]',addonString_servicehtpt(10).encode('utf-8'),"",4000) #The system is processing for solution...
	elif custom == "22": notification('$LOCALIZE[75062]','',"",4000) #The system is processing for solution...
	elif custom == "23": notification(localize(78929), localize(78980),"",4000) #Active download in background
	elif custom == "24": notification(localize(79195), localize(79154),"",2000) #Addon is missing! Trying to download addon
	elif custom == "25": notification('Want more related addons?', 'Check the Customize HTPT window (Ctrl+L)',"",4000) #Want more music addons? #Check the Customize HTPT window
	elif custom == "100": notification('$LOCALIZE[78971]' ,'[COLOR=Yellow]' + str74550.encode('utf-8') % (localize(342)) + '[/COLOR]' + space + addonString_servicehtpt(10).encode('utf-8') + space,"",7000) #MVAZEH TIKUN YADANI
	elif custom == "101": notification('$LOCALIZE[78971]' ,'[COLOR=Yellow]' + str74550.encode('utf-8') % (str36903.encode('utf-8')) + '[/COLOR]' + space + addonString_servicehtpt(10).encode('utf-8') + space,"",7000) #MVAZEH TIKUN YADANI

def replaceAll(file,searchExp,replaceExp):
    '''UNUSED?'''
    import fileinput 
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def replaceAll2(file,searchExp,replaceExp):
    '''UNUSED?'''
    import fileinput 
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)
		#if line == 0:
			#add sys.stdout.write('\n')
			#add sys.stdout.write('import xbmc, xbmcgui, xbmcaddon')

def write_to_file(path, content, append=False, silent=True , utf8=False): #UNUSED
	'''``r/r+/w/w+/a/a+'''
	if utf8 == True: import codecs
	try:
		if append == True:
			if utf8 == True: f = codecs.open(path, 'ab', encoding='utf-8')
			else: f = open(path, 'ab')
		else:
			if utf8 == True: f = codecs.open(path, 'wb', 'utf-8')
			else: f = open(path, 'wb')

		f.write(content)
		f.close()
		return True
	except:
		if silent != True:
			print("Could not write to " + path)
		return False

def getAddonInfo(addon):
	name = 'getAddonInfo' ; printpoint = ""
	thumb = "" ; fanart = "" ; summary = "" ; description = ""
	
	thumb = os.path.join(addons_path, addon, 'icon.png')
	fanart = os.path.join(addons_path, addon, 'fanart.jpg')
	addoninfo = os.path.join(addons_path, addon, 'addon.xml')
	addoninfo_ = read_from_file(addoninfo, silent=True, lines=False, retry=False, printpoint="", addlines="")
	systemlanguage_ = systemlanguage[:2].lower()
	
	if addoninfo_ != "":
		i = 0
		for i in range(0,2):
			if i == 0: summary = regex_from_to(addoninfo_, '<summary lang="'+systemlanguage_+'">', '</summary>', excluding=True)
			elif i == 1: summary = regex_from_to(addoninfo_, '<summary>', '</summary>', excluding=True)
			#elif i == 1: summary = regex_from_to(addoninfo_, '<summary lang="en">', '</summary>', excluding=True)
			if summary != "": break
		
		i = 0
		for i in range(0,2):
			if i == 0: description = regex_from_to(addoninfo_, '<description lang="'+systemlanguage_+'">', '</description>', excluding=True)
			elif i == 1: description = regex_from_to(addoninfo_, '<description>', '</description>', excluding=True)
			#elif i == 1: description = regex_from_to(addoninfo_, '<description lang="en">', '</description>', excluding=True)
			if description != "": break
	
	text = 'systemlanguage' + space2 + str(systemlanguage) + space + 'systemlanguage[:2]' + space2 + str(systemlanguage_) + newline + \
	'thumb' + space2 + str(thumb) + newline + \
	'fanart' + space2 + str(fanart) + newline + \
	'summary' + space2 + str(summary) + newline + \
	'description' + space2 + str(description)
	
	try: summary = summary.encode('utf-8')
	except: pass
	try: description = description.encode('utf-8')
	except: pass
	plot = '[COLOR=Yellow]'+summary+'[/COLOR]'+'[CR][CR]'+description
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	return thumb, fanart, summary, description, plot
	
def read_from_file(infile, silent=True, lines=False, retry=True, printpoint="", addlines=""):
	name = 'read_from_file' ; printpoint = "" ; returned = "" ; TypeError = "" ; extra = "" ; l = []
	try:
		if os.path.exists(infile):
			printpoint = printpoint + "1"
			infile_ = open(infile, 'rb')
			if lines == True:
				printpoint = printpoint + "2"
				for line in infile_.readlines():
					if addlines != "":
						line = CleanString(line, filter=[])
						l.append(str(addlines) + line)
					else: l.append(line)
				returned = l
			else:
				printpoint = printpoint + "3"
				r = infile_.read()
				returned = str(r)
			infile_.close()
		
		if (returned == "" or returned == None) and retry == True:
			printpoint = printpoint + "6"
			xbmc.sleep(2000)
			read_from_file(infile, silent=silent, lines=lines, retry=False, printpoint=printpoint)
			
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9"
	
	if returned != "" or (returned == None or returned == "") and retry == False:
		if admin and admin2 and admin3 or retry == False:
			print printfirst + name + "_LV" + printpoint + space + "infile" + space2 + str(infile) + space + "lines" + space2 + str(lines) + newline + \
			"returned[:10]" + space2 + str(returned[:10]) + extra
		
		return str(returned)
		
def regex_from_to(text, from_string, to_string, excluding=True):
    import re
    admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
    admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
    admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
    printpoint = "" ; TypeError = "" ; extra = ""
    if excluding:
        try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
        except Exception, TypeError:
            extra = newline + "TypeError" + space2 + str(TypeError)
            try:
				r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text)
				if r == None: r = ""
            except Exception, TypeError:
			    extra = newline + "TypeError" + space2 + str(TypeError)
			    r = ""
    else:
        try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
        except Exception, TypeError:
            try:
				extra = newline + "TypeError" + space2 + str(TypeError)
				r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text)
				if r == None: r = from_string + to_string
            except Exception, TypeError:
				extra = newline + "TypeError" + space2 + str(TypeError)
				r = ""
	
    if admin and admin2 and admin3 and 1 + 1 == 3:
		if excluding == True or r == "": print printfirst + "regex_from_to" + space2 + "from_string" + space2 + str(from_string) + space + "to_string" + space2 + str(to_string) + space + "r" + space2 + str(r) + space + "text" + space2 + str(text) + space + extra
		else: print printfirst + "regex_from_to" + space2 + "from_string" + space2 + "r" + space2 + str(r) + space + "text" + space2 + str(text) + space + extra
    return str(r)

def regex_get_all(text, start_with, end_with): #UNUSED
    import re
    r = re.findall("(?i)" + start_with + "([\S\s]+?)" + end_with, text)
    return r
	
def replace_word(infile,old_word,new_word, infile_="", LineR=False , LineClean=False):
	printpoint = "" ; extra = "" ; TypeError = "" ; value = ""

	if not os.path.isfile(infile): printpoint = printpoint + "9a" #(infile_ == "" or LineR == True) and
	elif old_word == None or new_word == None: printpoint = printpoint + "9b"
	else:
		if LineR == False:
			'''replace all'''
			printpoint = printpoint + "2" #if infile_ == "" or infile_ == None: 
			infile_ = read_from_file(infile, lines=False)
			value=infile_.replace(old_word,new_word)
			'''---------------------------'''
		else:
			'''replace each line'''
			printpoint = printpoint + "3"
			import fileinput, re
			infile_ = read_from_file(infile, lines=True)
			#print infile_
			for line in infile_:
				print line
				if LineClean == True and re.match(r'^\s*$', line): line = "" #line.replace('\n\n','\n') #re.match(r'^\s*$', line)
				elif old_word != "" and new_word != "":
					if old_word in line:
						value = value + newline + line.replace(old_word,new_word)
						#line = '\n' + line
						#sys.stdout.write(line)
						'''---------------------------'''
					else: value = value + newline + line
				else:
					value = value + line
				#if value != "": value = value + newline
				'''---------------------------'''
					#line = '\n' + line
					#sys.stdout.write(line)
				
				
				#if line != "": sys.stdout.write(line) #infile__.write(line)
				#infile__.write(value)
				#infile__.close()
		
		infile__=open(infile,'wb')
		infile__.write(value)
		infile__.close()
		'''---------------------------'''
		
	if admin and admin2 and admin3 or '9' in printpoint:
		print printfirst + "replace_word_LV" + printpoint + space + "infile" + space2 + str(infile) + space + newline + \
		"old_word" + space2 + str(old_word) + newline + \
		"new_word" + space2 + str(new_word) + newline + \
		extra
		#"value" + space2 + str(value) + extra

def ReloadSkin(admin):
	if property_reloadskin == "":
		xbmc.executebuiltin('ActivateWindow(1000)')
		xbmc.executebuiltin('SetProperty(ReloadSkin,true,home)')
		if playerhasmedia: xbmc.executebuiltin('Action(Stop)') ; notification('Video Stop',"","",1000) ; xbmc.sleep(1000)
		notification("..","","",1000)
		xbmc.sleep(200)
		xbmc.executebuiltin('ReloadSkin()') ; xbmc.sleep(1500)
		xbmc.executebuiltin('AlarmClock(reloadskin,ClearProperty(ReloadSkin,home),00:05,silent)')
		xbmc.executebuiltin('Action(Back)')
		#xbmc.executebuiltin('ReplaceWindow(CustomHomeCustomizer.xml)')
	else:
		pass
		#xbmc.executebuiltin('RunScript(script.htpt.smartbuttons,,?mode=215&value=_)')
	
def settingschange(window,systemgetbool,falsetrue,force,string1,string2):
	'''systemgetbool'''
	systemgetbool2 = xbmc.getCondVisibility('System.GetBool('+ systemgetbool +')')
	systemgetbool2str = str(systemgetbool2)
	if systemgetbool2str != falsetrue or force == 'yes':
		if admin: xbmc.executebuiltin('Notification(Admin,settingschange '+ systemgetbool +' ('+ systemgetbool2str +'),10000)')
		xbmc.executebuiltin('ActivateWindow('+ window +')')
		'''Right'''
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		if not string1 in systemcurrentcontrol:
			xbmc.executebuiltin('Action(Right)')
			xbmc.sleep(100)
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			if not string1 in systemcurrentcontrol:
				xbmc.executebuiltin('Action(Right)')
				xbmc.sleep(100)
				systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
				if not string1 in systemcurrentcontrol:
					xbmc.executebuiltin('Action(Right)')
					xbmc.sleep(100)
					systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
					if not string1 in systemcurrentcontrol:
						xbmc.executebuiltin('Action(Right)')
						xbmc.sleep(100)
						systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		xbmc.sleep(40)
		if string1 in systemcurrentcontrol: xbmc.executebuiltin('Action(Down)')
		
		'''Down'''
		xbmc.sleep(100)
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		if not string2 in systemcurrentcontrol:
			xbmc.executebuiltin('Action(Down)')
			xbmc.sleep(100)
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			if not string2 in systemcurrentcontrol:
				xbmc.executebuiltin('Action(Down)')
				xbmc.sleep(100)
				systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
				if not string2 in systemcurrentcontrol:
					xbmc.executebuiltin('Action(Down)')
					xbmc.sleep(100)
					systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
					if not string2 in systemcurrentcontrol:
						xbmc.executebuiltin('Action(Down)')
						xbmc.sleep(100)
						systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		xbmc.sleep(40)
		
		'''Select'''
		systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
		if string2 in systemcurrentcontrol:
			xbmc.executebuiltin('Action(Select)')
			xbmc.sleep(100)
			if systemgetbool2 != falsetrue and force == 'yes': xbmc.executebuiltin('Action(Select)')
			systemgetbool2 = xbmc.getCondVisibility('System.GetBool('+ systemgetbool +')')
			if admin: xbmc.sleep(1000)
			if systemgetbool2 != falsetrue and force == 'yes' or force == 'no': xbmc.executebuiltin('Action(Back)')
			if not systemgetbool2: xbmc.executebuiltin('Notification('+ systemcurrentcontrol +',,5000)')
			
def setGeneral_ScriptON(custom, General_ScriptON, mode):
	'''check if this script is already running'''
	name = 'setGeneral_ScriptON' ; printpoint = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
	property_addonisrunning = xbmc.getInfoLabel('Window(home).Property('+addonID+'_RUNNING)')
	
	if mode == None: mode = ""
	
	if custom == "0":
		'''------------------------------
		---SCRIPT-START------------------
		------------------------------'''
		if property_addonisrunning == "true":
			count = 0 ; printpoint = printpoint + "1"
			while count < 10 and property_addonisrunning and not xbmc.abortRequested:
				if count == 0:
					printpoint = printpoint + "2"
					if admin3: notification(addonID, "Start", "", 1000)
					elif addonID != "service.htpt.fix" and addonID != "service.htpt.debug": notification("...", "", "", 1000)
				xbmc.sleep(100)
				count += 1
				property_addonisrunning = xbmc.getInfoLabel('Window(home).Property('+addonID+'_RUNNING)')
				#property_addonisrunning = xbmc.getCondVisibility('!IsEmpty(Window(home).Property('+addonID+'_RUNNING))')
		xbmc.executebuiltin('SetProperty('+addonID+'_RUNNING, true, home)')
			
	elif custom == "1":
		'''------------------------------
		---SCRIPT-END--------------------
		------------------------------'''
		count = 0 ; printpoint = printpoint + "1"
		while count < 10 and property_addonisrunning != "true" and not xbmc.abortRequested:
			if count == 1:
				printpoint = printpoint + "2"
				if admin3: notification(addonID, "End", "", 1000)
				elif addonID != "service.htpt.fix" and addonID != "service.htpt.debug": notification("...", "", "", 1000)
			xbmc.sleep(100)
			count += 1
			property_addonisrunning = xbmc.getInfoLabel('Window(home).Property('+addonID+'_RUNNING)')
			#property_addonisrunning = xbmc.getCondVisibility('!IsEmpty(Window(home).Property('+addonID+'_RUNNING))')
		xbmc.executebuiltin('ClearProperty('+addonID+'_RUNNING, home)')

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	#property_addonisrunning = xbmc.getInfoLabel('Window(home).Property('+addonID+'_RUNNING)')
	#property_addonisrunning = xbmc.getCondVisibility('!IsEmpty(Window(home).Property('+addonID+'_RUNNING))')
	if admin and admin2 and admin3:
		print printfirst + "setGeneral_ScriptON_LV" + printpoint + space + "custom" + space2 + custom + space + "General_ScriptON" + space2 + General_ScriptON + space + "mode" + space2 + mode + newline + \
		space + "addonID" + space2 + str(addonID) + space + "property_addonisrunning" + space2 + str(property_addonisrunning)
		'''---------------------------'''
	
def setSkinSetting(custom,set1,set1v):
	if xbmc.getSkinDir() == 'skin.htpt':
		'''------------------------------
		---SET-SKIN-SETTING-1------------
		------------------------------'''
		
		name = 'setSkinSetting' ; printpoint = "" ; admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)') ; setting1 = ""
		
		if '$LOCALIZE' in set1v or '$ADDON' in set1v: 
			try: set1v = xbmc.getInfoLabel(set1v) ; printpoint = printpoint + "1"
			except Exception, TypeError: printpoint = printpoint + "9"
		''' custom: 0 = Skin.String, 1 = Skin.HasSetting'''
		'''---------------------------'''
		printpoint = printpoint + "2"
		if custom == "0":
			printpoint = printpoint + "3"
			setting1 = xbmc.getInfoLabel('Skin.String('+ set1 +')')
			if setting1 != set1v: xbmc.executebuiltin('Skin.SetString('+ set1 +','+ set1v +')')
			'''---------------------------'''
			
		elif custom == "1":
			printpoint = printpoint + "4"
			setting1 = xbmc.getInfoLabel('Skin.HasSetting('+ set1 +')')
			#print setting1 + "zzz"
			'''---------------------------'''
			if (setting1 == localize(20122) and localize(20122) != "") or setting1 == "true" or setting1 == "True": setting1 = "true"
			else: setting1 = "false"
			'''---------------------------'''
			if (set1v == localize(20122) and localize(20122) != "") or set1v == "true" or set1v == "True": set1v = "true"
			else: set1v = "false"
			'''---------------------------'''
			if setting1 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set1 +')')
			
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if setting1 != set1v and admin and admin2 and admin3:
			print printfirst + name + "_LV" + printpoint + space + custom + space + set1 + space2 + setting1 + " - " + set1v + space + \
			newline + "localize(20122)" + space2 + localize(20122)
			'''---------------------------'''

def setSkinSetting5(custom,set1,set1v,set2,set2v,set3,set3v,set4,set4v,set5,set5v):
	if xbmc.getSkinDir() == 'skin.htpt':
		'''------------------------------
		---SET-SKIN-SETTING-5------------
		------------------------------'''
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		
		try: set1v = set1v.encode('utf-8')
		except: pass
		try: set2v = set2v.encode('utf-8')
		except: pass
		try: set3v = set3v.encode('utf-8')
		except: pass
		try: set4v = set4v.encode('utf-8')
		except: pass
		try: set5v = set5v.encode('utf-8')
		except: pass
		''' custom: 0 = Skin.String, 1 = Skin.HasSetting'''
		if custom == "0":
			setting1 = xbmc.getInfoLabel('Skin.String('+ set1 +')')
			setting2 = xbmc.getInfoLabel('Skin.String('+ set2 +')')
			setting3 = xbmc.getInfoLabel('Skin.String('+ set3 +')')
			setting4 = xbmc.getInfoLabel('Skin.String('+ set4 +')')
			setting5 = xbmc.getInfoLabel('Skin.String('+ set5 +')')
			'''---------------------------'''
		elif custom == "1":
			setting1 = xbmc.getInfoLabel('Skin.HasSetting('+ set1 +')')
			setting2 = xbmc.getInfoLabel('Skin.HasSetting('+ set2 +')')
			setting3 = xbmc.getInfoLabel('Skin.HasSetting('+ set3 +')')
			setting4 = xbmc.getInfoLabel('Skin.HasSetting('+ set4 +')')
			setting5 = xbmc.getInfoLabel('Skin.HasSetting('+ set5 +')')
			'''---------------------------'''
			if (setting1 == localize(20122) and localize(20122) != "") or setting1 == "true" or setting1 == "True": setting1 = "true"
			else: setting1 = "false"
			if (setting2 == localize(20122) and localize(20122) != "") or setting2 == "true" or setting2 == "True": setting2 = "true"
			else: setting2 = "false"
			if (setting3 == localize(20122) and localize(20122) != "") or setting3 == "true" or setting3 == "True": setting3 = "true"
			else: setting3 = "false"
			if (setting4 == localize(20122) and localize(20122) != "") or setting4 == "true" or setting4 == "True": setting4 = "true"
			else: setting4 = "false"
			if (setting5 == localize(20122) and localize(20122) != "") or setting5 == "true" or setting5 == "True": setting5 = "true"
			else: setting5 = "false"
			'''---------------------------'''
			if (set1v == localize(20122) and localize(20122) != "") or set1v == "true" or set1v == "True": set1v = "true"
			else: set1v = "false"
			if (set2v == localize(20122) and localize(20122) != "") or set2v == "true" or set2v == "True": set2v = "true"
			else: set2v = "false"
			if (set3v == localize(20122) and localize(20122) != "") or set3v == "true" or set3v == "True": set3v = "true"
			else: set3v = "false"
			if (set4v == localize(20122) and localize(20122) != "") or set4v == "true" or set4v == "True": set4v = "true"
			else: set4v = "false"
			if (set5v == localize(20122) and localize(20122) != "") or set5v == "true" or set5v == "True": set5v = "true"
			else: set5v = "false"
			'''---------------------------'''
		if custom == "0":
			if setting1 != set1v: xbmc.executebuiltin('Skin.SetString('+ set1 +','+ set1v +')')
			if setting2 != set2v: xbmc.executebuiltin('Skin.SetString('+ set2 +','+ set2v +')')
			if setting3 != set3v: xbmc.executebuiltin('Skin.SetString('+ set3 +','+ set3v +')')
			if setting4 != set4v: xbmc.executebuiltin('Skin.SetString('+ set4 +','+ set4v +')')
			if setting5 != set5v: xbmc.executebuiltin('Skin.SetString('+ set5 +','+ set5v +')')
			'''---------------------------'''
		elif custom == "1":
			if setting1 != set1v: xbmc.executebuiltin('Skin.ToggleSetting('+ set1 +')')
			if setting2 != set2v: xbmc.executebuiltin('Skin.ToggleSetting('+ set2 +')')
			if setting3 != set3v: xbmc.executebuiltin('Skin.ToggleSetting('+ set3 +')')
			if setting4 != set4v: xbmc.executebuiltin('Skin.ToggleSetting('+ set4 +')')
			if setting5 != set5v: xbmc.executebuiltin('Skin.ToggleSetting('+ set5 +')')
			'''---------------------------'''
			
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''	
		if admin and (setting1 != set1v or setting2 != set2v or setting3 != set3v or setting4 != set4v or setting5 != set5v): print printfirst + "setSkinSetting5" + space2 + set1 + space + set2 + space + set3 + space + set4 + space + set5 + space3
		'''---------------------------'''

def setsetting_custom1(addon,set1,set1v):
	'''------------------------------
	---SET-ADDON-SETTING-1-----------
	------------------------------'''
	TypeError = ""
	try:
		getsetting_custom          = xbmcaddon.Addon(addon).getSetting
		setsetting_custom          = xbmcaddon.Addon(addon).setSetting
	except Exception, TypeError:
		TypeError = newline + "TypeError" + space2 + str(TypeError)
		print printfirst + "setsetting_custom1" + space + TypeError
	
	if TypeError == "":
		set = getsetting_custom(set1)
		set1v = str(set1v)
		'''---------------------------'''
		if set != set1v:
			setsetting_custom(set1,set1v)
			'''------------------------------
			---PRINT-END---------------------
			------------------------------'''
			if admin and not admin2 or TypeError != "": print printfirst + "setsetting_custom1" + space2 + addon + space + set1 + space2 + set1v + space3
			'''---------------------------'''

def supportcheck(name, supported, totalspace=1, Intel=False, silence=False, platform=""):
	'''------------------------------
	---CHECK-IF-MODEL-IS-SUPPORTED---
	------------------------------'''
	'''platform: 1- Windows, 2-Linux, 3-Linux-PI, 4-Android, 5-OSX, 6-IOS'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; platform_ = "_"
	id10str = xbmc.getInfoLabel('Skin.String(ID10)')
	
	try: name = name.encode('utf-8')
	except: pass
	
	try: scripthtptdebug_Info_TotalSpaceN = int(scripthtptdebug_Info_TotalSpace)
	except: scripthtptdebug_Info_TotalSpaceN = 0
	
	supported.append("ADMIN")
	extra = "" ; printpoint = "" ; returned = ""
	#if platform != "" and [systemplatformwindows + "1" in platform] | [systemplatformlinux + "2" in platform] | [systemplatformlinuxraspberrypi + "3" in platform] | [systemplatformandroid + "4" in platform] | [systemplatformosx + "5" in platform] | [systemplatformios + "6" in platform]:
	if platform != "":
		if systemplatformwindows: platform_ = "1"
		elif systemplatformlinux: platform_ = "2"
		elif systemplatformlinuxraspberrypi: platform_ = "3"
		elif systemplatformandroid: platform_ = "4"
		elif systemplatformosx: platform_ = "5"
		elif systemplatformios: platform_ = "6"
		else: platform_ = ""
		'''---------------------------'''
		
	if platform != "" and platform_ in platform and not admin3:
		printpoint = printpoint + "9"
		dialogok(localize(75062), "", "" ,str74542.encode('utf-8'))
	elif not id10str in supported and scripthtptdebug_Info_TotalSpaceN < totalspace or (Intel == True and scripthtptdebug_Info_Intel == "false"):
		'''------------------------------
		---UNSUPPORT-DEVICE--------------
		------------------------------'''
		printpoint = printpoint + "9"
		if id10str == "": id10str = "?"
		if scripthtptdebug_Info_Model != "": extra = '[CR]' + "[COLOR=Grey]" + scripthtptdebug_Info_Model + "[/COLOR]"
		if silence == False:
			if name == str75004.encode('utf-8'): dialogok('[COLOR=Yellow]' + addonString(124) % (id10str) + '[/COLOR]' + extra, localize(74541), localize(75784), '')
			else: dialogok('$LOCALIZE[79501]',str74540.encode('utf-8') % (id10str) + extra, str74543.encode('utf-8') % (name) ,str74542.encode('utf-8'))
			'''---------------------------'''
	else: printpoint = printpoint + "7"
	
	if "9" in printpoint: returned = "skip"
	else: returned = "ok"
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "supportcheck_LV" + printpoint + space + "name" + space2 + str(name) + space + "supported" + space2 + str(supported) + space + "totalspace" + space2 + str(totalspace) + space + "returned" + space2 + returned
	'''---------------------------'''
	
	'''---------------------------'''
	return returned
	
def datetostring(dt_str):
	TypeError = ""
	printpoint = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	
	
	dt_str2 = str(dt_str)
	dt_str2 = dt_str2.replace("00:00:00","",1)
	dt_str2 = dt_str2.replace("0:00:00","",1)
	dt_str2 = dt_str2.replace(" ","",1)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and admin2 or str(TypeError) != "": print printfirst + "datetostring_LV" + printpoint + space + "dt_str" + space2 + dt_str + space + "dt_str2" + space2 + dt_str2
	'''---------------------------'''
	return dt_str2

def getfileID(file):
	fileID = ""
	if file == "Nintendo 64.zip": fileID = "mwo6jqoey4tnsgx" #buyhtpt
	elif file == "Sony Playstation_4P.zip": fileID = "" #fixhtpt
	
	elif file == "metadata.common.imdb.com.zip": fileID = "zh8qb5xivoac668" #htpthtpt
	elif file == "metadata.common.impa.com.zip": fileID = "3nfx22a7lp7srzs" #htpthtpt
	elif file == "metadata.common.movieposterdb.com.zip": fileID = "gewjxbtbdb06rl8" #htpthtpt
	elif file == "metadata.common.ofdb.de.zip": fileID = "n2r3rf72i1qizor" #htpthtpt
	elif file == "metadata.common.port.hu.zip": fileID = "wp3hm7o3nzmxtty" #htpthtpt
	elif file == "metadata.common.rt.com.zip": fileID = "j401wzrw6t4msw1" #htpthtpt
	elif file == "metadata.common.trakt.tv.zip": fileID = "ttat1kqmcgnj8eb" #htpthtpt
	elif file == "metadata.universal.zip": fileID = "c199vd68mhknyyp" #htpthtpt
	elif file == "script.openelec.rpi.config.zip": fileID = "r98gcue3e3p3pr4" #htpthtpt
	elif file == "plugin.program.advanced.launcher.zip": fileID = "hnclp7yn4ea5433" #htpthtpt
	elif file == "repository.lambda.zip": fileID = "bnn0fua0tganq6a" #htpthtpt
	elif file == "script.module.unidecode.zip": fileID = "fojosavj4hvwgxe" #htpthtpt
	elif file == "plugin.video.dailymotion_com.zip": fileID = "fffcc2barlwyeuo" #htpthtpt
	
	elif file == "AceEngine.zip": fileID = "drh8nac0awpmxc4" #htpthtpt
	elif file == "emu_htpt.zip": fileID = "x1802zw4fhgcp44" #htpthtpt
	elif file == "Media.zip": fileID = "w55o5fp4cng3m7d" #htpthtpt
	
	elif file == "Arcade_2P_Plus.zip": fileID = "" #infohtpt
	elif file == "Sony Playstation_2P.zip": fileID = "" #tuluhtpt
	
	elif file == "Nintendo.zip": fileID = "nt05zl4ygnynxen" #htptuser1
	elif file == "Sega Genesis.zip": fileID = "b8lph86pb4b5e0l" #htptuser1
	elif file == "Sega Master System.zip": fileID = "c5ingtyhgkwjmx7" #htptuser1
	elif file == "Super Nintendo.zip": fileID = "d3zbfvw6umro1vn" #htptuser1
	elif file == "TurboGrafx 16.zip": fileID = "0zg9x4uw1hrm8zb" #htptuser1
	
	elif file == "Arcade_1P.zip": fileID = "7yfdgvzhduoihn3" #htptuser2
	elif file == "Arcade_3P.zip": fileID = "j6bl5uaa01uzspj" #htptuser2
	elif file == "Arcade_4P.zip": fileID = "5alcp543pmyqrzh" #htptuser2
	elif file == "Arcade_ADULT.zip": fileID = "rg4m5oi50c0g4e7" #htptuser2
	elif file == "Arcade_GEAR.zip": fileID = "8vojf28ojtdlgau" #htptuser2
	elif file == "Arcade_TULU.zip": fileID = "jhk1esc1x9k5bwx" #htptuser2

	elif file == "Arcade_2P.zip": fileID = "dfsu0sjydw2zuh5" #htptuser3 (FULL)
	elif file == "Arcade_2P_.zip": fileID = "3989r3p7hfxe2t3" #htptuser3 (FULL)
	
	elif file == "Arcade_2P_area51.zip": fileID = "39t73jvurnepho1" #htptuser4
	elif file == "Arcade_2P_area51mx.zip": fileID = "03b3oqm97lt06cj" #htptuser4
	
	elif file == "Sony Playstation_1P_Crash Bandicoot": fileID = "st3jd9y0no8pbn0" #htptuser5 (FULL)
	elif file == "Sony Playstation_1P_Dragon Valor": fileID = "7q43b820d8hd71i" #htptuser5 (FULL)
	elif file == "Sony Playstation_1P_Pacman World": fileID = "5j36isrgl4pasx7" #htptuser5 (FULL)
	elif file == "Sony Playstation_1P_Road Rash 3D": fileID = "my6lt21oixpuy3l" #htptuser5 (FULL)
	
	elif file == "Sony Playstation_1P_Final Fantasy VIII.zip": fileID = "gt5its29qvdt4f9" #htptuser6 (500MB)
	elif file == "Sony Playstation_1P_Spider-Man.zip": fileID = "e2wc0xa7pk85sf1" #htptuser6 (500MB)
	
	elif file == "Sony Playstation_1P_Final Fantasy VII.zip": fileID = "85llpgfjz4uih2z" #htptuser7
	elif file == "Sony Playstation_1P_Dino Crisis 2.zip": fileID = "awmx89zo20kmks4" #htptuser7
	elif file == "Sony Playstation_1P_Digimon World 3.zip": fileID = "esiv8i4on1h6wso" #htptuser7
	elif file == "Sony Playstation_1P_Crash Bandicoot 2.zip": fileID = "m0hnjiy8sup4jtv" #htptuser7
	
	elif file == "Sony Playstation_1P_Castlevania - Symphony Of The Night.zip": fileID = "1d8sik6zdjp5ago" #htptuser8
	elif file == "Sony Playstation_1P_Grand Theft Auto 2.zip": fileID = "zti40bzu1o5e2os" #htptuser8
	elif file == "Sony Playstation_1P_Jackie Chan Stuntmaster.zip": fileID = "kbm6jb9pvg9fyza" #htptuser8
	elif file == "Sony Playstation_1P_Mega Man X4.zip": fileID = "8kopww6klbqn0jq" #htptuser8
	elif file == "Sony Playstation_1P_Metal Gear Solid.zip": fileID = "zreea6rsbo6t7ca" #htptuser8
	
	elif file == "Sony Playstation_1P_Spyro Year of the Dragon.zip": fileID = "c8j2hgeyd6x33xi" #htptuser9
	elif file == "Sony Playstation_1P_Tales of Destiny.zip": fileID = "xtzt22coc1omcko" #htptuser9
	elif file == "Sony Playstation_1P_The Legend of Dragoon.zip": fileID = "cp6foxr496i78ay" #htptuser9
	
	elif file == "Sony Playstation_2P_.zip": fileID = "" #htptuser10
	
	elif file == "Sony Playstation_2P_.zip": fileID = "" #htptuser11
	
	elif file == "Sony Playstation_2P_.zip": fileID = "" #htptuser12
	
	elif file == "Sony Playstation_2P_.zip": fileID = "" #htptuser13
	
	elif file == "Sony Playstation_2P_.zip": fileID = "" #htptuser14
	
	elif file == "Sony Playstation_2P_.zip": fileID = "" #htptuser15
	
	elif file == "?": fileID = "" #htptuser16
	
	elif file == "?": fileID = "" #htptuser17
	
	elif file == "?": fileID = "" #htptuser18
	
	elif file == "?": fileID = "" #htptuser19 #
	
	elif file == "?": fileID = "" #htptuser20
	
	
	
	'''---------------------------'''
	return fileID

def stringtodate(dt_str, dt_func):
	#from datetime import datetime
	TypeError = ""
	extra = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	printpoint = ""
	count = 0
	dt_str = str(dt_str)
	dt_str = dt_str.replace(" ","",1)
	dt_obj = ""
	#dt_str = '9/24/2010 5:03:29 PM'
	#dt_func = '%m/%d/%Y %I:%M:%S %p'
	if dt_str == "" or dt_func == "" or dt_str == None or dt_func == None:
		printpoint = printpoint + "9"
		if admin: notification("stringtodate_ERROR!","isEMPTY","",1000)
	else:
		while count < 3 and not "7" in printpoint and not xbmc.abortRequested:
			try:
				if count == 0: from datetime import datetime
				dt_obj = datetime.strptime(dt_str, dt_func)
				printpoint = printpoint + "7"
			except Exception, TypeError:
				dt_obj = "error"
				if admin and not admin2 and count == 2:
					dialogkaitoastW = xbmc.getCondVisibility('Window.IsVisible(DialogKaiToast.xml)')
					if not dialogkaitoastW: notification("stringtodate_ERROR!","error","",1000)
			count += 1
			xbmc.sleep(100)

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	dt_objS = str(dt_obj)
	if TypeError != "": extra = newline + "TypeError" + space2 + str(TypeError) + space + "count" + space2 + str(count)
	if admin and admin2 or extra != "": print printfirst + "stringtodate_LV" + printpoint + space + "dt_str" + space2 + dt_str + space + "dt_objS" + space2 + dt_objS + extra
	'''---------------------------'''
	return dt_obj
	
class TextViewer_Dialog(xbmcgui.WindowXMLDialog):
    ACTION_PREVIOUS_MENU = [9, 92, 10]

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self)
        self.text = kwargs.get('text')
        self.header = kwargs.get('header')

    def onInit(self):
        self.getControl(1).setLabel(self.header)
        self.getControl(5).setText(self.text)

    def onAction(self, action):
        if action in self.ACTION_PREVIOUS_MENU:
            self.close()

    def onClick(self, controlID):
        pass

    def onFocus(self, controlID):
        pass

class Custom1000_Dialog(xbmcgui.Window):
  '''progress= | title= | '''
  def __init__(self):
	extra = "" ; extra2 = "" ; TypeError = "" ; printpoint = "" ; count_set = 0 ; exit_requested = False ; progress = '0' ; title = '' ; addonisrunning = '?'
	progress = xbmc.getInfoLabel('Window(home).Property(TEMP)')
	title = xbmc.getInfoLabel('Window(home).Property(TEMP2)')
	addonisrunning = xbmc.getInfoLabel('Window(home).Property(script.htpt.smartbuttons_RUNNING)')
	
	self.strActionInfo = xbmcgui.ControlLabel(0, 0, 1260, 680,'', 'Size42B', 'White2','',6)
	self.addControl(self.strActionInfo)
	self.strActionInfo.setLabel(localize(31407))
	
	if progress != "":
		'''Create Dialog Progress'''
		self.strActionInfo = xbmcgui.ControlLabel(0, 50, 1260, 680,'', 'size36B', 'Yellow','',6)
		self.addControl(self.strActionInfo)
		self.strActionInfo.setLabel(progress)
	
	if title != "":
		'''Create Subject'''
		self.strActionInfo = xbmcgui.ControlLabel(0, 100, 1260, 680,'', 'size28', 'White','',6)
		self.addControl(self.strActionInfo)
		self.strActionInfo.setLabel(str(title))
		
  def _exit(self):
      global exit_requested
      exit_requested = True
      self.close()
      if admin:
		print printfirst + 'Custom1000_Dialog' + space + 'progress' + space2 + str(progress) + space + "title" + space2 + str(title) + space + 'addonisrunning' + space2 + str(addonisrunning)
	  
  def onAction(self, action):
	if action == ACTION_PREVIOUS_MENU:
	  self._exit()
	elif action == ACTION_SELECT_ITEM:
	  self._exit()
	  
	  
def ActivateWindow(custom, addon, url, return0, wait=True):
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	containernumitems = ""
	printpoint = ""
	count = ""
	if return0 == 0: return0 = ',return'
	else: return0 = ""
	return0 = str(return0)
	if wait == True: setSkinSetting("1",'AutoViewoff',"true") ; xbmc.sleep(500)
	if custom == "0": xbmc.executebuiltin('RunAddon('+ addon +')')
	elif custom == "1": xbmc.executebuiltin('ActivateWindow(10025,'+ url +' '+ return0 +')')
	
	'''---------------------------'''
	if wait == True:
		printpoint = printpoint + "2"
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		containernumitems = xbmc.getInfoLabel('Container.NumItems')
		count = 0
		while count < 10 and not addon in containerfolderpath and not xbmc.abortRequested: #or containernumitems == "0"
			count += 1
			xbmc.sleep(300)
			containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
			containernumitems = xbmc.getInfoLabel('Container.NumItems')
			systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
			if systemidle1: xbmc.sleep(300)
			if containerfolderpath == "" and containernumitems == '8': count = 20
		if count < 10:
			if containerfolderpath == url: printpoint = printpoint + "5"
			else: printpoint = printpoint + "7"
		else: printpoint = printpoint + "9"
	else: printpoint = printpoint + "8"
	
	ViewSetFocus(admin)
	setSkinSetting("1",'AutoViewoff',"false")
	print printfirst + "ActivateWindow_LV" + printpoint + space + "addon" + space2 + addon + space + "containernumitems" + space2 + containernumitems + space + "count" + space2 + str(count)
	if "7" in printpoint: return "ok"
	elif "5" in printpoint: return "ok2"
	else: return ""
	
def ViewSetFocus(admin):
	containerviewmode = xbmc.getInfoLabel('Container.Viewmode')
	if containerviewmode == "addonsPT" or containerviewmode == "GeneralPT": viewmode = 50
	elif containerviewmode == "romPT": viewmode = 55
	elif containerviewmode == "IconsPT": viewmode = 58
	elif containerviewmode == "MoviesPT": viewmode = 57
	else: viewmode = ""
	if viewmode != "": xbmc.executebuiltin('Control.SetFocus('+ str(viewmode) +')')
	
	if admin: print printfirst + "ViewSetFocus" + space + "containerviewmode" + space2 + containerviewmode + space + "viewmode" + space2 + str(viewmode)


def printlog(title="", printpoint="", text="", level=0, option=""):
	exe = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	if level == 0:
		if admin and not admin2 and admin3: exe = 0
	elif level == 1:
		if admin and admin2 and admin3: exe = 1
	elif level == 2:
		if admin and not admin2: exe = 2
	elif level == 3:
		if admin: exe = 3
	
	if exe != "":
		print printfirst + title + '_LV' + printpoint + space + str(text)

def killall(admin, custom=""):
	customgui = xbmc.getInfoLabel('Skin.HasSetting(CustomGUI)')
	CloseSession()
	'''custom: ""=Just kill | "1"=Reload | "2"=Restore from gui1 | "3"=Restore from gui2'''
	name = 'killall' ; extra = "" ; TypeError = ""
	target = guisettings_file
	if "1" in custom and not customgui:
		import shutil
		from shared_modules4 import *
		x = os.path.join(addondata_path,'skin.htpt', '')
		if not os.path.exists(x): os.mkdir(x)
		if not os.path.exists(skin_userdata_path): os.mkdir(skin_userdata_path)
		source = guisettings4_file
		shutil.copyfile(guisettings_file, source)
		guiset(admin, guiread="")
		'''---------------------------'''
	elif "2" in custom: source = guisettings2_file
	elif "3" in custom: source = guisettings3_file
	else:
		source = ""
	
	print printfirst + name + '_LV' + space + 'custom' + space2 + str(custom) + space + 'customgui' + space2 + str(customgui) + newline +\
	'target' + space2 + str(target)
	
	if systemplatformandroid:
		try:
			if "1" in custom or "2" in custom or "3" in custom: extra = ''+extra+' & cp -rf '+source+' '+target+'' ; notification('1','2','',3000)
			'''---------------------------'''
			if "f" in custom:
				xbmcexe_path = 'adb shell am start -a org.xbmc.kodi'
				extra = ''+extra+' & sleep 1 & '+xbmcexe_path+''
			elif "r" in custom: extra = ''+extra+' & sleep1 & reboot' #am broadcast android.intent.action.ACTION_SHUTDOWN 
			elif "s" in custom: extra = ''+extra+' & sleep1 & reboot -p'
			'''---------------------------'''
			#killc = "adb shell ps | grep org.xbmc | awk '{print $2}' | xargs adb shell kill"
			killc = "adb shell ps | grep org.xbmc | awk '{print $2}' | xargs adb shell killall -9"
			#terminal(''+killc+' '+extra+'',name + space3 + custom) #adb shell am force-stop org.xbmc.kodi
			terminal('killall -9 org.xbmc.kodi '+extra+'',name + space3 + custom) #adb shell am force-stop org.xbmc.kodi
			
		except Exception, TypeError: print printfirst + 'killall' + space + "TypeError" + space2 + str(TypeError)
		if 1 + 1 == 3:
			
			#os.chdir('/storage/emulated/0/Android/data/org.xbmc.kodi/')
			#os.system('adb shell am force-stop org.xbmc.kodi')
			#try: os.system('adb shell am force-stop org.xbmc.kodi')
			#except: pass
			try: os.system('killall Kodi')
			except: pass
			try: os.system('killall -9 kodi.bin')
			except: pass
			try: os.system('killall XBMC')
			except: pass
			try: os.system('killall -9 xbmc.bin')
			except: pass
			
	elif systemplatformlinux or systemplatformlinuxraspberrypi:
		try:
			if "1" in custom or "2" in custom or "3" in custom: extra = '& sleep 1 & cp -rf '+source+' '+target+''
			'''---------------------------'''
			if "f" in custom: pass
			elif "r" in custom: extra = ''+extra+' && sleep 2 && reboot'
			elif "s" in custom: extra = ''+extra+' && sleep 2 && poweroff'
			'''---------------------------'''
			terminal('killall -9 kodi.bin '+extra+'',name + space3 + custom)
		except Exception, TypeError: print printfirst + 'killall' + space + "TypeError" + space2 + str(TypeError)
	
	elif systemplatformwindows:
		try:
			if '1' in custom or '2' in custom or '3' in custom: extra = '& copy "'+source+'" "'+target+'" /V /Y >NUL'
			'''---------------------------'''
			if "f" in custom:
				xbmcexe_path = os.path.join(xbmc_path, 'Kodi.exe')
				if os.path.exists(xbmcexe_path): xbmcexe_path = '"' + xbmcexe_path + '"'
				else: xbmcexe_path = '"C:\Program Files (x86)\Kodi\Kodi.exe"'
				extra = ''+extra+' & timeout 1 & '+xbmcexe_path+''
			elif "r" in custom:
				if admin3: extra = ''+extra+' && timeout 1 && shutdown -r & shutdown -a'
				else: extra = ''+extra+' & timeout 1 & shutdown -r'
				'''---------------------------'''
			elif "s" in custom:
				if admin3: extra = ''+extra+' & timeout 1 & shutdown -s & shutdown -a'
				else: extra = ''+extra+' & timeout 1 & shutdown -s'
				'''---------------------------'''
			terminal('TASKKILL /im Kodi.exe /f '+extra+'',name + space3 + custom)
		except Exception, TypeError: print printfirst + 'killall' + space + "TypeError" + space2 + str(TypeError)
		
		
		try:
			os.system('@ECHO off')
			os.system('tskill XBMC.exe')
		except: pass
		
		try:
			os.system('@ECHO off')
			os.system('TASKKILL /im XBMC.exe')
		except: pass
		try:
			os.system('@ECHO off')
			os.system('TASKKILL /im XBMC.exe /f')
		except: pass
				
	elif systemplatformosx:
		try: os.system('killall -9 XBMC')
		except: pass
		try: os.system('killall -9 Kodi')
		except: pass
	
	
	if 'q' in custom: xbmc.executebuiltin('Quit')
	elif 'f' in custom: xbmc.executebuiltin('RestartApp')
	elif 's' in custom:
		if not admin3: xbmc.executebuiltin('XBMC.Powerdown()')
	elif 'r' in custom:
		xbmc.executebuiltin('XBMC.Reset()')

def CloseSession():
	libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
	libraryisscanningmusic = xbmc.getCondVisibility('Library.IsScanningMusic')
	playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
	if libraryisscanningvideo:
		xbmc.executebuiltin('UpdateLibrary(video)')
		notification("Library Update Stop","...","",3000)
		xbmc.sleep(4000)
		
	elif libraryisscanningmusic:
		xbmc.executebuiltin('UpdateLibrary(music)')
		notification("Library Update Stop","...","",3000)
		xbmc.sleep(4000)
	
	if playerhasvideo:
		xbmc.executebuiltin('Action(Stop)')
		if playerhasvideo: notification("Video Stop","...","",1000)
		xbmc.sleep(2000)