import sys
N = int(sys.stdin.readline())
deQ = []
for _ in range(N):
    op = sys.stdin.readline().split()

    if op[0] == 'push_front':
        deQ = [int(op[1])] + deQ

    elif op[0] == 'push_back':
        deQ.append(int(op[1]))

    elif op[0] == 'pop_front':
        if deQ:
            print(deQ.pop(0))
        else:
            print(-1)

    elif op[0] == 'pop_back':
        if deQ:
            print(deQ.pop())
        else:
            print(-1)

    elif op[0] == 'size':
        print(len(deQ))

    elif op[0] == 'empty':
        if deQ:
            print(0)
        else:
            print(1)

    elif op[0] == 'front':
        if deQ:
            print(deQ[0])
        else:
            print(-1)

    elif op[0] == 'back':
        if deQ:
            print(deQ[-1])
        else:
            print(-1)
