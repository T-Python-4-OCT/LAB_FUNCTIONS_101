

def fun_number():
    num=int(input("anter your number"))
    for h in range(num,0,-1):
        for i in range(h,0,-1):
            print(i,end=" ")
        print()

fun_number()