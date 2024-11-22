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

    def set_student_details(self,new_course,new_id):
        self.id=new_id
        self.course=new_course

    def add_grades(self, new_grades):
        self.grades=new_grades
    
    def avg_grades(self):
        if len(self.grades)==0:
            return 0
        total=sum(self.grades)
        total=total / len(self.grades)
        print("Average grade is "+total)

    def get_student_summary(self,given_name,given_age,given_gender,given_id,given_course,given_grades,avg_grade):
        return self,given_name,given_age,given_gender,given_id,given_course,given_grades
    
class Prof(Person):
    def __init__ (self,given_name,given_age,given_gender,staff_id,department,salary):
        super().__init__(self,given_name,given_age,given_gender,)
        self.staff_id=staff_id
        self.department=department
        self.salary=salary

    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name} (ID: {student.student_id}) from Professor {self.name}:")
        print(feedback)

    def increase_salary(self, percentage):
        increase_amount = self.salary * (percentage / 100)
        self.salary += increase_amount
        print("Professor" + self.name+"'s" + "salary has been increased by "+ percentage + "%. New salary:" + self.salary + ".")

    def get_professor_summary(self):
        return "Professor" + self.name + "(ID: " + self.staff_id + ") is part of the " + self.department +  "department. " "Salary:" + self.salary + "."

class Administrator(Person):
    def __init__(self,given_name,given_age,given_gender,admin_id,office,years_of_service):
        super().__init__(self,given_name,given_age,given_gender,)
        self.admin_id=admin_id
        self.office=office
        self.years_of_service=years_of_service

    def set_admin_detrails(self,new_admin_id,new_office,new_years_of_service):
        self.admin_id=new_admin_id
        self.office=new_office
        self.years_of_service=new_years_of_service

    def increment_service_years(self,years_of_service):
        years_of_service=years_of_service+1

    def get_admin_summary(self):
        return "Admin: " + self.name + "ID: " + self.admin_id + "has been serving here for " + self.years_of_service + "years."
    
student1 = Student("Inas",16,"male",9091,"Computer science",98878878)
student2 = student("Arben",17,"male",9354,"Law",7777777)
