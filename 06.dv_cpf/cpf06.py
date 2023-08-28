def calcula_digitos_verificacao(cpf):
    #primeiro dígito

    soma_digito1 = 0

    for i in range(len(cpf) - 1, -1, -1):
        digito = int(cpf[i])
        multiplicador = len(cpf) - i + 1
        soma_digito1 += digito * multiplicador

    digito1 = (soma_digito1 * 10) % 11

    if digito1 == 10:
        digito1 = 0

    cpf2 = cpf + str(digito1)

    #segundo dígito
    
    soma_digito2 = 0

    for i in range(len(cpf2) -1, -1, -1):
        digito2 = int(cpf2[i])
        multiplicador_2 = len(cpf2) - i + 1
        soma_digito2 += digito2 * multiplicador

    digito_2 = (soma_digito2 * 10) % 11
    
    if digito_2 == 10:
        digito_2 = 0

    return str(digito1) + str(digito_2)
