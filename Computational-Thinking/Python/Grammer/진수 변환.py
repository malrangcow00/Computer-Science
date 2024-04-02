# text = '0269FAC9A0'
# text = '01D06079861D79F99F'
# text = '0F97A3'
# bin = ''
# for _ in text:
#     bin += format(int(_, 16), 'b').zfill(4)
# i = 1
# while bin[7*(i-1):7*i]:
#     print(int(bin[7*(i-1):7*i], 2), end=' ')
#     i += 1

# 딕셔너리 한자리 16진수 -> 네자리 2진수
HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

text = "0269FAC9A0"

# 16진수 -> 2진수
# text 를 순회해서 binary 문자열에 변환한 이진수값을 계속 더한다.
binary = ""
for h in text:
    binary += HEX_TO_BIN[h]

# 2진수값에서 암호화 비트가 끝점을 탐색(순회)
e = -1
for i in range(len(binary) - 1, -1, -1):
    if binary[i] == "1":
        e = i
        break

PASSWORD = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9
}
answer = []
for i in range(e - 5, -1, -6):
    code = PASSWORD[binary[i:i + 6]]
    answer.append(code)

# 만든 암호를 요소를 꺼꾸로 변경
answer.reverse()

print(answer)
print(''.join(map(str, answer)))