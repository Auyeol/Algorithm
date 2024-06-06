def solution(hp):
    cnt = 0
    
    result = hp
    cnt += result//5 
    result = hp%5
    
    cnt += result // 3
    result = result%3 
    
    cnt += result
    
    return cnt