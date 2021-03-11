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
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.ดูสินค้าในตะกร้า\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม")
    choice = input("กรุณาเลือกทํารายการ :")
def เพิ่มรายการสินค้า():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    add = input("กรุณาเลือกประเภทสินค้า  : ")
    if add == "A":
        เพิ่มรายการสินค้า1()
    elif add == "B":
        เพิ่มรายการสินค้า2()
def ลบรายการสินค้าของร้าน():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    delet = input("กรุณาเลือกประเภทสินค้าที่ต้องการจะลบ  : ")
    if delet == "A":
        ลบรายการสินค้าของร้าน1()
    elif delet == "B":
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
        a = int (input ("หมายเลขสินค้าที่จะลบ "))
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
def เพิ่มใส่ตะกร้าลูกค้า1():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    bs = input("กรุณาเลือกประเภทสินค้า  : ")
    if bs == "A":
        ร้านที่1()
    elif bs == "B":
        ร้านที่2()
def ลบออกจากตะกร้าลูกค้า1():
    print("ประเภทสินค้า")
    print("A.วัตถุดิบ \nB.อุปกรณ์เบเกอรี่")
    bs = input("กรุณาเลือกประเภทสินค้า  : ")
    if bs == "A":
        ลบออกจากตะกร้าลุกค้า2 ()

        
    elif bs == "B":
        ลบออกจากตะกร้าลุกค้า()
        


def ร้านที่1 ():
    
    costt()
    while(True):
        o = str (input ("รหัสสินค้าเลขสินค้า :  "))
        if o == '0':
            break;
        else:
            m = (o,)
            c.execute(' SELECT * FROM ingred WHERE รหัสสินค้า = ?',m)
            conn.commit ()
            result = c.fetchall()
            for x in result :
                basket2.append(x) 
    เพิ่มใส่ตะกร้าลูกค้า1()   
def ร้านที่2 ():
    
    costn()
    while(True):
        o = str (input ("รหัสสินค้าเลขสินค้า :  "))
        if o == '0':
            break;
            
        else:
            m = (o,)
            c.execute(' SELECT * FROM equipment WHERE รหัสสินค้า = ?',m)
            conn.commit ()
            result = c.fetchall()
            for x in result :
                basket.append(x)
    
        

    

def ลบออกจากตะกร้าลุกค้า ():
    while(True):
        o = str (input ("ลำดับสินค้าที่ต้องการลบ :  "))
        if o == '0':
            break;
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
    

def ลบออกจากตะกร้าลุกค้า2 ():
    while(True):
        o = str (input ("ลำดับสินค้าที่ต้องการลบ :  "))
        if o == '0':
            break;
        else:
            m = (o,)
            c.execute(' SELECT * FROM ingred WHERE ID = ?',m)
            conn.commit ()
            result = c.fetchall()
            for x in result :
                basket2.remove(x)
    print("สินค้าในตะกร้าที่เหลือ")
    print("รายการสินค้า ประเภทอุปกรณ์")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket2:    
        print(i)
    
    ลบออกจากตะกร้าลูกค้า1()

    
def screen_clear():
        clearscreen =os.system("cls")
def ตะกร้า():
    print("สินค้าในตะกร้า")
    print("รายการสินค้า ประเภทวัตถุดิบ")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for p in basket2:    
        print(p)
    print("สินค้าในตะกร้า")
    print("รายการสินค้า ประเภทอุปกรณ์")
    print("ลำดับที่","รหัสสินค้า","ชื่อสินค้า","ราคา")
    for i in basket: 
        print(i) 
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
            elif choice ==  "2":#ผ่าน
                os.system("cls")
                เพิ่มใส่ตะกร้าลูกค้า1 ()    
            elif choice == "3":  #ผ่าน
                os.system("cls")
                ตะกร้า()
            elif choice == "4":#เป็นหน้ากากเฉยๆยังไม่มีอะไร
                os.system("cls")
                ตะกร้า()
                ลบออกจากตะกร้าลูกค้า1()
                
           
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
            
            passw = input ("กรุณากรอกรหัสผ่านเพื่อเข้าสู่ระบบ   : ")

            
            if  passw =="149100":
                ins = input ("เลือกประเภทในการทำรายการ กรุณากด \n 1.เพิ่มรายการสินค้าในร้าน\n 2.ลบรายการสินค้าภายในร้าน\n 3.ปิดระบบ  : ")
                if ins == "1":
                    os.system("cls")
                    เพิ่มรายการสินค้า()
                    print("เพิ่มรายการสินค้าเรียบร้อย")
                elif ins== "2":
                    os.system("cls")
                    ลบรายการสินค้าของร้าน()
                    print("ลบรายการสินค้าเรียบร้อย")
                elif ins == "3":
                    os.system("cls")
                    print("        ปิดระบบเรียบร้อยค่ะ       ")
                    
                    break
            else :
                print("รหัสผ่านไม่ถูกต้องกรณาทำรายการใหม่ ")
                break
        menufrit()

 






      