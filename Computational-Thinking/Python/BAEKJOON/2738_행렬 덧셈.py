N, M = map(int, input().split())

arr_A = [list(map(int, input().split())) for i in range(N)]
arr_B = [list(map(int, input().split())) for i in range(N)]

for y in range(N):
    for x in range(M):
        arr_A[y][x] = arr_A[y][x] + arr_B[y][x]

for i in range(N):
    print(*arr_A[i])