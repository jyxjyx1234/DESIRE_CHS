py 图像处理\bmp_process1.py
py 图像处理\bmp_process2.py
py 图像处理\bmp_process3.py

for /R sysgrp_bmpout %%F in (*.bmp) do (
    SysgrpConverter.exe "%%F"
)

del /Q sysgrp_out\*.*

move sysgrp_bmpout\*.out sysgrp_out\

set "folder_path=sysgrp_out"

for %%F in ("%folder_path%\*.out") do (
    ren "%%F" "%%~nF"
)
for %%F in ("%folder_path%\*.bmp") do (
    ren "%%F" "%%~nF"
)
del sysgrp_out.rar
Rar>nul 2>nul a -m3 sysgrp_out.rar sysgrp_out\*