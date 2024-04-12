lst = []
while True:
    S = input()
    if S == '.':
        break
    lst.append(S)

for c in lst:
    ST = []
    result = 'yes'
    for s in c:
        if s == '(' or s == '[':
            ST.append(s)

        elif s == ')':
            if ST and ST[-1] == '(':
                ST.pop()
            else:
                result = 'no'
                break

        elif s == ']':
            if ST and ST[-1] == '[':
                elem = ST.pop()

            else:
                result = 'no'
                break
    if len(ST)>0:
        result = 'no'
    print(result)