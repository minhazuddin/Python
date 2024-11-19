def nextPrime(n):
    for x in range(n + 1, n + 100):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            return x


print(nextPrime(307))
