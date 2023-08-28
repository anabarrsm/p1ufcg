num = input()
num_list = input()
num_list_int = [int(n) for n in num_list.split()]

for i in num_list_int:
    if i == int(num):
        print("sim")
        break

else:
    print("não")
