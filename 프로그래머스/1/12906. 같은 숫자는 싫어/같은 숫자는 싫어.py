def solution(arr):
    ST = []
    ST.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            ST.append(arr[i])
    return ST