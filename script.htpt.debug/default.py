#!/usr/bin/python
import xbmc, sys, xbmcaddon


getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonString            = xbmcaddon.Addon().getLocalizedString

printfirst = addonName + ": !@# "
systemplatformwindows = xbmc.getCondVisibility('system.platform.windows')

'''Add-on_unicode_paths'''
#directory = dialog.browse(0, 'Title' , 'pictures').decode('utf-8')
#os.path.join(path, filename.decode('ascii'))


''''''




import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
import mimetypes, base64

def bash(bashCommand,bashname):
	'''run BASH commands'''
	import subprocess
	if not systemplatformwindows:
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		if bashname == "zip":
			if "adding: " in output or "updating: " in output or "freshening: " in output:
				returned == 'ok'
			else:
				returned == 'skip'
			print printfirst + bashname + ": " + output + " ( " + returned + " )"
			return returned
		if bashname == "ifconfig":
			print printfirst + bashname + ": " + output	
			return output
		if bashname == "df":
			print printfirst + bashname + ": " + output	
			return output
def sendMail(subject, text, *attachmentFilePaths):
    returned = 'skip'    
    gmailUser = "htptdebugout@gmail.com"
    gmailPassword = ap + bp + cp + dp + ep + fp + gp + hp
    recipient = "fixhtpt@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    for attachmentFilePath in attachmentFilePaths:
        msg.attach(getAttachment(attachmentFilePath))
    if loginscreen or custom1170 or admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 31],$ADDON[script.htpt.debug 2],1000)')
    #dialogok(addonString(10),addonString(32),"","")
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    if loginscreen or custom1170 or admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 32],$ADDON[script.htpt.debug 2],1000)')
    mailServer.ehlo()
    if loginscreen or custom1170 or admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 33],$ADDON[script.htpt.debug 2],1000)')
    mailServer.starttls()
    mailServer.ehlo()
    if loginscreen or custom1170 or admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 34],$ADDON[script.htpt.debug 2],1000)')
    mailServer.login(gmailUser, gmailPassword)	
    if loginscreen or custom1170 or admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 35],$ADDON[script.htpt.debug 2],2000)')
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    if loginscreen or custom1170 or admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 36],$ADDON[script.htpt.debug 2],1000)')
    returned = 'ok'
    mailServer.close()
    return returned
    

def getAttachment(attachmentFilePath):
    contentType, encoding = mimetypes.guess_type(attachmentFilePath)

    if contentType is None or encoding is not None:
        contentType = 'application/octet-stream'
    mainType, subType = contentType.split('/', 1)
    file = open(attachmentFilePath, 'rb')

    if mainType == 'text':
        attachment = MIMEText(file.read())
    elif mainType == 'message':
        attachment = email.message_from_file(file)
    elif mainType == 'image':
        attachment = MIMEImage(file.read(),_subType=subType)
    elif mainType == 'audio':
        attachment = MIMEAudio(file.read(),_subType=subType)
    else:
        attachment = MIMEBase(mainType, subType)

    attachment.set_payload(file.read())
    #encode_base64(attachment)
    file.close()
    attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(attachmentFilePath))
    return attachment

def dialogkeyboard(type, message1, message2, addonsetting):
	'''message1 =  ,message2 = subject'''
	keyboard = xbmc.Keyboard(message1,message2)
	keyboard.doModal()
	returned = 'skip'
	if (keyboard.isConfirmed()):
		input = keyboard.getText()
		
		if type == '1' and input != "": returned = 'ok'
		if type == '2' and input == message1: returned = 'ok'
	print printfirst + message2 + space2 + message1 + "( " + returned + " )"
	if returned == 'skip': return returned
	else:
		returned == input
		if addonsetting: setsetting(addonsetting, input)

