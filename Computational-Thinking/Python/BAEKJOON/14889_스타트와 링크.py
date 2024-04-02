import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
mn = 4000

def DFS(cnt, idx):
    global mn
    if cnt == N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        mn = min(mn, abs(start-link))
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            DFS(cnt+1,i+1)
            visited[i] = False

DFS(0,0)
print(mn)


















# 시간초과
# import sys
# input = sys.stdin.readline
#
# def clac_total(team_start, team_link):
#     start = 0
#     link = 0
#     for i in range(N//2-1):
#         for j in range(i+1, N//2):
#             start += arr[team_start[i]][team_start[j]] + arr[team_start[j]][team_start[i]]
#             link += arr[team_link[i]][team_link[j]] + arr[team_link[j]][team_link[i]]
#     return abs(start - link)
#
#
# def selection(depth, i):
#     global mn
#     if sum(team) == N//2:
#         team_start = []
#         team_link = []
#         for i in range(N):
#             if team[i] == 0:
#                 team_start.append(i)
#             else:
#                 team_link.append(i)
#         mn = min(mn, clac_total(team_start, team_link))
#     else:
#         for _ in range(i+1, N):
#             team[_] = 1
#             selection(depth+1, i+1)
#             team[_] = 0
#             selection(depth, i+1)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# team = [0] * N
# mn = 4000
# selection(0, -1)
# print(mn)