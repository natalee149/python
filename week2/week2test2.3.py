print("***********************************************************************************")
print("                            โปรแกรมหยิบสินค้าใส่ตะกร้า                                  ")
print("***********************************************************************************")
thislist = []
for i in range(5):
    a=input("หยิบสินค้าชิ้นใส่ตะกร้า"+ str(i+1) + ":")
    thislist.append(a)
print("สินค้าที่หยิบใส่ตะกร้ามีดังนี้")
print(" 1:"+thislist[0])
print(" 2:"+thislist[1])
print(" 3:"+thislist[2])
print(" 3:"+thislist[3])
print(" 4:"+thislist[4])
