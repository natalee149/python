import sqlite3 
import os
conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
c = conn.cursor()
basket = []
basket2 = []
result = 0
result2 = 0
w=0
def menufrit():
    global choice
    print("")
    print("")
    print("*"*30)
    print("     Panglairos Bakery    ")
    print("*"*30)
    print("กรุณากรอกประเภทผู้ใช้งาน")
    print(" 1.ลูกค้า\n 2.แอดมิน")
    choice = input("กรุณาเลือกทํารายการ :")
def menu():
    global choice
    print("*"*30)
    print("     Panglairos Bakery ")
    print("     เปิดบริการ 06.00-18.00น.")
    print("*"*30)
    print("           เมนู")
    print("-"*30)
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.ดูสินค้าในตะกร้า\n 4.ลบสินค้าในตะกร้า\n 5.ปิดโปรแกรม")
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
def baskets(): #สินค้ามี สองประเภท(อุปกรณ์)
    import sqlite3
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    c.execute('''SELECT รหัสสินค้า ,ชื่อสินค้า ,ราคา, จำนวน FROM baskets ''')
    result = c.fetchall()
    print("รายการสินค้า")
    print("รหัสสินค้า","ชื่อสินค้า","ราคา","จำนวน")
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
def addCustomer1():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้ยังไม่เพิมในการใช้งานทั้งสองอันนน แอดมิน
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    costt()
    basket=[]    
    n=[]
    t=input("กรอกรหัสสินค้าที่จะหยิบใส่ตะกร้า :")
    n.append(t)
    c.execute(' SELECT รหัสสินค้า,ชื่อสินค้า,ราคา FROM ingred WHERE รหัสสินค้า = ?',n)
    p=c.fetchall()
    for i in p:
        for j in i:
            basket.append(j)
    w=int(input("กรอกจำนวนสินค้าที่ต้องการซื้อ : "))  
    basket.append(w)  
    c.execute('INSERT INTO baskets(รหัสสินค้า,ชื่อสินค้า,ราคา,จำนวน) VALUES (?,?,?,?)',basket)
    conn.commit()
    conn.close()
    totalprice()

def addCustomer2():
    import sqlite3  # เทส เป็นอุปกรณืเครื่องใช้ยังไม่เพิมในการใช้งานทั้งสองอันนน แอดมิน
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    costn()
    basket=[]    
    n=[]
    t=input("กรอกรหัสสินค้าที่จะหยิบใส่ตะกร้า : ")
    n.append(t)
    c.execute(' SELECT รหัสสินค้า,ชื่อสินค้า,ราคา FROM equipment WHERE รหัสสินค้า = ?',n)
    p=c.fetchall()
    for i in p:
        for j in i:
            basket.append(j)
    w=int(input("กรอกจำนวนสินค้าที่ต้องการซื้อ : "))  
    basket.append(w)  
    c.execute('INSERT INTO baskets(รหัสสินค้า,ชื่อสินค้า,ราคา,จำนวน) VALUES (?,?,?,?)',basket)
    conn.commit()
    c.close()
    totalprice()

def totalprice()    :
    total=0
    c =conn.cursor()    
    c.execute(' SELECT ราคา*จำนวน FROM baskets ')
    x=c.fetchall()
    for i in x:
        for j in i:
            total = total+int(j)
    print("ราคาสินค้าทั้งหมด",total,"บาท")
    c.close()

def delbask() :
    baskets()
    c=conn.cursor()
    sel = input("กรอกรหัสสินค้าที่ต้องการลบ : ")
    n=[]
    n.append(sel)
    c.execute('DELETE FROM baskets WHERE รหัสสินค้า = ?',n)
    conn.commit()
    c.close()
    print("สินค้าคงเหลือในตะกร้า")
    baskets()
    totalprice()
def deletebasket():
    import sqlite3 
    conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
    c = conn.cursor()
    try : 
        c.execute('DELETE FROM baskets ')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

    finally :
        if conn :
            conn.close ()
while True :
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
                baskets()
                totalprice()
            elif choice == "4":  #ผ่าน
                os.system("cls")
                delbask()

            elif choice =="5":
                os.system("cls")
                c = input ("ต้องการใช้งานโปรแกรมต่อหรือไม่ กรุณากด **1.ใช้งานโปรแกรมต่อ 2.ฉันต้องการปิดโปรแกรม**  : ")
                if c== "1":
                    os.system("cls")
                elif c== "2":
                    os.system("cls")
                    deletebasket()
                    print("        ขอบคุณที่ใช้บริการ        ")
                    print("      Panglairos Bakery       ")
                    break
    elif choice== "2":  
        passw = input ("กรุณากรอกรหัสผ่านเพื่อเข้าสู่ระบบ   : ")
        while True:
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








      