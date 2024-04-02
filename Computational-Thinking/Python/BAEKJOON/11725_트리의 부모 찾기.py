import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def DFS(start):
    for i in nodes[start]:
        if not visited[i]:
            visited[i] = 1
            parents[i] = start
            DFS(i)

N = int(input())
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)
parents = [0] * (N + 1)
visited = [0] * (N + 1)
visited[1] = 1
DFS(1)

for _ in range(2, N+1):
    print(parents[_])