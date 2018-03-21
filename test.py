print('hello')


def iseven(i):
    return i % 2 == 0


even = [i for i in range(10000) if iseven(i)]
odd = [i for i in range(10000) if not iseven(i)]

print(odd)
