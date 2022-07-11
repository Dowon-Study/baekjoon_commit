import sys

string = list(sys.stdin.readline().rstrip())

answer = []

for i in string:
    if 65 <= ord(i) <= 90:
        temp = ord(i) - 65
        answer.append(chr(((temp + 13) % 26) + 65))
    elif 97 <= ord(i) <= 122:
        temp = ord(i) - 97
        answer.append(chr(((temp + 13) % 26) + 97))
    else:
        answer.append(i)
answer = "".join(answer)
print(answer)
