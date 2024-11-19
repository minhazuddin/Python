s = 9
for i in range(s):
    if i == 0:

        print("*")

    elif i == s - 1:

        print("* " * s)

    else:
        print("*", (" " * (i - 1)) * 2, "*", sep=" ")