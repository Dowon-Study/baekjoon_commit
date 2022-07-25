import sys
num = int(sys.stdin.readline())
num_bord = []
for _ in range(num):
    num_bord.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,len(num_bord)):
    num_bord[i][0] += min(num_bord[i-1][1],num_bord[i-1][2])
    num_bord[i][1] += min(num_bord[i-1][0],num_bord[i-1][2])
    num_bord[i][2] += min(num_bord[i-1][0],num_bord[i-1][1])
print(min(num_bord[num-1][0],num_bord[num-1][1],num_bord[num -1][2]))
