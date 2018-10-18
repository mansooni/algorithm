import sys
import math


n = int(input()) 
q = int(input()) 
chk = {}

for i in range(n):
	ext, mt = input().split()
	chk[ext.lower()] = mt

for i in range(q):
    fname = input().lower()

    if not '.' in fname:
        print("UNKNOWN")
        
    else :
        fname = fname.split(".")[-1]
            
        if chk.get(fname):
            print(chk.get(fname))
        else:
            print("UNKNOWN")

