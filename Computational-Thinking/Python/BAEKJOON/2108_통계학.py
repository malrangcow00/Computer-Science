import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

# 산술평균
print(round(sum(arr)/N))

# 중앙값
arr.sort()
print(arr[N//2])

# 최빈값
cnt = {}
for _ in arr:
    if _ in cnt:
        cnt[_] += 1
    else:
        cnt[_] = 1

mx = max(cnt.values())
cnt = dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True))

value_list = list(cnt.keys())
if list(cnt.values()).count(mx) > 1:
    print(value_list[1])
else:
    print(value_list[0])

# 최댓값 - 최솟값
print(max(arr)-min(arr))