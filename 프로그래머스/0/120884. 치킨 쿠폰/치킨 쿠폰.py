def solution(chicken):
    result = 0
    while chicken >= 10:
        div = chicken // 10 
        mod = chicken % 10
        result += div 
        chicken = div + mod 
    return result 