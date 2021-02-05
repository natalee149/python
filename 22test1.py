"""print("เลือกประเภทค่าบริการ")
print("***********************")
print("กด1 เลือกจ่ายเพิ่ม")
print("กด2 เลือกเหมาจ่าย")
a=int (input("เลือกประเภทการคิดบริการ :"))
print("กรุณาเลือกระยะทาง : ")
x=int(input(""))
if a==1 : 
    if x>25:
     print("ค่าบริการ = 80 ")
    else:
     print("ค่าบริการ = 25 ")
if a==2 : 
    if x < 25:
     print("ค่าบริการ = 25 ")
    else:
     print("ค่าบริการ = 55 ")"""


"""print("กรุณากรอกจำนวนครั้งการรับค่า : ")
x=int(input(""))
i=0
sum=0
while (i<x): 
    a=int(input("กรอกตัวเลข : "))
    i+=1
    sum=sum+a
print("ผลรวมค่าที่รับมาทั้งหมด = "+str(sum))"""


'''print("ป้อนชื่ออาหารสุดโปรดของคุณหรือ exit เพื่อออกจากโปรแกรม : ")
food=[]
a=0
while(True):
    n+=1
    
    menu=("อาหารที่ชอบ:{}")
x=str(input(""))
    if (x=="exit")):
        break'''
'''print("เลือกขนมที่คุณชอบหรือ exit เพื่อออกจากโปรแกรม : ")

i=0
x=1
blist=[]
while (True):
    i+=1 
    b=str(input(" ขนมที่ชอบอันดับที่ "+str(x)+":"))
    blist.append(b)
    x+=1
    if(b=="exit"):
        break    
print("ขนมโปรดของคุณมีดังนี้")
for x in range (1,i):
    print(x,'.',blist[x-1])'''

a=[]
while True:
    b = input ('------------นาบิ้วตี้ซาลอน---------\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ[x]\n')
    b = b.lower()
    if b== "a":
        c = input ("ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)")
        a.append(c)
        print("\n*****ข้อมูลได้เข้าสู่ระบบแล้ว*****\n")
    elif b== "s":
        print("{0:-<30}".format(""))
        print("{0:-<8}{1:-<10}{2:10}".format("รหัส","ชื่อ","จังหวัด"))
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        for d in a : 
            e = d.split(":")
            print("{0[0]:<6} {0[1]:>10}({0[2]:<10})".format(e))
            continue
    elif b== "x":
        break
print ("ทำคำสั่งถัดไป")






