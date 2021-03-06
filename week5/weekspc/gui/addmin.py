import sqlite3 
import os
ber = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
yer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def menufrit():
    global choice
    print("")
    print("")
    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ปลีก - ส่ง ")
    print("กรุณากรอกประเภทผู้ใช้งาน")
    print(" 1.ลูกค้า\n 2.แอดมิน")
    choice = input("กรุณาเลือกทํารายการ :")
def menu():
    global choice
    print("")
    print("")
    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ปลีก - ส่ง ")
    print("เปิดบริการ 06.00-18.00น.")
    print("           เมนู           \n ****************************\n")
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจํานวนและราคาสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม")
    choice = input("กรุณาเลือกทํารายการ :")
def เพิ่มรายการสินค้า():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    rs = int(input(" รหัสสินค้า : "))
    name_pro = str(input (" ชื่อสินค้า "))
    coss = int(input("ราคา "))
    data = [rs,name_pro,coss]
    c.execute('''INSERT INTO equipment (รหัสสินค้า,ชื่อสินค้า,ราคา) VALUES(?,?,?)''',data)
    conn.commit()
    conn.close()
def ลบรายการสินค้าของร้าน ():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    try : 
        a = int (input ("หมายเลขสินค้าที่จะลบ "))
        b = [a]
        c.execute('DELETE FROM equipment WHERE id = ?',b)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

    finally :
        if conn :
            conn.close ()

def costt(): #สินค้ามี สองประเภท(วัถุดิบ)
    
    import sqlite3
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM ingred ''')
    result = c.fetchall()
    print("รายการสินค้า ประเภทวัตถุดิบ")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for x in result :
        print(x)
           
def costn(): #สินค้ามี สองประเภท(อุปกรณ์)
    import sqlite3
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM equipment ''')
    result = c.fetchall()
    print("รายการสินค้า ประเภทอุปกรณ์")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for x in result :
        print(x)
fut =["1.แป้งเค้ก","2.น้ำตาล","3.ผงฟู","4.เบคกิ้งโซดา","5.ยีสต์","6.ยีสต์แห้ง","7.ยีสต์สำเร็จรูป","8.ไข่ไก่เบอร์2","9.เนยเค็ม","10.เนยจืด","11.เนยขาว","12.มาการีน","13.ผงโกโก้เข้ม","14.ผงชาเขียวrr","15.แยมบลูเบอร์รี่","16.แยมส้ม","17.แยมสตรอเบอร์รี่","18.ดาร์กช็อคโกฯ","19.ไวท์ช็อค","20.มาชเมลโล","21.ลูกเกด"]
price = [34,24,8,23,65,65,70,120,320,340,65,60,120,130,32,32,34,125,110,45,75]
futt =["1.เตาอบไฟฟ้า","2.เครื่องตีแป้ง","3.ช้อนตวง","4.ถ้วยตวง","5.เหยือกตวง","6.ชามผสม","7.ตะกร้อมือ","8.ตะแกรงร่อนแป้ง","9.ตะแกงพักขนม","10.มีดตัดเค้ก","11.ถุงมือกันความร้อน","12.แปรงทาเนย","13.ไม้พาย","14.พิมพ์ลายการ์ตูน","15.พิมพ์อบขนม","16.กระดาษรองอบ","17.ถาดอบ","18.หัวบีบ","19.เตาอบไฟฟ้า100L","20.ถาด"]
cosss = [1490,790,90,35,45,55,45,35,35,60,50,75,20,45,45,25,80,25,3490,130]
def หยิบสินค้า():
    global choice
    for x in range (0,21):
        print(fut[x])
    a=int(input("หยิบสินค้าหมายเลข: "))
    if a== 1 :
        ber[0] +=1
    elif a==2:
        ber[1] +=1
    elif a==3:
        ber[2] +=1
    elif a==4:
        ber[3] +=1
    elif a==5:
        ber[4] +=1
    elif a==6:
        ber[5] +=1
    elif a==7:
        ber[6] +=1
    elif a==8:
        ber[7] +=1
    elif a==9:
        ber[8] +=1
    elif a==10:
        ber[9] +=1
    elif a==11:
        ber[10] +=1  
    elif a==12:
        ber[11] +=1
    elif a==13:
        ber[12] +=1
    elif a==14:
        ber[13] +=1
    elif a==15:
        ber[14] +=1 
    elif a==16:
        ber[15] +=1 
    elif a==17:
        ber[16] +=1 
    elif a==18:
        ber[17] +=1 
    elif a==19:
        ber[18] +=1
    elif a==20:
        ber[19] +=1
    elif a==21:
        ber[20] +=1
        menu ()
def หยิบสินค้า2():
    global choice
    for x in range (0,20):
        print(futt[x])
    a=int(input("หยิบสินค้าหมายเลข: "))
    if a== 1 :
        yer[0] +=1
    elif a==2:
        yer[1] +=1
    elif a==3:
        yer[2] +=1
    elif a==4:
        yer[3] +=1
    elif a==5:
        yer[4] +=1
    elif a==6:
        yer[5] +=1
    elif a==7:
        yer[6] +=1
    elif a==8:
        yer[7] +=1
    elif a==9:
        yer[8] +=1
    elif a==10:
        yer[9] +=1
    elif a==11:
        yer[10] +=1  
    elif a==12:
        yer[11] +=1
    elif a==13:
        yer[12] +=1
    elif a==14:
        yer[13] +=1
    elif a==15:
        yer[14] +=1 
    elif a==16:
        yer[15] +=1 
    elif a==17:
        yer[16] +=1 
    elif a==18:
        yer[17] +=1 
    elif a==19:
        yer[18] +=1
    elif a==20:
        yer[19] +=1
    elif a==21:
        yer[20] +=1
        menu ()
