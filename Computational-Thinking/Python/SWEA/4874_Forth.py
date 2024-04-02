import sys
sys.stdin = open('input/4874.txt', 'r')

# 후위식표기법의 연산을 완료해서 결과를 반환...
# 도중에 에러가 발생하는 경우는 "error" 반환

operator = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

def solution(postfix):
    # 스택
    stack = []
    try:
        for i in range(len(postfix) - 1):
            if postfix[i].isdigit():  # 피연산자(숫자)
                stack.append(postfix[i])
            else:
                # 연산자라면 두개의 피연산자를 스택에서 빼서 계산..
                b = int(stack.pop())
                a = int(stack.pop())
                # if postfix[i] == '/':
                #     c = a // b
                # elif postfix[i] == '-':
                #     c = a - b
                # elif postfix[i] == '+':
                #     c = a + b
                # elif postfix[i] == '*':
                #     c = a * b
                # 람다식을 사용해서 멋있게 커스터마이즈
                if postfix[i] in ['*', '-', '/', '+']:
                    c = operator[postfix[i]](a, b)
                stack.append(c)
        return stack.pop()
    except:
        return "error"


# 테스트케이스
T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 후위표기법
    postfix = input().split()

    # 메인로직
    result = solution(postfix)

    # 출력
    print(f"#{tc} {result}")