class student :
    def __init__(self,name,year,sex,branch,province,school) :
        self.name = name
        self.year = year
        self.sex = sex
        self.branch = branch
        self.province = province
        self.school = school

    def showStudent(self) :
        print("*"*50)
        print("                        แนะนำตัว                   ")
        print("*"*50)
        sex = self.sex
        if sex == 'ชาย':
            print('สวัสดีครับ ผมชื่อ',self.name+'  นักศึกษาชั้นปีที่ '+self.year+'  สาขา '+self.branch+'  มาจากจังหวัด '+self.province+' โรงเรียนเดิมที่ศึกษา '+self.school)
        else :
            print('สวัสดีค่ะ ฉันชื่อ',self.name+'  นักศึกษาชั้นปีที่ '+self.year+'  สาขา '+self.branch+'  มาจากจังหวัด '+self.province+' โรงเรียนเดิมที่ศึกษา '+self.school)

date = []
stu = input('ชื่อ-นามสกุล,ชั้นปี,เพศ (ชาย/หญิง),สาขาวิชา,จังหวัด,โรงเรียนเดิมที่เคยศึกษา : ')
split_stu = stu.split(',')
date.append(split_stu[0])
date.append(split_stu[1])
date.append(split_stu[2])
date.append(split_stu[3])
date.append(split_stu[4])
date.append(split_stu[5])


x = student(date[0],date[1],date[2],date[3],date[4],date[5])
x.showStudent()