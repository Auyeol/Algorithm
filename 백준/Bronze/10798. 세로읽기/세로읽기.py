arr = [['']*15 for _ in range(5)]
result = ''
for i in range(5):
    word = input()

    for j in range(len(word)):
        arr[i][j] = word[j]


for row in range(15):
    for col in range(5):
        result += arr[col][row]

print(result)