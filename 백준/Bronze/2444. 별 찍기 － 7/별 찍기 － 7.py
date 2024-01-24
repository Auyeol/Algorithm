num = int(input())

for i in range(num):
    print(' '*(num-1-i)+'*'*(i+1)+'*'*i)
for j in range(num-1):
    print(' '*(j+1)+'*'*(num-1-j)+'*'*(num-2-j))