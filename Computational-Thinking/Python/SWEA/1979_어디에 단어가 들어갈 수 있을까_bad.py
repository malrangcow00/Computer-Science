import sys
sys.stdin = open('input/1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            fit_x = False
            fit_y = False
            if arr[y][x] == 1:
                if x+K <= N:
                    for i in range(1, K):
                        if 0 <= x-1 and arr[y][x-1] == 1:
                            fit_x = False
                        elif x+K < N and arr[y][x+K] == 1:
                            fit_x = False
                        elif arr[y][x+i] == 1:
                            fit_x = True
                        else:
                            fit_x = False
                            break
                if y+K <= N:
                    for i in range(1, K):
                        if 0 <= y-1 and arr[y-1][x] == 1:
                            fit_y = False
                        elif y+K < N and arr[y+K][x] == 1:
                            fit_y = False
                        elif arr[y+i][x] == 1:
                            fit_y = True
                        else:
                            fit_y = False
                            break
            if fit_x:
                cnt += 1
            if fit_y:
                cnt += 1
    print(f'#{tc} {cnt}')
