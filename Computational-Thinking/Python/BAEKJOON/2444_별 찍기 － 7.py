T = int(input())

for i in range(1, T+1):
    print(' ' * (T-i), end='')
    print('*' * (2 * i-1))

for i in range(T-1, 0, -1):
    print(' ' * (T-i), end='')
    print('*' * (2 * i-1))