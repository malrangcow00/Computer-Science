import sys
input = sys.stdin.readline
from collections import deque

# 최대한 다양한 종류의 초밥을 먹으려고 한다.

# N: 벨트 위 접시의 수
# d: 초밥의 가짓수
# k: 연속해서 먹는 접시의 수
# c: 쿠폰 번호 (무료인 초밥 번호)
N, d, k, c = map(int, input().split())
conveyor = []
for _ in range(N):
    conveyor.append(int(input()))

picks = deque(conveyor[-k:])

cnt = {}
for i in range(k):
    if picks[i] in cnt:
        cnt[picks[i]] += 1
    else:
        cnt[picks[i]] = 1

tmp = len(cnt)
mx = 0
for i in range(N):
    absorb = conveyor[i]
    picks.append(absorb)
    emit = picks.popleft()

    if absorb in cnt and cnt[absorb] > 0:
        cnt[absorb] += 1
    else:
        tmp += 1
        cnt[absorb] = 1
    cnt[emit] -= 1
    if cnt[emit] == 0:
        tmp -= 1
    if c in cnt and cnt[c] > 0:
        mx = max(mx, tmp)
    else:
        mx = max(mx, tmp+1)

print(mx)
