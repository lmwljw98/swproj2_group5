def combination(n, m):

    if m == 0:
        return 1

    elif n == m:
        return 1

    elif n <= m:
        return 0

    else:
        return combination(n-1, m-1) + combination(n-1, m)

    print("%dC%d = %d" %(n, m, combination(n, m)))

n = int(input("Enter n: "))
m = int(input("Enter m: "))
while n != -1:
    combination(n, m)
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
