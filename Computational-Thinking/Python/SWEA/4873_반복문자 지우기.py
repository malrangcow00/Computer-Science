import sys
sys.stdin = open('SWEA.input/4873.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 스택 생성
    stack = []
    #입력받은 문자열을 리스트로 생성
    word = list(input())
    # 리스트의 요소들을 순회하면서
    for i in word:
        # 스택이 비어있거나 스택의 top 부분의 요소가 i 와 다를 경우
        if stack == [] or stack[-1] != i:
            # 스택에 i 를 추가
            stack.append(i)
        # i 와 스택의 top 부분 요소가 같다면
        else:
            # 스택의 top 요소를 제거하고, i 가 다음 순서로 넘어가기 때문에
            # 스택에는 마주보는 문자가 중복되지 않는 요소만 추가된다.
            stack.pop()
    # word 리스트를 순회를 마치는 동안, 최종적으로 스택에 남게 되는 것은
    # 마주보는 문자가 중복되지 않는 요소들만 남게 되므로 스택의 길이를 출력한다.
    print(f'#{tc} {len(stack)}')

# T = int(SWEA.input())

# for tc in range(1, T + 1):
#     # 주어진 문자열을 pop 메서드를 사용하기 위해 리스트 형태로 입력받음
#     word = list(SWEA.input())

#     # 순회 시작 인덱스 설정
#     i = 1
#     # 인덱스가 문자열의 같아지기 전까지 반복
#     while i < len(word):
#         # i (현재위치) 번째 위치의 값과 i - 1 (이전위치) 번째 위치의 값을 비교
#         # 두 값이 같은 경우
#         if word[i - 1] == word[i]:
#             # i 번째 값을 pop
#             word.pop(i)
#             # i - 1 번째 값도 pop
#             word.pop(i - 1)
#             # 리스트의 길이가 위의 과정으로 변경되었기 때문에 i = 1 을 통해
#             # 새롭게 리스트를 순회
#             i = 1
#         # 두 값이 다른 경우
#         else:
#             # 다음 인덱스로 넘어감
#             i += 1
#             # 만약 리스트 안에 마주하는 단어 중 같은 단어가 없는 경우
#             # i 가 계속 증가하다가 word 의 길이와 같아질 때,
#             # 더 이상 리스트 내에 반복문자가 없기 때문에 while 이 종료

#     # word 리스트의 남은 길이 == 남은 문자열 이므로 len(word)를 출력
#     print(f'#{tc} {len(word)}')