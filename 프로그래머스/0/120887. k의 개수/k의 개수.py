def solution(i, j, k):
    cnt = 0
    
    for i in range(i, j+1):
        s = str(i)
        lst = list(s)
        
        cnt += lst.count(str(k))
    return cnt