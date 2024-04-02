import sys
sys.stdin = open('input/5656.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    # N : 시행 횟수
    # W : 너비
    # H : 높이
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    for y in range(H):
        for x in range(W):
            arr_tmp = arr[:]
            chain(x, y)
            for j in range(W):
                cnt = 0
                for i in range(-1, -H-1):
                    if arr_tmp[i][j] == 0:

                        cnt = 0
                    else:
                        cnt +=1







    result = 0

    print(f'#{tc} {result}')

def chain(x, y):
    n = arr[y][x]
    if n == 0:
        return
    for i in range(4):
        if n > 1:
            for j in range(1, n):
                nx, ny = x + j*dx[i], y + j*dy[i]
                chain(nx, ny)
                arr[ny][nx] = 0
        else:
            arr[y][x] = 0

# 세로로 덜어질때 탐색하는 방법까지 포함해서 함수 작성
# W^3 에 해당하는 과정을 함수로 반복시킨다