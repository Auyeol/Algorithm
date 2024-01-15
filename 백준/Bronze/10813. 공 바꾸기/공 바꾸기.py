num, case_num = map(int, input().split())
basket = [0]*num
temp = 0
for i in range(num):
  basket[i] = i+1

for i in range(case_num):
  a, b = map(int, input().split())
  temp = basket[a-1]
  basket[a-1] = basket[b-1]
  basket[b-1] = temp

for i in basket:
  print(i, end=' ')