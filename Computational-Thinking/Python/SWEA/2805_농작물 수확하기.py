import sys
sys.stdin = open('input/2805.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    start_x = N//2
    income = arr[0][start_x]
    dx = -1
    lx = start_x
    rx = start_x + 1
    for y in range(1, N):
        if y == N//2+1:
            dx = 1
        lx = lx + dx
        rx = rx - dx
        for x in range(lx, rx):
            income += arr[y][x]
    print(f'#{tc} {income}')