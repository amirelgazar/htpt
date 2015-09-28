import xbmc, xbmcgui, xbmcaddon
import xbmcplugin
import os, subprocess, sys
from variables import *
#from shared_variables import *
#from shared_modules import *
'''unused'''

#https://gdata.youtube.com/feeds/api/videos/dzbN8WG33Sg/related?v=2

def getsetting_custom1(addon,set1):
	'''------------------------------
	---GET-ADDON-SETTING-1-----------
	------------------------------'''
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	'''---------------------------'''
	returned = getsetting_custom(set1,set1v)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "getsetting_custom1" + space2 + addon + space + set1
	'''---------------------------'''
	return returned
	'''---------------------------'''

def checkID(admin, idstr, value):
	name = 'checkID' ; returned1 = "" ; returned2 = ""
	find = "<skin.htpt."+value+">"
	file1 = skin_userdata_path + "guisettings.xml"
	file2 = skin_userdata_path + "guisettings2.xml"
	if os.path.exists(file2):
		if not systemplatformwindows: returned2 = terminal('cat '+file2+' | grep -e '+find+' | grep -o ">[^ ]*<" | sed "s/[<>]//g"',"file2")
		else:
			returned2 = terminal('find """skin.htpt.ID""" "'+file2+'"',"file2")
			find_string(returned2, find, "</") #GAL THIS THIS!
			'''---------------------------'''
	if os.path.exists(file1):
		if not systemplatformwindows: returned1 = terminal('cat '+file1+' | grep -e '+find+' | grep -o ">[^ ]*<" | sed "s/[<>]//g"',"file1")
		else:
			returned1 = terminal('find """skin.htpt.ID""" '+file1+'',"file1")
			find_string(returned1, find, "</") #GAL THIS THIS!
			'''---------------------------'''
	print printfirst + name + space + "file1" + space2 + str(file1) + space + "file2" + space2 + str(file2) + newline + "find" + space2 + str(find) + space + "returned1" + space2 + str(returned1) + space + "returned2" + space2 + str(returned2)
	'''---------------------------'''
	if returned2 != "": return returned2
	else: return returned1
	'''---------------------------'''
	
def dialogprogress(id, progress, heading, line1, line2, line3): 
	'''------------------------------
	---DIALOG-OK-***BROKEN***--------
	------------------------------'''
	#try: progressN = int(progress)
	#except Exception, TypeError: progressN = 0
	'''---------------------------'''
	if '$LOCALIZE' in heading or '$ADDON' in heading: heading = xbmc.getInfoLabel(heading)
	if '$LOCALIZE' in line1 or '$ADDON' in line1: line1 = xbmc.getInfoLabel(line1)
	if '$LOCALIZE' in line2 or '$ADDON' in line2: line2 = xbmc.getInfoLabel(line2)
	if '$LOCALIZE' in line3 or '$ADDON' in line3: line3 = xbmc.getInfoLabel(line3)
	heading = str(heading.encode('utf-8'))
	line1 = str(line1.encode('utf-8'))
	line2 = str(line2.encode('utf-8'))
	line3 = str(line3.encode('utf-8'))
	
	#notification(str(progress),"","",2000)
	dp = xbmcgui.DialogProgress()
					
	if progress == 0:
		#pDialog.close
		dp.create(heading,line1,line2,line3)
	elif progress == 10: dp.close
	elif progress > 0: dp.update(progressN,line1,line2,line3)
	
	#pDialog = xbmcgui.DialogProgressBG()
	#pDialog.create(heading, line1)
	
	#def dialogprogress(admin, id, action, name, header, line1, line2):
	#id = xbmcgui.DialogProgress( )
	#if action == 0: returned = id.create(name, header, line1, line2)
	#else: returned = ""
	#return returned
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin:
		print printfirst + "dialogprogress" + space2 + heading + space2 + line1 + space2 + line2 + space2 + line3
		try:
			print printfirst + "TypeError" + space2 + str(TypeError)
			'''---------------------------'''
		except:
			pass
			'''---------------------------'''
	return dp
	
