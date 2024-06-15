def solution(n):
    arr = []
    for i in range(1, 12):
        arr.append(fact(i))
    
    result = 0
    
    for i in range(len(arr)):
        result = arr[i]
        if result > n:
            return i
    
    return result
    
def fact(num):
    val = 1
    for n in range(num, 0, -1):
        val *= n
        
    return val