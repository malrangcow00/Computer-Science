import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))

canyon = []

for index, power in enumerate(P):
    canyon.append([power, index])
canyon.sort()
print(canyon)

gap = [0]*(N-1)
for i in range(1, N):
    gap[i-1] = canyon[i][0] - canyon[i-1][0]

print(gap)
abyss = []

while canyon:
    for i in range(2, N):
        if canyon[-i][0]-canyon[-i-1][0] <= M:
            