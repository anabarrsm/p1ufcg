def maioridade_penal(nomes, idades):
    nomes_maioridade = []

    nomes = nomes.split()
    idades = idades.split()

    for i in range(len(nomes)):
        idade = int(idades[i])

        if idade >= 18:
            nomes_maioridade.append(nomes[i])

    saida = ""

    for i in range(len(nomes_maioridade)):
        saida += nomes_maioridade[i] + " "

        if len(nomes_maioridade) == 0:
            saida += ""

    return saida






























