def solution(bin1, bin2):
    result = int(bin1, 2) + int(bin2, 2)
    result = bin(result)
    return result[2:]