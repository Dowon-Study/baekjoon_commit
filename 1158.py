import sys
num = list(map(int,sys.stdin.readline().split()))
people = [i for i in range(1,num[0]+1)]
result = []
index = num[1] -1

while len(people):
    if index >= len(people):
        index = index % len(people)
    else:
        result.append(str(people.pop(index)))
        index += num[1] -1

print("<", ", ".join(result), ">",sep='')
