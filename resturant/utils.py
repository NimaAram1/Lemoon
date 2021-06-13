from random import randint

type_of_rand = randint(1,3)

rand1 = randint(0, 8)
rand2 = randint(0, 3)
rand3 = randint(0, 9)
rand4 = randint(0, 9)
rand5 = randint(0, 9)
rand6 = randint(0, 13)

a = ["A", "x", "c", "B", "h", "Q", "W", "e", "k"]
b = ["f", "T", "Y", "u"]
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
e = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
f = ["A", "x", "c", "B", "h", "Q", "W", "e", "k", "T", "u", "U", "i", "I"]

def get_order_name():
    if type_of_rand == 1:
        return f"lm-{a[rand1]}{b[rand2]}{c[rand3]}{d[rand4]}{e[rand5]}{f[rand6]}"
    elif type_of_rand == 2:
        return f"lm-{c[rand3]}{b[rand2]}{a[rand1]}{f[rand6]}{e[rand5]}{d[rand4]}"
    elif type_of_rand == 3:
        return f"lm-{b[rand2]}{c[rand3]}{f[rand6]}{a[rand1]}{e[rand5]}{d[rand4]}"        