def dialognumeric(type,heading,message1,addonsetting):
	'''type: 0 = #, 1 = DD/MM/YYYY, 2 = HH:MM, 3 = #.#.#.#, message2 = heading, message1 = content'''
	message1 = int(message1)
	try:
		if int(message1) > 001000000 and int(message1) < 9999999999: message1 = str(message1)
	except TypeError:
		message1 = 0
		message1 = str(message1)
		print printfirst + "dialognumeric " + "except TypeError (1)"
	print "dasd"
	type = int(type)
	input = xbmcgui.Dialog().numeric(type, heading, message1)
	type = str(type)
	if type == '0':
		try:
			if int(input) > 001000000 and int(input) < 9999999999: returned = 'ok'
			elif int(input) < 001000000 or int(input) > 9999999999: returned = 'skip0'
			print "testtt"
		except TypeError:
			returned = 'skip'
	#if type == '2' and input == message1: returned = 'ok'
	
	message1 = str(message1)
	print printfirst + heading + space2 + message1 + "( " + returned + " )"
	if returned == 'ok':
		returned == input
		setsetting(addonsetting, input)
	return returned
		
		
def dialogyesno(message1, message2):
	message1 = xbmc.getInfoLabel(message1)
	message2 = xbmc.getInfoLabel(message2)
	returned = 'skip'
	if dialog.yesno(message1,message2): returned = 'ok'
	
	print printfirst + message1 + "( " + returned + " )"
	return returned
	
def dialogok(heading, line1, line2, line3):
	dialog.ok(heading,line1,line2,line3)
	
def calculate(type,value,addonsetting):
	value = int(value)
	if type == '1':
		value += 1
	value = str(value)
	setsetting(addonsetting, value)

def changeset(type,value,addonsetting):
	import datetime
	timenow = datetime.date.today()
	timenow = str(timenow)
	print printfirst + value + ", " + timenow
	if type == '1':
		if value != timenow: setsetting(addonsetting, timenow)
'''variables'''
ap = "r"
bp = "o"
cp = "m"
dp = "1"
ep = "2"
fp = "3"
gp = "4"
hp = "5"
ip = "d"
jp = "D"
kp = "#"
space = " "
space2 = ": "
'''triggers'''
admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
debugbutton = xbmc.getCondVisibility('Container(50).HasFocus(5)') or (xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)') and xbmc.getCondVisibility('Container(50).HasFocus(102)'))
#systemidle40 = xbmc.getCondVisibility('System.IdleTime(40)')

loginscreen = xbmc.getCondVisibility('Window.IsVisible(LoginScreen.xml)')
custom1170 = xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)')
myprograms = xbmc.getCondVisibility('Window.IsVisible(MyPrograms.xml)')
startup = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
startup_a = xbmc.getCondVisibility('Window.IsActive(Startup.xml)')
''''''

temppath = "/storage/.kodi/temp"
logfile = "/storage/.kodi/temp/htptlog.zip"
logfile0 = "/storage/.kodi/temp/kodi.log"
logfilewindows = "z:\htpt.log"
'''ID = USERNAME EN , ID1 = USERNAME HE, ID2 = INSTALLATION DATE, ID3 = WARRENTY END, ID4 = ADDRESS, ID5 = TELEPHONE NUMBER, ID8 = TECHNICAL NAME, ID10 = HTPT'S MODEL'''
ID = xbmc.getInfoLabel('Skin.String(ID)')
ID1 = xbmc.getInfoLabel('Skin.String(ID1)')
ID2 = xbmc.getInfoLabel('Skin.String(ID2)')
ID3 = xbmc.getInfoLabel('Skin.String(ID3)')
ID4 = xbmc.getInfoLabel('Skin.String(ID4)')
ID5 = xbmc.getInfoLabel('Skin.String(ID5)')
ID8 = xbmc.getInfoLabel('Skin.String(ID8)')
ID10 = xbmc.getInfoLabel('Skin.String(ID10)')
''''''
IDname = xbmc.getInfoLabel('$LOCALIZE[1014]')
ID2name = xbmc.getInfoLabel('$LOCALIZE[70010]')
ID3name = xbmc.getInfoLabel('$LOCALIZE[70011]')
ID4name = xbmc.getInfoLabel('$LOCALIZE[19115]')
ID5name = xbmc.getInfoLabel('$LOCALIZE[75006]')
ID8name = xbmc.getInfoLabel('$LOCALIZE[70013]')
ID10name = xbmc.getInfoLabel('$LOCALIZE[79031]')
'''ADDON SETTINGS'''
service_call = getsetting('service_call')
service_call_no = getsetting('service_call_no')
startup_no = getsetting('startup_no')
lastdate = getsetting('lastdate')
unauthorized_no = getsetting('unauthorized_no')
username = getsetting('username')
address = getsetting('address')
telephone = getsetting('telephone')
curtrigger = getsetting('curtrigger')
issue_description = getsetting('issue_description')
if admin: xbmc.executebuiltin('Notification(admin,'+ curtrigger +',2000)')
'''addonString'''


