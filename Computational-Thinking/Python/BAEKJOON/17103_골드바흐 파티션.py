import sys
input = sys.stdin.readline

# 배열 내 소수 판단
def is_prime(num):
    if num == 2:
        return True
    for j in range(3, int(num**0.5)+1):
        if num % j == 0:
            return False
    return True

# 에라토스테네스의 체
# 가능한 n의 범위에서 존재하는 소수들을 배열을 미리 만들어 판단
# 배열 생성
arr = [True] * 1000001
arr[0], arr[1] = False, False
for _ in range(2, 1001):
    if is_prime(_):
        n = _ * 2
        while n <= 1000000:
            arr[n] = False
            n += _

# 테스트 케이스 개수
T = int(input())
for tc in range(T):
    # 짝수 N
    N = int(input())
    cnt = 0
    for num in range(N//2+1):
        if arr[num]:
            if arr[N-num]:
                cnt += 1
    print(cnt)