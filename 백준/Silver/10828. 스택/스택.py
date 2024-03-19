import sys
N = int(sys.stdin.readline())
ST = []
for _ in range(N):
    op = sys.stdin.readline().split()

    if op[0] == 'push':
        ST.append(int(op[1]))

    elif op[0] == 'pop':
        if ST:
            print(ST.pop())
        else:
            print(-1)

    elif op[0] == 'size':
        print(len(ST))

    elif op[0] == 'empty':
        if len(ST):
            print(0)
        else:
            print(1)

    elif op[0] == 'top':
        if ST:
            print(ST[-1])
        else:
            print(-1)