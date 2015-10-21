#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys
#import datetime, time
from variables import *
from shared_modules import *









def mode210(value, admin, name, printpoint):
	'''------------------------------
	---MOVE-ITEM---------------------
	------------------------------'''
	extra = "" ; TypeError = "" ; id1 = "" ; id2 = "" ; id1_ = "" ; id1__ = "" ; id1___ = "" ; id2_ = ""
	xbmc.executebuiltin('Action(Close)')
	
	try:
		id1 = property_buttonid
		if id1 == "": printpoint = printpoint + "9"
		else: test = int(id1) + 1
		id2 = value
		if id2 == "": printpoint = printpoint + "9"
		else: test = int(id2) + 2
	except Exception, TypeError:
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		printpoint = printpoint + "9"
		
	if id1 != "" and id2 != "" and id1 != id2:
		printpoint = printpoint + "1"
		includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True)
		if includes_homecontent_file_ == None: printpoint = printpoint + "8"
		else:
			'''Get current control ID'''
			printpoint = printpoint + "2"
			
			id1_ = regex_from_to(includes_homecontent_file_, '<item id="'+id1+'"','</item>', excluding=False)
			id2_ = regex_from_to(includes_homecontent_file_, '<item id="'+id2+'"','</item>', excluding=False)
	
	else: printpoint = printpoint + "9"
	
	if id1_ != "" and id2_ != "" and id1_ != id2_:
		printpoint = printpoint + "3"
		if id1_ != '<item id="'+id1+'"'+'</item>' and id2_ != '<item id="'+id2+'"'+'</item>':
			'''backup'''
			returned = copyfiles(includes_homecontent_file, skin_userdata_path+"Includes_HomeContent.xml", chmod="", mount=False)
			if returned != 'ok': printpoint = printpoint + "4"
			else:
				printpoint = printpoint + "5"
				id1__ = id1_.replace('<item id="'+id1+'"','<item id="'+id1+'9999"')
				replace_word(includes_homecontent_file,id1_,id1__)
				replace_word(includes_homecontent_file,id2_,id1_)
				replace_word(includes_homecontent_file,id1__,id2_)
				
				includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True)
				if id1__+"9999" in includes_homecontent_file_ or includes_homecontent_file_ == None or includes_homecontent_file_ == "" or not id1_ in includes_homecontent_file_ or not id2_ in includes_homecontent_file_:
					printpoint = printpoint + "9"
					copyfiles(skin_userdata_path+"Includes_HomeContent.xml",includes_homecontent_file, chmod="", mount=False)
					notification("Error occured!","Canceling...","",4000)
				else:
					printpoint = printpoint + "7"
					replace_word(includes_homecontent_file,'','', LineR=True, LineClean=True)
					
					
					mode219('1', admin, name, printpoint)
					
				ReloadSkin(admin)
	
	if not "5" in printpoint:
		'''Error'''
		notification("Error...","","",1000)
		xbmc.executebuiltin('Action(Close)')
		xbmc.executebuiltin('Action(Close)')
		xbmc.executebuiltin('ActivateWindow(1117)')
		
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "id1" + space2 + str(id1) + space + "id2" + space2 + str(id2) + newline + \
		"id1_" + space2 + str(id1_) + newline + \
		"id2_" + space2 + str(id2_) + newline + \
		"id1__" + space2 + str(id1__) + newline + \
		"id1___" + space2 + str(id1___) + newline + \
		extra
		'''---------------------------'''
	
	
