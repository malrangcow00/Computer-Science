import sys
sys.stdin = open('input/4047.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    cards = list(input())
    result = [[], [], [], []] # S D H C
    shape = ['S', 'D', 'H', 'C']
    while cards:
        card = []
        for _ in range(3):
            card.append(cards.pop(0))
        result[shape.index(card[0])].append(''.join(card))
    for _ in range(4):
        if len(result[_]) != len(set(result[_])):
            result = 'ERROR'
            break
        else:
            result[_] = 13 - len(result[_])
    if result != 'ERROR':
        print(f'#{tc}', *result)
    else:
        print(f'#{tc} {result}')