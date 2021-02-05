print("******************ferrent School***************")
a=int(input("please enter student :"))
i=0
n1=n2=n3=n4=n5=n6=0
while (i<a):
    b=int(input("please enter score :"))
    i+=1
    if b<=100 and b>=90 :
        n1+=1
    elif b<=89 and b>=80 :
        n2+=1
    elif b<=79 and b>=70 :
        n3+=1
    elif b<=69 and b>=60 :
        n4+=1
    elif b<=59 and b>=50 :
        n5+=1
    elif b<=49 and b>=0  :
        n6+=1
        
print("90-100 : ","*"*n1)
print("80-89 : ","*"*n2)
print("70-79 : ","*"*n3)
print("60-69 : ","*"*n4)
print("50-59 : ","*"*n5)
print("0-49 : ","*"*n6)