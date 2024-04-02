import sys
sys.stdin = open('input/5186.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    i = 1
    while i < 14:
        if N == 0:
            break
        elif N >= 2**(-1*i):
            result += str(int(N // 2**(-1*i)))
            N %= 2**(-1*i)
        else:
            result += '0'
        i += 1
    if len(result) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')