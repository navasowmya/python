ip = int(input("Enter the number = "))
res = 0
while ip > 0:
    res += ip % 10
    ip //= 10
print(res)    
