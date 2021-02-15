import sqlite3 
import os
word_dictionary  = {}
def menu():
    global choice
    print("---ระบบลงทะเบียน---\n"+'-'*25+'\n เพิ่มข้อมูลนักเรียนกด [a]\n แสดงข้อมูลนักเรียน [s]\n แก้ไขข้อมูลนักเรียน [e]\n ลบข้อมูลนักเรียน [d]\nออกจากโปรแกรม [x]\n')
    choice = input ("กรุณาเลือกทำรายการ : ")

def addstudent():
    global fname,lName,mail,sex,age,data1
    data1 = input("input name,lastname,email,sex,age (do not forget , ) :")
    data2 = data1.split(",")
    fname = data2[0]
    lName = data2[1]
    mail = data2[2]
    sex = data2[3]
    age = data2[4]
def insertTousers (fname,lName,mail,sex,age):
    try :
        conn = sqlite3.connect(r"D:\natalee_python\week5\week6.1.1.db")
        c = conn.cursor()
        sql = '''INSERT INTO urers (Name,Lastname,Email,Sex,Age) VALUES (?,?,?,?,?)'''
        data = (fname,lName,mail,sex,age)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn:
            conn.close()
def editstdinfo(fname,lName,mail,sex,age,change):
    try :
        conn = sqlite3.connect(r"D:\natalee_python\week5\week6.1.1.db")
        c = conn.cursor()
        data = (fname,lName,mail,sex,age,change)
        c.execute('''UPDATE users SET Name = ? , Lastname = ? ,Email=? , Sex = ? , Age=? ,WHERE NO = ?''',data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to edit : ",e)
    finally :
        if conn:
            conn.close()

def delet(delete):
    conn = sqlite3.connect(r"D:\natalee_python\week5\week6.1.1.db")
    c = conn.cursor()
    try :
        c.execute("""DELETE FROM users WHERE NO = ? """,delete)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to delete : ",e)
    finally :
        if conn:
            conn.close()
def show():
    conn = sqlite3.connect(r"D:\natalee_python\week5\week6.1.1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users ")
    rows = c.fetchall()
    print("{0: <15}{1: <15}{2: <15}{3: <35}{4: <15}{5: <15}\n".format("ลำดับที่","ชื่อ","นามสกุล","อีเมล","เพศ","อายุ")+"-"*120)
    for i in rows:
        print("{0: <10}{1: <15}{2: <14}{3: <33}{4: <15}{5: <15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print("ทำการแสดงรายการเสร็จสิ้น\n")

while True : 
    menu ()
    if choice == "a":
        os.system('cls')
        addstudent()
        insertTousers(fname,lName,mail,sex,age,)
    elif choice == "s":
        os.system("cls")
        show()
    elif choice == "e":
        os.system("cls")
        change = input ("กรุณากรอกตัวเลขของตำแหน่งที่ต้องการแก้ไขข้อมูล กรอก no หากไม่ต้องการแก้ไขข้อมูล : ")
        if change !="no":
            addstudent()
            editstdinfo(fname,lName,mail,sex,age,change)
    elif choice == "d":
        os.system("cls")
        delete = input ("กรุณากรอกตัวเลขของตำแหน่งที่ต้องการลบข้อมูล กรอก no หากไม่ต้องการลบข้อมูล : ")
        if delete != "no":
            delet(delete)
    elif choice == "x":
        os.system("cls")
        c = input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) : ")
        if c.lower() == "y":
            os.system("cls")
            break
        elif c.lower()=="n":
            os.system("cls")



