import sys
sys.stdin = open('input/7087.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    alphabetic = []
    for _ in range(N):
        alphabetic.append(ord(input()[0]))
    alphabetic = list(set(alphabetic))
    if alphabetic[0] == ord('A'):
        i = 1
        while i < len(alphabetic):
            if alphabetic[i] == alphabetic[i-1] + 1:
                i += 1
            else:
                break
        print(f'#{tc} {i}')
    else:
        print(f'#{tc} 0')
