number = int(input("Enter a number:"))

while number != -1:
    factorial = 1

    if number >= 0:
        for i in range(1, number+1):
            factorial *= i
        print(number, "!:", factorial)
    else:
        print("양수를 입력해주세요.")
    number = int(input("Enter a number:"))
