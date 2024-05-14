cnt = 20
score_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
           'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
credit_sum = 0
sum_v = 0
for _ in range(20):
    subject = list(input().split())

    if subject[2] == 'P':
        # credit_sum += float(subject[1])
        continue
    credit_sum += float(subject[1])
    sum_v += float(subject[1]) * float(score_dict[subject[2]])

print(sum_v/credit_sum)