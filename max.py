ip = int(input("Enter the number = "))
max = 0
while ip > 0:
    res = ip%10
    ip //= 10
    if res > max:
        max = res
print(max)    
