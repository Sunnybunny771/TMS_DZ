from datetime import date
class Person:
    def __init__(self, name , age):
         self.name = name
         self.age = age

@classmethod
def birth_year(cls, name, year):
    return cls(name, date.today().year - year)


@staticmethod
def is_adult(age):
    return age>18

person1 = Person('Misha', 23)
person2 = Person('Kate',32)

#print(person1.name, person1.age)

#print(person1.birth_year(2005))
Person.is_adult(23)