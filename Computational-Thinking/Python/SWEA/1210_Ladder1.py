import sys
sys.stdin = open('input/1210.txt', 'r')
for tc in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    player_coordinate = [arr[99].index(2), 99]
    while player_coordinate[1] > 0:
        is_moving_left = False
        while 0 <= player_coordinate[0] - 1 and arr[player_coordinate[1]][player_coordinate[0] - 1] == 1:
            player_coordinate[0] -= 1
            is_moving_left = True
        if not is_moving_left:
            while player_coordinate[0] + 1 < 100 and arr[player_coordinate[1]][player_coordinate[0] + 1] == 1:
                player_coordinate[0] += 1
        player_coordinate[1] -= 1
    print(f'#{tc} {player_coordinate[0]}')