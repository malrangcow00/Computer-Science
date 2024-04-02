import sys
sys.stdin = open('input/2819.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, depth):
    if depth == 7:
        comb.add(''.join(tmp))
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                tmp.append(str(arr[ny][nx]))
                dfs(nx, ny, depth+1)
                tmp.pop()

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    comb = set()
    for y in range(4):
        for x in range(4):
            tmp = [str(arr[y][x])]
            dfs(x, y, 1)
    print(f'#{tc} {len(comb)}')