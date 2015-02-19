import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon

getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName           = xbmcaddon.Addon().getAddonInfo("name")

'''OTHERS'''
xbmc.sleep(2000)
import datetime
printfirst = addonName + ": !@# "
space = " "
space2 = ": "
admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
systemplatformwindows = xbmc.getCondVisibility('system.platform.windows')

def bash(bashCommand,bashname):
	connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
	connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
	connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
	'''run BASH commands'''
	if not systemplatformwindows:
		#xbmc.sleep(40)
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		if bashname == "Connected":
			if admin: print printfirst + space + bashname + space2 + output
			'''1 packets transmitted, 0 packets received, 100% packet loss'''
			'''1 packets transmitted, 1 packets received, 0% packet loss
			   round-trip min/avg/max = 70.325/70.325/70.325 ms'''
			if ("1 packets received" or "0% packet loss") in output:
				if not connected: xbmc.executebuiltin('Skin.ToggleSetting(Connected)')
			else:
				print printfirst + space + "disconnected!"
				if connected: xbmc.executebuiltin('Skin.ToggleSetting(Connected)')
		if bashname == "Connected2":
			xbmc.executebuiltin('Skin.SetString(Test,'+ output +')')
			if not "packets:0" in output and "inet addr" in output:
				if not connected2: xbmc.executebuiltin('Skin.ToggleSetting(Connected2)')
			else:
				if connected2: xbmc.executebuiltin('Skin.ToggleSetting(Connected2)')
		if bashname == "Connected3":
			xbmc.executebuiltin('Skin.SetString(Test,'+ output +')')
			if not "packets:0" in output and "inet addr" in output:
				if not connected3: xbmc.executebuiltin('Skin.ToggleSetting(Connected3)')
			else:
				if connected3: xbmc.executebuiltin('Skin.ToggleSetting(Connected3)')
		'''ERROR 1020'''
		if bashname == "GUI1" and not "<skin>skin.htpt</skin>" in output:
			xbmc.executebuiltin('Notification($LOCALIZE[257]: 1020,$LOCALIZE[79505],2000)')
			os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copyskin.sh')

def dialogyesno(heading,line1):
	'''------------------------------
	---DIALOG-YESNO------------------
	------------------------------'''
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	returned = 'skip'
	if dialog.yesno(heading,line1): returned = 'ok'
	
	print printfirst + heading + "( " + returned + " )"
	return returned
	'''---------------------------'''
	
def dialogok(heading,line1,line2,line3):
	'''------------------------------
	---DIALOG-OK---------------------
	------------------------------'''
	dialog = xbmcgui.Dialog()
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	if '$LOCALIZE' in line2 or '$ADDON' in line2: line2 = xbmc.getInfoLabel(line2)
	if '$LOCALIZE' in line3 or '$ADDON' in line3: line3 = xbmc.getInfoLabel(line3)
	heading = str(heading)
	line1 = str(line1)
	line2 = str(line2)
	line3 = str(line3)
	dialog.ok(heading,line1,line2,line3)
	
	print printfirst + heading + space2 + line1 + space2 + line2 + space2 + line3
	'''---------------------------'''
	
