import sys
input = sys.stdin.readline

# 전선의 개수
number_of_wires = int(input())
# 전선의 연결 정보
connection = []
# DP 생성
DP = [1] * number_of_wires
# 전선의 연결 정보 저장
for i in range(number_of_wires):
    connection.append(list(map(int, input().split())))

# 전선의 시작점 기준으로 정렬
connection.sort()

i = 1
while i < number_of_wires:
    j = 0
    while j < i:
        if connection[i][1] > connection[j][1]:
            # 최다 연결 정보 갱신
            DP[i] = max(DP[i], DP[j] + 1)
        j += 1
    i += 1

print(number_of_wires - max(DP))