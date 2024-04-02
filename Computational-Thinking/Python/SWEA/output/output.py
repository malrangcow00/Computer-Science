import sys

# output.txt 파일을 출력하는 방법
f = open('output/1210.txt', 'r')
while True:
    sol = f.readline()
    if not sol: break
    print(sol, end='')
f.close()

# 출력결과를 test.txt 파일로 생성하는 방법
sys.stdout = open('output/test.txt', 'w')

# 출력결과를 output.txt 파일과 비교하는 방법
