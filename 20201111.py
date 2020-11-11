answers = [1, 2, 3, 4, 5]
answer = []
ans1 = []
ans2 = []
ans3 = []
res = 0
res1 = 0
res2 = 0
res3 = 0


sam1 = [2, 1, 2, 3, 2, 4, 2, 5]
sam2 = [3, 1, 2, 4, 5]

ansLen = len(answers)

for i in range(0, ansLen):
    ans1.append(i % 5 + 1)
    ans2.append(sam1[i % 8])
    ans3.append(sam2[int((i % 10) / 2)])

for i in range(0, ansLen):
    if (answers[i] == ans1[i]):
        res1 = res1 + 1

    if (answers[i] == ans2[i]):
        res2 = res2 + 1

    if (answers[i] == ans3[i]):
        res3 = res3 + 1

res = max(res1, res2, res3)

if res1 == res:
    answer.append(1)

if res2 == res:
    answer.append(2)

if res3 == res:
    answer.append(3)

print(answer)
