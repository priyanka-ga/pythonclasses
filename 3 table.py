# 3 table

'''for i in range(1,11):
    print(i*3)'''
   
    
    
    #febnoci series
    
num =int(input("enter the integer value"))
a=0
b=1
if num<1:
    print("invalid num")
else:
    print("fabnoci series of ",num,"is")
    print(a)
    print(b)
    for i in range (2,num):
        c = a + b
        a = b
        b = c
        print(c)
   