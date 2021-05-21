def b10_2_b32(num):
    repr = "0123456789abcdefghijklmnopqrstuv"
    base = 32
    xx = ""
    while (num):
        r = int(num % base)
        num = num - r
        num = num / base
        xx = repr[r] + xx
    return xx

def b32_2_b10(xx):
    repr = "0123456789abcdefghijklmnopqrstuv"
    base = 32
    num = 0
    while (len(xx)):
        r = repr.index(xx[0])
        xx = xx[1:]
        num = num * base
        num = num + r
    return num

def b10_2_b64(num):
    repr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-"
    base = 64
    xx = ""
    while (num):
        r = int(num % base)
        num = num - r
        num = num / base
        xx = repr[r] + xx
    return xx

def b64_2_b10(xx):
    repr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-"
    base = 64
    num = 0
    while (len(xx)):
        r = repr.index(xx[0])
        xx = xx[1:]
        num = num * base
        num = num + r
    return num