r = int(input("Enter the total number of rows: "))
print("Mirrored Right Angled Triangle Star Pattern")
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j<= r - i):
            print('', end = ' ')
        else:
            print('*', end = ' ')
    print()