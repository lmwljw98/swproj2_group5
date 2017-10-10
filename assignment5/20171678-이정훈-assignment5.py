import time

def iterfibo(n):
    if n == 0 or n == 1:
        return n
    
    f1 = 0
    f2 = 1
    number = 2
    while n >= number:
        fibo = f1 + f2
        f1 = f2
        f2 = fibo
        number = number + 1
    return fibo

def fibo(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return fibo(n-1) + fibo(n-2)
        

while True:
    n = int(input("Enter a number: "))
    if n == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(n)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(n, fibonumber, ts))
    
    ts1 = time.time()
    fibonumber = fibo(n)
    ts1 = time.time() - ts1
    print("Fibo(%d) = %d, time %.6f" %(n, fibonumber, ts1))
