def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    result = array.index(height)
    
    return result
    