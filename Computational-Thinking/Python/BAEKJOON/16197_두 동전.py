import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# N: 세로 크기, M: 가로 크기
N, M = map(int, input().split())

# 동전 A와 B의 위치 저장하고 같이 이동하기 !
# 동전이 서로 겹치는 경우는 바로 Cut

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

# # 동전의 위치 탐색 후 저장 -> 전역 설정하기 싫어서 함수 안에 집어 넣었다 ...
# nxt_coin = False
# explored = False
# for y in range(N):
#     if explored:
#         break
#     for x in range(M):
#         if nxt_coin and board[y][x] == 'o':
#             B_x = x
#             B_y = y
#             explored = True
#             break
#         elif board[y][x] == 'o':
#             A_x = x
#             A_y = y
#             nxt_coin = True

# # 방문배열 생성 -> 써먹어야 하는데 .. ?
# visited_A = [[0] * M for _ in range(N)]
# visited_B = [[0] * M for _ in range(N)]
# 각 동전마다 방문 배열을 2개 생성해서 사용 ... 하면 시간을 더 줄일 수 있을듯
# 벽을 만나는 조건에선 방문체크 하지 않기
# 1. 둘다 벽 만나
# 2. 하나만 벽 만나
# 길이 꼬여있는 경우가 있기 때문에 방문 조건을 A or B로 설정하여야 할듯 ...

# BFS -> 함수로 정의해서 최소값이 반환되도록 하자
def BFS():
    # 동전의 위치 탐색 후 저장
    nxt_coin = False
    explored = False
    for y in range(N):
        if explored:
            break
        for x in range(M):
            if nxt_coin and board[y][x] == 'o':
                B_x = x
                B_y = y
                explored = True
                break
            elif board[y][x] == 'o':
                A_x = x
                A_y = y
                nxt_coin = True
    coin = deque([[A_x, A_y, B_x, B_y, 0]])
    while coin:
        A_x, A_y, B_x, B_y, move_cnt = coin.popleft()
        for i in range(4):
            A_nx = A_x + dx[i]
            A_ny = A_y + dy[i]
            B_nx = B_x + dx[i]
            B_ny = B_y + dy[i]
            # 코인이 밖으로 나가는 경우
            # 1. 두 코인 모두 밖으로 나가는 경우
            if (A_nx < 0 or M <= A_nx or A_ny < 0 or N <= A_ny) and (B_nx < 0 or M <= B_nx or B_ny < 0 or N <= B_ny):
                continue
            # 2. 하나의 코인만 밖으로 나가는 경우 -> 목표 조건
            elif (A_nx < 0 or M <= A_nx or A_ny < 0 or N <= A_ny) or (B_nx < 0 or M <= B_nx or B_ny < 0 or N <= B_ny):
                if move_cnt+1 > 10:
                    return -1
                return move_cnt+1
            # 두 코인 모두 밖으로 나가지 않고 이동하는 경우
            if 0 <= A_nx < M and 0 <= A_ny < N and 0 <= B_nx < M and 0 <= B_ny < N:
            # 1. 코인이 이동하는 곳이 벽인 경우 (복합적으로 섞여야 한다)
                if board[A_ny][A_nx] == '#' and board[B_ny][B_nx] == '#':
                    continue
                # -> 한쪽이 벽을 만나 동전이 서로 겹치는 경우 (두 동전이 함께 움직이면 안되기 때문에 바로 제외)
                elif board[A_ny][A_nx] == '#':
                    if (A_nx, A_ny) != (B_nx, B_ny):
                        if move_cnt+1 <= 10:
                            coin.append([A_x, A_y, B_nx, B_ny, move_cnt+1])
                elif board[B_ny][B_nx] == '#':
                    if (A_nx, A_ny) != (B_nx, B_ny):
                        if move_cnt+1 <= 10:
                            coin.append([A_nx, A_ny, B_x, B_y, move_cnt+1])
                # 2. 벽을 만나지 않고 이동하는 경우
                else:
                    if move_cnt+1 <= 10:
                        coin.append([A_nx, A_ny, B_nx, B_ny, move_cnt+1])

    # 두 동전을 떨어뜨릴 수 없는 경우
    return -1

print(BFS())
