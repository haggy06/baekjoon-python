ScoreSum = 0
sub_time = 0
Dt = dict({'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0})
for i in range(20):
    title, time, grade = input().split()
    if grade != "P":
        ScoreSum += float(time) * Dt[grade]
        sub_time += float(time)
print(ScoreSum / sub_time)