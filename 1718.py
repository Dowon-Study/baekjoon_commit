number = int(input())

count = 1
result = 0

while 1:
    if number // (10 ** count) > 0:
        count += 1
    else:
        break
for i in range(count - 1):
    result += 9 * (10 ** i) * (i + 1)
result += (number - (10 ** (count - 1)) + 1) * count

print(result)
