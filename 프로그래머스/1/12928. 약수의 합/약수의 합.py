def solution(n):
    result = [] 
    i = 1
    while i <= n:
        if n % i == 0:
            result.append(i)
        i += 1
    
    return sum(result)