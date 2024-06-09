def solution(my_string, num1, num2):
    lst = list(my_string)
    result = ''
    temp = my_string[num1]
    
    lst[num1] = lst[num2]
    lst[num2] = temp
    
    for s in lst:
        result += s
        
    return result
        
    