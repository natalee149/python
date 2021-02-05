import os 
dic ={}
def menu ():
    global choice
    print('------------vocab---------\n 1.เพิ่มคำศัพท์ \n 2.แสดงคำศัพท์ \n 3.ลบศัพท์\n 4.ออกจากระบบ ')
    choice = input("input choice")
def add():
    a=input("\nเพิ่มคำศัพท์ : ")
    s=input("\nชนิดคำ(n.  , v. , adj. , adv  ) : ")
    d=input("\nความหมาย : ")
    dic[a]=s,d
    print("เพิ่มคำศัพท์เรียบร้อย")
def show():
    print("-"*30+"\n\tคำศัพท์ทั้งหมด\n"+"-"*30+"\nคำศัพท์  ประเภท  ความหมาย ")
    for key in dic:
        print("{}{:<5}{}".format(key,"",dic[key]))
def ลบคำศัพท์ออก():
    delist = input("\nกรุณาพิมพ์คำศัพท์ที่ต้องการลบ :")
    ex = input("ต้องการลบ {}ใช่หรือไม่ (y/n):".format(delist))
    if ex == "y":
        del dic[delist]
        print("ลบ"+delist+"เรียบร้อยแล้ว")

while True:
    menu()
    if choice=="1":
        add()
    elif choice=="2":
        show()
    elif choice=="3":
        ลบคำศัพท์ออก()
    elif choice=="4":
        ch = input ("\nคุณต้องการอยู่ในระบบต่อไปหรือไม่ (y/n) :")
        if ch =="y":
            print("ออกจากระบบเรียบร้อยแล้ว")
            break
        elif ch == "n":
            continue
    '''b = input ('------------vocab---------\n 1.เพิ่มคำศัพท์ [a]\n 2.แสดงคำศัพท์ [s]\n 3.ลบข้อความ[p]\n 4..ออกจากระบบ[x]\n')
    b = b.lower()
    if b== "a":
        c = input ("ป้อนคำศัพท์(เพิ่มคำศัพท์:ชนิดคำ:ความหมาย:)")
        a.append(c)
        print("\n*****ข้อมูลได้เข้าสู่ระบบแล้ว*****\n")
    elif b== "s":
        print("{0:*<30}".format(""))
        print("{0:-<5}  {1:-<5}  {2:10}".format("คำศัพท์","ชนิดคำ","ความหมาย"))
        print("{0:*<30}".format(""))
        for d in a : 
            e = d.split(":")
            print("{0[0]:<6} {0[1]:>8} {0[2]:<10}".format (e) )
            continue
    elif b=="p":

        gang = [a]
        print(gang)
            
    elif b== "x":
        break
print ("ทำคำสั่งถัดไป")"""







