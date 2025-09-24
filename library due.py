n = int(input("Enter the number of days = "))
if n <= 5:
   print(f"Fine = ${n * 1}")
elif n >= 6 and n <=10:
    print(f"Fine = ${n * 2}")
else:
    print(f"Fine = ${n * 5}")
