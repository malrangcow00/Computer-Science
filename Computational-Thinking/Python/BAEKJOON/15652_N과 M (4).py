import sys
input = sys.stdin.readline

def dfs(i):
    if len(selection) == M:
        print(' '.join(map(str, selection)))
        return
    for _ in range(i, N+1):
        selection.append(_)
        dfs(_)
        selection.pop()

N, M = map(int, input().split())
selection = []
dfs(1)