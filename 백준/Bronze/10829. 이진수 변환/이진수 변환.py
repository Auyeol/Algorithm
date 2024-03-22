# N = int(input())
# result = bin(N)
# print(result[2:])

N = int(input())
result = ''
while N > 0:
    if N % 2 == 1:
        result = '1' + result
    else:
        result = '0' + result
    N //= 2

print(result)