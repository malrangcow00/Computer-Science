import sys
sys.stdin = open("SWEA.test.txt", "r")

for T in range(1, 11):
    tc = int(input())
    two_dimensions = []
    for i in range(100):
        row = list(map(int, input().split()))
        two_dimensions.append(row)

    row_mx = sum(two_dimensions[0])
    for i in range(100):
        if row_mx < sum(two_dimensions[i]):
            row_mx = sum(two_dimensions[i])

    col_mx = 0
    for i in range(100):
        col_mx_temp = 0
        for j in range(100):
            col_mx_temp += two_dimensions[j][i]
        if col_mx_temp > col_mx:
            col_mx = col_mx_temp

    dia_mx_1 = 0
    for i in range(100):
        dia_mx_1 += two_dimensions[i][i]

    dia_mx_2 = 0
    for i in range(100):
        dia_mx_2 += two_dimensions[i][99-i]

    mx_sum = max(row_mx, col_mx, dia_mx_1, dia_mx_2)

    print(f'#{T} {mx_sum}')