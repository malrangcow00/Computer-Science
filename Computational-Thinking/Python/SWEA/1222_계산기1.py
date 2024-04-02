import sys
sys.stdin = open('input/1222.txt', 'r')

for tc in range(1, 11):
    input()
    arr = list(map(int, input()[::2]))
    print(f'#{tc} {sum(arr)}')