def UserBlock(custom):
	
	if custom == "ON": terminal('pgrep kodi.bin | xargs kill -SIGSTOP',"UserBlock-ON")
	else: terminal('pgrep kodi.bin | xargs kill -SIGCONT',"UserBlock-OFF")
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if custom != "ON": custom = "OFF"
	print printfirst + space + "UserBlock=" + custom
	'''---------------------------'''
	
def copy_rename(old_file_name, new_file_name):
	import shutil
	src_dir= os.curdir
	dst_dir= os.path.join(os.curdir , "/storage/")
	src_file = os.path.join(src_dir, old_file_name)
	shutil.copy(src_file,dst_dir)
	
	dst_file = os.path.join(dst_dir, old_file_name)
	new_dst_file_name = os.path.join(dst_dir, new_file_name)
	os.rename(dst_file, new_dst_file_name)
	
def stringtotime(dt_str, dt_func):
	from datetime import datetime
	import time
	#dt_str = '9/24/2010 5:03:29 PM'
	#dt_func = '%m/%d/%Y %I:%M:%S %p'
	#try:
	dt_obj = datetime.strptime(dt_str, dt_func)
	dt_objS = str(dt_obj)
	if dt_func == '%H':
		#time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=20, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
		find = dt_str
		found = find_string(dt_objS, find, "")
		'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin: print printfirst + "stringtotime" + space + "dt_objS" + space2 + dt_objS + space + "timenow3S" + space2 + timenow3S
	'''---------------------------'''
	
	return dt_obj
	
def General_CleanCache():
    dir=xbmc.translatePath('special://temp/')
    file=os.path.join(dir, 'commoncache.db')
    f = open(file, 'w')
    f.write('')
    f.close
    dialogok('[COLOR=Yellow]' + addonString(307).encode('utf-8') + addonString(308).encode('utf-8') + '[/COLOR]',"","","")
    '''---------------------------'''
	
def mes():

        
	try:
		link=OPEN_URL('http://goo.gl/r6eog7')
		r = re.findall(r'ANNOUNCEMENTWINDOW ="ON"',link)
		if not r:
			return
			
		match=re.compile('<new>(.*?)\\n</new>',re.I+re.M+re.U+re.S).findall(link)
		if not match[0]:
			return
			
		dire=os.path.join(xbmc.translatePath( "special://userdata/addon_data" ).decode("utf-8"), addonID)
		if not os.path.exists(dire):
			'''------------------------------
			---CREATE-USERDATA-DIRECTORY-----
			------------------------------'''
			os.makedirs(dire)
			'''---------------------------'''
		aSeenFile = os.path.join(dire, 'announcementSeen.txt')
		if (os.path.isfile(aSeenFile)): 
			f = open(aSeenFile, 'r') 
			content = f.read() 
			f.close() 
			if content == match[0] :
				return

		f = open(aSeenFile, 'w') 
		f.write(match[0]) 
		f.close() 

		dp = xbmcgui . Dialog ( )
		dp.ok("UPDATES", match[0])
	except:
		pass


def _____NONE(admin):
	'''------------------------------
	---MAC1/2------------------------
	------------------------------'''
	MAC1 = terminal("ifconfig -a | grep -e 'eth' | awk {'print $1,$5'}","LAN MAC")
	MAC2 = terminal("ifconfig -a | grep -e 'wlan' | awk {'print $1,$5'}","WLAN MAC")
	terminal('ifconfig eth0 up',"eth0 up")

