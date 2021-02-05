import os 
dic ={}
def menu ():
    global choice
    print('------------vocab---------\n 1.เพิ่มคำศัพท์ \n 2.แสดงคำศัพท์ \n 3.ลบศัพท์\n 4.ออกจากระบบ ')
    choice = input("กรุณาเลือกทำรายการ : ")
def เพิ่มคำศัพท์():
    a=input("\nเพิ่มคำศัพท์ : ")
    s=input("ชนิดคำ ( n.  ,  v. ,  adj.  , adv )  : ")
    d=input("ความหมาย : ")
    dic[a]=s,d
    print("เพิ่มคำศัพท์เรียบร้อย")
def แสดงคำศัพท์():
    print("*"*30+"\n\tคำศัพท์ทั้งหมด\n"+"*"*30+"\nคำศัพท์  ประเภท  ความหมาย ")
    for key in dic:
        print("{}{:<5}{}".format ( key,"  ",dic[key] ))
def ลบคำศัพท์ออก():
    delist = input("\nกรุณาพิมพ์คำศัพท์ที่ต้องการลบ :")
    ex = input("ต้องการลบ {}ใช่หรือไม่ (y/n):".format(delist))
    if ex == "y":
        del dic[delist]
        print("ลบ"+delist+"เรียบร้อยแล้ว")


while True:
    menu()
    if choice=="1":
        เพิ่มคำศัพท์()
    elif choice=="2":
        แสดงคำศัพท์()
    elif choice=="3":
        ลบคำศัพท์ออก()
    elif choice=="4":
        ch = input ("\nคุณต้องการอยู่ในระบบต่อไปหรือไม่ (ใช้/ไม่ใช่) :")
        if ch =="ไม่ใช่":
            print("ออกจากระบบเรียบร้อยแล้ว")
            break
        elif ch == "ใช่":
            continue
        