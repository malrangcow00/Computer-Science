from collections import deque
import sys
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 상어 기본 사이즈
shark_size = 2
# 물고기 스택 ( 사이즈 만큼 먹으면 0으로 초기화 )
lv = 0

def func(start):
    # BFS 탐색으로 물고기까지의 거리 구하기
    dist = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append(start)
    # 물고기 정보 FISH = (x좌표, y좌표, 거리)
    fish = []
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        # 사방탐색 시작 !
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            # 범위 조건
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 물고기가 지나갈 수 있는 조건 ( 크기가 같거나 작으면 지나갈 수 있음 )
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    # 그 안에서 먹을 수 있는 물고기 탐색 ( 크기가 작아야함, 같은건 못 먹음 )
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        fish.append((nx, ny, dist[nx][ny]))
    # 람다 ... 로 우선순위 조건
    fish.sort(key=lambda x: (x[2], x[0], x[1]))
    # 물고기 리스트 return 한다
    return fish
# 시작 위치 ( 상어(9)의 처음 위치 )
start = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0

# 물고기 먹는데 총 소요 시간
time = 0
while True:
    # 물고기 스택이 사이즈와 같아지면 사이즈 += 1 스택 = 0
    if lv == shark_size:
        shark_size += 1
        lv = 0
    # 방문 기록 ( 얘는 while문이 돌 때마다 초기화 )
    visited = [[False] * n for _ in range(n)]
    fish = func(start)
    # 먹을 수 있는 물고기가 있을 때
    if len(fish) > 0:
        # 물고기 좌표랑 거리 변수에 할당
        fish_x, fish_y, fish_d = fish[0]
        # 물고기 먹으면 거기서 다시 시작해야하므로 시작 위치 바꿔줌
        start = (fish_x, fish_y)
        # 걸린 시간 누적, 스택 1씩 누적
        time += fish_d
        lv += 1
        # 물고기 먹었으면 비워주기
        graph[fish_x][fish_y] = 0
    # 물고기 없으면 call mom
    else:
        break

print(time)