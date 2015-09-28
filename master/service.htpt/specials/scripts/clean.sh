#!/bin/bash

TEMP_PATH=$HOME/.kodi/temp
TEMP_PATH2=/storage/.kodi/temp
NONE=""
SKIP1=".log"
SUM1=0
for i in $TEMP_PATH/*; do
	echo I:  $i
	i2="$(echo $i | sed -e 's/\/storage\/.kodi\/temp\///g')" #REPLACE VARIABLE
	#i2=$i-$TEMP_PATH
	#i2=`echo $i | grep -v 'storage[^ ]'`
	#i2=`sed -r "s/$TEMP_PATH/$NONE/g" echo $i`
	#x="$(echo $x | sed 's/:/ /g')"
	echo I2: $i2
	
	if [ "$i2" != "${i2%$SKIP1*}" ]; then #FIND STRING IN STRING
		#if ".log" in $i2; then
		echo ".log found in " $i2 "NOT DELETED!"
	else
		rm -rf $i
		SUM1=`echo $(($SUM1+1))` #SUM +1
	fi
done
echo "TOTAL DELETED:" $SUM1
#rm -rf $TEMP_PATH