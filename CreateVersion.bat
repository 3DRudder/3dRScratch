rd /s /q dist
del install\3dRScratch.7z
del install\3dRScratchServer.exe
pyinstaller 3dRScratch.py
"c:\Program Files\7-Zip\7z.exe" a -r -t7z Install\3dRScratch.7z "dist\3dRScratch\*.*"
cd install
copy /b 7zS.sfx + config.txt + 3dRScratch.7z 3dRScratchServer.exe
signtool sign /a /sha1 298F2A4C32C4A958AF4952C057C8C8E1F47EF77F /tr http://timestamp.globalsign.com/?signature=sha2 /td SHA256 3dRScratchServer.exe
cd ..
