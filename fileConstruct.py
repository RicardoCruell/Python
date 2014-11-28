import sys
import fileinput

files = ['tweet1.txt','tweet2.txt','tweet3.txt','tweet4.txt','tweet5.txt','tweet6.txt','tweet7.txt','tweet8.txt','tweet9.txt']
newFile = 'tweetsAll.txt'
with open(newFile, 'w') as fout:
	for line in fileinput.input(files):
		fout.write(line)