def subject(admin):
	'''subject'''
	if debugbutton:
		subject = addonString(11) + ": " + ID + "(" + service_call_no + ")"
		print printfirst + "subject: " + addonString(11).encode('utf-8') + ": " + ID + " (" + service_call_no + ")"
	elif myprograms and not systemplatformwindows and not admin:
		subject = addonString(13) + ": " + ID + "(" + unauthorized_no + ")"
		print printfirst + "subject: " + addonString(13).encode('utf-8') + ": " + ID + " (" + unauthorized_no + ")"
	elif curtrigger != "":
		if curtrigger == '12':
			'''startup'''
			subject = addonString(12) + ": " + ID + " (" + startup_no + ")"
			print printfirst + "subject: " + addonString(12).encode('utf-8')
			calculate('1',startup_no,'startup_no')
		elif curtrigger == '13':
			'''unauthorized'''
			subject = addonString(13) + ": " + ID + " (" + unauthorized_no + ")"
			print printfirst + "subject: " + addonString(13).encode('utf-8')
			calculate('1',unauthorized_no,'unauthorized_no')
		elif curtrigger == '16':
			'''verrorstr != '7000' and verrorstr != 'NONE'''
			subject = addonString(16) + ": " + ID + " (" + error_no + ")"
			print printfirst + "subject: " + addonString(16).encode('utf-8')
			calculate('1',error_no,'error_no')
		elif curtrigger == '14':
			'''systemuptime12 & startup'''
			subject = addonString(14) + ": " + ID
			print printfirst + "subject: " + addonString(14).encode('utf-8')
		elif curtrigger == '17':
			'''lastdate != timenow & systemuptime12'''
			subject = addonString(17) + ": " + ID
			print printfirst + "subject: " + addonString(17).encode('utf-8')
			changeset('1',lastdate,'lastdate')
		elif curtrigger == '15':
			'''systemuptime120'''
			subject = addonString(15) + ": " + ID
			print printfirst + "subject: " + addonString(15).encode('utf-8')
		setsetting('curtrigger', "")
	returned = subject
	return returned

