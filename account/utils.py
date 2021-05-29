from random import randint



def generate6Code():
    num1 = randint(0, 9)
    num2 = randint(0, 9)
    num3 = randint(0, 9)
    num4 = randint(0, 9)
    num5 = randint(0, 9)
    num6 = randint(0, 9)
    code = f"{num1}{num2}{num3}{num4}{num5}{num6}"
    return code
