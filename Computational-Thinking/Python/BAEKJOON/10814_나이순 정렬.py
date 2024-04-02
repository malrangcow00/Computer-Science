N = int(input())

member = []
for _ in range(N):
    age, name = map(str, input().split())
    member.append((int(age), _, name))

member.sort()

for age, number, name in member:
    print(age, name)