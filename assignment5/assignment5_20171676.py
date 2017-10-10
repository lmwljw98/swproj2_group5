import time

def iterfibo(n):
    tmp1 = 0
    tmp2 = 1
    result = 0

    if n <= 1:
        return n
    else:
        for i in range(n-1):
            result = tmp1 + tmp2
            tmp1, tmp2 = tmp2, result
        return result


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    n = 0
    while True:
        n = int(input("Enter a number : "))

        if n == -1:
            break

        ts1 = time.time()
        a = iterfibo(n)
        ts1 = time.time() - ts1

        ts2 = time.time()
        b = fibo(n)
        ts2 = time.time() - ts2

        print("iterative fibo(%d) :" %(n), a, "// Elapsed Time :", ts1)
        print("recursive fibo(%d) :" %(n), b, "// Elapsed Time :", ts2)
