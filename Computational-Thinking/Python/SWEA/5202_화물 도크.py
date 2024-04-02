import sys
sys.stdin = open('input/5202.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x:x[1])
    cnt = 0
    j = 0
    for i in range(N):
        if times[i][0] >= j:
            cnt += 1
            j = times[i][1]
    print(f'#{tc} {cnt}')