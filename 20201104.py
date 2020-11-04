schoville = [1, 2, 3, 9, 10, 11]

K = 7

answer = 0
length = len(schoville) + 1

for _ in range(1, length):
    schoville.sort()
    if (schoville[0] < K):
        schoville[1] = schoville[0] + (schoville[1] * 2)
        del schoville[0]
        answer += 1
        if (len(schoville) == 1 and schoville[0] < K):
            answer = -1

print(answer)