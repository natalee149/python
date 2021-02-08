print("เลือกขนมที่คุณชอบหรือ exit เพื่อออกจากโปรแกรม : ")

i=0
x=1
blist=[]
while (True):
    i+=1 
    b=str(input(" ขนมที่ชอบอันดับที่ "+str(x)+":"))
    blist.append(b)
    x+=1
    if(b=="exit"):
        break    
print("ขนมโปรดของคุณมีดังนี้")
for x in range (1,i):
    print(x,'.',blist[x-1])