def solution(n):
    result = [1]
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)
            
    return result