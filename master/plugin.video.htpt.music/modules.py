# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	addDir(addonString(100).encode('utf-8'),'MyMusic',100,"",addonString(1000).encode('utf-8'),'1',50, getAddonFanart(100)) #My Music
	addDir(addonString(101).encode('utf-8'),'',101,htptservicemedia_path + "music.png",addonString(1010).encode('utf-8'),'1',58, getAddonFanart(101)) #Israeli Music
	addDir(addonString(102).encode('utf-8'),'',102,htptservicemedia_path + "karaoke.png",addonString(1020).encode('utf-8'),'1',58, getAddonFanart(102)) #Israeli Karaoke
	addDir(addonString(104).encode('utf-8'),'',104,htptservicemedia_path + "guitar.png",addonString(1040).encode('utf-8'),'1',58, getAddonFanart(104)) #Israeli Liveshows
	if admin: addDir(addonString(105).encode('utf-8'),'',105,htptservicemedia_path + "microphone.png",addonString(1050).encode('utf-8'),'1',58, getAddonFanart(105)) #Israeli Djs
	'''---------------------------'''
	addDir(addonString(111).encode('utf-8'),'',111,htptservicemedia_path + "music.png",addonString(1110).encode('utf-8'),'1',58, getAddonFanart(111)) #Foreign Music
	if admin: addDir(addonString(112).encode('utf-8'),'',112,htptservicemedia_path + "karaoke.png",addonString(1120).encode('utf-8'),'1',58, getAddonFanart(112)) #Foreign Karaoke
	if admin: addDir(addonString(114).encode('utf-8'),'',114,htptservicemedia_path + "guitar.png",addonString(1140).encode('utf-8'),'1',58, getAddonFanart(114)) #Foreign Liveshows
	if admin: addDir(addonString(115).encode('utf-8'),'',115,htptservicemedia_path + "microphone.png",addonString(1150).encode('utf-8'),'1',58, getAddonFanart(115)) #Foreign Djs
	'''---------------------------'''
	if admin: addDir(addonString(121).encode('utf-8'),'',121,htptservicemedia_path + "classical.png",addonString(1210).encode('utf-8'),'1',58, getAddonFanart(121)) #Classical Music

def CATEGORIES100(admin):
	'''------------------------------
	---My-Music----------------------
	------------------------------'''
	background = 100
	
	'''כפתור מוזיקה חדש..'''
	addDir(addonString(6).encode('utf-8'),"New",20,htptservicemedia_path + "clipboard.png",addonString(4).encode('utf-8') + addonString(7).encode('utf-8') + addonString(5).encode('utf-8'),'1',50, getAddonFanart(background))
	
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',50, getAddonFanart("Custom_Playlist1"))
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',50, getAddonFanart("Custom_Playlist2"))
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',50, getAddonFanart("Custom_Playlist3"))
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',50, getAddonFanart("Custom_Playlist4"))
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',50, getAddonFanart("Custom_Playlist5"))
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',50, getAddonFanart("Custom_Playlist6"))
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',50, getAddonFanart("Custom_Playlist7"))
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',50, getAddonFanart("Custom_Playlist8"))
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',50, getAddonFanart("Custom_Playlist9"))
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',50, getAddonFanart("Custom_Playlist10"))
	
