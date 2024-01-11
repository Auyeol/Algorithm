year = int(input())
is_year = False

if(year%4 == 0 and year%100 != 0 or year % 400 == 0):
  is_year = True
else:
  is_year = False

print(is_year*1)