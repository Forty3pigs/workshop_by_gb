def f(x):
    return x**2


def f(x):
    if x == 1:
        return 'Целое 1'
    elif x == 2.3:
        return 23
    else:
        return


print(f(1))             # Целое 1
print(f(2.3))           # 23
print(f(28))            # None
print(type(f(1)))       # str
print(type(f(2.3)))     # int
print(type(f(28)))      # NoneType
