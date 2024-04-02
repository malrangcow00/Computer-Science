import sys
input = sys.stdin.readline
from collections import deque


def DFS(V):
    visited[V] = 1
    print(V, end=' ')
    for i in nodes[V]:
        if not visited[i]:
            DFS(i)


def BFS(V):
    queue = deque([V])
    visited[V] = 1
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in nodes[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())

nodes = [[] * (N + 1) for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1, N+1):
    nodes[i].sort()

visited = [0] * (N + 1)
DFS(V)
print()

visited = [0] * (N + 1)
BFS(V)