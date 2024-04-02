import sys
sys.stdin = open('input/2007.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = input()
    i = 1
    j = 1
    # 첫 알파벳이 여러번 중복되는 경우 히든 케이스
    while i <= len(text[j*i:]):
        if text[:i] == text[i:2*i] == text[j*i:(1+j)*i]:
            j += 1
        else:
            i += 1
            j = 1
    print(f'#{tc} {i}')