import os
import subprocess

command_1 = "ls /home/eduardo/media/"
result = subprocess.check_output(command_1, stderr=subprocess.STDOUT, shell=True)
list = str(result.decode('utf-8')).split('\n')

for i in list:
	input = i
	output = "output/" + i
	if(len(input) > 0):
		command_2 = "ffmpeg -i " + input + " -c:v copy -c:a libmp3lame -q:a 2 -map 0 -map -0:a:0 -map -0:a:1 -map 0:a:0 -map 0:a:1 " + output
		os.system(command_2)
		command_3 = "rm -rvf " + input
		os.system(command_3)
		print(input)
		print(output)
