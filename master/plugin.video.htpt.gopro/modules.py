#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys
import xbmcplugin
import urllib
import urllib2
import re

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

def CATEGORIES():
	'''Go-Pro'''
	#YOUList2("GoProCamera", 'UCqhnX4jA0A5paNd1v-zEysw', "", "", '1')
	addDir('Go-Pro','GoProCamera',9,'https://yt3.ggpht.com/-sp0YiR_yyR0/AAAAAAAAAAI/AAAAAAAAAAA/kXU4u1ny2T4/s100-c-k-no/photo.jpg',"",'1',58)
	'''Exterme Sport'''
	addDir("Extreme Sport",'plugin://plugin.video.extreme.com',8,"special://home/addons/plugin.video.extreme.com/icon.png","",'1',50)   
	#addDir(addonString(57).encode('utf-8') + space + addonString(200).encode('utf-8') + space + "1" + space5 + addonString(16).encode('utf-8'),'UCqhnX4jA0A5paNd1v-zEysw',9,'http://i.ytimg.com/i/fm5IpcgGCooON4Mm2vq40A/1.jpg?v=52fcd974',addonString(116).encode('utf-8'),'1',"")
	#ShowFromUser('GoProCamera')