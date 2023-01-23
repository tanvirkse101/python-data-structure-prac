# Multiple Inheritance
class Person:
    def person_info(self, name, age):
        print('Inside Person Class')
        print('Name:', name, 'Age:', age)


class Company:
    def company_info(self, company_name, location):
        print('Inside company class')
        print('Name:', company_name, 'Location:', location)


class Employee(Person, Company):
    def employe_info(self, salary, skill):
        print('Inside Emp class')
        print('Salary:', salary, 'Skill:', skill)


emp = Employee()

emp.person_info('T', 28)
emp.company_info('G', 'A')
emp.employe_info(12000, 'ML')
