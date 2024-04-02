N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상인 경우
for i in range(N): # 모든 원소 arr[i][j]에 대해 ..
    for j in range(N):
        # arr[i][j]중심으로
        s = arr[i][j]
        # for k in range(4):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj <N: # 배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:


max_v = 0
for i in range(N):
    for j in range(N):
        # arr[i][j]중심으로
        s = arr[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: