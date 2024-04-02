import sys
sys.stdin = open('input/4613.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    mn = 2500
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for w in range(i+1):
                cnt += M - arr[w].count('W')
            for b in range(i+1, j+1):
                cnt += M - arr[b].count('B')
            for r in range(j+1, N):
                cnt += M - arr[r].count('R')
            mn = min(mn, cnt)
    print(f'#{tc} {mn}')