def addonsettings(name, addon,skinsettingS, skinsetting2S, usernameS, passwordS, set3,opt1,opt2,opt3):
	'''------------------------------
	---SET-USERNAME-AND-PASSWORD-----
	------------------------------'''
	getsetting_custom          = xbmcaddon.Addon(addon).getSetting
	setsetting_custom          = xbmcaddon.Addon(addon).setSetting
	
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	skinsetting = xbmc.getInfoLabel('Skin.HasSetting('+ skinsettingS +')')
	skinsetting2 = xbmc.getInfoLabel('Skin.String('+ skinsetting2S +')')
	#if setting_custom == localize(20122): setting_custom = "true"
	#else: setting_custom = "false"
	try: skinsetting2N = int(skinsetting2)
	except: skinsetting2N = 0
	username = getsetting_custom(usernameS)
	password = getsetting_custom(passwordS)
	setting3 = getsetting_custom(set3)
	printpoint = ""
	'''---------------------------'''
	if not id40str:
		if (skinsetting or id9str == 'Trial' or id2str == datenowS) and usernameS != "" and passwordS != "":
			if admin: notification("test0","","",1000)
			if ('htpt' in username and not "finalmakerr" in scripthtptinstall_User_ID) and scripthtptinstall_User_ID != username and id9str != 'Trial' and id2str != datenowS:
				'''------------------------------
				---SET-DEFAULT-------------------
				------------------------------'''
				setsetting_custom(usernameS,scripthtptinstall_User_ID)
				setsetting_custom(passwordS,idpstr)
				printpoint = printpoint + "1"
				if admin: notification("test1","","",1000)
				'''---------------------------'''
			elif id9str == 'Trial' or id2str == datenowS:
				'''------------------------------
				---SET-TRIAL---------------------
				------------------------------'''
				setsetting_custom(usernameS,idtrial)
				setsetting_custom(passwordS,idp2str)
				printpoint = printpoint + "2"
				if admin: notification("test2","","",1000)
				'''---------------------------'''
			elif skinsetting and ((username == "" or password == "") or skinsetting2 == "0"):
				'''------------------------------
				---SET-NONE----------------------
				------------------------------'''
				setsetting_custom(usernameS,"")
				setsetting_custom(passwordS,"")
				printpoint = printpoint + "5"
				if admin: notification("test1.2","","",1000)
				'''---------------------------'''
			elif skinsetting:
				'''------------------------------
				---NO-CHANGES--------------------
				------------------------------'''
				printpoint = printpoint + "6"
				if admin: notification("test1.3","","",1000)
				'''---------------------------'''
		else:
			'''------------------------------
			---NO-ACCOUNT-OR-TRIAL-----------
			------------------------------'''
			daynowS = get_daynow(1)
			timezone = get_timenow(1)
			General_TimeZone = getsetting('General_TimeZone')
			if name == 'REALDEBRID' and (daynowS == opt1 or General_TimeZone != opt2):
				'''------------------------------
				---SET-NONE----------------------
				------------------------------'''
				setsetting_custom(usernameS,"")
				setsetting_custom(passwordS,"")
				printpoint = printpoint + "3"
				'''---------------------------'''
			else:
				'''------------------------------
				---SET-DEFAULT-------------------
				------------------------------'''
				setsetting_custom(usernameS,scripthtptinstall_User_ID)
				setsetting_custom(passwordS,idpstr)
				printpoint = printpoint + "4"
				'''---------------------------'''
				
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if printpoint == "0": print printfirst + "addonsettings LV_0" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "?"
	if printpoint == "1": print printfirst + "addonsettings LV_1" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "RESET"
	elif printpoint == "2": print printfirst + "addonsettings LV_2" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "Trial / DATENOW"
	elif printpoint == "3": print printfirst + "addonsettings LV_3" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "NONE" + space + "ID: " + scripthtptinstall_User_ID + space + "daynowS" + space2 + daynowS + space + "timenow3S" + space2 + timenow3S + space + "datenowS" + space2 + datenowS + space + "timezone" + space2 + timezone
	elif printpoint == "4": print printfirst + "addonsettings LV_4" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "DEFAULT" + space + "ID: " + scripthtptinstall_User_ID + space + "timezone" + space2 + timezone
	elif printpoint == "5": print printfirst + "addonsettings LV_5" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "skinsetting2" + space2 + skinsetting2 + "UNREGISTER"
	elif printpoint == "6": print printfirst + "addonsettings LV_6" + space2 + addon + space + skinsettingS + space2 + skinsetting + space + "REGISTERED"
	elif printpoint == "": print printfirst + "addonsettings LV_0-Error?"
	'''---------------------------'''
	
