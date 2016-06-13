'''
    check_dup.py

    - Checks whether the two given files are the same file by computing md5sums of the files in chunks

    Usage:
        python check_dup.py -f1 [file 1 path] -f2 [file 2 path]
'''

import hashlib, argparse, sys

known_files = {}

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def compare(fname1, fname2):
	''' Takes in 2 files, compares whether they're same using md5 hashsum'''
	return md5(fname1) == md5(fname2)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f1', help='File 1')
	parser.add_argument('-f2', help='File 2')
	values = parser.parse_args()
	if (not (values.f1 and values.f2)):
		print 'Specify both files to compare'
		sys.exit(1)

	if compare(values.f1, values.f2):
		print 'Match'
	else:
		print 'No match'
