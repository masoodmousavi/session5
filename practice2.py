
def Multiplication_table(a,b):
    adade_aval = 1
    adade_dovom = 1

    for i in range(b): 
        

        for j in range(a):
            answer = adade_aval * adade_dovom
            print(answer,end="              ")
            adade_aval+=1

            if j == a+1:
                break

        print()  
        adade_aval =1
        adade_dovom += 1  


    
x = int(input("enter your number: "))
y = int(input("enter your number: "))

print(Multiplication_table(x, y))