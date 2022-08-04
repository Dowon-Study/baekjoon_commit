import sys
num = int(sys.stdin.readline())
step_list = [1] * 10
for _ in range(num - 1):
    step_temp = [1]
    temp = 1
    for i in range(1,10):
        step_temp.append(step_list[i] + temp)
        temp += step_list[i]
    step_list = step_temp
print(sum(step_list)%10007)
