ip = int(input("Enter a num = "))
for row in range(1, ip+1):
    for col in range(1, ip-row+2):
        print(col, end = " ")
    print()    
