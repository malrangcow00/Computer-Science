import sys
sys.stdin = open('input/9490.txt', 'r')

# # 상하좌우 단위벡터
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 행 M: 열, 3 <= N, M <= 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for y in range(N):
        for x in range(M):
            cnt = arr[y][x]
            for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]: # 위 방향에서 시계방향으로 90도씩
                nx, ny = x, y
                for i in range(arr[y][x]):
                    nx, ny = nx + dx, ny + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        cnt += arr[ny][nx] # 주변칸 풍선의 꽃가루 수
                mx = max(mx, cnt)
            # for i in range(4):
            #     for j in range(1, arr[y][x]+1):
            #         nx = x + j*dx[i]
            #         ny = y + j*dy[i]
            #         if 0 <= nx < M and 0 <= ny < N:
            #             cnt += arr[ny][nx]
            # mx = max(mx, cnt)
    print(f'#{tc} {mx}')