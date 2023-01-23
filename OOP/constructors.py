# Constructor overloading
# Python takes the last contructor only

"""
class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age


emma = Student('Emma')
kelly = Student('Kelly', 13)
"""


class Vehicle:
    def __init__(self, engine):
        print('Vehicle')
        self.engine = engine


class Car(Vehicle):
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Car')
        self.max_speed = max_speed


class Electric_Car(Car):
    count = 0

    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Electric Car')
        self.km_range = km_range
        Electric_Car.count = Electric_Car.count + 1


ev = Electric_Car('1500cc', 240, 750)
ev1 = Electric_Car('1500cc', 240, 750)
ev2 = Electric_Car('1500cc', 240, 750)
print(ev.engine, ev.max_speed, ev.km_range, Electric_Car.count)
