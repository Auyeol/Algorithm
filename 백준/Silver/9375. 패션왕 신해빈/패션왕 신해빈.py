import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    category_dict = {}
    sum_v = 1

    for _ in range(N):
        clothes, category = input().strip().split()

        if category in category_dict:
            category_dict[category] += 1
        else:
            category_dict[category] = 1

    for val in category_dict.values():
        sum_v *= (val + 1)

    print(sum_v - 1)