def YOULinkAll(url):
	dp = xbmcgui.DialogProgress()
	dp.create(addonName ,addonString(4).encode('utf-8')) #GAL CHECK THIS!
	dp.update(0)
	dp.update(0, "", str79520.encode('utf-8'))
	pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	pl.clear()
	link = OPEN_URL(url)
	match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
	playlist = []
	nItem = len(match)

	for nurl,desc,thumb,rname in match:
		rname=rname.replace('<','')
		#finalurl= "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+nurl+"&hd=1"
		finalurl= "plugin://plugin.video.youtube/play/?video_id="+nurl+"&hd=1"
		liz = xbmcgui.ListItem(rname, iconImage="DefaultVideo.png", thumbnailImage=thumb)
		liz.setInfo( type="Video", infoLabels={ "Title": rname, "Plot": desc}) #NEW UNTESTED!!! (PLOT...)
		liz.setProperty("IsPlayable","true")
		playlist.append((finalurl ,liz))
		progress = len(playlist) / float(nItem) * 100  
		dp.update(int(progress), str79520.encode('utf-8'),rname)
		#dp.update(i*5, str79529.encode('utf-8'), "")
		if dp.iscanceled():
			return

	
	for blob ,liz in playlist:
		try:
			if blob:
				if not 'UKY3scPIMd8' in blob:
					pl.add(blob,liz)
		except:
			pass
	dp.close()
	xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)

