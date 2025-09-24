n = int(input("Enter a number:"))
total = 0
while n >= 1:
    if n % 2 == 0:
        total += n
    n-=1    
print("Result",total)    
