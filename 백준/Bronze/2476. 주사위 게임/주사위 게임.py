T = int(input())
arr = []
for _ in range(T):
    n1, n2, n3 = map(int, input().split())
    price = 0

    if n1 == n2 == n3:
        price = 10000 + n1 * 1000

    elif (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2):
        price = 1000 + n1 * 100

    elif n2 == n3 and n2 != n1:
        price = 1000 + n2 * 100

    else:
        price = max(n1, n2, n3)*100
    arr.append(price)
print(max(arr))