import sys
sys.stdin = open('input/11315.txt', 'r')

dx = [1, 1, 0, -1]
dy = [0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(input().strip()) for _ in range(N)]
    complete = False
    for y in range(N):
        for x in range(N):
            if table[y][x] == 'o':
                for i in range(4):
                    for j in range(1, 5):
                        nx = x+j*dx[i]
                        ny = y+j*dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if table[ny][nx] == 'o':
                                complete = True
                            else:
                                complete = False
                                break
                        else:
                            complete = False
                            break
                    if complete:
                        break
                if complete:
                    break
        if complete:
            break
    if complete:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')