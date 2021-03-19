import sqlite3 
import os
conn = sqlite3.connect(r"D:\natalee_python\week5\weekspc\spcc1.db")
c = conn.cursor()
basket = []
basket2 = []
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
    print("") 
    print("")
    print("ร้านปังหลายรสอุปกรณ์เบเกอรี่ ")
    print("เปิดบริการ 06.00-18.00น.")
    print("           เมนู           \n ****************************\n")
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.ดูสินค้าในตะกร้า\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม")
    choice = input("กรุณาเลือกทํารายการ :")
def เพิ่มรายการสินค้า():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    add = input("กรุณาเลือกประเภทสินค้าที่ต้องการจะเพิ่ม  : ")
    if add == "A":
        เพิ่มรายการสินค้า1()
    elif add == "B":
        เพิ่มรายการสินค้า2()
def ลบรายการสินค้าของร้าน():
    print("ประเภทสินค้าภายในร้าน")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    delet = input("กรุณาเลือกประเภทสินค้าที่ต้องการจะลบ  : ")
    if delet == "A":
        costt()
        
        ลบรายการสินค้าของร้าน1()
    elif delet == "B":
        costn()  
        ลบรายการสินค้าของร้าน2()

def เพิ่มรายการสินค้า1():
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
def ลบรายการสินค้าของร้าน1 ():
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
def เพิ่มรายการสินค้า2():
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
def ลบรายการสินค้าของร้าน2():
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
def เพิ่มใส่ตะกร้าลูกค้า1():
    os.system("cls")
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    bs = input("กรุณาเลือกประเภทสินค้าที่ต้องการหยิบใส่ตะกร้า  : ")
    if bs == "A":
        ร้านที่1()
    elif bs == "B":
        ร้านที่2()
def ร้านที่1 ():
    
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
            for x in result :
                basket2.append(x) 
      
def ร้านที่2 ():
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
            for x in result :
                basket.append(x)
def ลบออกจากตะกร้าลูกค้า():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    bs = input("กรุณาเลือกประเภทสินค้าที่ต้องการลบ  : ")
    if bs == "A":
        ลบออกจากตะกร้าลุกค้า1 ()
    elif bs == "B":
        ลบออกจากตะกร้าลุกค้า2()
def ลบออกจากตะกร้าลุกค้า1 ():
    print("กรุณากรอกลำดับสินค้าที่ต้องการลบ \nหากต้องการออกจากรายการกด 0 ")
    while(True):
        o = str (input ("ลำดับสินค้าที่ต้องการลบ :  "))
        if o == '0':
            break
        else:
            m = (o,)
            c.execute(' SELECT * FROM ingred WHERE ID = ?',m)
            conn.commit ()
            result = c.fetchall()
            for x in result :
                basket2.remove(x)
    print("สินค้าในตะกร้าที่เหลือ")
    print("รายการสินค้า ประเภทวัตถุดิบ")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket2:    
        print(i)
def ลบออกจากตะกร้าลุกค้า2 ():
    print("กรุณากรอกลำดับสินค้าที่ต้องการลบ \nหากต้องการออกจากรายการกด 0 ")
    while(True):
        o = str (input ("ลำดับสินค้าที่ต้องการลบ :  "))
        if o == '0':
            break
        else:
            m = (o,)
            c.execute(' SELECT * FROM equipment WHERE ID = ?',m)
            conn.commit ()
            result = c.fetchall()
            for x in result :
                basket.remove(x)
    print("สินค้าในตะกร้าที่เหลือ")
    print("รายการสินค้า ประเภทอุปกรณ์")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket:    
        print(i)
def สินค้าในตะกร้า1():
    print("สินค้าในตะกร้า")
    print("รายการสินค้า ประเภทวัตถุดิบ")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket2:    
        print(i)
def สินค้าในตะกร้า2():
    print ("***************************************")
    print("สินค้าในตะกร้า")
    print("รายการสินค้า ประเภทอุปกรณ์")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket: 
        print(i) 
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
            เพิ่มใส่ตะกร้าลูกค้า1 ()    
        elif choice == "3":  #ผ่าน
            os.system("cls")
            สินค้าในตะกร้า1()
            สินค้าในตะกร้า2()
        elif choice== "4":
            os.system("cls")
            print("ประเภทสินค้าที่ต้องการลบ")
            print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
            bs = input("กรุณาเลือกประเภทสินค้าที่ต้องการลบ  : ")
            if bs == "A":
                os.system("cls")
                สินค้าในตะกร้า1()
                ลบออกจากตะกร้าลุกค้า1 ()
            elif bs == "B":
                os.system("cls")
                สินค้าในตะกร้า2()
                ลบออกจากตะกร้าลุกค้า2()
        elif choice =="5":
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
                เพิ่มรายการสินค้า()
                print("เพิ่มรายการสินค้าเรียบร้อย")
            elif ins == "2":
                os.system("cls")
                ลบรายการสินค้าของร้าน()
                print("ลบรายการสินค้าเรียบร้อย")
            elif ins == "3":
                os.system("cls")
                print("        ปิดระบบเรียบร้อยค่ะ       ")
                break
        else :
            os.system("cls")
            print("รหัสผ่านไม่ถูกต้องกรุณาทำรายการใหม่ ")
            break








      