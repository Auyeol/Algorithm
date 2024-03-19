import sys
N = int(sys.stdin.readline())
Q = []
for _ in range(N):
    op = sys.stdin.readline().split()

    if op[0] == 'push':
        Q.append(int(op[1]))

    elif op[0] == 'pop':
        if Q:
            print(Q.pop(0))
        else:
            print(-1)

    elif op[0] == 'size':
        print(len(Q))

    elif op[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)

    elif op[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)

    elif op[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)