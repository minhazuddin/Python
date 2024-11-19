def fibonacci():
    input_number = int(input("Enter Number: "))
    first = 1
    second = 1
    print(first,  second, end=" ")

    for x in range(input_number - 2):
        fib_number = first + second
        print(fib_number, end=" ")
        first = second
        second = fib_number

fibonacci()