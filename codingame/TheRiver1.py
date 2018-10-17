import sys
import math

r_1=int(input())
r_2=int(input())

while True:
	r1 = list(str(r_1))
	r2 = list(str(r_2))
	if r_1<=r_2:
		for i in r1:
			r_1+=int(i)
			
	elif r_1>r_2:
		for j in r2:
			r_2+=int(j)

	if r_1==r_2 :
		break

print(r_1)
