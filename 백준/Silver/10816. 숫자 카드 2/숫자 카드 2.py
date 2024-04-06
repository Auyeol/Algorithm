import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find_lst = list(map(int, sys.stdin.readline().split()))

card_dict = {}
result = []

for c in card:
    if c in card_dict:
        card_dict[c] += 1
    else:
        card_dict[c] = 1

for i in range(len(find_lst)):
    if find_lst[i] in card_dict:
        result.append(card_dict[find_lst[i]])
    else:
        result.append(0)

print(*result)