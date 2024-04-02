import sys
sys.stdin = open('SWEA.input/16432.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    
    N = int(input())

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    arr = [list(map(int, input().split()))for _ in range(N)]

    stack = []
    for y in range(1, N-1):
        for x in range(1, N-1):
            top = False
            for i in range(8):
                if arr[y][x] <= arr[y+dy[i]][x+dx[i]]:
                    top = False
                    break
                top = True
            if top == True:
                stack.append(arr[y][x])


    if len(stack) > 1:
        result = max(stack) - min(stack)
    elif len(stack) < 2:
        result = -1

    print(f'#{tc} {result}')