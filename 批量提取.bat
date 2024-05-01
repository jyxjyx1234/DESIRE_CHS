setlocal

set "DIRECTORY=ORI_FILE"

for /R "%DIRECTORY%" %%F in (*) do (
    ScriptDecoder.exe "%%F"
)

endlocal