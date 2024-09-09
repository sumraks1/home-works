from math import inf

def divine(first, second):
    a = int(first)
    b = int(second)
    if b <= 0:
        return inf
    rest = a / b
    return rest

