import sys

string = list(sys.stdin.readline().rstrip())
result = [0] * 26
for i in string:
    result[ord(i) - 97] += 1
print(*result)
 
