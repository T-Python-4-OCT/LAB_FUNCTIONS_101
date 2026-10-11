def check1(s, g):
    c = 0
    for i in range(4):
        if g[i] == s[i]:
            c = c + 1
    return c


def check2(s, g):
    l1 = list(s)
    l2 = list(g)
    for i in range(4):
        if l2[i] == l1[i]:
            l1[i] = "X"
            l2[i] = "Y"
            
    c2 = 0
    for i in range(4):
        for j in range(4):
            if l2[i] == l1[j] and l2[i] != "Y":
                c2 = c2 + 1
                l1[j] = "X"
                break
    return c2


def play():
    code = "4271"
    tries = 6
    
    print(" ALIEN VAULT GAME 0.0 ")
    for t in range(1, tries + 1):
        print("Attempt:", t)
        user_g = input("Try to guess the right code: ")
        
        if len(user_g) != 4 or not user_g.isdigit():
            print("you must to input 4 digit, try again\n")
            continue
            
        e = check1(code, user_g)
        m = check2(code, user_g)
        
        print(f"EXACT: {e} | MISPLACED: {m}")
        
        if e == 4:
            print("\nYou win Vault opened .")
            return
            
        print("-" * 20)
        
    print("\n Game over You lost.")


play()