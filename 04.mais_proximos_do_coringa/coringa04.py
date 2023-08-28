coringa = int(input())
numeros = input().split()
numeros = [int(n) for n in numeros]
distancia = []

for i in range(len(numeros)):
    distancia.append(abs(coringa - numeros[i]))

menor = distancia[0]

for i in range(1, len(distancia)):
    if distancia[i] < menor:
        menor = distancia[i]

print(f"menor distância absoluta: {menor}")
for i in range(len(distancia)):
    if distancia[i] == menor:
        print(f"{i}:{numeros[i]}")
