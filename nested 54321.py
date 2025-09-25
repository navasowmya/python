ip = int(input("Enter a num = "))
for row in range(ip):
    for col in range(ip,row,-1):
        print(col, end = " ")
    print()    
