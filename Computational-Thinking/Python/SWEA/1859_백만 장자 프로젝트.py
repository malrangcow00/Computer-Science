import sys
sys.stdin = open('input/1859.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    income = 0
    mx_price = 0
    for i in range(1, N+1):
        if price[-i] > mx_price:
            mx_price = price[-i]
        else:
            income += mx_price - price[-i]
    print(f'#{tc} {income}')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     income = 0
#     while len(arr) > 0:
#         idx = arr.index(max(arr))
#         income += max(arr) * (idx)
#         for i in range(idx):
#             income -= arr[i]
#         if idx + 1 != len(arr):
#             arr = arr[idx+1:]
#         else:
#             break
#     print(f'#{tc} {income}')