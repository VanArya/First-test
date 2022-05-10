def Conbin(n):
    a = str(bin(n))
    c = str(a.count('1'))
    return c

def myConBin(n):
    total = 0
    while( n > 0 ):
        if n % 2 == 1:
            total += 1
        n = n // 2
    return total
    
for i in range(0,16):
    print(Conbin(i), myConBin(i))
#https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python