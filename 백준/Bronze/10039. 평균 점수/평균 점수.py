sum_v = 0
for _ in range(5):
    score = int(input())
    
    if score < 40:
        score = 40
    sum_v += score
print(int(sum_v/5))
    
    