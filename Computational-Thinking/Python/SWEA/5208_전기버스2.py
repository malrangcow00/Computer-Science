import sys
sys.stdin = open('input/5208.txt', 'r')

def DFS(cnt, N):
    global mn
    if cnt > mn:
        return
    elif N >= distance:
        mn = min(mn, cnt)
        return
    for i in range(M[N], 0, -1):
        DFS(cnt+1, N+i)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = arr[1:]
    distance = N - 1
    mn = 100
    DFS(-1, 0)
    print(f'#{tc} {mn}')