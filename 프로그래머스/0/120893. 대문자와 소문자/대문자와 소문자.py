def solution(my_string):
    result = ''
    
    for c in my_string:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()
            
    return result