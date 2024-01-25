dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input_str = input()
t = 3
result = 0
for elem in input_str:
    for i in dial:
        if elem in i:
            result += (t+dial.index(i))
print(result)
