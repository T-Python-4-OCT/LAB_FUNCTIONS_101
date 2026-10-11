

#هنا سوينا الداله وعرفناها
def dicrese_loop(x:int):
    '''function print number from the bigeer to the smaller '''
   
    for i in range(x,0,-1):#هنا سوينا الفور لوب الاولى او الخارجيه ومهمتها تمشي على الارقام المدخله وتنزل بالتدريج
    
        for j in range(i,0,-1):#وهذي داله داخليه مهمتها تاخذ الرقم المخزن في المتغير وتطبع
            print(j , end="")

        print()

dicrese_loop(6)
print(dicrese_loop.__doc__)