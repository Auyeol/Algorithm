case_num = int(input())
for case in range(case_num):
    num1, num2 = list(map(int, input().split())) # 270 192
    aList = [num1, num2]
    while True:
        temp = num1%num2 
        num1 = num2 
        num2 = temp
        if temp == 0:
            gcd = num1
            break

    result = 1
    for num in aList:
        result *= (num//gcd)
    print(result*gcd)