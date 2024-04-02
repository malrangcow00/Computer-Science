import sys
sys.stdin = open('input/1952.txt', 'r')

def f(k, res, rest:list):
    global ans
    if k == 12:
        ans = min(res, ans)
    else:
        for i in range(4):
            next_rest = rest[:]
            next_res = res
            if i < 2:
                if i == 0:
                    next_res += price[i]*rest[k]
                    next_rest[k] = 0
                    next_k = 12
                    for j in range(k, 12):
                        if next_rest[j] != 0:
                            next_k = j
                            break
                    f(next_k, next_res, next_rest)
                else:
                    next_rest[k] = 0
                    next_res += price[i]
                    next_k = 12
                    for j in range(k, 12):
                        if next_rest[j] != 0:
                            next_k = j
                            break
                    f(next_k, next_res, next_rest)
            else:
                if i == 2:
                    for j in range(min(12, k+3)):
                        next_rest[j] = 0
                    next_res += price[i]
                    next_k = 12
                    for j in range(k, 12):
                        if next_rest[j] != 0:
                            next_k = j
                            break
                    f(next_k, next_res, next_rest)
                else:
                    for j in range(min(12, k+12)):
                        next_rest[j] = 0
                    next_res += price[i]
                    next_k = 12
                    for j in range(k, 12):
                        if next_rest[j] != 0:
                            next_k = j
                            break
                    f(next_k, next_res, next_rest)


T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = max(price)*365
    f(0, 0, plan)
    print(f'#{tc} {ans}')
