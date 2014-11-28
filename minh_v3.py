"""
Author: Ricardo Cruell
Date Last Revised: 10/13/2014
Lang.: Python
"""

import sys
from xlrd import open_workbook, cellname
from xlwt import Workbook
from tempfile import TemporaryFile

# open Excel file and acquire the first sheet
#workbook = open_workbook('KW SAMPLE FILE.xlsx')
workbook = open_workbook('PHARMA OCT 12 FOR KW SEARCH.xlsx')

worksheet = workbook.sheet_by_index(0)

# create Excel file to write to
book = Workbook()
sheet1 = book.add_sheet('SAMPLE OUPUT',cell_overwrite_ok=True)

# Gather, strip, and create a list of the keywords we're searching for
KW = ()
with open('KW.txt', 'r') as f:
	K = f.read()

# change all keywords to lowercase interpretation
# split string that was read in at each newline char
KW = K.lower().split("\n")

# For every Keyword starting at the third column, look for a 
# matching word in that string
i = 0
for word in KW:
	for row_index in range(worksheet.nrows):
		# Something is causing an AttributeError; Redirect it to error.txt file
		try:
			if word in worksheet.cell(row_index, 2).value.lower():
				sheet1.write(i,0, word)
				sheet1.write(i,1,worksheet.cell(row_index, 1).value)
				sheet1.write(i,2,worksheet.cell(row_index, 2).value)
				i = i + 1
		except AttributeError:
			print "There is an error occurring on row: "
			print (row_index+1)

book.save('SAMPLE OUTPUT.xlsx')
book.save(TemporaryFile())