def CATEGORIES101(admin):
	'''------------------------------
	---Israeli-Music-----------------
	------------------------------'''
	background = 101
	commonsearch = "commonsearch101"
	
	'''חיפוש'''
	addDir(localize(137),commonsearch,3,htptservicemedia_path + "se.png",addonString_servicehtpt(23).encode('utf-8') % (addonString(2).encode('utf-8')),'1',"", getAddonFanart(background))
	
	'''הכל'''
	#addDir(str593.encode('utf-8'),'livni2',9,"http://markharai.com/wp-content/uploads/2010/11/megaphone.png.scaled980-300x300.png","",'1',"", getAddonFanart(background))
	addDir(localize(593),'plugin://plugin.video.youtube/channel/UCw_JTl5vBNd_ILZsGOecXmQ/playlists/',8,"http://markharai.com/wp-content/uploads/2010/11/megaphone.png.scaled980-300x300.png","",'1',"", getAddonFanart(background))
	#ActivateWindow(10025,&quot;plugin://plugin.video.youtube/channel/UCw_JTl5vBNd_ILZsGOecXmQ/playlists/&quot;,return)
	
	'''אביתר בנאי'''
	addDir(addonString(10101).encode('utf-8'),'EviatarBanaiOfficial',9,'http://images.mouse.co.il/storage/7/f/eviatar-ggg.jpg',addonString(101010).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''אברהם טל'''
	addDir(addonString(10102).encode('utf-8'),'avrahamtal',9,'http://images.mouse.co.il/storage/a/d/Avraham_Tal_490.jpg',addonString(101020).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''אייל גולן'''
	addDir(addonString(10103).encode('utf-8'),'EyalGolanOfficial',9,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''איתי לוי'''
	addDir(addonString(10104).encode('utf-8'),'LevitayOfficial',9,'http://img.mako.co.il/2014/01/20/mooma_itay_levi_beleylot_karim_c.jpg',addonString(101040).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''אליעד'''
	addDir(addonString(10109).encode('utf-8'),'OfficialEliad',9,'http://img.mako.co.il/2015/07/15/GGkfkf5_c.jpg',addonString(101090).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''אתניקס'''
	addDir(addonString(10105).encode('utf-8'),'EthnixOfficial',9,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(101050).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''ברי סחרוף'''
	addDir(addonString(10106).encode('utf-8'),'sakharofficial',9,'http://img.mako.co.il/2010/10/22/dan_toren_15c.jpg',addonString(101060).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''גיא ויהל'''
	addDir(addonString(10108).encode('utf-8'),'GuyYahelOfficial',9,'http://i.ytimg.com/vi/9fkcGdgj-iI/hqdefault.jpg',addonString(101080).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''דודו אהרון'''
	addDir(addonString(10107).encode('utf-8'),'DuduAharonOfficiaI',9,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''דודו טסה'''
	addDir(addonString(10110).encode('utf-8'),'DuduTassaOfficial',9,'http://www.nrg.co.il/images/archive/465x349/1/028/989.jpg',addonString(101100).encode('utf-8'),'1',"", getAddonFanart(background))

	'''דני סנדרסון'''
	addDir(addonString(10111).encode('utf-8'),'PLWs5r3WqRUR0kiPs-hou6gtDbj9qlUBK_',13,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(101110).encode('utf-8'),'1',"", getAddonFanart(background))
			
	'''הפרויקט של רביבו'''
	addDir(addonString(10112).encode('utf-8'),'TheRevivoProject',9,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''הראל סקעת'''
	addDir(addonString(10113).encode('utf-8'),'skaatharel',9,'https://i.ytimg.com/i/BbOw6LiHmj6L9o_HlMvKKg/mq1.jpg?v=51c9be2d',addonString(101130).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''חיים משה'''
	addDir(addonString(10114).encode('utf-8'),'haimmosheoffical',9,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''יהושוע אהרון'''
	addDir(addonString(10115).encode('utf-8'),'worshipinisrael',9,'https://yt3.ggpht.com/-ohYJ_SZGouY/AAAAAAAAAAI/AAAAAAAAAAA/WTRKUc-dpwE/s100-c-k-no/photo.jpg',addonString(101150).encode('utf-8'),'1',"", getAddonFanart(background))	
	
	'''יעקב חתן'''
	addDir(addonString(10116).encode('utf-8'),'MrBeitarj',9,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ישי לוי'''
	addDir(addonString(10117).encode('utf-8'),'IshayLeviOfficial',9,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background))

	'''ליאור נרקיס'''
	addDir(addonString(10118).encode('utf-8'),'LiorNarkisOfficial',9,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''לירן דנינו'''
	addDir(addonString(10119).encode('utf-8'),'LiranDaninoMusic',9,'https://i.ytimg.com/i/vYVVsleioHXLy08I8LmVCQ/mq1.jpg?v=55057e3c',addonString(101190).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מאיה בוסקילה'''
	addDir(addonString(10120).encode('utf-8'),'mayabos',9,'https://yt3.ggpht.com/-5PEvWjlVLN4/AAAAAAAAAAI/AAAAAAAAAAA/tNQGMUjQfxE/s100-c-k-no/photo.jpg',addonString(101200).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''מוש בן ארי'''
	addDir(addonString(10121).encode('utf-8'),'MoshBA1',9,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(101210).encode('utf-8'),'1',"", getAddonFanart(background))

	'''מושיק עפיה'''
	addDir(addonString(10122).encode('utf-8'),'MoshikAfiaOfficial',9,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מירי מסיקה'''
	addDir(addonString(10123).encode('utf-8'),'MiriMesikaOfficial',9,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(101230).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''מאור אדרי'''
	addDir(addonString(10124).encode('utf-8'),'MaorEdriOfficiial',9,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''משה פרץ'''
	addDir(addonString(10125).encode('utf-8'),'MoshePerezOfficial',9,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''משינה'''
	addDir(addonString(10126).encode('utf-8'),'Mashinaofficial',9,'https://i.ytimg.com/i/HLMP6lold_s1cFfiLg4t6g/mq1.jpg?v=51b9bb69',addonString(101260).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''נתן גושן'''
	addDir(addonString(10127).encode('utf-8'),'NathanGoshenOfficial',9,'https://i.ytimg.com/i/Bh-trCMk-XPOP7WgAdkpPg/mq1.jpg?v=54d87328',addonString(101270).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''סאבלימינל'''
	addDir(addonString(10128).encode('utf-8'),'SubliminalOfficial',9,'https://yt3.ggpht.com/-BnbsgmTB25g/AAAAAAAAAAI/AAAAAAAAAAA/mUFJQWSaKA8/s100-c-k-no/photo.jpg',addonString(101280).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''סטלוס ואורן חן'''
	addDir(addonString(10129).encode('utf-8'),'plugin://plugin.video.youtube/channel/UClhlTKsREdNMKga6_I2dFyQ/',8,'https://yt3.ggpht.com/-2gpbz_o3W7I/AAAAAAAAAAI/AAAAAAAAAAA/PfzwwLycsmo/s100-c-k-no/photo.jpg',addonString(101290).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עברי לידר'''
	addDir(addonString(10130).encode('utf-8'),'IvriLiderOfficial',9,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(101300).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עידן רפאל חביב'''
	addDir(addonString(10131).encode('utf-8'),'baswaka9',9,'https://yt3.ggpht.com/-l9mhWhO0kT8/AAAAAAAAAAI/AAAAAAAAAAA/iv1toJVFwSQ/s100-c-k-no/photo.jpg',addonString(101310).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עידן רייכל'''
	addDir(addonString(10132).encode('utf-8'),'idanraichelofficial',9,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(101320).encode('utf-8'),'1',"", getAddonFanart(background))

	'''עומר אדם'''
	addDir(addonString(10133).encode('utf-8'),'OmerAdamOfficial',9,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עמיר בניון'''
	addDir(addonString(10134).encode('utf-8'),'nevelasorpr',9,'http://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Amir_Benayoun.JPG/450px-Amir_Benayoun.JPG',addonString(101340).encode('utf-8'),'1',"", getAddonFanart(background))

	'''פאר טסי'''
	addDir(addonString(10135).encode('utf-8'),'peertasimizrahi',9,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קובי אפללו'''
	addDir(addonString(10136).encode('utf-8'),'TheKobiAflalo',9,'https://yt3.ggpht.com/-W5wjK70SQ1U/AAAAAAAAAAI/AAAAAAAAAAA/Ibov9BPmodU/s100-c-k-no/photo.jpg',addonString(101360).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קובי פרץ'''
	addDir(addonString(10137).encode('utf-8'),'KobiPeretzOfficial',9,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קרן פלס'''
	addDir(addonString(10138).encode('utf-8'),'KerenPelesOfficial',9,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(101380).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ריטה'''
	addDir(addonString(10139).encode('utf-8'),'ritaofficial',9,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(101390).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''רמי קליינשטיין'''
	addDir(addonString(10140).encode('utf-8'),'RamiKleinshteinMusic',9,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(101400).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שירי מימון'''
	addDir(addonString(10141).encode('utf-8'),'ShiriMaimonOfficial',9,'http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sm_album3.jpg/250px-Sm_album3.jpg',addonString(101410).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שלום חנוך'''
	addDir(addonString(10142).encode('utf-8'),'ShalomHanoch',9,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(101420).encode('utf-8'),'1',"", getAddonFanart(background))

	'''שלומי שבת'''
	addDir(addonString(10143).encode('utf-8'),'shlomishabatofficiaI',9,'https://i.ytimg.com/i/GaHPMv8YIv_0HfRDQQ44cA/mq1.jpg?v=af5444',addonString(101430).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שלמה ארצי'''
	addDir(addonString(10144).encode('utf-8'),'ShlomoArtziOfficial',9,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(101440).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שרית חדד'''
	addDir(addonString(10145).encode('utf-8'),'SaritHadadOfficial',9,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(101450).encode('utf-8'),'1',"", getAddonFanart(background))
	
	''''''
	#addDir(addonString(10146).encode('utf-8'),'',9,'',addonString(101460).encode('utf-8'),'1',"", getAddonFanart(background))
	
	''''''
	#addDir(addonString(10147).encode('utf-8'),'',9,'',addonString(101470).encode('utf-8'),'1',"", getAddonFanart(background))
	
	''''''
	#addDir(addonString(10148).encode('utf-8'),'',9,'',addonString(101480).encode('utf-8'),'1',"", getAddonFanart(background))
	
	''''''
	#addDir(addonString(10149).encode('utf-8'),'',9,'',addonString(101490).encode('utf-8'),'1',"", getAddonFanart(background))
	
	''''''
	#addDir(addonString(10150).encode('utf-8'),'',9,'',addonString(101500).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עוד...'''
	addDir(str22082.encode('utf-8'),'HeliconRecords',9,"special://skin/media/icons/buttonadd.png","",'1',"", getAddonFanart(background))

def CATEGORIES102(admin):
	'''------------------------------
	---Israeli-Karaoke---------------
	------------------------------'''
	background = 102
	commonsearch = "commonsearch102"
	
	'''חיפוש'''
	addDir(localize(137),commonsearch,3,htptservicemedia_path + "se.png",addonString_servicehtpt(23) % (localize(13327).decode('utf-8')),'1',"", getAddonFanart(background))
	
	'''הכל'''
	list = []
	list.append('&youtube_ch=sharimkaraokeltd')
	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	list.append('&youtube_pl=PLjHwF6MA1nycO4TXyQ0Di7ADrg9wTJ8XW')
	list.append('&youtube_pl=PL6WvGFcuPjESeFQY0YyCzTy7qTofzMlaQ')
	list.append('&youtube_pl=PL7302191F8A43E01C')
	addDir(localize(593),list,17,"http://markharai.com/wp-content/uploads/2010/11/megaphone.png.scaled980-300x300.png","",'1',"", getAddonFanart(background))

	'''אייל גולן'''
	addDir(addonString(10103).encode('utf-8'),commonsearch,3,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''איתי לוי'''
	addDir(addonString(10104).encode('utf-8'),commonsearch,3,'http://img.mako.co.il/2014/01/20/mooma_itay_levi_beleylot_karim_c.jpg',addonString(101040).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''אתניקס'''
	addDir(addonString(10105).encode('utf-8'),commonsearch,3,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(101050).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''ברי סחרוף'''
	addDir(addonString(10106).encode('utf-8'),commonsearch,3,'http://img.mako.co.il/2010/10/22/dan_toren_15c.jpg',addonString(101060).encode('utf-8'),'1', 58)
		
	'''דודו אהרון'''
	addDir(addonString(10107).encode('utf-8'),commonsearch,3,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''דני סנדרסון'''
	addDir(addonString(10111).encode('utf-8'),commonsearch,3,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(101110).encode('utf-8'),'1',"", getAddonFanart(background))
			
	'''הפרויקט של רביבו'''
	addDir(addonString(10112).encode('utf-8'),commonsearch,3,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background))

	'''חיים משה'''
	addDir(addonString(10114).encode('utf-8'),commonsearch,3,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''יהושוע אהרון'''
	addDir(addonString(10115).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-ohYJ_SZGouY/AAAAAAAAAAI/AAAAAAAAAAA/WTRKUc-dpwE/s100-c-k-no/photo.jpg',addonString(101150).encode('utf-8'),'1',"", getAddonFanart(background))	
	
	'''יעקב חתן'''
	addDir(addonString(10116).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ישי לוי'''
	addDir(addonString(10117).encode('utf-8'),commonsearch,3,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background))

	'''ליאור נרקיס'''
	addDir(addonString(10118).encode('utf-8'),commonsearch,3,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''לירן דנינו'''
	addDir(addonString(10119).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/vYVVsleioHXLy08I8LmVCQ/mq1.jpg?v=55057e3c',addonString(101190).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מאיה בוסקילה'''
	addDir(addonString(10120).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-5PEvWjlVLN4/AAAAAAAAAAI/AAAAAAAAAAA/tNQGMUjQfxE/s100-c-k-no/photo.jpg',addonString(101200).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''מוש בן ארי'''
	addDir(addonString(10121).encode('utf-8'),commonsearch,3,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(101210).encode('utf-8'),'1',"", getAddonFanart(background))

	'''מושיק עפיה'''
	addDir(addonString(10122).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מירי מסיקה'''
	addDir(addonString(10123).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(101230).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''מאור אדרי'''
	addDir(addonString(10124).encode('utf-8'),commonsearch,3,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''משה פרץ'''
	addDir(addonString(10125).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''משינה'''
	addDir(addonString(10126).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/HLMP6lold_s1cFfiLg4t6g/mq1.jpg?v=51b9bb69',addonString(101260).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''נתן גושן'''
	addDir(addonString(10127).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/Bh-trCMk-XPOP7WgAdkpPg/mq1.jpg?v=54d87328',addonString(101270).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''סאבלימינל'''
	addDir(addonString(10128).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-BnbsgmTB25g/AAAAAAAAAAI/AAAAAAAAAAA/mUFJQWSaKA8/s100-c-k-no/photo.jpg',addonString(101280).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''סטלוס ואורן חן'''
	addDir(addonString(10129).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-2gpbz_o3W7I/AAAAAAAAAAI/AAAAAAAAAAA/PfzwwLycsmo/s100-c-k-no/photo.jpg',addonString(101290).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עברי לידר'''
	addDir(addonString(10130).encode('utf-8'),commonsearch,3,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(101300).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עידן רפאל חביב'''
	addDir(addonString(10131).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-l9mhWhO0kT8/AAAAAAAAAAI/AAAAAAAAAAA/iv1toJVFwSQ/s100-c-k-no/photo.jpg',addonString(101310).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עידן רייכל'''
	addDir(addonString(10132).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(101320).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עומר אדם'''
	addDir(addonString(10133).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עמיר בניון'''
	addDir(addonString(10134).encode('utf-8'),commonsearch,3,'http://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Amir_Benayoun.JPG/450px-Amir_Benayoun.JPG',addonString(101340).encode('utf-8'),'1',"", getAddonFanart(background))

	'''פאר טסי'''
	addDir(addonString(10135).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קובי אפללו'''
	addDir(addonString(10136).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-W5wjK70SQ1U/AAAAAAAAAAI/AAAAAAAAAAA/Ibov9BPmodU/s100-c-k-no/photo.jpg',addonString(101360).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קובי פרץ'''
	addDir(addonString(10137).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קרן פלס'''
	addDir(addonString(10138).encode('utf-8'),commonsearch,3,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(101380).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ריטה'''
	addDir(addonString(10139).encode('utf-8'),commonsearch,3,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(101390).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''רמי קליינשטיין'''
	addDir(addonString(10140).encode('utf-8'),commonsearch,3,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(101400).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שירי מימון'''
	addDir(addonString(10141).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-33p31sJqT88/AAAAAAAAAAI/AAAAAAAAAAA/taeHwLul6Io/s100-c-k-no/photo.jpg',addonString(101410).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שלום חנוך'''
	addDir(addonString(10142).encode('utf-8'),commonsearch,3,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(101420).encode('utf-8'),'1',"", getAddonFanart(background))

	'''שלומי שבת'''
	addDir(addonString(10143).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/GaHPMv8YIv_0HfRDQQ44cA/mq1.jpg?v=af5444',addonString(101430).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שלמה ארצי'''
	addDir(addonString(10144).encode('utf-8'),commonsearch,3,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(101440).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שרית חדד'''
	addDir(addonString(10145).encode('utf-8'),commonsearch,3,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(11450).encode('utf-8'),'1',"", getAddonFanart(background))
	
def CATEGORIES104(admin):
	'''------------------------------
	---Israeli-Liveshows-------------
	------------------------------'''
	background = 104
	commonsearch = "commonsearch104"
	
	'''חיפוש'''
	addDir(localize(137),commonsearch,3,htptservicemedia_path + "se.png",addonString_servicehtpt(23) % (addonString(1)),'1',"", getAddonFanart(background))
	
	'''הכל'''
	addDir(localize(593),'livni2',9,"http://markharai.com/wp-content/uploads/2010/11/megaphone.png.scaled980-300x300.png","",'1',"", getAddonFanart(background))

	'''אייל גולן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10103).encode('utf-8'),['&youtube_id=81Vh9FriKfc', '&youtube_pl=PLB781B8A94339CC67', '&youtube_id=RqLn1vCQVMo', '&youtube_id=fTTsZ1OGZV8', '&youtube_id=hqnv8qVOqLY', '&youtube_id=9GdWNAXvd0g', '&youtube_id=uhDjEYmF-oo', '&youtube_pl=PL2l4T5NjtOsrGnFacKHUc1m7F1Kojuisq', '&youtube_id=bI85XpkVTHg'], + \
	17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''איתי לוי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10104).encode('utf-8'),['&youtube_id=MH6pTUgIu2Y', '&youtube_id=ip559Yi1mtY', '&youtube_id=SitMVqRhX60', '&youtube_id=ercP3za8eSQ'],17,'http://img.mako.co.il/2014/01/20/mooma_itay_levi_beleylot_karim_c.jpg',addonString(101040).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''אתניקס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10105).encode('utf-8'),['&youtube_pl=PL7M1X2KObyxpFPtF2x33tdJVXKlpOE0wm', '&youtube_id=dzbN8WG33Sg', '&youtube_id=0_n5BLIk6D4', '&youtube_id=sRjlF4Z262w', '&youtube_id=q13ohAH_I-I'],17,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(101050).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''ברי סחרוף'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL01DA343E8BB95D12')
	list.append('&youtube_pl=PLeZqOp-eE-FpvoWCBK-G5Wr1y_VA5Y4ih')
	list.append('&youtube_pl=PLeZqOp-eE-FqJOAKrN7YN6aE8IsKxPqSZ&index=2')
	list.append('&youtube_pl=PL104313B485ECC1DB')
	list.append('&youtube_id=9Oyiis9B6pU')
	list.append('&youtube_id=sVXFm5lOqy8')
	list.append('&youtube_id=ku8mNNCrEys')
	list.append('&youtube_id=P5KW_r2Uu1c')
	addDir(addonString(10106).encode('utf-8'),list,17,'http://img.mako.co.il/2010/10/22/dan_toren_15c.jpg',addonString(101060).encode('utf-8'),'1', 50)
		
	'''דודו אהרון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLF487E714444A3272')
	list.append('&youtube_pl=PL2E6FC61CB0B4C510')
	list.append('&youtube_pl=PLEB6F71190B2A83D1')
	list.append('&youtube_pl=PL19F750D7137E32A2')
	list.append('youtube_id=TLT7tM6ZxLc')
	addDir(addonString(10107).encode('utf-8'),list,17,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''דני סנדרסון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10111).encode('utf-8'),['&youtube_pl=PLF867884C8D46A864', 'youtube_id=S2UWI6LooeM', 'youtube_id=eyimcCRqY4w', 'youtube_id=VNGXb8N5mrw', 'youtube_id=jnev_7SipPk', 'youtube_id=MWMvdkWlAis', 'youtube_id=7-UxjnOJkc0', 'youtube_id=goA2RNz1GXo', 'youtube_id=HDXDpyowM-w', 'youtube_id=FVe96EROE6k', 'youtube_id=634o-c7nsM8', 'youtube_id=U3ZonngA4E8', 'youtube_id=wwbYQOGTpYA'],17,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(101110).encode('utf-8'),'1',"", getAddonFanart(background))
			
	'''הפרויקט של רביבו'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10112).encode('utf-8'),['&youtube_pl=PLtQpQHKTXRlM7lPI_5rD4bpyPZRu0IkvB', '&youtube_id=kRzM7QxPk4I', '&youtube_id=GiOtZf7sV9c', '&youtube_id=at4HQssvFCY', '&youtube_id=khp0ONQKcS4', '&youtube_id=UJMB-wfkNqY', '&youtube_id=OqUuH03p1J4', '&youtube_id=iBaaYqMMCtI', '&youtube_id=n8b5YIXCEJ0'],17,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background))

	'''חיים משה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10114).encode('utf-8'),['&youtube_id=tp5jBsO1aKs', '&youtube_id=vxQkLouq2FA', '&youtube_id=v08pmMFcjzQ', '&youtube_id=ysMtHK3DufU', '&youtube_id=tNXkBUJh_0E', '&youtube_id=2GwVBzAp-j4', '&youtube_id=XksMJCIn8Xg', '&youtube_id=5wsETIhNIWo', '&youtube_id=ukik1um6_iU', '&youtube_id=-ICVE31U4lg', '&youtube_id=ccplk-lEIiQ', '&youtube_id=mqMcjRSZAhU', '&youtube_id=ZD5TKctpmS4'],17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''יהושוע אהרון'''
	#list = []
	#list.append('&youtube_se='+commonsearch+'')
	#addDir(addonString(10115).encode('utf-8'),list,17,'https://yt3.ggpht.com/-ohYJ_SZGouY/AAAAAAAAAAI/AAAAAAAAAAA/WTRKUc-dpwE/s100-c-k-no/photo.jpg',addonString(101150).encode('utf-8'),'1',"", getAddonFanart(background))	
	
	'''יעקב חתן'''
	#list = []
	#list.append('&youtube_se='+commonsearch+'')
	#addDir(addonString(10116).encode('utf-8'),'MrBeitarj',9,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ישי לוי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10117).encode('utf-8'),['&youtube_pl=PLv1v9m-FDMVqBylOgmLDDjxQucuVyKW12', '&youtube_pl=PL04D961E06FE727F7'],17,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background))

	'''ליאור נרקיס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10118).encode('utf-8'),['&youtube_pl=PLAA0970991BC5D286', '&youtube_id=hjpyGlciA74', '&youtube_id=qR5outGV3WE'],17,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''לירן דנינו'''
	#addDir(addonString(10119).encode('utf-8'),'LiranDaninoMusic',10419,'https://i.ytimg.com/i/vYVVsleioHXLy08I8LmVCQ/mq1.jpg?v=55057e3c',addonString(101190).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מאיה בוסקילה'''
	#addDir(addonString(10120).encode('utf-8'),'mayabos',10420,'https://yt3.ggpht.com/-5PEvWjlVLN4/AAAAAAAAAAI/AAAAAAAAAAA/tNQGMUjQfxE/s100-c-k-no/photo.jpg',addonString(101200).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''מוש בן ארי'''
	addDir(addonString(10121).encode('utf-8'),['&youtube_id=kNv3UW_9WxM', 'youtube_id=YeN12hSYDEQ', 'youtube_id=I0kHj1lz-7w', 'youtube_id=v67d3R96cS8', 'youtube_id=tI2ON_FCu0E', 'youtube_id=6V39QRTjxJA', 'youtube_id=pJaIMPEd6c8', 'youtube_id=VSW9-20xkt4', 'youtube_id=bWJgDQeXZc8', 'youtube_id=RcdlJ0Z5MEw'],17,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(101210).encode('utf-8'),'1',"", getAddonFanart(background))

	'''מושיק עפיה'''
	addDir(addonString(10122).encode('utf-8'),['&youtube_id=CeeA4BICM4M', '&youtube_id=PTmlzquqb0k', '&youtube_id=uxMPllmgV6c', '&youtube_id=AM2OQvGMqMA', '&youtube_id=PUQZp2_gTyg', '&youtube_id=5aFFOl4-SRY', '&youtube_id=1qalCKhglOE'],17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מירי מסיקה'''
	addDir(addonString(10123).encode('utf-8'),['&youtube_pl=PLfjHoXmP14hnvOwUzYY8A6YxM-YpZdLiK', '&youtube_id=hxktgo0Df_g', '&youtube_id=R2qT506LRpk', '&youtube_id=rbBvP5Z4lBs', '&youtube_id=rogROHXxFjM', '&youtube_id=lBAp2OWCcu4'],17,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(101230).encode('utf-8'),'1',"", getAddonFanart(background))
		
	'''מאור אדרי'''
	addDir(addonString(10124).encode('utf-8'),['&youtube_pl=PLmUWHf2-pPZEsNbXMoJYoA1O-2zGJEtHv', '&youtube_id=w3boSL65UZ4', '&youtube_id=IDVzo-FOE4k', '&youtube_id=3MOyFCkeViU', '&youtube_id=VpcqDALi97w', '&youtube_id=Pc1h1IcO5_o'],17,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''משה פרץ'''
	list = []
	list.append('&youtube_pl=PL_8KXLhQVQMKGzYt_5Wvdk7d_ve9Dc-AE')
	list.append('&youtube_id=xptpHXTrrv0')
	list.append('&youtube_id=dhW8XEkyzdU')
	list.append('&youtube_id=SdoFI2eqbQs')
	list.append('&youtube_id=SraFCGtrTtM')
	list.append('&youtube_id=vIyUoiA7R-c')
	list.append('&youtube_id=IUzhr-BkIcA')
	list.append('&youtube_id=mPSNlhZP-BM')
	list.append('&youtube_id=5M0rdjVBO4E')
	addDir(addonString(10125).encode('utf-8'),list,17,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''משינה'''
	list = []
	#list.append('&youtube_id=_hxkVbXt8G0')
	list.append('&youtube_se='+commonsearch+'')
	#list.append('')
	addDir(addonString(10126).encode('utf-8'),list,17,'https://i.ytimg.com/i/HLMP6lold_s1cFfiLg4t6g/mq1.jpg?v=51b9bb69',addonString(101260).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''נתן גושן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10127).encode('utf-8'),list,17,'https://i.ytimg.com/i/Bh-trCMk-XPOP7WgAdkpPg/mq1.jpg?v=54d87328',addonString(101270).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''סאבלימינל'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10128).encode('utf-8'),list,17,'https://yt3.ggpht.com/-BnbsgmTB25g/AAAAAAAAAAI/AAAAAAAAAAA/mUFJQWSaKA8/s100-c-k-no/photo.jpg',addonString(101280).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''סטלוס ואורן חן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10129).encode('utf-8'),list,17,'https://yt3.ggpht.com/-2gpbz_o3W7I/AAAAAAAAAAI/AAAAAAAAAAA/PfzwwLycsmo/s100-c-k-no/photo.jpg',addonString(101290).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עברי לידר'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10130).encode('utf-8'),list,17,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(101300).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עידן רפאל חביב'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10131).encode('utf-8'),list,17,'https://yt3.ggpht.com/-l9mhWhO0kT8/AAAAAAAAAAI/AAAAAAAAAAA/iv1toJVFwSQ/s100-c-k-no/photo.jpg',addonString(101310).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עידן רייכל'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10132).encode('utf-8'),list,17,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(101320).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עומר אדם'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10133).encode('utf-8'),list,17,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''עמיר בניון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10134).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Amir_Benayoun.JPG/450px-Amir_Benayoun.JPG',addonString(101340).encode('utf-8'),'1',"", getAddonFanart(background))

	'''פאר טסי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10135).encode('utf-8'),list,17,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קובי אפללו'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10136).encode('utf-8'),list,17,'https://yt3.ggpht.com/-W5wjK70SQ1U/AAAAAAAAAAI/AAAAAAAAAAA/Ibov9BPmodU/s100-c-k-no/photo.jpg',addonString(101360).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קובי פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10137).encode('utf-8'),list,17,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קרן פלס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10138).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(101380).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ריטה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10139).encode('utf-8'),list,17,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(101390).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''רמי קליינשטיין'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10140).encode('utf-8'),list,17,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(101400).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שירי מימון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10141).encode('utf-8'),list,17,'https://yt3.ggpht.com/-33p31sJqT88/AAAAAAAAAAI/AAAAAAAAAAA/taeHwLul6Io/s100-c-k-no/photo.jpg',addonString(101410).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שלום חנוך'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10142).encode('utf-8'),list,17,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(101420).encode('utf-8'),'1',"", getAddonFanart(background))

	'''שלומי שבת'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10143).encode('utf-8'),list,17,'https://i.ytimg.com/i/GaHPMv8YIv_0HfRDQQ44cA/mq1.jpg?v=af5444',addonString(101430).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שלמה ארצי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10144).encode('utf-8'),list,17,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(101440).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שרית חדד'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10145).encode('utf-8'),list,17,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(11450).encode('utf-8'),'1',"", getAddonFanart(background))

def CATEGORIES105(admin):
	'''------------------------------
	---Israeli-Djs-------------------
	------------------------------'''
	background = 105
	'''שרים קריוקי'''
	#addDir(addonString(302).encode('utf-8'),'sharimkaraokeltd',9,'https://yt3.ggpht.com/-rPZ4cqEBAPE/AAAAAAAAAAI/AAAAAAAAAAA/rUBUZCCaWpQ/s100-c-k-no/photo.jpg',addonString(352).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''בא לי קריוקי'''
	#addDir(addonString(303).encode('utf-8'),'plugin://plugin.video.youtube/user/balikaraoke40/',8,'https://yt3.ggpht.com/-rPZ4cqEBAPE/AAAAAAAAAAI/AAAAAAAAAAA/rUBUZCCaWpQ/s100-c-k-no/photo.jpg',addonString(353).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי ישראלי 1'''
	#addDir(addonString(102).encode('utf-8') + space + "1",'PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV',13,'special://skin/media/misc/help/hebflag.png',addonString(399).encode('utf-8'),'1',"", getAddonFanart(background))	

def CATEGORIES111(admin):
	'''------------------------------
	---Foreign-Music-----------------
	------------------------------'''
	background = 111
	commonsearch = "commonsearch111"
	
	'''חיפוש'''
	addDir(localize(137),commonsearch,3,htptservicemedia_path + "se.png",addonString_servicehtpt(23) % (commonsearch111),'1',"", getAddonFanart(background))
	
	'''הכל'''
	addDir(localize(593),'UC-9-kyTW8ZkZNDHQJ6FgpwQ',9,"http://markharai.com/wp-content/uploads/2010/11/megaphone.png.scaled980-300x300.png","",'1',"", getAddonFanart(background))
	
	'''Ariana Grande'''	
	if admin: addDir(addonString(11105).encode('utf-8'),'ArianaGrandeVevo',9,"https://yt3.ggpht.com/-u_W-R7bGk1c/AAAAAAAAAAI/AAAAAAAAAAA/u6lamzb3BPc/s100-c-k-no/photo.jpg",addonString(111050).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_ch=ArethaFranklinVEVO')
	list.append('&youtube_pl=-aVCoKV6XpVJ8U1wNNOkbo6BzgCdf83m')
	addDir(addonString(11126).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(111260).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Beyonce'''
	addDir(addonString(11102).encode('utf-8'),'beyonceVEVO',9,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(111020).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Bob Marley'''
	addDir(addonString(11122).encode('utf-8'),'plugin://plugin.video.youtube/channel/UCbvZKpr1g-6S0QuP4OmCabw/',8,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(111220).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Bob Dylan'''
	addDir(addonString(11123).encode('utf-8'),'plugin://plugin.video.youtube/channel/UCBqkojCXby4zGkWX86FEY7Q/',8,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(111230).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Bruno Marc'''
	if admin: addDir(addonString(11128).encode('utf-8'),'ElektraRecords',9,"https://yt3.ggpht.com/-Ymp7v1ycCBA/AAAAAAAAAAI/AAAAAAAAAAA/-R7WfWSAkag/s100-c-k-no/photo.jpg",addonString(111280).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Big Sean'''
	if admin: addDir(addonString(11148).encode('utf-8'),'BigSeanVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/BigSean2009.jpg/220px-BigSean2009.jpg",addonString(111480).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Britney Spears'''
	addDir(addonString(11150).encode('utf-8'),'BritneySpearsVEVO',9,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(111500).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Celine Dion'''
	
	'''Coldplay'''
	addDir(addonString(11129).encode('utf-8'),'ColdplayVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Coldplay-3.jpg/429px-Coldplay-3.jpg",addonString(111290).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Chris" Brown'''
	addDir(addonString(11116).encode('utf-8'),'ChrisBrownVEVO',9,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2015/09/chris_brown270915.jpg",addonString(111160).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''David Bowie'''
	list = []
	list.append('&youtube_ch=DavidBowieVEVO')
	list.append('&youtube_pl=PLD23E32ADB777242D')
	addDir(addonString(11151).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(111510).encode('utf-8'),'1',"", getAddonFanart(background,'https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg'))
	
	'''david guetta'''
	if admin: addDir(addonString(11146).encode('utf-8'),'davidguettavevo',9,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(111460).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Demi Lovato'''
	if admin: addDir(addonString(11136).encode('utf-8'),'DemiLovatoVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Demi_Lovato_2%2C_2013.jpg/375px-Demi_Lovato_2%2C_2013.jpg",addonString(111360).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Daft Punk'''
	if admin: addDir(addonString(11141).encode('utf-8'),'DaftPunkVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Daftpunklapremiere2010.jpg/375px-Daftpunklapremiere2010.jpg",addonString(111410).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Drake'''
	if admin: addDir(addonString(11139).encode('utf-8'),'DrakeVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Drake_at_Bun-B_Concert_2011.jpg/375px-Drake_at_Bun-B_Concert_2011.jpg",addonString(111390).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Enrique Iglesias'''
	if admin: addDir(addonString(11109).encode('utf-8'),'EnriqueIglesiasVEVO',9,"https://yt3.ggpht.com/-qsK10MKa204/AAAAAAAAAAI/AAAAAAAAAAA/pWY83V_O3Rg/s100-c-k-no/photo.jpg",addonString(111090).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Elvis Presley'''
	addDir(addonString(11120).encode('utf-8'),'ElvisPresleyVEVO',9,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(111200).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Eric Clapton'''
	addDir(addonString(11124).encode('utf-8'),'plugin://plugin.video.youtube/channel/UCXmEE051j5RhUENn7saUF3g/',8,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(111240).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Ellie Goulding'''
	if admin: addDir(addonString(11134).encode('utf-8'),'EllieGouldingVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Ellie_Goulding_March_18%2C_2014_%28cropped%29.jpg/375px-Ellie_Goulding_March_18%2C_2014_%28cropped%29.jpg",addonString(111340).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Eminem'''
	if admin: addDir(addonString(11138).encode('utf-8'),'EminemVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Eminem_performing_live_at_dj_hero_party.jpg/375px-Eminem_performing_live_at_dj_hero_party.jpg",addonString(111380).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Ed Sheeran'''
	if admin: addDir(addonString(11144).encode('utf-8'),'EdSheeran',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Ed_Sheeran_2013.jpg/375px-Ed_Sheeran_2013.jpg",addonString(111440).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Fetty Wap'''
	if admin: addDir(addonString(11149).encode('utf-8'),'harlemfetty',9,"https://yt3.ggpht.com/-z9iYN3U1TOk/AAAAAAAAAAI/AAAAAAAAAAA/IpV26AosUEw/s100-c-k-no/photo.jpg",addonString(111490).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''flo'''
	if admin: addDir(addonString(11127).encode('utf-8'),'officialflo',9,"https://yt3.ggpht.com/-03upv5VWDpQ/AAAAAAAAAAI/AAAAAAAAAAA/ufkXZipfRQ0/s100-c-k-no/photo.jpg",addonString(111270).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Jennifer Lopez'''
	addDir(addonString(11118).encode('utf-8'),'JenniferLopezVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(111180).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Justin Bieber'''
	if admin: addDir(addonString(11130).encode('utf-8'),'JustinBieberVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Believe_Tour_7%2C_2012.jpg/375px-Believe_Tour_7%2C_2012.jpg",addonString(111300).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Jason Derulo'''
	if admin: addDir(addonString(11145).encode('utf-8'),'JasonDerulo',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Jason-Derulo_by-Adam-Bielawski_2010-01-12.jpg/375px-Jason-Derulo_by-Adam-Bielawski_2010-01-12.jpg",addonString(111450).encode('utf-8'),'1',"", getAddonFanart(background))
 
	'''Hardwell'''
	if admin: addDir(addonString(11147).encode('utf-8'),'robberthardwell',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Hardwell.jpg/375px-Hardwell.jpg",addonString(111470).encode('utf-8'),'1',"", getAddonFanart(background))

	'''Kanye West'''
	if admin: addDir(addonString(11140).encode('utf-8'),'KanyeWestVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Kanye_West_SWU_Music_%26_Arts_Festival_2011_%28crop%29.jpg/375px-Kanye_West_SWU_Music_%26_Arts_Festival_2011_%28crop%29.jpg",addonString(111400).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Katy Perry'''
	if admin: addDir(addonString(11106).encode('utf-8'),'KatyPerryVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Katy_Perry_NRJ_2014_3.jpg/375px-Katy_Perry_NRJ_2014_3.jpg",addonString(111060).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Michael Jackson'''
	addDir(addonString(11101).encode('utf-8'),'plugin://plugin.video.youtube/channel/UCulYu1HEIa7f70L2lYZWHOw/',8,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg/375px-Michael_Jackson_in_1988.jpg",addonString(111010).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Maddona'''
	addDir(addonString(11111).encode('utf-8'),'MADONNAVEVO',9,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(111110).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Mariah Carey'''
	addDir(addonString(11113).encode('utf-8'),'MariahCareyVEVO',9,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(111130).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Marc anthony'''
	if admin: addDir(addonString(11119).encode('utf-8'),'marcanthonyVEVO',9,"https://yt3.ggpht.com/-CJIy_bXsp8g/AAAAAAAAAAI/AAAAAAAAAAA/oNaF1LsUhq4/s100-c-k-no/photo.jpg",addonString(111190).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Maroon5'''
	if admin: addDir(addonString(11125).encode('utf-8'),'Maroon5VEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Maroon_5%2C_2011.jpg/390px-Maroon_5%2C_2011.jpg",addonString(111250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Mark Ronson'''
	if admin: addDir(addonString(11142).encode('utf-8'),'MarkRonsonVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Mark-Ronson.jpg/330px-Mark-Ronson.jpg",addonString(111420).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Meghan Trainor'''
	if admin: addDir(addonString(11143).encode('utf-8'),'MeghanTrainorVEVO',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Meghan_Trainor_2014.jpg/375px-Meghan_Trainor_2014.jpg",addonString(111430).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''One Direction'''
	if admin: addDir(addonString(11131).encode('utf-8'),'OneDirectionVEVO',9,"https://yt3.ggpht.com/-QRypZt--uYA/AAAAAAAAAAI/AAAAAAAAAAA/Y8-NLYzQzZc/s100-c-k-no/photo.jpg",addonString(111310).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''psy '''
	if admin: addDir(addonString(11121).encode('utf-8'),'officialpsy',9,"https://yt3.ggpht.com/-0Xgl841SU7Y/AAAAAAAAAAI/AAAAAAAAAAA/_bKTxRDm1kw/s100-c-k-no/photo.jpg",addonString(111210).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Pitbull'''
	if admin: addDir(addonString(11108).encode('utf-8'),'PitbullVEVO',9,"http://i.telegraph.co.uk/multimedia/archive/02446/bowie2_2446365b.jpg",addonString(111080).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Roy Orbison'''
	addDir(addonString(11110).encode('utf-8'),'http://www.songs-tube.net/12664-Roy%20Orbison.html',9,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(111100).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Rihanna'''
	addDir(addonString(11103).encode('utf-8'),'RihannaVEVO',9,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(111030).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Shakira '''
	if admin: addDir(addonString(11107).encode('utf-8'),'shakiraVEVO',9,"https://yt3.ggpht.com/-Kcd3KMxoqzw/AAAAAAAAAAI/AAAAAAAAAAA/EvhGpQ4rsh8/s100-c-k-no/photo.jpg",addonString(111070).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Sam Smith'''
	if admin: addDir(addonString(11133).encode('utf-8'),'SamSmithWorldVEVO',9,"https://yt3.ggpht.com/-9z_bFRPDMYQ/AAAAAAAAAAI/AAAAAAAAAAA/czjhAF4k4aw/s100-c-k-no/photo.jpg",addonString(111330).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Selena Gomez'''
	if admin: addDir(addonString(11135).encode('utf-8'),'SelenaGomezVEVO',9,"https://yt3.ggpht.com/-hI_B55kfWg4/AAAAAAAAAAI/AAAAAAAAAAA/YLLvtATyko8/s100-c-k-no/photo.jpg",addonString(111350).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Taylor Swift'''
	if admin: aaddDir(addonString(11104).encode('utf-8'),'TaylorSwiftVEVO',9,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(111040).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Usher'''
	addDir(addonString(11115).encode('utf-8'),'UsherVEVO',9,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(111150).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Trey Songz'''
	if admin: addDir(addonString(11117).encode('utf-8'),'TreySongzVideos',9,"http://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Trey_Songz_SummerJam.jpg/375px-Trey_Songz_SummerJam.jpg",addonString(111170).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Whitney Houston'''
	addDir(addonString(11114).encode('utf-8'),'whitneyhoustonVEVO',9,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(111140).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''‎5 Seconds of Summer'''
	if admin: addDir(addonString(11132).encode('utf-8'),'5sosvevo',9,"https://yt3.ggpht.com/-y-nmdZcJTz4/AAAAAAAAAAI/AAAAAAAAAAA/yAqkAfvvrkI/s100-c-k-no/photo.jpg",addonString(111320).encode('utf-8'),'1',"", getAddonFanart(background))


	

	
	#notification(addonID,"","",1000)
	
def CATEGORIES112(admin):
	'''------------------------------
	---Foreign-Karaoke---------------
	------------------------------'''
	background = 112
	'''מלך הקריוקי'''
	addDir(addonString(1201).encode('utf-8'),'singkingkaraoke',9,"https://yt3.ggpht.com/-RQAPMaxL1gE/AAAAAAAAAAI/AAAAAAAAAAA/zawPgoguLwI/s100-c-k-no/photo.jpg",addonString(1251).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''ערוץ הקריוקי'''
	addDir(addonString(1202).encode('utf-8'),'TheKARAOKEChannel',9,"https://yt3.ggpht.com/-8Ee1BcZtW7g/AAAAAAAAAAI/AAAAAAAAAAA/JqoBo946g0Q/s100-c-k-no/photo.jpg",addonString(1252).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''כיף לי קריוקי'''
	addDir(addonString(1203).encode('utf-8'),'karafun',9,"https://i.ytimg.com/i/bqcG1rdt9LMwOJN4PyGTKg/mq1.jpg?v=510a8aea",addonString(1253).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''שיר שיר קריוקי'''
	addDir(addonString(1204).encode('utf-8'),'singsongsmusic',9,"https://yt3.ggpht.com/-iu_A8aYydvs/AAAAAAAAAAI/AAAAAAAAAAA/kXj4XMpmVnI/s100-c-k-no/photo.jpg",addonString(1254).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''VEVO קריוקי'''
	addDir(addonString(1205).encode('utf-8'),'KaraokeOnVEVO',9,"https://yt3.ggpht.com/-CyAdZgF4lts/AAAAAAAAAAI/AAAAAAAAAAA/c181cY8p6Lc/s100-c-k-no/photo.jpg",addonString(1255).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''Matt Monro Karaoke'''
	addDir(addonString(1206).encode('utf-8'),'PLLDeS1DKrNwyPjDuzHsoJiw4-rWn97Umq',13,"http://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Matt_Monro.png/220px-Matt_Monro.png",addonString(1256).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 1'''
	addDir(addonString(112).encode('utf-8') + space + "1",'PL5MV8_qxHC5u8I2IrcHWQQ_yLGIcAlOy7',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 2'''
	addDir(addonString(112).encode('utf-8') + space + "2",'PL5MV8_qxHC5s4l6yy6FGD2VnK-zYdZm0J',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 3'''
	addDir(addonString(112).encode('utf-8') + space + "3",'PLB52171717111CFFA',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 4'''
	addDir(addonString(112).encode('utf-8') + space + "4",'PLsNRPB4qRXumn6Y7BkkN5pJqWNa3Gd7LX',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 5 (2015)'''
	addDir(addonString(112).encode('utf-8') + space + "5" + space + "(2015)",'PLjWNGcq3dvNYt9SyA9f3vxmdMe10xnSOL',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 6 (2014)'''
	addDir(addonString(112).encode('utf-8') + space + "6" + space + "(2014)",'PLjWNGcq3dvNY23wYDKeYIZqurM60izBqm',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי לועזי 7 (2013)'''
	addDir(addonString(112).encode('utf-8') + space + "7" + space + "(2013)",'PLjWNGcq3dvNYdBUwW0zrNAnyg0-TaYDV-',13,"special://skin/media/icons/karaoke.png",addonString(1250).encode('utf-8'),'1',"", getAddonFanart(background))
	

def CATEGORIES114(admin):
	'''------------------------------
	---Foreign-Liveshows-------------
	------------------------------'''
	background = 114
	'''שרים קריוקי'''
	#addDir(addonString(302).encode('utf-8'),'sharimkaraokeltd',9,'https://yt3.ggpht.com/-rPZ4cqEBAPE/AAAAAAAAAAI/AAAAAAAAAAA/rUBUZCCaWpQ/s100-c-k-no/photo.jpg',addonString(352).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''בא לי קריוקי'''
	#addDir(addonString(303).encode('utf-8'),'plugin://plugin.video.youtube/user/balikaraoke40/',8,'https://yt3.ggpht.com/-rPZ4cqEBAPE/AAAAAAAAAAI/AAAAAAAAAAA/rUBUZCCaWpQ/s100-c-k-no/photo.jpg',addonString(353).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי ישראלי 1'''
	#addDir(addonString(102).encode('utf-8') + space + "1",'PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV',13,'special://skin/media/misc/help/hebflag.png',addonString(399).encode('utf-8'),'1',"", getAddonFanart(background))
	
	
	
	
def CATEGORIES115(admin):
	'''------------------------------
	---Foregin-Djs-------------------
	------------------------------'''
	background = 115
	'''שרים קריוקי'''
	#addDir(addonString(302).encode('utf-8'),'sharimkaraokeltd',9,'https://yt3.ggpht.com/-rPZ4cqEBAPE/AAAAAAAAAAI/AAAAAAAAAAA/rUBUZCCaWpQ/s100-c-k-no/photo.jpg',addonString(352).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''בא לי קריוקי'''
	#addDir(addonString(303).encode('utf-8'),'plugin://plugin.video.youtube/user/balikaraoke40/',8,'https://yt3.ggpht.com/-rPZ4cqEBAPE/AAAAAAAAAAI/AAAAAAAAAAA/rUBUZCCaWpQ/s100-c-k-no/photo.jpg',addonString(353).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''קריוקי ישראלי 1'''
	background = 115
	#addDir(addonString(102).encode('utf-8') + space + "1",'PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV',13,'special://skin/media/misc/help/hebflag.png',addonString(399).encode('utf-8'),'1',"", getAddonFanart(background))
	
def CATEGORIES121(admin):
	'''------------------------------
	---Classical-Music---------------
	------------------------------'''
	background = 121
	'''מוזיקה קלאסית 1'''
	addDir(addonString(121).encode('utf-8') + space + "1",'ClassicalMusicOnly',9,'https://yt3.ggpht.com/-ECuTE_OO3EU/AAAAAAAAAAI/AAAAAAAAAAA/2j-Kiyky9JU/s100-c-k-no/photo.jpg',addonString(2050).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מוזיקה קלאסית 2'''
	addDir(addonString(121).encode('utf-8') + space + "2",'TopClassicalMusic',9,'https://yt3.ggpht.com/-RcrsdLR_BvI/AAAAAAAAAAI/AAAAAAAAAAA/2kIbfIgVXi4/s100-c-k-no/photo.jpg',addonString(2051).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מוזיקה קלאסית 3'''
	addDir(addonString(121).encode('utf-8') + space + "3",'ClassicalMusicOn',9,'https://yt3.ggpht.com/-LuYmD_n6gFo/AAAAAAAAAAI/AAAAAAAAAAA/nNUB6_ECXJc/s100-c-k-no/photo.jpg',addonString(2052).encode('utf-8'),'1',"", getAddonFanart(background))
	
	'''מוזיקה קלאסית 4'''
	addDir(addonString(121).encode('utf-8') + space + "4",'PLcGkkXtask_fpbK9YXSzlJC4f0nGms1mI',13,'https://yt3.ggpht.com/-LFti8mQBHdE/AAAAAAAAAAI/AAAAAAAAAAA/F8sYy19ISBc/s88-c-k-no/photo.jpg',addonString(2053).encode('utf-8'),'1',"", getAddonFanart(background))
	

	
