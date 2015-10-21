'''------------------------------
---shared_variables--------------
------------------------------'''
import xbmcaddon, sys, os
servicehtptPath          = xbmcaddon.Addon('service.htpt').getAddonInfo("path")
sharedlibDir = os.path.join(servicehtptPath, 'resources', 'lib', 'shared')
sys.path.insert(0, sharedlibDir)
from shared_variables import *
'''---------------------------'''
'''---------------------------'''
#libDir = os.path.join(addonPath, 'resources', 'lib')
#sys.path.insert(0, libDir)

'''------------------------------
---script.htpt.emu---------------
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

General_LastModified = getsetting('General_LastModified')
video_black_frame_insertion2 = getsetting('video_black_frame_insertion2')
video_refresh_rate2 = getsetting('video_refresh_rate2')
video_smooth2 = getsetting('video_smooth2')
audio_device2 = getsetting('audio_device2')
audio_latency2 = getsetting('audio_latency2')
audio_out_rate2 = getsetting('audio_out_rate2')
audio_sync2 = getsetting('audio_sync2')
audio_volume2 = getsetting('audio_volume2')


'''------------------------------
---script.htpt.emu---------------
------------------------------'''
printpoint = ""
launcherfilename = 'launchers'
copylauncher = "false"
#scripthtptemu_folder = "/storage/.kodi/addons/script.htpt.emu/resources/lib/"
scripthtptemu_folder = os.path.join(addonPath,'lib/')
advancedlauncher_addondata_path= os.path.join(addondata_path, 'plugin.program.advanced.launcher', '')
htptemu_addondata_path = os.path.join(addondata_path, addonID, '')
htptemu_copy_path = os.path.join(addonPath, 'specials', 'scripts', 'copy', '')
htptemu_copyrepeat_path = os.path.join(addonPath, 'specials', 'scripts', 'copy', 'repeat', '')
htptemu_copyrepeatlaunchers_path = os.path.join(addonPath, 'specials', 'scripts', 'copy', 'repeat', 'launchers', '')
htptemu_copyonce_path = os.path.join(addonPath, 'specials', 'scripts', 'copy', 'once', '')
launcher_file = os.path.join(advancedlauncher_addondata_path, 'launchers.xml')
launcher2_file = os.path.join(htptemu_addondata_path, 'launchers.xml')
if not systemplatformwindows: configpath = os.path.join(emulators_path, 'retroarch', 'config', '')
elif systemplatformwindows: configpath = "Z:\\userdata\\addon_data\\script.htpt.emu\\"

file1_fix = os.path.join(addonPath, 'emusettings.py')
file1_fix2 = os.path.join(addondata_path, addonID, 'emusettings.py')
file1 = configpath + "retroarch.cfg"
file2 = configpath + "nestopia_libretro.so.cfg"
file3 = configpath + "snes9x_next_libretro.so.cfg"
file4 = configpath + "genesis_plus_gx_libretro.so.cfg"
file5 = configpath + "mame2014_libretro.so.cfg"
file6 = configpath + "mednafen_pce_fast_libretro.so.cfg"
file7 = configpath + "mednafen_psx_libretro.so.cfg"
file8 = configpath + "mupen64plus_libretro.so.cfg"
file9 = configpath + "desmume_libretro.so.cfg"
#file10 = configpath + "desmume_libretro.so.cfg"

emubutton = ((xbmc.getCondVisibility('Window.IsVisible(MyPrograms.xml)') or xbmc.getCondVisibility('Window.IsVisible(AddonBrowser.xml)')) and xbmc.getCondVisibility('StringCompare(ListItem.Label,'+ addonName +''))
emubutton2 = (myprogramsW and leftmenubutton110)
'''---------------------------'''