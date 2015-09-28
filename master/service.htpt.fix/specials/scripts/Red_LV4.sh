#!/bin/bash

if [ -d "/storage/emulators" ]; then
	rm -fr /storage/emulators
	echo removing /storage/emulators
fi

if [ -d "/storage/.kodi/userdata/addon_data/plugin.program.advanced.launcher" ]; then
	rm -fr /storage/.kodi/userdata/addon_data/plugin.program.advanced.launcher
	echo removing /storage/.kodi/userdata/addon_data/plugin.program.advanced.launcher
fi

if [ -d "/storage/.kodi/addons/plugin.program.advanced.launcher" ]; then
	rm -fr /storage/.kodi/addons/plugin.program.advanced.launcher
	echo removing /storage/.kodi/addons/plugin.program.advanced.launcher
fi

if [ -d "/storage/.kodi/addons/script.htpt.emu" ]; then
	rm -fr /storage/.kodi/addons/script.htpt.emu
	echo removing /storage/.kodi/addons/script.htpt.emu
fi

if [ -d "/storage/.kodi/userdata/addon_data/script.htpt.emu" ]; then
	rm -fr /storage/.kodi/userdata/addon_data/script.htpt.emu
	echo removing /storage/.kodi/userdata/addon_data/script.htpt.emu
fi
