z = [[0,0],[1,0],[2,0],[0,1],[0,2]]


def solution(board):
    bingo_O = 0
    bingo_X = 0
    for dz in range(5):
        dx, dy = z[dz]
        if board[dy][dx] == 'O':
            if dz == 0:
                if board[dy][dx] == board[1][1] == board[2][2]:
                    bingo_O += 1
                if board[dy][dx] == board[1][0] == board[2][0]:
                    bingo_O += 1
                if board[dy][dx] == board[0][1] == board[0][2]:
                    bingo_O += 1
            elif dz == 1:
                if board[dy][dx] == board[dy][1] == board[dy][2]:
                    bingo_O += 1
            elif dz == 2:
                if board[dy][dx] == board[dy][1] == board[dy][2]:
                    bingo_O += 1
                if board[dy][dx] == board[1][1] == board[dx][dy]:
                    bingo_O += 1
            elif 2 < dz <= 4:
                if board[dy][dx] == board[1][dx] == board[2][dx]:
                    bingo_O += 1
        elif board[dy][dx] == 'X':
            if dz == 0:
                if board[dy][dx] == board[1][1] == board[2][2]:
                    bingo_X += 1
                if board[dy][dx] == board[1][0] == board[2][0]:
                    bingo_X += 1
                if board[dy][dx] == board[0][1] == board[0][2]:
                    bingo_X += 1
            elif dz == 1:
                if board[dy][dx] == board[dy][1] == board[dy][2]:
                    bingo_X += 1
            elif dz == 2:
                if board[dy][dx] == board[dy][1] == board[dy][2]:
                    bingo_X += 1
                if board[dy][dx] == board[1][1] == board[dx][dy]:
                    bingo_X += 1
            elif 2 < dz <= 4:
                if board[dy][dx] == board[1][dx] == board[2][dx]:
                    bingo_X += 1

    cnt_O = 0
    cnt_X = 0

    for y in range(3):
        for x in range(3):
            if board[y][x] == 'O':
                cnt_O += 1
            if board[y][x] == 'X':
                cnt_X += 1
    if abs(cnt_O-cnt_X) > 1:
        return 0
    if cnt_O < cnt_X:
        return 0
    if bingo_O + bingo_X > 1:
        return 0
    if bingo_X and cnt_O != cnt_X:
        return 0
    return 1


board = ["OOO", "...", "..."]
print(solution(board))
