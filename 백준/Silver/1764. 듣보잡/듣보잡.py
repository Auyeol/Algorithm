import sys
N, M = map(int, sys.stdin.readline().split())
name_dict = {}
result = []
for _ in range(N):
    known = sys.stdin.readline().strip()
    name_dict[known] = 1

for _ in range(M):
    unknown = sys.stdin.readline().strip()

    if unknown in name_dict:
        result.append(unknown)

print(len(result))
result.sort()
for name in result:
    print(name)