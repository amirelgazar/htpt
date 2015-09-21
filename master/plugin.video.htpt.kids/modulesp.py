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
	addDir(addonString(41).encode('utf-8'),'',101,addonMediaPath + "41.png",addonString(141).encode('utf-8'),'1',58)
	addDir(addonString(42).encode('utf-8'),'',102,addonMediaPath + "42.jpg",addonString(142).encode('utf-8'),'1',58) #SHOWS
	addDir(addonString(44).encode('utf-8'),'',104,addonMediaPath + "44.png",addonString(144).encode('utf-8'),'1',58)
	addDir(addonString(45).encode('utf-8'),'',105,addonMediaPath + "45.jpg",addonString(145).encode('utf-8'),'1',50)
	addDir(addonString(46).encode('utf-8'),'',106,addonMediaPath + "46.png",addonString(146).encode('utf-8'),'1',58)
	addDir(addonString(47).encode('utf-8'),'',107,addonMediaPath + "47.jpg",addonString(147).encode('utf-8'),'1',58)
	addDir(addonString(48).encode('utf-8'),'',108,addonMediaPath + "48.jpg",addonString(148).encode('utf-8'),'1',50)
	addDir(addonString(49).encode('utf-8'),'',109,addonMediaPath + "49.jpg",addonString(149).encode('utf-8'),'1',50)
	if General_TrustedOnly == "false": addDir(addonString(43).encode('utf-8'),'',111,addonMediaPath + "42.jpg",addonString(143).encode('utf-8'),'1',"")
	
	
	
	
	'''many sources'''
	#YOUsubs('UC5RJ8so5jivihrnHB5qrV_Q')
	'''------------------------------
	---וואלה-VOD!--------------------
	------------------------------'''
	
	
	#if OFF_9 != "true": addDir(addonString(22).encode('utf-8'),'plugin://plugin.video.wallaNew.video/?mode=1&module=wallavod&name=%d7%99%d7%9c%d7%93%d7%99%d7%9d&url=englishName%3dkids',8,'https://lh6.ggpht.com/V8v_FzkTMqeLRg_oY7G00zf0bcxubsm659cLrbf9nEKMLHQG-5LSZdbbJGQgkV6j1PQ=w300',addonString(110).encode('utf-8'),'1',"")
	#if OFF_9 != "true": addDir('קלסיקלטת','plugin://plugin.video.wallaNew.video/?mode=1&module=338&name=קלסיקלטת&url=http://vod.walla.co.il/channel/338/clasicaletet',8,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTYE2VT8CR2O31MsqAhdaydYrqrCD--HCCdGcs7blBn3Zh92Kwq','','1',"")
	#if OFF_10 != "true": addDir('ניק','plugin://plugin.video.wallaNew.video/?mode=1&module=nick&name=ניק&url=http://nick.walla.co.il/',8,'http://www.karmieli.co.il/sites/default/files/images/nico.jpg','','1',"")
	#if OFF_11 != "true": addDir('גוניור','plugin://plugin.video.wallaNew.video/?mode=1&module=junior&name=גוניור&url=http://junior.walla.co.il/',8,'http://upload.wikimedia.org/wikipedia/he/1/19/%D7%A2%D7%A8%D7%95%D7%A5_%D7%92%27%D7%95%D7%A0%D7%99%D7%95%D7%A8.jpg','','1',"")
	#if OFF_13 != "true": addDir('וואלה ילדים','plugin://plugin.video.wallaNew.video/?mode=1&module=wallavod&name=י%d7%99%d7%9c%d7%93%d7%99%d7%9d&url=englishName%3dkids',8,'https://lh6.ggpht.com/V8v_FzkTMqeLRg_oY7G00zf0bcxubsm659cLrbf9nEKMLHQG-5LSZdbbJGQgkV6j1PQ=w300','','1',"")
	'''---------------------------'''
	

