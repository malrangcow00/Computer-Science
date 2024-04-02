# N : 지도의 한변의 길이
N = int(input())

# arr : N * N 집위치 지도
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]  # 방문체크 배열

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def dfs(x, y):
    global cnt
    cnt += 1
    # 현재 좌표에다가 방문 체크를 하고, 카운트를 1 높힌다. (최종적으로 카운트를 반환)
    visited[x][y] = True
    # 현재 좌표에서 인접한 좌표로 이동한다. (상하좌우에 접해있는 집 좌표)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당되는 좌표가 유효한지. (배열 범위를 넘지 않는지)
        # 해당 좌표에 집이 있는지, 방문 체크가 되어있는지...
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)


# 단지의 집 수를 저장하는 리스트
answer = []

for i in range(N):
    for j in range(N):
        # 집이 있는 위치에 단지에 포함되어 있는 집 수를 확인하기!
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

# 오름차순으로 정렬
answer.sort()

# 그 값을 각 줄에 출력
print(len(answer))
for i in answer:
    print(i)