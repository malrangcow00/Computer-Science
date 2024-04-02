arr = [list(map(int, range(1,11))) for _ in range(10)]

for i in arr:
    print(i)

print()
# 대칭 행열로 변환
for y in range(10):
    for x in range(10):
        if x < y:
            arr[x][y], arr[y][x] = arr[y][x], arr[x][y]

for i in arr:
    print(i)