def updateskin(run):
	'''check for skin update'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	htptv = xbmc.getInfoLabel('Skin.String(HTPTv)')
	htptc = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)')
	htptu = xbmc.getInfoLabel('Skin.HasSetting(HTPTu)')
	if not systemplatformwindows: log = open('/storage/.kodi/temp/kodi.log', 'r')
	elif systemplatformwindows: log = open('Z:\kodi.log', 'r')
	file = log.read()
	count = 0
	while count < 10 and not "FileManager: copy https://raw.githubusercontent.com/htpthtpt/htpt/master/skin.htpt/skin.htpt" in file and not xbmc.abortRequested:
		xbmc.sleep(1000)
		validationstartup('run')
		count += 1
		countS = str(count)
		if admin: xbmc.executebuiltin('Notification(Admin,UpdateSkin ('+ countS +'),1000)')
		if not systemplatformwindows: log = open('/storage/.kodi/temp/kodi.log', 'r')
		elif systemplatformwindows: log = open('Z:\kodi.log', 'r')
		file = log.read()
	log.close()
	count = 0
	while count < 10 and "FileManager: copy https://raw.githubusercontent.com/htpthtpt/htpt/master/skin.htpt/skin.htpt" in file and not xbmc.abortRequested:
		xbmc.sleep(1000)
		count += 1
		if count == 1:
			xbmc.executebuiltin('Notification($LOCALIZE[79200] '+ htptc +'),$LOCALIZE[31407],7000)')
			heading = xbmc.getInfoLabel('$LOCALIZE[79200]') + ' ' + htptc
			dialogok(heading, '$LOCALIZE[31407]', "", "")
		if not htptu: xbmc.executebuiltin('Skin.ToggleSetting(HTPTu)')
		#if count == 10: xbmc.executebuiltin('dialog.close(okdialog)')
			
	if htptv != htptc and not htptu:
		if admin: xbmc.executebuiltin('Notification(Admin,HTPTu on (2),1000)')
		xbmc.executebuiltin('Skin.ToggleSetting(HTPTu)')
	if "FileManager: copy http://raw.github.com/lambda81/lambda-repo/master/plugin.video.genesis/" in file:
		xbmc.executebuiltin('Notification($LOCALIZE[75000],$LOCALIZE[31407],2000)')
		xbmc.sleep(1000)
def htptv(admin,systemidle3,playerhasvideo):
	if systemidle3 and not playerhasvideo:
		htptv = xbmc.getInfoLabel('Skin.String(HTPTv)')
		htptc = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)')
		htptu = xbmc.getInfoLabel('Skin.HasSetting(HTPTu)')
		validation2 = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION2)')
		if htptu and htptv != htptc and not validation2:
			htptv = xbmc.getInfoLabel('Skin.String(HTPTv)')
			htptc = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)')
			message1 = xbmc.getInfoLabel('$LOCALIZE[79201]') + ' ' + htptc
			if not systemplatformwindows: log = open('/storage/.kodi/addons/skin.htpt/changelog.txt', 'r')
			elif systemplatformwindows: log = open('Z:\\addons\\skin.htpt\\changelog.txt', 'r')
			message2 = log.read()
			log.close()
			xbmc.executebuiltin('RunScript(script.toolbox,info=textviewer,header='+ message1 +',text='+ message2 +')')
			xbmc.executebuiltin('Skin.SetString(MessagesChangeLog,'+ message2 +')')
			if admin: print printfirst + "htptv" + space2 + message2
			xbmc.executebuiltin('Skin.ToggleSetting(HTPTu)')
			#dialog = xbmcgui.Dialog()
			#dialog.ok(message1,message2)
			xbmc.executebuiltin('Skin.SetString(HTPTv,'+ htptc +')')
def trial(run,admin):
	trial = xbmc.getInfoLabel('Skin.HasSetting(Trial)')
	trial2 = xbmc.getInfoLabel('Skin.HasSetting(Trial2)')
	trialdate = xbmc.getInfoLabel('Skin.String(TrialDate)')
	trialdate2 = xbmc.getInfoLabel('Skin.String(TrialDate2)')
	trialdate2p = xbmc.getInfoLabel('$LOCALIZE[70000]')
	trialstr = xbmc.getInfoLabel('$LOCALIZE[70001]')
	verrorstr = xbmc.getInfoLabel('$VAR[VERROR]')
	if trialdate and trial:
		if verrorstr == 'NONE':
			dialog = xbmcgui.Dialog()
			if trialdate2 == trialdate2p and trialdate == xbmc.getInfoLabel('System.Date(DD-MM-YY)') and not trial2:
				'''yes'''
				if admin: xbmc.executebuiltin('Notification(Admin,trialdate2 == trialdate2p,1000)')
				'''get date'''
				timenow = datetime.date.today()
				timenow2 = timenow.strftime('%d-%m-%Y')
				timeafter = timenow + datetime.timedelta(days=7)
				timeafter2 = timeafter.strftime('%d-%m-%Y')
				timenow = str(timenow)
				timeafter = str(timeafter)
				'''message'''
				message1 = "Trial Activate?"
				message2 = "Yes/No Required!"
				if dialog.yesno(message1,message2):
					xbmc.executebuiltin('Notification(Trial Start: '+ timenow2 +',Trial End: '+ timeafter2 +',5000)')
					xbmc.executebuiltin('Skin.SetString(TrialDate,'+ timenow +')')
					#xbmc.executebuiltin('Skin.SetString(TrialDate,'+ timenow2 +')')
					xbmc.executebuiltin('Skin.SetString(TrialDate2,'+ timeafter +')')
					#xbmc.executebuiltin('Skin.SetString(TrialDate2,'+ timeafter2 +')')
					xbmc.executebuiltin('Skin.SetString(ID9,'+ trialstr +')')
					if not trial2: xbmc.executebuiltin('Skin.ToggleSetting(Trial2)')
			if trialdate2 != trialdate2p or trial2:
				'''!!!'''
				if admin: xbmc.executebuiltin('Notification(Admin,trialdate2 != trialdate2p,1000)')
				'''message'''
				message1 = "Trial Activate?"
				message2 = "Please Choose NO"
				if dialog.yesno(message1,message2):
					xbmc.executebuiltin('Notification(Trial Failed!,Please Contact HTPT support!,5000)')
					xbmc.executebuiltin('Skin.SetString(ID9,)')
					xbmc.executebuiltin('Skin.SetString(ID7,'+ trialstr +')')
					xbmc.executebuiltin('Skin.SetString(ID3,'+ trialstr +')')
				if trial2: xbmc.executebuiltin('Skin.ToggleSetting(Trial2)')
		else:
			if admin: xbmc.executebuiltin('Notification(Admin,verrorstr != NONE,2000)')
	if trial:
		'''trial detected'''
		xbmc.executebuiltin('Skin.ToggleSetting(Trial)')
		if verrorstr != 'NONE': xbmc.executebuiltin('Skin.SetString(ID9,'+ trialstr +')')
	if not trial and not trial2:
		'''regular'''
		if admin: xbmc.executebuiltin('Notification(Admin,regular,1000)')
		if trialdate: xbmc.executebuiltin('Skin.SetString(TrialDate,)')
		if trialdate2: xbmc.executebuiltin('Skin.SetString(TrialDate2,)')
	if trial2:
		'''strings'''
		trialstr1 = xbmc.getInfoLabel('$LOCALIZE[79211]')
		trialstr2 = xbmc.getInfoLabel('$LOCALIZE[79081]')
		
		'''get date'''
		timenow = datetime.date.today()
		timenow2 = timenow.strftime('%d-%m-%Y')
		timeafter = timenow + datetime.timedelta(days=7)
		timeafter2 = timeafter.strftime('%d-%m-%Y')
		timenow = str(timenow)
		timeafter = str(timeafter)
		if admin and trialdate2 < timenow: xbmc.executebuiltin('Notification(Admin,trial end (1),2000)')
		elif admin and trialdate2 < trialdate: xbmc.executebuiltin('Notification(Admin,trial end (2),2000)')
		elif admin and timeafter < trialdate2: xbmc.executebuiltin('Notification(Admin,trial end (3),2000)')
		elif admin and timenow < trialdate: xbmc.executebuiltin('Notification(Admin,trial end (4),2000)')
		if trialdate2 < timenow or trialdate2 < trialdate or timeafter < trialdate2 or timenow < trialdate:
			'''trial end'''
			xbmc.executebuiltin('Skin.SetString(ID3,TrailEnd)')
			xbmc.executebuiltin('Skin.SetString(ID9,TrailEnd)')
			trialendstr = xbmc.getInfoLabel('$LOCALIZE[79115] $LOCALIZE[79119]')
			trialendstr2 = xbmc.getInfoLabel('$LOCALIZE[79203]')
			dialog = xbmcgui.Dialog()
			message1 = trialendstr + '!'
			message2 = trialendstr2 + '.' + '[CR]' '0547393531'
			if dialog.yesno(message1,message2):
				xbmc.executebuiltin('Notification('+ trialstr1 +','+ trialstr2 +',5000)')
			else:
				xbmc.executebuiltin('Notification('+ trialstr1 +','+ trialstr2 +',5000)')
		if timeafter < trialdate2 or timenow < trialdate:
			xbmc.executebuiltin('Notification(FORMATING DEVICE, PLEASE WAIT...,10000)')
			xbmc.executebuiltin('Skin.ToggleSetting(Trial2)')
			xbmc.executebuiltin('Skin.SetString(ID5,000)')
			xbmc.executebuiltin('Skin.SetString(ID7,000)')


def validationstartup(admin):
	validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')
	validation5 = xbmc.getInfoLabel('Skin.String(VALIDATION5)')
	count = 0
	if validation and validation5 != '0' and not xbmc.abortRequested:
		#if admin and count == 1: xbmc.executebuiltin('Notification(Admin,validationstartup)')
		xbmc.sleep(1000)
		startup_a = xbmc.getCondVisibility('Window.IsActive(Startup.xml)')
		skinsettings = xbmc.getCondVisibility('Window.IsVisible(SkinSettings.xml)')
		loginscreen = xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)')
		loginscreen_p = xbmc.getCondVisibility('Window.Previous(LoginScreen.xml)')
		validation = xbmc.getInfoLabel('Skin.HasSetting(VALIDATION)')
		validation5 = xbmc.getInfoLabel('Skin.String(VALIDATION5)')
		playerhasmedia = xbmc.getInfoLabel('Player.HasMedia')
		htptlogo = xbmc.getInfoLabel('Player.Filename') == "playHTPT.mp4"
		if not startup_a and not loginscreen and not loginscreen_p and not skinsettings and not htptlogo: xbmc.executebuiltin('ReplaceWindow(Startup.xml)')
		if playerhasmedia and not htptlogo:
			xbmc.executebuiltin('Action(Close)')
			xbmc.executebuiltin('Notification(HTPT AUTHENTICATION FAILED!,FOR SUPPORT: [COLOR Yellow]infohtpt@gmail.com[/COLOR],10000,icons/sc2.png)')

def videoplayertweak(admin,playerhasvideo):
	if playerhasvideo:
		#if admin: xbmc.executebuiltin('Notification(Admin,fix bug with subtitles (1),1000)')
		playerfolderpath = xbmc.getInfoLabel('Player.FolderPath')
		videoplayersubtitlesenabled = xbmc.getInfoLabel('VideoPlayer.SubtitlesEnabled')
		videoplayerhassubtitles = xbmc.getInfoLabel('VideoPlayer.HasSubtitles')
		'''fix bug with subtitles'''
		if videoplayerhassubtitles and videoplayersubtitlesenabled:
			fix = 'no'
			if '.sdarot.w' in playerfolderpath: fix = 'yes'
			elif xbmc.getCondVisibility('!VideoPlayer.Content(Movies)') and xbmc.getCondVisibility('!VideoPlayer.Content(Episodes)') and xbmc.getCondVisibility('IsEmpty(VideoPlayer.Year)') and xbmc.getCondVisibility('IsEmpty(VideoPlayer.Plot)') and xbmc.getCondVisibility('!SubString(Player.Title,S0)') and xbmc.getCondVisibility('!SubString(Player.Title,S1)') and xbmc.getCondVisibility('!SubString(VideoPlayer.Title,TNPB)') and xbmc.getCondVisibility('!SubString(VideoPlayer.Title,Staael)') and xbmc.getCondVisibility('!SubString(Player.Filename,YIFY)'): fix = 'yes'
			if fix == 'yes':
				if admin: xbmc.executebuiltin('Notification(Admin,fix bug with subtitles,1000)')
				xbmc.executebuiltin('Action(ShowSubtitles)')
			
		'''video osd auto close'''
		videoosd = xbmc.getCondVisibility('Window.IsVisible(VideoOSD.xml)')
		systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
		if videoosd and systemidle10:
			subtitleosdbutton = xbmc.getCondVisibility('Control.HasFocus(703)')
			if not subtitleosdbutton or not videoplayerhassubtitles:
				if admin: xbmc.executebuiltin('Notification(Admin,videoosdauto,1000)')
				xbmc.executebuiltin('Dialog.Close(VideoOSD.xml)')
			else:
				systemidle20 = xbmc.getCondVisibility('System.IdleTime(20)')
				if systemidle20: xbmc.executebuiltin('Dialog.Close(VideoOSD.xml)')
	
def memkeyboard(admin):
	smartkeyboard = xbmc.getInfoLabel('Skin.HasSetting(smartkeyboard)')
	dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
	systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
	count = 0
	while count < 400 and smartkeyboard and dialogkeyboard and not systemidle3:
		xbmc.sleep(100)
		count += 1
		dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
		systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
		input = xbmc.getInfoLabel('Control.GetLabel(312)')
		smartkeyboardh0 = xbmc.getInfoLabel('Skin.String(smartkeyboardH0)')
		if input != smartkeyboardh0:
			xbmc.executebuiltin('Skin.SetString(smartkeyboardH0,'+ input +')')
			if admin: xbmc.executebuiltin('Notification(Admin memkeyboard,'+ input +',1000)')
		#xbmc.executebuiltin('Notification(Admin memkeyboard,'+ input +',1000)')


def connectioncheck(admin,count,systemidle3):
	'''network status'''
	#systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	#systemcurrentwindow = xbmc.getInfoLabel('System.CurrentWindow')
	netsettingsbutton = (xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(108)')) or xbmc.getCondVisibility('Container(52).HasFocus(40)') or (xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(10)'))
	#xbmc.sleep(200)
	if systemidle3 and not netsettingsbutton:
		connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
		connected2 = xbmc.getInfoLabel('Skin.HasSetting(Connected2)')
		connected3 = xbmc.getInfoLabel('Skin.HasSetting(Connected3)')
		if count == 1 or ((not connected and (connected2 or connected3)) or (connected and not connected2 and not connected3)):
			bash('ifconfig wlan0',"Connected2")
			xbmc.sleep(200)
			bash('ifconfig eth0',"Connected3")
		if count > 1 and (connected2 or connected3):
			#bash('ping -W 1 -w 1 -4 -q www.google.co.il',"Connected")
			bash('ping -W 1 -w 1 -4 -q 8.8.8.8',"Connected")
			xbmc.sleep(200)
	else:
		if netsettingsbutton and admin: xbmc.executebuiltin('Notification(Admin,Connected2/3 pending...,1000)')

class startup:
	xbmc.executebuiltin('UpdateAddonRepos')
	#xbmc.executebuiltin('UpdateLocalAddons')
	trial('run',admin)
	print printfirst + "startup" + " (1) "
	if not systemplatformwindows:
		print printfirst + "startup" + " (2) "
		os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copyskin.sh')
		os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copy2.sh')
		os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copyonce.sh')
		os.system('sh /storage/.kodi/addons/service.htpt/specials/scripts/copyemu.sh')
	updateskin('run')
	print printfirst + "startup" + " (3) "
class repeat:
	updateskincheck = 'false'
	count = 0
	while not xbmc.abortRequested:
		xbmc.sleep(1000)
		admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
		systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
		if count < 10: count += 1
		elif count >= 10: count = 1
		countS = str(count)
		if admin: xbmc.executebuiltin('Skin.SetString(TimerService,'+ countS +')')
		'''actions'''
		htptv(admin,systemidle3,playerhasvideo)
		validationstartup(admin)
		videoplayertweak(admin,playerhasvideo)
		#memkeyboard(admin)
		#if count == 1:
		connectioncheck(admin,count,systemidle3)	
		if systemidle3 and not systemplatformwindows:
			'''system'''
			if count == 5 and not playerhasvideo: bash('cat /storage/.kodi/userdata/guisettings.xml',"GUI1")
	if xbmc.abortRequested:
		print printfirst + "Error 1170: AbortRequested!"
		sys.exit()
		
		
#repeat()