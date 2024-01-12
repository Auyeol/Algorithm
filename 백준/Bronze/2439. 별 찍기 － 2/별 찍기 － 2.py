n = int(input())
j = 0
for i in range(n-1,-1,-1):
  j += 1
  print(' '*i+'*'*j)