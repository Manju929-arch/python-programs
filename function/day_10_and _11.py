class student:
    clg = "Government Engineering College Mosalhosahalli"

    def setData(self,name ,age,id):
        self.name = name
        self.age = age
        self.id = id
s1=student()
s1.setData("Manju",18,101)
print(s1.name)
print(s1.age)
print(s1.id)
print(student.clg)
s1.dep="CSE"
s1.clg=" GECM"
s2= student()
s2.setData("Deekshith ",18,101)
print(s2.name)
print(s2.age)
print(s2.id)
print(student.clg)





