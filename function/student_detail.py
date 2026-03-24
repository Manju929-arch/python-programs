class Student:
    def __init__(self, name, usn, sem):
        self.name = name
        self.usn = usn
        self.sem = sem
        self.marks = []

    def input_marks(self):
        print("\nEnter marks for 5 subjects (out of 100):")
        for i in range(1, 6):
            mark = int(input(f"Subject {i}: "))
            self.marks.append(mark)

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def result(self):
        if any(mark < 40 for mark in self.marks):
            return "Fail"
        else:
            return "Pass"

    def display(self):
        print("\n------ Student Report ------")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Semester:", self.sem)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Percentage:", round(self.calculate_percentage(), 2), "%")
        print("Grade:", self.calculate_grade())
        print("Result:", self.result())


# Main program
name = input("Enter Student Name: ")
usn = input("Enter USN: ")
sem = input("Enter Semester: ")

student = Student(name, usn, sem)

student.input_marks()
student.display()