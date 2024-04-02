import sys
sys.stdin = open('SWEA.input/1219.txt', 'r')

def dfs(s):
    global visited
    visited[s] = 1
    for e in range(len(arr_dir[s])):
        if arr_dir[s][e] == 1:
            if visited[e] == 1:
                continue
            dfs(e)

while True:
    try:
        tc, N = map(int, input().split())
        arr_dir = [[0] * 100 for _ in range(100)]
        arr_tmp = list(map(int, input().split()))
        for i in range(0, 2*N, 2):
            arr_dir[arr_tmp[i]][arr_tmp[i+1]] = 1

        visited = [0] * 100

        result = 0

        dfs(0)

        if visited[99] == 1:
            result = 1

        print(f'#{tc} {result}')
    except EOFError:
        break