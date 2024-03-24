import sys

N = int(sys.stdin.readline())
num = '666'
cnt = 0

while True:
    if '666' in num:
        cnt += 1
        
    if cnt == N:
        print(num)
        break    
    num = str(int(num) + 1)
        