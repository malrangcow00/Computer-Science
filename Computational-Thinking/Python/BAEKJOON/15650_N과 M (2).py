import sys
input = sys.stdin.readline

def dfs(i):
    if len(selection) == M:
        print(' '.join(map(str, selection)))
        return
    for _ in range(i, N+1):
        if _ not in selection:
            selection.append(_)
            dfs(_+1)
            selection.pop()

N, M = map(int, input().split())
selection = []
dfs(1)