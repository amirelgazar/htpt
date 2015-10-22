import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon


from variables import *
from modules import *

class resetsettings:
	setsetting_custom1('service.htpt','Time_Delay',"0")
	setsetting_custom1('service.htpt','Time_Pass',"0")
	setsetting_custom1('service.htpt','Time_Shutdown',"")
	setsetting_custom1('service.htpt','General_Timer',"0")
	setsetting_custom1('service.htpt','General_ScriptON',"false")
	setsetting_custom1('service.htpt','Skin_UpdateCount',"0")
	setsetting_custom1('service.htpt','Skin_UpdateCount2',"0")
	setsetting_custom1('service.htpt','Skin_UpdateTimer',"0")
	setsetting_custom1('service.htpt','Skin_UpdateLog',"true")
	setsetting_custom1('service.htpt','Ping_Connected',"true")
				
	setSkinSetting("1",'Connected',"true")
	setSkinSetting("1",'Connected2',"true")
	setSkinSetting("1",'Connected3',"true")	
	'''---------------------------'''
		
	if datenowS == "":
		datenow, datenowS, dateafter, dateafterS, yearnow, yearnowS, daynow, daynowS, timenowS, timeow2S, timenow3S, timenow4S = refresh_datetime(admin, datenowS, timenowS)
		print printfirst + "service.py" + space + "datenowS is empty!"
	
