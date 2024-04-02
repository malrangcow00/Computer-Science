import sys
sys.stdin = open('SWEA.input/9489.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for y in range(N):
        stack = []
        for i in arr[y]:
                if i == 1:
                    stack.append(i)
                else:
                    mx = max(mx, sum(stack))
                    stack.clear()
                mx = max(mx, sum(stack))
    for x in range(M):
         stack = []
         for y in range(N):
            if arr[y][x] == 1:
                stack.append(1)
            else:
                mx = max(mx, sum(stack))
                stack.clear()
            mx = max(mx, sum(stack))

    print(f'#{tc} {mx}')