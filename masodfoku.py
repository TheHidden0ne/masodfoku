import math


def bekeres(valtozo_neve):
    user_input = input(f"{valtozo_neve} változó értéke: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Számot adjon meg")
    return user_input


a = bekeres("a")
b = bekeres("b")
c = bekeres("c")
D = b^2 - 4*a*c

if D < 0:
    print(f"Nincs megoldás, D={D}")
elif D == 0:
    x = (-b + math.sqrt(D)) / (2*a)
    print(f"Egy megoldás van: {x}")
else :
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    print(f"Megoldások: {x1}, {x2}")
