def solution(emergency):
    result = []
    temp = sorted(emergency, reverse=True)
    
    for e in emergency:
        result.append(temp.index(e)+1)
    
    return result