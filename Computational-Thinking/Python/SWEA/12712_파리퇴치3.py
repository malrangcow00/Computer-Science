import sys
sys.stdin = open('input/12712.txt', 'r')

crs_dx = [0, 0, -1, 1]
crs_dy = [1, -1, 0, 0]
dia_dx = [1, 1, -1, -1]
dia_dy = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0
    for y in range(N):
        for x in range(N):
            crs_fly = arr[y][x]
            dia_fly = arr[y][x]
            for i in range(4):
                for j in range(1, M):
                    nx, ny = x + j*crs_dx[i], y + j*crs_dy[i]
                    mx, my = x + j*dia_dx[i], y + j*dia_dy[i]
                    if N > nx >= 0 and N > ny >= 0:
                        crs_fly += arr[ny][nx]
                    if N > mx >= 0 and N > my >= 0:
                        dia_fly += arr[my][mx]
            max_fly = max(max_fly, crs_fly, dia_fly)
    print(f'#{tc} {max_fly}')