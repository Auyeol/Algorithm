arr = [0]*10

minus, plus = map(int, input().split())
arr[0] = plus - minus

for i in range(1, 10):
    minus, plus = map(int, input().split())

    arr[i] = arr[i-1] + plus - minus

print(max(arr))