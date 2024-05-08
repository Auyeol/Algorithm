def solution(s):
    ST = [] 
    answer = True 
    for c in s:
        if c == '(':
            ST.append(c)
        elif c == ')':
            if ST:
                while ST:
                    v = ST.pop()
                    if v == '(':
                        break 
                    
            else:
                answer = False 
                
    if ST:
        answer = False
        
    return answer 