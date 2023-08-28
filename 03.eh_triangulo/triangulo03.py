a = int(input())
b = int(input())
c = int(input())

perimetro = c + a + b

if (a - b) < c and (a + b) > c:
    print(f"triangulo valido. {perimetro}")

elif (a - c) < b and (a + c) > b:
    print(f"triangulo valido. {perimetro}")

elif (b - c) < a and b + c > a:
    print(f"triangulo valido. {perimetro}")

else:
    print("triangulo invalido.")

