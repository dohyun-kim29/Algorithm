array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
comLen = len(commands)


for i in range(0, comLen):
    splitedArray = array[commands[i][0] - 1 : commands[i][1]]
    splitedArray.sort()
    comIndex = commands[i][2] - 1
    answer.append(splitedArray[comIndex])


print(answer)