import time
name =[]
score =[]
temes =[]
asd =[]
def เวลา():
    timeis = time.localtime()
    a = time.strftime("%d %B %Y ,%H:%M:%S",timeis)
    print(a)
num= int(input("พิมพ์จำนวนผู้ซ้อมยิงปืน  : "))
for i in range (num):
    print("ป้อนข้อมูลคนที่",1+i)
    na = input ("ชื่อผู้ซ้อม :")
    sc = float (input("คะแนน :"))
    t = float (input("ระยะเวลาที่ใช้ : "))
    name.append(na)
    score.append(sc)
    temes.append(t)
    asd.append(sc/t)
for i in range (num):
    j=i 
    for j in range(num):
        if asd[i]>asd[j]:
            a,b,c,d= asd[i],name[i],score[i],temes[i]
            asd[i],name[i],score[i],temes[i] = asd[j],name[j],score[j],temes[j]
            asd[j],name[j],score[j],temes[j]=a,b,c,d
timeis = time.localtime()
a= time.strftime("%A",timeis)
a= time.strftime("%Y",timeis)
print("shotgun"+a+"Training",b,"\nCondtion : 1 ")
เวลา()
print("-"*77)
print('{0:-<6}{1:<-6}{2:<-8}{3:<-17}{4:<-12}{5:<-15}{6}'.format("NO.","PTS","TIME","COMPETITORName","HIT FACTOR","STATE POINTS","STATE PERCENT"))
print("-"*77)
for i in range(num):
    stawe_po = (asd[i]/asd[0])*50
    stawe_pe = (stawe_po/(asd[0]/asd[0]*50))*100
    print('{0:<6}{1:<6}{2:<8}{3:<17}{4:<12}{5:<15}{6}'.format(i+1,int(score[i]),int(temes[i]),name[i],"%.4f"%stawe_po,"%.2f"%stawe_pe))




