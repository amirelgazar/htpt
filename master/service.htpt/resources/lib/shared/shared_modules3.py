import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,random
import json

from variables import *
#from modules import *
from shared_modules import *

'''plugins'''
def addDir(name, url, mode, iconimage, desc, num, viewtype, fanart=""):
	url2 = url ; printpoint = "" ; returned = "" ; extra = ""
	if '$LOCALIZE' in name or '$ADDON' in name: name = xbmc.getInfoLabel(name)
	if '$LOCALIZE' in desc or '$ADDON' in desc: desc = xbmc.getInfoLabel(desc)
	

	if desc == None or desc == "" or desc == "None": desc = ""
	else:
		try: desc = str(desc).encode('utf-8')
		except:
			try: desc = str(desc)
			except Exception, TypeError:
				extra = extra + newline + "TypeError" + space2 + "desc Error" + space + "name" + space2 + str(name)
				desc = ""
	if iconimage == None or iconimage == "": iconimage = "" #iconimage = "None" #"None"
	if url == None or url == "": url = ""
	else:
		url = str(url)
	
	#if url == None or url == "": url = "None" #"None"
	
	if name == None or name == "": name = "" #name = "None" #"None"
	else:
		try: name = name.encode('utf-8')
		except: pass
	if fanart == None: fanart = ""
	
	if mode == 17: name = '[COLOR=Green]' + name + '[/COLOR]'
	elif mode == 5: name = '[COLOR=Yellow]' + name + '[/COLOR]'
	elif mode == 8: name = '[COLOR=White2]' + name + '[/COLOR]'
	
	
	if mode >= 100 and 1 + 1 == 2:
		#if url == "": url = "1"
		u=sys.argv[0]+"?url="+str(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)
	else:
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)
	
	
	
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc} )
	try:
		if Fanart_Enable != "" and Fanart_EnableCustom != "": pass
	except:
		Fanart_Enable = "true"
		Fanart_EnableCustom = "false"
		
	fanart2 = setaddonFanart(fanart, Fanart_Enable, Fanart_EnableCustom)
	if fanart2 != "": liz.setProperty('Fanart_Image', fanart2)
		
	menu = []
	#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	
	if admin: print printfirst + "addDir" + space2 + newline + "addonID" + space2 + str(addonID) + newline + "name" + space2 + str(name) + newline + "url " + space2 + str(url) + newline + "url2" + space2 + str(url2) + newline + "mode" + space2 + str(mode) + newline + "iconimage" + space2 + str(iconimage) + newline + "desc" + space2 + str(desc) + newline + "num" + space2 + str(num)
	
	if addonID == 'script.htpt.install':
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
	elif mode == 4 or mode == 3:
		'''------------------------------
		---play_video/2------------------
		------------------------------'''
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 5:
		'''------------------------------
		---PlayMultiVideos-(list)--------
		------------------------------'''
		if admin:
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.htpt.kids/?&mode=5&url=%s)"% (url)))
			#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://%s/?num&iconimage=''&mode=6&name=''&url=%s)"% (addonID, url)))
			#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://plugin.video.htpt.kids/?&mode=5&url="+url+")"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?iconimage="+iconimage+"&mode=5&name="+name+"&num="+num+"&url="+url+")"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.htpt.kids/?iconimage=http%3a%2f%2fmsc.wcdn.co.il%2fw-2-1%2fw-300%2f768225-54.jpg&mode=5&name=%d7%94%d7%9b%d7%91%d7%a9%d7%94%20%d7%a9%d7%95%d7%a9%d7%a0%d7%94&num=1&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d&viewtype=50)"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?&mode=5&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d)"))
			liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 6:
		'''------------------------------
		---ListMultiVideos-(play)--------
		------------------------------'''
		if admin:
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.htpt.kids/?&mode=5&url=%s)"% (url2)))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?iconimage="+iconimage+"&mode=5&name="+name+"&num="+num+"&url="+url+")"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.htpt.kids/?iconimage=http%3a%2f%2fmsc.wcdn.co.il%2fw-2-1%2fw-300%2f768225-54.jpg&mode=5&name=%d7%94%d7%9b%d7%91%d7%a9%d7%94%20%d7%a9%d7%95%d7%a9%d7%a0%d7%94&num=1&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d&viewtype=50)"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?&mode=5&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d)"))
			liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 12:
		'''------------------------------
		---View-Playlist-----------------
		------------------------------'''
		#url=urllib.unquote(url)
		#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://plugin.video.htpt.kids/?num&iconimage=''&mode=13&name=''&url=%s)"% (url)))
		#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://%s/?num&iconimage=''&mode=13&name=''&url=%s)"% (addonID, url)))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 9:
		'''------------------------------
		---TV-MODE-----------------------
		------------------------------'''
		#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://%s/?num&iconimage=''&mode=15&name=''&url=%s)"% (addonID, url)))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 8:
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
		returned = ok
		'''---------------------------'''
	elif mode == 11 or mode == 15:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 13:
		#menu.append(('[COLOR=Yellow]' + str79520.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://%s/?num&iconimage=''&mode=12&name=''&url=%s)"% (addonID, url)))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 17:
		'''------------------------------
		---TV-MODE-2---------------------
		------------------------------'''
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 18:
		'''------------------------------
		---TV-MODE-2+CUSTOM--------------
		------------------------------'''
		up, down = CheckMoveCustom(name, num)
		
		if up != "": menu.append(("Move Up", "XBMC.RunPlugin(plugin://%s/?url=%s&mode=23&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)" % (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num + "__" + up, viewtype, urllib.quote_plus(fanart)))) #Move Up
		if down != "": menu.append(("Move Down", "XBMC.RunPlugin(plugin://%s/?url=%s&mode=23&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)" % (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num + "__" + down, viewtype, fanart))) #Move Down
		#u=sys.argv[0]+"?url="+str(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)
		
		#menu.append((localize(16106), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=21&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, url, name, iconimage, desc, num, viewtype, fanart))) #Manage....
		
		menu.append((localize(16106), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=21&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num, viewtype, fanart))) #Manage....
		menu.append((localize(33063), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=22&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num, viewtype, fanart))) #Options....
		liz.addContextMenuItems(items=menu, replaceItems=True)
		if url == "None": ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		else: ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 20:
		'''------------------------------
		---New-Custom-Playlist-----------
		------------------------------'''
		menu.append((localize(33063), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=22&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num, viewtype, fanart))) #Options....
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 21:
		'''------------------------------
		---Manage...---------------------
		------------------------------'''
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 22:
		'''------------------------------
		---AdvancedCustom...-------------
		------------------------------'''
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
	
	if admin and not admin2 and admin3:
		print printfirst + "addDir_LV" + printpoint + space + "name" + space2 + str(name) + newline + \
		"desc" + space2 + str(desc) + space + "addonID" + space2 + str(addonID) + newline + \
		"iconimage" + space2 + str(iconimage) + newline + \
		"num" + space2 + str(num) + newline + \
		"fanart" + space2 + str(fanart) + extra
		'''---------------------------'''
	return returned
	
def addVideoLink(name, url, mode, iconimage='DefaultFolder.png', desc=""):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + name 
	#u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + name + "&iconimage="+str(iconimage)+"&desc="+str(desc)+"&desc="+str(desc)+"&desc="+str(desc)
	#u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode="+ str(mode) #SPOTIFY/BESTOFYOUTUBE
	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": urllib.unquote(name), "Plot": urllib.unquote(desc)})    
	liz.setProperty('IsPlayable', 'true')
	ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
	if admin: print printfirst + "addVideoLink" + space + "ok" + space2 + str(ok) + space + "u" + space2 + str(u)
	'''---------------------------'''
	return ok
		
def addLink(name, url, iconimage="", desc="", viewtype=""):
	printpoint = ""
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc})
	liz.setProperty("IsPlayable","true")
	
	if "plugin://plugin.video.youtube/playlist/" in url:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
		printpoint = printpoint + "1"
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
		printpoint = printpoint + "2"
	if admin: print printfirst + 'addLink' + "_LV" + printpoint + space + "ok" + space2 + str(ok) + space + "name" + space2 + str(name) + space + "url" + space2 + str(url) + space
	'''---------------------------'''
	return ok, liz
	
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
				params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
					param[splitparams[0]]=splitparams[1]
							
	return param

def ListLive(url):
	#addDir('[COLOR=Yellow]' + str79520.encode('utf-8') + '[/COLOR]',url,12,addonMediaPath + "190.png",str79526.encode('utf-8'),'1',"") #Quick-Play
	link = OPEN_URL(url)
	link=unescape(link)
	print printfirst + "link" + space2 + link
	matches1=re.compile('pe=(.*?)#',re.I+re.M+re.U+re.S).findall(link)
	#print str(matches1[0]) + '\n'
	for match in matches1 :
		#print "match=" + str(match)
		match=match+'#'
		if match.find('playlist') != 0 :
			'''------------------------------
			---url---------------------------
			------------------------------'''
			regex='name=(.*?)URL=(.*?)#'
			matches=re.compile(regex,re.I+re.M+re.U+re.S).findall(match)
			#print str(matches)
			for name,url in matches:
				thumb=''
				i=name.find('thumb')
				i2=name.find('description')
				if i>0:
					thumb=name[i+6:]
					name=name[0:i]
					description = name[i2+11:]
					print printfirst + "name" + space2 + name + space + "thumb" + space2 + thumb + space + "description" + space2 + description
		#print url
				addLink('[COLOR yellow]'+ name+'[/COLOR]',url,thumb,description,"")  
			
		else:
			'''------------------------------
			---.plx--------------------------
			------------------------------'''
			regex='name=(.*?)URL=(.*?).plx'
			matches=re.compile(regex,re.I+re.M+re.U+re.S).findall(match)
			for name,url in matches:
				thumb=''
				i=name.find('thumb')
				i2=name.find('description')
				if i>0:
					thumb=name[i+6:]
					name=name[0:i]
					description = name[i2+11:]
				url=url+'.plx'
				if name.find('Radio') < 0 :
					addDir('[COLOR blue]'+name+'[/COLOR]',url,7,thumb,description,'1',"")
					
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "ListLive" + space2 + "matches1" + space2 + str(matches1) + space
	'''---------------------------'''

def clean_commonsearch(x):
	y = x
	if "commonsearch" in y:
		y = y.replace("commonsearch101", space + commonsearch101)
		y = y.replace("commonsearch102", space + commonsearch102)
		y = y.replace("commonsearch104", space + commonsearch104)
		y = y.replace("commonsearch111", space + commonsearch111)
		y = y.replace("commonsearch112", space + commonsearch112)
		y = y.replace("commonsearch114", space + commonsearch114)
		y = y.replace(" ","%20")
	
	if "[COLOR" in y or "[/COLOR" in y:
		y = y.replace("[COLOR=Green]", "")
		y = y.replace("[COLOR=Yellow]", "")
		y = y.replace("[COLOR=White]", "")
		y = y.replace("[/COLOR]", "")
	
	if admin: print printfirst + "clean_commonsearch" + space + "x" + str(x) + space + "y" + space2 + str(y)
	return y
	
def YoutubeSearch(name, url, desc, viewtype):
	printpoint = "" ; admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; value = "" ; url2 = ""

	name = clean_commonsearch(name)
	url = clean_commonsearch(url)
	
	try: url = str(url).encode('utf-8')
	except: pass
	try: name = str(name).encode('utf-8')
	except: pass
	
	if name == localize(137):
		'''search'''
		printpoint = printpoint + "1"
		url2 = url.replace("%20", "")
		#print url2
		x = desc
		#addonString_servicehtpt(23).encode('utf-8') % (url2)
		returned = dialogkeyboard("", x, 0, '1', "", "")
		if returned != 'skip':
			value = returned + space + url2
		else:
			notification_common("8")
	else:
		'''commonsearch'''
		printpoint = printpoint + "2"
		value = name + space + url
	
	if value != "": update_view('plugin://plugin.video.youtube/search/?q=' + value, viewtype)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin:
		print printfirst + "YoutubeSearch" + space + "value" + space2 + str(value) + newline + \
		"url" + space2 + str(url) + newline + \
		"url2" + space2 + str(url2) + space 
		'''---------------------------'''
	
def ListPlaylist2(playlistid, page, viewtype):
	default = 'plugin://plugin.video.youtube/'
	update_view('plugin://plugin.video.youtube/playlist/' + playlistid + '/', viewtype)
	'''---------------------------'''
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    '''---------------------------'''
    return link

def play_video(url):
	#xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url +')')
	#match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
	url='https://gdata.youtube.com/feeds/api/videos/'+ url +''
	#url='https://gdata.youtube.com/feeds/api/videos/'+ url +'' + '?alt=json'
	#url='plugin://plugin.video.youtube/play/?video_id='+ url +''
	link = OPEN_URL(url)
	if admin: print printfirst + "play_video" + space + "link" + space2 + link
	if admin: print printfirst + "play_video" + space + "url" + space2 + url
	prms=json.loads(link)
	
	match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').url
	finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1"
	title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
	thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
	description = str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
	addLink(title,finalurl,thumb,description,"")
	#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)

def play_video2(url):
	
	if 'plugin.video.wallaNew.video' in url: xbmc.executebuiltin('PlayMedia('+ url +')')
	else:
		xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url +')')
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "play_video2" + space + "url" + space2 + str(url)
	'''---------------------------'''

def YOULink(mname, url, thumb, desc):
	if not "UKY3scPIMd8" in url or admin:
		ok=True
		url = "plugin://plugin.video.youtube/play/?video_id="+url
		#url='https://gdata.youtube.com/feeds/api/videos/'+url+'?alt=json&max-results=50' #TEST
		liz=xbmcgui.ListItem(mname, iconImage="DefaultVideo.png", thumbnailImage=thumb)
		liz.setInfo( type="Video", infoLabels={ "Title": mname, "Plot": desc } )
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
		if admin: print printfirst + "YOULink" + space + "url" + space2 + str(url) + space + "mname" + space2 + mname
		return ok
		