def mode211(value, admin, name, printpoint):
	'''------------------------------
	---Create-New-Item---------------
	------------------------------'''
	extra = "" ; TypeError = "" ; includes_homecontent_file_ = "" ; property_buttonid_ = "" ; property_buttonid___ = "" ; new_id = "" ; new_id_ = ""
	xbmc.executebuiltin('Action(Close)')

	try:
		if value != "": test = int(value) + 1
		else:
			if property_buttonid != "": printpoint = printpoint + "9"
			else: test = int(property_buttonid) + 1
	except Exception, TypeError:
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		printpoint = printpoint + "9"
		
	if not "9" in printpoint:
		printpoint = printpoint + "1"
		includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True)
		if includes_homecontent_file_ == None: printpoint = printpoint + "8"
		else:
			'''Get current control ID'''
			printpoint = printpoint + "2"
			property_buttonid_ = regex_from_to(includes_homecontent_file_, '<item id="'+property_buttonid+'"','</item>', excluding=False)
			'''Get new control ID'''
			for i in range(100,139):
				x = xbmc.getInfoLabel('Skin.HasSetting(del'+str(i)+')')
				if x == "":
					new_id = str(i)
					new_id_ = regex_from_to(includes_homecontent_file_, '<item id="'+new_id+'"','</item>', excluding=False)
					break
				else: x = ""
					
			if new_id_ == "": printpoint = printpoint + "9" ; notification("Cannot create new buttons","Delete some first","",2000)
	
	else: printpoint = printpoint + "9"
	
	if property_buttonid_ != "" and new_id_ != "" and property_buttonid_ != new_id_:
		printpoint = printpoint + "3"
		if property_buttonid_ != '<item id="'+property_buttonid+'"'+'</item>' and new_id_ != '<item id="'+new_id+'"'+'</item>':
			'''backup'''
			returned = copyfiles(includes_homecontent_file, skin_userdata_path+"Includes_HomeContent.xml", chmod="", mount=False)
			if returned != 'ok': printpoint = printpoint + "4"
			else:
				printpoint = printpoint + "5"
				
				x2 = includes_homecontent_file_.replace(new_id_, "", 1)
				x2 = x2.replace(property_buttonid_,new_id_ + newline + "\t" + "\t" + property_buttonid_, 1)
				replace_word(includes_homecontent_file,includes_homecontent_file_,x2)

				includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True)
				if not "9999" in includes_homecontent_file_ or includes_homecontent_file_ == None or includes_homecontent_file_ == "" or not property_buttonid_ in includes_homecontent_file_ or not new_id_ in includes_homecontent_file_:
					printpoint = printpoint + "9"
					copyfiles(skin_userdata_path+"Includes_HomeContent.xml",includes_homecontent_file, chmod="", mount=False)
					notification("Error occured!","Canceling...","",4000)
				else:
					printpoint = printpoint + "7"
					replace_word(includes_homecontent_file,'','', LineR=True, LineClean=True)
					mode232(new_id, admin, name, printpoint)
					setSkinSetting('1','del'+new_id,"true")
					ReloadSkin(admin)
					
	
	if not "5" in printpoint:
		'''Error'''
		notification("Error...","","",1000)
		
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + space + "new_id" + space2 + str(new_id) + newline + \
		"property_buttonid_" + space2 + str(property_buttonid_) + newline + \
		"property_buttonid___" + space2 + str(property_buttonid___) + newline + \
		"new_id_" + space2 + str(new_id_) + newline + \
		extra
		'''---------------------------'''

