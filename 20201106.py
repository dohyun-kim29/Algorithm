prices = [1, 2, 3, 2, 3]

answer = []
length = len(prices)

for i in range(0, length):
    for j in range(i, length):
        if prices[i] > prices[j]:
            answer.append(j)
            break
        elif j == length - 1:
            answer.append(j - i)
            break

print(answer)
