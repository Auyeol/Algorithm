def fact(n):
    sum_v = 1
    
    while n != 0:
        sum_v *= n
        n -= 1
    
    return sum_v
    
def solution(balls, share):
    answer = fact(balls) / (fact(balls-share) * fact(share))
    return answer