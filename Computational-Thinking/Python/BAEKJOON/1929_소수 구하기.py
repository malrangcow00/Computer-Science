import sys
input = sys.stdin.readline

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

M, N = map(int, input().split())
if M < 2:
    M = 2
for num in range(M, N+1):
    if is_prime(num):
        print(num)