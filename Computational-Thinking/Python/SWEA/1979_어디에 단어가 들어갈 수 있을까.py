import sys
sys.stdin = open('input/1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N : N * N 크기의 단어 퍼즐 (5 <= N <= 15)
    # K : 길이가 K인 단어가 들어갈 수 있는 자리 (2 <= K <= N)
    arr_1 = [list(map(int, input().split())) for _ in range(N)]
    arr_2 = [arr_1[_][:] for _ in range(N)]

    # 카운트
    cnt = 0

    # 가로 길이 판별
    for y in range(N):
        for x in range(N):
            if (x == N-1) or (arr_1[y][x+1] == 0):
                if arr_1[y][x] == K:
                    cnt += 1
                if x == N-1:
                    continue
            if arr_1[y][x] != 0 and arr_1[y][x+1] == 1:
                arr_1[y][x+1] += arr_1[y][x]
                arr_1[y][x] = 0

    # 세로 길이 판별
    for x in range(N):
        for y in range(N):
            if (y == N-1) or (arr_2[y+1][x] == 0):
                if arr_2[y][x] == K:
                    cnt += 1
                if y == N-1:
                    continue
            if arr_2[y][x] != 0 and arr_2[y+1][x] == 1:
                arr_2[y+1][x] += arr_2[y][x]
                arr_2[y][x] = 0

    # 출력
    print(f'#{tc} {cnt}')