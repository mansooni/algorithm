import sys
import math

s = input()
n = int(input())
answer = ''

for i in s:
    if i is not ' ':
        if ord(i)<91 and ord(i)>64:
            answer+=chr(((ord(i)+n)%65)%26+65)
        else:
            answer+=chr(((ord(i)+n)%97)%26+97)
    else:
        answer+=(' ')

print(answer)
