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

def b10_2_b128(num):
    repr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]:;<=>?@!#$%&'()*+,-./^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅ"
    base = 128
    xx = ""
    while (num):
        r = int(num % base)
        num = num - r
        num = num / base
        xx = repr[r] + xx
    return xx

def b128_2_b10(xx):
    repr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]:;<=>?@!#$%&'()*+,-./^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅ"
    base = 128
    num = 0
    while (len(xx)):
        r = repr.index(xx[0])
        xx = xx[1:]
        num = num * base
        num = num + ré
    return num

def b10_2_b256(num):
    repr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]:;<=>?@!#$%&'()*+,-./^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅ"
    base = 256
    xx = ""
    while (num):
        r = int(num % base)
        num = num - r
        num = num / base
        xx = repr[r] + xx
    return xx

def b256_2_b10(xx):
    repr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]:;<=>?@!#$%&'()*+,-./^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅ"
    base = 256
    num = 0
    while (len(xx)):
        r = repr.index(xx[0])
        xx = xx[1:]
        num = num * base
        num = num + r
    return num