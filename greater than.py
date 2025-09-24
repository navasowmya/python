n = int(input("Enter the number of days = "))
if n <= 5:
   print(f"Fine = ${n * 1}")
elif n >= 6 and n <=10:
    temp = n - 5
    print(f"Fine = ${temp * 2 + 5}")
else:
    temp1 = n - 10
    print(f"Fine = ${temp1 * 5 + 15}")



        
