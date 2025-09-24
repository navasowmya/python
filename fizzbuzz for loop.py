n = int(input("Enter a number:"))
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif(i % 5 == 0):
        print("buzz")
    elif(i % 3 == 0):
        print("fizzbuzz")
    else:
        print(i)
    i += 1    
