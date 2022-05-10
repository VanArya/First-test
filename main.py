def Conbin(n):
    a = str(bin(n))
    c = str(a.count('1'))
    return c


print(Conbin(0))
print(Conbin(4))