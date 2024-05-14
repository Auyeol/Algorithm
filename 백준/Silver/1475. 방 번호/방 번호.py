N = list(input())

for i in range(len(N)):
    N[i] = int(N[i])

arr = [0,1,2,3,4,5,6,7,8,6]

# [1,2,3,4,5,6,7,8,6]
# ['1','2','3','4','5','6','7','8','6']
cnt = 1
while N:
    elem = N.pop()

    if elem == 9:
        elem = 6

    if elem in arr:
        arr.remove(elem)

    else:
        arr.extend([0,1,2,3,4,5,6,7,8,6])
        arr.remove(elem)
        cnt += 1

print(cnt)