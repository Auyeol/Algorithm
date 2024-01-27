case_num = int(input()) 

for case in range(case_num):
    num1, num2 = list(map(int, input().split())) 
    a, b = num1, num2
    while b:
        a, b = b, a%b
    gcd = a

    lcm = (num1 * num2) // gcd
    print(lcm)