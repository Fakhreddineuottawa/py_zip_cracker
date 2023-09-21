#!/usr/bin/python
import zipfile
import argparse

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password.encode('utf-8'))
		print ("[+] Found password = " + password)
		return True
	except:
		return False

def main():
	parser = argparse.ArgumentParser("%prog -f <zipfile> -d <dictionary>")
	parser.add_argument("-f", dest="zname", help="specify zip file")
	parser.add_argument("-d", dest="dname", help="specify dictionary file")
	args = parser.parse_args()

	if (args.zname == None):
		print (parser.usage)
		exit(0)
	elif (args.dname == None):
		zname = args.zname
		dname = 'passwords.txt'
	else:
		zname = args.zname
		dname = args.dname
    
	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)
	variabl = False

	for line in passFile.readlines():
		password = line.strip("\n")
		found = extractFile(zFile, password)
		# Exit if password found
		if found :
			variabl = True
			break
	if (variabl == False)	:print('[-] Password not found.')

if __name__ == "__main__":
	main()
