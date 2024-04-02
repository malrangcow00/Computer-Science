import sys
input = sys.stdin.readline

# N: 캐릭터 수, M: 캐릭터 수제한 K: 보스 수
N, M, K = map(int, input().split())
# D: 캐릭터 당 데미지
D = []
for _ in range(N):
    D.append(int(input()))
D.sort(reverse=True)

bosses = []
for _ in range(K):
    # HP, 메소 순으로 들어감
    bosses.append(list(map(int, input().split())))

# 숙제한 캐릭터 카운트
cnt = 0
# 얻을 수 있는 총 보상
Q = 0

# 캐릭터 쎈 순서로 순회
for character in range(N):
    # 깎을 수 있는 HP
    HP = 900 * D[character]
    values = []
    # 전체 조합 저장해놓고 또 써먹으면 시간 줄어... (고쳐야함)
    for i in range(1 << K):
        cost = 0 # 깎은 HP
        tmp = 0 # 얻은 보상
        for j in range(K):
            if i & (1 << j):
                # 잡을 수 있는 보스 조합 모두 저장
                extra = bosses[j][0] % D[character]
                if extra == 0:
                    cost += bosses[j][0]
                    tmp += bosses[j][1]
                else:
                    cost += (bosses[j][0] - extra + D[character])
                    tmp += bosses[j][1]
        # 얻을 수 있는 금액 모두 저장
        if cost <= HP:
            values.append(tmp)
    # 모든 경우 중 최댓값 더하고 캐릭터 ++
    Q += max(values)
    cnt += 1

    # 숙제 다한 캐리터 갯수 M 도달시 종료
    if cnt == M:
        break

# 결과값 출력
print(Q)
