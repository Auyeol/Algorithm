import sys
N = int(sys.stdin.readline())
arr = []
result = []
for _ in range(N):
    arr.append((sys.stdin.readline().split()))

for i in range(N):
    arr[i] = arr[i][-1] + ' ' + arr[i][-2] + ' ' + arr[i][-3] + ' ' + arr[i][-4]
    result.append((arr[i].split()))

for i in range(N):
    for j in range(3):
        result[i][j] = int(result[i][j])

print(max(result)[3])
print(min(result)[3])