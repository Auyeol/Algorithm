N = int(input()) # 온라인 저지 회원의 수가 주어진다
age_lst = [[] for _ in range(201)]

for i in range(1, N+1):
    age, name = input().split()
    age_lst[int(age)].append(name)

for i in range(1, 201):
    if age_lst[i]:
        if len(age_lst[i])>=2:
            for elem in age_lst[i]:
                print(i, elem)
        else:
            print(i, *age_lst[i])