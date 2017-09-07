usr_input = int(input("Input Number : "))

while usr_input != -1:

    answer = 1

    for i in range(usr_input, 0, -1):
        answer *= i

    if not usr_input < -1:
        print(str(usr_input) + "! = " + str(answer))
    else:
        print("Wrong input")

    usr_input = int(input("Input Number : "))
