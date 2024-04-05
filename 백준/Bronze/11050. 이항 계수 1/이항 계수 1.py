def fac(num):
    sum_v = 1
    for i in range(1, num+1):
        sum_v *= i
    return sum_v

N, K = map(int, input().split())
result = fac(N) // (fac(K) * fac(N-K))
print(result)