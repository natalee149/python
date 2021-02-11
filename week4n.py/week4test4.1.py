import os
ber = [0,0,0,0,0,]
def menu():
    global choice
    print("")
    print("")
    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ปลีก - ส่ง ")
    print("เปิดบริการ 06.00-18.00น.")
    print("           เมนู           \n ****************************\n")
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจํานวนและราคาสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม")
    choice = input("กรุณาเลือกทํารายการ :")
def cost():
    print(" 1.แป้งเค้ก ราคา 34 บาท\n 2.ผงฟู ราคา 8 บาท\n 3.วิปครีม ราคา 220 บาท\n 4.ไข่ไก่ ราคา 120 บาท(แผง)\n 5.เนย ราคา 330 บาท")
fut =["1.แป้งเค้ก","2.ผงฟู","3.วิปครีม","4.ไข่ไก่","5.เนย"]
price = [34,8,220,120,330]
def สินค้าที่คุณหยิบ():
    global choice
    for x in range (0,5):
        print(fut[x])
    a=int(input("หยิบสินค้าหมายเลข: "))
    if a==1 :
        ber[0] +=1
    elif a==2:
        ber[1] +=1
    elif a==3:
        ber[2] +=1
    elif a==4:
        ber[3] +=1
    elif a==5:
        ber[4] +=1
        menu ()
def สินค้าที่คุณได้หยิบมีดังนี้ ():
    print ("สินค้าที่คุณหยิบมีดังนี้ :")
    print("{0:.<13}        {1:.<4}        {2:.<3}        {3}".format("สินค้าที่มีในตะกร้า","ราคา","จำนวน","รวม"))
    for i in range(0,5):
        print("{0:.<25}{1:.<15}{2:.<10}{3}".format(fut[i],price[i],ber[i],ber[i]*price[i]))
def เอาออก ():
    global choice
    for x in range (0,5):
        print(fut[x])
    a=int(input("หยิบสินค้าออก  กรุณาเลือกหมายเลขสินค้าที่ต้องการหยิบออก: "))
    if a==1 :
        ber[0] -=1
    elif a==2:
        ber[1] -=1
    elif a==3:
        ber[2] -=1
    elif a==4:
        ber[3] -=1
    elif a==5:
        ber[4] -=1
        menu()
def screen_clear():
        clearscreen =os.system("cls")
while True:
    menu()
    if choice == "1":
        os.system("cls")
        cost()
    elif choice == "2":
        os.system("cls")
        สินค้าที่คุณหยิบ()
    elif choice == "3":
        os.system("cls")
        สินค้าที่คุณได้หยิบมีดังนี้()
    elif choice == "4":
        os.system("cls")
        เอาออก()
    elif choice =="5":
        c = input ("ต้องการใช้งานโปรแกรมต่อหรือไม่ กรุณากด **11.yes 22.No**  : ")
        if c== "11":
            os.system("cls")
        elif c== "22":
            os.system("cls")
            print("        ขอบคุณที่ใช้บริการ        ")
            print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ปลีก - ส่ง")
            break


