import commands
import os
import sys
import re
import math

vertices = [500, 750, 1000, 1250, 1500, 1750, 2000]
edges = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for v in vertices:
    f = open('../dat/time'+str(v)+'.dat','w')
    for e in edges:
        ce = int(((v*v - v)/2)*e)
        exe = '../bin/main/graph -a../input-efficiency/v'+str(v)+'e'+str(int(e*100))+'.txt'
        print exe
        n = 0.0
        time = 0.0
        for i in range(1,5):
            time += float(commands.getoutput(exe))
            n = n + 1.0
        time = time / n
        f.write(str(int(e*100))+' '+str(time)+'\n')
        #print time
    f.close()
