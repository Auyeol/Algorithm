N = list(input())

for i in range(len(N)):
    N[i] = int(N[i])

N.sort(reverse=True)

print(*N, sep='')