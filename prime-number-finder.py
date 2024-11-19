def prime_number(number):
    prime_numbers = []
    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime_numbers.append(x)
    return prime_numbers


print(prime_number(50))


# Without function

# for x in range(2, 50):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#     else:
#         print(x)