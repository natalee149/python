import sqlite3 
import os
conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
c = conn.cursor()
basket = []
basket2 = []
result = 0
result2 = 0
def menufrit():
    global choice
    print("")
    print("")
    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ")
    print("กรุณากรอกประเภทผู้ใช้งาน")
    print(" 1.ลูกค้า\n 2.แอดมิน")
    choice = input("กรุณาเลือกทํารายการ :")
def menu():
    global choice
    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ")
    print("เปิดบริการ 06.00-18.00น.")
    print("           เมนู           \n ****************************\n")
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.ดูสินค้าในตะกร้า\n 4.ปิดโปรแกรม")
    choice = input("กรุณาเลือกทํารายการ :")
def addproduct():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    add = input("กรุณาเลือกประเภทสินค้าที่ต้องการจะเพิ่ม  : ")
    if add == "A":
        addproduct1()
    elif add == "B":
        addproduct2()
def deleteproduct():
    print("ประเภทสินค้าภายในร้าน")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    delet = input("กรุณาเลือกประเภทสินค้าที่ต้องการจะลบ  : ")
    if delet == "A":
        costt()
        deleteproduct1()
    elif delet == "B":
        costn()  
        deleteproduct2()

def addproduct1():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    rs = str(input(" รหัสสินค้า : "))
    name_pro = str(input (" ชื่อสินค้า "))
    coss = int(input("ราคา "))
    data = [rs,name_pro,coss]
    c.execute('''INSERT INTO ingred (รหัสสินค้า,ชื่อสินค้า,ราคา) VALUES(?,?,?)''',data)
    conn.commit()
    conn.close()
def deleteproduct1 ():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    try : 
        a = int (input ("ลำดับสินค้าที่ต้องการจะลบ "))
        b = [a]
        c.execute('DELETE FROM ingred WHERE id = ?',b)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

    finally :
        if conn :
            conn.close ()
def addproduct2():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้ยังไม่เพิมในการใช้งานทั้งสองอันนน แอดมิน
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    rs = str(input(" รหัสสินค้า : "))
    name_pro = str(input (" ชื่อสินค้า "))
    coss = int(input("ราคา "))
    data = [rs,name_pro,coss]
    c.execute('''INSERT INTO equipment (รหัสสินค้า,ชื่อสินค้า,ราคา) VALUES(?,?,?)''',data)
    conn.commit()
    conn.close()
def deleteproduct2():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้ยังไม่เพิมในการใช้งานทั้งสองอันนน แอดมิน
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    try : 
        a = int (input ("ลำดับสินค้าที่ต้องการจะลบ "))
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
def addCustomer():
    os.system("cls")
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    bs = input("กรุณาเลือกประเภทสินค้าที่ต้องการหยิบใส่ตะกร้า  : ")
    if bs == "A":
        addCustomer1()
    elif bs == "B":
        addCustomer2()
def addCustomer1 ():
    costt()
    print("กรุณากรอกรหัสสินค้า \nหากต้องการออกจากรายการกด 0 ")
    while(True):
        o = str (input ("รหัสสินค้าเลขสินค้า :  "))
        if o == '0':
            break
        else:
            m = (o,) #ใช้ตัวแปรแบบtuple
            c.execute(' SELECT * FROM ingred WHERE รหัสสินค้า = ?',m)
            conn.commit ()
            result = c.fetchall()
            price1(result)
            for x in result :
                basket2.append(x)     
def addCustomer2 ():
    costn()
    print("กรุณากรอกรหัสสินค้า \nหากต้องการออกจากรายการกด 0 ")
    while(True):
        o = str (input ("รหัสสินค้าเลขสินค้า :  "))
        if o == '0':
            break
            
        else:
            m = (o,)
            c.execute(' SELECT * FROM equipment WHERE รหัสสินค้า = ?',m)
            conn.commit ()
            result = c.fetchall()
            price2(result)
            for x in result :
                basket.append(x)

def Baskett1():
    global result
    print("สินค้าในตะกร้า")
    print("รายการสินค้า ประเภทวัตถุดิบ")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket2:    
        print(i)
    print("ราคาสินค้าประเภทวัตถุดิบรวม",result,"บาท")
    
def Baskett2():
    global result2
    print ("***************************************")
    print("สินค้าในตะกร้า")
    print("รายการสินค้า ประเภทอุปกรณ์")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket:    
        print(i)
    print("ราคาสินค้าประเภทอุปกรณ์รวม",result2,"บาท")
    

def price1(x):
    global result
    print("ราคาสินค้าที่หยิบ",x[0][3])
    if choice == '2':
        result = result + int(x[0][3])
    print("ราคารวมสินค้าที่หยิบทั้งหมด",result)
def price2(x):
    global result2
    print("ราคาสินค้าที่หยิบ",x[0][3])
    if choice == '2':
        result2 = result2 + int(x[0][3])
    print("ราคารวมสินค้าที่หยิบทั้งหมด",result2)


clearscreen = os.system("cls")
menufrit()
if choice == "1":
    os.system("cls")
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
        elif choice ==  "2":#ผ่าน
            os.system("cls")
            addCustomer ()    
        elif choice == "3":  #ผ่าน
            os.system("cls")
            Baskett1()
            Baskett2()
        elif choice =="4":
            os.system("cls")
            c = input ("ต้องการใช้งานโปรแกรมต่อหรือไม่ กรุณากด **1.ใช้งานโปรแกรมต่อ 2.ฉันต้องการปิดโปรแกรม**  : ")
            if c== "1":
                os.system("cls")
            elif c== "2":
                os.system("cls")
                print("        ขอบคุณที่ใช้บริการ        ")
                print("ร้านปังหลายรสอุปกรณ์เบเกอรี่")
                break
elif choice== "2": 
    while True:
        passw = input ("กรุณากรอกรหัสผ่านเพื่อเข้าสู่ระบบ   : ")
        if  passw =="149100":
            ins = input ("เลือกประเภทในการทำรายการ กรุณากด \n 1.เพิ่มรายการสินค้าในร้าน\n 2.ลบรายการสินค้าภายในร้าน\n 3.ปิดระบบ  : ")
            if ins == "1":
                os.system("cls")
                addproduct()
                print("เพิ่มรายการสินค้าเรียบร้อย")
            elif ins == "2":
                os.system("cls")
                deleteproduct()
                print("ลบรายการสินค้าเรียบร้อย")
            elif ins == "3":
                os.system("cls")
                print("        ปิดระบบเรียบร้อยค่ะ       ")
                break
        else :
            os.system("cls")
            print("รหัสผ่านไม่ถูกต้องกรุณาทำรายการใหม่ ")
            break








      