import sys

count = int(sys.stdin.readline())
stack = []
for _ in range(count):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.insert(0,int(command[1]))
    if command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if command[0] == "size":
        print(len(stack)) 
    if command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    if command[0] == "front":
        if stack :
            print(stack[len(stack) - 1])
        else:
            print(-1)
    if command[0] == "back":
        if stack:
            print(stack[0])
        else:
            print(-1)
