hour, minute = map(int, input().split())
if(minute<45):
  hour -= 1
  if(hour<0):
    hour = 23
  minute += 15
else:
  minute -= 45 
print(hour,minute)