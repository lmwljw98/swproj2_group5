def upper(n):
    if n == (origin_n - r + 1):
        return n
    else:
        return upper(n-1) * n


def lower(r):
    if r == 1:
        return r
    else:
        return lower(r-1) * r


if __name__ == "__main__":
    while True:
        n = int(input("n : "))
        r = int(input("r : "))
        if n == r:
            print(str(n) + "C" + str(r) + " =", 1)
            break
        elif n > 0 and r == 0:
            print(str(n) + "C" + str(r) + " =", 1)
            break
        elif n < r:
            print("Incorrect input.")
        else:
            origin_n = n
            print(str(n) + "C" + str(r) + " =", int(upper(n) / lower(r)))
            break
