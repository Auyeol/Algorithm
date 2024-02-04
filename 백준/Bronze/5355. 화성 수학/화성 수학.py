T = int(input())

for _ in range(T):
    arr = list(map(str, input().split()))
    num = float(arr[0])
    for i in range(len(arr)-1):
        s = arr[i+1]
        if s == '@':
            num *= 3
        if s == '%':
            num += 5
        if s == '#':
            num -= 7

    print(f'{num:.2f}')