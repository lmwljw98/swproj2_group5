import time
def fibo(nbr):
    if nbr <= 1:
        return nbr
    else:
        return fibo(nbr-1) + fibo(nbr-2)

def iterfibo(nbr):
    if nbr <= 1:
        return nbr
    else:
        fibo_list = [0,1,1]
        for i in range(1, nbr-1):
            a = fibo_list[i] + fibo_list[i+1]
            fibo_list.append(a)
        return fibo_list[nbr]

while True:
    nbr = int(input("Enter a number:"))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    ts2 = time.time()
    fibonumber2 = iterfibo(nbr)
    ts2 = time.time() - ts2
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber2, ts2))
