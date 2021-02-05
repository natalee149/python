
class student :
    def __init__(self,name,isd,saka,school,provin,sex):
        self.name = name
        self.isd = isd
        self.saka = saka
        self.school= school
        self.provin=provin
        self.sex=sex
    def showStudent(self):
        print("*"*50)
        print("                        แนะนำตัว                   ")
        print("*"*50)
        sex=self.sex
        sex.lower
        if sex=="men" :
            print("สวัสดีครับ",self.name+"นักศึกษาชั้นปีที่"+self.isd+"สาขา"+self.saka+"โรงเรียน"+self.school+"จังหวัด"+self.provin)
        else :
            print("สวัสดีค่ะ",self.name+"นักศึกษาชั้นปีที่"+self.isd+"สาขา"+self.saka+"โรงเรียน"+self.school+"จังหวัด"+self.provin)
deat = []
nit = input ("ชื่อ-นามสกล,ชั้นปี,สาขา,โรงเรียน,จังหวัด,เพศ(men or female) : ")
split_nit = nit.split(":")
deat.append(nit[0])
deat.append(nit[1])
deat.append(nit[2])
deat.append(nit[3])
deat.append(nit[4])
deat.append(nit[5])
       
x = student(deat[0],deat[1],deat[2],deat[3],deat[4],deat[5])
x.showStudent()




 



