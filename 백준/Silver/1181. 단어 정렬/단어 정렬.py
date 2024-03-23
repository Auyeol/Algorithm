import sys
N = int(sys.stdin.readline())
result = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    
    if word not in result:
        result.append(word)

result.sort(key=lambda x: (len(x),x))

for word in result:
    print(word)
    
    