repeat = int(input())
stack = []
result = []
for _ in range(repeat):
    commend = input().split()
    if(commend[0] == 'push'):
        stack.append(int(commend[1]))
    if(commend[0] == 'pop'):
        if(len(stack) == 0):
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])
            del stack[len(stack)-1]
    if(commend[0] == 'size'):
        result.append(len(stack))
    if(commend[0] == 'empty'):
        if(len(stack) == 0):
            result.append(1)
        else:
            result.append(0)
    if(commend[0] == 'top'):
        if(len(stack) == 0):
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])
for i in result:
    print(i)
