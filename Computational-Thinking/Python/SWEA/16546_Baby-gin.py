import sys
sys.stdin = open('input/16546.txt', 'r')

T = int(input())
# for tc in range(1, T+1):
for tc in range(1, 2):
    cards = list(map(int, list(input())))
    for i in cards:
        cnt = cars.count(i)
        if cnt == 6:
            result = 'true'
        elif cnt == 5:
            result = 'false'
        elif cnt == 4 or cnt == 3:
            for j in range(3):
                cards.remove(i)
            cards.sort()
            if list(range(cards[0],cards[0]+3))) == cards:
                result = 'true'
            else:
                result = 'false'
        elif cnt == 2:
            for j in range()





