import sys

num = int(sys.stdin.readline())

for _ in range(num):
    count = int(sys.stdin.readline())
    
    Fline = list(map(int,sys.stdin.readline().split()))
    Sline = list(map(int,sys.stdin.readline().split()))
    
    total = Fline + Sline

    answer = 0

    while sum(total) != 0 :

        index = total.index(max(total))
        answer += max(total)

        if index + 1 < count:
            zero = 0
            row = 0
        else:
            zero = count
            row = - count * 2
        
        if index == zero:
            total[1 + zero] = 0
        elif index == zero + count -1:
            total[index - 1] = 0
        else:
            total[index - 1] = 0
            total[index + 1] = 0
        
        total[index] = 0
        total[row + index + count] = 0

    print(answer)
