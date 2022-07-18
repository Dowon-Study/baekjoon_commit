t = [0, 1, 2]
for i in range(3, 1001):
  t.append(s[i - 2] + s[i - 1])
num = int(input())
print(t[num] % 10007)
