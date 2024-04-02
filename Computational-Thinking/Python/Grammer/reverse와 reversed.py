word = 'abcdefg' # word = word[::-1]
# reverse는 list 메서드이므로 list로 변환 후 사용하고 다시 string으로 변환
word = list(word)
word.reverse()
word = ''.join(word)
print(word)


# reversed
word = 'abcdefg'
for letter in reversed(word):
    print(letter, end='')
print()
print(reversed(word)) # 반복자 타입을 반환