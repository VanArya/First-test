def Conbin(n):
    a = str(bin(n))
    c = str(a.count('1'))
    return c


print(Conbin(0))
print(Conbin(4))
#https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python