usr_input = int(input("Input Number : "))

while usr_input != -1:

    answer = 1

    for i in range(usr_input, 0, -1):
        answer *= i

    if usr_input != 0 and not usr_input < -1:
        print(str(usr_input) + "! = " + str(answer))
    elif usr_input == 0:
        print("0! = 1")
    else:
        print("Wrong input")

    usr_input = int(input("Input Number : "))
