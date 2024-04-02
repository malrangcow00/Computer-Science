import sys
sys.stdin = open('input/16546.txt', 'r')

def check(arr):
    global cards
    # run - run 6장
    for i in range(0, 10):
        cards[0] = cards[1] = cards[2] = i
        for j in range(i, 10):
            cards[3] = cards[4] = cards[5] = j
            # <- 이 부분에서 순열 가짓수를 만들어서 테스트 (6P6)
            tmp = sorted(cards)
            if arr == tmp:
                return 'true'
    # run - tri 6장
    for i in range(0, 7):
        cards[0] = cards[1] = cards[2] = i
        for j in range(0, 8):
            cards[3] = j
            cards[4] = j + 1
            cards[5] = j + 2
            # <- 이 부분에서 순열 가짓수를 만들어서 테스트 (6P6)
            tmp = sorted(cards)
            if arr == tmp:
                return 'true'
    # tri - tri 6장
    for i in range(0, 8):
        cards = [0] * 6
        cards[0] = i
        cards[1] = i + 1
        cards[2] = i + 2
        for j in range(0, 8):
            cards[3] = j
            cards[4] = j + 1
            cards[5] = j + 2
            # <- 이 부분에서 순열 가짓수를 만들어서 테스트 (6P6)
            tmp = sorted(cards)
            if arr == tmp:
                return 'true'
    return 'false'

T = int(input())
for tc in range(1, T + 1):
# for tc in range(1):
    arr = list(map(int, list(input())))
    arr.sort()
    cards = [0] * 6
    print(f'#{tc}', check(arr))