import sys
sys.stdin = open('input/1865.txt', 'r')

def recursive(worker,p):
    global mx
    if worker == N:
        mx = p
        return
    for work in range(N):
        if not visit[work] and p * (arr[worker][work]/100) > mx:
            visit[work] = 1
            recursive(worker+1, p * (arr[worker][work]/100))
            visit[work] = 0
            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    visit = [0] * N
    recursive(0, 1)
    mx *= 100
    print(f'#{tc} {mx:.6f}')