T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    mx = max(num_list)
    mn = min(num_list)
    diff = mx - mn
    print(f'#{tc} {diff}')