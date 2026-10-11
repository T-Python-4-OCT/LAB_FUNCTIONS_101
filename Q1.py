num = input("Enter a number: ")

for i in range(int(num), 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()