import sys
sys.stdin = open('input/16780.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, text = input().split()
    bin = ''
    for _ in text:
        bin += format(int(_, 16), 'b').zfill(4)
    print(f'#{tc} {bin}')