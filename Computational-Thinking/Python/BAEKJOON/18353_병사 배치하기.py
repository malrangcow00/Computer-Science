import sys
input = sys.stdin.readline

N = int(input())

water_tank = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if water_tank[y][x] == 9:
            break
print(x, y)