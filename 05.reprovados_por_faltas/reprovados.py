alunos_reprov = 0

while True:
    presenca = input()
    if presenca == "-": break
    i = 0
    faltas = 0

    while i < len(presenca):
        if presenca[i] == "f":
            faltas += 1
        i += 1

    if faltas > 8:
        alunos_reprov += 1

print(f"{alunos_reprov} aluno(s) reprovado(s) por falta.")
