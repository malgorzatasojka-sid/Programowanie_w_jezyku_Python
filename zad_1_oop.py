class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = Student("Ania", [70, 80, 65])
student2 = Student("Bartek", [30, 40, 45])

print(student1.is_passed())
print(student2.is_passed())