def mode214(value, admin, name, printpoint):
	'''------------------------------
	---Create-New-Sub-Item-----------
	------------------------------'''
	extra = "" ; TypeError = "" ; includes_subcontent_file_ = "" ; includes_subcontent_file__ = "" ; new_id = "" ; new_id_ = ""

	try:		
		if property_buttonid == "": printpoint = printpoint + "9"
		else: test = int(property_buttonid) + 1
	except Exception, TypeError:
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		printpoint = printpoint + "9"
		
	if not "9" in printpoint:
		printpoint = printpoint + "1"
		includes_subcontent_file_ = read_from_file(includes_subcontent_file, silent=True)
		includes_subcontent_file__ = regex_from_to(includes_subcontent_file_, '<include name="SubContent_'+property_buttonid+'"','</include>', excluding=False)
		if includes_subcontent_file_ == None or includes_subcontent_file__ == '<include name="SubContent_'+property_buttonid+'"'+'</include>': printpoint = printpoint + "8"
		else:
			'''Get current control ID'''
			printpoint = printpoint + "2"
			'''Get new control ID'''
			for i in range(100,139):
				x = xbmc.getCondVisibility('Skin.HasSetting(del'+str(property_buttonid)+'_'+str(i)+')')
				if not x:
					new_id = str(i)
					new_id_ = regex_from_to(includes_subcontent_file__, '<item id="'+new_id+'"','</item>', excluding=False)
					break
				else: x = ""
					
			if new_id == "" or new_id_ == "" or new_id_ == '<item id="'+new_id+'"'+'</item>':
				printpoint = printpoint + "9" ; notification("Cannot create new buttons","Delete some first","",2000)
			else: printpoint = printpoint + "3"
	
	else: printpoint = printpoint + "9"
	
	if "3" in printpoint:
		printpoint = printpoint + "5"
	
		printpoint = printpoint + "7"
		#replace_word(includes_homecontent_file,'','', LineR=True, LineClean=True)
		mode232(new_id, admin, name, printpoint)
		setSkinSetting('1','del'+property_buttonid+'_'+new_id,"true")
					
	
	if not "5" in printpoint:
		'''Error'''
		notification("Error...","","",1000)
		
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + space + "new_id" + space2 + str(new_id) + newline + \
		"includes_subcontent_file__" + space2 + str(includes_subcontent_file__) + newline + \
		extra
		'''---------------------------'''

