import sys
sys.stdin = open('input/2805.txt', 'r')

# # """
# # 1
# # 5
# # 14054
# # 44250
# # 02032
# # 51204
# # 52212
# # """
# #
# # T = int(input())
# # for tc in range(1, T + 1):
# #     # 입력
# #     # 농작물 밭의 한변의 길이 N
# #     N = int(input())
# #     # N * N 사이즈의 농작물 배열
# #     arr = [list(map(int, input())) for _ in range(N)]
# #
# #     # 로직
# #     # 다이아몬드 형태로 순회
# #     # 누적합...
# #     total = 0
# #
# #     # 중간점
# #     M = N // 2
# #     s = e = M
# #
# #     for i in range(N):  # 0 -> 4
# #         # s -> e 순회..
# #         for j in range(s, e + 1):  # 2 -> 2
# #             total += arr[i][j]
# #         # 중간 지점을 도달할 때까지
# #         if i <= M:
# #             s -= 1
# #             e += 1
# #         else: # i > M
# #             s += 1
# #             e -= 1
# #
# #     # 출력
# #     print(f"#{tc} {total}")
# """
# 1
# 5
# 14054
# 44250
# 02032
# 51204
# 52212
# """
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # 농작물 밭의 한변의 길이 N
#     N = int(input())
#     # N * N 사이즈의 농작물 배열
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # 로직
#     # 다이아몬드 형태로 순회
#     # 누적합...
#     total = 0
#
#     # 중간점
#     M = N // 2
#     k = 0  # +- 추가되는 범위
#
#     for i in range(N):  # 0 -> 4
#         # (M - k) -> (M + k) 순회..
#         for j in range(M - k, M + k + 1):
#             total += arr[i][j]
#         # 중간 지점을 도달할 때까지
#         if i <= M:
#             k += 1
#         else:  # i > M
#             k -= 1
#
#     # 출력
#     print(f"#{tc} {total}")


# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # 농작물 밭의 한변의 길이 N
#     N = int(input())
#     # N * N 사이즈의 농작물 배열
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # 로직
#     # 다이아몬드 형태로 순회
#     # 누적합...
#     total = 0
#
#     # 중간점
#     M = N // 2
#
#     for i in range(N):
#         for j in range(N):
#             # (i, j)좌표 <ㅡ> (M, M) 좌표 <= M : 수확 가능!
#             if abs(i - M) + abs(j - M) <= M:
#                 total += arr[i][j]
#
#     # 출력
#     print(f"#{tc} {total}")

# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # 농작물 밭의 한변의 길이 N
#     N = int(input())
#     # N * N 사이즈의 농작물 배열
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # 로직
#     # 다이아몬드 형태로 순회
#     # 누적합...
#     total = 0
#
#     # 중간점
#     M = N // 2
#     k = 0  # +- 추가되는 범위
#
#     for i in range(N):  # 0 -> 4
#         # (M - k) -> (M + k) 순회..
#         for j in range(M - k, M + k + 1):
#             total += arr[i][j]
#         # 중간 지점을 도달할 때까지
#         if i <= M:
#             k += 1
#         else:  # i > M
#             k -= 1
#
#     # 출력
#     print(f"#{tc} {total}")

# di, dj 델타값.. (상하좌우 델타값)
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


# 사방탐색 진행
def dfs(i, j, depth):
    global total

    # 기저조건
    if depth == M:
        return

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:  # 배열 바깥을 나갔는지 체크
            total += arr[ni][nj]
            dfs(ni, nj, depth + 1)


T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 농작물 밭의 한변의 길이 N
    N = int(input())
    # N * N 사이즈의 농작물 배열
    arr = [list(map(int, input())) for _ in range(N)]

    # 로직
    # 다이아몬드 형태로 순회
    # 누적합...
    total = 0

    # 중간점
    M = N // 2

    # 방문 체크를 위한 visited 배열
    visited = [[False] * N for _ in range(N)]

    # (M, M) 좌표는 미리 방문하고, total 값으로 추가...!
    visited[M][M] = True
    total += arr[M][M]

    # (M, M) 좌표를 시작으로 하여 M 만큼 사방탐색 DFS 진행...
    dfs(M, M, 0)

    # 출력
    print(f"#{tc} {total}")