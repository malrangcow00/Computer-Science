# DP (다이나믹 프로그래밍)
memo = [0] * 100001
memo[0] = 0
memo[1] = 1

for i in range(2, 10000):
    # 문제에서 아래 같은 점화식을 찾아내야 한다.
    memo[i] = memo[i - 1] + memo[i - 2]
# 별도의 함수호출과정없이 계산이 가능해진다
print(memo[100])
