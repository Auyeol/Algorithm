def solution(n):
    idx = 2
    while n % idx != 1:
        idx += 1
    
    return idx