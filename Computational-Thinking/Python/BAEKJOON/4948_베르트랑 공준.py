import sys
input = sys.stdin.readline

def is_prime(num):
    for j in range(2, int(num**0.5)+1):
        if num % j == 0:
            return False
    return True

# 에라토스테네스의 체
# 가능한 n의 범위에서 존재하는 소수들을 배열을 미리 만들어 판단
arr = list(range(123456*2+1))
arr[1] = 0
for _ in range(4, 123456*2+1):
    if not is_prime(_):
        arr[_] = 0

while True:
    n = int(input())
    if n == 0:
        break
    lim = 2 * n
    cnt = 0
    if n % 2 == 0:
        i = n + 1
        while i <= lim:
            if arr[i]:
                cnt += 1
            i += 2
    else:
        if n == 1:
            cnt += 1
        else:
            i = n + 2
            while i <= lim:
                if arr[i]:
                    cnt += 1
                i += 2
    print(cnt)