import sys

count = int(sys.stdin.readline())
equation = list(sys.stdin.readline().rstrip())
number = []

for _ in range(count):
    num = int(input())
    number.append(num)

index = 0
total = 0
for i in equation:
    if i == '+':
        total = number[index - 1]  + number[index - 2]
        del number[index - 1]
        del number[index - 2]
        number.insert(index - 2,total)
        index -= 2
    elif i == '-':
        total = number[index - 2]  - number[index - 1]
        del number[index - 1]
        del number[index - 2]
        number.insert(index - 2,total)
        index -= 2
    elif i == '*':
        total = number[index - 1]  * number[index - 2]
        del number[index - 1]
        del number[index - 2]
        number.insert(index - 2,total)
        index -= 2
    elif i == '/':
        total = number[index - 2]  / number[index - 1]
        del number[index - 1]
        del number[index - 2]
        number.insert(index - 2,total)
        index -= 2

    index += 1

print('%.2f' %number[0])
