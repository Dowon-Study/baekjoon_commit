count = int(input())
result = []
for _ in range(count):
    string = input().split()
    result_temp = []
    for i in string:
        result_temp.append(i[::-1])
    result.append(" ".join(result_temp))
for s in result:
    print(s)
