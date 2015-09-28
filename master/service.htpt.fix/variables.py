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
---ADDON-COMMON------------------
------------------------------'''
getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

addonName2 = addonName
printfirst = addonName + ": !@# "

'''------------------------------
---service.htpt.fix--------------
------------------------------'''
General_DownloadON = getsetting('General_DownloadON')
General_ScriptON = getsetting('General_ScriptON')
Addon_Update = getsetting('Addon_Update')
Addon_UpdateDate = getsetting('Addon_UpdateDate')
Addon_UpdateLog = getsetting('Addon_UpdateLog')
Addon_Version = getsetting('Addon_Version')
Addon_ServiceON = getsetting('Addon_ServiceON')
'''---------------------------'''
Fix_1 = getsetting('Fix_1')
Fix_2 = getsetting('Fix_2')
Fix_3 = getsetting('Fix_3')
Fix_4 = getsetting('Fix_4')
Fix_5 = getsetting('Fix_5')
Fix_6 = getsetting('Fix_6')
Fix_7 = getsetting('Fix_7')
Fix_8 = getsetting('Fix_8')
Fix_9 = getsetting('Fix_9')
'''---------------------------'''
Fix_10 = getsetting('Fix_10')
Fix_11 = getsetting('Fix_11')
Fix_12 = getsetting('Fix_12')
Fix_13 = getsetting('Fix_13')
Fix_14 = getsetting('Fix_14')
'''---------------------------'''
Fix_100 = getsetting('Fix_100')
Fix_101 = getsetting('Fix_101')
Fix_102 = getsetting('Fix_102')
Fix_103 = getsetting('Fix_103')
Fix_104 = getsetting('Fix_104')
Fix_L = [Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_6, Fix_7, Fix_8, Fix_9, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104]
Fix_LastDate = getsetting('Fix_LastDate')
Fix_Done = getsetting('Fix_Done')
Fix_ScriptON = getsetting('Fix_ScriptON')
'''---------------------------'''
Red_Alert = getsetting('Red_Alert')
Red_LV1 = getsetting('Red_LV1')
Red_LV2 = getsetting('Red_LV2')
Red_LV3 = getsetting('Red_LV3')
Red_LV4 = getsetting('Red_LV4')
Red_LV5 = getsetting('Red_LV5')
Red_L = [Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5]
Red_LastDate = getsetting('Red_LastDate')
Red_Done = getsetting('Red_Done')
Red_ScriptON = getsetting('Red_ScriptON')
'''---------------------------'''
Ads_Date = getsetting('Ads_Date')
Ads_Timezone = getsetting('Ads_Timezone')

'''------------------------------
---$ADDON------------------------
------------------------------'''
addon = 'plugin.video.israelive'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	'''------------------------------
	---plugin.video.israelive--------
	------------------------------'''
	str30200 = xbmc.getInfoLabel('$ADDON['+ addon +' 32002]').decode('utf-8') #IsraeLIVE...
	'''---------------------------'''