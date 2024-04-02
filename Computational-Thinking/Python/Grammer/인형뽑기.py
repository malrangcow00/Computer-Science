from pprint import pprint
import random

n = int(input('학생을 몇명 뽑을지 입력하세요: '))

problems = []
for i in range(n):
    problem = input(f'문제{i + 1} 에 대한 이름을 입력하세요')
    problems.append(problem)

students = [
    "김경범", "김상훈", "김준수", "김지연", "김치욱",
    "김태용", "박규리", "박병조", "박정환", "송민석",
    "안유나", "양원석", "윤채송", "이재평", "이지연",
    "이현직", "임승환", "장준영", "정은진", "조수현",
    "최민경",
]

input('엔터를 누르시면 뽑기를 시작합니다.')
result = dict()
# 랜덤으로 n명을 뽑기
for problem, name in zip(problems, random.sample(students, n)):
    result.update({problem: name})

pprint(result)