"""
Author: Ricardo Cruell
Date Last Revised: 10/13/2014
Lang.: Python
"""

import sys
from xlrd import open_workbook, cellname
import xlrd
import datetime
#from datetime import datetime, timedelta
from xlwt import Workbook
import xlwt
from tempfile import TemporaryFile

# open Excel file and acquire the first sheet
workbook = open_workbook('PHARMA OCT 12 FOR KW SEARCH.xlsx')
worksheet = workbook.sheet_by_index(0)

# create Excel file to write to
book = Workbook()
sheet1 = book.add_sheet('KW SEARCH',cell_overwrite_ok=True)

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
				date = worksheet.cell(row_index, 0).value
				datetime_value = xlrd.xldate_as_tuple(date, 0)
				dates = str(datetime_value[1]) + '/' + str(datetime_value[2]) + '/' + str(datetime_value[0])
				if datetime_value[4] < 10:
					time = str(datetime_value[3]) + ':0' + str(datetime_value[4])
				else:
					time = str(datetime_value[3]) + ':' + str(datetime_value[4])
				timestamp = str(dates)# + '  ' + str(time)
				sheet1.write(i,0,word)
				#final = timestamp + '  [' + worksheet.cell(row_index,1).value + ']  ' + worksheet.cell(row_index, 2).value
				sheet1.write(i,1,timestamp)
				final = '[' + worksheet.cell(row_index,1).value + ']  ' + worksheet.cell(row_index, 2).value
				sheet1.write(i,2,final)
				i = i + 1
		except AttributeError:
			print "There is an error occurring on row: "
			print (row_index+1)

filename = 'KW SEARCH ON ' + str(datetime.date.today()) + ' .xlsx'
book.save(filename)
book.save(TemporaryFile())