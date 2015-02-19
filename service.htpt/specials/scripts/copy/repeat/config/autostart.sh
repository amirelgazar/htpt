#!/bin/sh
#chmod 644 $HOME/.config/autostart.sh ###ORIGNAL 644?###
#chmod +x $HOME/.config/autostart.sh ###ORIGNAL 644?###
ADDON_DIR=$HOME/.kodi/addons/emulator.retroarch
LD_LIBRARY_PATH=$ADDON_DIR/lib
SKIN_PATH=$HOME/.kodi/addons/skin.htpt
SERVICE_PATH=/storage/.kodi/addons/service.htpt
HOMEBUTTONS_PATH=/storage/.kodi/addons/script.htpt.homebuttons
REMOTE_PATH=/storage/.kodi/addons/script.htpt.remote
USERDATA=/storage/.kodi/userdata
USERDATA_PATH3=$HOME/.kodi/userdata/addon_data/skin.htpt/userdata

chmod +x $ADDON_DIR/bin/*
chmod +x $LD_LIBRARY_PATH/*
export LD_LIBRARY_PATH

chmod 766 $USERDATA/addon_data/plugin.video.genesis/settings.xml
chmod +x $SKIN_PATH/specials/scripts/*
chmod +x $SERVICE_PATH/specials/scripts/*
chmod +x $HOMEBUTTONS_PATH/specials/scripts/*
chmod +x $REMOTE_PATH/*
chmod +x $USERDATA_PATH3/*

$HOME/.kodi/addons/skin.htpt/specials/scripts/copy.sh

$REMOTE_PATH/remote.sh
#killall eventlircd
#ir-keytable -s rc0 -p NEC -t
#You can see if autostart.sh is executed from /var/log/messages file.
echo `(date)` >> /storage/autostart.log