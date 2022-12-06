

def print_star(a):


    b = 1     # چاپ اولین ستاره
    c =' '    # چاپ اسپیس
    d=user_input      #متغیر کمکی برای کم کردن اسپیس ها
    for i in range(user_input):
        print(c*d,end="")      #چاپ کردن اسپیش
        for j in range(b):
            print("*",end="")     #چاپ ستاره
        print()   
        d -=1     #کم کردن متغیر اسپیس
        b = b+2    #اضافه کردن متغیر ستاره


#-------------------------------------------------------------------------------

    star= (user_input*2-1)-2   #محاسبه تعداد چاپ ستاره ها در خط اول
    spase = ' '     #ساخت متغیر اسپیس
    spase2 =1
    for i in range(user_input):
        print(" ",end="")
        print(spase * spase2 ,end="")
        for i in range(star):
            print("*",end="")
        print()    
        star -=2 
        spase2+=1



user_input = int(input("pls enter your number: ")) 
print_star(user_input)