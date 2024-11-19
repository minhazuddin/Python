find = [8, 3, 2, 5, 1, 2, 7, 2, 1, 7]


for x in range(len(find)):
    if find[x-1] + find[x] == 8:
        print("Pair present")
        print(find[x - 1], find[x])