class Emplyee:
    company = "TCS"
    def setData(self,name,salary):
        self.name=name
        self.salary=salary
s1=Emplyee()
s1.setData("Manjunath",50000)
print(Emplyee.company)
print(s1.name)
print(s1.salary)


s1.Dept= "software Engineering"
print(s1.Dept)
s2= Emplyee()
s2.setData("Deekshith",50000)
print(Emplyee.company)
print(s2.name)
print(s2.salary)
s2.Dept ="softwar Engineering"
print(s2.Dept)
