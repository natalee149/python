print("กรุณากรอกจำนวนครั้งการรับค่า : ")
x=int(input(""))
i=0
sum=0
while (i<x): 
    a=int(input("กรอกตัวเลข : "))
    i+=1
    sum=sum+a
print("ผลรวมค่าที่รับมาทั้งหมด = "+str(sum))