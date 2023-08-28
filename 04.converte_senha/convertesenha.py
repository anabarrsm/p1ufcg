senha = input()
nova_senha = senha[0]
conv = 0

for i in range(1, len(senha)):
    l = senha[i]
    if l == "a" or l == "A":
        nova_senha += "4"
        conv += 1

    elif l == "e" or l == "E":
        nova_senha += "3"
        conv += 1

    elif l == "i" or l == "I":
        nova_senha += "1"
        conv += 1

    elif l == "o" or l == "O":
        nova_senha += "0"
        conv += 1

    else:
        nova_senha += l

print(f"{nova_senha} ({conv} troca(s))")
