import sys
input = sys.stdin.readline

def binary_search(st, ed, key):
    while st <= ed:
        mid = (st+ed)//2
        if key==have_card[mid]:
            return 1
        elif have_card[mid] > key:
            ed = mid - 1

        elif have_card[mid] < key:
            st = mid + 1

    return 0

N = int(input())
have_card = list(map(int, input().split()))
M = int(input())
all_card = list(map(int, input().split()))
have_card.sort()
result = []
for card in all_card:
    result.append(binary_search(0, len(have_card)-1,card))

print(*result)