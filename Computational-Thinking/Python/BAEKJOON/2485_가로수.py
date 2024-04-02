import sys

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

N = int(sys.stdin.readline())
point = []
for _ in range(N):
    point.append(int(sys.stdin.readline()))

dis = []
for _ in range(1, N):
    dis.append(point[_]-point[_-1])

tmp = dis[0]

for _ in dis:
    tmp = GCD(tmp, _)

len_point = (max(point)-min(point)) // tmp + 1
print(len_point-len(point))