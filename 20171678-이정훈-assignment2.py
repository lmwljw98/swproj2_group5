def factorial(n):

    result = 1
    for i in range(1, n+1):
        result *= i

    print("%d! = "%n, result)
                
n = int(input("Enter a number: "))
while n != -1:
    factorial(n)
    n = int(input("Enter a number: "))
