def solution(n):
    str_num = ''
    
    arr = list(str(n))
    
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        
    arr.sort(reverse=True)
    for elem in arr:
        str_num += str(elem)
    
    return int(str_num)
    