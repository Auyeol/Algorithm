def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        t_cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                t_cnt += 1
            
            if t_cnt >= 3:
                cnt += 1
                break
                
    return cnt 
            
        