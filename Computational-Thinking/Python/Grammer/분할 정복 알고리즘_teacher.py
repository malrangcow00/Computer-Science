# 반복문을 사용해서
# 시간복잡도는 O(n)
cnt = 0

def power1(x, n):
    global cnt
    tmp = 1
    for _ in range(n):
        tmp *= x
        cnt += 1
    return tmp


print(power1(2, 100000))
print(cnt)

# 재귀함수 (분할정복)
# 시간복잡도 : 0(log(n))
cnt = 0


def power2(x, n):
    global cnt
    cnt += 1
    # 기저조건
    if x == 0 or n == 0:
        return 1
    # 지수가 짝수라면....
    if n % 2 == 0:
        tmp = power2(x, n // 2)
        return tmp * tmp
    # 지수가 홀수라면...
    else:
        tmp = power2(x, n // 2)
        return tmp * tmp * x

print(power2(2, 100000))
print(cnt)