def mode215(value, admin, name, printpoint):
	'''------------------------------
	---Create-New-Sub-Item-----------
	------------------------------'''
	extra = "" ; TypeError = "" ; id9999_ = "" ; idpos_ = "" ; idpos__ = "" ; newid = "" ; newid_ = "" ; includes_subcontent_file_ = "" ; includes_subcontent_file__ = ""

	try:
		if property_buttonid == "": printpoint = printpoint + "9"
		else: test = int(property_buttonid) + 1
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9"
		
	if not "9" in printpoint:
		printpoint = printpoint + "1"
		includes_subcontent_file_ = read_from_file(includes_subcontent_file, silent=True)
		includes_subcontent_file__ = regex_from_to(includes_subcontent_file_, '<include name="SubContent_'+property_buttonid+'">','</include>', excluding=False)

		if includes_subcontent_file_ == None or includes_subcontent_file_ == "": printpoint = printpoint + "8"
		elif includes_subcontent_file__ == '<include name="SubContent_'+property_buttonid+'">'+'</include>':
			'''creating include'''
			idpos_ = regex_from_to(includes_subcontent_file_, '</includes','>', excluding=False)
			if idpos_ != '</includes>': printpoint = printpoint + "8"
			else:
				'''backup'''
				returned = copyfiles(includes_subcontent_file, skin_userdata_path+"Includes_SubContent.xml", chmod="", mount=False)
				if returned != 'ok': printpoint = printpoint + "4"
				else:
					printpoint = printpoint + "A"
					includes_subcontent_file__ = includes_subcontent_file__.replace('<include name','\t' + '<include name',1)
					includes_subcontent_file__ = includes_subcontent_file__.replace('</include>', newline + newline + '\t' + '</include>',1)
					replace_word(includes_subcontent_file,idpos_,includes_subcontent_file__ + idpos_)
					includes_subcontent_file_ = read_from_file(includes_subcontent_file, silent=True)
					includes_subcontent_file__ = regex_from_to(includes_subcontent_file_, '<include name="SubContent_'+property_buttonid+'"','</include>', excluding=False)
					if idpos_ in includes_subcontent_file_ and includes_subcontent_file__ != "" and includes_subcontent_file__ != '<include name="SubContent_'+property_buttonid+'"'+'</include>': printpoint = printpoint + "B"
					else:
						'''restore last saved'''
						printpoint = printpoint + "8"
						copyfiles(skin_userdata_path+"Includes_SubContent.xml",includes_subcontent_file, chmod="", mount=False)
						notification("Error occured!","Canceling...","",4000)
		if not "8" in printpoint:
			'''Get current control ID'''
			printpoint = printpoint + "2"
			
			id9999_ = regex_from_to(includes_subcontent_file_, '<item id="9999"','</item>', excluding=False)
			idpos__ = regex_from_to(includes_subcontent_file__, '</include','>', excluding=False)
			
			if id9999_ == "" or id9999_ == None or id9999_ == '<item id="9999"</item>' or idpos__ == "" or idpos__ == "None": printpoint = printpoint + "9"
			else:
				'''Get new control ID'''
				for i in range(100,109):
					x = regex_from_to(includes_subcontent_file__, '<item id="'+str(i)+'"','</item>', excluding=False)
					if x == '<item id="'+str(i)+'"'+'</item>':
						newid = str(i)
						newid_ = id9999_.replace(' id="9999"', ' id="'+str(newid)+'"')
						newid_ = newid_.replace('0000', property_buttonid)
						newid_ = newid_.replace('<visible>false</visible>',"")
						newid_ = newid_.replace('9999',str(newid))
						break
					else: x = ""
						
				if newid_ == "": printpoint = printpoint + "9" ; notification("Cannot create new buttons","Delete some first","",2000)
	
	else: printpoint = printpoint + "9"
	
	if id9999_ != "" and newid_ != "" and id9999_ != newid_ and idpos__ == '</include>':
		printpoint = printpoint + "3"
		if id9999_ != '<include name="SubContent_'+property_buttonid+'"'+'</include>' and newid_ != '<item id="'+newid+'"'+'</item>':
			'''backup'''
			returned = copyfiles(includes_subcontent_file, skin_userdata_path+"Includes_SubContent.xml", chmod="", mount=False)
			if returned != 'ok': printpoint = printpoint + "4"
			else:
				printpoint = printpoint + "5"
				newid__ = includes_subcontent_file__.replace(idpos__, newid_ + newline + '\t' + idpos__,1)
				replace_word(includes_subcontent_file,includes_subcontent_file__,newid__)
				
				includes_subcontent_file_ = read_from_file(includes_subcontent_file, silent=True)
				includes_subcontent_file__ = regex_from_to(includes_subcontent_file_, '<include name="SubContent_'+property_buttonid+'"','</include>', excluding=False)
				if includes_subcontent_file_ == None or includes_subcontent_file__ == "" or not idpos__ in includes_subcontent_file_ or not newid_ in includes_subcontent_file__:
					printpoint = printpoint + "9"
					copyfiles(skin_userdata_path+"Includes_SubContent.xml",includes_subcontent_file, chmod="", mount=False)
					notification("Error occured!","Canceling...","",4000)
				else:
					printpoint = printpoint + "7"
					replace_word(includes_subcontent_file,'','', LineR=True, LineClean=True)
					mode232(newid, admin, name, printpoint)
				ReloadSkin(admin)
	
	if not "5" in printpoint:
		'''Error'''
		notification("Error...","","",4000)
		
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonname" + space2 + str(property_buttonname) + newline + \
		"id9999_" + space2 + str(id9999_) + newline + \
		"idpos_" + space2 + str(idpos_) + newline + \
		"idpos__" + space2 + str(idpos__) + newline + \
		"newid" + space2 + str(newid) + newline + \
		"newid_" + space2 + str(newid_) + newline + \
		"includes_subcontent_file__" + space2 + str(includes_subcontent_file__) + newline + \
		extra
		'''---------------------------'''

