from datetime import date
class Person:
    def __init__(self, name ):
         self.name = name
         #self.age = age

    #@classmethod
    #def birth_year(cls, name, year):
        #return cls(name, date.today().year - year)


    @staticmethod
    def is_adult(year_of_birth):
        if 2021 - year_of_birth >= 18:
            print('access is allowed')
        else:
            print('accsess is forbiden')

person1 = Person('Misha')

person1.is_adult(2005)