def calcula_media(valores):
    soma = 0
    for e in valores:
        soma += e

    return soma / len(valores)

media_fixa = float(input())

while True:
    entrada = input()

    if entrada == "fim": break

    valores = entrada.split()
    ocorrencias = [int(n) for n in valores]
    media_total = calcula_media(ocorrencias)

    if media_total < (media_fixa / 2):
        break

    if media_total > media_fixa:
        saida = entrada

print(saida)
