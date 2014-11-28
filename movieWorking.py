import sys
import re
import datetime as dt

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

# open Excel file and acquire the first sheet
# workbook = open_workbook('animateme.xlsx')
# worksheet = workbook.sheet_by_index(0)

#init counter
count = 0

#init x and y arrays for axis vals
x = []
y = []

lines = []
date = []

with open('tweetsAll.txt', 'r') as f:
    lines = f.read()

# strip all dates from the supplied file
text = lines.split("\n")
dateFormat = '\d{4}-\d{2}-\d{2}'
for s in text:
    match = re.search(dateFormat.decode('utf-8'), s)
    if match:
        date.append(dt.datetime.strptime(match.group(), '%Y-%m-%d').date())
    else:
        print "no match on for:  " + s 
        continue

date.sort()
print date[0]
print date[len(date)-1]
"""Are we obtaining correctly formatted data?"""
# for i in range(len(date)):
    # print date[i]

i = 0
temp = date[0]
for i in range(len(date)):
    if temp == date[i]:
        count = count + 1
        i = i + 1
    else:
        x.append(temp)
        y.append(count)
        temp = date[i]
        count = 1

print x
print y

# create list of FORMATTED dates
# dts = []
# for i in range(len(x)):
    # dts.append(datetime.strptime(x[i],'%m/%d/%Y'))
#print dts
#convert the dates into usable "floats"
fig, ax = plt.subplots()
# #ax=plt.gca()

ax.xaxis_date()
datenums = matplotlib.dates.date2num(x)
t0 = datenums[0]
t1 = datenums[len(datenums)-1]
#prep graph axis for dates, including proper date format
xfmt = matplotlib.dates.DateFormatter('%m/%d/%Y')
ax.xaxis.set_major_formatter(xfmt)

ax.autoscale_view()

# # #t = ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
# # #           [1,0,4,7,9,1,5,2,1,3,23,12,34,23,43,32,21])
t = (datenums,y)
q = np.array(t)
# # print datenums[0]
# # print dts[0]
# #fig, ax = plt.subplots()
line, = ax.plot([], [], 'g-')

plt.xlim(t0,t1)
plt.ylim(0, max(y))
plt.xlabel('Date')
plt.ylabel('# of Tweets')
plt.title('KEYWORD: EBOLA')
#plt.plot_date(datenums, y, tz=None, xdate=True)

def update_line(num, q, line):
    line.set_data(q[...,:num])
    return line,


	
line_ani = animation.FuncAnimation(fig, update_line, 150, fargs=(q, line),
     blit=True)

# #line_ani.save('lines.mp4')

plt.show()