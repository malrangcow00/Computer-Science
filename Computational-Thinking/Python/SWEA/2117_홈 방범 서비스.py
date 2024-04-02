import sys
sys.stdin = open('input/2142.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ppl = 0
    for _ in arr:
        ppl += sum(_)
    k = 1
    while k <= N + 1:
        k += 1
        mx_cnt = 1
        for y in range(N):
            for x in range(N):
                cnt = 0
                for ny in range(N):
                    for nx in range(N):
                        if arr[ny][nx] == 1 and abs(nx-x) + abs(ny-y) < k:
                            cnt += 1
                mx_cnt = max(mx_cnt, cnt)
    print(f'#{tc} {mx_cnt}')