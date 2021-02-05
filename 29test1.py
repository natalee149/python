"""import os
choice = 0 
filename = " "

def menu():
    global choice
    print("Menu \n 1.open Calculator\n 2.open Notepad\n 3.Exit ")
    choice = input ("select Menu :")
def opennotepad():
    filename = "c:\\windows\\SysWOW64\\notepad.exe"
    print("Memmorandum writing %s" %filename)
    os.system(filename)
def opencalculator():
    filename = "c:\\windows\\SysWOW64\\calc.exe"
    print("Calculate Number %s" %filename)
    os.system(filename)
while True:
    menu()
    if choice == '1' :
        opencalculator()
    elif choice == '2' :
        opennotepad()
    else:
        break"""
print("***********************************************************************************")
print("                            ร้านของชำ                                               ")
print("***********************************************************************************")
print("")
print("โปรแกรมร้านค้าออนไลน์")
print("1.แสดงรายการสินค้า")
print("2.หยิบสินค้าเข้าตะกร้า")
print("3.แสดงรายการสินค้าและราคาสินค้า")
print("4.หยิบสินค้าออกจากตะกร้า")
print("5.ปิดโปรแกรม")
a = int (input(print("กรุณาเลือกทำรายกาย"))
thislist=["แสดงรายการสินค้า"," หยิบสินค้าใส่ตะกร้า","แสดงรายการสินค้า  "," หยิบสินค้าออกจากตะกร้า","ปิดโปรแกรม "]

def produce():
    print("1.แป้ง ราคา 25 บาท ")
    print("2.นม ราคา 25 บาท ")
    print("3.ไข่ ราคา 25 บาท ")
    print("4.มาม่า ราคา 25 บาท ")
    print("5.ของใช้ ราคา 25 บาท ")

a=int (input("เลือกสินค้า : "))
thislist=["แป้ง","นม","ไข่","มาม่า","ของใช้"]
price = [["30","45","55","60","80" ]]
print("ค่าบริการรถ",thislist[a-1])
print("ลากกระบัง --> บางบ่อ =",price[a-1][0], "บาท")

