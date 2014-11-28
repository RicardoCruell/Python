import sys
from xlrd import open_workbook, cellname
import xlrd
from datetime import datetime
from xlwt import Workbook
import xlwt
from tempfile import TemporaryFile

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

# open Excel file and acquire the first sheet
workbook = open_workbook('animateme.xlsx')
worksheet = workbook.sheet_by_index(0)

#init counter
count = 0

#init x and y arrays for axis vals
x = []
y = []

# grab first value; dates in datetime format
cmp = worksheet.cell(0, 1).value
for row_index in range(worksheet.nrows):
    if cmp == worksheet.cell(row_index,1).value:
        count = count + 1
    else:
        x.append(cmp)
        y.append(count)
        cmp = worksheet.cell(row_index,1).value
        count = 1

# reverse order of x to chronological
x.reverse()
y.reverse
# create list of FORMATTED dates
dts = []
for i in range(len(x)):
    dts.append(datetime.strptime(x[i],'%m/%d/%Y'))
#print dts
#convert the dates into usable "floats"
fig, ax = plt.subplots()
#ax=plt.gca()

ax.xaxis_date()
datenums=matplotlib.dates.date2num(dts)
t0 = datenums[0]
t1 = datenums[len(datenums)-1]
#prep graph axis for dates, including proper date format
xfmt = matplotlib.dates.DateFormatter('%m/%d/%Y')
ax.xaxis.set_major_formatter(xfmt)

ax.autoscale_view()

#t = ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
#           [1,0,4,7,9,1,5,2,1,3,23,12,34,23,43,32,21])
t = (datenums,y)
q=np.array(t)
print t
print datenums[0]
print dts[0]
#fig, ax = plt.subplots()
line, = ax.plot([], [], 'g-')

plt.xlim(t0,t1)
plt.ylim(0, max(y))
plt.xlabel('Date')
plt.ylabel('# of Tweets')
plt.title('FILE')
#plt.plot_date(datenums, y, tz=None, xdate=False)

def update_line(num, q, line):
    line.set_data(q[...,:num])
    return line,


	
line_ani = animation.FuncAnimation(fig, update_line, 200, fargs=(q, line),
     blit=False)

#line_ani.save('lines.mp4')

plt.show()