def สินค้าที่คุณได้หยิบมีดังนี้ ():
        print ("สินค้าประเภทวัตถุดิบที่คุณหยิบมีดังนี้ :")
        print("{0:.<13}        {1:.<4}        {2:.<3}        {3}".format("สินค้าที่มีในตะกร้า","ราคา","จำนวน","รวม"))
        for i in range(0,21):
            print("{0:.<25}{1:.<15}{2:.<10}{3}".format(fut[i],price[i],ber[i],ber[i]*price[i]))
    
def สินค้าที่คุณหยิบมีดังนี้2 ():
        print ("สินค้าประเภทอุปกรณ์ที่คุณหยิบมีดังนี้ :")
        print("{0:.<13}        {1:.<4}        {2:.<3}        {3}".format("สินค้าที่มีในตะกร้า","ราคา","จำนวน","รวม"))    
        for i in range(0,20):
            print("{0:.<25}{1:.<15}{2:.<10}{3}".format(futt[i],cosss[i],yer[i],yer[i]*cosss[i]))
def เอาออก1 ():
    global choice
    for x in range (0,21):
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
    elif a==6:
        ber[5] -=1
    elif a==7:
        ber[6] -=1
    elif a==8:
        ber[7] -=1
    elif a==9:
        ber[8] -=1
    elif a==10:
        ber[9] -=1
    elif a==11:
        ber[10] -=1
    elif a==12:
        ber[11] -=1
    elif a==13:
        ber[12] -=1
    elif a==14:
        ber[13] -=1
    elif a==15:
        ber[14] -=1
    elif a==16:
        ber[15] -=1
    elif a==17:
        ber[16] -=1
    elif a==18:
        ber[17] -=1
    elif a==19:
        ber[18] -=1
    elif a==20:
        ber[19] -=1
    elif a==21:
        ber[20] -=1
        menu()    
def เอาออก2 ():
    global choice
    for x in range (0,19):
        print(futt[x])
    a=int(input("หยิบสินค้าออก  กรุณาเลือกหมายเลขสินค้าที่ต้องการหยิบออก: "))
    if a==1 :
        yer[0]  -=1 
    elif a==2:
        yer[1]  -=1 
    elif a==3:
        yer[2]  -=1 
    elif a==4:
        yer[3]  -=1 
    elif a==5:
        yer[4]  -=1 
    elif a==6:
        yer[5]  -=1 
    elif a==7:
        yer[6]  -=1 
    elif a==8:
        yer[7]  -=1 
    elif a==9:
        yer[8]  -=1 
    elif a==10:
        yer[9]  -=1 
    elif a==11:
        yer[10] -=1
    elif a==12:
        yer[11] -=1
    elif a==13:
        yer[12] -=1
    elif a==14:
        yer[13] -=1
    elif a==15:
        yer[14] -=1
    elif a==16:
        yer[15] -=1
    elif a==17:
        yer[16] -=1
    elif a==18:
        yer[17] -=1
    elif a==19:
        yer[18] -=1
    elif a==20:
        yer[19] -=1
    elif a==21:
        yer[20] -=1
        menu()
def screen_clear():
        clearscreen =os.system("cls")
menufrit()
while True:
    if choice == "1":
        
        while True:
            menu()
            if choice == "1":
                print("กรุณาเลือกประเภทสินค้า")
                print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
                z=input ("กรุณาเลือกประเภทสินค้า : ")
                if z=="A":
                    os.system("cls")
                    costt()
                elif z=="B":
                    os.system("cls")
                    costn()
            elif choice ==  "2":#เป็นหน้ากากเฉยๆยังไม่มีอะไร
                print("กรุณาเลือกประเภทสินค้า")
                print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
                z=input ("กรุณาเลือกประเภทสินค้า : ")
                if z=="A":
                    os.system("cls")
                    หยิบสินค้า()
                elif z=="B":
                    os.system("cls")
                    หยิบสินค้า2()      
            elif choice == "3":  #เป็นหน้ากากเฉยๆยังไม่มีอะไร
                os.system("cls")
                สินค้าที่คุณได้หยิบมีดังนี้()
                print("------------------------------------------------------")
                สินค้าที่คุณหยิบมีดังนี้2()
            elif choice == "4":#เป็นหน้ากากเฉยๆยังไม่มีอะไร
                print("กรุณาเลือกประเภทสินค้า")
                print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
                z=input ("กรุณาเลือกประเภทสินค้า : ")
                if z=="A":
                    os.system("cls")
                    เอาออก1()
                elif z=="B":
                    os.system("cls")
                    เอาออก2()    
            elif choice =="5":
                c = input ("ต้องการใช้งานโปรแกรมต่อหรือไม่ กรุณากด **1.ใช้งานโปรแกรมต่อ 2.ฉันต้องการปิดโปรแกรม**  : ")
                if c== "1":
                    os.system("cls")
                elif c== "2":
                    os.system("cls")
                    print("        ขอบคุณที่ใช้บริการ        ")
                    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ปลีก - ส่ง")
                    break
    elif choice== "2": 
        while True:
            ins = input ("เลือกประเภทในการทำรายการ กรุณากด \n 1.เพิ่มรายการสินค้าในร้าน\n 2.ลบรายการสินค้าภายในร้าน\n   : ")
            if ins == "1":
                os.system("cls")
                เพิ่มรายการสินค้า()
                print("เพิ่มรายการสินค้าเรียบร้อย")
            elif ins== "2":
                os.system("cls")
                ลบรายการสินค้าของร้าน()
                print("ลบรายการสินค้าเรียบร้อย")
                menufrit()






      