startup(admin)
	
	
class main:
	'''------------------------------
	---SERVICE-LOOP------------------
	------------------------------'''
	setTime_Start(admin)
	updateskincheck = 'false'
	count = 0
	while 1 and not xbmc.abortRequested:
		if xbmc.getSkinDir() != 'skin.htpt':
			xbmc.sleep(20000)
		else:
			custom1000W = xbmc.getCondVisibility('Window.IsVisible(Custom1000.xml)')
			if custom1000W:
				xbmc.sleep(10000)
			else:
				'''------------------------------
				---VARIABLES---------------------
				------------------------------'''
				systeminternetstate = xbmc.getInfoLabel('System.InternetState')
				try: networkipaddress = xbmc.getInfoLabel('Network.IPAddress')
				except: print printfirst + "main_Error_" + "networkipaddress"
				connected = xbmc.getInfoLabel('Skin.HasSetting(Connected)')
				'''---------------------------'''
				TypeError = ""
				admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
				admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
				playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
				playerhasmedia = xbmc.getCondVisibility('Player.HasMedia')
				playerpaused = xbmc.getCondVisibility('Player.Paused')
				systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
				performance = xbmc.getInfoLabel('Skin.HasSetting(Performance)')
				systemidle120 = xbmc.getCondVisibility('System.IdleTime(120)') #2M
				systemidle540 = xbmc.getCondVisibility('System.IdleTime(540)') #9M
				systemidle600 = xbmc.getCondVisibility('System.IdleTime(600)') #10M
				systemidle900 = xbmc.getCondVisibility('System.IdleTime(900)') #15M
				systemidle1200 = xbmc.getCondVisibility('System.IdleTime(1200)') #20M
				systemidle300 = xbmc.getCondVisibility('System.IdleTime(300)')
				systemidle5400 = xbmc.getCondVisibility('System.IdleTime(5400)') #1.5H
				homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
				'''---------------------------'''
				getsetting         = xbmcaddon.Addon().getSetting
				setsetting         = xbmcaddon.Addon().setSetting
				General_Timer = getsetting('General_Timer')
				try: General_TimerN = int(General_Timer)
				except: General_TimerN = 0
				Time_Delay = getsetting('Time_Delay')
				try: Time_DelayN = int(Time_Delay)
				except Exception, TypeError: Time_DelayN = 0
				Time_Start = getsetting('Time_Start')
				Time_Pass = getsetting('Time_Pass')
				Time_Shutdown = getsetting('Time_Shutdown')
				htptskinversion = xbmc.getInfoLabel('System.AddonVersion(skin.htpt)')
				Skin_UpdateCount = getsetting('Skin_UpdateCount')
				Skin_UpdateCount2 = getsetting('Skin_UpdateCount2')
				Skin_UpdateTimer = getsetting('Skin_UpdateTimer')
				try: Skin_UpdateTimerN = int(Skin_UpdateTimer)
				except: Skin_UpdateTimerN = 0
				Skin_Update = getsetting('Skin_Update')
				Skin_UpdateDate = getsetting('Skin_UpdateDate')
				Skin_UpdateLog = getsetting('Skin_UpdateLog')
				Skin_Version = getsetting('Skin_Version')
				
				Ping_Connected = getsetting('Ping_Connected')
				Ping_Rate = getsetting('Ping_Rate')
				Ping_Now = getsetting('Ping_Now')
				'''---------------------------'''
				Library_UpdateDate = getsetting('Library_UpdateDate')
				Library_CleanDate = getsetting('Library_CleanDate')
				'''---------------------------'''
				
				#if admin and General_TimerN in A10: print printfirst + "VARCHECK1" + space2 + "Skin_UpdateLog" + space2 + Skin_UpdateLog + space + "Time_Pass" + space2 + Time_Pass + space + "General_Timer" + space2 + General_Timer
				#xbmc.executebuiltin('RunScript(service.htpt)')
				'''---------------------------'''
				
				'''------------------------------
				---count-------------------------
				------------------------------'''
				
				if not systemplatformwindows and (not systemidle300 or General_TimerN in A10): xbmc.sleep(50)
				elif systemplatformwindows and (not systemidle300 or General_TimerN in A10): xbmc.sleep(800)
				else: xbmc.sleep(1000)
				if performance: xbmc.sleep(2000)
				'''---------------------------'''
				
				'''------------------------------
				---setGeneral_Timer--------------
				------------------------------'''
				setGeneral_Timer(admin, admin2, General_Timer, count)
				'''---------------------------'''
				
				'''------------------------------
				---setTime_Delay-----------------
				------------------------------'''
				setTime_Delay(admin, admin2, Time_Delay, count, systemidle3, playerhasvideo, playerhasmedia, playerpaused, performance)
				'''---------------------------'''
				
				#if admin and General_TimerN in A10: print printfirst + "VARCHECK2" + space2 + "Skin_UpdateLog" + space2 + Skin_UpdateLog + space + "Time_Pass" + space2 + Time_Pass + space + "General_Timer" + space2 + General_Timer
				
				if General_Timer == "1":
					'''------------------------------
					---SetTime_Pass------------------
					------------------------------'''
					SetTime_Pass(admin, admin2, Time_Pass)
					'''---------------------------'''
				
				if Skin_UpdateTimer != "0":
					'''------------------------------
					---Skin_UpdateTimer--------------
					------------------------------'''
					SetSkin_UpdateTimer(admin, admin2, Skin_UpdateTimer)
					'''---------------------------'''
				
				if Skin_UpdateTimer == "0" and Skin_UpdateCount == Skin_UpdateCount2:
					'''------------------------------
					---setSkin_UpdateCount-----------
					------------------------------'''
					Skin_UpdateCount2 = setSkin_UpdateCount2(admin, Skin_UpdateCount, Time_Pass)
					'''---------------------------'''
						
				if Skin_UpdateCount2 != Skin_UpdateCount and (systemidle120 or admin or Skin_UpdateCount == "0") and not playerhasvideo and connected:
					'''------------------------------
					---UpdateAddons------------------
					------------------------------'''
					UpdateAddons(admin, Skin_UpdateCount, Skin_UpdateCount2)
					'''---------------------------'''

				if (Skin_Update != "true" and (((Skin_UpdateTimerN < 70 or admin) and Skin_UpdateTimerN > 0) or Skin_Version != htptskinversion)) or (Skin_Update == "true" and Skin_Version == htptskinversion):
					'''------------------------------
					---Skin_Update-(NEW-ONLY)--------
					------------------------------'''
					setSkin_Update(admin, Skin_Version, htptskinversion, Skin_Update)
					'''---------------------------'''

				if Skin_Update == "true" or Skin_UpdateDate == "":
					'''------------------------------
					---setSkin_UpdateDate-(NEW-ONLY)-
					------------------------------'''
					setSkin_UpdateDate(admin, Skin_Version, htptskinversion, Skin_Update, Skin_UpdateDate)
					'''---------------------------'''
					
				if Skin_Update == "true" or Skin_Version == "":
					'''------------------------------
					---setSkin_Version---------------
					------------------------------'''
					setSkin_Version(admin, Skin_Version, htptskinversion)
					'''---------------------------'''
				
				if Skin_Version == htptskinversion and Skin_UpdateLog == "true" and Skin_UpdateDate != "" and systemidle3 and not playerhasvideo and homeW:
					'''------------------------------
					---setSkin_UpdateLog-------------
					------------------------------'''
					printpoint = ""
					dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
					dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
					dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
					dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
					dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
					dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
					startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
					custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
					'''---------------------------'''
					
					if not dialogbusyW and not dialogokW and not dialogprogressW and not dialogselectW and not dialogtextviewerW and not dialogyesnoW and not startupW and not custom1191W:
						printpoint = printpoint + "1"
						if datenowS == "":
							datenow, datenowS, dateafter, dateafterS, yearnow, yearnowS, daynow, daynowS, timenowS, timeow2S, timenow3S, timenow4S = refresh_datetime(admin, datenowS, timenowS) #PREVENT RANDOM BUG WITH datetime
							printpoint = printpoint + "6"
						if Skin_UpdateLog == "true":
							printpoint = printpoint + "2"
							setSkin_UpdateLog(admin, Skin_Version, Skin_UpdateDate, datenowS, Skin_Name)
							'''---------------------------'''
						else: printpoint = printpoint + "9" ; setsetting('Skin_UpdateLog',"false")
							
					'''------------------------------
					---PRINT-END---------------------
					------------------------------'''
					if admin: print printfirst + "setSkin_UpdateLog_LV" + printpoint + space + space2 + Skin_UpdateLog + space + "Time_Start" + space2 + Time_Start
					'''---------------------------'''
				
				if General_TimerN in A10 and Ping_Connected == "true":
					'''------------------------------
					---setPing_Rate-(1-5)------------
					------------------------------'''
					Ping_1 = getsetting('Ping_1')
					Ping_2 = getsetting('Ping_2')
					Ping_3 = getsetting('Ping_3')
					Ping_4 = getsetting('Ping_4')
					Ping_5 = getsetting('Ping_5')
					Ping_6 = getsetting('Ping_6')
					Ping_7 = getsetting('Ping_7')
					Ping_8 = getsetting('Ping_8')
					Ping_9 = getsetting('Ping_9')
					Ping_10 = getsetting('Ping_10')
					'''---------------------------'''
					setPing_Rate(admin, admin2, Ping_Rate, Ping_1, Ping_2, Ping_3, Ping_4, Ping_5, Ping_6, Ping_7, Ping_8, Ping_9, Ping_10)
					'''---------------------------'''
				
				'''------------------------------
				---videoplayertweak--------------
				------------------------------'''
				videoplayertweak(admin, playerhasvideo)
				'''---------------------------'''
				
				if Time_DelayN == 10: #TEST
					pass
					#screensaver(admin, playerhasvideo)
					#notification("ahh","","",2000)
					'''---------------------------'''
				elif Time_DelayN == 20: #TEST
					pass
					'''---------------------------'''
					
				if not systemidle300 or not connected or (not connected2 and not connected3):
					'''------------------------------
					---connectioncheck---------------
					------------------------------'''
					connectioncheck(admin, admin2, count, systemidle3, Ping_Now, Ping_Connected)
					'''---------------------------'''
					
					if Time_Shutdown != "":
						dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
						dialogHeader = xbmc.getInfoLabel('Control.GetLabel(1)')
						setsetting_custom1('service.htpt','Time_Shutdown',"")
						if dialogokW and dialogHeader == str79532.encode('utf-8'):
							xbmc.executebuiltin('dialog.close(okdialog)')
							notification_common("8")
					
					'''------------------------------
					---setPing-----------------------
					------------------------------'''
					#setPing(admin,count,systemidle3)
					'''---------------------------'''
				else:
					if General_TimerN in A10: connectioncheck(admin, admin2, count, systemidle3, Ping_Now, Ping_Connected)
					
					if Time_DelayN > 540 and Time_DelayN < 600: #systemidle540 and not systemidle600:
						pass
						'''---------------------------'''
					elif Time_DelayN > 590 and Time_DelayN < 610: #systemidle600 and not systemidle900:
						if count in A10: screensaver(admin, playerhasvideo)
						'''---------------------------'''
					elif Time_DelayN == 700:
						if count in A10: xbmc.executebuiltin('RunScript(service.htpt.fix,,?mode=12)')
						'''---------------------------'''
					elif Time_DelayN == 900: #systemidle900 and not systemidle1200:
						LibraryUpdate(admin, Library_CleanDate, Library_UpdateDate)
						'''---------------------------'''
						
					elif Time_DelayN > 5400 and not systemplatformwindows: #systemidle5400 :
						doAutoShutdown(admin, Time_Shutdown, Time_DelayN)
						'''---------------------------'''
				
				if count < 60: count += 1
				elif count >= 60: count = 1
				'''---------------------------'''
				
				if TypeError != "": print printfirst + "service.py" + space + "TypeError" + space2 + str(TypeError)
				
	if xbmc.abortRequested:
		print printfirst + "Error 1170: AbortRequested!"
		sys.exit()
		'''---------------------------'''
		
		
#repeat()