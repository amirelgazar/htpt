#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon, os
from variables import *
#from variablesp import *
from shared_modules import *



def setInfo(admin):
	#addonsL = []
	#addonsL.append('script.htpt.homebuttons')
	#addonsL.append('script.htpt.debug')
	#removeaddons(addonsL,"12")
	
	'''------------------------------
	---setInfo-----------------------
	------------------------------'''
	name = 'setInfo' ; printpoint = "" ; TypeError = "" ; extra = ""
	systemmemorytotal2 = systemmemorytotal.replace("MB","") ; setsetting('Info_TotalMemory',systemmemorytotal2)

	'''---------------------------'''
	if systemplatformwindows:
		#totalspacegb = systemtotalspace
		#totalspacegb.split(' ')
		#totalspacegb = totalspacegb[0]
		#totalspacegb = CleanString(totalspacegb)
		totalspacegb = systemtotalspace
		if admin and not admin2: print printfirst + "totalspacegb" + space2 + str(totalspacegb)
		totalspacegb = totalspacegb.replace("MB","")
		totalspacegb = totalspacegb.replace(" ","")
		try:
			totalspacegb = totalspacegb.replace(localize(20161).encode('utf-8'),"")
			totalspacegb = totalspacegb.replace(localize(20161),"")
			totalspacegb = totalspacegb.replace('Total',"")
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
		
		try: totalspacegb = int(totalspacegb) / 1000
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			totalspacegb = 0
		
	elif systemplatformlinux or systemplatformlinuxraspberrypi:
		output = terminal("df -k | grep -e '/storage' | head -1 | awk {'print $2'}","total space")
		try: totalspacegb = int(output) / 1000000
		except: totalspacegb = 0
		'''---------------------------'''
	elif systemplatformandroid:
		output = terminal("df /storage/emulated/0 | head -2 | awk {'print $2'}")
		try: totalspacegb = int(output)
		except: totalspacegb = 0
	else: totalspacegb = 0
	
	
	
	totalspacegb = round(totalspacegb) ; totalspacegb = str(totalspacegb).replace(".0","")
	setsetting('Info_TotalSpace',str(totalspacegb))
	'''---------------------------'''
	
	if systemplatformwindows:
		output3 = ""
		output = terminal("wmic cpu get name","model name")
		output = CleanString(output, filter=['Name  '])
		output = output.replace("  ", " ")
		setsetting('Info_Model',output)
		'''---------------------------'''
	elif systemplatformlinux or systemplatformlinuxraspberrypi:
		output = terminal("cat /proc/cpuinfo | grep -e 'model name' | head -1 | awk {'print $4,$5,$6,$7,$8,$9,$10'}","model name")
		output = output.replace(' \n',"")
		setsetting('Info_Model',output)
		'''---------------------------'''
	elif systemplatformandroid:
		output = terminal("cat /proc/cpuinfo | grep -e 'Processor' | head -1 | awk {'print $4,$5,$6,$7,$8,$9,$10'}","model name")
		output = output.replace(' \n',"")
		setsetting('Info_Model',output)
	else: pass
	if "Intel" in Info_Model: setsetting('Info_Intel',"true")
	else: setsetting('Info_Intel',"false")
	'''---------------------------'''
	
	
	if systemplatformlinuxraspberrypi: setSkinSetting("0",'ID10',"C")
	elif "ARMv7 Processor rev 10 (v7l)" in Info_Model: setSkinSetting("0",'ID10',"C?")
	elif "Intel(R) Celeron(R) CPU N28" in Info_Model: setSkinSetting("0",'ID10',"A")
	elif totalspacegb > 700 and systemmemorytotal2 > 2000 and id10str != "B": setSkinSetting("0",'ID10',"B?")
	elif totalspacegb > 300 and systemmemorytotal2 > 1500 and id10str != "A": setSkinSetting("0",'ID10',"A?")
	elif totalspacegb > 2 and totalspacegb < 100 and id10str != "C": setSkinSetting("0",'ID10',"C?")
	#elif "Intel(R) Core(TM) i3-3120M CPU @ 2.50GHz" in Info_Model: setSkinSetting("0",'ID10',"B")
	'''---------------------------'''
	
	if systemplatformwindows:
		output = terminal('wmic cpu get SystemName','')
		output = CleanString(output, filter=['SystemName '])
		setsetting('Info_SystemName',output)
	#output = terminal('wmic cpu get SystemName','')
	#output = terminal('wmic cpu get Manufacturer','')
	
	if systemplatformlinux:
		output = terminal('bluetoothctl', "Bluetooth")
		setsetting('Info_Bluetooth', str(output))
		'''---------------------------'''
		
	print printfirst + name + "_LV" + printpoint + space2 + "totalspacegb" + space2 + str(totalspacegb)
	
