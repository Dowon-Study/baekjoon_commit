
try1 = input()
try2 = input()
try3 = input()

test = [try1,try2,try3]

for i in test:
    count = 0
    for k in i:
        if(k == "1"):
            count += 1
    if(count == 4):
        print("E")
    elif(count == 3):
        print("A")
    elif(count == 2):
        print("B")
    elif(count == 1):
        print("C")
    else:
        print("D")

