S = input()
sum_v = 10
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        sum_v += 5
    else:
        sum_v += 10

print(sum_v)