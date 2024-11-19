number = int(input("Enter Number: "))

for x in range(number):
    for y in range(number - x):
        print("x", end="")

    print()