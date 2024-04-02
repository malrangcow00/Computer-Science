import sys
sys.stdin = open('input/4014.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        now_idx = 0
        v_len = 1
        need_plus = True
        for j in range(1, N):
            if graph[i][now_idx] == graph[i][j]:
                v_len += 1
            else:
                if graph[i][now_idx] < graph[i][j]:
                    val = v_len - (graph[i][j]-graph[i][now_idx])*X
                    if val < 0:
                        need_plus = False
                        break
                    v_len = 1
                    now_idx = j
                else:
                    val = v_len
                    if val < 0:
                        need_plus = False
                        break
                    v_len = 1 - (graph[i][now_idx]-graph[i][j])*X
                    now_idx = j
        if need_plus and v_len >= 0:
            ans += 1
        now_idx = 0
        v_len = 1
        need_plus = True
        for j in range(1, N):
            if graph[now_idx][i] == graph[j][i]:
                v_len += 1
            else:
                if graph[now_idx][i] < graph[j][i]:
                    val = v_len - X*(graph[j][i]-graph[now_idx][i])
                    if val < 0:
                        need_plus = False
                        break
                    v_len = 1
                    now_idx = j
                else:
                    val = v_len
                    if val < 0:
                        need_plus = False
                        break
                    v_len = 1 - X*(graph[now_idx][i]-graph[j][i])
                    now_idx = j
        if need_plus and v_len >= 0:
            ans += 1
    print(f'#{tc} {ans}')