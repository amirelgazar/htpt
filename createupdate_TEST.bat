@echo off
SET cc=%cd%
SET skin="skin.htpt"
SET service="service.htpt"
SET servicefix="service.htpt.fix"
SET servicehelp="service.htpt.help"
SET widgets="script.htpt.widgets"
SET refresh="script.htpt.refresh"
SET homebuttons="script.htpt.homebuttons"
SET smartbuttons="script.htpt.smartbuttons"
SET debug="script.htpt.debug"
SET install="script.htpt.install"
SET remote="script.htpt.remote"
SET emu="script.htpt.emu"
SET kids="plugin.video.htpt.kids"
SET gopro="plugin.video.htpt.gopro"
SET music="plugin.video.htpt.music"

SET repository="repository.htpt"

if exist Z:\addons\%smartbuttons% xcopy Z:\addons\%smartbuttons% %cc%\%smartbuttons% /s /i /y /EXCLUDE:excludelist1.txt >NUL

exit


if exist Z:\addons\%debug% xcopy Z:\addons\%debug% %cc%\%debug% /s /i /y /EXCLUDE:excludelist1.txt >NUL
if exist Z:\addons\%install% xcopy Z:\addons\%install% %cc%\%install% /s /i /y /EXCLUDE:excludelist1.txt >NUL
if exist Z:\addons\%remote% xcopy Z:\addons\%remote% %cc%\%remote% /s /i /y /EXCLUDE:excludelist1.txt >NUL
if exist Z:\addons\%emu% xcopy Z:\addons\%emu% %cc%\%emu% /s /i /y /EXCLUDE:excludelist1.txt >NUL
if exist Z:\addons\%widgets% xcopy Z:\addons\%widgets% %cc%\%widgets% /s /i /y /EXCLUDE:excludelist1.txt >NUL

echo COPYING %kids% and %gopro% and %music%...
if exist Z:\addons\%kids% xcopy Z:\addons\%kids% %cc%\%kids% /s /i /y /EXCLUDE:excludelist1.txt >NUL
if exist Z:\addons\%gopro% xcopy Z:\addons\%gopro% %cc%\%gopro% /s /i /y /EXCLUDE:excludelist1.txt >NUL
if exist Z:\addons\%music% xcopy Z:\addons\%music% %cc%\%music% /s /i /y /EXCLUDE:excludelist1.txt >NUL

echo COPYING %repository%...
if exist Z:\addons\%repository% xcopy Z:\addons\%repository% %cc%\%repository% /s /i /y /EXCLUDE:excludelist1.txt >NUL

echo COPYING TEMP TO %skin%...
if exist %cc%\temp\ xcopy %cc%\temp %cc%\%skin% /s /i /y >NUL
if exist %cc%\temp\ rmdir %cc%\temp\ /s /q
if exist %cc%\%skin%\changelog.txt copy %cc%\%skin%\changelog.txt %cc%\changelog_he.txt /Y >NUL
if exist %cc%\%skin%\changelog_en.txt copy %cc%\%skin%\changelog_en.txt %cc%\changelog_en.txt /Y >NUL

echo RUNNING repo_prep.py
python %cc%\repo_prep.py
pause