import os, sys 

print(os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb devices"))
print(os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb kill-server"))
print(os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb tcpip 5555"))
print(os.system("C:/Users/DTI001/AppData/Local/Android/SDK/platform-tools/adb connect 192.168.0.22"))
