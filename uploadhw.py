#!/usr/bin/python3

from ftplib import FTP
import sys

developmentMode = False

def connectToFTP():
	ftp = FTP()
	if not developmentMode:
		ftp = FTP("140.117.168.12")
		ftp.login("stu","105stu")
	else:
		ftp.connect("localhost",2121)
		ftp.login("test","passwd")
	return ftp;

def openFile(filePath):
	try:
		f = open(filePath,'rb')
		return f
	except IOError:
		print("Error: cannot open file *{0}*".format(filePath))
		return False


ftp = connectToFTP()

#TODO : parse args instead of hard coding it
hwName = sys.argv[1]
stuID = sys.argv[2]
filePath = sys.argv[3]

ftp.cwd(hwName)

uploadFile = openFile(filePath)
if uploadFile == False:
	ftp.quit()
	exit()

uploadFileName = stuID + ".cpp"

#ftp.retrlines('LIST') 

currentDirFileList = ftp.nlst()
index = 1
while uploadFileName in currentDirFileList:
	uploadFileName =  stuID + "_" + str(index) + ".cpp"
	index = index + 1

ftp.storlines("STOR " + uploadFileName, uploadFile)

print("Successfully uploaded. File revition : {0}".format(index))

ftp.quit()
