import sys
sys.stdin = open('input/10966.txt', 'r')
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pool = list(list(map(int, list(input().rstrip().replace('W', '0').replace('L', '1')))) for _ in range(N))
    cnt = 2
    state = True
    for y in range(N):
        for x in range(M):
            if pool[y][x] == 0:
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < M and 0 <= ny < N and pool[ny][nx] == 1:
                        pool[ny][nx] = cnt
                        cnt += 1
        print(pool)
        # for y in range(N):
        #     for x in range(M):
        #         if pool[y][x] == 0:
        #             break
        #         else:
        #             state = False





    print(pool)


