def solution(array, n):
    arr = []
    result = []
    
    for a in array:
        arr.append(abs(n-a))
        
    idx = 0
    min_v = min(arr) 
    
    for i in range(len(arr)):
        if arr[i] == min_v:
            result.append(array[i]) 
    
    return min(result)
    
            