def sendMail(mode, subject, text, *attachmentFilePaths):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEImage import MIMEImage
    #from email import Encoders
    TypeError = "" ; extra = "" ; gmailUser = ""
    try:
        if mode == 1 or (admin3): notification(addonString(74481), addonString_servicehtpt(10), "", 1000)
        
        if General_MailService == "1":
            mailServer = smtplib.SMTP('smtp.gmail.com', 587) #, timeout=20
            gmailUser = sendtostr
            gmailPassword = mystr
            #mailServer = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 587, timeout=20)
            #gmailUser = sendtostr14
            #gmailPassword = mystr2
            #mailServer = smtplib.SMTP('smtp.mail.com', 25, timeout=20)
            #gmailUser = sendtostr1
            #gmailPassword = mystr2
            #mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
            #gmailUser = sendtostr5
            #gmailPassword = mystr2
        elif General_MailService == "2":
			mailServer = smtplib.SMTP('smtp.gmail.com', 587) #, timeout=20
			gmailUser = sendtostr2
			gmailPassword = mystr
        elif General_MailService == "3":
            mailServer = smtplib.SMTP('smtp.gmail.com', 587) #, timeout=20
            gmailUser = sendtostr3
            gmailPassword = mystr
        elif General_MailService == "4":
            mailServer = smtplib.SMTP('smtp.gmail.com', 587)
            gmailUser = sendtostr4
            gmailPassword = mystr2
        else:
			mailServer = smtplib.SMTP('smtp.gmail.com', 587)
			gmailUser = sendtostr
			gmailPassword = mystr
			
        recipient = recipientstr
        msg = MIMEMultipart()
        msg['From'] = gmailUser
        msg['To'] = recipient
        msg['Subject'] = subject
        #text = text.decode('utf-8')
        #encoders.encode_base64(text)
        #text = text.encode('utf-8')
        msg.attach(MIMEText(text))
        for attachmentFilePath in attachmentFilePaths:
			try: msg.attach(getAttachment(attachmentFilePath))
			except Exception, TypeError: print printfirst + "sendMail" + space + "TypeError" + space2 + str(TypeError)
		
        if mode == 1 or (admin3): notification(addonString(74481), addonString(74482) % ("1","4"), "", 1000)		
        #mailServer.ehlo()
        mailServer.starttls()
        if mode == 1 or (admin3): notification(addonString(74481), addonString(74482) % ("2","4"), "", 1000)
        mailServer.ehlo()
        if mode == 1 or (admin3): notification(addonString(74481), addonString(74482) % ("3","4"), "", 1000)
        mailServer.login(gmailUser, gmailPassword)	
        if mode == 1 or (admin3): notification(addonString(74481), addonString(74482) % ("4","4"), "", 1000)
        #if mode == 1 or (admin and not admin2): notification(addonString(74481), addonString(74482) % ("5","5"), "", 1000)
        mailServer.sendmail(gmailUser, recipient, msg.as_string())
        mailServer.quit()
        if mode == 1 or admin3: notification(addonString(74483), addonString(31407), "", 2000)
        returned = 'ok'
        return returned, str(TypeError)
        '''---------------------------'''
    except Exception, TypeError:
		try: mailServer.quit()
		except: pass
		if mode == 1 or admin: notification(addonString(8).encode('utf-8'), str(TypeError), "", 2000)
		if admin: extra = extra + "gmailUser" + space2 + str(gmailUser)
		print printfirst + "sendMail" + space + "General_MailService" + space2 + str(General_MailService) + space + extra + newline + \
		"TypeError" + space2 + str(TypeError)
		if "535, '5.7.8 Username and Password not accepted." in TypeError:
			'''gmail'''
			returned = 'skip'
		elif "552," in TypeError and "5.2.3 Your message exceeded Google" in TypeError:
			'''gmail'''
			returned = 'error'
		elif "534, '5.7.14" in TypeError:
			'''gmail'''
			returned = 'skip'
		elif 'Server not connected' in TypeError:
			'''outlook'''
			returned = 'skip'
		elif 'getaddrinfo failed' in TypeError:
			returned = 'skip2'
		elif 'Connection unexpectedly closed' in TypeError:
			'''outlook'''
			returned = 'skip'
		else:
			returned = 'skip'
		'''---------------------------'''
		return returned, str(TypeError)
		
