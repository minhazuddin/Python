s = 7
for i in range(s):
    if i == 0:
        print('* ' * s)
    elif i == s - 1:
        print('* ' * s)
    else:
        print('*', ' ' * (2*s-3), '*', sep='')