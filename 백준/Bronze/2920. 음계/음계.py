def func(arr):
    state = 2
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) != 1:
            state = 2
            break
        elif arr[i] + 1 == arr[i+1]:
            state = 0
        elif arr[i] - 1 == arr[i+1]:
            state = 1
    return state

arr = list(map(int, input().split()))

result = func(arr)

if result == 0:
    print('ascending')
elif result == 1:
    print('descending')
else:
    print('mixed')