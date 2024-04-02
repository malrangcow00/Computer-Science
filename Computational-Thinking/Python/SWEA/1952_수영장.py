import sys
sys.stdin = open('input/1952.txt', 'r')

def monthly_plan(i, j):
    mn = 0
    for k in range(i, j):
        mn += min(plans[k]*prices[0], prices[1])
    return mn

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    min_price = prices[-1]
    tmp = 0
    for i in range(12):
        if plans[i]:
            for j in range(5):
                if i+j < 11 and not plans[i+j+1]:
                    break
            if j == 5:
                if min(prices[2]*2, prices[1]*6, prices[0]*sum(plans[i:i+j+1])) == prices[2]*2:
                    plans[i], plans[i+1], plans[i+2] = 0, 0, 0
                    tmp += prices[2]
                else:
                    tmp += monthly_plan(i, i+1)
                    plans[i] = 0
            elif j >= 2:
                imm = monthly_plan(i, j)
                for k in range(i, i+j+1):
                    if k + 3 < i + j:
                        imm = min(imm, monthly_plan(i, k) + monthly_plan(k, k+3) + monthly_plan(k+3, i+j+1))
                tmp += imm
            elif j < 2:
                tmp += monthly_plan(i, i+j+1)

    min_price = min(min_price, tmp)
    print(f'#{tc} {min_price}')
