import sys
sys.stdin = open('SWEA.input/6019.txt', 'r')

# 테스트 케이스의 개수
T = int(input())
 
for tc in range(1, T+1):
    # D : 처음 기차 사이의 거리
    # A : 기차 A의 속력
    # B : 기차 B의 속력
    # F : 파리의 속력
    D, A, B, F = map(int, input().split())
    
    distance = 0 # 파리가 이동한 거리
    value = F*D/(A+B) # distance가 수렴하게 되는 값(참 값)
    
    # 절대오차 (초기값)
    absolute_error = value
    # 상대오차 (초기값)
    relative_error = value
    
    # 절대오차와 상대오차 비교
    while value > distance and absolute_error > 10**(-6):
    # while value > distance and relative_error > 10**(-6):
        # 파리가 B를 향해 날아간 거리
        distance += D/(F + B)*F
        D -= (A+B)*D/(F+B) # 남은 기차간 거리
        # 파리가 A를 향해 날아간 거리
        distance += D/(F + A)*F
        D -= (A+B)*D/(F+A)
        
        # 절대오차
        absolute_error = value - distance
        # 상대오차
        relative_error = (value - distance) / value
       
    # 절대오차와 또는 상대오차 선택 
    # 이 문제에서는 절대오차를 비교하는 방법이 더 정확하다
        
    print(f'#{tc} {distance}')