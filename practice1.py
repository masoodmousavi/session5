
def chess(x,y): 
    c = 0
    for i in range(x): 
        c = 0
        for j in range(y):
            print("*",end="")
            c+=1
            if c == y:
                break
            else:    
                print("#",end="")
                c+=1
            if c == y:
                break
        print()    


a = int(input("enter your number: "))
b = int(input("enter your number: "))

print(chess(a, b))

