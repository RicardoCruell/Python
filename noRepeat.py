import sys


lines = open('ebola.txt', 'r').readlines()

lines_set = set(lines)

out  = open('noRepeat.txt', 'w')

for line in lines_set:
    out.write(line)