import sys
input = sys.stdin.readline

N = int(input())

# 문어끼리 잡는 손은 1:1
# 같은 문어와 2개 이상의 손을 잡을 수 없다.
# 잡는 손은 서로 같은 번호여야 한다.

result = [1, 2] * (N//2)
if N % 2 == 0:
    print(*result)
else:
    result += [3]
    print(*result)
