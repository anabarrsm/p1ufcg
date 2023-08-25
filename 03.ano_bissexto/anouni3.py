ano = int(input())

if ano % 400 == 0 or ano % 4 == 0:
    print(f"{ano} é bissexto")

elif ano % 100 == 0:
    print(f"{ano} não é bissexto")

else:
    print(f"{ano} não é bissexto")