def SeasonsFromShow(showApiUrl):
	#print showApiUrl
	resultJSON = json.loads(OPEN_URL(showApiUrl))
	seasons=resultJSON['feed']['entry']
	for i in range (0, len(seasons)) :
		#print seasons[i].keys()
		#print seasons[i]['title']['$t']
		for index,item in  enumerate(seasons[i]['gd$feedLink']) :
			if item['countHint'] !=0:
				resultJSON = json.loads(OPEN_URL( seasons[i]['gd$feedLink'][index]['href']+'&alt=json'))
				for  j in range (0, len(resultJSON['feed']['entry'])) :
					title= str(resultJSON['feed'][u'entry'][j][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
					thumb =str(resultJSON['feed'][u'entry'][j][ u'media$group'][u'media$thumbnail'][-1][u'url'])
					episode_num=resultJSON['feed']['entry'][j]['yt$episode']['number']
					url= resultJSON['feed']['entry'][j]['link'][0]['href']
					match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').findall(url)
					#finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
					finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1"
					addLink(title+' '+episode_num ,finalurl,thumb,'',"")

def YOUsubs(user):
	murl='http://gdata.youtube.com/feeds/api/users/'+user+'/subscriptions?alt=json&start-index=1&max-results=50'
	resultJSON = json.loads(OPEN_URL(murl))
	feed=resultJSON['feed']['entry']
	for i in range (0, len(feed)) :
		image=str(feed[i]['media$thumbnail']['url'])
		name = feed[i]['title']['$t'].replace('Activity of:','').encode('utf-8')
		url=feed[i]['yt$channelId']['$t'].encode('utf-8')
		addDir(name,url,9,image,'1','1',"")

	

		
def ListPlaylist(playlistid, page):
	printpoint = "" ; TypeError = "" ; extra = "" ; playlist = []
	try:
		pageN = int(page)
		if pageN < 1: pageN = 1
		'''---------------------------'''
	except:
		pageN = 1
		'''---------------------------'''
	pageS = str(page)
	'''---------------------------'''
	pagesizeN = 40
	pagesizeS = str(pagesizeN)
	'''---------------------------'''
	if pageN <= 1: indexN = 1
	else: indexN = pageN * pagesizeN - pagesizeN
	indexS = str(indexN)
	'''---------------------------'''
	url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+playlistid+'&key=AIzaSyASEuRNOghvziOY_8fWSbKGKTautNkAYz4&part=snippet&maxResults=40&pageToken=' #?
	link = OPEN_URL(url)
	prms=json.loads(link)
	if admin:
		print "url" + space2 + str(url) + newline + \
		"link" + space2 + str(link) + newline + \
		"prms" + space2 + str(prms) + newline #+ \ + "totalResults" + space2 + str(totalResults)
		'''---------------------------'''
		
	addDir('[COLOR=Yellow]' + str79520.encode('utf-8') + '[/COLOR]',url,11,"special://skin/media/DefaultPlaylist.png",str79526.encode('utf-8'),'1',"") #Quick-Play
	'''---------------------------'''
	validS = "" #URLS
	duplicatesN = 0 #DUPLICATES
	invalidN = 0
	invalidS = "" #DELETES/PRIVATE
	'''---------------------------'''
	exceptN = 0
	totalResults=int(prms['pageInfo'][u'totalResults']) #if bigger than pagesize needs to add more result
	totalpagesN = (totalResults / pagesizeN) + 1
	'''---------------------------'''

	i = 0
	while i < pagesizeN and not "8" in printpoint and not xbmc.abortRequested: #h<totalResults
		try:
			print "i" + space2 + str(i) + space + "duplicatesN" + space2 + str(duplicatesN)
			#urlPlaylist= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$player'][0][u'url'])
			
			#https://www.youtube.com/watch?v=rjLmzRcmnSs&list=PLPWc8VdaIIsAHPacvuyNfA-y8VSxoh4or
			#match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').findall(id)
			#finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1"
			#finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
			#finalurl="https://www.youtube.com/watch?v="+id+"&list="+playlistid
			#finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
			#finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
			#title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
			#thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
			
			id=str(prms['items'][i][u'snippet'][u'resourceId'][u'videoId']) #Video ID
			finalurl="plugin://plugin.video.youtube/play/?video_id="+id
			title=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
			thumb=str(prms['items'][i][u'snippet'][u'thumbnails'][u'default'][u'url'])
			desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
			#id = "" ; finalurl = "" ; title = "" ; thumb = "" ; desc = ""
			
			if not finalurl in validS and not "Deleted video" in title and not "Private video" in title and finalurl != "":
				ok, liz = addLink(title,finalurl, thumb, desc)
				#name, url, mode, iconimage='DefaultFolder.png', desc="", num="", viewtype=""
				validS = validS + space + finalurl
				playlist.append((finalurl ,liz))
				'''---------------------------'''
			else:
				if "Deleted video" in title or "Private video" in title:
					invalidN = invalidN + 1
					invalidS = PlayListGain3 + space + finalurl
				elif finalurl in validS:
					duplicatesN = duplicatesN + 1
					#if admin: print "finalurl_Duplicate" + space2 + finalurl
					'''---------------------------'''
		except Exception, TypeError:
			exceptN = exceptN + 1
			if not 'list index out of range' in TypeError: extra = extra + newline + "i" + space2 + str(i) + space + "TypeError" + space2 + str(TypeError)
			else: printpoint = printpoint + "8"
			'''---------------------------'''
		
		i = i + 1
	numOfItems2 = totalResults - invalidN - duplicatesN - exceptN
	totalpagesN = (numOfItems2 / pagesizeN) + 1

	nextpage = pageN + 1
	nextpageS = str(nextpage)
	
	#url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=40&start-index=2'
	#addDir('[COLOR=Yellow]' + str79521.encode('utf-8') + '[/COLOR]',playlistid,9,"special://skin/media/icons/se.png",str79528.encode('utf-8'),'25',"") #More Results
	#if totalpagesN > pageN: addDir('[COLOR=Yellow]' + str79521.encode('utf-8') + '[/COLOR]','plugin://plugin.video.youtube/playlist/'+playlistid+'/',13,"special://skin/media/DefaultPlaylist.png",str79528.encode('utf-8'),nextpageS,"") #More Results
	if totalpagesN > pageN: addDir('[COLOR=Yellow]' + str33078.encode('utf-8') + '[/COLOR]',playlistid,13,"special://skin/media/DefaultVideo2.png",str79528.encode('utf-8'),nextpageS,50) #Next Page

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if admin:
		if validS != "": extra = "validS" + space2 + str(validS) + newline + extra
		if invalidS != "": extra = "invalidS" + space2 + str(invalidS) + newline + extra
		if playlist != "": extra = "playlist" + space2 + str(playlist) + newline + extra
		
		print printfirst + "ListPlaylist_LV" + printpoint + space + "i" + space2 + str(i) + space + "totalResults" + space2 + str(totalResults) + space + "numOfItems2" + space2 + str(numOfItems2) + newline + \
		"playlistid" + space2 + playlistid + space + "page" + space2 + pageS + " / " + str(totalpagesN) + space + "pagesize" + space2 + str(pagesizeN) + newline + \
		"extra" + space2 + str(extra)
		'''---------------------------'''

	
def Trial(admin):
	'''------------------------------
	---TRIAL-------------------------
	------------------------------'''
	if xbmc.getSkinDir() == 'skin.htpt':
		from shared_variables import htpt_a1, htpt_a2
		printpoint = ""
		trialdateD = stringtodate(trialdate,'%Y-%m-%d')
		trialdate2D = stringtodate(trialdate2,'%Y-%m-%d')
		datenowD = stringtodate(datenowS,'%Y-%m-%d')
		dateafterD = stringtodate(dateafterS,'%Y-%m-%d')
		id3str = xbmc.getInfoLabel('Skin.String(ID3)')
		id9str = xbmc.getInfoLabel('Skin.String(ID9)')
		'''---------------------------'''
		if trialdate and trial:
			'''------------------------------
			---SET-NEW-TRIAL-----------------
			------------------------------'''
			if trialdate2 == str70000 and trialdate == xbmc.getInfoLabel('System.Date(DD-MM-YY)') and not trial2:
				printpoint = printpoint + "1"
				returned = dialogyesno('$LOCALIZE[78869]', '$LOCALIZE[78870]')
				if returned == "ok":
					'''------------------------------
					---ACTIVATE-TRIAL-1--------------
					------------------------------'''
					setSkinSetting("0", 'TrialDate', datenowS)
					setSkinSetting("0", 'TrialDate2', dateafterS)
					setSkinSetting("0", 'ID9', trialstr)
					setSkinSetting("1", 'Trial2', "true")
					dialogok('$LOCALIZE[78871]', str79536.encode('utf-8') % (datenowS, dateafterS),"", "", line1c="Yellow")
					'''---------------------------'''
				else: notification_common("9")
				'''---------------------------'''
				
			elif trialdate2 != str70000 or trial2:
				printpoint = printpoint + "2"
				returned = dialogyesno('$LOCALIZE[76535]', '$LOCALIZE[76536]')
				if returned == "ok":
					'''------------------------------
					---ACTIVATE-TRIAL-2--------------
					------------------------------'''
					setSkinSetting("0", 'ID3', trialstr)
					setSkinSetting("0", 'ID7', trialstr)
					setSkinSetting("0", 'ID9', "")
					dialogok('$LOCALIZE[76537]', '$LOCALIZE[76538]', '$LOCALIZE[79081]', "", line1c="Yellow")
					'''---------------------------'''
			else: printpoint = printpoint + "3"
			'''---------------------------'''

		if trial2 and trialdate and trialdate2:
			'''------------------------------
			---TRIAL-CHECK-------------------
			------------------------------'''
			printpoint = printpoint + "5"
			
			if trialdate2D < datenowD or trialdate2D < trialdateD or dateafterD < trialdate2D or datenowD < trialdateD:
				'''------------------------------
				---TRIAL-ENDED-------------------
				------------------------------'''
				printpoint = printpoint + "6"
				if id3str != trial3str or id9str != trial3str: xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=3)')
				setSkinSetting("0", 'ID3', trial3str)
				setSkinSetting("0", 'ID9', trial3str)
				dialogok('$LOCALIZE[78991]', str79536.encode('utf-8') % (trialdate, trialdate2) + '[CR]', '$LOCALIZE[78990]',str79081 + space4 + '0547009911', line1c="Green", line3c="Yellow")
				'''---------------------------'''
				
			if dateafterD < trialdate2D or datenowD < trialdateD:
				'''------------------------------
				---TRIAL-USER-ERROR--------------
				------------------------------'''
				printpoint = printpoint + "!"
				setSkinSetting("0", 'ID5', "000")
				setSkinSetting("0", 'ID7', "000")
				xbmc.sleep(1000)
				setSkinSetting("1", 'Trial2', "false")
				'''---------------------------'''
				
		'''------------------------------
		---RESET-SETTINGS----------------
		------------------------------'''
		if not trial and not trial2:
			setSkinSetting("0", 'TrialDate', "")
			setSkinSetting("0", 'TrialDate2', "")
			'''---------------------------'''
		setSkinSetting("1", 'Trial', "false")
		'''---------------------------'''
		id9str = xbmc.getInfoLabel('Skin.String(ID9)')
		id3str = xbmc.getInfoLabel('Skin.String(ID3)')
		id7str = xbmc.getInfoLabel('Skin.String(ID7)')
		if id9str == htpt_a2 and id3str != trialstr and id7str != trialstr: setSkinSetting("1", 'Trial2', "false")
		'''---------------------------'''
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		if admin: moreinfo = "id9str" + space2 + id9str + space + "id3str" + space2 + id3str + space + "id7str" + space2 + id7str
		else: moreinfo = ""
		print printfirst + "Trial_LV" + printpoint + space + moreinfo
		'''---------------------------'''

def Trial_Renew(idstr_, htptfixversion_, Addon_Version, htptfixversion):
	'''------------------------------
	---***---------------------------
	------------------------------'''
	if xbmc.getSkinDir() == 'skin.htpt':
		from variables import datenowS, dateafterS, trialstr
		printpoint = ""
		if id9str == trial3str and id3str == trial3str:
			printpoint = printpoint + "1"
			if trialdate != "" and trialdate2 != "":
				printpoint = printpoint + "2"
				if (Addon_Version != htptfixversion and htptfixversion == htptfixversion_) and idstr_ == scripthtptinstall_User_ID:
					printpoint = printpoint + "3"
					'''execute'''
					setSkinSetting("1", 'Trial', "false")
					setSkinSetting("1", 'Trial2', "true")
					setSkinSetting("0",'TrialDate',datenowS)
					setSkinSetting("0",'TrialDate2',dateafterS)
					setSkinSetting("0",'ID3',trial2str)
					setSkinSetting("0",'ID9',trialstr)
					'''---------------------------'''
					if id5str == "000": setSkinSetting("0",'ID5',"0")
					if id7str == "000": setSkinSetting("0",'ID7',"")
					'''---------------------------'''
					dialogyesno_aW = xbmc.getCondVisibility('Window.IsActive(DialogYesNo.xml)')
					if dialogyesno_aW: xbmc.executebuiltin('Action(close)')
					xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=2)')
					dialogok('$LOCALIZE[77779]',str79573.encode('utf-8') + space2 + trialdate + " - " + trialdate2, str79574.encode('utf-8') + space2 + datenowS + " - " + dateafterS, '[CR]' + '[COLOR=Yellow]' + '$LOCALIZE[79084]' + '[/COLOR]', line1c="Yellow")
					'''---------------------------'''
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "Trial_Renew_LV" + printpoint + space + "idstr_" + space2 + idstr_ + space + "scripthtptinstall_User_ID" + space2 + str(scripthtptinstall_User_ID)
		if not "1" in printpoint: print printfirst + "Trial_Renew_LV" + printpoint + space + "trial/2" + space2 + trial + " / " + trial2 + space + "id9str" + space2 + id9str + space + "id3str" + space2 + id3str + space
		if not "3" in printpoint: print printfirst + "Trial_Renew_LV" + printpoint + space + "htptfixversion_" + space2 + htptfixversion_ + space + "htptfixversion" + space2 + htptfixversion + space + "Addon_Version" + space2 + Addon_Version + space + "trialdate/2" + space + trialdate + " / " + trialdate2 + space
		if "3" in printpoint: print printfirst + "Trial_Renew_LV" + printpoint + space2 + "datenowS" + space2 + datenowS + space + "dateafterS" + space2 + dateafterS
		'''---------------------------'''
	
