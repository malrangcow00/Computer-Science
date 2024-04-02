import sys
input = sys.stdin.readline

def fib(n):
    global cnt_1
    if n < 3:
        cnt_1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt_2
    f = [0] * 41
    f[1] = f[2] = 1
    for i in range(3, n+1):
        cnt_2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

cnt_1 = 0
cnt_2 = 0
n = int(input())
fib(n)
fibonacci(n)
print(cnt_1, cnt_2)