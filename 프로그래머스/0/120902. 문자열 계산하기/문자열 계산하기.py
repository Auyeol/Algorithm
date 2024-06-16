def solution(my_string):
    arr = my_string.split()
    
    sum_v = int(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == '+':
            sum_v += int(arr[i+1])
            i += 1
        elif arr[i] == '-':
            sum_v -= int(arr[i+1])
            i += 1
    
    return sum_v