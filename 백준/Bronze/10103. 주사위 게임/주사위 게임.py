import sys
T = int(sys.stdin.readline())
score_a = score_b = 100
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        score_b -= A
    elif A < B:
        score_a -= B
    else:
        continue

print(score_a)
print(score_b)