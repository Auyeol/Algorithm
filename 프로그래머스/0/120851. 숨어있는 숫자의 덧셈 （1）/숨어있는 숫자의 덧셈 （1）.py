def solution(my_string):
    result = 0
    
    for c in my_string:
        if c.isdigit():
            result += int(c)
    
    return result