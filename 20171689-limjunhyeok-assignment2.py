def factorial_for(num):
    sum_val = 1
    for i in range(1, num+1):
        sum_val *= i
    return sum_val


def factorial_recursive(num):
    return_val = 0
    if num ==  1 or num == 0:
        return_val = 1
    else:
        return_val = n * factorial_recursive(num-1)
    return return_val

memo = [0 for a in range(10000)]
def factorial_memoization(num):
    if num == 1 or n == 0:
        memo[n] = 1
    elif memo[n] != 0:
        pass
    else:
        memo[n] = n * factorial_memoization(num-1)
    return memo[n]


def factorial(num):
    print("%d! = %d"%(num, factorial_for(num)))

    
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    while num != -1:
        factorial(num)
        num = int(input("Enter a number: "))
