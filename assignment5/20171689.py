import time


def fibo(num):
    if num < 2:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

    
def iterfibo(num):
    front_num = 0
    back_num = 1
    for i in range(num):
        front_num, back_num = back_num, front_num + back_num
    return front_num


def iterfibo2(num):
    fibo_table = [0,1,1]
    if num <= 2:
        return fibo_table[num]
    else:
        for i in range(2,num):
            fibo_table.append(fibo_table[i]+fibo_table[i-1])
        return fibo_table[num]
    
while True:
    input_num = int(input("Enter a number: "))
    if input_num == -1:
        break

    ts = time.time()
    fibo_num = iterfibo(input_num)
    ts = time.time() - ts

    print("Basic iteration iterfibo(%d) = %d,\ttime = %.6f"%(input_num, fibo_num, ts))

    ts = time.time()
    fibo_num = iterfibo2(input_num)
    ts = time.time() - ts

    print("Indexed iteration iterfibo2(%d) = %d,\ttime = %.6f"%(input_num, fibo_num, ts))
    
    ts = time.time()
    fibo_num = fibo(input_num)
    ts = time.time() - ts

    print("Recursive fibo(%d) = %d,\ttime = %.6f"%(input_num, fibo_num, ts)) 
