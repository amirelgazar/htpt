#!/bin/bash

if [ -d "/storage/emulators" ]; then
	rm -fr /storage/emulators
	echo removing /storage/emulators
fi

if [ -d "/storage/.kodi/userdata/addon_data" ]; then
	rm -fr /storage/.kodi/userdata/addon_data/plugin*
	echo removing /storage/.kodi/userdata/addon_data/plugin*
fi

if [ -d "/storage/.kodi/addons" ]; then
	rm -fr /storage/.kodi/addons/plugin*
	echo removing /storage/.kodi/addons/plugin*
fi

df -h | grep "/var/media/" | awk {'print $2,$6'} | awk {'print substr($2, 12, length($2)-1)'} | tee /storage/externalusb.log
TOTALUSB=`wc -l /storage/externalusb.log | grep -o '[0-9]*'` #ls /var/media -1 | wc -l
USB1=`head -1 /storage/externalusb.log`
USB2=`sed -n 2p /storage/externalusb.log`
USB3=`sed -n 3p /storage/externalusb.log`
if [ $TOTALUSB -gt 0 ]; then
	rm -fr /var/media/$USB1/*
	echo removing /var/media/$USB1/*
	if [ $TOTALUSB -gt 1 ]; then
		rm -fr /var/media/$USB2/*
		echo removing /var/media/$USB2/*
		if [ $TOTALUSB -gt 2 ]; then
			rm -fr /var/media/$USB3/*
			echo removing /var/media/$USB3/*
		fi
	fi
fi
