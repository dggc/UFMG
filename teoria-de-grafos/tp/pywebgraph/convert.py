import commands
import os
import sys
import re

fName = 'lala.txt'
f = open(fName, 'r')
max = 0
for line in f:
    words = line.split()
    a = int(words[0])
    b = int(words[2])

    #print a
    #print b

    if a > max:
        max = a
    if b > max:
        max = b

matrix = []
for i in range(max):
    row = []
    for j in range(max):
        row.append(0)
    matrix.append(row)

f.close()
f = open(fName, 'r')
for line in f:
    words = line.split()
    a = int(words[0])
    b = int(words[2])
    a = a-1
    b = b-1
    matrix[a][b] = 1
    matrix[b][a] = 1

print max
for row in matrix:
    line = ''
    for cell in row:
        line += str(cell)
        line += ' '
    print line
f.close()
