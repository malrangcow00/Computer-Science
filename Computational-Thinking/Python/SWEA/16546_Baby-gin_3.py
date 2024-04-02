import sys
sys.stdin = open('input/16546.txt', 'r')

def check():
    i = g = 0
    while i < 8:
        if g == 2:
            return 'true'
            break
        elif c[i] >= 3:
            c[i], g = c[i] - 3, g + 1
        elif c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i], c[i+1], c[i+2], g = c[i]-1, c[i+1]-1, c[i+2]-1, g + 1
        else:
            i += 1
    return 'false'

for tc in range(1, int(input().strip()) + 1):
    N = int(input().strip())
    c = [0] * 10
    for i in range(6):
        c[N % 10] += 1
        N //= 10
    print(f'#{tc} {check()}')