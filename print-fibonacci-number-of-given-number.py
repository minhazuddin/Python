def fibonacci(n):
    first = 1
    second = 1
    fib = [1, 1]

    for x in range(n - 2):
        fib_number = int(first + second)
        fib.append(fib_number)
        first = second
        second = fib_number
    return fib[n-1]


fibonacci(4)