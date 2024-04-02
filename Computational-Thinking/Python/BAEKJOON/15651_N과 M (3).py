import sys
input = sys.stdin.readline

def dfs():
    if len(selection) == M:
        print(' '.join(map(str, selection)))
        return
    for _ in range(1, N+1):
        selection.append(_)
        dfs()
        selection.pop()

N, M = map(int, input().split())
selection = []
dfs()