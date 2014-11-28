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
yk = []

# store lines of text and dates
lines = []
date = []
linesk = []
datek = []

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

""""""
with open('ebola.txt', 'r') as f:
    linesk = f.read()

# strip all dates from the supplied file
text = lines.split("\n")
dateFormat = '\d{4}-\d{2}-\d{2}'
for s in text:
    match = re.search(dateFormat.decode('utf-8'), s)
    if match:
        datek.append(dt.datetime.strptime(match.group(), '%Y-%m-%d').date())
    else:
        #print "no match on for:  " + s 
        continue

# we know all the entries contain the keyword; sorting will no have
# a negative impact
datek.sort()

#Count number of ALL tweets per day
i = 0
temp = datek[0]
for i in range(len(datek)):
    if temp == datek[i]:
        count = count + 1
        i = i + 1
    else:
        #x.append(temp)
        yk.append(count)
        temp = datek[i]
        count = 1
""""""

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

t = (datenums,y)
q = np.array(t)
tk = (datenums,yk)
qk = np.array(tk)
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
plt.plot(x,yk,'b-')

def update_line(num, q, line):
    line.set_data(q[...,:num])
    return line,


	
line_ani = animation.FuncAnimation(fig, update_line, 150, fargs=(q, line),
     blit=True)
line_ani = animation.FuncAnimation(fig, update_line, 150, fargs=(qk, line),
     blit=True)

# #line_ani.save('lines.mp4')

plt.show()