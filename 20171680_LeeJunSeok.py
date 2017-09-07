while 1 :
    number = int(input("Enter a number:"))
    factorial = 1

    if number >= 0 :
        for i in range(1, number+1) :
            factorial = i * factorial
        print(number,"!:",factorial)
    elif number == -1 :
        break
    else :
        print("정수를 입력해주세요.")
