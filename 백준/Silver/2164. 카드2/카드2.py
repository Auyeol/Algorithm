from collections import deque
N = int(input())
deQ_card = deque((i+1) for i in range(N))

while len(deQ_card) != 1:
    deQ_card.popleft()
    back = deQ_card.popleft()
    deQ_card.append(back)

print(deQ_card[0])
