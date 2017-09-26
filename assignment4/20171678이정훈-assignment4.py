def combination_rec(n, m):

    if m == 0:
        return 1

    elif n == m:
        return 1

    elif n < m:
        return 0

    else:
        return combination_rec(n-1, m-1) + combination_rec(n-1, m)

    print("%dC%d = %d" %(n, m, combination_rec(n, m)))


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i

    return res

def combination(n, m):
   print("%dC%d = %d" %(n, m, factorial(n) // factorial(m) // factorial(n-m)))

n = int(input("Enter n: "))
m = int(input("Enter m: "))
while n != -1:
    combination_rec(n, m)
    combination(n, m)
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    
