def solution(dot):
    dot_dict = {'++':1, '-+':2, '--':3, '+-':4}
    result1 = ''
    
    if dot[0] > 0:
        result1 += '+'
    else:
        result1 += '-'
    
    if dot[1] > 0:
        result1 += '+'
    else:
        result1 += '-'
    
    return dot_dict[result1]