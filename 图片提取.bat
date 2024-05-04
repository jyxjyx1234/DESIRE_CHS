setlocal

set "DIRECTORY=sysgrp"

for /R "%DIRECTORY%" %%F in (*) do (
    SysgrpConverter.exe "%%F"
)

endlocal