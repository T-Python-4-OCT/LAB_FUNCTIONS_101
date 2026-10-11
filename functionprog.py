secrit_cod="4271"



#هذي داله تحسب كل رقم صحيح في مكانه الصحيح
def exact_numbers(x):
    correct_numbers=0
    for i in range(4):
        if x[i] ==secrit_cod[i]:
            correct_numbers+= 1
    print ("correct and exact numbers :",correct_numbers)
            
    return(correct_numbers)
#وهذي الداله تسحب الارقام الصحيحه اللي في غير موقعها
def misplaced_numbers(y):
    misplaced_count=0
    chaked_numbers=[]
    for i in range(4):
        if y[i]!= secrit_cod[i]and y[i] in secrit_cod and y[i] not in chaked_numbers:
                if y.count(y[i]) <= secrit_cod.count(y[i]):
                     
                    misplaced_count+=1
                    chaked_numbers.append(y[i])
    print("correct but misplaced :",misplaced_count)
 
    return(misplaced_count)
#وهذي الداله المسؤله عن تشغيل الكود
def run_cod():
    for attempt in range(1,7):
        user_cod= input("inter your cod guess :")

        correct = exact_numbers(user_cod)
        misplaced= misplaced_numbers(user_cod)
        if correct ==4:
             print ("your answer is correct ")
             break
        else:
             print("try again:")
        
run_cod()
    