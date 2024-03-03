T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus[i] += 1

    P = int(input())
    result = []
    for _ in range(P):
        num = int(input())
        result.append(bus[num])

    print(f'#{tc} {" ".join(map(str, result))}')
