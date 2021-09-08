import math

a = int(input("Add meg az 'a' változót: "))
b = int(input("Add meg a 'b' változót: "))  # TODO: elegánsabban
c = int(input("Add meg a 'c' változót: "))
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
