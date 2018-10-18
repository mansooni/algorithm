from datetime import date
import sys
import math
from dateutil import rrule

begin = input().split(".")
end = input().split(".")
ans = ''

begin = [int(i) for i in begin]
end = [int(i) for i in end]


y = list(rrule.rrule(rrule.YEARLY, dtstart=date(begin[2],begin[1], begin[0]), until=date(end[2],end[1    ],end[0])))
m = list(rrule.rrule(rrule.MONTHLY, dtstart=date(begin[2],begin[1], begin[0]), until=date(end[2],end[1],end[0])))
d = list(rrule.rrule(rrule.DAILY, dtstart=date(begin[2],begin[1], begin[0]), until=date(end[2],end[1],end[0])))



if len(y)-1 > 1:
	ans = str(len(y)-1)+" years, "
elif len(y)-1 == 1:
	ans = str(len(y)-1)+" year, "
	

if (len(m)-1)%12 > 1:
	ans += str((len(m)-1)%12)+" months, "
elif (len(m)-1)%12 == 1:
	ans += str((len(m)-1)%12) +" month, "

print(ans+"total "+str(len(d)-1)+" days")
