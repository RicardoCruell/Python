import sys
import re
import datetime as dt

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

#init counter
count = 0

#init x and y arrays for axis vals
x = []
y = []

# store lines of text and dates
lines = []
date = []

with open('tweetsAll.txt', 'r') as f:
    lines = f.read()

# strip all dates from the supplied file
text = lines.split("\n")
dateFormat = '\d{4}-\d{2}-\d{2}'
for s in text:
    match = re.search(dateFormat, s)
    if match:
        date.append(dt.datetime.strptime(match.group(), '%Y-%m-%d').date())
    else:
        #print "no match on for:  " + s 
        continue

# we know all the entries contain the keyword; sorting will no have
# a negative impact
date.sort()

#Count number of ALL tweets per day
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

fig, ax = plt.subplots()
# #ax=plt.gca()

qq = 0
for qq in range(len(x)):
    print str(x[qq]) + ' ' + str(y[qq])

""" Need an end date to reflect the drop in ebola tweets"""
enddate = dt.datetime.strptime('2014-11-01', '%Y-%m-%d')

ax.xaxis_date()
datenums = matplotlib.dates.date2num(x)
t0 = datenums[0]
t1 = enddate

#prep graph axis for dates, including proper date format
xfmt = matplotlib.dates.DateFormatter('%m/%d/%Y')
ax.xaxis.set_major_formatter(xfmt)

ax.autoscale_view()

t = (datenums,y)
q = np.array(t)
line, = ax.plot([], [], 'g-')

plt.xlim(t0,t1)
plt.ylim(0, 30000)
plt.xlabel('Date')
plt.ylabel('# of Tweets')
plt.title('KEYWORD: EBOLA')
#plt.plot_date(datenums, y, tz=None, xdate=True)

def update_line(num, q, line):
    line.set_data(q[...,:num])
    return line,
	
line_ani = animation.FuncAnimation(fig, update_line, 150, fargs=(q, line),
     blit=True)

plt.show()