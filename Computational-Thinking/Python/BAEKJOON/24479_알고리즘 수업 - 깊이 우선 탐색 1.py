import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    global cnt
    visited[start] = cnt
    for i in node[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, sys.stdin.readline().split())
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    node[u].append(v)
    node[v].append(u)
for _ in range(N):
    node[_].sort()

dfs(R)

for _ in range(1, N+1):
    print(visited[_])