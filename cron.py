import os.path
if not os.path.isfile("data.txt"):
	f = open("data.txt","w")
	f.write("1 1\n")
	f.close()

f = open("data.txt","r")
month,year = f.readline().split()

bashCommand = 'defaults write com.apple.desktop Background \'{default = {ImageFilePath = "~/apps/l-cal/images/t-test_'+year+'_'+month+'.jpeg"; };}\';killall Dock'
import subprocess
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
output = process.communicate()[0]

month = int(month)
year = int(year)

month += 1
if month > 12:
	month = 1
	year += 1

f.close()
f = open("data.txt","w")
f.write(str(month)+" "+str(year))