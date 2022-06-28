count = int(input())
stack = []
list_num = 1
result = []
erro = False
for _ in range(count):
    num = int(input())
    for _ in range(num - list_num + 1):
        result.append("+")
        stack.append(list_num)
        list_num  += 1
    last_num = stack.pop()
    if(num == last_num):
        result.append("-")
    else:
        erro = True
if(erro):
    result = ["NO"]
for i in result:
    print(i)
