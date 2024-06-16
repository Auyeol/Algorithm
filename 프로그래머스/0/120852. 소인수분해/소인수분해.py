def solution(n):
    idx = 2
    result = []
    while n != 1:
        if n % idx == 0:
            n //= idx
            result.append(idx)
        else:
            idx += 1
            
    answer = set(result)
    
    return sorted(list(answer))
    