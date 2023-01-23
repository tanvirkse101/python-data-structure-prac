class Student:
    school_name = "ABC"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        self.age = new_age

    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name


example = Student("Tanvir", 27)

example.show()
example.change_age(28)
Student.modify_school_name('XYZ')
example.show()
