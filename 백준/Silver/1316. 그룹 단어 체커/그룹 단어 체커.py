N = int(input())
cnt = 0

for _ in range(N):
    word = list(input())
    arr = []
    is_true = True

    c = word.pop()
    arr.append(c)

    while word:
        c = word.pop()
        if arr[-1] == c:
            continue
        else:
            if c in arr:
                is_true = False
                break
            else:
                arr.append(c)

    if is_true:
        cnt += 1

print(cnt)

