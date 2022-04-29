# Stockholm
A small ransomware program that affects a directory called "infection" in your /home.
The program will act only on files with the extensions that were affected by Wannacry 
and will encrypt and rename all the files in the mentioned folder adding the ".ft" extension.

Algorithm used: AES

# Usage:

[] Normal mode:
python3 stockholm.py

[-h] help flag:
show help message and exits

[-v] version flag:
displays program version

[-r] reversee flag:
decreypts the encrypted files

[-s] silent mode
