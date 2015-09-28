'''------------------------------
---shared_variables--------------
------------------------------'''
import xbmcaddon, sys, os
servicehtptPath          = xbmcaddon.Addon('service.htpt').getAddonInfo("path")
sharedlibDir = os.path.join(servicehtptPath, 'resources', 'lib', 'shared')
sys.path.insert(0, sharedlibDir)

from shared_variables import *
'''---------------------------'''
#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)

'''------------------------------
---service.htpt------------------
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

printfirst = addonName + ": !@# "
'''---------------------------'''
General_ScriptON = getsetting('General_ScriptON')
General_Timer = getsetting('General_Timer')
try: General_TimerN = int(General_Timer)
except: General_TimerN = 0
Time_Delay = getsetting('Time_Delay')
Time_Start = getsetting('Time_Start')
Time_Pass = getsetting('Time_Pass')
Time_Shutdown = getsetting('Time_Shutdown')
'''---------------------------'''
Skin_UpdateCount = getsetting('Skin_UpdateCount')
Skin_UpdateCount2 = getsetting('Skin_UpdateCount2')
Skin_UpdateTimer = getsetting('Skin_UpdateTimer')
Skin_Update = getsetting('Skin_Update')
Skin_UpdateDate = getsetting('Skin_UpdateDate')
Skin_UpdateLog = getsetting('Skin_UpdateLog')
Skin_Version = getsetting('Skin_Version')
Skin_Name = getsetting('Skin_Name')
'''---------------------------'''
Ping_Connected = getsetting('Ping_Connected')
Ping_Now = getsetting('Ping_Now')
Ping_Rate = getsetting('Ping_Rate')
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
Library_UpdateDate = getsetting('Library_UpdateDate')
Library_CleanDate = getsetting('Library_CleanDate')
'''---------------------------'''
A10 = [0, 10, 20, 30, 40, 50 , 60]
