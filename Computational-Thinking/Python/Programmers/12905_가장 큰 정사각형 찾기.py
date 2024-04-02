def solution(board):
    # board는 정사각형이 아니었습니다...
    n = len(board)
    m = len(board[0])
    answer = 0

    # 2차원 배열 탐색
    for y in range(n):
        for x in range(m):
            if y > 0 and x > 0 and board[y][x] == 1:
                # 왼쪽 위 대각선, 왼쪽, 위쪽 중 가장 작은 값 비교 후 + 1
                board[y][x] = min(board[y-1][x-1], board[y-1][x], board[y][x-1]) + 1
                answer = max(answer, board[y][x])
            else:
                answer = max(answer, board[y][x])

    return answer ** 2

