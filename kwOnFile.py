import sys

#init keyword
keyword = "ebola"
newFile = "ebola.txt"
# store lines of text and dates
lines = []

with open('tweetsAll.txt', 'r') as f:
    lines = f.read()

# separate each entry
text = lines.split("\n")

# give new file a name and write all desired entries
#newFile = 'tweetsFiltered.txt'
i = 1
with open(newFile, 'w') as fout:
    for line in text:
        if keyword not in line.lower():
            i = i + 1
        else:
            fout.write(line)
            fout.write("\n")
        i = i + 1