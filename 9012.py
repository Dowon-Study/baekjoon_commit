count = int(input())
for _ in range(count):
    stop = True
    stack = []
    ps = input()
    for i in ps:
        if(i == '('):
            stack.append(i)
        elif(i==')'):
            try:
                stack.pop()
            except:
                print("NO")
                stop = False
                break
    if(stop):
        if(stack):
            print("NO")
        else:
            print("YES")
