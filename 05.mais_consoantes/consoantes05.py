from consoantes import conta_consoantes

cont_palavras = 0
encontrou = False

while True:
    palavra = input()

    if conta_consoantes(palavra):
        encontrou = True
        cont_palavras += 1
        print(cont_palavras)
        break

    if not encontrou:
        cont_palavras += 1
