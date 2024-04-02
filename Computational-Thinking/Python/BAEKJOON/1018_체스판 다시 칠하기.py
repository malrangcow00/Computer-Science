N, M = map(int, input().split())

def check_88(arr_88):
    main_checker = arr_88[0][0]
    if main_checker == 'B':
        sub_checker = 'W'
    else:
        sub_checker = 'B'
    cnt = 0
    for y in range(8):
        for x in range(8):
            if (y+x) % 2 == 0:
                if arr_88[y][x] == main_checker:
                    cnt += 1
            else:
                if arr_88[y][x] == sub_checker:
                    cnt += 1
    return min(cnt, 64-cnt)

arr = [list(map(str, input())) for _ in range(N)]

mn = 8*8//2
for y in range(N-7):
    for x in range(M-7):
        arr_88 = []
        for i in range(8):
            arr_88_col = []
            for j in range(8):
                    arr_88_col.append(arr[y+i][x+j])
            arr_88.append(arr_88_col)
        mn = min(mn, check_88(arr_88))
print(mn)