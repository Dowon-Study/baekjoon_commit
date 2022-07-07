import sys
from tabnanny import check

lenght = int(input())

number = list(map(int,sys.stdin.readline().split()))

for _ in range(lenght):
    check = True
    for j in number:
        if number[0] < j:
            print(j,end=' ')
            del number[0]
            check = False
            break
    if check:
        print(-1,end=' ')
