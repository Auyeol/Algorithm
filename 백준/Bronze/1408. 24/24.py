import sys
st = list(map(int,sys.stdin.readline().strip().split(':')))
ed = list(map(int,sys.stdin.readline().strip().split(':')))

for i in range(2,0,-1):
    if ed[i] - st[i] < 0:
        ed[i] = 60 - st[i] + ed[i]
        if ed[i-1] == 0:
            st[i-1] += 1
        else:
            ed[i-1] -= 1
    else:
        ed[i] -= st[i]

ed[0] -= st[0]
if ed[0] < 0:
    ed[0] += 24
print(f'{ed[0]:02d}:{ed[1]:02d}:{ed[2]:02d}')
