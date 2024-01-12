hour, minute = map(int, input().split())
need_time = int(input())

hour += need_time//60
minute += need_time%60

if(minute>59):
  hour += minute//60
  minute = minute%60
if(hour>23):
  hour -= 24
 
print(hour, minute)