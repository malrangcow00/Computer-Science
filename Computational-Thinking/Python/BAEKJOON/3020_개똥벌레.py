import sys
input = sys.stdin.readline

# N: 석순과 종유석의 개수, H: 동굴 높이
N, H = map(int, input().split())
# index와 같은 길이를 가지는 석순과 종유석의 개수 배열...
up = [0] * (H + 1)
down = [0] * (H + 1)

# 석순과 종유석 순으로 반복 입력
for i in range(N):
    if i % 2:
        up[int(input())] += 1
    else:
        down[int(input())] += 1

# 길이가 긴 것부터 역순으로 더해 내려오면서 카운트
# 같은 높이에서 겹치는 장애물의 개수를 저장
for i in range(H)[::-1]:
    up[i] += up[i + 1]
    down[i] += down[i + 1]

# print(up)
# print(down)

min_obstacles = N
ways = 0
# 동굴 높이가 H지만 바닥과 천장에서 출발하지는 않는다 (벌레도 힘들다...)
for i in range(1, H+1):
    obstacles = up[i] + down[H - i + 1]
    # 최소 값을 갱신하는 경우
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        ways = 1
    # 최소 값과 같은 경우
    elif obstacles == min_obstacles:
        ways += 1

print(min_obstacles, ways)
