def solution(s):
    arr = s.split()
    
    sum_v = 0 
    idx = 0
    
    for i in range(len(arr)):
        if arr[i].isalpha():
            sum_v -= int(arr[idx])
        else:
            sum_v += int(arr[i])
            idx = i
    return sum_v           