def mode219(value, admin, name, printpoint):
	'''------------------------------
	---SET-POSITION------------------
	------------------------------'''
	extra = "" ; TypeError = "" ; extra2 = "" ; list = [] ; includes_homecontent_file_ = "" ; includes_homecontent_file__ = "" ; includes_homecontent_file___ = "" ; includes_homecontent_file__2 = "" ; x = "" ;
	from variables2 import *
	if '1' in value:
		'''main menu set position'''
		i2 = [] ; x = "" ; x_ = newline
		includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True) ; includes_homecontent_file__ = includes_homecontent_file_
		for i in range(0,60):
			x2 = ""
			includes_homecontent_file___ = regex_from_to(includes_homecontent_file__, '<item id="','</item>', excluding=False)
			if includes_homecontent_file___ != "" and includes_homecontent_file___ != '<item id="'+'</item>':
				'''level found'''
				x2 = regex_from_to(includes_homecontent_file___, '<item id="','"', excluding=True)
				if x2 != "":
					try:
						'''check if number'''
						test = int(x2) + 1
						if int(x2) in i2 or 92 in i2:
							x2 = x2 + space + "Duplicated!"
						else:
							setSkinSetting('0','pos'+x2,str(i))
							i2.append(int(x2))
					except Exception, TypeError: extra = extra + newline + "i" + space2 + str(i) + space + "TypeError" + space2 + str(TypeError)
				
				includes_homecontent_file__ = includes_homecontent_file__.replace(includes_homecontent_file___, "", 1)
				
			if admin and not admin2 and admin3 and x2 != "": x_ = x_ + newline + str(i) + space2 + "x2" + space2 + str(x2)
			
		if admin and not admin2 and admin3:
			print printfirst + name + "_LV" + space + "value" + space2 + str(value) + space + "x" + space2 + str(x) + x_ + newline + \
			"i2" + space2 + str(i2) + newline + \
			"includes_homecontent_file___" + space2 + str(includes_homecontent_file___) + newline + \
			"extra" + space2 + extra
			'''---------------------------'''
	
	if '5' in value:
		#import global
		'''main menu get position'''
		count = 0

		while count < 60 and not xbmc.abortRequested:
			x = str(posT.get(count))
			#if str(count) in posT:
			if x != None:
				if count in list:
					'''duplicated'''
					x = x + space + "duplicated!"
				else:
					#x = posT[str(count)]
					#x = str(posT.get(str(count)))
					list.append(x)
			else: x = x + 'error!'
			
			try: list_ = str(list[count])
			except: list_ = ""
			if admin and not admin2 and admin3: extra2 = extra2 + newline + "count" + space2 + str(count) + space + "x" + space2 + str(x) + space + "list[count]" + space2 + list_
			count += 1
			
		if admin and not admin2 and admin3: 
			print printfirst + name + "_LV" + printpoint + newline + \
			extra2 + newline + \
			"list" + space2 + str(list) + newline + \
			"posT" + space2 + str(posT)
		
		extra2 = ""
		x = ""
		
	if '2' in value:
		'''main menu restore position'''
		if list == []: printpoint = printpoint + "9"
		else:
			includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True)
			includes_homecontent_file__ = regex_from_to(includes_homecontent_file_, '<include name="Content_Home">','</include>', excluding=False) #New lineup
			includes_homecontent_file__2 = includes_homecontent_file__ #New lineup Compare
			includes_homecontent_file___ = regex_from_to(includes_homecontent_file_, '<include name="Content_Home">','</include>', excluding=True)
			if includes_homecontent_file__ != "" and includes_homecontent_file__ != '<include name="Content_Home">'+'</include>' and includes_homecontent_file___ != "":
				printpoint = printpoint + "2"
				id_9999 = regex_from_to(includes_homecontent_file__, '<item id="9999"','</item>', excluding=False)
				count = 0
				for i in range(0,60):
					try:
						x = list[count]
						#x = str(posT.get(count))
						if 'pos' in x:
							x = x.replace('pos',"")
							test = int(x) + 1
						else: x = "Error"
						
					except: x = "Error"
					
					if x != "" and x != "Error":
						x2 = regex_from_to(includes_homecontent_file__, '<item id="'+str(x)+'"','</item>', excluding=False)
						if x2 != "" and x2 != '<item id="'+str(x)+'"''</item>':
							'''level found'''
							includes_homecontent_file__ = includes_homecontent_file__.replace(id_9999, newline + '\t' + '\t' + x2 + newline + id_9999, 1)
							#includes_homecontent_file__ = includes_homecontent_file__.replace('\t' + '\t' + x2, "", 1)
							includes_homecontent_file__ = includes_homecontent_file__.replace(x2, "", 1)
							includes_homecontent_file___ = includes_homecontent_file___.replace(x2, "", 1)
						else: x = "Error"
					
					if admin and not admin2 and admin3:
						extra2 = extra2 + newline + "count" + space2 + str(count) + space + "i" + space2 + str(i) + space + "x" + space2 + str(x) + \
						space + \
						newline + "x2" + space2 + str(x2) + newline + "includes_homecontent_file__" + space2 + str(includes_homecontent_file__)
					count += 1
					
				if includes_homecontent_file___ != "" and 1 + 1 == 2:
					'''add unpositions items'''
					printpoint = printpoint + "3"
					includes_homecontent_file___2 = includes_homecontent_file___ #FOR DEBUG
					y2 = regex_from_to(includes_homecontent_file___, '<item id="','</item>', excluding=False)
					count2 = 0
					while count2 < 60 and y2 != '<item id="'+'</item>' and y2 != "" and not xbmc.abortRequested:
						includes_homecontent_file__ = includes_homecontent_file__.replace(id_9999, newline + '\t' + '\t' + y2 + newline + id_9999, 1)
						includes_homecontent_file__ = includes_homecontent_file__.replace('\t' + '\t' + y2 + newline,"", 1)
						includes_homecontent_file___ = includes_homecontent_file___.replace(y2,"")
						y2 = regex_from_to(includes_homecontent_file___, '<item id="','</item>', excluding=False)
					
				'''backup'''
				returned = copyfiles(includes_homecontent_file, skin_userdata_path+"Includes_HomeContent.xml", chmod="", mount=False)
				if returned != 'ok': printpoint = printpoint + "4"
				else:
					printpoint = printpoint + "5"
					includes_homecontent_file__ = includes_homecontent_file__.replace(id_9999, '\t' + '\t' + id_9999, 1) #ADD SPACE
					replace_word(includes_homecontent_file,includes_homecontent_file__2,includes_homecontent_file__)
					replace_word(includes_homecontent_file,'','', LineR=True, LineClean=True)
					
					includes_homecontent_file_ = read_from_file(includes_homecontent_file, silent=True)
					includes_homecontent_file__ = regex_from_to(includes_homecontent_file_, '<include name="Content_Home">','</include>', excluding=False) #New lineup
					
					z1 = len(includes_homecontent_file__)
					z2 = len(includes_homecontent_file__2)

					if not '</include>' in includes_homecontent_file__ or int(z1) - int(z2) > 10 or int(z1) - int(z2) > 10:
						printpoint = printpoint + "9"
						copyfiles(skin_userdata_path+"Includes_HomeContent.xml",includes_homecontent_file, chmod="", mount=False)
						notification("Error occured!","Canceling...","",4000)
					else:
						printpoint = printpoint + "7"
						ReloadSkin(admin)
						
			else: printpoint = printpoint + "9"
			
			if admin and not admin2 and admin3:
				print printfirst + name + "_LV" + printpoint + space + newline + \
				'lenincludes_homecontent_file__' + space2 + str(len(includes_homecontent_file__)) + space + 'lenincludes_homecontent_file__2' + space2 + str(len(includes_homecontent_file__2)) + newline + \
				extra2 + newline + \
				"includes_homecontent_file__" + space2 + str(includes_homecontent_file__) + newline + \
				"includes_homecontent_file__2" + space2 + str(includes_homecontent_file__2) + newline + \
				"includes_homecontent_file___" + space2 + str(includes_homecontent_file___) + newline + \
				"includes_homecontent_file___2" + space2 + str(includes_homecontent_file___2)


				
