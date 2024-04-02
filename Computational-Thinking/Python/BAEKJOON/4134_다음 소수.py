import sys
input = sys.stdin.readline

def find_prime_num(num):
    if num < 2:
        return 2
    i = 2
    lim = int(num**0.5)
    while i <= lim:
        if num % i == 0:
            i = 2
            num += 1
            lim = int(num**0.5)
        else:
            i += 1
    return num

T = int(input())
for _ in range(T):
    n = int(input())
    print(find_prime_num(n))