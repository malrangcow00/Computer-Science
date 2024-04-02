dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(r, c):
    global graph
    res = 1
    graph[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < N and nc >= 0 and nc < N:
            if graph[nr][nc] == 1:
                res += dfs(nr, nc)
    return res

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
ans = []
for i in range(0, N):
    for j in range(0, N):
        if graph[i][j]:
            ans.append(dfs(i, j))
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])