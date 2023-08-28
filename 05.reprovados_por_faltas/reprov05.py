presenca = input()
alunos_reprov = 0

while len(presenca) == 14 and presenca != "-":
    if presenca.lower().count("f") > 8:
        alunos_reprov += 1
    presenca = input()

print(f"{alunos_reprov} aluno(s) reprovado(s) por falta.")
