import sys
sys.stdin = open('input/2805.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    distance = (N+1)//2
    income = arr[0][distance]
    for y in range(N):
        for x in range(N):
            if x + y == distance:
                income += arr[y][x]
    print(f'#{tc} {income}')