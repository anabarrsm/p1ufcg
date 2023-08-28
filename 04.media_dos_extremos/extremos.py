num = int(input())
lista = []

for i in range(num):
    numeros = int(input())
    lista.append(numeros)

maior = lista[0]
menor = lista[0]

for elemento in range(len(lista)):
    if lista[elemento] >= maior:
        maior = lista[elemento]

    if lista[elemento] <= menor:
        menor = lista[elemento]

media = (maior + menor) / 2
cont_abaixo = 0
cont_acima = 0

for i in range(len(lista)):
    if lista[i] < media:
        cont_abaixo += 1
    
    else:
        cont_acima += 1

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Média dos extremos: {media:.2f}")
print(f"{cont_abaixo} número(s) abaixo da média")
print(f"{cont_acima} número(s) acima da média")