def content(admin):
	'''content'''
	if debugbutton:
		issue_description = getsetting('issue_description')
		#issue_description = issue_description.decode('utf-8')
		#xbmc.executebuiltin('Skin.SetString(issue_description,'+ issue_description +')')
		#xbmc.sleep(1000)
		#issue_description = xbmc.getInfoLabel('Skin.String(issue_description)')
		#issue_description = issue_description.encode('utf-8')
		#print issue_description
		#issue_description = issue_description.decode('utf-8')
		#issue_description = issue_description.encode('ascii')
		#issue_description = issue_description.decode("iso-8859-8")
		#issue_description = issue_description.encode("cp1255")
		#1#issue_description = issue_description.encode("cp862")
		#2#issue_description = issue_description.encode("iso-8859-8")
		#3#issue_description = issue_description.encode("cp1255")
		#4#issue_description = issue_description.encode("cp424")
		#5$issue_description = issue_description.encode("cp856")
	elif not debugbutton: issue_description = ""
	''''''
	if xbmc.getCondVisibility('System.HasAddon(service.htpt)'): htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)') + "+"
	elif xbmc.getCondVisibility('!System.HasAddon(service.htpt)'): htptversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)') + "-"
	buildversion = xbmc.getInfoLabel('System.BuildVersion')
	htptdebugversion = xbmc.getInfoLabel('System.AddonVersion(script.htpt.debug)')
	htptserviceversion = xbmc.getInfoLabel('ystem.AddonVersion(service.htpt)')
	htpthelpversion = xbmc.getInfoLabel('System.AddonVersion(service.htpt.help)')
	''''''
	localip = xbmc.getInfoLabel('Network.IPAddress')
	gateway = xbmc.getInfoLabel('Network.GatewayAddress')
	dhcpaddress = xbmc.getInfoLabel('Network.DHCPAddress')
	systemuptime2 = xbmc.getInfoLabel('System.Uptime') + " / " + xbmc.getInfoLabel('System.TotalUptime') 
	freespace2 = xbmc.getInfoLabel('System.TotalSpace') + " / " + xbmc.getInfoLabel('System.FreeSpacePercent')
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	screenresolution = xbmc.getInfoLabel('ScreenResolution')
	mac = xbmc.getInfoLabel('Network.MacAddress') + "( " + xbmc.getInfoLabel('Skin.String(MAC1)') + " / " + xbmc.getInfoLabel('Skin.String(MAC2)') + " )"
	
	ifconfig = bash('ifconfig -a',"ifconfig")
	#dfterminal = 'df -k /storage | awk {'print $6,$5,$4'}'
	df = bash('df -k /storage',"df")
	
	#? = xbmc.getInfoLabel('')
	#? = xbmc.getInfoLabel('')
	#? = xbmc.getInfoLabel('')
	#? = xbmc.getInfoLabel('')
	#? = xbmc.getInfoLabel('')
	content = '''
	USERNAME:          %s
	USER WRITE:        %s
	---------------------
	INSTALLATION DATE: %s
	TEL:               %s
	TECHNICAL NAME:    %s
	HTPT MODEL:        %s
	---------------------
	HTPT VER:          %s
	BUILD VER:         %s
	HTPT DEBUG VER:    %s
	HTPT SERVICE VER:  %s
	HTPT HELP VER:     %s
	---------------------
	LOCAL IP:          %s
	GATEWAY:           %s
	DHCPADDRESS:       %s
	SYSTEM UP TIME:    %s
	FREE SPACE:        %s
	---------------------
	CURRENT CONTROL:   %s
	SCREEN RESOLUTION: %s
	MAC(1=lan/2=wlan): %s
	IFCONFIG:          %s
	DF:                %s
	---------------------
	''' % (ID, issue_description, ID2, ID5, ID8, ID10, htptversion, buildversion, htptdebugversion, htptserviceversion, htpthelpversion, localip, gateway, dhcpaddress, systemuptime2, freespace2, systemcurrentcontrol, screenresolution, mac, ifconfig, df)

							#xbmc.executebuiltin('AlarmClock(HTPTCHECK: '+ idstr +'*0 | '+ id1str +'*1 | '+ id2str +'*2 | '+ id3str +'*3 | '+ id4str +'*4 | '+ id5str +'*5 | '+ id6str +'*6 | '+ id7str +'*7 | '+ id8str +'*8 | '+ id9str +'*9 | '+ id10str +'*10 | '+ mac1str +'*MAC1 | '+ mac2str +'*MAC2 | '+ mac3str +'*MAC3 | '+ macaddress +'*MAC | '+ systemtotaluptime +'*TOTALUPTIME | '+ verrorstr +'*VERROR | ,Action(Stop),0,silent)')
							
	if admin: print printfirst + " content: " + content
	 
	returned = content
	return returned
