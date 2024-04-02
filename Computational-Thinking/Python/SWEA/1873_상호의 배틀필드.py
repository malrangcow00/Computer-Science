import sys
sys.stdin = open('input/1873.txt', 'r')
# sys.stdout = open('output/test.txt', 'w')

def move(player_coordinate, state):
    nx = player_coordinate[0] + dx[dir.index(state)]
    ny = player_coordinate[1] + dy[dir.index(state)]
    if 0 <= nx < W and 0 <= ny < H and arr[ny][nx] == '.':
        player_coordinate[0] = nx
        player_coordinate[1] = ny

def shoot(player_coordinate, state):
    nx = player_coordinate[0] + dx[dir.index(state)]
    ny = player_coordinate[1] + dy[dir.index(state)]
    while True:
        if 0 <= nx < W and 0 <= ny < H and (arr[ny][nx] == '-' or arr[ny][nx] == '.'):
            nx = nx + dx[dir.index(state)]
            ny = ny + dy[dir.index(state)]
            continue
        elif 0 <= nx < W and 0 <= ny < H and arr[ny][nx] == '*':
            arr[ny][nx] = '.'
            break
        break

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    input()
    command = list(input())

    cmd = ['U', 'R', 'D', 'L']
    dir = ['^', '>', 'v', '<']
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    player_coordinate = [0, 0]
    for y in range(H):
        for x in range(W):
            if arr[y][x] in dir:
                player_coordinate[0] = x
                player_coordinate[1] = y
                state = arr[y][x]
                arr[y][x] = '.'

    while command:
        if command[0] in cmd:
            state = dir[cmd.index(command[0])]
            move(player_coordinate, state)
        else:
            shoot(player_coordinate, state)
        command = command[1:]

    arr[player_coordinate[1]][player_coordinate[0]] = state

    print(f'#{tc} ', end='')
    for _ in arr:
        print(''.join(_))