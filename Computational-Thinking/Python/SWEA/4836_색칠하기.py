T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        # 문제의 조건에서 x1 < x2, y1 < y2이 주어졌다.
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if color == 1:
                    if arr[y][x] == 2 or arr[y][x] == 3:
                        arr[y][x] = 3
                    else:
                        arr[y][x] = 1
                if color == 2:
                    if arr[y][x] == 1 or arr[y][x] == 3:
                        arr[y][x] = 3
                    else:
                        arr[y][x] = 2
    cnt = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')