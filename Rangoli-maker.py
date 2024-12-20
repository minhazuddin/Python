import string


def print_rangoli(size):
    alpha = string.ascii_lowercase
    a = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        a.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(a[:0:-1] + a))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
