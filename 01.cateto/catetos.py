import math

hipotenusa = float(input())
c1  = float(input())

c2 = math.sqrt((hipotenusa ** 2) - (c1 ** 2))

print(f"hipotenusa: {hipotenusa:.2f}")
print(f"cateto 1: {c1:.2f}")
print(f"cateto 2: {c2:.2f}")

