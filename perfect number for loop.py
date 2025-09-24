ip = int(input("Enter the number = "))
i = 1
res = 0
while i <= ip//2:
    if ip%i==0:
        res += i
    i += 1
if ip == res:
    print("Perfect number")
else:
    print("Not a perfect number")

