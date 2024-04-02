import sys
sys.stdin = open('input/6190.txt', 'r')

def is_monoincrease(num):
    text = str(num)
    for _ in range(1, len(text)):
        if int(text[_]) >= int(text[_-1]):
            continue
        else:
            return False
    return True

# 테스트 케이스 개수 입력
T = int(input())
for tc in range(1, T+1):
    # 숫자의 개수 입력
    N = int(input())
    # 배열 입력
    arr = list(map(int, input().split()))
    # 곱의 합을 넣어줄 리스트 생성
    lst = []
    for i in range(N-1):
        for j in range(i + 1, N):
            lst.append(arr[i]*arr[j])
    mx = -1
    for num in lst:
        if is_monoincrease(num) and mx < num:
            mx = num
    print(f'#{tc} {mx}')