def mode216(value, admin, name, printpoint):
	'''------------------------------
	---REMOVE-SUB-ITEM---------------
	------------------------------'''
	extra = "" ; TypeError = "" ; includes_subcontent_file_ = "" ; includes_subcontent_file__ = "" ; property_subbuttonid_ = ""
	xbmc.executebuiltin('Action(Close)')
	
	try:
		if property_buttonid == "" or property_subbuttonid == "": printpoint = printpoint + "9"
		else: test = int(property_buttonid) + 1 ; test = int(property_subbuttonid) + 1	
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9"
		
	if not "9" in printpoint:
		printpoint = printpoint + "1"
		includes_subcontent_file_ = read_from_file(includes_subcontent_file, silent=True)
		includes_subcontent_file__ = regex_from_to(includes_subcontent_file_, '<include name="SubContent_'+property_buttonid+'"','</include>', excluding=False)
		if includes_subcontent_file_ == None or includes_subcontent_file__ == "": printpoint = printpoint + "8"
		else:
			'''Get current control ID'''
			printpoint = printpoint + "2"
			
			property_subbuttonid_ = regex_from_to(includes_subcontent_file__, '<item id="'+property_subbuttonid+'"','</item>', excluding=False)
					
			if property_subbuttonid_ == "": printpoint = printpoint + "9" ; notification("Cannot remove button","Contact HTPT team","",2000)
	
	else: printpoint = printpoint + "9"
	
	if property_subbuttonid_ != "":
		printpoint = printpoint + "3"
		if property_subbuttonid_ != '<item id="'+property_subbuttonid+'"'+'</item>':
			xbmc.sleep(100) ; returned = dialogyesno("Remove Item" + space2 + str(property_subbuttonname), "Choose YES to Remove Item")
			if returned == 'skip': printpoint = printpoint + "8"
			else:
				'''backup'''
				returned = copyfiles(includes_subcontent_file, skin_userdata_path+"Includes_SubContent.xml", chmod="", mount=False)
				if returned != 'ok': printpoint = printpoint + "4"
				else:
					printpoint = printpoint + "5"
					
					replace_word(includes_subcontent_file,property_subbuttonid_,"")
					
					includes_subcontent_file_ = read_from_file(includes_subcontent_file, silent=True)
					includes_subcontent_file__ = regex_from_to(includes_subcontent_file_, '<include name="SubContent_'+property_buttonid+'"','</include>', excluding=False)
					if property_subbuttonid_ in includes_subcontent_file__ or not "9999" in includes_subcontent_file_ or not '<include name="SubContent_'+property_buttonid+'"' in includes_subcontent_file_:
						printpoint = printpoint + "9"
						copyfiles(skin_userdata_path+"Includes_SubContent.xml",includes_subcontent_file, chmod="", mount=False)
						notification("Error occured!","Canceling...","",4000)
					else:
						setSkinSetting('1',"sub" + property_buttonid + "_" + property_subbuttonid,"false")
						setSkinSetting('0',"sublabel" + property_buttonid + "_" + property_subbuttonid,"")
						setSkinSetting('0',"subaction" + property_buttonid + "_" + property_subbuttonid,"")
						printpoint = printpoint + "7"
						replace_word(includes_subcontent_file,'','', LineR=True, LineClean=True)
					#ReloadSkin(admin)
	
	if not "5" in printpoint and not "8" in printpoint:
		'''Error'''
		notification("Error...","","",1000)
		
	if admin and not admin2 and admin3:
		print printfirst + name + "_LV" + printpoint + space + "value" + space2 + str(value) + space + "property_buttonname" + space2 + str(property_buttonname) + space + "property_subbuttonname" + space2 + str(property_subbuttonname) + space + newline + \
		"property_buttonid" + space2 + str(property_buttonid) + space + "property_subbuttonid_" + space2 + str(property_subbuttonid_) + newline + \
		"property_subbuttonid_" + space2 + str(property_subbuttonid_) + newline + \
		"includes_subcontent_file__" + space2 + str(includes_subcontent_file__) + newline + \
		extra
		'''---------------------------'''
		




		