def getAttachment(attachmentFilePath):
    from email.MIMEText import MIMEText
    from email.MIMEBase import MIMEBase
    import mimetypes, base64
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
    '''---------------------------'''
	
def setGeneral_Start(admin):
	General_Start = getsetting('General_Start')
	setsetting('General_Start',timenow2S)
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	print printfirst + "setGeneral_Start" + space2 + "General_Start" + space2 + General_Start + " - " + timenow2S
	'''---------------------------'''

def SetGeneral_Pass(admin):
	General_Pass = getsetting('General_Pass')
	calculate('service.htpt.debug','General_Pass','1',"")
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	General_Pass2 = getsetting('General_Pass')
	if admin: print printfirst + "setGeneral_Pass" + space2 + "General_Pass" + space2 + General_Pass + " - " + General_Pass2 + space3
	'''---------------------------'''

def setGeneral_ScriptON2(admin):
	General_ScriptON = getsetting('General_ScriptON')
	setsetting('General_ScriptON',"false")
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "setGeneral_ScriptON2" + space2 + "General_ScriptON" + space2 + General_ScriptON
	'''---------------------------'''
	
def debugtrigger(admin, connected, General_ScriptON, General_Start, General_Pass, ModeOn_1, ModeOn_2, ModeOn_3, ModeOn_4, ModeOn_5, ModeOn_6, ModeOn_7, ModeOn_8, ModeOn_9, ModeOn_10, ModeOn_11, ModeOn_12, ModeOn_13, ModeOn_14, ModeOn_15, ModeOn_16, ModeOn_17, ModeOn_18, ModeOn_19, ModeOn_20, ModeOn_21):
	'''------------------------------
	---LOCATE-TRIGGERS---------------
	------------------------------'''
	systemplatformwindows = xbmc.getCondVisibility('System.Platform.Windows')
	startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
	currentMode = ""
	try: General_PassN = int(General_Pass)
	except: General_PassN = 0
	'''---------------------------'''

	if General_ScriptON == "false" and connected:
		'''------------------------------
		---CONTINUE----------------------
		------------------------------'''
		
		if General_PassN > 0:
			'''------------------------------
			---TRIGGERS----------------------
			------------------------------'''
			
			if ModeOn_1 == 'true':
				'''------------------------------
				---DEBUG-BUTTON------------------
				------------------------------'''
				currentMode = "ModeOn_1" + space2 + ModeOn_1
				#setsetting_custom1('service.htpt.debug','ModeOn_1',"false")
				setsetting('ModeOn_1',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=1)')
				'''---------------------------'''
			
			elif ModeOn_2 == 'true':
				'''------------------------------
				---?-------------------
				------------------------------'''
				currentMode = "ModeOn_2" + space2 + ModeOn_2
				#setsetting_custom1('service.htpt.debug','ModeOn_2',"false")
				setsetting('ModeOn_2',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=2)')
				'''---------------------------'''
			
			elif ModeOn_3 == 'true':
				'''------------------------------
				---?-------------------
				------------------------------'''
				currentMode = "ModeOn_3" + space2 + ModeOn_3
				#setsetting_custom1('service.htpt.debug','ModeOn_3',"false")
				setsetting('ModeOn_3',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=3)')
				'''---------------------------'''
			
			elif ModeOn_4 == 'true':
				'''------------------------------
				---SUSPEND-----------------------
				------------------------------'''
				currentMode = "ModeOn_4" + space2 + ModeOn_4
				#setsetting_custom1('service.htpt.debug','ModeOn_4',"false")
				setsetting('ModeOn_4',"false")
				if ModeTime_4 != "": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=4)')
				'''---------------------------'''
			
			elif ModeOn_5 == 'true':
				'''------------------------------
				---RED-DONE----------------------
				------------------------------'''
				currentMode = "ModeOn_5" + space2 + ModeOn_5
				#setsetting_custom1('service.htpt.debug','ModeOn_5',"false")
				setsetting('ModeOn_5',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=5)')
				'''---------------------------'''
			
			elif ModeOn_6 == 'true':
				'''------------------------------
				---FIX-DONE----------------------
				------------------------------'''
				currentMode = "ModeOn_6" + space2 + ModeOn_6
				#setsetting_custom1('service.htpt.debug','ModeOn_6',"false")
				setsetting('ModeOn_6',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=6)')
				'''---------------------------'''
				
			elif ModeOn_7 == 'true':
				'''------------------------------
				---SOFT-REBOOT-------------------
				------------------------------'''
				currentMode = "ModeOn_7" + space2 + ModeOn_7
				#setsetting_custom1('service.htpt.debug','ModeOn_7',"false")
				setsetting('ModeOn_7',"false")
				if ModeTime_7 != "": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=7)')
				'''---------------------------'''
			
			elif ModeOn_8 == 'true':
				'''------------------------------
				---REBOOT------------------------
				------------------------------'''
				currentMode = "ModeOn_8" + space2 + ModeOn_8
				#setsetting_custom1('service.htpt.debug','ModeOn_8',"false")
				setsetting('ModeOn_8',"false")
				if ModeTime_8 != "": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=8)')
				'''---------------------------'''
				
			elif ModeOn_9 == 'true':
				'''------------------------------
				---REGULAR-POWEROFF--------------
				------------------------------'''
				currentMode = "ModeOn_9" + space2 + ModeOn_9
				#setsetting_custom1('service.htpt.debug','ModeOn_9',"false")
				setsetting('ModeOn_9',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=9)')
				'''---------------------------'''
			
			elif ModeOn_10 == 'true':
				'''------------------------------
				---SPECIAL-POWEROFF--------------
				------------------------------'''
				currentMode = "ModeOn_10" + space2 + ModeOn_10
				#setsetting_custom1('service.htpt.debug','ModeOn_10',"false")
				setsetting('ModeOn_10',"false")
				if ModeTime_10 != "": xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=10)')
				'''---------------------------'''
				
			elif ModeOn_11 == 'true':
				'''------------------------------
				---AUTO-POWEROFF-----------------
				------------------------------'''
				currentMode = "ModeOn_11" + space2 + ModeOn_11
				#setsetting_custom1('service.htpt.debug','ModeOn_11',"false")
				setsetting('ModeOn_11',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=11)')
				'''---------------------------'''
				
			elif ModeOn_12 == 'true':
				'''------------------------------
				---STARTUP-----------------------
				------------------------------'''
				currentMode = "ModeOn_12" + space2 + ModeOn_12
				#setsetting_custom1('service.htpt.debug','ModeOn_12',"false")
				setsetting('ModeOn_12',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=12)')
				'''---------------------------'''
				
			elif ModeOn_13 == 'true':
				'''------------------------------
				---UNAUTHORIZED------------------
				------------------------------'''
				currentMode = "ModeOn_13" + space2 + ModeOn_13
				#setsetting_custom1('service.htpt.debug','ModeOn_13',"false")
				setsetting('ModeOn_13',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=13)')
				'''---------------------------'''
				
			elif ModeOn_14 == 'true' and General_PassN > 12 and startupW:
				'''------------------------------
				---UPTIME12----------------------
				------------------------------'''
				currentMode = "ModeOn_14" + space2 + ModeOn_14
				#setsetting_custom1('service.htpt.debug','ModeOn_14',"false")
				setsetting('ModeOn_14',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=14)')
				'''---------------------------'''
				
			elif ModeOn_15 == 'true' and General_PassN > 120:
				'''------------------------------
				---UPTIME120---------------------
				------------------------------'''
				currentMode = "ModeOn_15" + space2 + ModeOn_15
				#setsetting_custom1('service.htpt.debug','ModeOn_15',"false")
				setsetting('ModeOn_15',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=15)')
				'''---------------------------'''
				
			elif ModeOn_16 == 'true' and General_PassN > 5:
				'''------------------------------
				---ERROR-------------------------
				------------------------------'''
				currentMode = "ModeOn_16" + space2 + ModeOn_16
				#setsetting_custom1('service.htpt.debug','ModeOn_16',"false")
				setsetting('ModeOn_16',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=16)')
				'''---------------------------'''
				
			elif ModeOn_17 == 'true' and General_PassN > 60:
				'''------------------------------
				---UPTIME60----------------------
				------------------------------'''
				currentMode = "ModeOn_17" + space2 + ModeOn_17
				#setsetting_custom1('service.htpt.debug','ModeOn_17',"false")
				setsetting('ModeOn_17',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=17)')
				'''---------------------------'''
				
			elif ModeOn_18 == 'true':
				'''------------------------------
				---PURCHASED---------------------
				------------------------------'''
				currentMode = "ModeOn_18" + space2 + ModeOn_18
				#setsetting_custom1('service.htpt.debug','ModeOn_18',"false")
				setsetting('ModeOn_18',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=18)')
				'''---------------------------'''
				
			elif ModeOn_19 == 'true':
				'''------------------------------
				---?----------------------
				------------------------------'''
				currentMode = "ModeOn_19" + space2 + ModeOn_19
				#setsetting_custom1('service.htpt.debug','ModeOn_19',"false")
				setsetting('ModeOn_19',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=19)')
				'''---------------------------'''
				
			elif ModeOn_20 == 'true':
				'''------------------------------
				---INSTALLED---------------------
				------------------------------'''
				currentMode = "ModeOn_20" + space2 + ModeOn_20
				#setsetting_custom1('service.htpt.debug','ModeOn_20',"false")
				setsetting('ModeOn_20',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=20)')
				'''---------------------------'''
			
			elif ModeOn_21 == 'true':
				'''------------------------------
				---UNINSTALLED-------------------
				------------------------------'''
				currentMode = "ModeOn_21" + space2 + ModeOn_21
				#setsetting_custom1('service.htpt.debug','ModeOn_20',"false")
				setsetting('ModeOn_21',"false")
				xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=21)')
				'''---------------------------'''
			
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if General_PassN == 0 and admin: print printfirst + "debugtrigger" + space2 + "General_Pass" + space2 + General_Pass + space3
		if admin: print printfirst + "debugtrigger" + space2 + "currentMode" + space2 + currentMode + space3
		'''---------------------------'''
		
