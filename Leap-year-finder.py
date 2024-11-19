year = int(input("Input the Year: "))


if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a Leap Year")

elif year % 400 == 0:
    print(f"{year} is a Leap Year")

elif year % 100 == 0 and year % 400 != 0:
    print(f"{year} is a not Leap Year")

else:
    print(f"{year} is a not Leap Year")

