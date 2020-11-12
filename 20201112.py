progresses = [93, 30, 55]
speeds = [1, 30, 5]
date = []
state = 0
answer = []

proLen = len(progresses)

for i in range(0, proLen):
    if ((100 - progresses[i]) % speeds[i] == 0):
        date.append(int((100 - progresses[i]) / speeds[i]))
    else:
        date.append(int((100 - progresses[i]) / speeds[i]) + 1 )


maximum = date[0]

for i in range(0, proLen):
    if (i == 0):
        state = state + 1
        continue

    else:
        if (date[i] <= maximum):
            state = state + 1
            answer.append(state)
            state = 0

        elif (i == (proLen - 1)):
            state = state + 1
            answer.append(state)
            state = 0

        else:
            state = state + 1

print(answer)