def MultiVideos(mode, name, url, iconimage, desc, num, viewtype):
	printpoint = "" ; i = 0 ; i2 = 0 ; extra = "" ; desc = str(desc)
	pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	pl.clear()
	playlist = []
	
	
	url2 = url.replace("['","")
	url2 = url2.replace("']","")
	url2 = url2.replace("'","")
	url2 = url2.replace("' ","'")
	url2 = url2.replace("'',","")
	
	url2 = url2.replace("&amp;", "&")
	
	url2 = url2.replace(" &custom","&custom")
	url2 = url2.replace(" &wallaNew2","&wallaNew2")
	url2 = url2.replace(" &wallaNew","&wallaNew")
	
	url2 = url2.replace(" &sdarot","&sdarot")
	url2 = url2.replace(" &seretil","&seretil")
	url2 = url2.replace(" &hotVOD","&hotVOD")
	
	url2 = url2.replace(" &youtube_ch","&youtube_ch")
	url2 = url2.replace(" &youtube_pl","&youtube_pl")
	url2 = url2.replace(" &youtube_id","&youtube_id")
	url2 = url2.replace(" &youtube_se","&youtube_se")
	
	#url2 = url2.replace(",","")
	
	url2a = url2
	url2 = url2.split(',')
	if General_TVModeShuffle == "true" and mode == 5: random.shuffle(url2) ; printpoint = printpoint + "0"
		
		
	if admin: print "url_first_check" + space2 + newline + "url " + space2 + str(url) + newline + "url2a" + space2 + str(url2a) + newline + "url2" + space2 + str(url2)

	returned = get_types(url)
	for x in url2:
		x = str(x) ; finalurl = "" ; finalurlL = [] ; numOfItems2 = 0
		x = x.replace("[","")
		x = x.replace(",","")
		x = x.replace("'","")
		x = x.replace("]","")
		if x not in playlist and x != "":
			i += 1
			if mode == 5:
				if "&custom=" in x:
					x = x.replace("&custom=","")
					finalurl=x
					'''---------------------------'''
				elif "&wallaNew=" in x:
					x = x.replace("&wallaNew=","")
					if "item_id" in x: finalurl="plugin://plugin.video.wallaNew.video/?url="+x+"&mode=10&module=wallavod"
					'''---------------------------'''
				elif "&wallaNew2=" in x:
					x = x.replace("&wallaNew2=","")
					#z = '1'
					#addDir(name + space + str(i), "plugin://plugin.video.wallaNew.video/?url="+x+"&mode="+z+"&module=nickjr", 8, iconimage, desc, num, viewtype)
					'''---------------------------'''
				elif "&sdarot=" in x:
					x = x.replace("&sdarot=","")
					#finalurl="plugin://plugin.video.sdarot.tv/?mode=4&"+x
					'''---------------------------'''
				elif "&seretil=" in x:
					x = x.replace("&seretil=","")
					#finalurl="plugin://plugin.video.sdarot.tv/?mode=4&"+x
					'''---------------------------'''
				elif "&hotVOD=" in x:
					x = x.replace("&hotVOD=","")
					if "FCmmAppVideoApi_AjaxItems" in x:
						finalurl="plugin://plugin.video.hotVOD.video/?url="+x+"&mode=4"
						'''---------------------------'''
				elif "&youtube_ch=" in x:
					#i2 += 1
					x = x.replace("&youtube_ch=","")
					#finalurl="plugin://plugin.video.youtube/play/?playlist_id="+x+""
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					#i2 += 1
					#x = x.replace("&youtube_pl=","")
					try: finalurlL, numOfItems2 = youtube_pl_to_youtube_id(x, playlist)
					except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					#finalurl="plugin://plugin.video.youtube/play/?playlist_id="+x+""
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					finalurl="plugin://plugin.video.youtube/play/?video_id="+x+"&hd=1"
					'''---------------------------'''
				elif "&youtube_se=" in x:
					#try: str(name).encode('utf-8')
					#except: str(name)
					#x = x.replace("&youtube_se=","")
					x = x + space + str(name)
					finalurlL, numOfItems2 = youtube_pl_to_youtube_id(x, playlist)
					#except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					#finalurl="plugin://plugin.video.youtube/play/?video_id="+x+"&hd=1"
					'''---------------------------'''
					
				if admin: extra = extra + newline + str(i) + space2 + str(finalurl)
				'''---------------------------'''
				#title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
				#thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
				#description = str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
				
				if finalurl != "" or finalurlL != []:
					returned = get_types(finalurl)
					returned2 = get_types(finalurlL)
					count = 0
					if finalurlL != [] and 'list' in returned2:
						if General_TVModeShuffle == "true" and mode == 5: random.shuffle(finalurlL) ; printpoint = printpoint + "0"
						#finalurlL2 = str(finalurlL)
						#finalurlL2 = finalurlL2.split(',')
						if numOfItems2 > 0:
							for y in finalurlL:
								count += 1
								#if not y in playlist:
								pl.add(y)
								playlist.append(y)
								if not "3" in printpoint:
									printpoint = printpoint + "3"
									xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl) ; xbmc.sleep(2000)
									'''---------------------------'''
								
								
								if count >= numOfItems2: break
								if admin: print printfirst + "MultiVideos" + space + "i" + space2 + str(i) + space + "y" + space2 + str(y) + space + "count" + space2 + str(count) + newline + "finalurlL" + space2 + str(finalurlL) #+ newline + "finalurlL2" + space2 + str(finalurlL2)
							
					elif finalurl != "" and 'str' in returned:	
						pl.add(finalurl)
						playlist.append(finalurl)
						if not "3" in printpoint:
							printpoint = printpoint + "3"
							xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
							'''---------------------------'''
					else: printpoint = printpoint + "9"
					
					if admin: print printfirst + "MultiVideos___" + space + "i" + space2 + str(i) + space + "count" + space2 + str(count) + space + "playlist" + space2 + str(playlist)
					
			elif mode == 6:
					
				if "&youtube_ch=" in x:
					x = x.replace("&youtube_ch=","")
					if "/playlists" in x: pass
					addDir(name + space + str(i), x, 9, iconimage, desc, num, viewtype) #addonString(192).encode('utf-8')
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					i2 += 1
					x = x.replace("&youtube_pl=","")
					addDir(name + space + str(i), x, 13, iconimage, desc, num, viewtype) #addonString(192).encode('utf-8')
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					addDir(name + space + str(i), x, 4, iconimage, desc, num, viewtype)
					'''---------------------------'''
				elif "&youtube_se=" in x:
					#try: str(name).encode('utf-8')
					#except: str(name)
					x = x.replace("&youtube_se=","")
					x = x + space + str(name)
					x = clean_commonsearch(x)
					addDir(name + space + str(i), x, 3, iconimage, desc, num, viewtype)
					'''---------------------------'''	
				else:
					if "&wallaNew=" in x:
						x = x.replace("&wallaNew=","")
						if "item_id" in x: z = '10'
						elif "seriesId" in x: z = '5'
						elif "seasonId" in x: z = '3'
						elif "genreId" in x: z = '2'
						else: z = '10'
						addDir(name + space + str(i), "plugin://plugin.video.wallaNew.video/?url="+x+"&mode="+z+"&module=wallavod", 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&wallaNew2=" in x:
						x = x.replace("&wallaNew2=","")
						z = '1'
						addDir(name + space + str(i), "plugin://plugin.video.wallaNew.video/?url="+x+"&mode="+z+"&module=nickjr", 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&sdarot=" in x:
						x = x.replace("&sdarot=","")
						if "episode_id=" in url: z = '4'
						elif "season_id" in url: z = '5'
						elif "series_id=" in url: z = '3'
						else: z = '2'
						
						if 1 + 1 == 2:
							if not "summary=" in x:
								if z == '3':
									if not "summary" in x: summary = "&summary"
									else: summary = ''
								else: summary = "&summary="
								#elif desc != "": summary = "&summary="+desc
							else: summary = ''
						else: summary = ''
						
						if admin and not admin2:
							print printfirst + "MultiVideos" + space + "Testing x" + space2 + newline + \
							"x" + space2 + str(x) + newline + \
							"z" + space2 + str(z) + newline + \
							"summary" + space2 + str(summary) + newline
						
						if not "series_name=" in x: series_name = "&series_name="
						else: series_name = ''
						addDir(name + space + str(i), "plugin://plugin.video.sdarot.tv/?mode="+z+summary+series_name+"&image="+iconimage+"&name="+name+"&"+x, 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&seretil=" in x:
						x = x.replace("&seretil=","")
						if "?mode=211&url=http%3a%2f%2fseretil.me" in x: name2 = '[COLOR=Red]' + name + space + str(i) + '[/COLOR]'
						else: name2 = name + space + str(i)
						addDir(name2, "plugin://plugin.video.seretil/"+x, 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&hotVOD=" in x:
						x = x.replace("&hotVOD=","")
						if "TopSeriesPlayer" in x: z = '3&module=%2fCmn%2fApp%2fVideo%2fCmmAppVideoApi_AjaxItems%2f0%2c13776%2c'
						elif "FCmmAppVideoApi_AjaxItems" in x: z = '4'
						else: z = '3&module=%2fCmn%2fApp%2fVideo%2fCmmAppVideoApi_AjaxItems%2f0%2c13776%2c'
						addDir(name + space + str(i), "plugin://plugin.video.hotVOD.video/?mode="+z+"&url="+x, 8, iconimage, desc, num, viewtype)
						'''---------------------------'''	
						
					elif "&custom=" in x:
						x = x.replace("&custom=","")
						addLink(name + space + str(i), x, iconimage, desc, viewtype)
						'''---------------------------'''
					else: addLink(name + space + str(i), x, iconimage, desc, viewtype)
			
	if mode == 5 and playlist == []:
		notification(addonString_servicehtpt(1).encode('utf-8'), addonString_servicehtpt(2).encode('utf-8'), "", 2000)
		#xbmc.executebuiltin('RunScript('+addonID+'/?mode=6&name='+name+'&url='+url+'&iconimage='+str(iconimage)+'&desc='+desc+'&num='+str(num)+'&viewtype='+str(viewtype)+')')
		#MultiVideos(6, name, url, iconimage, desc, num, viewtype)
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin or extra != "":
		print printfirst + "MultiVideos_LV" + printpoint + space + "mode" + space2 + str(mode) + space + "i" + space2 + str(i) + space + newline + \
		"url " + space2 + str(url) + newline + \
		"url2" + space2 + str(url2) + newline + \
		"pl" + space2 + str(pl) + space + "playlist" + space2 + str(playlist) + newline + \
		"finalurl" + space2 + str(finalurl) + space + "finalurlL" + space2 + str(finalurlL) + space + newline + \
		extra
		'''---------------------------'''
	
def PlayPlayList(playlistid):
	printpoint = ""
	url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=40'
	link = OPEN_URL(url)
	prms=json.loads(link)

	playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	playlist.clear()
	playlist1 = []
	numOfItems=int(prms['feed'][u'openSearch$totalResults'][u'$t']) #if bigger than 40 needs  to add more result
	
	j=1
	h=1
	pages = (numOfItems //50)+1
	while  j<= pages:
		link=OPEN_URL(url)
		prms=json.loads(link)
		i=0
		while i< 50  and  h<numOfItems :
			try:
				urlPlaylist= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$player'][0][u'url'])
				match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').findall(urlPlaylist)
				#finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
				finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1"
				title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
				thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
				liz = xbmcgui.ListItem(title, iconImage="DefaultVideo.png", thumbnailImage=thumb)
				liz.setInfo( type="Video", infoLabels={ "Title": title} )
				liz.setProperty("IsPlayable","true")
				playlist1.append((finalurl ,liz))
			except:
				pass
			if playlist1 != [] and not "3" in printpoint:
				for blob ,liz in playlist1:
					try:
						if blob:
							playlist.add(blob,liz)
							xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playlist)
							printpoint = printpoint + "3"
							xbmc.sleep(2000)
					except:
						printpoint = printpoint + "4"
				
				
			i=i+1
			h=h+1

		j=j+1
		url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=50&start-index='+str (j*50-49)
	random.shuffle(playlist1)
	for blob ,liz in playlist1:
		try:
			if blob:
				playlist.add(blob,liz)
		except:
			pass
	notification_common("15")
	playlist.shuffle()
	
	#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playlist)

#https://gdata.youtube.com/feeds/api/users/polosoft/playlists (gets playlist fro, user) https://gdata.youtube.com/feeds/api/users/polosoft/playlists?alt=json
#https://gdata.youtube.com/feeds/api/playlists/PLN0EJVTzRDL_53Jz8bhZl4m3UtkY2btbV?max-results=50?alt=json  (gets items in playlist)
#https://gdata.youtube.com/feeds/api/playlists/PLN0EJVTzRDL_53Jz8bhZl4m3UtkY2btbV?max-results=50&alt=json
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "PlayPlayList_LV" + printpoint + space + "playlistid" + space2 + playlistid + space + "numOfItems" + space2 + str(numOfItems) + space + "playlist1" + space2 + str(playlist1)
	'''---------------------------'''

def PlayPlayList2(playlistid):
	default = 'plugin://plugin.video.youtube/'
	default2 = 'play/?playlist_id='

	xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?playlist_id='+ playlistid +')')
	#addLink("",'plugin://plugin.video.youtube/play/?playlist_id=' + playlistid,"","","")
	#xbmc.executebuiltin('RunPlugin(plugin://plugin.video.youtube/play/?playlist_id='+ playlistid +'&order=default)')
	#plugin://plugin.video.youtube/playlist/PL4RuBaWCIgHrFNTIP37qBS254y7-2r9e4/
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "PlayPlayList2" + space + "playlistid" + space2 + str(playlistid)
	'''---------------------------'''

def PlayPlayList3(playlistid):
	default = 'plugin://plugin.video.youtube/'
	default2 = 'play/?playlist_id='
	update_view(default + default2 + playlistid + '/', viewtype)
	'''---------------------------'''
	
def getCustom_Playlist(admin):
	#from variables import Custom_Playlist1
	returned = "" ; printpoint = ""
	if Custom_Playlist1_ID  == "": returned = 'Custom_Playlist1_ID'
	elif Custom_Playlist2_ID  == "": returned = 'Custom_Playlist2_ID'
	elif Custom_Playlist3_ID  == "": returned = 'Custom_Playlist3_ID'
	elif Custom_Playlist4_ID  == "": returned = 'Custom_Playlist4_ID'
	elif Custom_Playlist5_ID  == "": returned = 'Custom_Playlist5_ID'
	elif Custom_Playlist6_ID  == "": returned = 'Custom_Playlist6_ID'
	elif Custom_Playlist7_ID  == "": returned = 'Custom_Playlist7_ID'
	elif Custom_Playlist8_ID  == "": returned = 'Custom_Playlist8_ID'
	elif Custom_Playlist9_ID  == "": returned = 'Custom_Playlist9_ID'
	elif Custom_Playlist10_ID  == "": returned = 'Custom_Playlist10_ID'
	'''---------------------------'''
	if admin and not admin2 and admin3: print printfirst + "getCustom_Playlist_LV" + printpoint + space + "returned" + space2 + str(returned) + space + "Custom_Playlist1_ID" + space2 + str(Custom_Playlist1_ID)
	return returned

def setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, name, viewtype):
	printpoint = "" ; extra = "" ; New_Type = ""
	if "&list=PL" in New_ID:
		'''Playlist'''
		New_Type = localize(559) #Playlist
		extra = addonString_servicehtpt(47).encode('utf-8') % (New_Type) + space + addonString_servicehtpt(49).encode('utf-8') #New %s, Update Succesfully!
		New_ID = find_string(New_ID, "&list=PL", "")
		New_ID = New_ID.replace("&list=","&youtube_pl=")
		New_ID_ = New_ID.replace("&youtube_pl=","")
		'''---------------------------'''
	elif "/user/" in New_ID or "/channel/" in New_ID:
		'''Channel'''
		New_Type = localize(19029) #Channel
		extra = addonString_servicehtpt(46).encode('utf-8') % (New_Type) + space + addonString_servicehtpt(48).encode('utf-8') #New %s, Update Succesfully!
		if "/channel/" in New_ID:
			New_ID = find_string(New_ID, "/channel/", "")
			New_ID = New_ID.replace("/channel/", "&youtube_ch=")
		elif "/user/"    in New_ID:
			New_ID = find_string(New_ID, "/user/", "")
			New_ID = New_ID.replace("/user/", "&youtube_ch=")
			
		New_ID_ = New_ID.replace("&youtube_ch=","")
		'''---------------------------'''
	elif "watch?v=" in New_ID:
		'''Single Video'''
		New_Type = localize(157) #Video
		extra = addonString_servicehtpt(46).encode('utf-8') % (New_Type) + space + addonString_servicehtpt(48).encode('utf-8') #New %s, Update Succesfully!
		New_ID = find_string(New_ID, "watch?v=", "")
		New_ID = New_ID.replace("watch?v=", "&youtube_id=")
		New_ID_ = New_ID.replace("&youtube_id=","")
		'''---------------------------'''
	
	elif New_ID == "None":
		New_Type = localize(2080) #Empty list
		extra = addonString_servicehtpt(47).encode('utf-8') % (New_Type) + space + addonString_servicehtpt(49).encode('utf-8') #New %s, Update Succesfully!
		New_ID_ = ""
		
	if New_Type != "":
		if New_ID in url:
			check = dialogyesno(addonString(12).encode('utf-8'), localize(19194)) # Duplicated URL found!, Continue?
			if check == "ok": pass				
			else: notification_common("9") ; printpoint = printpoint + "8"
		
		if not "8" in printpoint:
			if mode == 20:
				setsetting(Custom_Playlist_ID, New_ID)
			elif mode == 21:
				setsetting(Custom_Playlist_ID, str(url) + "," + New_ID)
				#extra = "Previous ID: " + str(url)		
			#extra = addonString_servicehtpt(46).encode('utf-8') % (New_Type) + space + addonString_servicehtpt(48).encode('utf-8')
			dialogok(extra, "ID: " + str(New_ID_), str(name), "") ; xbmc.sleep(100)
			update_view(url, viewtype)
			'''---------------------------'''

	else: notification_common("17")
	
	if admin and not admin2 and admin3:
		print printfirst + "setCustom_Playlist_ID_LV" + printpoint + space + "name" + space2 + str(name) + newline + \
		"New_Type" + space2 + str(New_Type) + space + "New_ID" + space2 + str(New_ID) + space + "New_ID_" + space2 + str(New_ID_) + space
		'''---------------------------'''

def AdvancedCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	'''------------------------------
	---Save and Load your addon-design
	------------------------------'''
	printpoint = "" ; extra = "" ; formula = "" ; formula_ = "" ; path = "" ; file1 = "" ; file2 = "" ; file3 = "" ; returned = "" ; returned2 = ""; returned3 = "" ; y = "s"
	
	if name == addonString(6).encode('utf-8'):
		list = ['-> (Exit)']
		list.append(localize(190) + space + localize(593)) #Save All
		list.append(addonString_servicehtpt(51).encode('utf-8') + space + localize(593) + space + "[LOCAL]") #Load All [LOCAL]
		list.append(addonString_servicehtpt(51).encode('utf-8') + space + localize(593) + space + "[REMOTE]") #Load All [REMOTE] 
		list.append(localize(10035) + space + localize(593)) #Reset All
		y = "s"
		'''---------------------------'''
	else:
		list = ['-> (Exit)']
		list.append(localize(190) + space + addonString_servicehtpt(57).encode('utf-8')) #Save One
		list.append(addonString_servicehtpt(51).encode('utf-8') + space + addonString_servicehtpt(57).encode('utf-8') + space + "[LOCAL]") #Load One [LOCAL]
		list.append(addonString_servicehtpt(51).encode('utf-8') + space + addonString_servicehtpt(57).encode('utf-8') + space + "[REMOTE]") #Load One [REMOTE]
		y = ""
		
		Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
		if Custom_Playlist_ID == "": notification("Error ID", "Use HTPT Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
		Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
		Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
		Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
		'''---------------------------'''
	returned, value = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		
		if returned == 1 or returned == 2: path = os.path.join(addondata_path, addonID, '')
		elif returned == 3: path = os.path.join(addonPath, 'resources', 'templates', '')
		elif returned == 4: pass
		else: path = ""
		
		if path != "":

			if returned == 3:
				check = dialogyesno(addonString(15).encode('utf-8'), addonString(22).encode('utf-8')) #Share My Music buttons, Choose YES to learn how to share Your Music button
				if check == 'ok':
					header = addonString(15).encode('utf-8')
					msg1 = localize(190) + space + localize(592) ; msg1.decode('utf-8').encode('utf-8') #; msg1 = '[B]' + msg1 + '[/B]'
					msg2 = os.path.join(addondata_path, addonID) ; msg2 = msg2.decode('utf-8').encode('utf-8')
					message = "1. " + addonString(17).encode('utf-8') % (msg1) + ".[CR]" + "2. " + addonString(18).encode('utf-8') + "[CR]" + msg2 + ".[CR]" + "3. " + addonString_servicehtpt(52).encode('utf-8') + "[CR]" + "4. " + addonString_servicehtpt(53).encode('utf-8') % ("templates") + "[CR]" + "5. " + addonString_servicehtpt(54).encode('utf-8') + ".[CR]" + "6. " + addonString(19).encode('utf-8') + ".[CR]" + "7. " + addonString_servicehtpt(55).encode('utf-8') + ".[CR]" + "8. " + addonString_servicehtpt(56).encode('utf-8') % ("Commit") + ".[CR][CR]" + "*You should now wait for the next addon update."
					diaogtextviewer(header,message)
					
			'''read existing files'''
			file1 = os.path.join(path, "Addon_SavedButton"+y+"1.txt")
			file2 = os.path.join(path, "Addon_SavedButton"+y+"2.txt")
			file3 = os.path.join(path, "Addon_SavedButton"+y+"3.txt")
			'''---------------------------'''
			
			if os.path.exists(file1):
				infile1 = read_from_file(file1, silent=True)
				filename1 = regex_from_to(infile1, "&name=", "&", excluding=True)
			else: filename1 = None
			if os.path.exists(file2):
				infile2 = read_from_file(file2, silent=True)
				filename2 = regex_from_to(infile2, "&name=", "&", excluding=True)
			else: filename2 = None
			if os.path.exists(file3):
				infile3 = read_from_file(file3, silent=True)
				filename3 = regex_from_to(infile3, "&name=", "&", excluding=True)
			else: filename3 = None
			
			value1 = 'NO.' + space + "1" + space + "(" + str(filename1) + ")"
			value2 = 'NO.' + space + "2" + space + "(" + str(filename2) + ")"
			value3 = 'NO.' + space + "3" + space + "(" + str(filename3) + ")"
			
			'''save/load'''
			if filename1 == None: value1 = '[COLOR=Red]' + value1 + '[/COLOR]'
			if filename2 == None: value2 = '[COLOR=Red]' + value2 + '[/COLOR]'
			if filename3 == None: value3 = '[COLOR=Red]' + value3 + '[/COLOR]'
		
			list = ['-> (Exit)', value1, value2, value3]
				
			returned2, value2 = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
			
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
			
			if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
				
				if returned2 == 1: printpoint = printpoint + "1" #1
				elif returned2 == 2: printpoint = printpoint + "2" #2
				elif returned2 == 3: printpoint = printpoint + "3" #3
				
				if returned == 1: printpoint = printpoint + "A" #SAVE
				elif returned == 2: printpoint = printpoint + "B" #LOAD
				elif returned == 3: printpoint = printpoint + "C" #TEMPLATES
		
				if "A" in printpoint:
					if y == "s":
						'''------------------------------
						---Save-All-----------------------
						------------------------------'''
						formula = ""

						if Custom_Playlist1_ID != "":
							formula = "Custom_Playlist1_ID" + "=5" + Custom_Playlist1_ID
							formula = formula + newline + "Custom_Playlist1_Description" + "=5" + Custom_Playlist1_Description
							formula = formula + newline + "Custom_Playlist1_Fanart" + "=5" + Custom_Playlist1_Fanart
							formula = formula + newline + "Custom_Playlist1_Name" + "=5" + Custom_Playlist1_Name
							formula = formula + newline + "Custom_Playlist1_Thumb" + "=5" + Custom_Playlist1_Thumb
						if Custom_Playlist2_ID != "":
							formula = formula + newline + "Custom_Playlist2_ID" + "=5" + Custom_Playlist2_ID + "=5" + Custom_Playlist2_ID
							formula = formula + newline + "Custom_Playlist2_Description" + "=5" + Custom_Playlist2_Description
							formula = formula + newline + "Custom_Playlist2_Fanart" + "=5" + Custom_Playlist2_Fanart
							formula = formula + newline + "Custom_Playlist2_Name" + "=5" + Custom_Playlist2_Name
							formula = formula + newline + "Custom_Playlist2_Thumb" + "=5" + Custom_Playlist2_Thumb
						if Custom_Playlist3_ID != "":
							formula = formula + newline + "Custom_Playlist3_ID" + "=5" + Custom_Playlist3_ID + "=5" + Custom_Playlist3_ID
							formula = formula + newline + "Custom_Playlist3_Description" + "=5" + Custom_Playlist3_Description
							formula = formula + newline + "Custom_Playlist3_Fanart" + "=5" + Custom_Playlist3_Fanart
							formula = formula + newline + "Custom_Playlist3_Name" + "=5" + Custom_Playlist3_Name
							formula = formula + newline + "Custom_Playlist3_Thumb" + "=5" + Custom_Playlist3_Thumb
						if Custom_Playlist4_ID != "":
							formula = formula + newline + "Custom_Playlist4_ID" + "=5" + Custom_Playlist4_ID + "=5" + Custom_Playlist4_ID
							formula = formula + newline + "Custom_Playlist4_Description" + "=5" + Custom_Playlist4_Description
							formula = formula + newline + "Custom_Playlist4_Fanart" + "=5" + Custom_Playlist4_Fanart
							formula = formula + newline + "Custom_Playlist4_Name" + "=5" + Custom_Playlist4_Name
							formula = formula + newline + "Custom_Playlist4_Thumb" + "=5" + Custom_Playlist4_Thumb
						if Custom_Playlist5_ID != "":
							formula = formula + newline + "Custom_Playlist5_ID" + "=5" + Custom_Playlist5_ID + "=5" + Custom_Playlist5_ID
							formula = formula + newline + "Custom_Playlist5_Description" + "=5" + Custom_Playlist5_Description
							formula = formula + newline + "Custom_Playlist5_Fanart" + "=5" + Custom_Playlist5_Fanart
							formula = formula + newline + "Custom_Playlist5_Name" + "=5" + Custom_Playlist5_Name
							formula = formula + newline + "Custom_Playlist5_Thumb" + "=5" + Custom_Playlist5_Thumb
						if Custom_Playlist6_ID != "":
							formula = formula + newline + "Custom_Playlist6_ID" + "=5" + Custom_Playlist6_ID + "=5" + Custom_Playlist6_ID
							formula = formula + newline + "Custom_Playlist6_Description" + "=5" + Custom_Playlist6_Description
							formula = formula + newline + "Custom_Playlist6_Fanart" + "=5" + Custom_Playlist6_Fanart
							formula = formula + newline + "Custom_Playlist6_Name" + "=5" + Custom_Playlist6_Name
							formula = formula + newline + "Custom_Playlist6_Thumb" + "=5" + Custom_Playlist6_Thumb
						if Custom_Playlist7_ID != "":
							formula = formula + newline + "Custom_Playlist7_ID" + "=5" + Custom_Playlist7_ID + "=5" + Custom_Playlist7_ID
							formula = formula + newline + "Custom_Playlist7_Description" + "=5" + Custom_Playlist7_Description
							formula = formula + newline + "Custom_Playlist7_Fanart" + "=5" + Custom_Playlist7_Fanart
							formula = formula + newline + "Custom_Playlist7_Name" + "=5" + Custom_Playlist7_Name
							formula = formula + newline + "Custom_Playlist7_Thumb" + "=5" + Custom_Playlist7_Thumb
						if Custom_Playlist8_ID != "":
							formula = formula + newline + "Custom_Playlist8_ID" + "=5" + Custom_Playlist8_ID + "=5" + Custom_Playlist8_ID
							formula = formula + newline + "Custom_Playlist8_Description" + "=5" + Custom_Playlist8_Description
							formula = formula + newline + "Custom_Playlist8_Fanart" + "=5" + Custom_Playlist8_Fanart
							formula = formula + newline + "Custom_Playlist8_Name" + "=5" + Custom_Playlist8_Name
							formula = formula + newline + "Custom_Playlist8_Thumb" + "=5" + Custom_Playlist8_Thumb
						if Custom_Playlist9_ID != "":
							formula = formula + newline + "Custom_Playlist9_ID" + "=5" + Custom_Playlist9_ID + "=5" + Custom_Playlist9_ID
							formula = formula + newline + "Custom_Playlist9_Description" + "=5" + Custom_Playlist9_Description
							formula = formula + newline + "Custom_Playlist9_Fanart" + "=5" + Custom_Playlist9_Fanart
							formula = formula + newline + "Custom_Playlist9_Name" + "=5" + Custom_Playlist9_Name
							formula = formula + newline + "Custom_Playlist9_Thumb" + "=5" + Custom_Playlist9_Thumb
						if Custom_Playlist10_ID != "":
							formula = formula + newline + "Custom_Playlist10_ID" + "=5" + Custom_Playlist10_ID + "=5" + Custom_Playlist10_ID
							formula = formula + newline + "Custom_Playlist10_Description" + "=5" + Custom_Playlist10_Description
							formula = formula + newline + "Custom_Playlist10_Fanart" + "=5" + Custom_Playlist10_Fanart
							formula = formula + newline + "Custom_Playlist10_Name" + "=5" + Custom_Playlist10_Name
							formula = formula + newline + "Custom_Playlist10_Thumb" + "=5" + Custom_Playlist10_Thumb
					elif y == "":
						'''------------------------------
						---Save-One-----------------------
						------------------------------'''
						formula = ""

						if Custom_Playlist_ID != "":
							formula = Custom_Playlist_ID + "=5" + getsetting(Custom_Playlist_ID)
							formula = formula + newline + Custom_Playlist_Fanart + "=5" + getsetting(Custom_Playlist_Fanart)
							formula = formula + newline + Custom_Playlist_Name + "=5" + getsetting(Custom_Playlist_Name)
							formula = formula + newline + Custom_Playlist_Thumb + "=5" + getsetting(Custom_Playlist_Thumb)
							formula = formula + newline + Custom_Playlist_Description + "=5" + getsetting(Custom_Playlist_Description)
							'''---------------------------'''
							
					if "1" in printpoint:
						if filename1 == None: filename = ""
						else: filename = filename1
					elif "2" in printpoint:
						if filename2 == None: filename = ""
						else: filename = filename2
					elif "3" in printpoint:
						if filename3 == None: filename = ""
						else: filename = filename3
					
					filename = dialogkeyboard(filename, localize(21821), 0, "", "", "") #Description
					filename_ = "&name="+str(filename)+"&"
					formula = filename_ + newline + formula
					
					try: formula.encode('utf-8')
					except: pass
					
					if "1" in printpoint:
						write_to_file(file1, str(formula), append=False, silent=True, utf8=False)
						#setsetting('Addon_SavedButton'+y+'1', str(formula))
					elif "2" in printpoint:
						write_to_file(file2, str(formula), append=False, silent=True, utf8=False)
						#setsetting('Addon_SavedButton'+y+'2', str(formula))
					elif "3" in printpoint:
						write_to_file(file3, str(formula), append=False, silent=True, utf8=False)
						#setsetting('Addon_SavedButton'+y+'3', str(formula))
						'''---------------------------'''
					
					if y == "s": notification(addonString(20).encode('utf-8') + space + addonString_servicehtpt(58).encode('utf-8'), str(filename), "", 4000) #Your Music buttons Saved Succesfully!, 
					elif y == "": notification(addonString(21).encode('utf-8') + space + addonString_servicehtpt(59).encode('utf-8'), str(filename), "", 4000) #Your Music button Saved Succesfully!, 
				
				elif "B" in printpoint or "C" in printpoint:
					'''------------------------------
					---Load/Templates----------------
					------------------------------'''

					if "1" in printpoint:
						if filename1 == None: printpoint = printpoint + "Q"
						else: file = file1
					elif "2" in printpoint:
						if filename2 == None: printpoint = printpoint + "Q"
						else: file = file2
					elif "3" in printpoint:
						if filename2 == None: printpoint = printpoint + "Q"
						else: file = file3
					
					if "Q" in printpoint or file == "":
						'''nothing to load'''
						if "C" in printpoint: notification(localize(19055), "Share Your Music button first.", "", 4000) #No information available
						else:
							if y == "": extra2 = localize(190) + space + localize(592)
							else: extra2 = localize(190) + space + localize(593)
							extra2 = extra2.decode('utf-8').encode('utf-8')
							notification(localize(19055), addonString(14).encode('utf-8') % (extra2), "", 4000) #No information available
					else:
						#formula_ = formula_.split(',')
						#formula_ = CleanString(formula_, filter=[])
						import fileinput
						for line in fileinput.input([file]):
							x = "" ; x1 = "" ; x2 = "" ; x3 = ""
							if "=5" in line:
								'''setsetting'''
								x = line.replace("=5","=")
								x1 = find_string(x, "", "=")
								x2 = find_string(x, "=", "")
								x1 = x1.replace("=","")
								x2 = x2.replace('=&', '&') #CLEAN STRINGS
								x2 = x2.replace('\n', '') #CLEAN STRINGS
								if not "_ID" in x:
									'''Clean values for none ID lines'''
									x2 = x2.replace("=","")
									#x2 = x2.replace("\n","")
								
								if y == "":
									count = 0
									while count <= 10 and not xbmc.abortRequested:
										if str(count) in x1:
											x1 = x1.replace(str(count), str(num))
											count = 40
										else: count += 1
								setsetting(str(x1), str(x2))
								
							if admin3 and admin and not admin2: extra = extra + newline + space + "line" + space2 + str(line) + space + "x" + space2 + str(x) + space + "x1" + space2 + str(x1) + space + "x2" + space2 + str(x2) + space + "x3" + space2 + str(x3)
							'''---------------------------'''	
		elif returned == 4:
			'''------------------------------
			---Reset-All---------------------
			------------------------------'''
			returned = dialogyesno(localize(10035) + space + localize(593) + space + "(" + localize(19291) + ")", "You may want to SAVE your settings just in case..") #Reset all (Delete permanently),
			if returned == 'ok':
				file = os.path.join(addondata_path, addonID, 'settings.xml')
				removefiles(file) ; xbmc.sleep(500)
				setsetting('General_AutoView', General_AutoView)
				setsetting('General_TVModeShuffle', General_TVModeShuffle)
				setsetting('General_TVModeDialog', General_TVModeDialog)
				setsetting('Addon_ShowLog', Addon_ShowLog)
				setsetting('Addon_ShowLog2', Addon_ShowLog2)
				setsetting('Addon_Update', Addon_Update)
				setsetting('Addon_UpdateDate', Addon_UpdateDate)
				setsetting('Addon_UpdateLog', Addon_UpdateLog)
				setsetting('Addon_Version', Addon_Version)
				setsetting('Fanart_Enable', Fanart_Enable)
				setsetting('Fanart_EnableCustom', Fanart_EnableCustom)
				setsetting('Fanart_Custom100', Fanart_Custom100)
				setsetting('Fanart_Custom101', Fanart_Custom101)
				setsetting('Fanart_Custom102', Fanart_Custom102)
				setsetting('Fanart_Custom103', Fanart_Custom103)
				setsetting('Fanart_Custom104', Fanart_Custom104)
				setsetting('Fanart_Custom105', Fanart_Custom105)
				setsetting('Fanart_Custom106', Fanart_Custom106)
				setsetting('Fanart_Custom107', Fanart_Custom107)
				setsetting('Fanart_Custom108', Fanart_Custom108)
				setsetting('Fanart_Custom109', Fanart_Custom109)
				setsetting('Fanart_Custom110', Fanart_Custom110)
				setsetting('Fanart_Custom111', Fanart_Custom111)
				setsetting('Fanart_Custom112', Fanart_Custom112)
				setsetting('Fanart_Custom113', Fanart_Custom113)
				setsetting('Fanart_Custom114', Fanart_Custom114)
				setsetting('Fanart_Custom115', Fanart_Custom115)
				setsetting('Fanart_Custom116', Fanart_Custom116)
				setsetting('Fanart_Custom117', Fanart_Custom117)
				setsetting('Fanart_Custom118', Fanart_Custom118)
				setsetting('Fanart_Custom119', Fanart_Custom119)
				setsetting('Fanart_Custom120', Fanart_Custom120)
				setsetting('Fanart_Custom121', Fanart_Custom121)
				setsetting('Fanart_Custom122', Fanart_Custom122)
				setsetting('Fanart_Custom123', Fanart_Custom123)
				setsetting('Fanart_Custom124', Fanart_Custom124)
				setsetting('Fanart_Custom125', Fanart_Custom125)
				setsetting('Fanart_Custom126', Fanart_Custom126)
				setsetting('Fanart_Custom127', Fanart_Custom127)
				setsetting('Fanart_Custom128', Fanart_Custom128)
				setsetting('Fanart_Custom129', Fanart_Custom129)
				setsetting('Fanart_Custom130', Fanart_Custom130)
				
				
				
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		if not "Q" in printpoint and not "A" in printpoint:
			notification(".","","",1000)
			xbmc.sleep(500)
			notification("..","","",1000)
			update_view(url, viewtype)
			'''---------------------------'''
			
	if admin and not admin2 and admin3:
		print printfirst + 'AdvancedCustom' + space2 + 'name_' + space2 + name + "_LV" + printpoint + space + newline + \
		"path" + space2 + str(path) + newline + \
		"file1" + space2 + str(file1) + newline + \
		"file2" + space2 + str(file2) + newline + \
		"file3" + space2 + str(file3) + newline + \
		"formula" + space2 + str(formula) + space + "formula_" + space2 + str(formula_) + newline + \
		"extra" + space2 + str(extra)
		#"Addon_SavedButtons1" + space2 + str(Addon_SavedButtons1) + newline + \
		
def AddCustom(mode, name, url, iconimage, desc, num, viewtype):
	'''------------------------------
	---New-Button--------------------
	------------------------------'''
	printpoint = ""
	Custom_Playlist_ID = getCustom_Playlist(admin) ; New_Type = "" ; New_ID = "" ; New_Name = ""
	Custom_Playlist_Name = Custom_Playlist_ID.replace("_ID","_Name")
	if Custom_Playlist_ID == "": notification("Playlist limit reached!", "You may delete some playlists and try again!", "", 4000)
	else:
		New_ID = dialogkeyboard("", "Enter YouTube URL", 0, "5", "" , "")
		if New_ID != "skip":
			New_Name = dialogkeyboard("My Music", "Button Name", 0, "",Custom_Playlist_Name, "0")
			setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, New_Name, viewtype)
				
	if admin and not admin2 and admin3: print printfirst + "AddCustom_LV" + printpoint + space + "name" + space2 + str(name)
	'''---------------------------'''
	
def CheckMoveCustom(name, num):
	extra = "" ; printpoint = "" ; down = "" ; up = ""
	
	'''---------------------------'''
	if num == "1":
		'''---------------------------'''
		if Custom_PlaylistL[1] != "": down = "2"
		elif Custom_PlaylistL[2] != "": down = "3"
		elif Custom_PlaylistL[3] != "": down = "4"
		elif Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "2":
		if Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[2] != "": down = "3"
		elif Custom_PlaylistL[3] != "": down = "4"
		elif Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "3":
		if Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[3] != "": down = "4"
		elif Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "4":
		if Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "5":
		if Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "6":
		if Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "7":
		if Custom_PlaylistL[6] != "": up = "7"
		elif Custom_PlaylistL[5] != "": up = "6"
		elif Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[8] != "": up = "9"
		elif Custom_PlaylistL[9] != "": up = "10"
		'''---------------------------'''
	elif num == "8":
		if Custom_PlaylistL[7] != "": up = "8"
		elif Custom_PlaylistL[6] != "": up = "7"
		elif Custom_PlaylistL[5] != "": up = "6"
		elif Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "10":
		if Custom_PlaylistL[8] != "": up = "9"
		elif Custom_PlaylistL[7] != "": up = "8"
		elif Custom_PlaylistL[6] != "": up = "7"
		elif Custom_PlaylistL[5] != "": up = "6"
		elif Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
	
	if admin and not admin2 and admin3:
		print printfirst + "CheckMoveCustom_LV" + printpoint + space + "name" + space2 + str(name) + space + "num" + space2 + str(num) + space + "down" + space2 + str(down) + space + "up" + space2 + str(up)
		
	return up, down

def cleanfanartCustom(fanart):
	printpoint = ""
	fanart2 = fanart.replace("/","")
	fanart2 = fanart2.replace("\\","")
	addonFanart2 = addonFanart.replace("/","")
	addonFanart2 = addonFanart2.replace("\\","")
	if fanart2 == addonFanart2:
		printpoint = printpoint + "7"
		fanart = "" # or not os.path.exists(fanart)
	
	if admin and not admin2 and admin3:
		print printfirst + "cleanfanartCustom_LV" + printpoint + newline + \
		"fanart" + space2 + str(fanart) + newline + \
		"fanart2" + space2 + str(fanart2) + newline + \
		"addonFanart" + space2 + str(addonFanart) + newline + \
		"addonFanart2" + space2 + str(addonFanart2)
	return fanart
	
def MoveCustom(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''23'''
	printpoint = ""
	'''---------------------------'''
	if not "__" in num: printpoint = printpoint + "9"
	else:
		printpoint = printpoint + "1"
		num = num.split("__")
		num1 = num[0]
		num2 = num[1]
	try:
		test = int(num1) + 1
		test = int(num2) + 1
	except Exception, TypeError: printpoint = printpoint + "9"
	
	fanart = cleanfanartCustom(fanart)
	
	if not "9" in printpoint:
		printpoint = printpoint + "3"
		Custom_Playlist_ID = "Custom_Playlist" + num1 + "_ID"
		if Custom_Playlist_ID == "": notification("Error ID", "Use HTPT Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name = "Custom_Playlist" + num1 + "_Name"
		Custom_Playlist_Thumb = "Custom_Playlist" + num1 + "_Thumb"
		Custom_Playlist_Description = "Custom_Playlist" + num1 + "_Description"
		Custom_Playlist_Fanart = "Custom_Playlist" + num1 + "_Fanart"
		'''---------------------------'''
		Custom_Playlist_ID2 = "Custom_Playlist" + str(num2) + "_ID"
		if Custom_Playlist_ID2 == "": notification("Error ID", "Use HTPT Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name2 = "Custom_Playlist" + str(num2) + "_Name"
		Custom_Playlist_Thumb2 = "Custom_Playlist" + str(num2) + "_Thumb"
		Custom_Playlist_Description2 = "Custom_Playlist" + str(num2) + "_Description"
		Custom_Playlist_Fanart2 = "Custom_Playlist" + str(num2) + "_Fanart"
		'''---------------------------'''
	
	if not "9" in printpoint:
		printpoint = printpoint + "7"
		'''---------------------------'''
		setsetting(Custom_Playlist_ID, getsetting(Custom_Playlist_ID2))
		setsetting(Custom_Playlist_Name, getsetting(Custom_Playlist_Name2))
		setsetting(Custom_Playlist_Thumb, getsetting(Custom_Playlist_Thumb2))
		setsetting(Custom_Playlist_Description, getsetting(Custom_Playlist_Description2))
		setsetting(Custom_Playlist_Fanart, getsetting(Custom_Playlist_Fanart2))
		'''---------------------------'''
		setsetting(Custom_Playlist_ID2, url)
		setsetting(Custom_Playlist_Name2, name)
		setsetting(Custom_Playlist_Thumb2, iconimage)
		setsetting(Custom_Playlist_Description2, desc)
		setsetting(Custom_Playlist_Fanart2, fanart)
		'''---------------------------'''
		update_view(url, viewtype)
	
	if admin and not admin2 and admin3:
		print printfirst + "MoveCustom_LV" + printpoint + space + "url" + space2 + str(url) + space + "num" + space2 + str(num)
		
def ManageCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	extra = "" ; printpoint = "" ; New_ID = ""
	
	Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
	if Custom_Playlist_ID == "": notification("Error ID", "Use HTPT Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
	Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
	Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
	Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
	Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
	
	if printpoint != "9":
		list = ['-> (Exit)']
		list.append(addonString_servicehtpt(38).encode('utf-8')) #Edit URL
		list.append(addonString_servicehtpt(41).encode('utf-8')) #Rename Button
		if thumb == "": list.append(addonString_servicehtpt(36).encode('utf-8')) #Add Thumb
		else: list.append(addonString_servicehtpt(37).encode('utf-8')) #Remove Thumb
		if desc == "": list.append(addonString_servicehtpt(32).encode('utf-8')) #Add Description
		else: list.append(addonString_servicehtpt(33).encode('utf-8')) #Edit Description
		fanart = cleanfanartCustom(getsetting(Custom_Playlist_Fanart))
		if fanart == "": list.append(addonString_servicehtpt(34).encode('utf-8')) #Add Fanart
		else: list.append(addonString_servicehtpt(35).encode('utf-8')) #Remove Fanart
		list.append(localize(13336)) #'Remove Button'

		returned, value = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
			
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
	
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		if returned == 1: printpoint = printpoint + "A" #Edit URL
		elif returned == 2: printpoint = printpoint + "B" #Rename
		elif returned == 3: printpoint = printpoint + "C" #Add/Remove Thumb
		elif returned == 4: printpoint = printpoint + "D" #Add/Edit Description
		elif returned == 5: printpoint = printpoint + "E" #Add/Remove Fanart
		elif returned == 6: printpoint = printpoint + "F" #Remove Button
		'''---------------------------'''
	if "A" in printpoint:
		'''------------------------------
		---Edit-URL----------------------
		------------------------------'''
		list = ['-> (Exit)']
		list.append(addonString_servicehtpt(42).encode('utf-8')) #View URL
		list.append(addonString_servicehtpt(40).encode('utf-8')) #Add URL
		list.append(addonString_servicehtpt(39).encode('utf-8')) #Remove URL
		
		returned2, value = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
			
		if returned2 == -1: printpoint = printpoint + "9"
		elif returned2 == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
		if returned2 == 1: printpoint = printpoint + "1" #View URL
		elif returned2 == 2: printpoint = printpoint + "2" #Add URL
		elif returned2 == 3: printpoint = printpoint + "3" #Remove URL
		
		if "1" in printpoint:
			'''------------------------------
			---View-URL----------------------
			------------------------------'''
			message2 = "" ; i = 0
			url2 = url.split(",")
			for x in url2:
				i += 1
				x2 = ""
				if "&youtube_ch=" in x:
					x = x.replace("&youtube_ch=","")
					x2 = space + "[" + "YouTube Channel" + "]"
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					x = x.replace("&youtube_pl=","")
					x2 = space + "[" + "YouTube Playlist" + "]"
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					x2 = space + "[" + "YouTube Video" + "]"
					'''---------------------------'''
				if x2 != "": message2 = message2 + '[CR]' + str(i) + space2 + str(x) + str(x2)
				'''---------------------------'''
			header = addonString_servicehtpt(42).encode('utf-8') + space2 + str(name)
			if message2 != "": message = message2 + '[CR][CR]' + addonString(7).encode('utf-8')
			else: message = addonString(9).encode('utf-8') #URL Error occured.
			diaogtextviewer(header,message)
			'''---------------------------'''
			
		elif "2" in printpoint:
			'''------------------------------
			---Add-URL-----------------------
			------------------------------'''
			New_ID = dialogkeyboard("", addonString_servicehtpt(40).encode('utf-8'), 0, "5", "" , "")
			setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, name, viewtype)
			
				
		elif "3" in printpoint:
			'''------------------------------
			---Remove-URL--------------------
			------------------------------'''
			list = ['-> (Exit)']
			url2 = url.split(',')
			i = 0
			for x in url2:
				i += 1
				list.append(x)

			returned2, value = dialogselect(addonString_servicehtpt(31).encode('utf-8'),list,0)
				
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
			
			if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
				
				if i == 1:
					'''Warning 1 URL found!'''
					check = dialogyesno(localize(13336), addonString(10).encode('utf-8') + '[CR]' + addonString(11).encode('utf-8'))
					if check == "ok":
						'''Remove Button'''
						printpoint = printpoint + "F"
					else:
						'''Skip'''
				else:
					if value + "," in url:
						'''multi links'''
						value2 = url.replace(value + ",","",1)
					elif value in url:
						'''single link'''
						value2 = url.replace(value,"",1)
					else: value2 = ""
					if value2 == "": notification_common("17")
					else:
						setsetting(Custom_Playlist_ID, value2)
						notification(addonString_servicehtpt(44).encode('utf-8') + space + addonString_servicehtpt(43).encode('utf-8'),str(name), "", 4000) #URL Removed Succesfully!
						'''---------------------------'''
				
	elif "B" in printpoint:
		'''------------------------------
		---Rename-Button-----------------
		------------------------------'''
		New_Name = dialogkeyboard(name, addonString_servicehtpt(41).encode('utf-8'), 0, "", Custom_Playlist_Name, "0")
		if New_Name != "skip" and New_Name != name:
			notification(addonString_servicehtpt(45).encode('utf-8') + space + addonString_servicehtpt(30).encode('utf-8'), str(name), "", 4000) #Button Name Update Succesfully!
			'''---------------------------'''
		
	elif "C" in printpoint:
		if thumb == "":
			'''------------------------------
			---Add-Thumb---------------------
			------------------------------'''
			New_Thumb = ""
			returned = dialogyesno(str(name), addonString_servicehtpt(31).encode('utf-8'), nolabel=localize(20017), yeslabel=localize(20015))
			if returned == 'ok':
				'''remote'''
				x = localize(20015) #Remote thumb
				value = dialogkeyboard("", x + space + "URL", 0, "1", "", "")
				if value != "skip":
					returned = urlcheck(value, ping=False)
					if returned != "ok":
						notification("URL Error", "Try again..", "", 2000)
						header = "URL Error"
						message = "Examine your URL for errors:" + newline + '[B]' + str(value) + '[/B]'
						diaogtextviewer(header,message)
					else:
						New_Thumb = value
			else:
				'''local'''
				x = localize(20017) #Local thumb
				xbmc.executebuiltin('Skin.SetString('+addonID+'_Temp,)')
				xbmc.executebuiltin('Skin.SetImage('+addonID+'_Temp,)') ; xbmc.sleep(4000)
				dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
				while dialogfilebrowserW and not xbmc.abortRequested:
					xbmc.sleep(500)
					dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
					xbmc.sleep(500)
				xbmc.sleep(500)
				New_Thumb = xbmc.getInfoLabel('Skin.String('+addonID+'_Temp)')
			
			if New_Thumb != "":
				setsetting(Custom_Playlist_Thumb, New_Thumb)
				notification(str(x) + space + addonString_servicehtpt(30).encode('utf-8'), str(name), "", 4000) #Thumb* Update Succesfully!
				'''---------------------------'''
		else:
			'''------------------------------
			---Remove-Thumb------------------
			------------------------------'''
			if os.path.exists(thumb): x = localize(20017) #Local thumb
			else: x = localize(20015)
			setsetting(Custom_Playlist_Thumb, "")
			notification(str(x) + space + addonString_servicehtpt(43).encode('utf-8'), str(name), "", 2000) #Thumb* Removed Succesfully!
			'''---------------------------'''
			
	elif "D" in printpoint:
		'''------------------------------
		---Add-Description---------------
		------------------------------'''
		returned, value = getRandom("0", min=0, max=100, percent=50)
		if int(value) <= 10: notification("Tip New Line:", "[CR]", "", 4000)
		elif int(value) <= 20: notification("Tip Bold:", "[B]text[/B]", "", 4000)
		elif int(value) <= 30: notification("Tip Color:", "[COLOR=X]text[/COLOR]", "", 4000)
		elif int(value) <= 40: notification("Tip Italic:", "[I]text[/I]", "", 4000)
		
		if Custom_Playlist_Description == "": extra1 = addonString_servicehtpt(32).encode('utf-8') #Add Description
		else: extra1 = addonString_servicehtpt(33).encode('utf-8') #Edit Description
		
		returned = dialogkeyboard(desc, extra1, 0, "", Custom_Playlist_Description, "0")
		if returned != "skip":
			if returned == "": extra2 = addonString_servicehtpt(43).encode('utf-8') #Removed Succesfully!
			else: extra2 = addonString_servicehtpt(30).encode('utf-8') #Update Succesfully!
			if returned != desc: notification(localize(21821) + space + extra2, str(name), "", 4000) #Description Update/Removed Succesfully!
			'''---------------------------'''
	
	elif "E" in printpoint:
		
		if fanart == "":
			'''------------------------------
			---Add-Fanart----------------
			------------------------------'''
			New_Fanart = ""
			returned = dialogyesno(str(name), addonString_servicehtpt(31).encode('utf-8'), nolabel=localize(20438), yeslabel=localize(20441))
			if returned == 'ok':
				'''remote'''
				x = localize(20441) #Remote fanart
				value = dialogkeyboard("", localize(20441), 0, "1", "", "")
				if value != "skip":
					returned2 = urlcheck(value, ping=False)
					if returned2 != "ok":
						notification("URL Error", "Try again..", "", 2000)
						header = "URL Error"
						message = "Examine your URL for errors:" + newline + '[B]' + str(value) + '[/B]'
						diaogtextviewer(header,message)
					else:
						New_Fanart = value
			else:
				'''local'''
				x = localize(20438) #Local fanart
				xbmc.executebuiltin('Skin.SetString('+addonID+'_Temp,)')
				xbmc.executebuiltin('Skin.SetImage('+addonID+'_Temp,)') ; xbmc.sleep(4000)
				dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
				while dialogfilebrowserW and not xbmc.abortRequested:
					xbmc.sleep(500)
					dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
					xbmc.sleep(500)
				xbmc.sleep(500)
				New_Fanart = xbmc.getInfoLabel('Skin.String('+addonID+'_Temp)')
			
			if New_Fanart != "":
				setsetting(Custom_Playlist_Fanart, New_Fanart)
				 
				notification(str(x) + space + addonString_servicehtpt(30).encode('utf-8'), str(New_Fanart), "", 2000) #Fanart* Update Succesfully!
				xbmc.sleep(2000)
				if Fanart_Enable != "true": notification(addonString_servicehtpt(28).encode('utf-8') + space + localize(24023) + "!", "->" + localize(1045), "", 4000) # Allow Backgrounds Disabled, ->Add-on settings
				elif Fanart_EnableCustom != "true": notification(localize(21389) + space + localize(24023) + "!", "->" + localize(1045), "", 4000) # Enable custom background Disabled, ->Add-on settings
				'''---------------------------'''
		else:
			'''------------------------------
			---Remove-Fanart------------
			------------------------------'''
			setsetting(Custom_Playlist_Fanart, "")
			notification(localize(33068) + space + localize(19179) + "!", str(name), "", 4000) #Background Deleted!
			'''---------------------------'''
			
	if "F" in printpoint:
		if Custom_Playlist_Description != "":
			'''------------------------------
			---Remove-Button-----------------
			------------------------------'''
			returned = dialogyesno(localize(13336) + '[CR]' + str(name),localize(19194)) #Remove Button, Continue?
			if returned == "ok":
				setsetting(Custom_Playlist_ID, "")
				setsetting(Custom_Playlist_Name, "")
				setsetting(Custom_Playlist_Thumb, "")
				setsetting(Custom_Playlist_Description, "")
				setsetting(Custom_Playlist_Fanart, "")
				'''---------------------------'''
				if desc != "": extra1 = localize(21821) + space2 + str(desc)
				else: extra1 = ""
				dialogok(localize(50) + space + addonString_servicehtpt(43).encode('utf-8') + '[CR]' + str(name), "ID" + space2 + str(url), "", extra1)
				'''---------------------------'''
				
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		update_view(url, viewtype)
		#xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
	if admin and not admin2 and admin3:
		print printfirst + "ManageCustom_LV" + printpoint + space + "name" + space2 + str(name) + newline + \
		"Custom_Playlist_ID" + space2 + str(Custom_Playlist_ID) + newline + \
		"Custom_Playlist_Name" + space2 + str(Custom_Playlist_Name) + newline + \
		"Custom_Playlist_Thumb" + space2 + str(Custom_Playlist_Thumb) + newline + \
		"thumb" + space2 + str(thumb) + newline + \
		"Custom_Playlist_Description" + space2 + str(Custom_Playlist_Description) + newline + \
		"Custom_Playlist_Fanart" + space2 + str(Custom_Playlist_Fanart) + newline + \
		"fanart" + space2 + str(fanart) + newline + \
		"New_ID" + space2 + str(New_ID) + newline + \
		"url" + space2 + str(url) + newline
		'''---------------------------'''
		
def youtube_pl_to_youtube_id(x, playlist=[]):
	printpoint = "" ; TypeError = "" ; extra = "" ; page = 1 ; pagesize = 40
	valid_ = "" ; invalid_ = 0 ; invalid__ = "" ; duplicates_ = 0 ; duplicates__ = "" ; except_ = 0 ; except__ = ""
	
	returned = get_types(playlist)
	if not 'list' in returned: playlist = []
	
	if "&youtube_pl=" in x:
		printpoint = printpoint + "1"
		x = x.replace("&youtube_pl=","")
	elif "&youtube_se=" in x:
		printpoint = printpoint + "2"
		x = x.replace("&youtube_se=","")
		x = clean_commonsearch(x)
		
	
	
	if "1" in printpoint: url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+x+'&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4&part=snippet&maxResults=40&pageToken='
	elif "2" in printpoint:
		url = 'https://www.googleapis.com/youtube/v3/search?q='+x+'&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4&safeSearch=moderate&type=video&part=snippet&maxResults=40&pageToken='
		#url = url.decode('utf-8')
	else: printpoint = printpoint + "8"
	if admin and 1 + 1 == 2:
		pass
		print "123test" + space2 + str(x)
		print "123test" + space2 + str(url) + newline
		
	link = OPEN_URL(url)
	prms=json.loads(link)
	if admin:
		print "url" + space2 + str(url) + newline + \
		"link" + space2 + str(link) + newline + \
		"prms" + space2 + str(prms) + newline #+ \ + "totalResults" + space2 + str(totalResults)
		'''---------------------------'''

	totalResults=int(prms['pageInfo'][u'totalResults']) #if bigger than pagesize needs to add more result
	totalpagesN = (totalResults / pagesize) + 1
	'''---------------------------'''

	i = 0
	while i < pagesize and not i > totalResults and not "8" in printpoint and not xbmc.abortRequested: #h<totalResults
		try:
			#print "i" + space2 + str(i) + space + "duplicatesN" + space2 + str(duplicatesN)
			id = "" ; finalurl = ""
			if "1" in printpoint: id=str(prms['items'][i][u'snippet'][u'resourceId'][u'videoId']) #Video ID (Playlist)
			elif "2" in printpoint: id=str(prms['items'][i][u'id'][u'videoId']) #Video ID (Search)
			if id != "":
				finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
				title=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
				thumb=str(prms['items'][i][u'snippet'][u'thumbnails'][u'default'][u'url'])
				desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
				#id = "" ; finalurl = "" ; title = "" ; thumb = "" ; desc = ""
			
			if not finalurl in playlist and not "Deleted video" in title and not "Private video" in title and finalurl != "":
				#ok, liz = addLink(title,finalurl, thumb, desc)
				#name, url, mode, iconimage='DefaultFolder.png', desc="", num="", viewtype=""
				#playlist.append((finalurl ,liz))
				playlist.append(finalurl)
				'''---------------------------'''
			else:
				if "Deleted video" in title or "Private video" in title:
					invalid_ += 1
					invalid__ = "i" + space2 + str(i) + space + "id" + space2 + str(id)
				elif finalurl in playlist:
					duplicates_ += 1
					duplicates__ = "i" + space2 + str(i) + space + "id" + space2 + str(id)
					
		except Exception, TypeError:
			except_ += 1
			except__ = "i" + space2 + str(i) + space + "id" + space2 + str(id)
			if not 'list index out of range' in TypeError: extra = extra + newline + "i" + space2 + str(i) + space + "TypeError" + space2 + str(TypeError)
			else: printpoint = printpoint + "8"
			'''---------------------------'''
		
		i += 1
	numOfItems2 = totalResults - invalid_ - duplicates_ - except_
	if numOfItems2 > pagesize: numOfItems2 = 40
	totalpages = (numOfItems2 / pagesize) + 1

	nextpage = page + 1
	
	#if totalpages > page: addDir('[COLOR=Yellow]' + str33078.encode('utf-8') + '[/COLOR]',x,13,"special://skin/media/DefaultVideo2.png",str79528.encode('utf-8'),str(nextpage),50) #Next Page

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin:
		if duplicates__ != "": extra = "duplicates__" + space2 + str(duplicates__) + "(" + str(duplicates_) + ")" + newline + extra
		if invalid__ != "": extra = "invalid__" + space2 + str(invalid__) + "(" + str(invalid_) + ")" + newline + extra
		if except__ != "": extra = "except__" + space2 + str(except__) + "(" + str(except_) + ")" + newline + extra
		if playlist != []: extra = "playlist" + space2 + str(playlist) + newline + extra
		
		print printfirst + "youtube_pl_to_youtube_id_LV" + printpoint + space + "i" + space2 + str(i) + space + "totalResults" + space2 + str(totalResults) + space + "numOfItems2" + space2 + str(numOfItems2) + newline + \
		"x" + space2 + x + space + "page" + space2 + str(page) + " / " + str(totalpages) + space + "pagesize" + space2 + str(pagesize) + newline + \
		"extra" + space2 + str(extra)
		'''---------------------------'''
	return playlist, numOfItems2
	
def PlaylistsFromUser(user):
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#https://www.googleapis.com/youtube/v3/videos?id=<video_id>&key=<YOUR_API_KEY>&part=snippet
	#url ='https://www.googleapis.com/youtube/v3/videos?id='+user+'&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4&part=snippet'
	#url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+user+'&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4&part=snippet' #SEEM TO WORK!
	#url = 'https://www.googleapis.com/youtube/v3/playlistItems?channelId='+user+'&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4&part=snippet'
	#Get user's Channel ID - https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername={{user}}&key={{API key}}
	#url = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UCcYc90JDakyeXGeZgPL1ejA&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4'
	#url = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=UCcYc90JDakyeXGeZgPL1ejA&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4'
	#https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=jambrose42&key={YOUR_API_KEY}
	#url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=50&playlistId=UUpRmvjdu3ixew5ahydZ67uA&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4'
	#url='https://gdata.youtube.com/feeds/api/users/'+user+ '/playlists?alt=json&max-results=50'
	link = OPEN_URL(url)
	prms=json.loads(link)
	print "url" + space2 + str(url) + newline + \
	"link" + space2 + str(link) + newline + \
	"prms" + space2 + str(prms)
	TotalPlaylists=int(prms['items'][u'pageInfo$totalResults'][u'$t'])
	#TotalPlaylists=int(prms['feed'][u'openSearch$totalResults'][u'$t'])
	j=1
	h=1
	lst=[]
	pages= (TotalPlaylists//50)  +1
	while  j<=pages :
		link = OPEN_URL(url)
		prms=json.loads(link)
		i=0
		while h<TotalPlaylists +1  and i<50:
			thumb=''
			try:
				playlistid=str(prms['feed'][u'entry'][i][u'yt$playlistId'][u'$t'])
				title=str(prms['feed'][u'entry'][i][u'title'][u'$t'].encode('utf-8'))
				thumb=str(prms['feed'][u'entry'][i][u'media$group'][u'media$thumbnail'][2][u'url'])
			except:
				pass
			i=i+1
			h=h+1
			lst.append((playlistid,title,thumb))
		j=j+1
		url='https://gdata.youtube.com/feeds/api/users/'+user+ '/playlists?alt=json&max-results=50&start-index='+str (j*50-49)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "PlaylistsFromUser" + space2 + user + space + "TotalPlaylists" + space2 + str(TotalPlaylists) + space + "url" + space2 + url #"link" + space2 + link
	'''---------------------------'''
	return lst
	
def RanFromPlayList(playlistid):
	random.seed()
	url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=50'
	link = OPEN_URL(url)
	prms=json.loads(link)
	numOfItems=int(prms['feed'][u'openSearch$totalResults'][u'$t']) #if bigger than 50 needs  to add more result
	if numOfItems >1 :
		link = OPEN_URL(url)
		prms=json.loads(link)
		if numOfItems>49:
			numOfItems=49
		i=random.randint(1, numOfItems-1)
		#print str (len(prms['feed'][u'entry']))  +"and i="+ str(i)
		try:
			urlPlaylist= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$player'][0][u'url'])
			match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').findall(urlPlaylist)
			finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1" #finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
			title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
			thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
			desc= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
		except :
			 return "","","",""  # private video from youtube
		'''liz = xbmcgui.ListItem(title, iconImage="DefaultVideo.png", thumbnailImage=thumb)
		liz.setInfo( type="Video", infoLabels={ "Title": title} )
		liz.setProperty("IsPlayable","true")
		pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
		pl.clear()
		pl.add(finalurl, liz)'''
		#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
		return finalurl,title,thumb,desc
	else:
		return "","","",""

def myView(type):
	name = 'myView' ; value = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	if type == "A":
		if xbmc.getSkinDir() != "skin.htpt":
			try: value = int(General_AutoView_A)
			except: value = ""
		else: value = "50"
		
	elif type == "B":
		if xbmc.getSkinDir() != "skin.htpt":
			try: value = int(General_AutoView_B)
			except: value = ""
	elif type == "C":
		if xbmc.getSkinDir() != "skin.htpt":
			try: value = int(General_AutoView_C)
			except: value = ""

	if admin: print printfirst + name + space + "type" + space2 + str(type) + space + "value" + space2 + str(value)
	
	return value

def setView(content, viewType, containerfolderpath2):
	'''set content type so library shows more views and info'''
	name = 'setView' ; printpoint = ""
	
	if content:
		printpoint = printpoint + "1"
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if viewType == None:
		printpoint = printpoint + "2"
		if containerfolderpath2 == 'plugin://' + addonID + "/": viewType = 50
		elif viewType == None: pass
		elif content == 'episodes': viewType = 50
		elif content == 'seasons': viewType = 50
		elif content == 'tvshows': viewType = 58
		elif content == 'movies': viewType = 58
		

	if General_AutoView == "true" and viewType != None:
		if xbmc.getSkinDir() == 'skin.htpt':
			xbmc.executebuiltin("Container.SetViewMode(%s)" % str(viewType) )
			printpoint = printpoint + "7"
			'''---------------------------'''
		else: printpoint = printpoint + "8"
	else: printpoint = printpoint + "9"

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + name + "_LV" + printpoint + space + "content" + space2 + str(content) + space + "viewType" + space2 + str(viewType) + newline + \
	"containerfolderpath2" + space2 + containerfolderpath2
	'''---------------------------'''

def ShowFromUser(user):
	'''reads  user names from my subscriptions'''
	murl='https://gdata.youtube.com/feeds/api/users/'+user+'/shows?alt=json&start-index=1&max-results=50&v=2'
	resultJSON = json.loads(OPEN_URL(murl))
	shows=resultJSON['feed']['entry']
	#print shows[1]
	hasNext= True
	while hasNext:
		shows=resultJSON['feed']['entry']
		for  i in range (0, len(shows)) :
			showApiUrl=shows[i]['link'][1]['href']
			showApiUrl=showApiUrl[:-4]+'/content?v=2&alt=json'
			showName=shows[i]['title']['$t'].encode('utf-8')
			image= shows[i]['media$group']['media$thumbnail'][-1]['url']
			addDir(showName,showApiUrl,14,image,'','1',"")
		hasNext= resultJSON['feed']['link'][-1]['rel'].lower()=='next'
		if hasNext:
			resultJSON = json.loads(OPEN_URL(resultJSON['feed']['link'][-1]['href']))
			
def TVMode_check(admin, url, playlists):
	printpoint = ""
	returned = ""
	if General_TVModeDialog == "true":
		printpoint = printpoint + "1"
		#list = [40,41,42,43,44,45,46,47,48,49]
		#for i in list:
		#if "mode=" + str(i) in containerfolderpath: #or (i == 40 and containerfolderpath == "plugin://" + addonID + "/")
		#if admin: print printfirst + "YOUList-General_TVModeDialog" + space + "i" + space2 + str(i) + space + containerfolderpath
		printpoint = printpoint + "3"
		countl = 0
		for space in playlists:
			countl += 1
		countlS = str(countl)
		if playlists==[] or countl > 1:  #no playlists on  youtube channel
			'''------------------------------
			---PLAYLIST->-1------------------
			------------------------------'''
			printpoint = printpoint + "5"
			returned = dialogyesno(addonString_servicehtpt(7).encode('utf-8'), addonString_servicehtpt(8).encode('utf-8'))
			if returned == "ok": returned = TvMode(url)
			'''---------------------------'''
		else: printpoint = printpoint + "8"
				
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "TVMode_check_LV" + printpoint
	'''---------------------------'''
	return returned

def TvMode2(mode, name, url, iconimage, desc, num, viewtype):
	returned = ""
	if url == "None":
		'''Empty button'''
		notification("no valid URL founds!", "...", "", 2000)
	else:
		if General_TVModeDialog == "true":
			if General_TVModeShuffle == "true": extra = addonString_servicehtpt(8).encode('utf-8')
			else: extra = addonString_servicehtpt(61).encode('utf-8') + '[CR]' + addonString_servicehtpt(62).encode('utf-8')
			returned = dialogyesno(addonString_servicehtpt(7).encode('utf-8'), extra)
		
		if returned == "ok": mode = 5
		else: mode = 6
		
		MultiVideos(mode, name, url, iconimage, desc, num, viewtype)
		
		return mode
	
def TvMode(user):
	printpoint = ""
	returned = ""
	try: playlists=PlaylistsFromUser(user)
	except: playlists = []
	if playlists == []:  #no playlists on  youtube channel
		from default import CATEGORIES
		dialog = xbmcgui.Dialog()
		ok = dialog.ok('HTPT', addonString(302).encode('utf-8'))
		CATEGORIES()
	#print "str is" +  str(random.choice(playlists)[0])
	else:
		count = 0
		while count < 10 and xbmc.Player().isPlayingVideo() and not xbmc.abortRequested:
			xbmc.sleep(100)
			count += 1
			if count == 1: xbmc.executebuiltin('Action(Stop)')
		pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
		pl.clear()
		dp= xbmcgui.DialogProgress()
		dp.create('HTPT',"")
		PlayListGain = "" #URLS
		PlayListGain2 = 0 #DUPLICATES
		PlayListGain3 = "" #DELETES
		count = 0
		while count <= 40 and not "9" in printpoint and not xbmc.abortRequested:
			for i in range (1,41):  #40  RANDOM PROGRAMS IN TV MODE
				count += 1
				countS = str(count)
				if count == 1: dp.update(i*50, str79529.encode('utf-8'), "")
				else: dp.close()
				#print str (playlists)
				ran=str(random.choice(playlists)[0])
				finalurl,title,thumb,desc= RanFromPlayList(ran)
				liz = xbmcgui.ListItem(title, iconImage="DefaultVideo.png", thumbnailImage=thumb)
				liz.setInfo( type="Video", infoLabels={ "Title": title} )
				liz.setProperty("IsPlayable","true")
				
				if not finalurl in PlayListGain and not "Deleted video" in title: pl.add(finalurl, liz)
				elif "Deleted video" in title: PlayListGain3 = PlayListGain3 + space + finalurl
				else:
					PlayListGain2 = PlayListGain2 + 1
					if PlayListGain2 > 10:
						playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
						notification(addonString(305).encode('utf-8') % (str(playlistlength), str(PlayListGain2)),addonString(306).encode('utf-8'),"",4000)
						printpoint = printpoint + "9"
						#sys.exit()
						'''---------------------------'''
				PlayListGain = PlayListGain + space + finalurl
				if count == 1:
					dp.update(100, str79529.encode('utf-8'), "")
					xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
					count2 = 0
					while count2 < 10 and not xbmc.Player().isPlayingVideo() and not xbmc.abortRequested:
						xbmc.sleep(500)
						count2 += 1
						xbmc.sleep(500)
						'''---------------------------'''
				elif not xbmc.Player().isPlayingVideo(): printpoint = printpoint + "9" #sys.exit(1)
		playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
		playlistlengthN = int(playlistlength)
        if xbmc.Player().isPlayingVideo() and playlistlengthN > 5:
            printpoint = printpoint + "7"
            PlayListGain2S = str(PlayListGain2)
            notification(addonString(305).encode('utf-8') % (playlistlength, PlayListGain2S),addonString(306).encode('utf-8'),"",4000)
            print printfirst + "PlayListGain_" + countS + space + PlayListGain2S + space + "Duplicated Not Added!"
			#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
            '''---------------------------'''
			
        print printfirst + "TvMode" + space2 + "count" + space2 + countS + space + "PlayListGain2S" + space + PlayListGain2S + space + "PlayListGain3" + space2 + PlayListGain3
		
	if "7" in printpoint: returned = "ok"
	'''---------------------------'''
	return returned
	
def update_view(url, viewtype):
    ok=True
    xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
    if admin: print printfirst + "update_view" + space2 + "url" + space2 + str(url) + space + "viewtype" + space2 + str(viewtype)
    return ok

def unescape(text):
	try:            
		rep = {"&nbsp;": " ",
			   "\n": "",
			   "\t": "",
			   "\r":"",
			   "&#39;":"",
			   "&quot;":"\""
			   }
		for s, r in rep.items():
			text = text.replace(s, r)
			
		# remove html comments
		text = re.sub(r"<!--.+?-->", "", text)    
			
	except TypeError:
		pass

	return text

def urlcheck(url, ping=False):
	import urllib2
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	name = "urlcheck" ; printpoint = "" ; returned = "" ; extra = ""
	
	
	try:
		#urllib2.urlopen(url)
		request = urllib2.Request(url)
		response = urllib2.urlopen(request, timeout=7)
		#content = response.read()
		#f = urllib2.urlopen(url)
		#f.fp._sock.recv=None # hacky avoidance
		response.close()
		del response
		printpoint = printpoint + "7"
		
	except urllib2.HTTPError, e: 
		extra = extra + newline + str(e.code) + space + str(e)
		printpoint = printpoint + "8"
	except urllib2.URLError, e:
		extra = extra + newline + str(e.args) + space + str(e)
		printpoint = printpoint + "9"
	except Exception, TypeError:
		printpoint = printpoint + "9"
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		if 'The read operation timed out' in TypeError: returned = 'timeout'
		
	if not "7" in printpoint:
		if ping == True:
			if systemplatformwindows: output = terminal('ping '+url+' -n 1',"Connected2")
			else: output = terminal('ping -W 1 -w 1 -4 -q '+url+'',"Connected")
			if (not systemplatformwindows and ("1 packets received" in output or not "100% packet loss" in output)) or (systemplatformwindows and ("Received = 1" in output or not "100% loss" in output)): printpoint = printpoint + "7"
	
	if "UKY3scPIMd8" in url: printpoint = printpoint + "6"
	elif "7" in printpoint: returned = "ok"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin or addonID == 'script.htpt.install': print printfirst + name + "_LV" + printpoint + space + "url" + space2 + url + space + "ping" + space2 + str(ping) + space + extra
	'''---------------------------'''
	return returned
	
def YOUList2(name, url, iconimage, desc, num, viewtype):
	returned = ""
	#playlists=PlaylistsFromUser(url)
	
	
	#TVMode_check(admin, url, playlists)
	if General_TVModeDialog != "true" or returned != "ok":
		#url2='plugin://plugin.video.youtube/channel/'+url+'/'
		#link = OPEN_URL('http://youtube.com/channel/'+url+'')
		
		default = 'http://www.youtube.com/'
		url1 = 'channel/' + url + '/'
		url2 = 'user/' + url + '/'
		returned1 = urlcheck(default + url1)
		returned2 = urlcheck(default + url2)
		
		default2 = 'plugin://plugin.video.youtube/'
		
		#print "543-link1" + space2 + link
		#print "543-link2" + space2 + link2
		#update_view('plugin://plugin.video.youtube/channel/'+url+'/', viewtype)
		if returned1 == 'ok': update_view(default2 + url1, viewtype)
		elif returned2 == 'ok': update_view(default2 + url2, viewtype)
		#xbmc.executebuiltin('XBMC.Container.Update(%s)' % url2 )
		'''---------------------------'''
		
def YOUList(name, url, iconimage, desc, num):
	returned = ""
	printpoint = ""
	try:
		playlists = PlaylistsFromUser(url)
		returned = TVMode_check(admin, url, playlists)
	except: printpoint = printpoint + "8"
				
	if General_TVModeDialog != "true" or returned != "ok":
		if num == "" or num == None: num = '1'
		numN = int(num)
		num3N = 1
		'''---------------------------'''
		murl='http://gdata.youtube.com/feeds/api/users/'+url+'/uploads?&max-results=50&start-index='+num
		#murl='https://gdata.youtube.com/feeds/users/'+url+'/uploads?&max-results=50&start-index='+num
		print printfirst + "murl" + space2 + murl
		link=OPEN_URL(murl)
		#print link
		if addonID == 'plugin.video.htpt.gopro' or addonID == 'plugin.video.htpt.music': addDir('[COLOR=Yellow]' + str79525.encode('utf-8') + '[/COLOR]',url,15,"special://skin/media/DefaultRecentlyAddedEpisodes.png",str79524.encode('utf-8'),'1',"") #TV Mode
		else: addDir('[COLOR=Yellow]' + str79520.encode('utf-8') + '[/COLOR]',murl,11,"special://skin/media/DefaultPlaylist.png",str79526.encode('utf-8'),'1',"") #Quick-Play
		
		match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
		
		if not "8" in printpoint:
			for playlistid,title,thumb, in playlists:
				'''PlayList'''
				if num == '1':
					num3N += 1
					numN += 1
					#num = str(numN)
					addDir('[COLOR=Yellow2]' + title + '[/COLOR]',playlistid,12,thumb,str79527.encode('utf-8'),num,"")
					#addDir(title + '[COLOR=Yellow]' + addonString(7).encode('utf-8') + space2 + '[/COLOR]',playlistid,12,thumb,'',num,"")
					#print "123 " + playlistid
		
		if 1 + 1 == 3:
			for nurl,desc,thumb,rname in match:
				'''Media'''
				if (num == '1' and num3N < 8) or (num != '1' and num3N < 40):
					rname=rname.replace('<','')
					num3N += 1
					numN += 1
					#num = str(numN)
					#YOULink(rname, nurl, thumb, desc)
					#addLink(rname, nurl, thumb, desc,"")
		
		'''Show More Results'''
		if (num == '1' and num3N <= 8): num2N = int(num) + num3N
		else: num2N = int(num) + 40
		num2 = str(num2N)
		num3 = str(num3N)

		if admin or num == '1' or num3N == 40:
			'''TEMP SOLUTION'''
			#addDir('[COLOR=Yellow]' + str79521.encode('utf-8') + '[/COLOR]',url,9,"special://skin/media/icons/se.png",str79528.encode('utf-8'),num2,"")
			if addonID == 'plugin.video.htpt.music': addDir('[COLOR=Yellow]' + str79521.encode('utf-8') + '[/COLOR]','plugin://plugin.video.youtube/user/'+url+'/',8,"special://skin/media/DefaultPlaylist.png",str79528.encode('utf-8'),num2,"") #More Results
			else: addDir('[COLOR=Yellow]' + str79521.encode('utf-8') + '[/COLOR]','plugin://plugin.video.youtube/channel/'+url+'/',8,"special://skin/media/DefaultPlaylist.png",str79528.encode('utf-8'),num2,"") #More Results
			#addDir(name,'plugin://plugin.video.youtube/channel/'+url+'/',8,"","","","")
			#addDir(name,'plugin://plugin.video.youtube/video_id/'+nurl+'/',8,"","","","")
		
		
		if admin: print printfirst + "YOUList_LV" + printpoint + " " + "num/2/3" + space2 + num + " / " + num2 + " / " + num3 + space + "returned" + space2 + returned + space + "name" + space2 + str(name) + space + "url" + space2 + url
		if admin: print printfirst + "YOUList" + space + "link" + space2 + str(link)
		if admin: print printfirst + "YOUList" + space + "match" + space2 + str(match)
		#if admin: print printfirst + "YOUList" + space + "nurl" + space2 + str(nurl) + space + "desc" + space2 + str(desc) + space + "thumb" + space2 + str(thumb) + space + "rname" + space2 + str(rname)

def setaddonFanart(fanart, Fanart_Enable, Fanart_EnableCustom):
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	#admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	returned = "" ; printpoint = "" ; TypeError = "" ; extra = ""
	try:
		Fanart_Enable = getsetting('Fanart_Enable')
		Fanart_EnableCustom = getsetting('Fanart_EnableCustom')
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if Fanart_Enable == "true" and extra == "":
		printpoint = printpoint + "1"
		if Fanart_EnableCustom != "true":
			returned = addonFanart
			printpoint = printpoint + "3"
		elif fanart != "":
			try:
				if os.path.exists(fanart):
					printpoint = printpoint + "4"
					returned = fanart
				elif "http://" in fanart or "www." in fanart:
					printpoint = printpoint + "5"
					returned = fanart
				else: pass
			except Exception, TypeError: pass
			
			printpoint = printpoint + "2"
			
		else: printpoint = printpoint + "8"
	else: printpoint = printpoint + "9"
	
	if admin and not admin2 and admin3:
		print printfirst + "setaddonFanart_LV" + printpoint + space + "Fanart_Enable" + space2 + str(Fanart_Enable) + space + "Fanart_EnableCustom" + space2 + str(Fanart_EnableCustom) + newline + \
		"fanart" + space2 + str(fanart) + extra
	return returned

def getAddonFanart(category):
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	#admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	returned = "" ; category_path = "" ; printpoint = "" ; extra = ""
	if category == 100: category_path = Fanart_Custom100
	elif category == 101: category_path = Fanart_Custom101
	elif category == 102: category_path = Fanart_Custom102
	elif category == 103: category_path = Fanart_Custom103
	elif category == 104: category_path = Fanart_Custom104
	elif category == 105: category_path = Fanart_Custom105
	elif category == 106: category_path = Fanart_Custom106
	elif category == 107: category_path = Fanart_Custom107
	elif category == 108: category_path = Fanart_Custom108
	elif category == 109: category_path = Fanart_Custom109
	elif category == 110: category_path = Fanart_Custom110
	elif category == 111: category_path = Fanart_Custom111
	elif category == 112: category_path = Fanart_Custom112
	elif category == 113: category_path = Fanart_Custom113
	elif category == 114: category_path = Fanart_Custom114
	elif category == 115: category_path = Fanart_Custom115
	elif category == 116: category_path = Fanart_Custom116
	elif category == 117: category_path = Fanart_Custom117
	elif category == 118: category_path = Fanart_Custom118
	elif category == 119: category_path = Fanart_Custom119
	elif category == 120: category_path = Fanart_Custom120
	elif category == 121: category_path = Fanart_Custom121
	elif category == 122: category_path = Fanart_Custom122
	elif category == 123: category_path = Fanart_Custom123
	elif category == 124: category_path = Fanart_Custom124
	elif category == 125: category_path = Fanart_Custom125
	elif category == 126: category_path = Fanart_Custom126
	elif category == 127: category_path = Fanart_Custom127
	elif category == 128: category_path = Fanart_Custom128
	elif category == 129: category_path = Fanart_Custom129
	elif category == 130: category_path = Fanart_Custom130
	
	else:
		try:
			if "Custom_Playlist" in category:
				if category == "Custom_Playlist1": category_path = Custom_Playlist1_Fanart
				elif category == "Custom_Playlist2": category_path = Custom_Playlist2_Fanart
				elif category == "Custom_Playlist3": category_path = Custom_Playlist3_Fanart
				elif category == "Custom_Playlist4": category_path = Custom_Playlist4_Fanart
				elif category == "Custom_Playlist5": category_path = Custom_Playlist5_Fanart
				elif category == "Custom_Playlist6": category_path = Custom_Playlist6_Fanart
				elif category == "Custom_Playlist7": category_path = Custom_Playlist7_Fanart
				elif category == "Custom_Playlist8": category_path = Custom_Playlist8_Fanart
				elif category == "Custom_Playlist9": category_path = Custom_Playlist9_Fanart
				elif category == "Custom_Playlist10": category_path = Custom_Playlist10_Fanart
				else: printpoint = printpoint + "8"
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			printpoint = printpoint + "8"
	
	
	if category_path != "":
		if "http://" in category_path or "www." in category_path:
			printpoint = printpoint + "5"
			returned = category_path
			#valid = urlcheck(value, ping=False)
		elif os.path.exists(category_path):
			printpoint = printpoint + "7"
			category_path = os.path.join(xbmc.translatePath(category_path).decode("utf-8"))
			try: category_path.encode('utf-8')
			except: pass
			returned = category_path
		else:
			printpoint = printpoint + "9"
	else:
		printpoint = printpoint + "9"
			
	if "9" in printpoint or "8" in printpoint:
		try:
			if os.path.exists(addonFanart2): returned = addonFanart2
			elif os.path.exists(addonFanart): returned = addonFanart
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			returned = ""
	
	if admin and not admin2 and admin3:
		print printfirst + "getAddonFanart_LV" + printpoint + space + "category" + space2 + str(category) + space + "returned" + space2 + str(returned) + newline + \
		"category_path" + space2 + str(category_path) + extra
	return returned	
	
def pluginend(admin):
	try: from modules import *
	except: pass
	try: from modulesp import *
	except: pass
	printpoint = "" ; TypeError = "" ; extra = ""
	
	'''------------------------------
	---params------------------------
	------------------------------'''
	params=get_params()
	url=None
	name=None
	mode=None
	iconimage=None
	desc=None
	num=None
	viewtype=None
	fanart=None
	#value=None
	'''---------------------------'''
	try: url=urllib.unquote_plus(params["url"])
	except: pass
	try: name=urllib.unquote_plus(params["name"])
	except: pass
	try: iconimage=urllib.unquote_plus(params["iconimage"])
	except: pass
	try: mode=int(params["mode"])
	except: pass
	try: desc=urllib.unquote_plus(params["desc"])
	except: pass
	
	try: num=urllib.unquote_plus(params["num"])
	except: pass
	try: viewtype=int(params["viewtype"])
	except: pass
	try: fanart=urllib.unquote_plus(params["fanart"])
	except: pass
	#try: value=urllib.unquote_plus(params["value"])
	#except: pass
	'''---------------------------'''

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	try: IconImageS = str(IconImage)
	except: IconImageS = "None"
	'''---------------------------'''
	if admin: print printfirst + "pluginend" + space + "mode" + space2 + str(mode) + newline + \
	"url" + space2 + str(url) + newline + \
	"name" + space2 + str(name) + space + "IconImage" + space2 + IconImageS + space + "desc" + space2 + str(desc) + newline + \
	"viewtype" + space2 + str(viewtype) + space + "fanart" + space2 + str(fanart) + newline + \
	"params" + space2 + str(params)
	'''---------------------------'''

	'''------------------------------
	---MODES-LIST--------------------
	------------------------------'''
	if mode == None or ((url == None or len(url)<1) and mode < 100): 
		CATEGORIES()
	
		try:
			getsetting('Addon_Update')
			getsetting('Addon_Version')
			getsetting('Addon_UpdateDate')
			getsetting('Addon_UpdateLog')
			getsetting('Addon_ShowLog')
			getsetting('Addon_ShowLog2')
			
			checkAddon_Update(admin, Addon_Update, Addon_Version, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2)
			if Addon_UpdateLog == "true":
				if addonID == 'plugin.video.htpt.kids':
					if systemlanguage != "Hebrew": notification("This addon does not support Engish yet","...","",2000)
					installaddon2(admin, 'repository.xbmc-israel', version="", update=True, silent=False)
					'''---------------------------'''
				elif addonID == 'plugin.video.htpt.music':
					if systemlanguage != "Hebrew": notification("This addon does not support Engish yet","...","",2000)
					
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			printpoint = printpoint + "2"
			'''---------------------------'''
	
	#1-99 = COMMANDS
	elif mode == 1:
		pass
	elif mode == 2:
		pass
	elif mode == 3:
		YoutubeSearch(name, url, desc, viewtype)
	elif mode == 4:
		#play_video(url) #API V3 issues
		play_video2(url)
	elif mode == 5:
		MultiVideos(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 6:
		MultiVideos(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 7:
		ListLive(url)
	elif mode == 8:
		update_view(url, viewtype)
	elif mode == 9:
		#YOUList(name, url, iconimage, desc, num)
		YOUList2(name, url, iconimage, desc, num, viewtype)
	elif mode == 10:
		pass #YOUsubs(url)
	elif mode == 11:
		pass #YOULinkAll(url)
	elif mode == 12:
		#PlayPlayList(url)
		PlayPlayList2(url)
	elif mode == 13:
		#ListPlaylist(url, num)
		ListPlaylist2(url, num, viewtype)
	elif mode == 14:       
		pass #SeasonsFromShow(url)
	elif mode == 15:
		TvMode(url)
	elif mode == 16:       
		ShowFromUser(url)
	elif mode == 17:
		mode = TvMode2(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 18:
		'''Custom Playlist'''
		mode = TvMode2(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 20:
		AddCustom(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 21:
		ManageCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 22:
		AdvancedCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 23:
		MoveCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 100:
		CATEGORIES100(admin)
	elif mode == 101:
		CATEGORIES101(admin)
	elif mode == 102: 
		CATEGORIES102(admin)
	elif mode == 103:       
		CATEGORIES103(admin)
	elif mode == 104:       
		CATEGORIES104(admin)
	elif mode == 105:    
		CATEGORIES105(admin)
	elif mode == 106:       
		CATEGORIES106(admin)
	elif mode == 107:       
		CATEGORIES107(admin)
	elif mode == 108:       
		CATEGORIES108(admin)
	elif mode == 109:       
		CATEGORIES109(admin)
	
	elif mode == 111:
		CATEGORIES111(admin)
	elif mode == 112: 
		CATEGORIES112(admin)
	elif mode == 113:       
		CATEGORIES113(admin)
	elif mode == 114:       
		CATEGORIES114(admin)
	elif mode == 115:    
		CATEGORIES115(admin)
	elif mode == 116:       
		CATEGORIES116(admin)
	elif mode == 117:       
		CATEGORIES117(admin)
	elif mode == 118:       
		CATEGORIES118(admin)
	elif mode == 119:       
		CATEGORIES119(admin)
		
	elif mode == 121:
		CATEGORIES121(admin)
	elif mode == 122: 
		CATEGORIES122(admin)
	elif mode == 123:       
		CATEGORIES123(admin)
	elif mode == 124:       
		CATEGORIES124(admin)
	elif mode == 125:    
		CATEGORIES125(admin)
	elif mode == 126:       
		CATEGORIES126(admin)
	elif mode == 127:       
		CATEGORIES127(admin)
	elif mode == 128:       
		CATEGORIES128(admin)
	elif mode == 129:       
		CATEGORIES129(admin)
	
	elif mode == 131:
		CATEGORIES131(admin)
	elif mode == 132: 
		CATEGORIES132(admin)
	elif mode == 133:       
		CATEGORIES133(admin)
	elif mode == 134:       
		CATEGORIES134(admin)
	elif mode == 135:    
		CATEGORIES135(admin)
	elif mode == 136:       
		CATEGORIES136(admin)
	elif mode == 137:       
		CATEGORIES137(admin)
	elif mode == 138:       
		CATEGORIES138(admin)
	elif mode == 139:       
		CATEGORIES139(admin)
	
	#10101+ = SUB-CATEGORIES2
	elif mode == 10101:
		CATEGORIES10101(name, iconimage, desc)
	elif mode == 10102:
		CATEGORIES10102(name, iconimage, desc)
	elif mode == 10103:
		CATEGORIES10103(name, iconimage, desc)
	elif mode == 10104:
		CATEGORIES10104(name, iconimage, desc)
	elif mode == 10105:
		CATEGORIES10105(name, iconimage, desc)
	elif mode == 10106:
		CATEGORIES10106(name, iconimage, desc)
	elif mode == 10107:
		CATEGORIES10107(name, iconimage, desc)
	elif mode == 10108:
		CATEGORIES10108(name, iconimage, desc)
	elif mode == 10109:
		CATEGORIES10109(name, iconimage, desc)
		
	elif mode == 10201:
		CATEGORIES10201(name, iconimage, desc)
	elif mode == 10202:
		CATEGORIES10202(name, iconimage, desc)
	elif mode == 10203:
		CATEGORIES10203(name, iconimage, desc)
	elif mode == 10204:
		CATEGORIES10204(name, iconimage, desc)
	elif mode == 10205:
		CATEGORIES10205(name, iconimage, desc)
	elif mode == 10206:
		CATEGORIES10206(name, iconimage, desc)
	elif mode == 10207:
		CATEGORIES10207(name, iconimage, desc)
	elif mode == 10208:
		CATEGORIES10208(name, iconimage, desc)
	elif mode == 10209:
		CATEGORIES10209(name, iconimage, desc)
	
	elif mode == 10401:
		CATEGORIES10401(name, iconimage, desc)
	elif mode == 10402:
		CATEGORIES10402(name, iconimage, desc)
	elif mode == 10403:
		CATEGORIES10403(name, iconimage, desc)
	elif mode == 10404:
		CATEGORIES10405(name, iconimage, desc)
	elif mode == 10406:
		CATEGORIES10406(name, iconimage, desc)
	elif mode == 10407:
		CATEGORIES10407(name, iconimage, desc)
	elif mode == 10408:
		CATEGORIES10408(name, iconimage, desc)
	elif mode == 10409:
		CATEGORIES10409(name, iconimage, desc)
	elif mode == 10410:
		CATEGORIES10410(name, iconimage, desc)
	elif mode == 10411:
		CATEGORIES10411(name, iconimage, desc)
	elif mode == 10412:
		CATEGORIES10412(name, iconimage, desc)
	elif mode == 10413:
		CATEGORIES10413(name, iconimage, desc)
	elif mode == 10414:
		CATEGORIES10414(name, iconimage, desc)
	elif mode == 10415:
		CATEGORIES10415(name, iconimage, desc)
	elif mode == 10416:
		CATEGORIES10416(name, iconimage, desc)
	elif mode == 10417:
		CATEGORIES10417(name, iconimage, desc)
	elif mode == 10418:
		CATEGORIES10418(name, iconimage, desc)
	elif mode == 10419:
		CATEGORIES10419(name, iconimage, desc)
	elif mode == 10420:
		CATEGORIES10420(name, iconimage, desc)
	elif mode == 10421:
		CATEGORIES10421(name, iconimage, desc)
	elif mode == 10422:
		CATEGORIES10422(name, iconimage, desc)
	elif mode == 10423:
		CATEGORIES10423(name, iconimage, desc)
	elif mode == 10424:
		CATEGORIES10424(name, iconimage, desc)
	elif mode == 10425:
		CATEGORIES10425(name, iconimage, desc)
	elif mode == 10426:
		CATEGORIES10426(name, iconimage, desc)
	elif mode == 10427:
		CATEGORIES10427(name, iconimage, desc)
	elif mode == 10428:
		CATEGORIES10428(name, iconimage, desc)
	elif mode == 10429:
		CATEGORIES10429(name, iconimage, desc)
	elif mode == 10430:
		CATEGORIES10430(name, iconimage, desc)
		
	else: notification("?","","",1000)
	
	if mode != 17 and mode != 5 and mode != 21: # and mode != 20
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
		printpoint = printpoint + "7"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "pluginend_LV" + printpoint + extra
	'''---------------------------'''
	return url, name, mode, iconimage, desc, num, viewtype, fanart
	
	
def pluginend2(admin, url, containerfolderpath, viewtype):
	printpoint = "" ; count = 0 ; countmax = 10 ; url = str(url) ; containerfolderpath2 = ""
	returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
	
	#xbmc.sleep(1000) #TIME FOR DIALOGBUSY
	'''------------------------------
	---countmax-ADJUST---------------
	------------------------------'''
	if "plugin.video.10qtv" in url: countmax = 40
	'''---------------------------'''
	
	while (count < countmax and (returned_Dialog == "dialogbusyW" or returned_Dialog == "dialogprogressW")) or (count < 2 and returned_Dialog == "") and not xbmc.abortRequested:
		count += 1
		if count == 1: printpoint = printpoint + "1"
		xbmc.sleep(500)
		returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
		'''---------------------------'''
		
	if count < countmax:
		printpoint = printpoint + "2"
		if count == 0: xbmc.sleep(1000)
		else: xbmc.sleep(500)
		containerfolderpath2 = xbmc.getInfoLabel('Container.FolderPath')
		if viewtype == None:
			'''------------------------------
			---viewtype-ADJUST---------------
			------------------------------'''
			printpoint = printpoint + "3"
			if containerfolderpath2 == 'plugin://'+addonID+'/?&': printpoint = printpoint + "4" ; viewtype = 50
			elif "http://nickjr.walla.co.il/" in url: viewtype = 50
			elif ("plugin.video.gozlan.me" in url or "plugin.video.seretil" in url or "plugin.video.supercartoons" in url or "plugin.video.sdarot.tv" in url or "seretil.me" in url): viewtype = 58
			'''---------------------------'''
		if containerfolderpath != containerfolderpath2 or "4" in printpoint: #GAL CHECK THIS! #containerfolderpath2 == "plugin://"+addonID+"/"
			printpoint = printpoint + "5"
			setView('', viewtype, containerfolderpath2)
			'''---------------------------'''
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin and not admin2 and admin3:
		print printfirst + "pluginend2_LV" + printpoint + space + "count" + space2 + str(count) + space + "returned_Dialog" + space2 + returned_Dialog + space + "containerfolderpath/2" + newline + \
		str(containerfolderpath) + newline + \
		str(containerfolderpath2) + newline + \
		"url" + space2 + str(url)
		'''---------------------------'''