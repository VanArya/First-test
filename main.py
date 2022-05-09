def isDigit(string):
    try:
        if type(int(string)) is int:
            return True
    except:
        try:
            if type(float(string)) is float:
                return True
        except:
            return False

print(isDigit("--12.5"))
 #link https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python