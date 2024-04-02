arr_1 = str(map(str, 'a b c d e d f'))
arr_2 = ''.join(str(map(str, 'a b c d e d f')))
arr_3 = list(map(str, 'a b c d e d f'))
print(arr_1)
print(arr_2)
print(arr_3)

# encode ?
a = 'a'
print(id(arr))
print(arr.encode())
print(a.encode(encoding='ascii'))
print(a.encode(encoding='utf-8'))

# hash