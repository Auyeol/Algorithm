a, b, c = map(int, input().split())
money = 0
if(a==b and b==c):
  money = 10000 + a * 1000
elif((a==b and b!=c) or (a==c and a!=b)):
  money = 1000 + a * 100
elif((b==c and a!=b)):
  money = 1000 + b * 100 
else:
  money = max(a,b,c) * 100
print(money)