def getAll(mode):
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	subject = None
	content = None
	file = None
	subject2 = User_ID + space3 + space
	
	if mode == 1:
		'''------------------------------
		---DEBUG-BUTTON------------------
		------------------------------'''
		#if ModeOn_1 == "true":
		addon = 'skin.htpt'
		if os.path.exists(os.path.join(addons_path, addon, '')) and xbmc.getCondVisibility('System.HasAddon('+ addon +')'): header = addonString(79551)
		else: header = 'SERVICE CALL RECEIVED!'
		subject = subject2 + header + " (" + Sum_1 + ")"
		content = content0u + content1 + content3 + content4 + content5 + content19 + content20
		file = file1
		'''---------------------------'''
	
	elif mode == 2:
		'''------------------------------
		---?-------------------
		------------------------------'''
		subject = subject2 + addonString(79552) + " (" + Sum_2 + ")"
		content = content0 + content1
		file = file1
		'''---------------------------'''
		
	elif mode == 3:
		'''------------------------------
		---?-------------------
		------------------------------'''
		subject = subject2 + addonString(79553) + " (" + Sum_3 + ")"
		content = content0 + content1
		file = file1
		'''---------------------------'''
	
	elif mode == 4:
		'''------------------------------
		---SUSPEND-----------------------
		------------------------------'''
		subject = subject2 + addonString(79554) % (ModeTime_4) + " (" + Sum_4 + ")"
		content = content0 + content4 + content5
		file = file1
		'''---------------------------'''
	
	elif mode == 5:
		'''------------------------------
		---RED-DONE----------------------
		------------------------------'''
		if servicehtptfix_Red_Done != "" and servicehtptfix_Red_LastDate != "":
			subject = subject2 + addonString(79555) + " (" + Sum_5 + ")"
			content = content0 + content1r + content21
			file = file1
			'''---------------------------'''
		
	elif mode == 6:
		'''------------------------------
		---FIX-DONE----------------------
		------------------------------'''
		if servicehtptfix_Fix_Done != "" and servicehtptfix_Fix_LastDate != "":
			subject = subject2 + addonString(79556) + " (" + Sum_6 + ")"
			content = content0 + content1 + content1f
			file = file1
			'''---------------------------'''
		
	elif mode == 7:
		'''------------------------------
		---SOFT-REBOOT-------------------
		------------------------------'''
		subject = subject2 + addonString(79557) + " (" + Sum_7 + ")"
		content = content0 + content1 + content3 + content4 + content5
		file = file1
		'''---------------------------'''
		
	elif mode == 8:
		'''------------------------------
		---REBOOT------------------------
		------------------------------'''
		subject = subject2 + addonString(79558) % (ModeTime_8) + " (" + Sum_8 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content19
		file = file1
		'''---------------------------'''
		
	elif mode == 9:
		'''------------------------------
		---?-----------------------------
		------------------------------'''
		subject = subject2 + addonString(79559) + " (" + Sum_9 + ")"
		content = content0 + content3 + content4 + content5 + content9 + content10 + content11
		file = file1
		'''---------------------------'''
		
	elif mode == 10:
		'''------------------------------
		---POWEROFF----------------------
		------------------------------'''
		subject = subject2 + addonString(79560) + space + ModeTime_10 + " (" + Sum_10 + ")"
		content = content0 + content3 + content4 + content5 + content9 + content10 + content11 + content19
		if datenowS in ModeTime_10: file = file2
		else: file = file1
		'''---------------------------'''
		
	elif mode == 11:
		'''------------------------------
		---AUTO-POWEROFF-----------------
		------------------------------'''
		subject = subject2 + addonString(79561) + " (" + Sum_11 + ")"
		content = content0 + content3 + content4 + content5 + content9 + content10 + content11 + content19
		file = file1
		'''---------------------------'''
			
	elif mode == 12:
		'''------------------------------
		---STARTUP-----------------------
		------------------------------'''
		subject = subject2 + addonString(79562) + space + General_Start + " (" + Sum_12 + ")"
		content = content0 + content1 + content3 + content4 + content6 + content19
		file = file2
		'''---------------------------'''
		
	elif mode == 13:
		'''------------------------------
		---UNAUTHORIZED------------------
		------------------------------'''
		subject = subject2 + addonString(79563) + " (" + Sum_13 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content20
		file = file1
		'''---------------------------'''
		
	elif mode == 14:
		'''------------------------------
		---UPTIME12----------------------
		------------------------------'''
		subject = subject2 + addonString(79564) + " (" + Sum_14 + ")"
		content = content0 + content3 + content4 + content6 + content19
		file = file1
		'''---------------------------'''

	elif mode == 15:
		'''------------------------------
		---UPTIME120---------------------
		------------------------------'''
		subject = subject2 + addonString(79565) + " (" + Sum_15 + ")"
		content = content0 + content3 + content4 + content9 + content10 + content11 + content19
		file = file1
		'''---------------------------'''
		
	elif mode == 16:
		'''------------------------------
		---ERROR-------------------------
		------------------------------'''
		subject = subject2 + addonString(79566) % ("?") + " (" + Sum_16 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content19 + content20
		file = file1
		'''---------------------------'''
		
	elif mode == 17:
		'''------------------------------
		---UPTIME60----------------------
		------------------------------'''
		subject = subject2 + addonString(79567) + " (" + Sum_17 + ")"
		content = content0 + content1 + content4 + content5 + content20
		file = file1
		'''---------------------------'''
	
	elif mode == 18:
		'''------------------------------
		---PURCHASED---------------------
		------------------------------'''
		subject = subject2 + addonString(79568) + " (" + Sum_18 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content20
		file = file1
		'''---------------------------'''
	
	elif mode == 19:
		'''------------------------------
		---VERSION-UPDATED---------------
		------------------------------'''
		subject = subject2 + addonString(79569) + " (" + Sum_19 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content20
		file = file1
		'''---------------------------'''
	
	elif mode == 20:
		'''------------------------------
		---INSTALLED---------------------
		------------------------------'''
		subject = subject2 + addonString(120) + " (" + Sum_20 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content6 + content19 + content20 + content21
		file = file2
		'''---------------------------'''
	
	elif mode == 21:
		'''------------------------------
		---UNINSTALLED-------------------
		------------------------------'''
		subject = subject2 + addonString(121) + " (" + Sum_21 + ")"
		content = content0 + content1 + content3 + content4 + content5 + content20
		file = file1
		'''---------------------------'''
	
	'''------------------------------
	---EXTRAS------------------------
	------------------------------'''
	
	if playerhasvideo:
		if scripthtptrefresh_General_ScriptON == "true": content = str(content) + content8
		else: content = str(content) + content7
		
	if (mode == 1 or mode == 5 or mode == 6 or mode == 19 or mode == 20):
		extra = ""
		
		for i in range(1,7):
			extra2 = ""
			if i == 1:
				if os.path.exists(guisettings_file): extra2 = "guisettings.xml:" + newline + catfile(guisettings_file)
			elif i == 2:
				if (systemplatformlinux or systemplatformlinuxraspberrypi or systemplatformandroid): Command = 'cat /proc/cpuinfo','cpuinfo'
				elif systemplatformwindows: Command = 'wmic cpu get caption, numberofcores, manufacturer, family'
				else: Command = ""
				if Command != "": extra2 = terminal(Command, 'cpuinfo')
			elif i == 3:
				if (systemplatformlinux or systemplatformlinuxraspberrypi): Command = 'df -h'
				elif systemplatformwindows: Command = 'wmic logicaldisk get name, volumename, size, description'
				elif systemplatformandroid: Command = 'df /system'
				else: Command = ""
				if Command != "": extra2 = terminal(Command, 'logicaldisk')
			elif i == 4:
				if (systemplatformlinux or systemplatformlinuxraspberrypi or systemplatformandroid): Command = 'cat /proc/meminfo'
				elif systemplatformwindows: Command = 'wmic memorychip list full'
				else: Command = ""
				if Command != "": extra2 = terminal(Command, 'memory info')
			elif i == 5:
				filepath = os.path.join(addondata_path, 'service.htpt.fix', 'settings.xml')
				if os.path.exists(filepath): extra2 = catfile(filepath)
				'''---------------------------'''
			elif i == 6 and (systemplatformlinux or systemplatformlinuxraspberrypi):
				filepath = os.path.join('/storage', 'copy.log')
				if os.path.exists(filepath): extra2 = catfile(filepath)
				'''---------------------------'''
			elif i == 7 and (systemplatformlinux or systemplatformlinuxraspberrypi):
				filepath = os.path.join('/storage', 'emulators', '')
				if os.path.exists(filepath): extra2 = terminal('find '+filepath+' -type d', "folders_count")
				'''---------------------------'''
			extra = newline + newline + str(extra) + newline + newline + str(extra2)
			'''---------------------------'''
		content = str(content) + newline + newline + str(extra)
			
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin or xbmc.getSkinDir() != 'skin.htpt':
		if subject == None: subjectS = str(subject)
		else: subjectS = str(subject.encode('utf-8'))
		try: print printfirst + "getAll" + space + "mode" + space2 + str(mode) + space + "subject" + space2 + subjectS
		except Exception, TypeError: print printfirst + "getAll" + space + "TypeError" + space2 + str(TypeError)
		'''---------------------------'''
	
	'''---------------------------'''
	return subject, content, file

