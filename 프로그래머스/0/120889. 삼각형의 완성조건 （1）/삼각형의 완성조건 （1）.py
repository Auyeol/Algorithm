def solution(sides):
    result = 2
    sum_v = sum(sides)
    
    if sum_v - max(sides) > max(sides):
        result = 1

    return result