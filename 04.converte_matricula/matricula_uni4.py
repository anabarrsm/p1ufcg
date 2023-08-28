matricula1 = str(input())
matricula2 = ""


if matricula1[0] == "2" and len(matricula1) == 8:
    for i in range(len(matricula1)):
        if i == 0:
            matricula2 += "1"

        elif i == 5:
            matricula2 += matricula1[i] + "0"

        else:
            matricula2 += matricula1[i]

    print(matricula2)
