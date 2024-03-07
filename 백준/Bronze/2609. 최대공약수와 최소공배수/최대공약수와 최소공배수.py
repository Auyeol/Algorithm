# 최대공약수와 최소공배수

import sys
A, B = map(int, sys.stdin.readline().split())
max_num = max(A,B)
min_num = min(A,B)

while min_num:
    max_num, min_num = min_num, max_num % min_num


print(max_num)      # 최대공약수 출력 
print(A*B//max_num) # 최소공배수 출력