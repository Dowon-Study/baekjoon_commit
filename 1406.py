from sys import stdin

string = input()
count = int(stdin.readline())
cosor = len(string) + 1
string_list = []

for i in string:
    string_list.append(i)

for _ in range(count):
    command = stdin.readline().split()
    if(command[0] == "L"):
        if(cosor > 0):
            cosor -= 1
    if(command[0] == "D"):
        if(cosor < len(string_list)):
            cosor += 1
    if(command[0] == "B"):
        if(cosor > 0):
            del string_list[cosor - 1]
    if(command[0] == "P"):
        string_list.insert(cosor,command[1])

print("".join(string_list))
