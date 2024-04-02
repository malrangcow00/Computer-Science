num = 0

def ab():
    global num
    num += 1
    global name
    name = 'jp'

print(num)
ab()
print(num)
print(name)