def SendDebug(mode, subject, content, file):
	printpoint = "" ; TypeError = "" ; TypeError2 = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	forcemodeL = [1,2,3,5,13,16,18,19,20]
	if General_AllowDebug == "true" or mode in forcemodeL or macstr in forcemac: returned, TypeError = sendMail(mode, subject, content, file)
	else: returned = 'ok2'
	
	if returned == None: printpoint = printpoint + "6"
	elif returned == "error":
		setsetting('General_ServiceON',"false")
		#setsetting_custom1('service.htpt.debug','General_ServiceON',"false")
		printpoint = printpoint + "9"
	elif 'ok' in returned:
		printpoint = printpoint + "7"
	else: printpoint = printpoint + "6"
	
	if "6" in printpoint:
		'''------------------------------
		---PRINT-MAIL-FAILED------------
		------------------------------'''
		setsetting_custom1('service.htpt.debug','ModeOn_' + str(mode),"true")
		if not "skip2" in returned:
			printpoint = printpoint + "C"
			try:
				if int(General_MailService) >= int(General_MailService_):
					printpoint = printpoint + "D"
					General_MailService2 = 1
					setsetting('General_ServiceON',"false")
				else:
					General_MailService2 = int(General_MailService) + 1
					printpoint = printpoint + "E"
			except Exception, TypeError2: General_MailService2 = 1 ; print printfirst + "SendDebug" + space + "TypeError2" + space2 + str(TypeError2)

			#setsetting_custom1('service.htpt.debug','General_MailService', str(General_MailService2))
			setsetting('General_MailService', str(General_MailService2))
			'''---------------------------'''
		
		if mode == 1:
			if "error" in returned: pass
			elif "skip2" in returned: pass
			elif "E" in printpoint and 1 + 1 == 3:
				notification_common("2")
				SendDebug(mode, subject, content, file)
			else:
				returned = dialogyesno(addonString(8).encode('utf-8'), addonString_servicehtpt(21).encode('utf-8') + '[CR]' + str(TypeError))
				if returned == 'ok': xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=1)')
				else:
					notification(localize(16200), addonString_servicehtpt(10), "", 2000)
					setsetting('ModeOn_1',"false")
					'''---------------------------'''
	
	elif "7" in printpoint or "9" in printpoint:
		'''------------------------------
		---PRINT-MAIL-SUCUESS------------
		------------------------------'''
		if "7" in printpoint: calculate('service.htpt.debug','Sum_' + str(mode),'1',"")

		setsetting_custom1('service.htpt.debug','ModeOn_' + str(mode),"false")
		setsetting_custom1('service.htpt.debug','ModeTime_' + str(mode),"")
		'''---------------------------'''
		if mode == 1:
			setSkinSetting("0", 'ID1',User_Name)
			print printfirst + "User_Name" + space2 + User_Name + space + "User_Email" + space2 + User_Email + space + "User_Tel" + space2 + User_Tel + space 
			dialogok(addonString(9).encode('utf-8'), addonString(10).encode('utf-8') + space + localize(549) + space2 + Sum_1, localize(1014) + space2 + User_Name ,addonString(7).encode('utf-8') % (User_Issue))
			'''---------------------------'''
		
		elif mode == 5:
			'''------------------------------
			---Red_Done----------------------
			------------------------------'''
			setsetting_custom1('service.htpt.fix','Red_Done',"")
			#setsetting_custom1('service.htpt.fix','Red_LastDate',"")
			'''---------------------------'''
		
		elif mode == 6:
			'''------------------------------
			---Fix_Done----------------------
			------------------------------'''
			setsetting_custom1('service.htpt.fix','Fix_Done',"")
			#setsetting_custom1('service.htpt.fix','Fix_LastDate',"")
			'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin or xbmc.getSkinDir() != 'skin.htpt':
		if subject == None: subjectS = str(subject)
		else: subjectS = str(subject.encode('utf-8'))
		try: print printfirst + "SendDebug_LV" + printpoint + space + "mode" + space2 + str(mode) + space + "subject" + space2 + subjectS + space + "returned" + space2 + str(returned)
		except Exception, TypeError: print printfirst + "SendDebug" + space + "TypeError" + space2 + str(TypeError)
		'''---------------------------'''
		
	return printpoint
		