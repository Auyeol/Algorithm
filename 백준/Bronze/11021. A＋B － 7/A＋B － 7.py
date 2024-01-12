n = int(input())
idx = 0
while(idx<n):
  a, b = map(int, input().split())
  print(f'Case #{idx+1}: {a+b}')
  idx += 1