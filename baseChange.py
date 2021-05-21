def b10_2_b64(num):
    order = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-"
    base = 64
    xx = ""
    while (num):
        r = int(num % base)
        num = num - r
        num = num / base
        xx = order[r] + xx
    return xx

def b64_2_b10(xx):
    order = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-"
    base = 64
    num = 0
    while (len(xx)):
        r = order.index(xx[0])
        xx = xx[1:]
        num = num * base
        num = num + r
    return num