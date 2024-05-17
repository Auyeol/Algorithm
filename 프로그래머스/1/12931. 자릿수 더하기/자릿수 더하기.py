def solution(n):
    sum_v = 0
    n = list(str(n))
    for elem in n:
        sum_v += int(elem)
    
    return sum_v
        