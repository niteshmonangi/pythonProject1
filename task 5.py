row = int(input("enter the number"))

for i in range(0, row):
    for j in range(0, i + 1):
        print("*", end="")
    print()