''''''
if debugbutton:
	import xbmcgui
	dialog = xbmcgui.Dialog()
	
	'''username prompt'''
	returned = dialogkeyboard('1',ID1,IDname,'username')
	if returned == 'skip': xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[75002],2000)')
	else:
		'''address prompt'''
		if address != "": returned = dialogkeyboard('1',address,ID4name,'address')
		else:
			returned = dialogkeyboard('1',ID4,ID4name,'address')
		if returned == 'skip': xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[75002],2000)')
		else:
			'''telephone prompt'''
			try:
				if int(telephone) > 001000000 and int(telephone) < 9999999999: returned = dialognumeric('0',ID5name,telephone,"telephone")
				elif int(ID5) > 001000000 and int(ID5) < 9999999999: returned = dialognumeric('0',ID5name,ID5,"telephone")
				
			except TypeError:
				returned = dialognumeric('0',ID5name,0,"telephone")
				print printfirst + "dialognumeric " + "except TypeError (2)"
			if returned == 'skip': xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[75002],2000)')
			elif returned == 'skip0': xbmc.executebuiltin('Notification($LOCALIZE[257],$ADDON[script.htpt.debug 30],2000)')
			elif returned == 'ok':
				'''issue description'''
				returned = dialogkeyboard('1',issue_description,addonString(44).encode("utf-8"),'issue_description')
				if returned == 'skip': xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[75002],2000)')
				else:
					'''send debug prompt'''
					returned = dialogyesno('$LOCALIZE[79219]','$LOCALIZE[79059]')
					if returned == 'skip': xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[31406],2000)')
					elif returned == 'ok':
						subject = subject(admin)
						content = content(admin)
						if not systemplatformwindows:
							bash('rm -r /storage/.kodi/temp/htptlog.zip && sleep 1 && zip -j9 /storage/.kodi/temp/htptlog.zip /storage/.kodi/temp/kodi.log',"zip")
							if returned == 'skip': xbmc.executebuiltin('Notification($LOCALIZE[257],COMPRESSED ZIP FAILED!,2000)')
							else:
								returned = 'skip'
								returned = sendMail(subject, content, logfile0)
						elif systemplatformwindows:
							returned = 'skip'
							returned = sendMail(subject, content, logfilewindows)
						xbmc.sleep(200)
						if returned != 'ok':
							'''mail failed'''
							print(printfirst + 'sendMail Failed!')
						else:
							'''mail sucuess'''
							print(printfirst + 'sendMail done!')
							calculate('1',service_call_no,'service_call_no')
							#dialogok($LOCALIZE[79518],
							xbmc.executebuiltin('Notification($LOCALIZE[79518],,5000)')
							
else:
	'''unknown'''
	subject = subject(admin)
	content = content(admin)
	returned = 'skip'
	if systemplatformwindows: returned = sendMail(subject, content, logfilewindows)
	elif not systemplatformwindows: returned = sendMail(subject, content, logfile0)
	if returned != 'ok':
		'''mail failed'''
		print(printfirst + 'sendMail Failed!')
	else:
		'''mail sucuess'''
		print(printfirst + 'sendMail done!')
		#if addonString(17) in subject: changeset('1',lastdate,'lastdate')
		#elif addonString(16) in subject or addonString(13) in "subject": calculate('1',unauthorized_no,'unauthorized_no')
		#elif addonString(12) in subject: calculate('1',startup_no,'startup_no')
		
		if admin: xbmc.executebuiltin('Notification($ADDON[script.htpt.debug 4],$ADDON[script.htpt.debug 3],1000)')
	
	#xbmc.executebuiltin('Notification($LOCALIZE[257],$LOCALIZE[79058],2000)')
sys.exit()
		#if admin: xbmc.executebuiltin('Notification($LOCALIZE[79518],,1000)')
		
	#xbmc.executebuiltin('Notification($LOCALIZE[79072],For Support: [COLOR Yellow]$LOCALIZE[79081][/COLOR],4000)')
	#fixhtptstr = xbmc.getInfoLabel('Skin.String(fixhtpt)')
					#if admin: xbmc.executebuiltin('Notification(Admin,'+ fixhtptstr +',1000)')
					#if fixhtptstr != "":
