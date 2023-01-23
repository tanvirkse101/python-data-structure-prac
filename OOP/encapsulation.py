class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self._roll = roll
        self.__age = age

    def show(self):
        print('Details:', self.name, self._roll, self.__age)

    def get_roll(self):
        return self._roll

    def get_age(self):
        return self.__age

    def set_roll(self, no):
        if no > 50:
            print('Roll must be less than 50')
        else:
            self._roll = no

    def set_age(self, age):
        if age > 150:
            print('Set proper age less than 150')
        else:
            self.__age = age


tanvir = Student('Tanvir', 10, 15)
tanvir.show()
tanvir.set_age(175)
tanvir.set_roll(51)
tanvir.set_age(100)
tanvir.set_roll(49)
tanvir.show()
