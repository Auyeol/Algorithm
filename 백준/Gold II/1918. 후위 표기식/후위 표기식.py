def back_expression(S):
    ST = []
    lst = []
    out_p = {'(':3, '+':1, '-':1, '*':2, '/':2}
    in_p = {'(':0, '+':1, '-':1, '*':2, '/':2}
    for c in S:
        if c.isalpha():
            lst.append(c)
        elif c == ')':
            while ST[-1] != '(':
                lst.append(ST.pop())
            ST.pop()

        else: # 연산자가 들어오는 경우
            if ST and out_p[c] > in_p[ST[-1]]:
                ST.append(c)
            else:
                while ST and out_p[c] <= in_p[ST[-1]]:
                    lst.append(ST.pop())
                ST.append(c)

    while ST:
        lst.append(ST.pop())
    return lst


S = input()
print(*back_expression(S), sep='')
