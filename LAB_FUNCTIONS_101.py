def nmubr (n:int):
    '''function that takes 1 parameter of type int , then it prints out the result formatted '''
    for i in range (n, 0, -1):
        for j in range(i, 0, -1):
            print (j , end = " ")
        print()
nmubr (5)
print(nmubr.__doc__)
