n = int(input())
cnt = 0
number = 1
while True:
   number_str = str(number)
   if '666' in number_str:
      cnt += 1
   if cnt == n:
      print(number)
      break
   number += 1