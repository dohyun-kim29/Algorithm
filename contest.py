input1, input2 = map(int, input().split())
str = []

for i in range(0, input1):
    str.append(input())

strLen = len(str)

answer = []
realAnswer = []

for i in range(0, strLen):
    strListLen = len(str[i])
    strList = list(str[i])

    for j in range(0, strListLen):

        for k in range(0, input2):
            answer.append(strList[j])
            answerStr = "".join(answer)
print(answerStr)

# num = int(input())
# ans = []
#
# def numberSelector(k):
#     state = 0
#     # if(k == 1):
#     #     ans.append(1)
#     for i in range(1, k + 1):
#         if k % i == 0:
#             state = state + 1
#     if (state == 2):
#         ans.append(1)
#
#
#
#
# for i in range(1, num + 1):
#     if(num == 2):
#         ans.append(1)
#         break
#     numberSelector(i)
#
# print(len(ans))















