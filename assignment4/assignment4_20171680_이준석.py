def Combination (n, m):
    if n == 1 or m == n or m == 0:
        return 1
    elif n <= -1:
        return -1
    else:
        return Combination(n-1, m) + Combination(n-1, m-1)

n = int(input("Enter n:"))
m = int(input("Enter m:"))

if n >= m:
    while n != -1:
        C = Combination(n, m)
        print("C(%d, %d) = %d" %(n, m, C))
        n = int(input("Enter n:"))
        m = int(input("Enter m:"))
