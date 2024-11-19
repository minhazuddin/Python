# Given an Integer "n", perform the following conditional action,
# If "n" is odd, print Weird
# If "n" is even and in the inclusive range of 2 to 5, print Not Weird
# If "n" is even and in the inclusive range of 6 to 20, print Weird
# If "n" is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n < 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

# One Liner


print("Not " * (int(input().strip()) in {2, 4} | set(range(22, 101, 2))) + 'Weird')


# Using Lambda

print((lambda n: 'Weird' if n % 2 or 5 < n < 21 else 'Not Weird')(int(input())))