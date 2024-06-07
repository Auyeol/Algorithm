def solution(box, n):
    xyz = []
    result = 1
    
    for i in range(3):
        xyz.append(box[i]//n)
        
    for i in xyz:
        result *= i
        
    return result