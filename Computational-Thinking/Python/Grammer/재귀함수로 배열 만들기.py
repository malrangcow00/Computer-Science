arr = [3, 6, 7, 1, 5, 4]

n = len(arr)  # n : 원소의 개수

for i in range(1 << n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번 비트가 1인경우
            print(arr[j], end=", ")  # j번 원소 출력
    print()
print()

# # 반복문을 사용한 방법
# bit = [0] * n
# for i in range(2):
#     bit[0] = i  # 0번째 원소
#     for j in range(2):
#         bit[1] = j  # 1번째 원소
#         for k in range(2):
#             bit[2] = k  # 2번째 원소
#             for l in range(2):
#                 bit[3] = l  # 3번째 원소
#                 print(bit)  # 생성된 부분집합 출력

# # 재귀함수
# def recursive(bit, depth):
#     # 기저조건
#     if depth == n:
#         for j in range(n):  # 원소의 수만큼 비트를 비교함
#             if bit[j]:  # i의 j번 비트가 1인경우
#                 print(arr[j], end=", ")
#         print()
#         return

#     # 로직
#     for i in range(2):
#         bit[depth] = i  # depth번째 원소
#         # 재귀호출
#         recursive(bit, depth + 1)


# recursive(bit, 0)

# def print_subset(bit):
#     print(bit)

# def recursive(bit, depth):
#     if depth == len(bit):
#         print_subset(bit)
#         return

#     for i in range(2):
#         bit[depth] = i  # depth번째 원소
#         # 재귀호출
#         recursive(bit, depth + 1)

# bit = [0, 0, 0, 0]
# recursive(bit, 0)
