def solution(my_string):
    result = []
    for c in my_string:
        if c.isdigit():
            result.append(int(c))
    return sorted(result)