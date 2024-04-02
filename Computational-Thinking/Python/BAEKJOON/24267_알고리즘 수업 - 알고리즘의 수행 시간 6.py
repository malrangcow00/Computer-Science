n = int(input())

# cnt = 0
# for i in range(1, n-1):
#     for j in range(i+1, n):
#         for k in range(j+1, n+1):
#             cnt += 1
#             print(i, j, k)
#     print()
# print(cnt)

# 식을 보았을 때 연산 횟수는
# n개의 숫자 중에서 3개를 고르는 조합 nC3과 결과가 같다

total = 0
for i in range(1, n-1):
    print(i*(i+1)//2)
    total += i*(i+1)//2

print(total)