def Activate_Account(idstr_, htptfixversion_, Addon_Version, htptfixversion, id2set):
	'''------------------------------
	---***---------------------------
	------------------------------'''
	if xbmc.getSkinDir() == 'skin.htpt':
		from shared_variables import htpt_a1, htpt_a2, datenowS
		import datetime as dt #Can cause a bug with stringtodate!
		
		id1str = xbmc.getInfoLabel('Skin.String(ID1)')
		printpoint = "" ; id2setD = ""
		if (Addon_Version != htptfixversion and htptfixversion == htptfixversion_) and idstr_ == scripthtptinstall_User_ID:
			printpoint = printpoint + "1"
			datenowD = stringtodate(datenowS,'%Y-%m-%d')
			try:
				id2strD = stringtodate(id2str,'%Y-%m-%d')
				if not id2strD <= datenowD: id2strD = ""
			except: id2strD = ""

			#if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
			#elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
			'''---------------------------'''
			'''execute'''
			setSkinSetting("0",'TrialDate',"")
			setSkinSetting("0",'TrialDate2',"")
			setSkinSetting("1",'Trial',"false")
			setSkinSetting("1",'Trial2',"false")

			if id2set != "":
				try:
					id2setD = stringtodate(id2set,'%Y-%m-%d')
					if not id2set <= datenowD: id2setD = ""
				except: id2setD = ""
				
			if id2setD != "":
				printpoint = printpoint + "4"
				dateafter364 = id2setD + dt.timedelta(days=364)
				dateafter364S = str(dateafter364)
				dateafter364S = dateafter364S.replace(" 00:00:00","",1)
				setSkinSetting("0",'ID2',id2set)
				setSkinSetting("0",'ID3',dateafter364S)
				'''---------------------------'''
					
			elif id2strD != "":
				printpoint = printpoint + "5"
				dateafter364 = id2strD + dt.timedelta(days=364)
				dateafter364S = str(dateafter364)
				dateafter364S = dateafter364S.replace(" 00:00:00","",1)
				setSkinSetting("0",'ID3',dateafter364S)
				'''---------------------------'''
			else:
				printpoint = printpoint + "6"
				datenowM7 = datenow - dt.timedelta(days=7)
				datenowM7S = str(datenowM7)
				datenowM14 = datenow - dt.timedelta(days=14)
				datenowM14S = str(datenowM14)
				dateafter364 = datenow + dt.timedelta(days=364)
				dateafter357 = datenow + dt.timedelta(days=357)
				dateafter350 = datenow + dt.timedelta(days=350)
				dateafter364S = str(dateafter364)
				dateafter364S = dateafter364S.replace(" 00:00:00","",1)
				dateafter357S = str(dateafter357)
				dateafter357S = dateafter357S.replace(" 00:00:00","",1)
				dateafter350S = str(dateafter350)
				dateafter350S = dateafter350S.replace(" 00:00:00","",1)
				'''---------------------------'''
				if id3str == "":
					setSkinSetting("0",'ID2',datenowS)
					setSkinSetting("0",'ID3',dateafter364S)
					'''---------------------------'''
				elif id3str == trialstr:
					setSkinSetting("0",'ID2',datenowM7S)
					setSkinSetting("0",'ID3',dateafter357S)
					'''---------------------------'''
				elif id3str == trial2str:
					setSkinSetting("0",'ID2',datenowM14S)
					setSkinSetting("0",'ID3',dateafter350S)
					'''---------------------------'''
				elif id3str == trial3str:
					setSkinSetting("0",'ID2',datenowM14S)
					setSkinSetting("0",'ID3',dateafter350S)
					'''---------------------------'''
				else:
					setSkinSetting("0",'ID2',datenowS + "?")
					setSkinSetting("0",'ID3',dateafter364S + "?")
					'''---------------------------'''
			if id4str == "": setSkinSetting("0",'ID4',"?")
			if id5str == "" or id5str == "000": setSkinSetting("0",'ID5',"?")
			if id6str == "": setSkinSetting("0",'ID6',"?")
			if id7str == "000" or id7str == "Trial": setSkinSetting("0",'ID7',"")
			if id8str == "": setSkinSetting("0",'ID8',"?")
			setSkinSetting("0",'ID9',htpt_a2)
			xbmc.executebuiltin('RunScript(service.htpt.debug,,?mode=18)')
			dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
			if dialogyesnoW: xbmc.executebuiltin('Action(close)')
			dialogok(str79538.encode('utf-8') % (id1str.decode('utf-8').encode('utf-8')), xbmc.getInfoLabel('$LOCALIZE[74537]') + '[CR][CR]', '$LOCALIZE[79084]',"", line1c="Yellow")
			'''---------------------------'''
		
		'''------------------------------
		---PRINT-END---------------------
		------------------------------'''
		print printfirst + "Activate_Account_LV" + printpoint + space + "idstr_" + space2 + idstr_ + space + "scripthtptinstall_User_ID" + space2 + str(scripthtptinstall_User_ID) + space + "datenowS" + space2 + datenowS
		'''---------------------------'''