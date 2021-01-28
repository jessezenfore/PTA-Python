
x = int(input())

def f(x):

    if x == 0:
        return 0
    else:
        return 1 / x

print("f( {0:.1f} ) = {1:.1f}".format(x, f(x)))