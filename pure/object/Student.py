# encoding: utf-8
from pure.object.Person import Person


class Student(Person):
    def __init__(self, school, grade, height, weight, age, cloth):
        super().__init__(height, weight, age, cloth)
        self.school = school
        self.grade = grade

    def set_school(self, school):
        self.school = school

    def set_grade(self, grade):
        self.grade = grade

    def set_cloth(self, cloth):
        self.cloth = cloth


s = Student('187', '87', '87', 'purple', 'NY', 'High')
print(s.school, s.grade)

s.set_school('GS')
s.set_cloth('red')
print(s.school)
