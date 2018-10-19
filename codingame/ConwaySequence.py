import sys
import math

r = int(input())
l = int(input())

ans = list()
res = list()
tmp = r
count = 0

for i in range(l-1):
	res.insert(0,tmp)
	for i in range(len(ans)):
		if ans[i] == tmp:
			count+=1
		if i == len(ans)-1:
			res.insert(0,count)
			print("res["+str(i)+"] = "+str(count))
		else:
			res.insert(0,count)
			print("res["+str(i)+"] = "+str(count))
			count = 0
			tmp = ans[i]
	ans = res
	res = list()

	print(ans)
	
	
