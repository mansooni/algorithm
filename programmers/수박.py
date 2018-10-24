import sys
import math

n = int(input())
answer = ''

for i in range(n):
    if i%2==0:
        answer +='수'
    else:
        answer+='박'

print(answer)
