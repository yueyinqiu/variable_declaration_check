x1: int = 1
def f1():
    x2: int = 2
    def f2():
        global x1
        nonlocal x2
        x1 = 3
        x2 = 4
    f2()
    print(x2)

f1()
print(x1)