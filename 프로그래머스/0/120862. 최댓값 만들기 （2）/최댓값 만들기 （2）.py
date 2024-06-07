def solution(numbers):
    result = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            result.append(numbers[i] * numbers[j])
            
    return max(result)