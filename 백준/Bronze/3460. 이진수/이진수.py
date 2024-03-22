T = int(input())

for _ in range(T):
    N = int(input())
    bin_N = ''
    result = []
    while N > 0:
        if N % 2 == 1:
            bin_N = bin_N + '1'
        else:
            bin_N = bin_N + '0'
        N //= 2

    for i in range(len(bin_N)):
        if bin_N[i] == '1':
            result.append(i)

    print(*result)