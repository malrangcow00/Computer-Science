# import sys
# sys.stdin = open('input/16811.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1. 상자 종류는 소 중 대 3종류 로 포장
    # 2. 같은 크기의 당근은 같은 상자에
    # 3. 비어 있는 상자가 있으면 안 된다.
    # 4. 한 상자에 N/2개를 초과하는 당근이 있으면 안된다.
    # 5. 각 상자에 든 당근의 개수 차이가 최소가 되어야 한다.
    result = 0
    carrots = list(map(int, input().split()))
    carrots.sort()

    small = []
    middle = []
    large = []

    try:
        small.append(carrots.pop(0))
        i = 0
        while carrots and small[i] == carrots[0]:
            small.append(carrots.pop(0))
            i += 1
        middle.append(carrots.pop(0))
        i = 0
        while carrots and middle[i] == carrots[0]:
            middle.append(carrots.pop(0))
            i += 1
        large.append(carrots.pop(0))
        i = 0
        while carrots and large[i] == carrots[0]:
            large.append(carrots.pop(0))
    except:
        print(f'#{tc} -1')
        continue

    while carrots:
        if carrots and len(large) == min([len(small), len(middle), len(large)]):
            i = len(large)
            large.append(carrots.pop(0))
            while carrots and large[i] == carrots[0]:
                large.append(carrots.pop(0))
                i += 1
        if large and len(middle) == min([len(small), len(middle), len(large)]):
            i = len(middle)
            middle.append(large.pop(0))
            while large and middle[i] == large[0]:
                middle.append(large.pop(0))
                i += 1
        if middle and len(small) == min([len(small), len(middle), len(large)]):
            i = len(small)
            small.append(middle.pop(0))
            while middle and small[i] == middle[0]:
                small.append(middle.pop(0))
                i += 1

    result = max([abs(len(small) - len(middle)), abs(len(small) - len(large)), abs(len(middle) - len(large))])

    if max([len(small), len(middle), len(large)]) > N//2:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {result}')

    # 화장실 다녀왔는데 춘식이가 그랬어요
