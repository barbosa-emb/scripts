import os, sys 

cPath = "C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb "

os.system(cPath + "devices")
os.system(cPath + "kill-server")
os.system(cPath + "tcpip 5555")
os.system(cPath + "connect 192.168.0.22")
