import sys
sys.stdin = open('SWEA.input/1989.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    word = input()
    upset = word[::-1]
    ans = 1
    for _ in range(len(word)):
        if word[_] != upset[_]:
            ans = 0
            break

    print(f'#{tc} {ans}')
        