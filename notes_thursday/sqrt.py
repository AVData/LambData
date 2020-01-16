def lazy_sqrt(x):
    '''Takes x and returns the squre roor'''
    return x**0.5


def builtin_sqrt(x):
    '''uses built-in library math to get squre root'''
    from math import sqrt
    return sqrt(x)


def newton_sqrt1(x):
    '''return the square root of x using Newton's method'''
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
