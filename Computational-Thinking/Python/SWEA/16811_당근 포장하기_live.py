import sys
sys.stdin = open('input/16811.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    packing = False
    mn = 1000
    for i in range(1, N-1):
        for j in range(i+1, N):
            small = arr[:i]
            middle = arr[i:j]
            large = arr[j:]
            if set(small) & set(middle) or set(small) & set(large) or set(middle) & set(large):
                continue
            elif len(small) > N//2 or len(middle) > N//2 or len(large) > N//2:
                continue
            tmp = max([abs(len(small) - len(middle)), abs(len(small) - len(large)), abs(len(middle) - len(large))])
            mn = min(mn, tmp)
            packing = True
    if packing:
        print(f'#{tc} {mn}')
    else:
        print(f'#{tc} -1')