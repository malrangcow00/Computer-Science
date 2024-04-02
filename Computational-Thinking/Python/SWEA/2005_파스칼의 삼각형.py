import sys
sys.stdin = open('SWEA.input/2005.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+1) for _ in range(N+1)]

    arr[1][1] = 1
    for y in range(2, N+1):
        for x in range(1, y+1):
            arr[y][x] = arr[y-1][x-1] + arr[y-1][x]
    
    print(f'#{tc}')
    for y in range(1, N+1):
        for x in range(1, y+1):
            print(arr[y][x], end=' ')
        print()

