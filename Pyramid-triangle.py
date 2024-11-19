number = int(input("Enter Number: "))

for i in range(number):
    for j in range(number - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end="")

    print()