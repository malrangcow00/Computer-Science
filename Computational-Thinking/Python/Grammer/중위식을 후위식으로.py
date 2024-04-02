text = input()  #중위식 표현식

stack = []
# 문자열을 하나하나식 순회
for ch in text:
    # 1. 피연산자 (숫자)     4
    if ch.isdigit():
        # 숫자는 그대로 출력
        print(ch, end = ' ')
    # 2. 여는 괄호 (        3 / 0
    # 가장 우선 순위가 높기 때문에 스택에 바로 쌓아둔다.
    if ch == '(':
        stack.append(ch)
    # 3. * / 연산           2
    elif ch in ['*', '/']:
        if stack != [] and stack[-1] in ['*', '/']:
            # 같은 우선순위를 가진 연산자이기에 스택에서 빼내어 주고 출력
            print(stack.pop(), end='')
        stack.append(ch)
    # 4. + - 연산           2
    elif ch in ['+', '-']:
        while len(stack) > 0 and stack[-1] in ['*', '/', '+', '-']:
            # 같은 우선순위를 가진 연산자이기에 스택에서 빼내어 주고 출력
            print(stack.pop(), end='')
        stack.append(ch)
    # 5. 닫는 괄호 )        -1
    # 여는 괄호가 나올 때까지 스택을 pop을 하면서 진행한다
    elif ch == ')':
        while len(stack) > 0 and stack[-1] == '(':
            # 여는 괄호가 나올 때까지 pop을 진행
            print(stack.pop(), end='')
        stack.append(ch)

# 스택에 남아있는 연산자 모두 pop을 하여 출력
while len(stack) > 0:
    print(stack.pop(), end='')
    
print()