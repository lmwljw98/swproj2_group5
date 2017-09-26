def factorial(num):
    if num == 1 or num == 0:
        return_val = 1
    else:
        return_val = num * factorial(num-1)
    return return_val


def combination(n, r):
    son = 1
    mother = factorial(r)
    if n - r < r:
        r = n - r
    for i in range(r):
        son *= n-i

    return int(son/mother)


def combination2(n, r):
    return int(factorial(n)/(factorial(n-r) * factorial(r)))


def combination_recursive(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if n < r:
        return 0
    return combination_recursive(n-1, r-1) + combination_recursive(n-1, r)


if __name__ == "__main__":
    print(combination(10,3))
    print(combination2(10,3))
    print(combination_recursive(10,3))
