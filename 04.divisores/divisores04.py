num = int(input())

for i in range(1, num + 1):
    if num > 0:
        if i < num and num % i == 0:
            print(i)
