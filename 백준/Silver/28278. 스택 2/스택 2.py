# 스택 2
import sys

N = int(sys.stdin.readline()) # 명령의 수
ST = [] # 스택 초기화
for i in range(N): # 명령은 5가지
    op = sys.stdin.readline().split()
    if op[0] == '1':
        ST.append(int(op[-1]))
    elif op[0] == '2':
        if ST:
            print(ST.pop(-1))
            continue
        print(-1)
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4':
        if ST:
            print(0)
            continue
        print(1)
    elif op[0] == '5':
        if ST:
            print(ST[-1])
            continue
        print(-1)