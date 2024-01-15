num, case_num = map(int, input().split())
basket = [0]*num

for i in range(case_num):
  a,b,c = map(int, input().split())

  for j in range(a-1,b):
    basket[j] = c

for ball in basket:
  print(ball, end=' ')
