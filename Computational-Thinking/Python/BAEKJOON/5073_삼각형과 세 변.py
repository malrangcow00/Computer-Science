while True:
    tri = list(map(int, input().split()))
    if tri == [0]*3:
        break
    elif 2*max(tri) >= sum(tri):
        print('Invalid')
    elif len(set(tri)) == 1:
        print('Equilateral')
    elif len(set(tri)) == 2:
        print('Isosceles')
    else:
        print('Scalene')