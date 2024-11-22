import random

class Person:
    def __init__ (self,given_name,given_age,given_gender):
        self.name=given_name
        self.age=given_age
        self.gender=given_gender

    def set_details(self,new_name,new_age,new_gender):
        self.name=new_name
        self.gender=new_gender
        self.age=new_age

    def get_details(self,new_name,new_age,new_gender):
        print("Name"+"[" + new_name + "]" + "Age"+"[" + new_age + "]" +"Gender"+"[" + new_gender + "]")

class Student(Person):
    def __init__ (self,given_name,given_age,given_gender,given_id,given_course,given_grades):
        super().__init__(self,given_name,given_age,given_gender,)
        self.id=given_id
        self.course=given_course
        self.grades=given_grades

    def set_student_details(self,new_student,new_id):
        self.id=new_id
        self.course=new.course

    def add_grades(self, new_grades):
        self.grades=new_grades
    
