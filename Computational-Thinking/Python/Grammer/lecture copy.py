# 빈 리스트
stack = []

# push : 마지막의 요소를 삽입
def push(item):
    stack.append(item)


# isEmpty : 현재 스택이 비어있는지 여부를 반환해주는 함수
def isEmpty():
    return len(stack) == 0

# pop :  마지막의 요소를 꺼내는 연산
# pop을 시행했을 때 요소가 없다면??? (에러!)
def pop():
    if isEmpty():
        return
    return stack.pop()


# peek : 가장 마지막에 넣었던 요소의 값을 반환 함수
def peek():
    if isEmpty():
        return
    return stack[-1]


# 괄호 검사 (소괄호만)

def check(text):
    for ch in text:
        # '(' 괄호를 만났을 때에는 '(' 삽입(push)
        if ch == '(':
            push('(')
        # ')' 괄호를 만났을 때에는 삭제(pop)
        elif ch == ')':
            if isEmpty():  # 도중에 비어있는 스택에서 삭제(pop)를 진행
                return False
            pop()

    if isEmpty():
        return True
    else:
        return False


# 괄호 검사 성공한 경우는 괄호 검사를 수행 완료한 후에 스택이 비어있는 경우.
#  //      실패한 경우는 검사를 수행하는 도중에 비어있는 스택에서 삭제(pop)를 진행하려 하거나,
#                        괄호 검사를 수행 완료한 후에 스택이 차 있는 경우.
test = '((( )((((( )( )((( )( ))((( ))))))'

if check(test):
    print("성공")
else:
    print("실패")
