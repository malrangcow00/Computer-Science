import sys
sys.stdin = open('SWEA.input/5432.txt', 'r')

# SWEA.input TestCase
T = int(input())

for tc in range(1, T+1):
    # arr of laser and bar on the table
    full = input()
    # transform laser into '|'
    full = full.replace('()', '|')
    # number of raw bars on the current point
    i = 0
    # number of all bars on the current point
    j = 0
    # number of accumulated bar pieces
    cnt = 0
    # current point on the table
    for _ in full:
        if _ == '(':
            i += 1
            j += 1
        elif _ == '|':
            cnt += i+j
            i = 0
        else:
            if i > 0:
                i -= 1
            j -= 1
    # SWEA.output
    print(f'#{tc} {cnt}')