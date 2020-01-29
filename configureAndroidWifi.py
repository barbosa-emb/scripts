import os, sys 

os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb devices")
os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb kill-server")
os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb tcpip 5555")
os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb connect 192.168.0.22")
