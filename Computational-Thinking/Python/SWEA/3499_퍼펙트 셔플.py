import sys
sys.stdin = open('input/3499.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    if N % 2 != 0:
        num = 'odd'
        mid = N // 2 + 1
    else:
        num = 'even'
        mid = N // 2

    fore = cards[:mid]
    back = cards[mid:]

    print(f'#{tc}', end=' ')
    if num == 'odd':
        for i in range(mid-1):
            print(fore[i], end=' ')
            print(back[i], end=' ')
        print(fore[mid-1], end=' ')
    else:
        for i in range(mid):
            print(fore[i], end=' ')
            print(back[i], end=' ')
    print()


