def conta_consoantes(palavra):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    vogais = "aeiou"
    vogais_cont = 0
    consoantes_cont = 0

    for l in palavra:
        if l.lower() in vogais:
            vogais_cont += 1

        elif l.lower() in consoantes:
            consoantes_cont += 1

    return consoantes_cont > vogais_cont
