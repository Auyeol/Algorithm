def cal_expression(lst):
    ST = []

    for c in lst:
        if 'A' <= c <= 'Z':  
            ST.append(arr[ord(c) - ord('A')])
        else:
            v2 = float(ST.pop())
            v1 = float(ST.pop())
            ST.append(calc(v1, v2, c))
    return ST.pop()
def calc(num1, num2, exp):
    if exp == '+':
        return num1 + num2
    elif exp == '-':
        return num1 - num2
    elif exp == '*':
        return num1 * num2
    elif exp == '/':
        return num1 / num2

N = int(input())
S = input().strip()
arr = []
for i in range(N):
    arr.append(int(input()))
# print(S)
# print(arr)
print('{:.2f}'.format(cal_expression(S)))