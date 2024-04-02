# str() 함수를 사용하지 않고, itoa() 를 구현해 봅시다.
# 양의 정수를 입력 받아 문자열로 변환하는 함수
# 입력 값 : 변환할 정수 
# 반환 값 : 없음
# [참고] ord(), chr()
# 음수를 변환할 때는 어떤 고려 사항이 필요한가요 ?

def itoa(num):
    # 숫자를 자릿수를 분리해서 문자로 변환
    result = []
    # 거꾸로 뒤집어서
    # 리스트를 문자열로만 변환
    
    # 123
    while num != 0:
        # 첫번째 자리수만 문자로 변환해서 result에 추가
        result.append(chr(ord('0') + num % 10)) # 첫 자리수 # 3
        num = num // 10 # 12
    
    # 거꾸로 뒤집어서
    result.reverse()

    # 리스트를 문자열로 변환
    return ''.join(result)

num = 1234

print(itoa(num))

# ord() : 해당 문자 -> ASCII 코드 값
# ex) ord('A') -> 65
# chr() : 해당 ASCII 코드 값 -> 문자
# ex) chr(65) -> 'A'