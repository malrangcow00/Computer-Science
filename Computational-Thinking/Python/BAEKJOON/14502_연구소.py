import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 연구실 초기 바이러스의 위치를 저장할 데이터 구조
virus = deque()

# 연구소 내 빈 공간의 개수
blank = 0

# 배열 탐색
for y in range(N):
    for x in range(M):
        # 바이러스의 위치
        if arr[y][x] == 2:
            virus.append((y, x))
        # 빈 공간
        elif arr[y][x] == 0:
            blank += 1
# 로직
# 공간 3곳을 먼저 선택
# 해당 공간 3곳이 모두 빈 공간이었을 경우
# 선택된 공간들을 막고 바이러스를 확산시켜 남은 빈 공간의 개수를 판단
mx = 0
# N * M 크기의 공간에서 3곳을 선택
for i in range(N * M - 2):
    for j in range(i + 1, N * M - 1):
        for k in range(j + 1, N * M):
            # 선택 3곳이 모두 빈 공간인 경우
            if arr[i // M][i % M] == arr[j // M][j % M] == arr[k // M][k % M] == 0:
                # 남은 빈 공간을 뜻하는 cnt 변수 선언 & 3곳을 선택해서 벽으로 막았기 때문에 전체 빈공간의 개수 - 3
                arr[i // M][i % M] = arr[j // M][j % M] = arr[k // M][k % M] = 1
                cnt = blank - 3
                # 2차원 배열에서의 visited 배열 생성
                visited = [[0] * M for _ in range(N)]
                # 바이러스의 위치를 담을 배열 queue 생성
                queue = deque()
                # 바이러스의 좌표를 queue로 전달하면서 해당 공간을 방문체크
                for y, x in virus:
                    queue.append((y, x))
                    visited[y][x] = 1
                while queue:
                    # 빈공간의 수가 이미 앞서 측정된 mx값 보다 작아졌을 경우 반복문 탈출
                    if mx >= cnt:
                        break
                    # 바이러스가 퍼지기 시작하는 시작점 선출
                    sy, sx = queue.popleft()
                    # 사방탐색
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx = sx + dx
                        ny = sy + dy
                        # 해당 탐색 위치에 바이러스가 있는지 체크
                        # 바이러스가 존재할 경우 방문체크 후 남은 빈 공간의 수 - 1
                        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and not arr[ny][nx]:
                            cnt -= 1
                            visited[ny][nx] = 1
                            # 새롭게 바이러스가 퍼진 공간을 다시 배열에 추가하여 모든 방향 탐색이 불가능해지고 queue의 모든 요소가 popleft()될 때까지 반복
                            queue.append((ny, nx))

                # mx 최신화
                if mx < cnt:
                    mx = cnt

                # 처음 막았던 3개의 공간을 개방하고 다시 다른 3곳을 선택하여 탐색
                arr[i // M][i % M] = arr[j // M][j % M] = arr[k // M][k % M] = 0
# 출력
print(mx)