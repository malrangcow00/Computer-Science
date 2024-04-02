# 메모이제이션 (계산값을 저장해서 반환)

memo = [0] * 100001

def fibo(n):
    if n < 2:
        return n
    if memo[2] != 0:
        return memo[n]
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]