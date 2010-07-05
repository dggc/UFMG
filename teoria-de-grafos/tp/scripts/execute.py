import commands
import os
import sys
import re
import math

vertices = [500, 750, 1000, 1250, 1500, 1750, 2000]
edges = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for v in vertices:
    for e in edges:
        ce = int(((v*v - v)/2)*e)
        gen = './genwebgraph.py -t 4 -o lala.txt -u undirected -s -v ' + str(v) + ' -e ' + str(ce)
        print gen
        print commands.getoutput(gen)

        con = 'python convert.py ../input-efficiency/v'+str(v)+'e'+str(int(e*100))+'.txt'
        print con
        print commands.getoutput(con)
