a, b, c, d, e, f = map(int, input().split())

# -999<= a, b, c, d, e, f, x, y <= 999

cnt = 0
for y in range(-999, 1000):
    for x in range(-999, 1000):
        if a*x+b*y == c and d*x+e*y==f:
            cnt += 1
            sol_x, sol_y = x, y
if cnt == 1:
    print(sol_x, sol_y)
