import sys
sys.stdin = open('input/1220.txt', 'r')

for tc in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    for y in range(100):
        for x in range(100):
            if x < y:
                arr[x][y], arr[y][x] = arr[y][x], arr[x][y]

    # N : 1 (index : 99로 향한다)
    # S : 2 (index : 0으로 향한다)
    cnt = 0
    for y in range(100):
        out = True
        while arr[y]: # 범위 수정
            magnetic = arr[y].pop(0)
            if out == True:
                if magnetic == 1:
                    out = False
            elif out == False:
                if magnetic == 2:
                    out = True
                    cnt += 1
    print(f'#{tc} {cnt}')