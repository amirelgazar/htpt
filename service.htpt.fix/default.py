import xbmc, os, subprocess, sys
import xbmcgui, xbmcaddon

from variables import *
from modules import *
	
class main:
	'''------------------------------
	---Red_Alert---------------------
	------------------------------'''
	if Red_Alert == 'true': Red_Done = Execute_Red(admin, Red_Done, Red_L, Red_LV1, Red_LV2, Red_LV3, Red_LV4, Red_LV5)
	'''---------------------------'''

	'''---------------------------'''
	if systemidle7: Fix_Done = Execute_Fix(admin, Fix_Done, Fix_L, Fix_1, Fix_2, Fix_3, Fix_4, Fix_5, Fix_10, Fix_11, Fix_12, Fix_13, Fix_14, Fix_100, Fix_101, Fix_102, Fix_103, Fix_104)
	'''---------------------------'''

	if Addon_Update != "true" or (Addon_Update == "true" and Addon_Version == htptfixversion):
		'''------------------------------
		---Addon_Update-(NEW-ONLY)--------
		------------------------------'''
		setAddon_Update(admin, Addon_Version, htptfixversion, Addon_Update)
		'''---------------------------'''

	if Addon_Update == "true" or Addon_UpdateDate == "":
		'''------------------------------
		---setAddon_UpdateDate-(NEW-ONLY)-
		------------------------------'''
		setAddon_UpdateDate(admin, Addon_Version, htptfixversion, Addon_Update, Addon_UpdateDate)
		'''---------------------------'''

	if Addon_Update == "true" or Addon_Version == "":
		'''------------------------------
		---setAddon_Version---------------
		------------------------------'''
		setAddon_Version(admin, Addon_Version, htptfixversion)
		'''---------------------------'''

	if Addon_Version == htptfixversion and Addon_UpdateLog == "true" and Addon_UpdateDate != "" and Fix_Done != "" and systemidle7 and not playerhasvideo and home_aW:
		'''------------------------------
		---Addon_UpdateLog----------------
		------------------------------'''
		dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
		dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
		if not dialogokW and not dialogselectW and not dialogprogressW and not dialogbusyW and not startupW and not dialogtextviewerW:
			import datetime
			datenow = datetime.date.today()
			datenowS = str(datenow)
			if datenowS != "": #PREVENT RANDOM BUG WITH datetime
				setAddon_UpdateLog(admin, Addon_Version, Addon_UpdateDate, datenowS)
				setsetting('Addon_UpdateLog',"false")
				'''---------------------------'''
	
	if systemhasaddon_scripthtptdebug:
		if (Fix_Done != "" and Fix_LastDate != "") or (Red_Done != "" and Red_LastDate != ""):
			xbmc.executebuiltin('RunScript(script.htpt.debug)')
			xbmc.sleep(10000)
	if not "true" in Fix_L and not "true" in Red_L and Addon_Version == htptfixversion and Addon_Update == "false" and Addon_ServiceON != "false": setsetting_custom1("service.htpt.fix",'Addon_ServiceON',"false")