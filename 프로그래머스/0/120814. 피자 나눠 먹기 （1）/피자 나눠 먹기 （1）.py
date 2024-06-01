def solution(n):
    result = 1
    
    if n>7:
        result = n//7
        if n%7 > 0:
            result += 1
    
    return result 
        