'''1=SONGS, 2=SHOWS, 3=LITTLE, 4=TVSHOWS, 5=MOVIES, 6=?, 7=BABY, 8=?, 9=OTHERS'''
def CATEGORIES101(admin):
	
	'''אוסף שירים בעברית'''
	addDir('אוסף שירים בעברית',['&youtube_pl=PLFw7KwIWHNB1_mXvYXwqFOw6S026LL3tj', '&youtube_ch=UCfm5IpcgGCooON4Mm2vq40A/playlists', '&youtube_ch=23music', '&youtube_pl=PLF11AD94724D37E02', '&wallaNew=genre%3dkids%26genreId%3d7450', '&wallaNew=item_id%3D2538763', '&wallaNew=item_id%3D2538765', '&wallaNew=item_id%3D2538766', '&wallaNew=item_id%3D2538767', '&wallaNew=item_id%3D2538768', '&youtube_pl=PL0495C8F5A2024FA4', '&wallaNew=', '&wallaNew=', '&wallaNew=', '&wallaNew=', '&wallaNew=', '&wallaNew='],17,'http://www.diskids.co.il/images/stories/feature/1.png',addonString(110).encode('utf-8'),'1',50)
	
	'''השירים הראשונים שלי'''
	addDir('השירים הראשונים שלי',['&youtube_id=6LNpGsYpWJw', '&youtube_id=YtuVAZyWoG4', '&youtube_pl=PLpnRNlRK18UaUnOabh_ZysDsOY3QLvjkd', '&youtube_pl=PLdhkcuUltKcfTUBHVy02eKfRIEnmg7fnn'],17,'http://ypk.cs4u.co.il/mall_product_images/auction_product/ZF21388.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''שירי עוזי חיטמן'''
	addDir('שירי עוזי חיטמן',['&wallaNew=item_id%3D2538763', '&youtube_pl=21zlKTnPBcU&list=RD21zlKTnPBcU', '&youtube_pl=PL0145D27A0D5E1810', '&youtube_id=YMLsE_DMPGQ', '&youtube_id=21zlKTnPBcU'],17,'http://www.lifemusic.co.il/files/singers/big/1248883756s56Ly.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''שירי לילה טוב'''
	addDir('שירי לילה טוב',['&youtube_pl=PLErYJg2XgxyVYzsbPxH2dzhlWLs9sWGTa', '&youtube_pl=PLErYJg2XgxyXTMAJvmFXoW6Qe66Ztw0Fk'],17,'http://erezdvd.co.il/sites/default/files/imagecache/product_full/products/numi-numi.jpg',addonString(128).encode('utf-8'),'1',"")
	
	'''שירי פרפר נחמד'''
	addDir('שירי פרפר נחמד',['&youtube_pl=PL51YAgTlfPj45OPEXI-ibfJy8ON0k1ARh', '&youtube_pl=PLNWPkdPqwKqtbM6--m50SdENigIXvoAqm'],17,'http://www.sdarot.wf/media/series/1092.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''שירי דיסני'''
	addDir('שירי דיסני','plugin://plugin.video.youtube/channel/UC6QxAhInaZ79pTg7wi3ZF-Q/',8,'http://i.ytimg.com/i/6QxAhInaZ79pTg7wi3ZF-Q/1.jpg?v=78ea3c',addonString(138).encode('utf-8'),'1',"")
	
	'''שירי מיכל כלפון'''
	addDir('שירי מיכל כלפון',['&youtube_pl=PL9boemkB6hYz5WlmI-QH_xmRyZDpHKvt9'],17,'http://yt3.ggpht.com/-4Rd1GQEZnaM/AAAAAAAAAAI/AAAAAAAAAAA/pfQtiUaNjng/s88-c-k-no/photo.jpg',addonString(107750).encode('utf-8'),'1',50)
	
	'''שירי ענבלי בא לי'''
	addDir('שירי ענבלי בא לי','PLPWc8VdaIIsAHPacvuyNfA-y8VSxoh4or',13,'http://www.tel-aviv.gov.il/ToEnjoy/CulterAndArts/DocLib4/inbali.jpg.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''שירים וסיפורים באנגלית'''
	addDir('שירים באנגלית',['&youtube_ch=UC-qWJlvaPME3MWvrY-yjXeA', '&youtube_ch=UCLsooMJoIpl_7ux2jvdPB-Q', '&youtube_ch=UCtgpDqkeOToveUgh8igrvXQ', '&youtube_ch=UC3djj8jS0370cu_ghKs_Ong', '&youtube_ch=UCBnZ16ahKA2DZ_T5W0FPUXg'],6,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSP5wUCoBJU4xmqJym822S6aRCKUWJzImIbcymG_WAq5ujJOtdCpw',addonString(110).encode('utf-8'),'1',50)
	
	'''אוסף סיפורים בעברית'''
	addDir(addonString(10160).encode('utf-8'),['&youtbe_pl=PL74E72320D1F7932C', '&youtube_pl=PL6jaO-hu0Ivzi0gndI5Rb6YYcqut13wlD', '&youtube_id=qSOsMgZ1iwk', '&wallaNew=seasonId%3d2867134', '&youtube_id=tl64w59Hh8E', '&wallaNew=item_id%3D2833303', '&wallaNew=item_id%3D2833303', '&wallaNew=seasonId%3d2585073', '&wallaNew=seasonId%3d2535850', '&wallaNew=seasonId%seasonId%3d2554281', '&wallaNew=item_id%3D2526364', '&youtube_id=NPqxLDRQF3M', '&youtube_id=CvlF7okXM2g', '&youtube_id=uGXiT9zyYa0', '&youtube_id=HAXPFap0P0A', '&youtube_id=RCFSjBSXKHk', '&youtube_id=QCFEPr9LLA0', '&youtube_id=8-t8ujUVVIQ', '&wallaNew=seasonId%3d2867134'],17,'http://www.gidikoren.com/gidikoren/images/book_pitz_azar.jpg',addonString(101600).encode('utf-8'),'1',"")
	
	'''סיפורי סבא טוביה'''
	addDir('סיפורי סבא טוביה',['&youtube_pl=PL6jaO-hu0IvwHsU9bzS8caFo8reAxEseX', '&youtube_pl=kbs02_gshRs'],17,'http://images.mouse.co.il/storage/2/e/b-saba.jpg',addonString(110).encode('utf-8'),'1',"")

	'''סיפורים בעברית 2'''
	addDir(addonString(58).encode('utf-8') + space + addonString(200).encode('utf-8') + space + "2",'plugin://plugin.video.wallaNew.video/?mode=2&module=wallavod&name=%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%d7%9d%20(5)&url=genre%3dkids%26genreId%3d7451',8,'https://lh6.ggpht.com/V8v_FzkTMqeLRg_oY7G00zf0bcxubsm659cLrbf9nEKMLHQG-5LSZdbbJGQgkV6j1PQ=w300',addonString(198).encode('utf-8'),'1',"")

def CATEGORIES10103(name, iconimage, desc):
	YOULink('שמוליק קיפוד, הצב של אורן, והלו הלו אבא', 'qSOsMgZ1iwk', 'http://best-store.co.il/images/prudact/Shmulik.Kipod_Main.Image.jpg',addonString(110).encode('utf-8'))
	
def CATEGORIES102(admin):
	
	'''עוד...'''
	list = []
	list.append('&youtube_id=0FaBsetswDA')
	list.append('&youtube_id=PUL2C9mEAKQ')
	list.append('&youtube_id=o20-0VygrsE')
	list.append('&youtube_id=-ihwgBW3sVs')
	list.append('&youtube_id=_ixMuVcAGhA')
	list.append('&youtube_id=YOs5zhvXUf8')
	list.append('&youtube_id=kbzPyZV3cck')
	list.append('&youtube_id=i5yQxLraENk')
	list.append('&youtube_id=yfEzE5V409k')
	list.append('&wallaNew=item_id%3D2833366')
	list.append('&wallaNew=item_id%3D2817611')
	addDir(localize(22082),list,17,addonMediaPath + 'buttonadd.png',addonString(102000).encode('utf-8'),'1',50)
	
	'''101 כלבים דלמטים'''
	YOULink(addonString(10202).encode('utf-8'), '020c8c5ebfe70', 'http://www.pashbar.co.il/pictures/show_big_0712083001297352431.jpg',addonString(102020).encode('utf-8'))
	
	'''אי המטמון'''
	YOULink(addonString(10204).encode('utf-8'), 'Cmd0VxJmmBA', 'http://images.mouse.co.il/storage/0/e/ggg--Matmon.jpg',addonString(102040).encode('utf-8'))
	
	'''אלדין'''
	addDir(addonString(10205).encode('utf-8'),['&youtube_id=sVCYRfk3Wcc', '&youtube_id=aIY0onCV9u0'],17,'http://www.tipa.co.il/images/contentImages/images/TV/al.jpg',addonString(102050).encode('utf-8'),'1',50)
	
	'''בילבי'''
	YOULink(addonString(10207).encode('utf-8'), 'sHMEnVpDJR8', 'http://i.ytimg.com/vi/2mxOiPccxOs/maxresdefault.jpg',addonString(102070).encode('utf-8'))
	
	'''גאליס המופע'''
	YOULink(addonString(10209).encode('utf-8'), 'a6f7eacf00f28', 'http://up389.siz.co.il/up1/znmi3xqzndjg.jpg',addonString(102090).encode('utf-8'))
	
	'''גיבורי האור'''
	YOULink(addonString(10211).encode('utf-8'), 'nwlo00FHCRc', 'http://www.booknet.co.il/imgs/site/prod/7294276219850b.jpg',addonString(102110).encode('utf-8'))
	
	'''גיגיגיגונת קלטת ילדים'''
	YOULink(addonString(10213).encode('utf-8'), 'tKDm79jqRcI', 'http://erezdvd.co.il/sites/default/files/imagecache/product_full/products/369504.jpg',addonString(102130).encode('utf-8'))
	
	'''דוד חיים'''
	addDir(addonString(10219).encode('utf-8'),['&youtube_id=ugmThlqdPJw', '&youtube_id=X3j6mQ9VgLI', '&youtube_id=T_a52ktWfLc', '&youtube_id=FruAxOYP0uw'],17,'http://www.nmcunited.co.il/Images/dynamic/movies/Dod-Haim2.jpg',addonString(102190).encode('utf-8'),'1',50)
	
	'''הרקולס - המחזמר המלא'''
	YOULink(addonString(10227).encode('utf-8'), 'UiqG4WAcvCM', 'http://moridim.me/images/large/191.jpg',addonString(102270).encode('utf-8'))
	
	'''יובל המבולבל'''
	addDir(addonString(10731).encode('utf-8'),['&youtube_id=6UrdISJBBC4', '&youtube_id=920d18542f05a', '&youtube_id=C2Rm4IuVWNQ', '&youtube_id=99c23afc06d1a', '&youtube_id=CZDniCIenbA', '&youtube_id=H9rwsZ1roRQ'],17,'http://yt3.ggpht.com/-FHcf2Rxu08A/AAAAAAAAAAI/AAAAAAAAAAA/dxzE2ng3uXI/s88-c-k-no/photo.jpg',addonString(107310).encode('utf-8'),'1',50)
	
	'''ילד פלא'''
	YOULink(addonString(10231).encode('utf-8'), 'e5c134277697c', 'http://tzavta.co.il/images/siteCont/Content_233.2463.jpg',addonString(102310).encode('utf-8'))
	
	'''יניב המגניב'''
	YOULink(addonString(10233).encode('utf-8'), 'f9s_aunAElY', 'http://img.mako.co.il/2013/07/22/kids_yaniv_hamagniv_.jpg',addonString(102330).encode('utf-8'))
	
	'''לירן הקוסם מהאגדות'''
	YOULink(addonString(10239).encode('utf-8'), 'kNS4xMdPIos', 'http://i.ytimg.com/vi/5gN4SMO8EfE/maxresdefault.jpg',addonString(102390).encode('utf-8'))
	
	'''מותק הילדות התחברו'''
	addDir(addonString(10243).encode('utf-8'),['&youtube_id=1wLhD4yqQxU', '&youtube_id=_Lv0UHXaY4I', '&youtube_id=j_BClvgFwMw', '&youtube_id=_WBgn4iw8gw'],17,'http://media.org.il/images/Baby.girls.tap.the.musical.IL.1999_Front.Cover.jpg',addonString(102430).encode('utf-8'),'1',50)

	'''מותק של פסטיבל'''
	addDir(addonString(10244).encode('utf-8'),['&youtube_pl=PLE915B350E437A7D8', '&youtube_pl=PL8C370A361DD07BDB', '&youtube_id=t2ksCC_RyLw', '&youtube_id=2KQBeOM'],17,'http://www.yap.co.il/prdPics/4991_desc3_5_1_1409123377.jpg',addonString(102440).encode('utf-8'),'1',50)
	
	'''מיכל הקטנה''' #UCPCJS9igpTu7COLmoDeMKXQ
	addDir(addonString(10245).encode('utf-8'),['&wallaNew=item_id%3D2567432', '&wallaNew=item_id%3D2698903', '&wallaNew=item_id%3D2583625', '&youtube_id=IEeuv8mtRLI'],17,'http://www.pashbar.co.il/pictures/show_big_0523173001376412565.jpg',addonString(102450).encode('utf-8'),'1',"")
	
	'''מרקו'''
	YOULink(addonString(10248).encode('utf-8'), 'XgnCNCt71d8', 'http://www.ykp.co.il/cd_halev.jpg',addonString(102480).encode('utf-8'))
	
	'''משחקי הפסטיגל'''
	YOULink(addonString(10250).encode('utf-8'), 'd2953353ab9e8', 'http://www.ligdol.co.il/Upload/pestigal2014_poster.jpg',addonString(102500).encode('utf-8'))
	
	'''סינדרלה - בר רפאלי'''
	YOULink(addonString(10255).encode('utf-8'), 'snr9wxyEzpA', 'http://afisha.israelinfo.ru/pictures/19949.jpg',addonString(102550).encode('utf-8'))
	
	'''ספר הגונגל'''
	YOULink(addonString(10258).encode('utf-8'), 'TlWVoNz_B3o', 'http://images.mouse.co.il/storage/3/7/ggg--book20090908_2343750_0..jpg',addonString(102580).encode('utf-8'))
	
	'''עמי ותמי'''
	YOULink(addonString(10261).encode('utf-8'), '8d6a2e7a3cd54', 'http://www.tivon.co.il/vault/Zoar/amitami-B.jpg',addonString(102610).encode('utf-8'))
	
	'''עליבאבא וארבעים השודדים'''
	YOULink(addonString(10262).encode('utf-8'), 'gxgvTe3kPGY', 'http://i.ytimg.com/vi/EMtHOrNBXKU/hqdefault.jpg',addonString(102620).encode('utf-8'))
	
	'''עליסה בארץ הפלאות'''
	YOULink(addonString(10263).encode('utf-8'), '4Zp-6Ts07Qw', 'http://images.mouse.co.il/storage/3/0/b--alice.jpg',addonString(102630).encode('utf-8'))	
	
	'''פיטר פן - הראל סקעת'''
	YOULink(addonString(10267).encode('utf-8'), 'gTuMB5sz8pY', 'http://i48.tinypic.com/f5ceuq.jpg',addonString(102670).encode('utf-8'))
	
	'''פסטיבל כיף לי'''
	addDir('פסטיבל כיף לי',['&youtube_id=lZgpGH9wTHY'],17,'http://3.bp.blogspot.com/-LIy_QkefJ-M/UuaoyVJu82I/AAAAAAAAAus/Dpd7rKKbUfM/s1600/KEF2014+POS+copy.jpg','','1',50)
	
	'''פסטיגל'''
	list = []
	list.append('&youtube_ch=UCKs_S8Uo5rLCNhlSanFpfFQ')
	list.append('&youtube_ch=UCTxlaUXzxohVekL_Zym-hsw')
	list.append('&youtube_ch=UC8z6QWcSpDfeHY0sni4IDwA')
	list.append('&youtube_pl=PLwimDnICcPKPL4MdOLIQrGDMTOAshuQ2l')
	addDir('פסטיגל',list,17,'http://yt3.ggpht.com/-2Nux9ubjSCA/AAAAAAAAAAI/AAAAAAAAAAA/P8I968rchgE/s88-c-k-no/photo.jpg',addonString(137).encode('utf-8'),'1',"")
	'''---------------------------'''
	
	'''צ'פצ'ולה' - מיכל כלפון'''
	addDir(addonString(10775).encode('utf-8'),['&wallaNew=item_id%3D2728550', '&youtube_id=EKlFN3awN_w', '&youtube_id=UC64wDQFgTq9RpI1P8_p-SxA'],17,'http://yt3.ggpht.com/-4Rd1GQEZnaM/AAAAAAAAAAI/AAAAAAAAAAA/pfQtiUaNjng/s88-c-k-no/photo.jpg',addonString(107750).encode('utf-8'),'1',50)
	
	'''רובין הוד'''
	YOULink(addonString(10272).encode('utf-8'), '6nZk0H89jDQ', 'http://erezdvd.co.il/sites/default/files/imagecache/product_full/products/14810.jpg',addonString(102720).encode('utf-8'))
	
	'''רינת גבאי'''
	YOULink(addonString(10274).encode('utf-8'), 'ykKWS-Udw2s', 'http://img.mako.co.il/2013/09/16/fantasy50X70-poster_SHOWS_g.jpg',addonString(102740).encode('utf-8'))
	
	'''שורום זורום'''
	YOULink(addonString(10284).encode('utf-8'), '9rGV96uhqPw', 'http://www.tipa.co.il/images/contentImages/images/dvd/shorom.jpg',addonString(102840).encode('utf-8'))
	
	'''שלגיה והצייד'''
	YOULink(addonString(10287).encode('utf-8'), '0rPEJ-kD1dc', 'http://www.dossinet.me/coverage_pics/1b5d66af0d230ff716d50f07fd6defc0.jpg',addonString(102870).encode('utf-8'))
	
	'''סבא טוביה'''
	addDir(addonString(19).encode('utf-8'),['&youtube_pl=PLE494A88ED3823578'],17,'http://yt3.ggpht.com/--gG5kz68N_k/AAAAAAAAAAI/AAAAAAAAAAA/37Cr6jMJSCg/s88-c-k-no/photo.jpg',addonString(119).encode('utf-8'),'1',"")
	'''---------------------------'''
	
def CATEGORIES104(admin):
	'''עוד...'''
	list = []
	list.append('&sdarot=plugin://plugin.video.sdarot.tv/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f7%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&url=all-heb')
	list.append('&youtube_ch=UCDfoEu-jaKsjNL6Fl0h5PUQ')
	list.append('&wallaNew=genre%3dkids%26genreId%3d7447')
	if General_TrustedOnly == "false" or admin: list.append('&youtube_ch=UC9DU2y9iXnrI0Y5NFoBQ4RQ/playlists')
	addDir(localize(22082),list,6,addonMediaPath + 'buttonadd.png',addonString(110).encode('utf-8'),'1',50) ; list = []
	'''---------------------------'''
	
	'''אגדות המלך שלמה'''
	addDir('אגדות המלך שלמה',['&sdarot=series_id=815&series_name=%d7%90%d7%92%d7%93%d7%95%d7%aa%20%d7%94%d7%9e%d7%9c%d7%9a%20%d7%a9%d7%9c%d7%9e%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f815%2ftales-of-a-wise-king-hebdub-%d7%90%d7%92%d7%93%d7%95%d7%aa-%d7%94%d7%9e%d7%9c%d7%9a-%d7%a9%d7%9c%d7%9e%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=PLOx5NGhretuY8wp75WCY5PQQx8agiZ2IC'],17,'http://www.sdarot.pm/media/series/815.jpg',addonString(104000).encode('utf-8'),'1',50)
	
	'''אוטובוס הקסמים'''
	addDir('אוטובוס הקסמים',['&sdarot=season_id=1&series_id=1032&series_name=%d7%90%d7%95%d7%98%d7%95%d7%91%d7%95%d7%a1%20%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1032%2fthe-magic-school-bus-%d7%90%d7%95%d7%98%d7%95%d7%91%d7%95%d7%a1-%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94', '&youtube_pl=PLojgGSYuCHTB2q0TvkcGuhKteg3hNsZle'],17,'http://www.sdarot.pm/media/series/1032.jpg','גברת פריזל היא מורה ייחודית שמעבירה את שיעוריה באמצעות טיולי שדה קסומים.','1',50)
	
	'''אנימניאקס'''
	addDir('אנימניאקס',['&sdarot=series_id=1104&summary&series_name=%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1104%2fanimaniacs-%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94'],6,'http://www.sdarot.pm/media/series/1104.jpg','סדרת אנימציה אנרכיסטית שמאגדת את כל היצורים המצויירים שעשו יותר מדי בעיות לחברת האחים וורנר, ועל כן לא זכו לתהילת עולם כמו באגס באני ודאפי דאק.[CR]במרכז שלושה כתמים שחורים בשם יאקו וואקו ואחותם דוט, ומצטרפים אליהם לפרקים גם פינקי התמים ו-Brain השואף לכבוש את העולם במזימות קונספירטיביות, שלוש יונים בשם בובי, פסטו וסקוויט, וסנאית מזדקנת בשם סלאפי, שזכתה לעדנה מסוימת בתקופת תור הזהב של וורנר ועכשיו מתייבשת בפנסיה.','1',50)
								 
	'''אקס מן'''
	addDir('אקס מן',['&sdarot=series_id=1434&series_name=%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1434%2fx-men-%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94', '&youtube_pl=PLN0EJVTzRDL9ObPf7m4GCN2BL6Ayreybh', '&youtube_pl=PL240D6E0D52552316', '&youtube_pl=PL8D5045D1EA3AA091', '&youtube_pl=PLE69A961D0351E331'],17,'http://www.sdarot.pm/media/series/1434.jpg','סדרה מצוירת על חבורת גיבורי על מוטנטיים נלחמים למען הצדק והאמונה של בני האדם.','1',50)
							  
	'''אקס-מן: הדור הבא'''
	addDir('אקס-מן: הדור הבא',['&sdarot=series_id=1435&series_name=%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f%3a%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1435%2fx-men-evolution-%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f-%d7%94%d7%93%d7%95%d7%a8-%d7%94%d7%91%d7%90-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94'],6,'http://www.sdarot.pm/media/series/1435.jpg','חברי האקס-מן מתפתחים וגדלים כעבור השנים, אבל עכשיו ישנם מוטנטים שרוצים להורגם.[CR]החברים זקוקים לעזרה וכך מצטרפים אליהם חברים חדשים לצוות כדי לנצח את הרעים.','1',50)
	
	'''ארתור'''
	addDir('ארתור',['&sdarot=series_id=461&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f461%2farthur-%d7%90%d7%a8%d7%aa%d7%95%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94', '&youtube_pl=PL17sRM9raf1Q-i_fTe45N0UBqNgdnZTD6', '&youtube_pl=PLN0EJVTzRDL96B86muPPFwgdymQjlwmLZ'],17,'http://www.sdarot.pm/media/series/461.jpg',addonString(104000).encode('utf-8'),'1',50)
	
	'''בילבי'''
	addDir('בילבי',['&sdarot=season_id=1&series_id=1159&series_name=%d7%91%d7%99%d7%9c%d7%91%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary=%d7%91%d7%99%d7%9c%d7%91%d7%99%20%d7%94%d7%99%d7%90%20%d7%99%d7%9c%d7%93%d7%94%20%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%aa%20%d7%91%d7%9e%d7%99%d7%a0%d7%94%20%d7%a9%d7%a2%d7%95%d7%a9%d7%94%20%d7%9b%d7%9c%20%d7%9e%d7%94%20%d7%a9%d7%91%d7%90%20%d7%9c%d7%94.%20%d7%94%d7%99%d7%90%20%d7%97%d7%96%d7%a7%d7%94%20%d7%95%d7%90%d7%9e%d7%99%d7%a6%d7%94%2c%20%d7%97%d7%9b%d7%9e%d7%94%20%d7%9e%d7%9b%d7%95%d7%9c%d7%9d%2c%20%d7%a9%d7%95%d7%91%d7%91%d7%94%20%d7%95%d7%91%d7%9c%d7%92%d7%a0%d7%99%d7%a1%d7%98%d7%99%d7%aa%20%d7%9c%d7%90%20%d7%a7%d7%98%d7%a0%d7%94.%20%d7%94%d7%99%d7%90%20%d7%97%d7%99%d7%94%20%d7%91%d7%95%d7%99%d7%9c%d7%94%20%d7%a2%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%94%3a%20%d7%94%d7%90%d7%97%d7%99%d7%9d%20%d7%98%d7%95%d7%9e%d7%99%20%d7%95%d7%90%d7%a0%d7%99%d7%a7%d7%94%2c%20%d7%94%d7%a7%d7%95%d7%a3%20%22%d7%9e%d7%a8%20%d7%a0%d7%9c%d7%a1%d7%95%d7%9f%22%20%d7%95%d7%94%d7%a1%d7%95%d7%a1%20%d7%a9%d7%9c%d7%94.%20%d7%94%d7%97%d7%91%d7%95%d7%a8%d7%94%20%d7%97%d7%95%d7%95%d7%94%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%a8%d7%91%d7%95%d7%aa%20%d7%95%d7%9c%d7%a4%d7%a2%d7%9e%d7%99%d7%9d%20%d7%92%d7%9d%20%d7%9e%d7%a1%d7%aa%d7%91%d7%9b%d7%aa%20%d7%91%d7%a6%d7%a8%d7%95%d7%aa%3b%20%d7%90%d7%91%d7%9c%2c%20%d7%9c%d7%90%20%d7%9c%d7%93%d7%90%d7%95%d7%92%20%d7%91%d7%99%d7%9c%d7%91%d7%99%20%d7%aa%d7%9e%d7%99%d7%93%20%d7%9e%d7%a6%d7%9c%d7%99%d7%97%d7%94%20%d7%9c%d7%94%d7%aa%d7%92%d7%91%d7%a8%20%d7%a2%d7%9c%20%d7%9b%d7%9c%20%d7%94%d7%a7%d7%a9%d7%99%d7%99%d7%9d%20%d7%94%d7%a2%d7%95%d7%9e%d7%93%d7%99%d7%9d%20%d7%91%d7%93%d7%a8%d7%9a%20%d7%91%d7%96%d7%9b%d7%95%d7%aa%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%d7%99%d7%94%20%d7%94%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%99%d7%9d%2c%20%d7%94%d7%90%d7%a0%d7%a8%d7%92%d7%99%d7%94%20%d7%95%d7%94%d7%93%d7%9e%d7%99%d7%95%d7%9f%20%d7%94%d7%9e%d7%a4%d7%95%d7%aa%d7%97%20%d7%a9%d7%9c%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1159%2fpippi-longstocking-%d7%91%d7%99%d7%9c%d7%91%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94', '&youtube_id=CBWXP_5gxSw', '&youtube_id=kgLCdl2q8XQ', '&youtube_id=5tc2MzqqHH8', '&youtube_id=L878q4J48L8'],17,'http://www.sdarot.pm/media/series/1159.jpg',addonString(104100),'1',50)
	
	'''דורימון'''
	addDir("דורימון",['&youtube_pl=PL95CWWe9DuaJ6xtv1V8ZxDvoG_cB3z4bc'],17,'http://www.animation-animagic.com/img/conteudo/2632008151425.jpg',addonString(110).encode('utf-8'),'1',"")
	
	'''דיגימון'''
	addDir("דיגימון",['&youtube_pl=PLk98jt4ayAVJr26ugq6oAD6j0QjfVxSGD'],17,'http://forumsgallery.tapuz.co.il/ForumsGallery/galleryimages/medium/453gallery_13767.gif',addonString(110).encode('utf-8'),'1',"")
	
	'''דני שובבני'''
	addDir("דני שובבני",['&sdaort=season_id=1&series_id=448&series_name=%d7%93%d7%a0%d7%99%20%d7%a9%d7%95%d7%91%d7%91%d7%a0%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%93%d7%a0%d7%99%20%d7%a9%d7%95%d7%91%d7%91%d7%a0%d7%99%20%d7%94%d7%95%d7%90%20%d7%99%d7%9c%d7%93%20%d7%a9%d7%9c%d7%90%20%d7%9e%d7%a4%d7%a1%d7%99%d7%a7%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%a9%d7%98%d7%95%d7%99%d7%95%d7%aa%2c%20%d7%9c%d7%94%d7%a6%d7%99%d7%a7%20%d7%9c%d7%a9%d7%9b%d7%a0%d7%99%d7%9d%2c%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%a0%d7%96%d7%a7%d7%99%d7%9d%20%d7%95%d7%91%d7%a7%d7%99%d7%a6%d7%95%d7%a8%20%d7%9c%d7%94%d7%99%d7%95%d7%aa%20%d7%9b%d7%9e%d7%95%20%d7%9b%d7%9c%20%d7%99%d7%9c%d7%93%20%d7%91%d7%9f%20%d7%92%d7%99%d7%9c%d7%95.%20%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%9b%d7%9c%d7%91%d7%95%20%d7%94%d7%9e%d7%95%d7%a4%d7%a8%d7%a2%20%d7%91%d7%a9%d7%9d%20%d7%a8%d7%90%d7%a3%2c%20%d7%93%d7%a0%d7%99%20%d7%9e%d7%97%d7%95%d7%9c%d7%9c%20%d7%9e%d7%94%d7%95%d7%9e%d7%95%d7%aa%20%d7%91%d7%a9%d7%9b%d7%95%d7%a0%d7%94%2c%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%9b%d7%95%d7%95%d7%a0%d7%95%d7%aa%d7%99%d7%95%20%d7%94%d7%98%d7%95%d7%91%d7%95%d7%aa%2c%20%d7%94%d7%a8%d7%a6%d7%95%d7%9f%20%d7%94%d7%9e%d7%95%d7%98%d7%a2%d7%94%20%d7%9c%d7%a2%d7%96%d7%95%d7%a8%20%d7%95%d7%94%d7%a1%d7%a7%d7%a8%d7%a0%d7%95%d7%aa%20%d7%a9%d7%9c%d7%95%20%d7%a9%d7%90%d7%99%d7%a0%d7%94%20%d7%99%d7%95%d7%93%d7%a2%d7%aa%20%d7%a9%d7%95%d7%91%d7%a2%20%d7%9e%d7%95%d7%91%d7%99%d7%9c%d7%99%d7%9d%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9c%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%95%d7%9b%d7%99%d7%95%d7%a4%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f448%2fdennis-the-menace-%d7%93%d7%a0%d7%99-%d7%a9%d7%95%d7%91%d7%91%d7%a0%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=EvU1EzELJI8&list=PL68ECBFC6278EB7BE', '&youtube_id=zWwqxZPg8as', '&youtube_id=yLMFuFM5b7U', '&youtube_id=VYxab_Lh0gg', '&youtube_id=EjpsfP86Neo'],17,'http://www.sdarot.pm/media/series/448.jpg','דני שובבני הוא ילד שלא מפסיק לעשות שטויות, להציק לשכנים, לעשות נזקים ובקיצור להיות כמו כל ילד בן גילו. יחד עם כלבו המופרע בשם ראף, דני מחולל מהומות בשכונה, כאשר כוונותיו הטובות, הרצון המוטעה לעזור והסקרנות שלו שאינה יודעת שובע מובילים אותו להרפתקאות וכיופים.','1',"")
	
	'''דן דין השופט'''
	addDir('דין דין השופט',['&sdarot=season_id=1&series_id=1009&series_name=%d7%93%d7%9f%20%d7%93%d7%99%d7%9f%20%d7%94%d7%a9%d7%95%d7%a4%d7%98%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%93%d7%9f%20%d7%93%d7%99%d7%9f%20%d7%94%d7%95%d7%90%20%d7%a9%d7%95%d7%a4%d7%98%20%d7%97%d7%9b%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%a0%d7%a7%d7%a8%d7%90%20%d7%a2%22%d7%99%20%d7%94%d7%92%d7%9e%d7%93%d7%99%d7%9d%20%d7%91%d7%9b%d7%9c%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9c%d7%a4%d7%aa%d7%95%d7%a8%20%d7%90%d7%aa%20%d7%91%d7%a2%d7%99%d7%95%d7%aa%d7%99%d7%94%d7%9d.%20%d7%a0%d7%a2%d7%96%d7%a8%20%d7%91%d7%a2%d7%95%d7%96%d7%a8%d7%95%2c%20%d7%91%d7%99%d7%a0%d7%95%2c%20%d7%93%d7%9f%20%d7%93%d7%99%d7%9f%20%d7%a2%d7%a3%20%d7%9c%d7%9b%d7%9c%20%d7%9e%d7%a7%d7%95%d7%9d%20%d7%a2%d7%9c%20%d7%92%d7%91%d7%95%20%d7%a9%d7%9c%20%d7%98%d7%99%d7%9c%d7%99%20%d7%94%d7%91%d7%a8%d7%91%d7%95%d7%a8.%20%d7%94%d7%92%d7%9e%d7%93%d7%99%d7%9d%20%d7%a6%d7%a8%d7%99%d7%9b%d7%99%d7%9d%20%d7%9c%d7%94%d7%99%d7%96%d7%94%d7%a8%20%d7%9e%d7%94%d7%98%d7%a8%d7%95%d7%9c%d7%99%d7%9d%20%d7%94%d7%a8%d7%a2%d7%99%d7%9d%20%d7%a9%d7%9e%d7%aa%d7%a0%d7%9b%d7%9c%d7%99%d7%9d%20%d7%9c%d7%94%d7%9d%20%d7%91%d7%9b%d7%9c%20%d7%94%d7%96%d7%93%d7%9e%d7%a0%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1009%2fthe-wisdom-of-the-gnomes-%d7%93%d7%9f-%d7%93%d7%99%d7%9f-%d7%94%d7%a9%d7%95%d7%a4%d7%98-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=PL17sRM9raf1Q-i_fTe45N0UBqNgdnZTD6'],17,'http://www.sdarot.pm/media/series/1009.jpg',addonString(104000).encode('utf-8'),'1',50)
	
	'''הדבורה מאיה'''
	addDir('הדבורה מאיה',['&sdarot=season_id=1&series_id=668&series_name=%d7%94%d7%93%d7%91%d7%95%d7%a8%d7%94%20%d7%9e%d7%90%d7%99%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%9e%d7%90%d7%99%d7%94%20%d7%94%d7%99%d7%90%20%d7%93%d7%91%d7%95%d7%a8%d7%94%20%d7%9e%d7%a8%d7%93%d7%a0%d7%99%d7%aa%2c%20%d7%a1%d7%a7%d7%a8%d7%a0%d7%99%d7%aa%20%d7%95%d7%a9%d7%95%d7%91%d7%91%d7%94.%20%d7%94%d7%99%d7%90%20%d7%a2%d7%95%d7%96%d7%91%d7%aa%20%d7%90%d7%aa%20%d7%94%d7%9b%d7%95%d7%95%d7%a8%d7%aa%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%a6%d7%90%d7%aa%20%d7%9c%d7%98%d7%99%d7%95%d7%9c%20%d7%91%d7%a2%d7%95%d7%9c%d7%9d%20%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%94%d7%93%d7%91%d7%95%d7%a8%d7%95%d7%9f%20%d7%95%d7%95%d7%99%d7%9c%d7%99.%20%d7%94%d7%a9%d7%a0%d7%99%d7%99%d7%9d%20%d7%a2%d7%95%d7%91%d7%a8%d7%99%d7%9d%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%a7%d7%a1%d7%95%d7%9e%d7%95%d7%aa%20%d7%95%d7%a4%d7%95%d7%92%d7%a9%d7%99%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%91%d7%93%d7%a8%d7%9a%20%d7%97%d7%93%d7%a9%d7%99%d7%9d.%20%d7%9e%d7%90%d7%99%d7%94%20%d7%97%d7%95%d7%96%d7%a8%d7%aa%20%d7%9c%d7%9b%d7%95%d7%95%d7%a8%d7%aa%20%d7%97%d7%96%d7%a7%d7%94%20%d7%95%d7%97%d7%9b%d7%9e%d7%94%20%d7%94%d7%a8%d7%91%d7%94%20%d7%99%d7%95%d7%aa%d7%a8.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f668%2fmaya-the-bee-%d7%94%d7%93%d7%91%d7%95%d7%a8%d7%94-%d7%9e%d7%90%d7%99%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=PLfcYs4SRZfuKJs0CL98BF0_OOGRWlmpdQ'],17,'http://tochka.bg/uploads/ckfinder/images/maya_the_bee.png',addonString(100).encode('utf-8'),'1',50)
	
	'''הדרדסים'''
	addDir('הדרדסים',['&youtube_pl=PL66F75CE8DFB7A2A2', '&youtube_pl=PLo3vmw8N0knb9tZuIy7AR9fMPTUzr1oiI', '&sdarot=series_id=236&series_name=%d7%94%d7%93%d7%a8%d7%93%d7%a1%d7%99%d7%9d%20-%20%d7%9e%d7%93%d7%95%d7%91%d7%91&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f236%2fthe-smurfs-%d7%94%d7%93%d7%a8%d7%93%d7%a1%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&hotVOD=http%3a%2f%2fhot.ynet.co.il%2fExt%2fComp%2fHot%2fTopSeriesPlayer_Hot%2fCdaTopSeriesPlayer_VidItems_Hot%2f0%2c13031%2cL-10842-525-0-0%2c00.html', '&hotVOD=http%3A%2F%2Fhot.ynet.co.il%2FCmn%2FApp%2FVideo%2FCmmAppVideoApi_AjaxItems%2F0%2C13776%2C48507-0%2C00.html'],17,'http://f.nanafiles.co.il/upload/Xternal/IsraBlog/73/34/75/753473/misc/23130510.jpg',addonString(104000).encode('utf-8'),'1',50)
	
	'''הזרבובים'''
	addDir("הזרבובים",['&youtube_pl=PLR7DTcU2p0QiY-wI8KC6f01uzKLDZcuAc', '&sdarot=season_id=1&series_id=1313&series_name=%d7%94%d7%96%d7%a8%d7%91%d7%95%d7%91%d7%99%d7%9d&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1313%2fthe-snorks-%d7%94%d7%96%d7%a8%d7%91%d7%95%d7%91%d7%99%d7%9d'],17,'http://www.sdarot.pm/media/series/1313.jpg','הזרבובים הם יצורים תת מימיים, עליזים, ססגוניים, שמשתמשים בשנורקל שעל ראשם כדי לנוע במהירות במים וכדי לעשות מוסיקה.','1',50)
	
	'''החתולים הסמוראים'''
	addDir("החתולים הסמוראים",['&youtube_pl=PLR7DTcU2p0QhPmznEmitRHkv5RcUG3E-s'],17,'http://www.sdarot.pm/media/series/1147.jpg',"כשרובוט גרעיני עתיר ממדים קופץ לבקר בעירכם, למי תקראו? לחתולים הסמוראים!! פעולה, בידור והרבה אנשובי, הם המרכיבים העיקרים לרקיחת סדרת הרפתקאות מרגשות של חבורת החתולים הסמוראים, שוחרי הפיצה. כאשר הם אינם עסוקים בהצלת העולם מציפורניהם של אדוני הרשע והפשע, מנהלים החתולים הלוחמניים בית פיצה. אבל כל אימת שהרשע נושא אל-על את ראשו' הופכת הפיצריה החתולית למטה היי-טקי מתוחכם." + '[CR]' + 'מחמ"לם המצוייד, שולפים החתולים את ציפורניהם המושחזות ונכנסים לפעולה מהירה.','1',50)
	
	'''הקטקטים'''
	addDir("הקטקטים",['&youtube_pl=PLR7DTcU2p0Qg5sF-jE09YnRymKba8N8l_','&youtube_pl=PLN0EJVTzRDL-WaGew7sZQHQc1l48LSZmp'],17,'http://www.23tv.co.il/sip_storage/FILES/5/8305.jpg',addonString(110).encode('utf-8'),'1',50)	
	
	'''המומינים'''
	addDir("המומינים",['&youtube_pl=PL_8KXLhQVQMLvEJlwakyjEeFfOgGQKaCo','&youtube_pl=PL_8KXLhQVQMLB8AzFqkq5Tg7c_8ZX8RRb', '&youtube_pl=PLN0EJVTzRDL-IJiTK4_B1ni8tlRNQvaBg'],17,'http://upload.wikimedia.org/wikipedia/he/2/2b/%D7%94%D7%9E%D7%95%D7%9E%D7%99%D7%A0%D7%99%D7%9D.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''המעופפים הנועזים'''
	addDir("המעופפים הנועזים",['&youtube_pl=PLR7DTcU2p0QhYwFJuI0zFXFmAN-q6n4A0','&youtube_pl=PL_8KXLhQVQMLhguXwe-d2HjvficZsfbEj','&sdarot=season_id=1&series_id=1387&series_name=%d7%94%d7%9e%d7%a2%d7%95%d7%a4%d7%a4%d7%99%d7%9d%20%d7%94%d7%a0%d7%95%d7%a2%d7%96%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1387%2fthe-little-flying-bears-%d7%94%d7%9e%d7%a2%d7%95%d7%a4%d7%a4%d7%99%d7%9d-%d7%94%d7%a0%d7%95%d7%a2%d7%96%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91'],17,'http://upload.wikimedia.org/wikipedia/he/archive/e/e8/20060406072630!Flying_bears.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''הלב מרקו'''
	addDir("הלב מרקו",['&youtube_pl=PL_8KXLhQVQMLx3W2W6YXTmaNHoPmlLl28'],17,'http://www.dossinet.me/coverage_pics/a0b25bf2f9a27e362a22f5a1dfac507f.jpg',addonString(110).encode('utf-8'),'1',"")
	
	'''הענק הירוק'''
	if General_TrustedOnly == "true" or admin: addDir("הענק הירוק",['&sdarot=series_id=1738&series_name=%d7%94%d7%a2%d7%a0%d7%a7%20%d7%94%d7%99%d7%a8%d7%95%d7%a7%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1738%2fthe-incredible-hulk-%d7%94%d7%a2%d7%a0%d7%a7-%d7%94%d7%99%d7%a8%d7%95%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91'],6,'http://www.sdarot.pm/media/series/1738.jpg','"הענק" (באנגלית: The Incredible Hulk, או בכינויו העברי "הענק הירוק") הוא דמות בדיונית המופיעה בחוברות קומיקס של חברת מארוול קומיקס.[CR]','1',50)
	
	'''הפנתר הורוד'''
	addDir('הפנתר הורוד',['&sdarot=series_id=1347&series_name=%d7%94%d7%a4%d7%a0%d7%aa%d7%a8%20%d7%94%d7%95%d7%95%d7%a8%d7%95%d7%93%20%2a%d7%90%d7%99%d7%9c%d7%9d%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1347%2fthe-pink-panther-cartoons-%d7%94%d7%a4%d7%a0%d7%aa%d7%a8-%d7%94%d7%95%d7%95%d7%a8%d7%95%d7%93-%d7%90%d7%99%d7%9c%d7%9d', '&youtube_ch=PinkPanthersShow'],6,'http://www.sdarot.pm/media/series/1347.jpg',addonString(113).encode('utf-8'),'1',50)
	
	'''וולברין והאקס מן'''
	addDir("וולברין והאקס מן",['&youtube_pl=PLR7DTcU2p0QhGsv3LuA3GnCJWjoPBCafl', '&sdarot=season_id=1&series_id=823&series_name=%d7%95%d7%95%d7%9c%d7%91%d7%a8%d7%99%d7%9f%20%d7%95%d7%94%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f823%2fwolverine-and-the-x-men-%d7%95%d7%95%d7%9c%d7%91%d7%a8%d7%99%d7%9f-%d7%95%d7%94%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94'],17,'http://i.ytimg.com/vi/_C9qXB0iPUY/hqdefault.jpg','שנה אחרי פיצוץ מסתורי בבית הספר למוטנטים לוגן מתעמת שוב מול מוס שמכניס לכלא משפחה שהחביאה את לוגן. האנק מנסה לפענח את הפיצוץ בביה"ס ויחד עם לוגן מתכונן למלחמה הקרובה. וולברין ואקס מן - וולברין מאחד את צוות אקס מן- צוות מוטנטים רודפי השלום. הצוות מתמודד גם מול אויבים מוטנטים בהנהגתו של מגנטו, וגם מול בני אדם, בפיקודו של הסנאטור קלי, ומנסה למנוע מלחמה בין בני האדם למוטנטים שתביא להרס עולמי/','1',"")
	
	'''חוש חש הבלש'''
	addDir("חוש חש הבלש",['&sdarot=season_id=1&series_id=1397&series_name=%d7%97%d7%95%d7%a9%20%d7%97%d7%a9%20%d7%94%d7%91%d7%9c%d7%a9%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%a7%d7%95%d7%9e%d7%99%d7%aa%2c%20%22%d7%97%d7%95%d7%a9%20%d7%97%d7%a9%22%20%d7%94%d7%95%d7%90%20%d7%91%d7%9c%d7%a9%20%d7%9e%d7%a4%d7%95%d7%96%d7%a8%2c%20%d7%9e%d7%92%d7%95%d7%a9%d7%9d%20%d7%95%d7%9c%d7%90%20%d7%99%d7%95%d7%a6%d7%9c%d7%97%20%d7%a9%d7%91%d7%92%d7%95%d7%a4%d7%95%20%d7%94%d7%95%d7%a9%d7%aa%d7%9c%d7%95%20%d7%90%d7%99%d7%91%d7%a8%d7%99%d7%9d%20%d7%91%d7%99%d7%95%d7%a0%d7%99%d7%99%d7%9d%20%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%a7%d7%a0%d7%99%d7%9d%20%d7%9c%d7%95%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%20%d7%a2%d7%9c%20%d7%98%d7%91%d7%a2%d7%99%d7%99%d7%9d.%20%d7%90%d7%95%d7%99%d7%91%d7%95%20%d7%94%d7%a2%d7%99%d7%a7%d7%a8%d7%99%20%d7%94%d7%95%d7%90%20%d7%93%d7%95%d7%a7%d7%98%d7%95%d7%a8%20%d7%a8%d7%a9%d7%a2%20%d7%95%d7%9e%d7%a1%d7%aa%d7%95%d7%a8%d7%99%2c%20%d7%9e%d7%a0%d7%94%d7%99%d7%92%20%d7%90%d7%a8%d7%92%d7%95%d7%9f%20%d7%a4%d7%a9%d7%a2.%20%d7%9c%d7%97%d7%95%d7%a9%20%d7%97%d7%a9%20%d7%a2%d7%95%d7%96%d7%a8%d7%99%d7%9d%20%d7%90%d7%97%d7%99%d7%99%d7%a0%d7%99%d7%aa%d7%95%20%d7%a7%d7%a8%d7%9f%20%d7%95%d7%9b%d7%9c%d7%91%d7%94%20%d7%94%d7%97%d7%9b%d7%9d%20%22%d7%9e%d7%95%d7%97%22%2c%20%d7%9b%d7%9e%d7%95%20%d7%92%d7%9d%20%d7%a9%d7%a0%d7%99%20%d7%94%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%99%d7%9d%20%d7%a4%d7%99%d7%93%d7%92%27%d7%98%20%d7%95%d7%93%d7%99%d7%92%27%d7%98%20%d7%94%d7%9e%d7%9b%d7%95%d7%a0%d7%99%d7%9d%20%22%d7%94%d7%97%d7%95%d7%a9%d7%97%d7%a9%d7%99%d7%9d%22.%20%d7%94%d7%9d%20%d7%9e%d7%a6%d7%99%d7%9c%d7%99%d7%9d%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9e%d7%a1%d7%9b%d7%a0%d7%95%d7%aa%20%d7%95%d7%9e%d7%9b%d7%95%d7%95%d7%a0%d7%99%d7%9d%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9c%d7%a1%d7%99%d7%9b%d7%95%d7%9c%20%d7%94%d7%a4%d7%a9%d7%a2%20%d7%9e%d7%91%d7%9c%d7%99%20%d7%a9%d7%94%d7%95%d7%90%20%d7%9e%d7%95%d7%93%d7%a2%20%d7%9c%d7%9b%d7%9a%20%d7%91%d7%9b%d7%9c%d7%9c.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1397%2finspector-gadget-%d7%97%d7%95%d7%a9-%d7%97%d7%a9-%d7%94%d7%91%d7%9c%d7%a9-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=PLcnOogeoQ4TrfP9mO57AQY543KTLaTl8N', '&youtube_id=MbgrFDbE3b0', '&youtube_id=kWmBP09MM9w', '&youtube_id=P3gW3zPEhjY', '&youtube_id=uj9miIc0Ow4'],17,'http://www.sdarot.pm/media/series/1397.jpg','','1',50)
	
	'''טום וג'רי'''
	addDir("טום וג'רי",['&youtube_pl=PLN0EJVTzRDL-jbMDnITZcYO48kE1Hv3mc', '&youtube_pl=PLs3DueTtwGGppFDT2xv9zVBf4mz6RuOLj', '&youtube_pl=PL6hnqKp_bygo_2MFE6j3WWLitYXwhHGx3'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/2/23/Tomjerrylogo40s.jpg/280px-Tomjerrylogo40s.jpg',"טום וג'רי (באנגלית: Tom and Jerry)‏ היא שמה של סדרת סרטי אנימציה קצרים מיוחדים ומצחיקים שנוצרו על ידי ויליאם האנה וג'וזף ברברה עבור MGM בשנות הארבעים, שנות החמישים ושנות השישים.",'1',50)
	
	'''משטרת האגדות'''
	addDir("משטרת האגדות",['&youtube_pl=PLR7DTcU2p0QiaEmc56lGHMpxW4ladE93X'],17,'http://www.tvland.co.il/Pics/mishterethaagadotbig.jpg',addonString(110).encode('utf-8'),'1',"")
	
	'''נאנוק'''
	addDir("נאנוק",['&youtube_pl=PL_8KXLhQVQMJJ4nHubadbykzbHhzzmUPu'],17,'http://www.popy.co.il/media/Objects/Contents/E39C72A33AED45878CAB555CC24CE6BB.png.img?w=209&h=161&t=f',addonString(110).encode('utf-8'),'1',50)
	
	'''נילס הולגרסון'''
	addDir("נילס הולגרסון",['&youtube_pl=PL_8KXLhQVQMKVZInMgWpGe9osYlO5lcBa'],17,'http://www.sratim.co.il/contents/series/images/IL/2072.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''סמשריקי (רוסית)'''
	list = []
	list.append('&youtube_pl=PL7D9A5D1CCBF96850')
	list.append('&youtube_pl=PLdBOR-FS76gzBslnoA7yjz9CsyX4d32Oz')
	list.append('&youtube_pl=PLK7zXb6tNkib1KxdOFqWGAxZEUBv3l_fv')
	addDir("סמשריקי (רוסית)",list,17,'http://www.nevcheeses.com/images/%D1%81%D0%BC.jpg','Kikoriki, known in Russian as Smeshariki (Russian: Смеша́рики), is a Russian animated television series consisting of 208 episodes of 6 minutes and 30 seconds each, aimed at children of 3 to 8 years.[CR]The first episode premiered in Russia on May 7, 2004. English-language distribution rights to the series were acquired by 4Kids Entertainment from worldwide distributor Fun Game Media, Munich[1] and began airing as part of The CW4Kids block on The CW on September 13, 2008, under the name GoGoRiki.[CR]Fun Game Media is also producing a European version, which began airing on KI.KA on December 8, 2008.[CR]The Smeshariki (the name is derived from смешные "smeshnye" meaning "funny", and шарики "shariki" meaning "little balls") are stylized rounded animals. Each of the nine characters has a unique personality and a range of interests with no negative characters among them. Plots are built not on the battle of opposing forces but on the unexpected situations the animated characters stumble upon in their interactions deemed similar to the ones that children may encounter in their everyday lives. Many of the topics foreground the guidance that friendship and community provide to the individual making his or her way in the world. Complex themes and specific cultural references place this cartoon firmly within the Russian tradition of animation.[5] Much attention was devoted to the humor in the series, some of which has attracted adults as well.','1',50)
	
	'''ספיד רייסר'''
	addDir("ספיד רייסר",['&youtube_pl=PLR7DTcU2p0QjzH9muKiw1eTbp0aU3hB63'],17,'http://www.sdarot.pm/media/series/1804.jpg','הסדרה מתמקדת הפעם בבנו של ספיד רייסר האגדי. צעיר, מוכשר, הולך בעקבות אביו המחליט לפתוח בית ספר לנערים ושם למצוא את הנהג הצעיר המהיר בעולם.','1',50)
	
	'''פאואר ריינגרס'''
	
	'''פיטר פן'''
	addDir("פיטר פן",['&youtube_pl=PL_8KXLhQVQMIMJ_lQkl0Z393wwTtRgg_i', '&youtube_pl=PLiDCIQSNnvwc-FqtPLIy3i3i5p0UoB5Fr', '&sdarot=season_id=1&series_id=1000&series_name=%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1000%2fpeter-pan-%d7%a4%d7%99%d7%98%d7%a8-%d7%a4%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91'],17,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSpAqoUxOIErj3Kgl4053S4oixnvZCcvoJwhf83xupmupsHWKh8',"הטלוויזיה החינוכית חוזרת לשדר את הסדרה הקלסית פיטר פן, המבוססת על ספרו של ג'יימס מתיו ברי, ספר שיצא בשנת 1911 תחת השם"'"פיטר וּוונדי".','1',50)
	
	'''פינגווינים'''
	addDir("פינגווינים",['&youtube_pl=PL_8KXLhQVQMIkR9iafygY0ztBUPSAyUki'],17,'https://i.ytimg.com/vi/vzVdiqGJZ7E/default.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''פינוקיו'''
	addDir('פינוקיו',['&youtube_pl=PL17BB1526E0625514', '&sdarot=series_id=904&series_name=%d7%a4%d7%99%d7%a0%d7%95%d7%a7%d7%99%d7%95%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f904%2fthe-adventures-of-pinocchio-%d7%a4%d7%99%d7%a0%d7%95%d7%a7%d7%99%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_id=V098tHKky5A', '&youtube_id=Rv1VHwYWPsE'],17,'http://www.sdarot.pm/media/series/904.jpg',"ג'פטו, הנגר הבודד, גילף מבול עץ בובה שניעורה לחיים והפכה לבן שמעולם לא היה לו.[CR]"'פינוקיו השובב נשלח לבי"ס, אך ברח מהבית, ויצא לגלות את העולם ולעבור הרפתקאות רבות עם הברווזה בלה.','1',50)
	
	'''פיקסי (רוסית)''' #fixiki
	list = []
	list.append('&youtube_pl=PLC72B44008078E9FE')
	list.append('&youtube_pl=PLK7zXb6tNkibmTrztTTHZjd6QignUW4Cq')
	list.append('&youtube_pl=PLbDVT2u1fI0CNahEm2F8SSlZrDN5GrbJn')
	
	addDir('פיקסי (רוסית)',list,17,'http://www.youloveit.ru/uploads/gallery/main/791/youloveit_ru_fixiki_kartinki18.jpg','','1',50)
	
	
	'''קופיקו'''
	addDir('קופיקו',['&youtube_pl=UCCktKuBGZ1kHifzp9Mxu6Eg', '&youtube_pl=PLN0EJVTzRDL_9qHYdDXgf6tslifiY_4zI', '&youtube_pl=PLR7DTcU2p0QhDzYbbniDNwSbXUM_p6N3f', '&youtube_pl=PLR7DTcU2p0QgEdLPHhrhKtxElvYVrseAQ', '&youtube_pl=PLR7DTcU2p0QhNGUffSgu8_5dP3lnOGZTx', '&sdarot=season_id=1&series_id=1810&series_name=%d7%a7%d7%95%d7%a4%d7%99%d7%a7%d7%95%20%d7%97%d7%95%d7%a7%d7%99%20%d7%94%d7%92%27%d7%95%d7%a0%d7%92%d7%9c&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1810%2fkofiko-jungle-laws-%d7%a7%d7%95%d7%a4%d7%99%d7%a7%d7%95-%d7%97%d7%95%d7%a7%d7%99-%d7%94%d7%92-%d7%95%d7%a0%d7%92%d7%9c', '&sdarot=series_id=422&series_name=%d7%a7%d7%95%d7%a4%d7%99%d7%a7%d7%95&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f422%2fkofiko-%d7%a7%d7%95%d7%a4%d7%99%d7%a7%d7%95'],17,'http://www.sdarot.pm/media/series/422.jpg',addonString(104070).encode('utf-8'),'1',50)
	
	'''רובוטריקים'''
	if General_TrustedOnly == "true" or admin: addDir('רובוטריקים',['&sdarot=series_id=1395&series_name=%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1395%2ftransformers-hebdub-%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91'],17,'http://www.sdarot.pm/media/series/1395.jpg','הרובוטריקים (באנגלית: Transformers) הנה סדרת תכניות ילדים שהומצאה בעקבות סדרת צעצועים מצליחה של חברת טאקארה היפנית ולאחריה נוצרו גם סרטים נלווים וספרי קומיקס.[CR]היא נוצרה בארצות הברית בשנות ה-80. בסדרה מתואר מאבק בין מכונות?ענק בעלות תודעה, המסוגלות להפוך את צורתן מצורה דמוית-אנוש לצורה אחרת, לרוב כלי-רכב שונים.[CR]בישראל שודרו שתי העונות הראשונות של הסדרה בשנות השמונים בטלוויזיה החינוכית בדיבוב המקורי באנגלית עם כתוביות בעברית. כיום משודרת הסדרה בערוץ פוקס קידס בפרקים חדשים ובדיבוב לעברית.','1',50)
	
	'''רחוב סומסום'''
	addDir('רחוב סומסום',['&youtube_pl=PLN0EJVTzRDL-zyHvJ7O4PTkwfwhm0GM0O', '&youtube_id=S9yMeuZnqf8', '&youtube_id=8Ce3d4Y1lXc', '&youtube_id=irGBfOr5M-0', '&youtube_id=7MsiQVLXANI', '&youtube_id=b9cppzqQEdk', '&youtube_id=UbebFD2BzSQ', '&youtube_id=5dHad5l61t0', '&youtube_id=f4Z0MxSQ3dc', '&youtube_id=hBsDetJvy2E', '&youtube_id=Y8CFfUbvuZI', '&youtube_id=ELQ0xiL5X7I', '&youtube_id=5uRyIMy2ktA'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/4/41/SessemeStreet.jpg/200px-SessemeStreet.jpg',addonString(104000).encode('utf-8'),'1',50)
	
	'''צבי הנינג'ה'''
	addDir("צבי הנינג'ה",['&sdarot=season_id=1&series_id=636&series_name=%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92%27%d7%94%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f636%2fteenage-mutant-ninja-turtles-%d7%a6%d7%91%d7%99-%d7%94%d7%a0%d7%99%d7%a0%d7%92-%d7%94-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94', '&youtube_id=W7B3NXG0aDY', '&youtube_id=E7naeIx3rqo'],17,'http://www.sdarot.pm/media/series/636.jpg',"צבי הנינג'ה היא סדרת אנימציה ופעולה פופולרית המבוססת במקור על קומיקס למבוגרים.[CR]הסדרה הופקה לטלוויזיה במקור לערוץ סינדיקציה, ואחר כך עברה ל-CBS. התוכנית שודרה בין השנים 1987 ל-1996.",'1',50)
	
	'''צבי הנינג'ה הדור הבא'''
	if General_TrustedOnly == "true": addDir("צבי הנינג'ה הדור הבא",['&sdarot=series_id=1670&series_name=%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92%27%d7%94%3a%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1670%2fninja-turtles-the-next-mutation-%d7%a6%d7%91%d7%99-%d7%94%d7%a0%d7%99%d7%a0%d7%92-%d7%94-%d7%94%d7%93%d7%95%d7%a8-%d7%94%d7%91%d7%90-%d7%9e%d7%93%d7%95%d7%91%d7%91'],6,'http://www.sdarot.pm/media/series/862.jpg',"מאסטר צ'ונג אי, ידידו הוותיק של ספלינטר, חולה מאד. לפני מותו, הוא מבקש מבתו המאומצת להתאחד עם צבי הנינג'ה אשר בימים אלה התבגרו כדי להציל את האנושות מפני דרקון-לורד, אשר השתחרר מארץ החלומות ומתכוון לשלוט בעולם.[CR]",'1',50)
	
	'''סנדוקאן'''
	addDir("סנדוקאן",['&youtube_pl=PLR7DTcU2p0QgWYVQap5zPK0MkwJizYku_'],17,'http://www.sdarot.pm/media/series/1308.jpg','הסדרה מספרת את סיפור הרפתקאותיהם של סנדוקאן, נסיך שהודח מכיסאו ומנסה להשיב לעצמו את כס המלוכה ואת אהובתו, הנסיכה מריאנה, ושל יאנז, הרפתקן פורטוגזי המשמש כיד ימינו.','1',50)
	
	'''סופר סטרייקה'''
	addDir(addonString(70).encode('utf-8'),['&sdarot=series_id=1566&series_name=%d7%a1%d7%95%d7%a4%d7%a8%20%d7%a1%d7%98%d7%a8%d7%99%d7%99%d7%a7%d7%94%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1566%2fsupa-strikas-%d7%a1%d7%95%d7%a4%d7%a8-%d7%a1%d7%98%d7%a8%d7%99%d7%99%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=PLU6_PRY_7y1TQMr67fJ6WC2mzkqtVyU3B', '&youtube_pl=PLKMFPiSCwUk3bjgDUSlTPskV9rA74nBiB'],17,'http://www.musicaneto.com/wp-content/uploads/2015/03/6246725.jpg',addonString(170).encode('utf-8'),'1',50)
	
	'''שאלתיאל קוואק'''
	addDir('שאלתיאל קוואק',['&youtube_pl=PL_8KXLhQVQMKOtRoV1SuOu95dvVo-ea2J', '&sdarot=series_id=1137&series_name=%d7%a9%d7%90%d7%9c%d7%aa%d7%99%d7%90%d7%9c%20%d7%a7%d7%95%d7%95%d7%90%d7%a7%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1137%2falfred-j-kwak-%d7%a9%d7%90%d7%9c%d7%aa%d7%99%d7%90%d7%9c-%d7%a7%d7%95%d7%95%d7%90%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91'],17,'http://www.sdarot.pm/media/series/1137.jpg','זמן קצר לאחר לידתו, שאלתיאל קוואק מאבד את הוריו, אחיו ואחיותיו אשר נהרגים בתאונת דרכים.[CR]חפי החפרפרת, חבר טוב של משפחתו, מגדל אותו. יחד עם חבריו יוצא שאלתיאל להרפתקאות רבות ומשונות ומפיק לקחים. המדינה בה מתגוררים שאלתיאל קוואק וקרוביו היא מַיִמוניה (בהולנדית Groot-Waterland, באנגלית Great Waterland, כלומר "ארץ המים הגדולה").','1',50)
	
	'''שלגיה ושבעת הגמדים'''
	addDir("שלגיה ושבעת הגמדים",['&youtube_pl=PL_8KXLhQVQMKKrMMm0glr1TMQoxCjFuTk'],17,'http://www.coloring4fun.com/wp-content/uploads/2013/03/snow-white-600x300.jpg',addonString(110).encode('utf-8'),'1',50)
	'''---------------------------'''
	
	'''ערוץ גאליס 1''' '''צריך לסנן להראות רק פרקים מלאים'''
	#if OFF_20 != "true": addDir(addonString(56).encode('utf-8') + space + "1",'UC1ZvZmYKkigob8Vg7MSgqjg',9,'http://yt3.ggpht.com/-2NPlgdL7mU8/AAAAAAAAAAI/AAAAAAAAAAA/ch9GzL2fOlM/s88-c-k-no/photo.jpg',addonString(156).encode('utf-8'),'1',"")
	
	#'''סדרות לילדים'''
	#seriestvheb1 = 'ערוצי סדרות א'
	#if OFF_17 != "true": addDir(addonString(44).encode('utf-8') + space + "10",seriestvheb1.decode('utf-8'),9,"https://yt3.ggpht.com/-hbyD79o9YWk/AAAAAAAAAAI/AAAAAAAAAAA/gOv2DB9cLC4/s100-c-k-no/photo.jpg",addonString(93).encode('utf-8'),'1',"")
	
	'''Walt Disney Cartoons'''
	addDir('Walt Disney Cartoons','plugin://plugin.video.supercartoons/?mode=400&page=1',8,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQQoKkxPt4MxnzTqM-ChAH7My_OdIZQJ2U6CoXIeDzOkdMBaG8G',addonString(130).encode('utf-8'),'1',58)
	
	'''סדרות לילדים באנגלית 2''' #NOT WORKING!
	if admin and not admin2: addDir('test','https://dl.dropboxusercontent.com/s/cwcptnocx310g00/Merry_Melodies.plx',7,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmzwydiY6V_l5sE_ed7Rf66G6B8Ug2p7ajn4uPAhH2NYpDVMNBUQ','','1',"")
	
	'''test'''
	#addDir("test",'http://www.navixtreme.com/wiilist/all.plx?page=4',7,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmzwydiY6V_l5sE_ed7Rf66G6B8Ug2p7ajn4uPAhH2NYpDVMNBUQ','','1',"")
	
	
def CATEGORIES105(admin):
	'''------------------------------
	---checksites--------------------
	------------------------------'''
	'''plugin.video.seretil'''
	check_seretil_me = urlcheck('http://seretil.me', ping=True)
	check_10q_tv = urlcheck('http://10q.tv', ping=True)
	check_gozlan_me = urlcheck('http://gozlan.me', ping=True)
	check_movix_me = urlcheck('http://www.movix.me/series', ping=True) #GAL CHECK THIS (PING)
	#if systemplatformwindows: output = terminal('ping seretil.me -n 1',"Connected2")
	#else: output = terminal('ping -W 1 -w 1 -4 -q seretil.me',"Connected")
	#if (not systemplatformwindows and ("1 packets received" in output or not "100% packet loss" in output)) or (systemplatformwindows and ("Received = 1" in output or not "100% loss" in output)): check_seretil_me = "true"
	'''---------------------------'''
	
	'''plugin.video.10qtv'''
	
	#if systemplatformwindows: output = terminal('ping 10q.tv -n 1',"Connected2")
	#else: output = terminal('ping -W 1 -w 1 -4 -q 10q.tv',"Connected")
	#if (not systemplatformwindows and ("1 packets received" in output or not "100% packet loss" in output)) or (systemplatformwindows and ("Received = 1" in output or not "100% loss" in output)): check_10q_tv = "true"
	'''---------------------------'''
	
	
	'''סרטים מדובבים'''
	count = 1
	if check_movix_me == 'ok':
		addDir(addonString(10520).encode('utf-8') + space + str(count),'plugin://plugin.video.movixws/?iconimage=http%3a%2f%2fwww.in-hebrew.co.il%2fimages%2flogo-s.jpg&mode=2&name=Kids%20-%20%d7%99%d7%9c%d7%93%d7%99%d7%9d&url=http%3a%2f%2fwww.movix.me%2fgenres%2fKids',8,'http://www.in-hebrew.co.il/images/logo-s.jpg','','1',50) ; count += 1
		addDir(addonString(10520).encode('utf-8') + space + str(count),'plugin://plugin.video.movixws/?iconimage=http%3a%2f%2ficons.iconarchive.com%2ficons%2fdesignbolts%2ffree-movie-folder%2f256%2fAnimated-icon.png&mode=2&name=Animation%20-%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&url=http%3a%2f%2fwww.movix.me%2fgenres%2fAnimation',8,'http://icons.iconarchive.com/icons/designbolts/free-movie-folder/256/Animated-icon.png','','1',50) ; count += 1
	if check_seretil_me == 'ok':
		#addDir(addonString(10520).encode('utf-8'),list1,6,'http://www.iphoneil.net/icone/111185-icon.png',addonString(105200).encode('utf-8'),'1',50)
		addDir(addonString(10520).encode('utf-8') + space + str(count),'plugin://plugin.video.seretil/?mode=4&name=%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d%20%d7%a8%d7%90%d7%a9%d7%99&url=http%3a%2f%2fseretil.me%2fcategory%2f%25D7%25A1%25D7%25A8%25D7%2598%25D7%2599%25D7%259D-%25D7%259E%25D7%2593%25D7%2595%25D7%2591%25D7%2591%25D7%2599%25D7%259D%2fpage1%2f',8,'http://blog.tapuz.co.il/seretilNET/images/3745375_1.jpg',addonString(105200).encode('utf-8'),'1',58) ; count += 1
		if General_TrustedOnly == "false" or admin: 
			addDir('[COLOR=Red]' + addonString(10520).encode('utf-8') + space + str(count) + '[/COLOR]','plugin://plugin.video.seretil/?mode=211&name=%20%d7%90%d7%95%d7%a1%d7%a3%20%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d&url=http%3a%2f%2fseretil.me%2f%25D7%2590%25D7%2595%25D7%25A1%25D7%25A3-%25D7%25A1%25D7%25A8%25D7%2598%25D7%2599%25D7%259D-%25D7%259E%25D7%2593%25D7%2595%25D7%2591%25D7%2591%25D7%2599%25D7%259D%2f',8,'http://blog.tapuz.co.il/seretilNET/images/3745375_1.jpg',addonString(196).encode('utf-8'),'1',50) ; count += 1
			addDir('[COLOR=Red]' + addonString(10520).encode('utf-8') + space + str(count) + '[/COLOR]','plugin://plugin.video.seretil/?mode=211&name=%d7%90%d7%95%d7%a1%d7%a3%20%d7%9e%d7%a1%d7%a4%d7%a8%202%20%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d&url=http%3a%2f%2fseretil.me%2f%25D7%2590%25D7%2595%25D7%25A1%25D7%25A3-%25D7%2592%25D7%2593%25D7%2595%25D7%259C-%25D7%25A9%25D7%259C-%25D7%25A1%25D7%25A8%25D7%2598%25D7%2599%25D7%259D-%25D7%259E%25D7%25A6%25D7%2595%25D7%2599%25D7%25A8%25D7%2599%25D7%259D%25D7%259E%25D7%2593%25D7%2595%25D7%2591%25D7%2591%25D7%2599%25D7%259D%2f',8,'http://blog.tapuz.co.il/seretilNET/images/3745375_1.jpg',addonString(196).encode('utf-8'),'1',50) ; count += 1
			'''---------------------------'''
	'''---------------------------'''	

	'''סרטים מתורגמים'''
	count = 1
	if check_gozlan_me == 'ok':
		addDir(addonString(10535).encode('utf-8') + space + str(count),'plugin://plugin.video.gozlan.me/?mode=1&name=%d7%a1%d7%a8%d7%98%d7%99%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&url=http%3a%2f%2fanonymouse.org%2fcgi-bin%2fanon-www.cgi%2fhttp%3a%2f%2fgozlan.co%2f%2fsearch.html%3fg%3d%25D7%2590%25D7%25A0%25D7%2599%25D7%259E%25D7%25A6%25D7%2599%25D7%2594',8,'http://ftp.acc.umu.se/mirror/addons.superrepo.org/v5/addons/plugin.video.gozlan.me/icon.png','','1',58) ; count += 1
		addDir(addonString(10535).encode('utf-8') + space + str(count),'plugin://plugin.video.gozlan.me/?mode=1&name=%d7%a1%d7%a8%d7%98%d7%99%20%d7%9e%d7%a9%d7%a4%d7%97%d7%94&url=http%3a%2f%2fanonymouse.org%2fcgi-bin%2fanon-www.cgi%2fhttp%3a%2f%2fgozlan.co%2f%2fsearch.html%3fg%3d%25D7%259E%25D7%25A9%25D7%25A4%25D7%2597%25D7%2594',8,'http://ftp.acc.umu.se/mirror/addons.superrepo.org/v5/addons/plugin.video.gozlan.me/icon.png','','1',58) ; count += 1
		'''---------------------------'''
	if check_10q_tv == 'ok': 
		addDir(addonString(10535).encode('utf-8') + space + str(count),'plugin://plugin.video.10qtv/?mode=6&name=אנימציה&url=http://www.10q.tv/board/filmy/animciha/5',8,'http://mirror.cinosure.com/superrepo/v5/addons/plugin.video.10qtv/icon.png',addonString(110).encode('utf-8'),'1',57) ; count += 1
		addDir(addonString(10535).encode('utf-8') + space + str(count),'plugin://plugin.video.10qtv/?mode=6&name=%d7%9e%d7%a9%d7%a4%d7%97%d7%94&url=http%3a%2f%2fwww.10q.tv%2fboard%2ffilmy%2fmshfhha%2f17',8,'http://mirror.cinosure.com/superrepo/v5/addons/plugin.video.10qtv/icon.png',addonString(110).encode('utf-8'),'1',57) ; count += 1
		'''---------------------------'''
	
	addDir(addonString(10535).encode('utf-8') + space + str(count),['&wallaNew=genre%3dkids%26genreId%3d7449', '&wallaNew=genre%3dmovies%26genreId%3d6261'],6,'https://lh6.ggpht.com/V8v_FzkTMqeLRg_oY7G00zf0bcxubsm659cLrbf9nEKMLHQG-5LSZdbbJGQgkV6j1PQ=w300',addonString(189).encode('utf-8'),'1',50) ; count += 1	
	'''---------------------------'''
	
def CATEGORIES106(admin):

	'''אוליבר'''
	addDir('אוליבר',['&youtube_pl=PLRnOaTF6ebYrvwkVqB6fC-93hwHZmYnDk', '&youtube_id=UftKh1FeHSs'],17,'http://media.israel-music.com/images/7290013890849.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''בייבי איינשטיין'''
	addDir('בייבי איינשטיין',['&youtube_pl=PLvadvyUkv4iFxFnsG0i1mLhuvR5nQBUcf', '&youtube_pl=PLFB481A7458E12A61'],17,'http://d202m5krfqbpi5.cloudfront.net/books/1170326163l/46377.jpg',addonString(120).encode('utf-8'),'1',50) #TerrapinStation5
	
	'''בייבי'''
	addDir('בייבי','UCj10fKNd5h64J_M9YIQu0Zw/playlists',9,'http://yt3.ggpht.com/-RYFi0L82fh4/AAAAAAAAAAI/AAAAAAAAAAA/1hhzmsuRybc/s88-c-k-no/photo.jpg',addonString(131).encode('utf-8'),'1',50)
	
	'''אוצר מילים עם נוני'''
	addDir('אוצר מילים עם נוני',['&youtube_pl=PLErYJg2XgxyXmgk6cyROtlJh2g-Fk_T6n', '&youtube_id=hu7Wa2URXi4', '&youtube_id=zSHKufiJvL4'],17,'http://i.ytimg.com/vi/m67adbe1SOg/0.jpg',addonString(173).encode('utf-8'),'1',50)
	
	'''בילי בם בם'''
	
	'''גילגולון'''
	
	'''דובים ונהנים'''
	addDir('דובים ונהנים',['&youtube_pl=P5xdsj7ImrA&list=PLTleo-h9TFqIaAW5pDJO8ThJ_rrohsRLE'],17,'http://luli.tv/Img/Albums/556/medium/%D7%93%D7%95%D7%91%D7%99%D7%9D-%D7%95%D7%A0%D7%94%D7%A0%D7%99%D7%9D3.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''דרקו'''
	
	'''הגלופסים'''
	
	'''הכבשה שושנה'''
	addDir(addonString(10630).encode('utf-8'),['&wallaNew=item_id%3D2819037', '&wallaNew=item_id%3D2819043', '&wallaNew=item_id%3D2819050', '&wallaNew=item_id%3D2817560', '&wallaNew=item_id%3D2817583', '&wallaNew=item_id%3D2817533', '&wallaNew=item_id%3D2820067', '&youtube_pl=PLC47880737B43FF96'],17,'http://www.sdarot.pm/media/series/1487.jpg',addonString(106300).encode('utf-8'),'1',50)
	
	'''הנימנונמים'''
	addDir(addonString(10633).encode('utf-8'),['&wallaNew=seasonId%3d2556132', '&sdarot=season_id=1&series_id=873&series_name=%d7%94%d7%a0%d7%99%d7%9e%d7%a0%d7%95%d7%9e%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f873%2fhanimnumim-%d7%94%d7%a0%d7%99%d7%9e%d7%a0%d7%95%d7%9e%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91'],6,'http://www.sdarot.pm/media/series/873.jpg',addonString(106300).encode('utf-8'),'1',50)
	
	''''''
	
	''''''
	
	'''זומזומים'''
	
	''''''
	
	'''טונקי'''
	
	'''טיגה וטוגה'''
	
	''''''
	
	'''טימי הטלה'''
	addDir('טימי הטלה',['&youtube_pl=PLLkqDC9xIu8Z7Aflrjr9SVbULT-42942l', '&youtube_pl=PLnw_wYZBfzuNfTcbuUfPrDov2jC8APZk0', '&youtube_id=_vb2lCx36bA'],17,'http://www.littleprince.co.il/pub/5897/timmy/timmy~big%20and%20cuddly~hr~21017.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''טין טן'''
	
	'''טיפה טופה'''
	
	'''טלטאביז'''
	addDir(addonString(10642).encode('utf-8'),['&youtube_pl=PLBDE473A2E30EE847', '&youtube_id=TGmpQKg2NtQ', '&youtube_id=mAlgerULqyU', '&youtube_id=3cJYHKsa52E', '&youtube_id=BOzl3RHn4Io', '&youtube_id=VZzivZvWidI', '&youtube_id=NN_gqjA8jJQ', '&youtube_id=AL0RVZMr-VY', '&youtube_id=C_Km9NYD-Pw', '&youtube_id=d_zk--Iconw', '&youtube_id=d3yfZlIUwF4', '&youtube_id=GUWpiwVZ-gI', '&youtube_id=wTm5rDg8tqI', '&youtube_id=1E9Z0-ppTl0', '&youtube_id=JdKoA4lIENc', '&youtube_id=GI4j0xDtU5Y'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/4/49/Teletubbies_DVD.jpg/200px-Teletubbies_DVD.jpg',addonString(106420).encode('utf-8'),'1',50)
	
	'''לולה בייבי'''
	addDir('לולה בייבי','UCOYUFFxT50nvDaRj5Mn5XNg',9,'http://yt3.ggpht.com/-C9HFu_35bmk/AAAAAAAAAAI/AAAAAAAAAAA/O5-pgwvceRI/s88-c-k-no/photo.jpg',addonString(154).encode('utf-8'),'1',"")
	
	'''לולי'''
	addDir('לולי',['&youtube_ch=UCcYc90JDakyeXGeZgPL1ejA/playlists', '&youtube_pl=PLwimDnICcPKNQy5TSz2s5XKWsE6kKV5C1'],17,'http://yt3.ggpht.com/-n8_yk3MKYEk/AAAAAAAAAAI/AAAAAAAAAAA/0lOK__EwCtg/s88-c-k-no/photo.jpg',addonString(133).encode('utf-8'),'1',50)
	
	'''מאשה והדוב'''
	addDir('מאשה והדוב',['&youtube_pl=PL4-zn_348odBKcfUeZznqhkc_-UYtWnep', '&youtube_pl=PLdAdTJgxziWAXNLIR5oeHbUT8HDnXOjAt', '&youtube_pl=PLXnIohISHNIvsnUNe8RwvhksUSFzdQsiT'],17,'http://assets3.mi-web.org/foto_miniaturas/0012/5812/Masha_Oso028_mediano.jpg?1368008744',addonString(110).encode('utf-8'),'1',50)
	
	'''מוסטי'''
	
	'''מיילו'''
	
	'''מיפי'''
	addDir('מיפי',['&youtube_pl=PLTleo-h9TFqJWHazTOTJNQrcrkSZ_Gg83', '&wallaNew=seasonId%3d2542087', '&sdarot=season_id=1&series_id=881&series_name=%d7%9e%d7%99%d7%a4%d7%99%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%9e%d7%91%d7%95%d7%a1%d7%a1%d7%aa%20%d7%a2%d7%9c%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%a1%d7%a4%d7%a8%d7%99%20%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%9e%d7%a6%d7%9c%d7%99%d7%97%d7%94%20%d7%94%d7%97%d7%95%d7%a9%d7%a4%d7%aa%20%d7%90%d7%aa%20%d7%94%d7%a6%d7%95%d7%a4%d7%99%d7%9d%20%d7%91%d7%a4%d7%a0%d7%99%20%d7%9e%d7%95%d7%a9%d7%92%d7%99%20%d7%99%d7%a1%d7%95%d7%93%20%d7%9b%d7%9e%d7%95%20%d7%a6%d7%91%d7%a2%d7%99%d7%9d%2c%20%d7%a1%d7%a4%d7%a8%d7%95%d7%aa%20%d7%95%d7%a6%d7%95%d7%a8%d7%95%d7%aa.%20%d7%91%d7%9b%d7%9c%20%d7%a4%d7%a8%d7%a7%20%d7%90%d7%a0%d7%97%d7%a0%d7%95%20%d7%9e%d7%92%d7%9c%d7%99%d7%9d%20%d7%a7%d7%a6%d7%aa%20%d7%a2%d7%9c%20%d7%94%d7%97%d7%99%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%9e%d7%99%d7%a4%d7%99%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%94%20%d7%94%d7%98%d7%95%d7%91%d7%99%d7%9d%20%d7%95%d7%99%d7%95%d7%a6%d7%90%d7%99%d7%9d%20%d7%9c%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa.%20%d7%9e%d7%99%d7%a4%d7%99%20%d7%94%d7%90%d7%a8%d7%a0%d7%91%d7%aa%20%d7%94%d7%90%d7%94%d7%95%d7%91%d7%94%20%d7%95%d7%94%d7%9e%d7%95%d7%9b%d7%a8%d7%aa%20%d7%a0%d7%95%d7%9c%d7%93%d7%94%20%d7%91%d7%9b%d7%aa%d7%91%d7%99%d7%95%20%d7%95%d7%a6%d7%99%d7%95%d7%a8%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%94%d7%90%d7%9e%d7%9f%20%d7%94%d7%94%d7%95%d7%9c%d7%a0%d7%93%d7%99%20%d7%93%d7%99%d7%a7%20%d7%91%d7%a8%d7%95%d7%a0%d7%90%d7%94%20%d7%91%d7%a9%d7%a0%d7%aa%201955%2c%20%d7%9e%d7%aa%d7%95%d7%9a%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%d7%9d%20%d7%a9%d7%a1%d7%99%d7%a4%d7%a8%20%d7%9c%d7%91%d7%99%d7%aa%d7%95%20%d7%91%d7%aa%20%d7%94%d7%a9%d7%a0%d7%94%20%d7%a2%d7%9c%20%d7%90%d7%a8%d7%a0%d7%91%d7%aa%20%d7%a9%d7%a4%d7%92%d7%a9%d7%95%20%d7%99%d7%97%d7%93%d7%99%d7%95%20%d7%91%d7%97%d7%99%d7%a7%20%d7%94%d7%98%d7%91%d7%a2.%20%d7%91%d7%a1%d7%93%d7%a8%d7%aa%20%d7%94%d7%a1%d7%a8%d7%98%d7%99%d7%9d%2c%20%d7%a0%d7%a4%d7%92%d7%95%d7%a9%20%d7%90%d7%aa%20%d7%9e%d7%99%d7%a4%d7%99%20%d7%95%d7%90%d7%aa%20%d7%91%d7%a0%d7%99%20%d7%9e%d7%a9%d7%a4%d7%97%d7%aa%d7%94%20%d7%94%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%3a%20%d7%94%d7%95%d7%a8%d7%99%d7%94%2c%20%d7%94%d7%a1%d7%91%d7%99%d7%9d%2c%20%d7%93%d7%95%d7%93%d7%94%20%d7%90%d7%9c%d7%99%d7%a1%2c%20%d7%91%d7%a8%d7%91%d7%a8%d7%94%20%d7%95%d7%91%d7%95%d7%a8%d7%99%d7%a1%20%d7%94%d7%93%d7%95%d7%91%d7%99%d7%9d%2c%20%d7%a4%d7%95%d7%a4%d7%99%20%d7%94%d7%97%d7%96%d7%99%d7%a8%2c%20%d7%95%d7%a2%d7%95%d7%93.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f881%2fmiffy-%d7%9e%d7%99%d7%a4%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91'],17,'http://www.sdarot.pm/media/series/881.jpg','סדרה המבוססת על סדרת ספרי ילדים מצליחה החושפת את הצופים בפני מושגי יסוד כמו צבעים, ספרות וצורות.[CR]בכל פרק אנחנו מגלים קצת על החיים של מיפי וחבריה הטובים ויוצאים להרפתקאות. מיפי הארנבת האהובה והמוכרת נולדה בכתביו וציוריו של האמן ההולנדי דיק ברונאה בשנת 1955, מתוך סיפורים שסיפר לביתו בת השנה על ארנבת שפגשו יחדיו בחיק הטבע. בסדרת הסרטים, נפגוש את מיפי ואת בני משפחתה השונים : הוריה, הסבים, דודה אליס, ברברה ובוריס הדובים, פופי החזיר, ועוד.','1',50)
	
	'''מספרי משימה'''
	addDir('מספרי משימה',['&youtube_pl=PLn0MlLMGvwMVJrWgO028RM6UJrax1ItDr'],17,'http://i.ytimg.com/vi/DjUCZgrL8cY/hqdefault.jpg',addonString(106000).encode('utf-8'),'1',50)
	''''''
	
	''''''
	
	''''''
	
	''''''
	
	''''''
	
	'''פים ופימבה'''
	addDir("פים ופימבה",['&youtube_pl=PLTNonj9ImqaI2F7DHlMxZ3VDn8gwpaTKe', '&youtube_pl=PLaorT66MlVdw0Ebw7cVh44jKZUQZjMbfJ'],17,'http://msc.wcdn.co.il/archive/941107-54.jpg',addonString(154).encode('utf-8'),'1',58)
	
	'''פיצי'''
	addDir('פיצי',['&youtube_pl=PL5kivPlEfMCTa3yiShQstAKsvzsdZIbkx', '&youtube_id=FKRVfhMczq8'],17,'http://i.ytimg.com/vi/Y02LzkHJ_Uk/hqdefault.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''צרלי ודודו'''
	
	''''''
	
	'''קוקו הארנב'''
	addDir('קוקו הארנב',['&youtube_pl=PLTleo-h9TFqLxJd-fvXvoQFuxMXBt8k1g', '&youtube_id=WIug1uuY3OM'],17,'http://www.luli.tv/Img/Albums/377/medium/koko.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''קטני'''
	addDir("קטני",['&youtube_pl=PLbHXbhgZi5cL97NlobjLHNtBwIA9VHcmw', '&youtube_pl=PLFdlLLQanAPDDSueGBJBwdSLnQCwdog9H'],17,'https://i.ytimg.com/vi/QS3UHEmaaaQ/default.jpg',addonString(110).encode('utf-8'),'1',58)
	
	'''קמי'''
	
	'''שבט גולו'''
	
	'''תולי האהוב'''
	
	'''תפודים קטנים'''
	
def CATEGORIES107(admin):
	
	'''עוד...'''
	list = []
	list.append('&youtube_ch=UCDfoEu-jaKsjNL6Fl0h5PUQ')
	list.append('&wallaNew2=http://nickjr.walla.co.il/')
	list.append('&wallaNew=genre%3dkids%26genreId%3d7623')
	list.append('&youtube_ch=UCQWDQwBdFVOPjvBy6mgqUQQ')
	if General_TrustedOnly != "true" or admin:
		list.append('&wallaNew=genre%3dkids%26genreId%3d7452')
		list.append('&wallaNew=genre%3dkids%26genreId%3d7453')
		list.append('&youtube_ch=UC9DU2y9iXnrI0Y5NFoBQ4RQ/playlists')
	addDir(localize(22082),list,6,addonMediaPath + 'buttonadd.png',addonString(194).encode('utf-8'),'1',50) ; list = []
	'''---------------------------'''
	
	'''אדיבו'''
	addDir(addonString(10702).encode('utf-8'),['&youtube_pl=PL_8KXLhQVQMLeDwIbMl6RyoMQiCuY7tu-', '&sdarot=season_id=1&series_id=1641&series_name=%d7%90%d7%93%d7%99%d7%91%d7%95%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1641%2fadiboo-%d7%90%d7%93%d7%99%d7%91%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91'],6,'http://www.sdarot.pm/media/series/1641.jpg',addonString(107020).encode('utf-8'),'1',50)
	
	'''בגינה של לין'''
	addDir(addonString(10705).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsDcjHMTBavJG-Rm8p0wvvW_'],17,'http://img.youtube.com/vi/lQt9W6DU5dQ/0.jpg',addonString(107110).encode('utf-8'),'1',"")
	
	'''בוב הבנאי'''
	addDir(addonString(10707).encode('utf-8'),['&youtube_pl=PL_8KXLhQVQMK80XCn7g3qVj7RwhrwiGHG'],17,'http://www.moviesforkids.co.il/images/MainCatMovies/%D7%91%D7%95%D7%91-%D7%94%D7%91%D7%A0%D7%90%D7%99.jpg',addonString(107070).encode('utf-8'),'1',50)
	
	'''בולי איש השלג'''
	list = []
	list.append('&sdarot=season_id=1&series_id=1642&series_name=%d7%91%d7%95%d7%9c%d7%99%20%d7%90%d7%99%d7%a9%20%d7%94%d7%a9%d7%9c%d7%92%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1642%2fbouli-%d7%91%d7%95%d7%9c%d7%99-%d7%90%d7%99%d7%a9-%d7%94%d7%a9%d7%9c%d7%92-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	list.append('&youtube_id=2j2ISqZ40GU')
	list.append('&youtube_id=oV_sUQa4BLE')
	list.append('&youtube_id=qi5D5LnmrYk')
	addDir(addonString(10708).encode('utf-8'),list,17,'http://www.sdarot.pm/media/series/1641.jpg',addonString(107080).encode('utf-8'),'1',50)
	
	'''ברבונסקי (רוסית)'''
	list = []
	list.append('&youtube_pl=PLogBXxHVJONDRWSpXcDV6qK9nM_WP-q_n')
	list.append('&youtube_pl=PLogBXxHVJONDRWSpXcDV6qK9nM_WP-q_n')
	list.append('&youtube_id=j4tavakwmcg')
	addDir(addonString(10709).encode('utf-8') + space + "(" + addonString(205).encode('utf-8') + ")",list,17,'https://upload.wikimedia.org/wikipedia/ru/4/4d/%D0%91%D0%B0%D1%80%D0%B1%D0%BE%D1%81%D0%BA%D0%B8%D0%BD%D1%8B.png',addonString(107090).encode('utf-8'),'1',50)
	
	'''דן הדוור'''
	addDir(addonString(10712).encode('utf-8'),['&sdarot=season_id=1&series_id=1577&series_name=%d7%93%d7%9f%20%d7%94%d7%93%d7%95%d7%95%d7%a8&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1577%2fdan-hadavar-%d7%93%d7%9f-%d7%94%d7%93%d7%95%d7%95%d7%a8' ,'&youtube_pl=PL_8KXLhQVQMK05YV3wTQ4SZyEo2kWDvNH'],6,'http://www.sdarot.pm/media/series/1577.jpg','','1',50)
	
	'''הדוד חיים'''
	addDir(addonString(10715).encode('utf-8'),['&youtube_pl=PLTNonj9ImqaIuFt2AyqdYFx6bCnKoFsIc'],17,'http://www.yap.co.il/prdPics/4298_desc3_2_2_1390119036.jpg',addonString(107150).encode('utf-8'),'1',50)
	'''---------------------------'''
	
	'''הורים וגורים'''
	addDir(addonString(10717).encode('utf-8'),['&youtube_pl=PL51YAgTlfPj5sp5nUKFuwuUddCXYjiH8F'],17,'https://i.ytimg.com/vi/2QOPSd1hKhQ/default.jpg',addonString(107200).encode('utf-8'),'1',50)
	
	'''היי בינבה'''
	list = []
	list.append('&sdarot=season_id=1&series_id=1142&series_name=%d7%94%d7%99%d7%99%20%d7%91%d7%99%d7%a0%d7%91%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1142%2fbumpety-boo-%d7%94%d7%99%d7%99-%d7%91%d7%99%d7%a0%d7%91%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	list.append('&youtube_pl=PLsCZljh6GgKUyE7rFV66powMC1H7XrXx3')
	list.append('&youtube_id=YUNtUxIc708')
	addDir(addonString(10719).encode('utf-8'),list,6,'http://www.sdarot.pm/media/series/1142.jpg',addonString(107190).encode('utf-8'),'1',50)
	
	'''הלו קיטי'''
	addDir(addonString(10721).encode('utf-8'),['&youtube_pl=PL-_BcMXVkaspyjwz7S5Hs_Rgih0F1d8_d'],17,'http://www.ligdol.co.il/Upload/hello%20kitty285.jpg',addonString(107210).encode('utf-8'),'1',50)
	
	'''הנסיכה סופיה הראשונה'''
	addDir(addonString(10722).encode('utf-8'),['&sdarot=image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1636.jpg&name=%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94%20%d7%a1%d7%95%d7%a4%d7%99%d7%94%20%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1636&series_name=%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94%20%d7%a1%d7%95%d7%a4%d7%99%d7%94%20%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1636%2fsofia-the-first-%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94-%d7%a1%d7%95%d7%a4%d7%99%d7%94-%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91"', '&youtube_pl=PLVwL64lSxWWyAUC6Bv-GAbdgQAv3CuCrr'],6,'http://upload.wikimedia.org/wikipedia/he/a/a4/%D7%94%D7%A0%D7%A1%D7%99%D7%9B%D7%94_%D7%A1%D7%95%D7%A4%D7%99%D7%94.png',addonString(107220).encode('utf-8'),'1',50)
	
	'''הסוד של מיה'''
	addDir(addonString(10723).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsCGEVOC2iJxnWNEjI13xbnA'],17,'http://msc.wcdn.co.il/w-2-1/w-300/768225-54.jpg',addonString(107230).encode('utf-8'),'1',50)
	
	'''זמן לזוז'''
	addDir(addonString(10727).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsDYbIQJMDX4usMYw7pYmPxj'],17,'http://images1.ynet.co.il/PicServer3/2012/12/04/4315826/lazooz_01.jpg',addonString(107270).encode('utf-8'),'1',50)
	
	'''יובל המבולבל'''
	addDir(addonString(10731).encode('utf-8'),['&youtube_ch=UC0r3m54hCOvyG47jzz08X2Q', '&youtube_pl=PL0495C8F5A2024FA4'],6,'http://yt3.ggpht.com/-FHcf2Rxu08A/AAAAAAAAAAI/AAAAAAAAAAA/dxzE2ng3uXI/s88-c-k-no/photo.jpg',addonString(107310).encode('utf-8'),'1',"")
	
	'''יצירה בקצרה'''
	addDir(addonString(10734).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsC0SPM0_dgOVIDn5vcCH8Ti', '&youtube_pl=PLPWc8VdaIIsD85fRihIJFTzwt9v_JX2t6'],6,'http://msc.wcdn.co.il/archive/1475513-5.jpg',addonString(107340).encode('utf-8'),'1',50)
	
	'''מולי וצומי'''
	addDir(addonString(10742).encode('utf-8'),['&youtube_pl=PLfcYs4SRZfuJHmb8y_BpUpzAsm1guoAlK'],17,'http://www.yap.co.il/prdPics/4309_desc3_2_1_1390393153.jpg',addonString(107420).encode('utf-8'),'1',50)

	'''מועדון המאפים הטובים'''
	addDir(addonString(10745).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsDUd9awquJznDcL_aSyi00T','&youtube_pl=PLPWc8VdaIIsCfrHCUj7XKDG_rvLwE9V-p'],6,'http://www.erezdvd.co.il/sites/default/files/imagecache/product_full/products/gilisip.jpg',addonString(107450).encode('utf-8'),'1',"")
	
	'''מיכל הקטנה'''
	addDir(addonString(10245).encode('utf-8'),['&youtube_pl=PLTNonj9ImqaKElCJ-4e8X_3BzXvzEYU_0'],17,'http://www.pashbar.co.il/pictures/show_big_0523173001376412565.jpg',addonString(102450).encode('utf-8'),'1',50)
	
	'''מיקי כוכבת הילדים'''
	addDir(addonString(10746).encode('utf-8'),['&youtube_id=5Zf0uSGOzlA', '&youtube_id=BKCAXKFXwEg', '&youtube_id=zGyEGXx3qkU'],17,'http://yt3.ggpht.com/-LQQaGMJh2g0/AAAAAAAAAAI/AAAAAAAAAAA/KebzcCn-y_Y/s88-c-k-no/photo.jpg',addonString(107460).encode('utf-8'),'1',50)
	
	'''מיקמק'''
	addDir(addonString(10747).encode('utf-8'),['&youtube_pl=PL663sDNTault52-VzCCu4w0CfnoAtrmRg', '&youtube_pl=PL663sDNTaulu5KpP6eyz9Xr3caOQUDEl_', '&sdarot=series_id=861&series_name=%d7%9e%d7%99%d7%a7%d7%9e%d7%a7%20%3a%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f861%2fmikmak-hasidra-%d7%9e%d7%99%d7%a7%d7%9e%d7%a7-%d7%94%d7%a1%d7%93%d7%a8%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&youtube_pl=PL663sDNTault52-VzCCu4w0CfnoAtrmRg', '&youtube_id=1CshWmAFinY', '&youtube_id=a5WNY-FMMyQ'],17,'http://www.sdarot.wf/media/series/861.jpg',addonString(107470).encode('utf-8'),'1',50)
	
	'''מר עגבניה'''
	addDir(addonString(10798).encode('utf-8'),['&youtube_pl=PLwimDnICcPKMSeyub1DLM_2jG4aPjqI7n'],17,'http://www.sdarot.wf/media/series/861.jpg',addonString(107980).encode('utf-8'),'1',50)

	'''מרתה מדברת'''
	addDir(addonString(10799).encode('utf-8'),['&youtube_pl=PL_8KXLhQVQMLtfN5bkh11lSA6Awg5rt9y'],17,'https://i.ytimg.com/vi/6kSynpNXMBs/default.jpg',addonString(107990).encode('utf-8'),'1',50)
	
	'''מר למה וגברת ככה'''
	addDir(addonString(10748).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsC8iEN7EhY46jmy93imkpHI'],17,'http://msc.wcdn.co.il/archive/1673912-35.gif',addonString(107480).encode('utf-8'),'1',"")
	
	'''משפחת יומולדת'''
	addDir(addonString(10749).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsBOUPxtM2CD7yGs1D8NCM_Z'],17,'http://msc.wcdn.co.il/archive/1620289-35.gif',addonString(107490).encode('utf-8'),'1',"")
	
	'''סיפורי פיות'''
	addDir(addonString(10755).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsD8YvtRkkqjYC5SF7TKvAcM'],17,'http://isc.wcdn.co.il/w9/skins/nick_jr/17/header_pic_2745.png',addonString(107550).encode('utf-8'),'1',"")
	
	'''סמי הכבאי'''
	addDir(addonString(10757).encode('utf-8'),['&youtube_pl=PL_TbWUH2U7KmZtYRZlJtxzmYFP_m81vSk', '&youtube_pl=PLN0EJVTzRDL-IJiTK4_B1ni8tlRNQvaBg', '&youtube_pl=PL8x83ieZ_yGXSJbCVjtUc6ZV3XWY95iEH'],6,'http://www.ligdol.co.il/Upload/hello%20kitty285.jpg',addonString(107570).encode('utf-8'),'1',"")
	
	'''עולמו הקסום של מקס'''
	addDir(addonString(10760).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsCeVQhASYBNmykK4gKh0DCe'],17,'http://images1.ynet.co.il/PicServer3/2013/07/21/4745895/max_01.jpg',addonString(107600).encode('utf-8'),'1',50)
	
	'''ערוץ הופ!'''
	addDir(addonString(10762).encode('utf-8'),['&youtube_ch=UClZXqxeY540_Epab3WDHFGw/playlists','&youtube_ch=UCfNjGgy-3XfTzgWoGMt_QOw/playlists'],6,'http://yt3.ggpht.com/-A6Z6Bj0Y5os/AAAAAAAAAAI/AAAAAAAAAAA/k-1dO4Dm0m8/s88-c-k-no/photo.jpg',addonString(107620).encode('utf-8'),'1',50)
	
	'''פליפר ולופקה'''
	list = []
	list.append('&sdarot=series_id=1153&series_name=%d7%a4%d7%9c%d7%99%d7%a4%d7%a8%20%d7%95%d7%9c%d7%95%d7%a4%d7%a7%d7%94%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1153%2fflipper-and-lopaka-%d7%a4%d7%9c%d7%99%d7%a4%d7%a8-%d7%95%d7%9c%d7%95%d7%a4%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	list.append('&youtube_pl=PLerEkB0tFW3aCqMAK0gzZkkF0QjxQx-4h')
	list.append('&youtube_pl=PLerEkB0tFW3brFpEnqz3N4vU6L4NUBQi3')
	addDir(addonString(10765).encode('utf-8'),list,6,'http://www.sdarot.pm/media/series/1153.jpg','וכבי סדרת האנימציה המדובבת לעברית, המתרחשת באי טרופי קסום ואידילי הם הדולפין פליפר והילד לופקה שהפכו לחברים טובים לאחר שפליפר הציל את לופקה מטביעה באוקיינוס.[CR]פליפר ולופקה, יחד עם החבורה האמיצה שלהם, יוצאים להרפתקאות מרתקות ונלחמים בכוחות הרוע שבראשם התמנון הענק והמרושע דקסטר ושומרי ראשו הכרישים חסרי המוח.','1',50)
	
	'''צ'פצ'ולה' - מיכל כלפון'''
	addDir(addonString(10768).encode('utf-8'),['&youtube_ch=UC64wDQFgTq9RpI1P8_p-SxA', '&youtube_id=_Jsa4Ml77-I', '&youtube_id=BduVyZALCYs', '&wallaNew=item_id%3D2728301', '&wallaNew=item_id%3D2728353'],17,'http://yt3.ggpht.com/-4Rd1GQEZnaM/AAAAAAAAAAI/AAAAAAAAAAA/pfQtiUaNjng/s88-c-k-no/photo.jpg',addonString(107680).encode('utf-8'),'1',50)
	
	'''רוי בוי'''
	addDir(addonString(10772).encode('utf-8'),['&youtube_pl=PLR7DTcU2p0Qg8pxiEld0Fg3K2Bd8gTKw5'],17,'https://i.ytimg.com/vi/9s7UMkxTIJ8/hqdefault.jpg',addonString(107720).encode('utf-8'),'1',50)
	
	'''רוני וקשיו'''
	addDir(addonString(10773).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsDPb04SHd5fzzqYt3FtmWs-','&youtube_pl=PLPWc8VdaIIsDCX6hU5b-ve2I_MRESc8FZ'],6,'http://amarganim.co.il/images_bo/%D7%A8%D7%95%D7%A0%D7%99%20%D7%95%D7%A7%D7%A9%D7%99%D7%95.jpg',addonString(107730).encode('utf-8'),'1',"")
	
	'''רינת ויויו'''
	addDir(addonString(10774).encode('utf-8'),['&youtube_pl=PLVisQUXwii8qa6lRDe1OmCIup6ylcprfc'],17,'http://media.israel-music.com/images/7290012163999.jpg',addonString(107740).encode('utf-8'),'1',"")
	
	'''שטויות בחדשות'''
	addDir(addonString(10777).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsBzxaUfj3smv1tJ8sKQXwrW'],17,'http://images1.ynet.co.il/PicServer3/2013/02/04/4440787/shtuyot_01.jpg',addonString(107770).encode('utf-8'),'1',"")
	
	'''שלדון'''
	addDir(addonString(10778).encode('utf-8'),['&youtube_pl=PL_8KXLhQVQMLzs0EHUhG_9PwxVsFgDAo4'],17,'https://i.ytimg.com/vi/6kSynpNXMBs/default.jpg',addonString(107780).encode('utf-8'),'1',50)
	
	'''שלוש ארבע לעבודה'''
	addDir(addonString(10779).encode('utf-8'),['&youtube_pl=PLPWc8VdaIIsASIzs8TcS3FFYEL68jBPWO'],17,'http://www.hll.co.il/web/8888/nsf/web/8017/%D7%A9%D7%9C%D7%95%D7%A9-%D7%90%D7%A8%D7%91%D7%A2-%D7%9C%D7%A2%D7%91%D7%95%D7%93%D7%94.jpg',addonString(107790).encode('utf-8'),'1',"")
	
	'''תותית'''
	addDir(addonString(10784).encode('utf-8'),['&youtube_pl=PLfcYs4SRZfuJgh8F-yrhcqKuQke6YbHLj', '&wallaNew=seasonId%3d2710592','&youtube_pl=PL-1E5hVd_frIjdhE0PzTB2VJr8RWgKbJ1'],17,'https://i1.ytimg.com/sh/YO96TrSN7Do/showposter.jpg?v=508e4f85',addonString(107840).encode('utf-8'),'1',50)
	
def CATEGORIES108(admin):
	
	'''בבית של פיסטוק'''
	addDir('בבית של פיסטוק',['&youtube_pl=PLN0EJVTzRDL96B86muPPFwgdymQjlwmLZ'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/6/6c/FistukLogo.jpg/250px-FistukLogo.jpg',addonString(108040).encode('utf-8'),'1',50)
	
	'''בלי סודות''' #addonString(10804).encode('utf-8')
	addDir('בלי סודות',['&youtube_pl=PL9FD9492D8C95F00F', '&youtube_pl=PL29CF6709AA760AB5'],6,'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/%D7%9C%D7%95%D7%92%D7%95_%D7%A6%D7%91%D7%A2%D7%95%D7%A0%D7%99.jpg/250px-%D7%9C%D7%95%D7%92%D7%95_%D7%A6%D7%91%D7%A2%D7%95%D7%A0%D7%99.jpg','בבית של פיסטוק היא ספין-אוף של סדרת הטלוויזיה הישראלית לילדים "רגע עם דודלי".[CR]הסדרה הופקה על ידי הטלוויזיה החינוכית במשך שתי עונות בין השנים 1981 - 1983 וכללה 29 פרקים שצולמו בעונה הראשונה בשחור-לבן (18 פרקים) ובעונה השנייה בצבע (11 פרקים). הסדרה שודרה בשידורים חוזרים לאורך כל שנות השמונים והתשעים וזכתה לפופולריות רבה בקרב ילדי ישראל.[CR]עלילת הסדרה מתמקדת בהרפתקאותיהם של פיסטוק (ספי ריבלין) וידידו רגע (ציפי מור). פיסטוק הוא אדם תמהוני חביב ומגושם המתגורר בבית קטן ומוזר על ראש גבעה ורגע הוא בובה שהפכה לילד. בנוסף, התוכנית הכילה גם פינה של בובה בשם "פלטיאל ממגדיאל" וסדרה נוספת עם בובות מהולנד בשם סיפורימפו אשר דובבו לעברית.[CR]הסדרה הופקה בתקציב נמוך משמעותית מסדרת האם "רגע עם דודלי". למעט פרקים מיוחדים היא צולמה רובה ככולה באולפני הטלוויזיה החינוכית ברמת אביב. החל מעונתה השנייה, זו הייתה ההפקה הראשונה של הטלוויזיה החינוכית שצולמה בצבע.[CR]רבים מפרקי הסדרה שצולמו בשחור-לבן נחשבים כיום לאבודים, מאחר שהטלוויזיה החינוכית מעולם לא שימרה אותם ולא העבירה אותם מהסרטים המקוריים לפורמט דיגיטלי מודרני.[CR]שיר הפתיחה של התוכנית נכתב על ידי לאה נאור, הולחן על ידי נורית הירש, ובוצע על ידי אילנית.','1',50)
	
	'''גיבורי התנ"ך'''
	addDir('גיבורי התנ"ך',['&sdarot=season_id=1&series_id=1083&series_name=%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99%20%d7%94%d7%aa%d7%a0%22%d7%9a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1083%2fgreatest-heroes-and-legends-of-the-bible-%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99-%d7%94%d7%aa%d7%a0-%d7%9a', '&youtube_pl=PLE8E08292878C59A1', '&youtube_pl=PL67F1DD7B9B45213A', '&youtube_pl=PLx1dI0IFg6RqlKwV-RPhXx_YZfDbadc7h'],6,'http://www.sdarot.pm/media/series/1083.jpg','אנתולוגיה של אירועים מפורסמים בתנ"ך.','1',50)
	
	'''גלילאו''' #addonString(10810).encode('utf-8')
	addDir('גלילאו',['&youtube_pl=PLth1a195qHsjFGXCmLtU0WZDuLq4CiWz4', '&youtube_pl=PL51YAgTlfPj6Ypxb-_Dh0eoCztCXiBYsN', '&youtube_pl=PLth1a195qHsigShKnT9DsIyKxcTBQ70Tf'],6,'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Hila_Korach.jpg/250px-Hila_Korach.jpg',addonString(108100).encode('utf-8'),'1',50)
	
	'''הופה היי'''
	addDir('הופה היי',['&youtube_pl=PL1236E31BAFB62B85'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/e/ef/Hopa_Hey.jpg/250px-Hopa_Hey.jpg','הופה היי הייתה להקה ותוכנית טלוויזיה ישראלית מצליחה לילדים ולכל המשפחה אשר הופיעה וצולמה ברחבי ישראל במהלך שנות השמונים ושנות התשעים.[CR]סדרת הטלוויזיה של הופה היי הופקה לטלוויזיה מיוני 1986 עד מאי 1995 והכילה 63 פרקים. הסדרה שודרה בערוץ הראשון במסגרת מחלקת התוכניות לילדים ונוער.[CR]בעקבות הצלחת סדרת הטלוויזיה בקרב ילדי ישראל, במהלך שנות פעילותה הופיעה הלהקה ברחבי ישראל בשמונה מופעים מצליחים והוציאה שבעה אלבומים. מוצרים נלווים נוספים של הופה היי אשר נמכרו לאורך השנים כוללים ספרים, קלטות וידאו וחטיף שוקולד.','1',50)
	
	'''היה היה'''
	addDir('היה היה',['&sdarot=season_id=1&series_id=440&series_name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%3a%20%d7%94%d7%97%d7%99%d7%99%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f440%2fonce-upon-a-time-life-%d7%94%d7%99%d7%94-%d7%94%d7%99%d7%94-%d7%94%d7%97%d7%99%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&sdarot=season_id=1&series_id=418&series_name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%3a%20%d7%94%d7%90%d7%93%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f418%2fonce-upon-a-time-man-%d7%94%d7%99%d7%94-%d7%94%d7%99%d7%94-%d7%94%d7%90%d7%93%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&sdarot=series_id=575&series_name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%3a%20%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f575%2fonce-upon-a-time-planet-earth-%d7%94%d7%99%d7%94-%d7%94%d7%99%d7%94-%d7%9b%d7%93%d7%95%d7%a8-%d7%94%d7%90%d7%a8%d7%a5-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&sdarot=season_id=1&series_id=785&series_name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%3a%20%d7%9e%d7%9e%d7%a6%d7%99%d7%90%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f785%2fonce-upon-a-time-the-discoverers-%d7%94%d7%99%d7%94-%d7%94%d7%99%d7%94-%d7%9e%d7%9e%d7%a6%d7%99%d7%90%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91', '&sdarot=season_id=1&series_id=803&series_name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%3a%20%d7%94%d7%97%d7%9c%d7%9c%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f803%2fonce-upon-a-time-space-%d7%94%d7%99%d7%94-%d7%94%d7%99%d7%94-%d7%94%d7%97%d7%9c%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91','&youtube_id=6WCaz40rvns','&youtube_id=yeReDzCnrzM','&youtube_id=Ftbsw1Bnm6U','&youtube_id=-HoFfctF_SM','&youtube_id=j53c8kOZHE4','&youtube_id=jEQWJ4yepSA','&youtube_id=bAf0wS2WHXY','&youtube_id=yybYd8d_CJc'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/0/04/Once_Upon_a_Time..._Life.jpg/250px-Once_Upon_a_Time..._Life.jpg','היה היה, היא סדרת אנימציה צרפתית לילדים אשר הופקה ב-1986 על ידי חברת ההפקות הצרפתית "פרוסידיס" של אלבר בארייה.[CR]הסדרה שודרה במקור ב-1987 בערוץ הצרפתי FR3. בישראל שודרה בדיבוב לעברית בטלוויזיה החינוכית לראשונה בסוף שנות ה-80 של המאה ה-20, ולאחר מכן בשידורים חוזרים רבים. בשנים האחרונות שודרה הסדרה בערוץ לוגי ב-HOT.[CR]התוכנית מלמדת חומר חינוכי באנימציה הומוריסטית.','1',50)
	
	'''הקומדי סטור''' #addonString(10807).encode('utf-8')
	addDir('הקומדי סטור',['&youtube_id=OnTGfthIrSE','&youtube_id=xyo6FLeZ3Aw','&youtube_id=aSke8kN719Q','&youtube_id=Ui6doOZZdgg','&youtube_id=kQ-w5sdqOZ8','&youtube_id=eyUuh89Ivi0','&youtube_id=Tciexh7ZTio','&youtube_id=bCGekFm2_w4','&youtube_id=xlbcC9iQA0M'],17,'https://upload.wikimedia.org/wikipedia/he/5/58/Komedi.jpg',addonString(108070).encode('utf-8'),'1',"")
	
	'''חידון התנך''' #10809
	addDir('חידון התנך',['&youtube_pl=PL51YAgTlfPj51ODBIMhtOF_lYxjS1cuQh'],17,'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Peresohad1985hidon.jpg/350px-Peresohad1985hidon.jpg',addonString(108090).encode('utf-8'),'1',50)
	
	'''לימוד שפה - אנגלית'''
	addDir('לימוד שפה - אנגלית',['&youtube_ch=UC43wDpoNIpAK2NYfMz1m0Ow'],9,'https://yt3.ggpht.com/-vviGyJGiPjE/AAAAAAAAAAI/AAAAAAAAAAA/kfJgGMxLQTw/s100-c-k-no/photo.jpg',addonString(110).encode('utf-8'),'1',"50")
	
	'''ערוץ החינוכית''' #addonString(10802).encode('utf-8')
	addDir('ערוץ החינוכית','UCYFLZdLRZGnmKQBH6RB8IjA/playlists',9,'https://yt3.ggpht.com/-1dd8K8gC_zQ/AAAAAAAAAAI/AAAAAAAAAAA/TI0NA67Pzv4/s100-c-k-no/photo.jpg',addonString(108020).encode('utf-8'),'1',"")
	
	'''ערוץ הילדים''' #10800
	addDir('ערוץ הילדים','UCOFp2_GttW3ljCuOc7r4l7g/playlists',9,'http://yt3.ggpht.com/-87JARv-G_rg/AAAAAAAAAAI/AAAAAAAAAAA/X9aVp9A1UiQ/s88-c-k-no/photo.jpg',addonString(108000).encode('utf-8'),'1',"")
	
	'''פרפר נחמד'''
	addDir('פרפר נחמד',['&youtube_pl=PL51YAgTlfPj7XTzORdSrWpgCfF1x7ZUeK', '&youtube_pl=PL5B247BE19DDE24D5'],6,'http://31.168.230.11/flix/buffer/thumbs/flx2202065_200611121829495450.jpg',addonString(110).encode('utf-8'),'1',50)
	
	'''קשת וענן''' #addonString(10805).encode('utf-8')
	addDir('קשת וענן',['&youtube_pl=PL51YAgTlfPj6qcpdP7e44dNj7xHuwd3oo', '&sdarot=season_id=1&series_id=1751&series_name=%d7%a7%d7%a9%d7%aa%20%d7%95%d7%a2%d7%a0%d7%9f&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1751%2fkeshet-veanan-%d7%a7%d7%a9%d7%aa-%d7%95%d7%a2%d7%a0%d7%9f'],6,'https://upload.wikimedia.org/wikipedia/he/thumb/5/56/Keshet_and_Anan_logo.jpg/250px-Keshet_and_Anan_logo.jpg',addonString(108050).encode('utf-8'),'1',50)
	
	'''ראש גדול'''
	addDir('ראש גדול',['&sdarot=series_id=572&series_name=%d7%a8%d7%90%d7%a9%20%d7%92%d7%93%d7%95%d7%9c&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f572%2frosh-gadol-%d7%a8%d7%90%d7%a9-%d7%92%d7%93%d7%95%d7%9c', '&youtube_pl=PLNMdxRa6e5t-8xyd3eFtXKIHbd6gcZPXG', '&youtube_id=2cuxr5DLnwg', '&youtube_id=TEuf9SojWug', '&youtube_id=dspu_9neTsA', '&youtube_id=syv0DjQqJQ0'],17,'http://www.sdarot.pm/media/series/572.jpg','הסדרה סובבת סביב תלמידי חטיבת ביניים טיפוסית, ופותחת צוהר אל עולמם של ילדים מרקעים שונים בגיל הייחודי שבין ילדות לבגרות.[CR]בסדרה נחשפים האלמנטים המרכזיים של חייהם: הווי בית הספר, המורים והבחינות; עולם התקשורת, המחשבים והאינטרנט; מותגים, תדמיות, וחיפוש אחר זהות אישית; מערכות היחסים עם האחים וההורים; תחילתה של עצמאות כלכלית מסוימת בגיל שבו אפשר לעבוד קצת; ובעיקר - התעוררות מהוססת וראשונית של יחסי אהבה ומשיכה לבני המין השני.','1',50)
	
	'''רגע עם דודלי''' #addonString(10806).encode('utf-8')
	addDir('רגע עם דודלי',['&youtube_pl=PL51YAgTlfPj5gUK-SIhbYyAMUQASzrZAw'],17,'https://upload.wikimedia.org/wikipedia/he/thumb/f/fe/Dodlee.jpg/250px-Dodlee.jpg',addonString(108060).encode('utf-8'),'1',50)
	
	'''שרגא בישגדא''' #addonString(10808).encode('utf-8')
	addDir('שרגא בישגאד',['&youtube_pl=PL51YAgTlfPj5KPYOntZkqg2Nwyqj2M1Lf'],17,'https://i.ytimg.com/vi/E5JQ2o84iSw/hqdefault.jpg',addonString(108080).encode('utf-8'),'1',50)
	'''---------------------------'''
	
def CATEGORIES109(admin):
	'''קטנטנים בהולנדית 1'''
	addDir(addonString(47).encode('utf-8') + space + "(" + addonString(202).encode('utf-8') + ")" + "1",'UCMf-gZNpJSPq80r9e22wl9A',9,'http://yt3.ggpht.com/-BXNeRxPOFpU/AAAAAAAAAAI/AAAAAAAAAAA/3DZSjgkhfJM/s88-c-k-no/photo.jpg',addonString(110).encode('utf-8'),'1',"")
	
	'''קטנטנים באוקראינית 1'''
	addDir(addonString(47).encode('utf-8') + space + "(" + addonString(203).encode('utf-8') + ")" + "1",'UCZAL3xoDj13SeJGTFhq00Tw',9,'http://yt3.ggpht.com/-TrrOJ-NiNys/AAAAAAAAAAI/AAAAAAAAAAA/lhx315yY5gs/s88-c-k-no/photo.jpg',addonString(110).encode('utf-8'),'1',"")
	
	'''שירים בצרפתית 1'''
	addDir(addonString(57).encode('utf-8') + space + "(" + addonString(204).encode('utf-8') + ")" + "1",'comptines',9,'https://yt3.ggpht.com/-MT6ThcO_qNI/AAAAAAAAAAI/AAAAAAAAAAA/GDibk7v0-FA/s100-c-k-no/photo.jpg',addonString(110).encode('utf-8'),'1',"")
	
	'''קטנטנים בצרפתית 1'''
	addDir(addonString(47).encode('utf-8') + space + "(" + addonString(204).encode('utf-8') + ")" + "1",'ssebastienn',9,'https://yt3.ggpht.com/-dhcbXAt2vto/AAAAAAAAAAI/AAAAAAAAAAA/hCIp6-YvL6w/s100-c-k-no/photo.jpg',addonString(188).encode('utf-8'),'1',"")
	
	'''שירים ברוסית 1'''
	addDir(addonString(57).encode('utf-8') + space + "(" + addonString(205).encode('utf-8') + ")" + "1",['&youtube_pl=PLJgmMSdWwadtTK4JzHhl5N5YR49ZVcGTK'],17,'http://www.mapsofworld.com/images/world-countries-flags/russian-federation-flag.gif',addonString(110).encode('utf-8'),'1',"")
	
	'''ערוץ החיות באנגלית'''
	addDir(addonString(65).encode('utf-8') + space + "(" + addonString(201).encode('utf-8') + ")",'UCS6hLNMMXi77SajUIvKGx5g',9,'http://yt3.ggpht.com/-9wTC-JCukjc/AAAAAAAAAAI/AAAAAAAAAAA/EqtzN1DW6HA/s88-c-k-no/photo.jpg',addonString(165).encode('utf-8'),'1',"")
	
	'''סי בייביס באנגלית'''
	addDir(addonString(63).encode('utf-8') + space + "(" + addonString(201).encode('utf-8') + ")",'UC0fXNmjDoC7ckPyT6qM8Urw',9,'http://yt3.ggpht.com/-lrofuJsz1c8/AAAAAAAAAAI/AAAAAAAAAAA/8YJ0rAktf_o/s88-c-k-no/photo.jpg',addonString(163).encode('utf-8'),'1',"")
	
	'''רחוב סומסום באנגלית'''
	addDir(addonString(62).encode('utf-8') + space + "(" + addonString(201).encode('utf-8') + ")",'UCoookXUzPciGrEZEXmh4Jjg',9,'http://yt3.ggpht.com/-Udx0C3ZTHUg/AAAAAAAAAAI/AAAAAAAAAAA/3BE1yYHQccs/s88-c-k-no/photo.jpg',addonString(162).encode('utf-8'),'1',"")
	
	'''יו-גאבה-גאבה באנגלית'''
	addDir('יו-גאבה-גאבה באנגלית','UCxezak0GpjlCenFGbJ2mpog',9,'http://yt3.ggpht.com/-DCqlRFygCMs/AAAAAAAAAAI/AAAAAAAAAAA/OmWJ9YLZviE/s88-c-k-no/photo.jpg',addonString(160).encode('utf-8'),'1',"")
	
#add_cat("דורה ודייגו", "PLqx6fN1abed4oHQ2Y5xadY-ILjzFdoMNM")
#add_cat("פסטיגל", "PLwimDnICcPKPL4MdOLIQrGDMTOAshuQ2l")
#add_cat("מיקי", "PLwimDnICcPKP4vFp6zklqeNUSdq08mN1H")

