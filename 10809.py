import sys

string = list(sys.stdin.readline().rstrip())

answer = [-1] * 26

for i in range(len(string)):
    if answer[ord(string[i]) - 97] == -1:
        answer[ord(string[i]) - 97] = i
        
print(*answer) 
