while True:
    arr = list(map(int, input().split()))

    if arr[0] == arr[1] == arr[2] == 0:
        break

    max_v = arr.pop(arr.index(max(arr))) ** 2

    for i in range(len(arr)):
        arr[i] **= 2
    if max_v == sum(arr):
        print('right')
    else:
        print('wrong')