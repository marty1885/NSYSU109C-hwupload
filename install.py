#!/usr/bin/python3
import os

if os.name == 'nt':
	os.system("copy uploadhw.py C:\\windows\\system32\\uploadhw.py")
else:
	os.system("cp uploadhw.py /usr/bin/uploadhw.py")
	
print("Install success!")
