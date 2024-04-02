import sys
sys.stdin = open('input/1242.txt', 'r')

# 16진수 -> 2진수 딕셔너리...
hex2bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'}

ratios = {(2, 1, 1): 0,
          (2, 2, 1): 1,
          (1, 2, 2): 2,
          (4, 1, 1): 3,
          (1, 3, 2): 4,
          (2, 3, 1): 5,
          (1, 1, 4): 6,
          (3, 1, 2): 7,
          (2, 1, 3): 8,
          (1, 1, 2): 9}


# 바이너리 문자열로 변환 반환해주는 함수
def hex_to_binary(hex_str):
    return ''.join([hex2bin[h] for h in hex_str])


# 코드가 8자리...
# (홀수합의값 * 3 + 짝수값 + 검증코드) % 10 == 0
def isValid(code):
    return ((code[1] + code[3] + code[5] + code[7]) * 3 + (code[0] + code[2] + code[4] + code[6])) % 10 == 0


T = int(input())
for tc in range(1, T + 1):
    # 입력
    # N : 세로크기, M: 가로크기
    N, M = map(int, input().split())

    # N * M 암호코드가 포함된 배열...
    # 중복 라인에 대한 전처리를 해줄 필요...!
    raws = set()
    for _ in range(N):
        raws.add(input().strip())

    # 로직
    # 누적합 (결과)
    answer = 0

    # 중복 방지 (같은 코드를 이전에 체크하였다면, 다시 반영하지 않도록 방문체크!)
    existed = []

    # raws 의 값을 한줄씩 꺼내서 순회...
    for raw in raws:
        # 16 진수 -> 2진수
        binary = hex_to_binary(raw).rstrip('0')

        # 해석된 암호코드를 넣는 리스트 (8자리)
        password = []

        # 암호코드를 해석...
        # 코드의 n1, n2, n3, n4 비율을 찾기! 각각은 카운트 변수 (n1은 사실 아무것도 역할을 안해요 :9 )
        n1, n2, n3, n4 = 0, 0, 0, 0
        for i in range(len(binary) - 1, -1, -1):
            # n4
            if binary[i] == '1' and n3 == 0:
                n4 += 1
            # n3
            elif binary[i] == '0' and n2 == 0:
                n3 += 1
            # n2
            elif binary[i] == '1' and n1 == 0:
                n2 += 1
            elif binary[i] == '0' and binary[i - 1] == '1':
                # 배율을 계산...
                n = min(n2, n3, n4)
                n2, n3, n4 = n2 // n, n3 // n, n4 // n
                password.append(ratios[(n2, n3, n4)])
                # 비율 카운트 변수를 초기화
                n1, n2, n3, n4 = 0, 0, 0, 0

                # 암호코드가 8자가 되었으면
                if len(password) == 8:
                    # 암호코드를 검증하고 해당 코드가 두번 누적되지 않도록 중복체크!
                    if isValid(password) and password not in existed:
                        existed.append(password)  # 방문처리, 두번 넣어지지 않도록
                        answer += sum(password)  # 검증이 되었다면 answer에 누적
                    password = []

    # 출력
    print(f"#{tc} {answer}")

    # Segoe Print
    # Lucida Calligraphy
