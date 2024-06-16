def solution(array):
    cnt = 0
    
    for a in array:
        temp = list(str(a))
        cnt += temp.count('7')
        
    return cnt