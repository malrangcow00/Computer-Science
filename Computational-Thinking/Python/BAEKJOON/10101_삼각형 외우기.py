lst = [int(input()) for i in range(3)]

if sum(lst) != 180:
    print('Error')
elif len(set(lst)) == 1:
    print('Equilateral')
elif len(set(lst)) == 2:
    print('Isosceles')
else:
    print('Scalene')